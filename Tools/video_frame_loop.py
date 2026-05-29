#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

import numpy as np


SHOWINFO_RE = re.compile(r"pts_time:([0-9.]+)")
SRT_TIME_RE = re.compile(
    r"(?P<h1>\d{2}):(?P<m1>\d{2}):(?P<s1>\d{2}),(?P<ms1>\d{3})\s+-->\s+"
    r"(?P<h2>\d{2}):(?P<m2>\d{2}):(?P<s2>\d{2}),(?P<ms2>\d{3})"
)


@dataclass
class Candidate:
    path: Path
    time: float
    gray: np.ndarray
    avg_hash: np.ndarray


@dataclass
class Representative:
    candidate: Candidate
    hamming_from_previous: int | None
    ssim_from_previous: float | None
    change_ratio_from_previous: float | None


@dataclass
class Subtitle:
    start: float
    end: float
    text: str


def run(cmd: list[str], *, stdout=None, stderr=None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(cmd, check=True, stdout=stdout, stderr=stderr)


def seconds_to_srt_time(value: float) -> str:
    value = max(0, value)
    hours = int(value // 3600)
    minutes = int((value % 3600) // 60)
    seconds = int(value % 60)
    millis = int(round((value - math.floor(value)) * 1000))
    if millis == 1000:
        seconds += 1
        millis = 0
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def seconds_to_label(value: float) -> str:
    value = max(0, value)
    hours = int(value // 3600)
    minutes = int((value % 3600) // 60)
    seconds = int(value % 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def parse_srt_time(match: re.Match[str], prefix: str) -> float:
    return (
        int(match.group(f"h{prefix}")) * 3600
        + int(match.group(f"m{prefix}")) * 60
        + int(match.group(f"s{prefix}"))
        + int(match.group(f"ms{prefix}")) / 1000
    )


def parse_srt(path: Path) -> list[Subtitle]:
    entries: list[Subtitle] = []
    chunks = path.read_text(encoding="utf-8-sig").split("\n\n")
    for chunk in chunks:
        lines = [line.strip() for line in chunk.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        time_line_index = 1 if "-->" in lines[1] else 0
        match = SRT_TIME_RE.search(lines[time_line_index])
        if not match:
            continue
        text = "\n".join(lines[time_line_index + 1 :]).strip()
        if text:
            entries.append(Subtitle(parse_srt_time(match, "1"), parse_srt_time(match, "2"), text))
    return entries


def extract_scene_candidates(video: Path, output_dir: Path, threshold: float, ffmpeg: str, overwrite: bool) -> list[tuple[Path, float]]:
    candidates_dir = output_dir / "candidates"
    log_path = output_dir / "scene_extract.log"
    candidates_dir.mkdir(parents=True, exist_ok=True)
    if overwrite:
        for old in candidates_dir.glob("frame_*.jpg"):
            old.unlink()

    first_frame = candidates_dir / "frame_000000.jpg"
    if overwrite or not first_frame.exists():
        run(
            [
                ffmpeg,
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-ss",
                "0",
                "-i",
                str(video),
                "-frames:v",
                "1",
                "-q:v",
                "2",
                str(first_frame),
            ]
        )

    if overwrite or not any(candidates_dir.glob("frame_scene_*.jpg")):
        cmd = [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(video),
            "-vf",
            f"select='gt(scene,{threshold})',showinfo",
            "-vsync",
            "vfr",
            "-q:v",
            "2",
            str(candidates_dir / "frame_scene_%06d.jpg"),
        ]
        with log_path.open("wb") as log_file:
            run(cmd, stdout=subprocess.DEVNULL, stderr=log_file)

    times = [0.0]
    if log_path.exists():
        for line in log_path.read_text(errors="ignore").splitlines():
            match = SHOWINFO_RE.search(line)
            if match:
                times.append(float(match.group(1)))

    scene_frames = sorted(candidates_dir.glob("frame_scene_*.jpg"))
    if len(times) - 1 != len(scene_frames):
        times = [0.0] + [float(i) for i in range(1, len(scene_frames) + 1)]

    frames = [(first_frame, 0.0)] + list(zip(scene_frames, times[1:]))
    deduped: list[tuple[Path, float]] = []
    seen_times: set[float] = set()
    for path, time in frames:
        rounded = round(time, 3)
        if rounded not in seen_times and path.exists():
            deduped.append((path, time))
            seen_times.add(rounded)
    return sorted(deduped, key=lambda item: item[1])


def image_to_gray(path: Path, ffmpeg: str, width: int = 160, height: int = 90) -> np.ndarray:
    cp = subprocess.run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(path),
            "-vf",
            f"scale={width}:{height},format=gray",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "gray",
            "-",
        ],
        check=True,
        stdout=subprocess.PIPE,
    )
    return np.frombuffer(cp.stdout, dtype=np.uint8).reshape((height, width)).astype(np.float32)


def avg_hash(gray: np.ndarray, size: int = 8) -> np.ndarray:
    h, w = gray.shape
    usable_h = (h // size) * size
    usable_w = (w // size) * size
    cropped = gray[:usable_h, :usable_w]
    small = cropped.reshape(size, usable_h // size, size, usable_w // size).mean(axis=(1, 3))
    return small > small.mean()


def hamming(a: np.ndarray, b: np.ndarray) -> int:
    return int(np.count_nonzero(a != b))


def ssim(a: np.ndarray, b: np.ndarray) -> float:
    x = a.astype(np.float64)
    y = b.astype(np.float64)
    c1 = 6.5025
    c2 = 58.5225
    mux = x.mean()
    muy = y.mean()
    vx = x.var()
    vy = y.var()
    cov = ((x - mux) * (y - muy)).mean()
    return float(((2 * mux * muy + c1) * (2 * cov + c2)) / ((mux * mux + muy * muy + c1) * (vx + vy + c2)))


def change_ratio(a: np.ndarray, b: np.ndarray, threshold: float = 35.0) -> float:
    return float(np.mean(np.abs(a - b) > threshold))


def cluster_candidates(candidates: list[tuple[Path, float]], ffmpeg: str) -> list[Representative]:
    loaded: list[Candidate] = []
    for path, time in candidates:
        gray = image_to_gray(path, ffmpeg)
        loaded.append(Candidate(path=path, time=time, gray=gray, avg_hash=avg_hash(gray)))

    reps: list[Representative] = []
    last: Candidate | None = None
    for candidate in loaded:
        if last is None:
            reps.append(Representative(candidate, None, None, None))
            last = candidate
            continue

        ham = hamming(last.avg_hash, candidate.avg_hash)
        sim = ssim(last.gray, candidate.gray)
        ratio = change_ratio(last.gray, candidate.gray)
        is_new_page = ratio >= 0.16 or sim <= 0.82 or (ham >= 14 and ratio >= 0.08)
        if is_new_page:
            reps.append(Representative(candidate, ham, sim, ratio))
            last = candidate
    return reps


def copy_representatives(reps: list[Representative], output_dir: Path) -> list[Path]:
    frames_dir = output_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for index, rep in enumerate(reps, start=1):
        dest = frames_dir / f"{index:04d}_{int(rep.candidate.time * 1000):010d}.jpg"
        shutil.copy2(rep.candidate.path, dest)
        paths.append(dest)
    return paths


def run_ocr(paths: list[Path], swift_script: Path) -> dict[str, dict]:
    if not paths:
        return {}
    cp = subprocess.run(
        ["swift", str(swift_script), *map(str, paths)],
        text=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    results: dict[str, dict] = {}
    for line in cp.stdout.splitlines():
        if not line.strip():
            continue
        data = json.loads(line)
        results[str(Path(data["path"]).resolve())] = data
    return results


def classify_frame(ocr: dict) -> tuple[str, str]:
    text = ocr.get("text", "") or ""
    confidence = float(ocr.get("mean_confidence", 0) or 0)
    block_count = len(ocr.get("blocks", []) or [])
    compact_len = len(re.sub(r"\s+", "", text))
    if compact_len < 15:
        return "低文字或视觉题页", "需要视觉 LLM 或讲义/PDF 对齐"
    if compact_len >= 120 or block_count >= 12:
        return "文字密集/表格页", "OCR 已召回主要文字，但需要 LLM 修层级"
    if confidence >= 0.55 and compact_len >= 30 and block_count >= 3:
        return "普通文字 PPT", "OCR 可作为草稿使用"
    if confidence >= 0.45 and compact_len >= 30:
        return "文字/结构混合页", "OCR 部分可用，建议视觉 LLM 复核"
    return "低置信度画面", "需要视觉 LLM 复核"


def subtitles_between(subtitles: list[Subtitle], start: float, end: float) -> str:
    lines: list[str] = []
    for item in subtitles:
        mid = (item.start + item.end) / 2
        if start <= mid < end:
            lines.append(item.text)
    return "\n".join(lines).strip()


def write_markdown(
    output_dir: Path,
    title: str,
    reps: list[Representative],
    frame_paths: list[Path],
    ocr_results: dict[str, dict],
    subtitles: list[Subtitle],
) -> Path:
    md_path = output_dir / "lecture.md"
    lines: list[str] = [
        f"# {title}",
        "",
        "> 自动生成：画面变化抽帧 -> 相似度聚类 -> macOS Vision OCR -> 字幕按时间段归并。",
        "",
    ]
    for index, (rep, frame_path) in enumerate(zip(reps, frame_paths), start=1):
        start = rep.candidate.time
        end = reps[index].candidate.time if index < len(reps) else float("inf")
        ocr = ocr_results.get(str(frame_path.resolve()), {})
        frame_type, status = classify_frame(ocr)
        confidence = float(ocr.get("mean_confidence", 0) or 0)
        ocr_text = (ocr.get("text", "") or "").strip()
        subtitle_text = subtitles_between(subtitles, start, end)

        end_label = seconds_to_label(end) if math.isfinite(end) else "视频结束"
        lines.extend(
            [
                f"## {index:03d}. {seconds_to_label(start)} - {end_label}",
                "",
                f"![frame]({frame_path.relative_to(output_dir).as_posix()})",
                "",
                "### 画面判断",
                f"- 类型：{frame_type}",
                f"- OCR 置信度：{confidence:.2f}",
                f"- 处理状态：{status}",
            ]
        )
        if rep.hamming_from_previous is not None:
            lines.extend(
                [
                    f"- 与上一保留帧 hash 距离：{rep.hamming_from_previous}",
                    f"- 与上一保留帧 SSIM：{rep.ssim_from_previous:.3f}",
                    f"- 与上一保留帧变化面积：{rep.change_ratio_from_previous:.3f}",
                ]
            )
        lines.extend(["", "### OCR", ""])
        lines.append(ocr_text if ocr_text else "（未识别到可靠文字）")
        lines.extend(["", "### 对应讲解", ""])
        lines.append(subtitle_text if subtitle_text else "（此时间段没有匹配到字幕）")
        lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return md_path


def write_manifest(
    output_dir: Path,
    video: Path,
    srt: Path,
    candidates: list[tuple[Path, float]],
    reps: list[Representative],
    frame_paths: list[Path],
    ocr_results: dict[str, dict],
    threshold: float,
) -> Path:
    manifest = {
        "video": str(video),
        "srt": str(srt),
        "scene_threshold": threshold,
        "candidate_count": len(candidates),
        "representative_count": len(reps),
        "frames": [],
    }
    for rep, path in zip(reps, frame_paths):
        ocr = ocr_results.get(str(path.resolve()), {})
        frame_type, status = classify_frame(ocr)
        manifest["frames"].append(
            {
                "time": rep.candidate.time,
                "time_label": seconds_to_srt_time(rep.candidate.time),
                "source_candidate": str(rep.candidate.path),
                "frame": str(path),
                "ocr_confidence": ocr.get("mean_confidence", 0),
                "ocr_text_length": len(re.sub(r"\s+", "", ocr.get("text", "") or "")),
                "frame_type": frame_type,
                "status": status,
                "hamming_from_previous": rep.hamming_from_previous,
                "ssim_from_previous": rep.ssim_from_previous,
                "change_ratio_from_previous": rep.change_ratio_from_previous,
            }
        )
    path = output_dir / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract PPT-like keyframes from a course video and merge OCR with SRT into Markdown.")
    parser.add_argument("--video", required=True, type=Path)
    parser.add_argument("--srt", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--title", default=None)
    parser.add_argument("--scene-threshold", type=float, default=0.20)
    parser.add_argument("--ffmpeg", default="ffmpeg")
    parser.add_argument("--swift-ocr", type=Path, default=Path("Tools/vision_ocr.swift"))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    candidates = extract_scene_candidates(args.video, args.output_dir, args.scene_threshold, args.ffmpeg, args.overwrite)
    reps = cluster_candidates(candidates, args.ffmpeg)
    frame_paths = copy_representatives(reps, args.output_dir)
    ocr_results = run_ocr(frame_paths, args.swift_ocr)
    subtitles = parse_srt(args.srt)
    title = args.title or args.video.stem
    md_path = write_markdown(args.output_dir, title, reps, frame_paths, ocr_results, subtitles)
    manifest_path = write_manifest(args.output_dir, args.video, args.srt, candidates, reps, frame_paths, ocr_results, args.scene_threshold)
    print(json.dumps({"lecture": str(md_path), "manifest": str(manifest_path), "candidates": len(candidates), "frames": len(reps)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
