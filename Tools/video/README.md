# Video tools

视频工具用于把 Raw 视频转成 AI 可读的字幕、关键帧和临时 Markdown。

规则：

- 原始视频保留在 `Raw/` 根目录，或用户明确指定的 Raw 子目录。
- 字幕、关键帧和 OCR 结果优先输出到 `.tmp/`。
- 中间结果不等于 Wiki。
- Codex 读取中间结果后，把方法、案例、步骤和坑编译进 `Wiki/`。

常用 ASR 工具：

```bash
python Tools/video/long_video_funasr.py "Raw/example.mp4" --output-dir ".tmp/video/example/asr"
```

常用抽帧工具：

```bash
python Tools/video/video_frame_loop.py \
  --video "Raw/example.mp4" \
  --srt ".tmp/video/example/asr/example.srt" \
  --output-dir ".tmp/video/example" \
  --title "example"
```
