#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

try:
    from tqdm import tqdm
except Exception:  # pragma: no cover - tqdm is optional at runtime
    tqdm = None


SRT_TIME_EPSILON_MS = 120
MODELSCOPE_ALIAS_CACHE_PATHS = {
    "paraformer-zh": "iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    "fsmn-vad": "iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
    "ct-punc": "iic/punc_ct-transformer_cn-en-common-vocab471067-large",
    "ct-punc-c": "iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Use ffmpeg + FunASR to transcribe long Chinese videos into SRT subtitles."
    )
    parser.add_argument("input", help="Input video or audio file path.")
    parser.add_argument("-o", "--output-dir", default="outputs", help="Output directory.")
    parser.add_argument("--output-srt", default=None, help="Final SRT path. Default: <output-dir>/<input-stem>.srt")
    parser.add_argument("--segment-minutes", type=float, default=25.0, help="ffmpeg segment length in minutes.")
    parser.add_argument("--keep-segments", action="store_true", help="Keep extracted 16 kHz WAV segments.")
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting the final SRT/TXT files.")

    parser.add_argument("--model", default="paraformer-zh", help='ASR model name, e.g. "paraformer-zh" or "iic/SenseVoiceSmall".')
    parser.add_argument("--vad-model", default="fsmn-vad", help='VAD model name. Use "" to disable.')
    parser.add_argument("--punc-model", default="ct-punc", help='Punctuation model name. Use "" or --no-punc to disable.')
    parser.add_argument("--no-punc", action="store_true", help="Disable punctuation model.")
    parser.add_argument("--hub", default="ms", choices=["ms", "hf"], help="Model hub: ms=ModelScope, hf=Hugging Face.")
    parser.add_argument("--device", default="mps", help='Inference device: "mps", "cpu", "cuda:0", or "auto".')
    parser.add_argument("--allow-cpu-fallback", action="store_true", help="Fallback to CPU if MPS is unavailable.")

    parser.add_argument("--vad-max-ms", type=int, default=30000, help="Max single VAD segment length in milliseconds.")
    parser.add_argument("--batch-size-s", type=float, default=None, help="FunASR dynamic batch size in seconds.")
    parser.add_argument("--sentence-timestamp", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--language", default="zh", help="SenseVoice language option: zh, yue, en, ja, ko, auto.")
    parser.add_argument("--merge-vad", action=argparse.BooleanOptionalAction, default=True, help="SenseVoice VAD merge option.")
    parser.add_argument("--merge-length-s", type=float, default=15.0, help="SenseVoice merged VAD length.")
    parser.add_argument("--hotword", default=None, help="Optional Paraformer hotword string.")

    parser.add_argument("--max-subtitle-chars", type=int, default=42, help="Split very long captions above this character count.")
    parser.add_argument("--continue-on-error", action="store_true", help="Skip failed segments and continue.")
    parser.add_argument("--ffmpeg", default="ffmpeg", help="ffmpeg executable path.")
    parser.add_argument("--ffprobe", default="ffprobe", help="ffprobe executable path.")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    return parser.parse_args()


def configure_logging(output_dir: Path, level: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    log_path = output_dir / "long_video_funasr.log"
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_path, encoding="utf-8"),
        ],
    )
    return log_path


def run_command(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    logging.debug("Running command: %s", " ".join(cmd))
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def ensure_executable(name: str) -> None:
    if shutil.which(name) is None and not Path(name).exists():
        raise RuntimeError(f"Cannot find executable: {name}")


def probe_duration_seconds(path: Path, ffprobe: str) -> float:
    cp = run_command(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ]
    )
    data = json.loads(cp.stdout)
    return float(data["format"]["duration"])


def split_to_wav_segments(input_path: Path, segments_dir: Path, segment_seconds: float, ffmpeg: str) -> list[Path]:
    segments_dir.mkdir(parents=True, exist_ok=True)
    pattern = segments_dir / "part_%05d.wav"
    cmd = [
        ffmpeg,
        "-hide_banner",
        "-y",
        "-i",
        str(input_path),
        "-map",
        "0:a:0",
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        "-f",
        "segment",
        "-segment_time",
        f"{segment_seconds:.3f}",
        "-reset_timestamps",
        "1",
        "-c:a",
        "pcm_s16le",
        str(pattern),
    ]
    try:
        run_command(cmd)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"ffmpeg failed:\n{exc.stderr}") from exc

    segments = sorted(segments_dir.glob("part_*.wav"))
    if not segments:
        raise RuntimeError("ffmpeg produced no audio segments. Check whether the input has an audio track.")
    return segments


def resolve_device(device: str, allow_cpu_fallback: bool) -> str:
    if device != "auto" and device != "mps":
        return device

    os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

    try:
        import torch
    except Exception as exc:
        if allow_cpu_fallback or device == "auto":
            logging.warning("PyTorch import failed, falling back to CPU: %s", exc)
            return "cpu"
        raise RuntimeError("PyTorch is not importable, so device='mps' cannot be verified.") from exc

    if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return "mps"

    if device == "auto" or allow_cpu_fallback:
        logging.warning("MPS is unavailable. Falling back to CPU.")
        return "cpu"

    raise RuntimeError("MPS is unavailable. Use --device cpu or add --allow-cpu-fallback.")


def is_sensevoice_model(model_name: str) -> bool:
    return "sensevoice" in model_name.lower()


def modelscope_cache_root() -> Path:
    return Path.home() / ".cache" / "modelscope" / "hub" / "models"


def resolve_cached_model_name(model_name: str) -> str:
    if not model_name:
        return model_name
    if Path(model_name).expanduser().exists():
        return str(Path(model_name).expanduser().resolve())
    repo_path = MODELSCOPE_ALIAS_CACHE_PATHS.get(model_name)
    if not repo_path:
        return model_name
    cache_path = modelscope_cache_root() / repo_path
    if (cache_path / "configuration.json").exists() and (cache_path / "config.yaml").exists() and (cache_path / "model.pt").exists():
        logging.info("Using cached local model for %s: %s", model_name, cache_path)
        return str(cache_path)
    return model_name


def build_model(args: argparse.Namespace, device: str) -> Any:
    from funasr import AutoModel

    kwargs: dict[str, Any] = {
        "model": resolve_cached_model_name(args.model),
        "device": device,
        "hub": args.hub,
        "disable_update": True,
    }
    if args.vad_model:
        kwargs["vad_model"] = resolve_cached_model_name(args.vad_model)
        kwargs["vad_kwargs"] = {"max_single_segment_time": args.vad_max_ms}
    if args.punc_model and not args.no_punc:
        kwargs["punc_model"] = resolve_cached_model_name(args.punc_model)
    if is_sensevoice_model(args.model):
        kwargs["trust_remote_code"] = True

    logging.info("Loading FunASR model with args: %s", {k: v for k, v in kwargs.items() if k != "cache"})
    return AutoModel(**kwargs)


def generate_for_segment(model: Any, audio_path: Path, args: argparse.Namespace) -> Any:
    batch_size_s = args.batch_size_s
    if batch_size_s is None:
        batch_size_s = 60 if is_sensevoice_model(args.model) else 300

    kwargs: dict[str, Any] = {
        "input": str(audio_path),
        "cache": {},
        "batch_size_s": batch_size_s,
    }
    if args.sentence_timestamp:
        if args.no_punc or not args.punc_model:
            logging.warning("Disabling sentence_timestamp because FunASR 1.3.1 fails with VAD + sentence_timestamp + no punc_model.")
        else:
            kwargs["sentence_timestamp"] = True
    if args.hotword and not is_sensevoice_model(args.model):
        kwargs["hotword"] = args.hotword
    if is_sensevoice_model(args.model):
        kwargs.update(
            {
                "language": args.language,
                "use_itn": True,
                "merge_vad": args.merge_vad,
                "merge_length_s": args.merge_length_s,
            }
        )
    return model.generate(**kwargs)


def clean_text(text: str, sensevoice: bool = False) -> str:
    text = text or ""
    if sensevoice:
        try:
            from funasr.utils.postprocess_utils import rich_transcription_postprocess

            text = rich_transcription_postprocess(text)
        except Exception:
            pass
    text = re.sub(r"<\|[^|]+?\|>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", text)
    return text


def result_entries(result: Any) -> list[dict[str, Any]]:
    if isinstance(result, dict):
        return [result]
    if isinstance(result, list):
        return [x for x in result if isinstance(x, dict)]
    return []


def value_to_ms(value: Any, duration_s: float) -> int | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if isinstance(value, float) and number <= duration_s + 10:
        return int(round(number * 1000))
    return int(round(number))


def split_text_units(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    raw_parts = [p for p in re.split(r"(?<=[。！？!?；;])", text) if p]
    parts: list[str] = []
    for part in raw_parts or [text]:
        if len(part) <= max_chars:
            parts.append(part)
            continue
        for i in range(0, len(part), max_chars):
            parts.append(part[i : i + max_chars])

    grouped: list[str] = []
    current = ""
    for part in parts:
        if current and len(current) + len(part) > max_chars:
            grouped.append(current)
            current = part
        else:
            current += part
    if current:
        grouped.append(current)
    return grouped


def split_caption_by_length(entry: dict[str, Any], max_chars: int) -> list[dict[str, Any]]:
    text = entry["text"]
    units = split_text_units(text, max_chars)
    if len(units) == 1:
        return [entry]

    start = int(entry["start_ms"])
    end = max(int(entry["end_ms"]), start + len(units) * SRT_TIME_EPSILON_MS)
    duration = end - start
    total_chars = sum(max(len(unit), 1) for unit in units)

    output: list[dict[str, Any]] = []
    cursor = start
    for index, unit in enumerate(units):
        if index == len(units) - 1:
            unit_end = end
        else:
            unit_end = start + round(duration * sum(len(x) for x in units[: index + 1]) / total_chars)
        output.append({"start_ms": cursor, "end_ms": max(unit_end, cursor + SRT_TIME_EPSILON_MS), "text": unit})
        cursor = output[-1]["end_ms"]
    return output


def extract_subtitles(result: Any, offset_ms: int, duration_ms: int, max_chars: int, sensevoice: bool) -> list[dict[str, Any]]:
    duration_s = duration_ms / 1000
    subtitles: list[dict[str, Any]] = []

    for item in result_entries(result):
        sentence_info = item.get("sentence_info") or item.get("sentences") or []
        if sentence_info:
            for sent in sentence_info:
                if not isinstance(sent, dict):
                    continue
                text = clean_text(str(sent.get("text", "")), sensevoice=sensevoice)
                if not text:
                    continue
                start = value_to_ms(sent.get("start"), duration_s)
                end = value_to_ms(sent.get("end"), duration_s)
                if (start is None or end is None) and sent.get("timestamp"):
                    timestamps = sent["timestamp"]
                    if isinstance(timestamps, list) and timestamps:
                        starts = [value_to_ms(ts[0], duration_s) for ts in timestamps if isinstance(ts, list) and len(ts) >= 2]
                        ends = [value_to_ms(ts[1], duration_s) for ts in timestamps if isinstance(ts, list) and len(ts) >= 2]
                        starts = [x for x in starts if x is not None]
                        ends = [x for x in ends if x is not None]
                        if starts and ends:
                            start = min(starts)
                            end = max(ends)
                if start is None:
                    start = 0
                if end is None:
                    end = min(duration_ms, start + 3000)
                subtitles.extend(
                    split_caption_by_length(
                        {
                            "start_ms": offset_ms + start,
                            "end_ms": offset_ms + max(end, start + SRT_TIME_EPSILON_MS),
                            "text": text,
                        },
                        max_chars,
                    )
                )
            continue

        text = clean_text(str(item.get("text", "")), sensevoice=sensevoice)
        if text:
            subtitles.extend(
                split_caption_by_length(
                    {"start_ms": offset_ms, "end_ms": offset_ms + duration_ms, "text": text},
                    max_chars,
                )
            )

    return subtitles


def srt_timestamp(ms: int) -> str:
    ms = max(0, int(round(ms)))
    hours, rem = divmod(ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    seconds, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def normalize_subtitles(subtitles: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    last_start = 0
    for entry in sorted(subtitles, key=lambda x: (x["start_ms"], x["end_ms"])):
        text = clean_text(str(entry["text"]))
        if not text:
            continue
        start = max(int(entry["start_ms"]), last_start)
        end = max(int(entry["end_ms"]), start + SRT_TIME_EPSILON_MS)
        normalized.append({"start_ms": start, "end_ms": end, "text": text})
        last_start = start
    return normalized


def write_srt(path: Path, subtitles: list[dict[str, Any]]) -> None:
    lines: list[str] = []
    for index, entry in enumerate(subtitles, start=1):
        lines.append(str(index))
        lines.append(f"{srt_timestamp(entry['start_ms'])} --> {srt_timestamp(entry['end_ms'])}")
        lines.append(entry["text"])
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_txt(path: Path, subtitles: list[dict[str, Any]]) -> None:
    text = "\n".join(entry["text"] for entry in subtitles)
    path.write_text(text + "\n", encoding="utf-8")


def iter_progress(items: list[Path], desc: str) -> Iterable[Path]:
    if tqdm is None:
        return items
    return tqdm(items, desc=desc, unit="seg")


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists():
        raise FileNotFoundError(input_path)
    if args.segment_minutes <= 0:
        raise ValueError("--segment-minutes must be positive.")

    output_dir = Path(args.output_dir).expanduser().resolve()
    log_path = configure_logging(output_dir, args.log_level)
    ensure_executable(args.ffmpeg)
    ensure_executable(args.ffprobe)

    output_srt = Path(args.output_srt).expanduser().resolve() if args.output_srt else output_dir / f"{input_path.stem}.srt"
    output_txt = output_srt.with_suffix(".txt")
    if not args.overwrite:
        for path in (output_srt, output_txt):
            if path.exists():
                raise FileExistsError(f"{path} exists. Add --overwrite to replace it.")

    device = resolve_device(args.device, args.allow_cpu_fallback)
    logging.info("Using device=%s", device)

    run_id = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    work_dir = output_dir / f"{input_path.stem}_work_{run_id}"
    segments_dir = work_dir / "segments"
    raw_jsonl = work_dir / "raw_results.jsonl"
    errors_jsonl = work_dir / "errors.jsonl"
    work_dir.mkdir(parents=True, exist_ok=True)

    try:
        input_duration = probe_duration_seconds(input_path, args.ffprobe)
        logging.info("Input duration: %.2f seconds", input_duration)

        segment_seconds = args.segment_minutes * 60
        logging.info("Extracting audio to 16 kHz mono WAV segments of %.1f seconds", segment_seconds)
        segments = split_to_wav_segments(input_path, segments_dir, segment_seconds, args.ffmpeg)
        durations = [probe_duration_seconds(path, args.ffprobe) for path in segments]
        logging.info("Created %d segments. Sum duration: %.2f seconds", len(segments), sum(durations))

        model = build_model(args, device)
        all_subtitles: list[dict[str, Any]] = []
        offset_ms = 0
        sensevoice = is_sensevoice_model(args.model)

        with raw_jsonl.open("w", encoding="utf-8") as raw_fp, errors_jsonl.open("w", encoding="utf-8") as err_fp:
            for index, segment in enumerate(iter_progress(segments, "Transcribing"), start=1):
                duration_ms = int(round(durations[index - 1] * 1000))
                logging.info("Transcribing segment %d/%d: %s", index, len(segments), segment.name)
                try:
                    result = generate_for_segment(model, segment, args)
                    raw_fp.write(json.dumps({"segment": segment.name, "offset_ms": offset_ms, "result": result}, ensure_ascii=False, default=str) + "\n")
                    raw_fp.flush()
                    all_subtitles.extend(
                        extract_subtitles(
                            result,
                            offset_ms=offset_ms,
                            duration_ms=duration_ms,
                            max_chars=args.max_subtitle_chars,
                            sensevoice=sensevoice,
                        )
                    )
                except Exception as exc:
                    logging.exception("Segment failed: %s", segment)
                    err_fp.write(json.dumps({"segment": segment.name, "offset_ms": offset_ms, "error": repr(exc)}, ensure_ascii=False) + "\n")
                    err_fp.flush()
                    if not args.continue_on_error:
                        raise
                finally:
                    offset_ms += duration_ms

        subtitles = normalize_subtitles(all_subtitles)
        if not subtitles:
            raise RuntimeError("No subtitle entries were produced.")

        output_srt.parent.mkdir(parents=True, exist_ok=True)
        write_srt(output_srt, subtitles)
        write_txt(output_txt, subtitles)
        logging.info("Wrote SRT: %s", output_srt)
        logging.info("Wrote TXT: %s", output_txt)
        logging.info("Log file: %s", log_path)
        logging.info("Raw FunASR JSONL: %s", raw_jsonl)

        if args.keep_segments:
            logging.info("Kept work directory: %s", work_dir)
        else:
            shutil.rmtree(work_dir, ignore_errors=True)
            logging.info("Removed temporary work directory.")
        return 0
    except Exception:
        logging.exception("Transcription failed. Work directory is kept for debugging: %s", work_dir)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
