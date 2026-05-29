# PDF tools

PDF 工具现在只作为 Raw 辅助处理，不生成 `Sources/`。

推荐流程：

1. 原始 PDF 放在 `Raw/` 根目录。
2. 使用根目录工具转写到 `.tmp/`。
3. Codex 读取 `.tmp/` 中间结果和原始 PDF，把可复用内容编译进 `Wiki/`。

正式教程、案例、比较和 SOP 必须从 `Wiki/` 生成。
