#!/usr/bin/env python3
"""Convert Raw PDFs with Marker.

This vault uses its local `.venv-marker` runtime by default.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
RAW_DIR = VAULT / "Raw"
OUT_DIR = VAULT / ".tmp" / "marker-extractions"
LOCAL_MARKER_BIN = VAULT / ".venv-marker" / "bin" / "marker_single"
LOCAL_MARKER_BATCH_BIN = VAULT / ".venv-marker" / "bin" / "marker"
CONVERTER_VERSION = "marker-pdf-1.10.2"


def marker_bin() -> Path:
    env_bin = os.environ.get("MARKER_BIN")
    candidates = [Path(env_bin)] if env_bin else []
    candidates += [LOCAL_MARKER_BIN]
    for candidate in candidates:
        if candidate and candidate.exists():
            return candidate
    raise SystemExit(
        "Marker runtime not found. Install local .venv-marker or set MARKER_BIN. "
        f"Checked: {LOCAL_MARKER_BIN}"
    )


def marker_batch_bin() -> Path:
    env_bin = os.environ.get("MARKER_BATCH_BIN")
    candidates = [Path(env_bin)] if env_bin else []
    candidates += [LOCAL_MARKER_BATCH_BIN]
    for candidate in candidates:
        if candidate and candidate.exists():
            return candidate
    raise SystemExit(
        "Marker batch runtime not found. Install local .venv-marker or set MARKER_BATCH_BIN. "
        f"Checked: {LOCAL_MARKER_BATCH_BIN}"
    )


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def yaml_quote(value: str) -> str:
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def sanitize_component(value: str) -> str:
    value = value.strip().replace("/", "-").replace(":", "-")
    value = value.replace("－", "-").replace("—", "-").replace("–", "-")
    return value or "_"


def output_dir_for(pdf: Path) -> Path:
    relative = pdf.relative_to(RAW_DIR)
    # Preserve the old Raw/pdf/<name>.pdf convention for backwards
    # compatibility with early vault outputs.
    if relative.parent == Path("pdf"):
        return OUT_DIR / sanitize_component(pdf.stem)
    parent_parts = [sanitize_component(part) for part in relative.parent.parts]
    return OUT_DIR.joinpath(*parent_parts, sanitize_component(pdf.stem))


def batch_output_parent_for(raw_parent: Path) -> Path:
    relative = raw_parent.relative_to(RAW_DIR)
    if relative == Path("pdf"):
        return OUT_DIR
    parent_parts = [sanitize_component(part) for part in relative.parts]
    return OUT_DIR.joinpath(*parent_parts)


def read_existing_hash(md: Path) -> str | None:
    if not md.exists():
        return None
    head = md.read_text(encoding="utf-8", errors="ignore")[:3000]
    for line in head.splitlines():
        if line.startswith("source_sha256:"):
            return line.split(":", 1)[1].strip()
    return None


def add_frontmatter(md: Path, pdf: Path, started: str) -> None:
    text = md.read_text(encoding="utf-8", errors="ignore")
    if text.startswith("---\n") and "converter: marker" in text[:1000]:
        return
    title = pdf.stem
    image_count = text.count("![")
    meta_path = md.with_name(f"{title}_meta.json")
    page_count = ""
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            page_count = meta.get("page_count") or meta.get("pages") or ""
        except Exception:
            page_count = ""
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    fm = f"""---
type: source-pdf-marker
title: {yaml_quote(title)}
converter: marker
converter_version: {CONVERTER_VERSION}
raw_pdf: [[{rel(pdf)}]]
raw_path: {yaml_quote(rel(pdf))}
source_sha256: {sha256(pdf)}
page_count: {page_count}
markdown_chars: {len(text)}
markdown_image_count: {image_count}
status: marker-ingested
started: {started}
updated: {now}
---

# {title} — Marker conversion

> Raw PDF: [[{rel(pdf)}]]  
> Converter: Marker / marker-pdf 1.10.2  
> Images extracted: {image_count}

"""
    md.write_text(fm + text, encoding="utf-8")


def convert_one(pdf: Path, force: bool) -> tuple[str, Path, int, int]:
    title = pdf.stem
    out_folder = output_dir_for(pdf)
    md = out_folder / f"{title}.md"
    source_hash = sha256(pdf)
    if not force and read_existing_hash(md) == source_hash:
        text = md.read_text(encoding="utf-8", errors="ignore")
        return "skipped", md, len(text), text.count("![")

    if out_folder.exists():
        shutil.rmtree(out_folder)
    out_folder.parent.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env.setdefault("TORCH_DEVICE", "cpu")
    env.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")
    started = datetime.now().astimezone().isoformat(timespec="seconds")
    cmd = [
        str(marker_bin()),
        str(pdf),
        "--output_dir", str(out_folder.parent),
        "--output_format", "markdown",
        "--disable_multiprocessing",
        "--config_json", str(VAULT / "Tools" / "marker_no_ocr_config.json"),
    ]
    subprocess.run(cmd, cwd=VAULT, env=env, check=True)
    if not md.exists():
        raise RuntimeError(f"Marker finished but markdown not found: {md}")
    add_frontmatter(md, pdf, started)
    text = md.read_text(encoding="utf-8", errors="ignore")
    return "converted", md, len(text), text.count("![")


def temp_batch_dir(raw_parent: Path) -> Path:
    digest = hashlib.sha1(rel(raw_parent).encode("utf-8")).hexdigest()[:12]
    return VAULT / ".tmp" / "marker-batches" / digest


def convert_group_batch(pdfs: list[Path], force: bool, workers: int) -> list[tuple[str, Path, int, int]]:
    rows: list[tuple[str, Path, int, int]] = []
    pending: list[Path] = []
    for pdf in pdfs:
        title = pdf.stem
        md = output_dir_for(pdf) / f"{title}.md"
        if not force and read_existing_hash(md) == sha256(pdf):
            text = md.read_text(encoding="utf-8", errors="ignore")
            rows.append(("skipped", md, len(text), text.count("![")))
        else:
            pending.append(pdf)

    if not pending:
        return rows

    raw_parent = pending[0].parent
    out_parent = batch_output_parent_for(raw_parent)
    out_parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = temp_batch_dir(raw_parent)
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True, exist_ok=True)

    for pdf in pending:
        out_folder = output_dir_for(pdf)
        if out_folder.exists():
            shutil.rmtree(out_folder)
        link = tmp_dir / pdf.name
        try:
            link.symlink_to(pdf)
        except OSError:
            shutil.copy2(pdf, link)

    env = os.environ.copy()
    env.setdefault("TORCH_DEVICE", "cpu")
    env.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")
    started = datetime.now().astimezone().isoformat(timespec="seconds")
    cmd = [
        str(marker_batch_bin()),
        str(tmp_dir),
        "--output_dir", str(out_parent),
        "--output_format", "markdown",
        "--config_json", str(VAULT / "Tools" / "marker_no_ocr_config.json"),
        "--workers", str(workers),
        "--max_tasks_per_worker", str(max(1, len(pending))),
    ]
    subprocess.run(cmd, cwd=VAULT, env=env, check=True)

    for pdf in pending:
        title = pdf.stem
        md = output_dir_for(pdf) / f"{title}.md"
        if not md.exists():
            raise RuntimeError(f"Marker batch finished but markdown not found: {md}")
        add_frontmatter(md, pdf, started)
        text = md.read_text(encoding="utf-8", errors="ignore")
        rows.append(("converted", md, len(text), text.count("![")))

    shutil.rmtree(tmp_dir, ignore_errors=True)
    return rows


def write_index(rows: list[tuple[str, Path, int, int]]) -> None:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    if not rows:
        body = "当前还没有已转换的 PDF。"
    else:
        body = "\n".join(
            f"- {status}: [[{md.relative_to(VAULT).with_suffix('').as_posix()}|{md.stem}]] — chars: `{chars}`, images: `{imgs}`"
            for status, md, chars, imgs in rows
        )
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "index.md").write_text(f"""---
type: temporary-marker-index
title: Temporary Marker PDF Extractions
converter: marker
status: maintained
updated: {now}
---

# Temporary Marker PDF Extractions

{body}
""", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--only")
    parser.add_argument("--mode", choices=["batch", "single"], default="batch")
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()

    pdfs = sorted(RAW_DIR.rglob("*.pdf"))
    if args.only:
        needle = args.only.lower()
        pdfs = [p for p in pdfs if needle in rel(p).lower()]

    rows = []
    if args.mode == "single":
        for pdf in pdfs:
            print(f"==> marker converting {pdf.name}", flush=True)
            status, md, chars, imgs = convert_one(pdf, args.force)
            rows.append((status, md, chars, imgs))
            print(f"{status}\t{rel(md)}\tchars={chars}\timages={imgs}", flush=True)
    else:
        groups: dict[Path, list[Path]] = {}
        for pdf in pdfs:
            groups.setdefault(pdf.parent, []).append(pdf)
        for raw_parent, group in sorted(groups.items()):
            print(f"==> marker batch {rel(raw_parent)} pdfs={len(group)}", flush=True)
            group_rows = convert_group_batch(sorted(group), args.force, args.workers)
            rows.extend(group_rows)
            for status, md, chars, imgs in group_rows:
                print(f"{status}\t{rel(md)}\tchars={chars}\timages={imgs}", flush=True)

    write_index(rows)
    print(f"Done. Temporary Marker index: {rel(OUT_DIR / 'index.md')}")


if __name__ == "__main__":
    main()
