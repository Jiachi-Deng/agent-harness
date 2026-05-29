#!/usr/bin/env python3
"""Run local Ollama vision inference for PDF/video visual pages."""

from __future__ import annotations

import argparse
import base64
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps


VAULT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MODEL = "qwen3-vl:8b-instruct"
DEFAULT_URL = "http://localhost:11434/api/chat"
DEFAULT_SYSTEM_PROMPT = (
    "你是文档视觉 OCR 和结构复核器。只能依据图片和用户提供的 OCR 参考回答；"
    "看不清写[不确定]；不要根据常识、课程经验或上下文补全。"
)


def preprocess_image(
    image_path: Path,
    work_dir: Path,
    *,
    resize_width: int | None,
    max_edge: int | None,
    center_square: int | None,
) -> tuple[Path, dict[str, Any]]:
    image = ImageOps.exif_transpose(Image.open(image_path)).convert("RGB")
    original_size = image.size

    if max_edge:
        width, height = image.size
        edge = max(width, height)
        if edge > max_edge:
            scale = max_edge / edge
            image = image.resize(
                (max(1, round(width * scale)), max(1, round(height * scale))),
                Image.Resampling.LANCZOS,
            )

    if resize_width:
        width, height = image.size
        new_height = max(1, round(height * resize_width / width))
        image = image.resize((resize_width, new_height), Image.Resampling.LANCZOS)

    if center_square:
        width, height = image.size
        size = min(center_square, width, height)
        left = max(0, (width - size) // 2)
        top = max(0, (height - size) // 2)
        image = image.crop((left, top, left + size, top + size))
        if size != center_square:
            image = image.resize((center_square, center_square), Image.Resampling.LANCZOS)

    if not (resize_width or max_edge or center_square):
        return image_path, {
            "source_image": str(image_path),
            "prepared_image": str(image_path),
            "original_size": original_size,
            "prepared_size": image.size,
        }

    work_dir.mkdir(parents=True, exist_ok=True)
    out = work_dir / f"{image_path.stem}.ollama-prepared.jpg"
    image.save(out, quality=92)
    return out, {
        "source_image": str(image_path),
        "prepared_image": str(out),
        "original_size": original_size,
        "prepared_size": image.size,
        "resize_width": resize_width,
        "max_edge": max_edge,
        "center_square": center_square,
    }


def read_image_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def request_ollama(
    *,
    url: str,
    model: str,
    image: Path,
    prompt: str,
    max_tokens: int,
    temperature: float,
    timeout: int,
    response_format: str | None,
    retries: int,
    retry_sleep: float,
    num_ctx: int | None,
    seed: int | None,
    keep_alive: str | None,
    system_prompt: str | None,
) -> dict[str, Any]:
    options: dict[str, Any] = {
        "temperature": temperature,
        "num_predict": max_tokens,
    }
    if num_ctx:
        options["num_ctx"] = num_ctx
    if seed is not None:
        options["seed"] = seed

    messages: list[dict[str, Any]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append(
        {
            "role": "user",
            "content": prompt,
            "images": [read_image_base64(image)],
        }
    )

    payload: dict[str, Any] = {
        "model": model,
        "stream": False,
        "messages": messages,
        "options": options,
    }
    if response_format:
        payload["format"] = response_format
    if keep_alive:
        payload["keep_alive"] = keep_alive

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(retry_sleep * (attempt + 1))
    raise RuntimeError(f"ollama request failed after {retries + 1} attempt(s): {last_error}") from last_error


def extract_answer(data: dict[str, Any], *, fallback_thinking: bool) -> str:
    message = data.get("message") or {}
    content = message.get("content") or ""
    if content:
        return content.strip()

    thinking = message.get("thinking") or ""
    if fallback_thinking and thinking:
        return thinking.strip()
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Image path to analyze")
    parser.add_argument("--prompt", help="Prompt for the vision model")
    parser.add_argument("--prompt-file", type=Path, help="Read prompt from a UTF-8 text file")
    parser.add_argument("--system-prompt", default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Ollama model name")
    parser.add_argument("--url", default=DEFAULT_URL, help="Ollama chat API URL")
    parser.add_argument("--max-tokens", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--retry-sleep", type=float, default=2.0)
    parser.add_argument("--num-ctx", type=int, default=8192)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--keep-alive", default="10m")
    parser.add_argument("--resize-width", type=int, default=None)
    parser.add_argument("--max-edge", type=int, default=None)
    parser.add_argument("--center-square", type=int, default=None)
    parser.add_argument("--format", choices=["json"], default=None, help="Ask Ollama for a structured response")
    parser.add_argument("--fallback-thinking", action="store_true", help="Use thinking text if content is empty")
    parser.add_argument("--allow-empty", action="store_true", help="Exit 0 even if the model returns empty content")
    parser.add_argument("--min-chars", type=int, default=0, help="Warn if extracted content is shorter than this")
    parser.add_argument("--work-dir", type=Path, default=VAULT_ROOT / ".tmp" / "ollama-vl")
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--raw-output", type=Path, default=None)
    parser.add_argument("--metadata-output", type=Path, default=None)
    args = parser.parse_args()

    image = args.image.expanduser().resolve()
    if not image.exists():
        raise SystemExit(f"image not found: {image}")
    if not args.prompt and not args.prompt_file:
        raise SystemExit("either --prompt or --prompt-file is required")
    prompt = args.prompt_file.expanduser().read_text(encoding="utf-8") if args.prompt_file else args.prompt

    prepared, prep_meta = preprocess_image(
        image,
        args.work_dir,
        resize_width=args.resize_width,
        max_edge=args.max_edge,
        center_square=args.center_square,
    )

    started = time.time()
    data = request_ollama(
        url=args.url,
        model=args.model,
        image=prepared,
        prompt=prompt,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        timeout=args.timeout,
        response_format=args.format,
        retries=args.retries,
        retry_sleep=args.retry_sleep,
        num_ctx=args.num_ctx,
        seed=args.seed,
        keep_alive=args.keep_alive,
        system_prompt=args.system_prompt,
    )
    answer = extract_answer(data, fallback_thinking=args.fallback_thinking)
    elapsed = time.time() - started
    data["_codex_meta"] = {
        **prep_meta,
        "elapsed_seconds": round(elapsed, 3),
        "prompt_chars": len(prompt or ""),
        "answer_chars": len(answer),
    }

    if not answer and not args.allow_empty:
        if args.raw_output:
            args.raw_output.parent.mkdir(parents=True, exist_ok=True)
            args.raw_output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        raise SystemExit("empty answer from ollama")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(answer + "\n", encoding="utf-8")
    else:
        print(answer)

    if args.raw_output:
        args.raw_output.parent.mkdir(parents=True, exist_ok=True)
        args.raw_output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.metadata_output:
        args.metadata_output.parent.mkdir(parents=True, exist_ok=True)
        args.metadata_output.write_text(json.dumps(data["_codex_meta"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if prepared != image:
        print(f"[prepared_image] {prepared}", file=sys.stderr)

    message = data.get("message") or {}
    if not answer and message.get("thinking"):
        print("[warning] empty content; model returned thinking text only", file=sys.stderr)
    if args.min_chars and len(answer) < args.min_chars:
        print(f"[warning] short answer: chars={len(answer)} min_chars={args.min_chars}", file=sys.stderr)
    if data.get("done_reason") == "length":
        print("[warning] generation reached max-tokens; output may be truncated", file=sys.stderr)
    print(
        f"[ollama] model={args.model} elapsed={elapsed:.1f}s "
        f"done={data.get('done_reason')} eval_count={data.get('eval_count')}",
        file=sys.stderr,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
