# Where To Find Raw

Raw 由用户手动抓取。Codex 不默认自动抓网页、repo、文档或社交媒体内容，除非用户明确要求。

## 优先收集什么

围绕 AI 应用落地收集：

- AI 编程 / WebCoding 教程、实战项目、调试复盘。
- AI 做网页、网站、落地页、产品 demo 的案例和教程。
- AI 做 PPT、Word、表格、报告、方案的流程和模板。
- AI 电商、外贸、获客、客服、运营自动化案例。
- AI 视频、短剧、漫剧、配音、分镜、剪辑流水线。
- 生产级 AI agent 产品、tool calling、评估、观测性、数据飞轮和多 agent 架构案例。
- AI 一人公司、独立开发、个人业务自动化案例。
- 工具横评、价格变化、能力边界、替代方案。

## What to save

关键来源优先保存快照或可复现锚点：

- 网页 / blog：优先放进 `Clippings/`，保留 frontmatter、原始 URL、发布时间。
- NotebookLM / 人工审片记录：放入 `Raw/NotebookLM/`，因为它是用户加工后的判断，不是外部原文。
- 课程 prompt / 课件 / 示例文件：放入 `Raw/CourseKits/`，原始文件不改写；先编译进 `Wiki/`，正式 prompt / SOP / 讲义再从 Wiki 生成到 `Outputs/`。
- PDF：放入 `Raw/` 根目录。
- 视频：放入 `Raw/` 根目录，或只保存视频 URL、字幕、关键帧到 `Clippings/` / `.tmp/`。
- 截图：放入 `Raw/` 根目录；如果截图很多，再自然长出 `Raw/assets/`。
- repo / demo：放入 `Raw/` 根目录，记录 URL、commit、release 或压缩包。
- 数据：放入 `Raw/` 根目录；如果数据很多，再自然长出 `Raw/datasets/`。

## Rule

Raw 和 Clippings 只保存原始证据，不直接生成正式 Outputs。需要使用时，先编译进 `Wiki/`；需要交付产物时，再从 Wiki 生成 `Outputs/`。
