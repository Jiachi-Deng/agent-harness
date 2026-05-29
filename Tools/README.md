# Tools

这里保留轻量辅助工具。工具只做转写、扫描、digest、OCR、视频 / PDF 辅助处理，不再生成 `Sources/` 四件套。

## 常用命令

```bash
cd "/Users/jachi/Documents/agent-harness"
Tools/course-digest.sh
Tools/ingest_raw_pdfs_marker.py
```

## 规则

- PDF / 视频转写的中间结果进入 `.tmp/`。
- 中间结果不是正式知识层。
- AI 读取中间结果后，把可复用内容编译进 `Wiki/`。
- 不要恢复旧 `Sources/` 工作流。
