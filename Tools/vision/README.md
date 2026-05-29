# Local Vision Backend

本目录保留 Ollama 视觉辅助工具，用于识别截图、视频帧、PPT 页面、网页截图、表格和流程图。

视觉结果只是中间材料，应进入 `.tmp/` 或作为 Wiki 编译时的参考，不直接作为正式 Output。

示例：

```bash
Tools/vision/ollama_vlm.py \
  ".tmp/video/example/frames/frame-0001.jpg" \
  --resize-width 768 \
  --max-tokens 512 \
  --prompt "识别这张 AI 应用教程截图，输出可复核的 Markdown。看不清写[不确定]，不要编造。" \
  --output ".tmp/video/example/vision/frame-0001.md"
```
