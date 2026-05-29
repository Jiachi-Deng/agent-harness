# Raw

这里保存非 clipping 的原始材料。Raw 是 source of truth，只新增，不改写，不覆盖。

`Clippings/` 是浏览器剪藏 Markdown 的保留目录；不要把它搬进 Raw。

Raw 默认扁平化，不预设 `papers/`、`blogs/`、`repos/`、`videos/` 这类分类目录。文件多到确实需要拆分时，再从材料自然长出 `assets/`、`media/`、`datasets/` 等少数目录。

适合放入 Raw 根目录的材料：

- PDF、电子书、报告、论文。
- 视频、课程、录屏。
- 截图、长图、界面图。
- repo 快照、clone 记录、commit 记录。
- 表格、JSON、数据文件。

Raw 不是 Wiki。需要使用 Raw 时，先读取 / 转写 / OCR，再编译进 `Wiki/`。如果要做 prompt、SOP、讲义或图文卡片，再从 Wiki 生成 `Outputs/`。

## 当前例外目录

- `Raw/NotebookLM/`：用户把视频、课程或长文放进 NotebookLM 后形成的对话、追问、总结和人工审片判断。它是用户加工证据，不是外部原文。
- `Raw/CourseKits/`：课程作者提供的 prompt、课件、示例文件和截图等配套资产。原始文件保持不改写；先编译进 Wiki；正式 prompt、SOP 或讲义再从 Wiki 生成到 `Outputs/`。

维护时先看这些 Raw 记录里的用户判断，再回查对应 `Clippings/` 原文。

## 当前库存与队列

截至 2026-05-29，Raw 里有三类材料：

| 类别 | 文件 | 状态 | 下一步 |
| --- | --- | --- | --- |
| NotebookLM 审片记录 | `Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md` | 已编译 | 后续只在维护 Vibe Coding 全栈课时回查用户判断。 |
| NotebookLM 审片记录 | `Raw/NotebookLM/2026-05-29--youtube--OpenAI Codex Full Course 4 Hours Build & Ship.md` | 已编译 | 后续维护 Codex Desktop、skills、MCP、automations、worktrees 和 Creator Carousel Studio 相关页面时回查。 |
| NotebookLM 审片记录 | `Raw/NotebookLM/2026-05-29--youtube--CODEX FULL COURSE From Zero to Deployed App (2026).md` | 已编译 | 后续维护 Codex CLI 新手起步、AI 图像 API MVP、OpenRouter 调试和 Vercel 部署相关页面时回查。 |
| CourseKit | `Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/` | 已编译 | 原始 prompt 保持不动；正式 prompt 产物已迁入 `Outputs/SOP与模板/`。 |
| Karpathy skill 线索与 repo 快照 | `Raw/Get笔记-AI大佬Andrej Karpathy三年经验提炼：15个核心技能解析.md`、`Raw/GitHub-LearnPrompt-andrej-karpathy-skills-19fc6870.md` | 已编译 | 后续维护 `Wiki/Vibe Coding/60-Agent Skills/LearnPrompt Karpathy Skills仓库.md` 时回查。 |
| PDF | `Raw/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks.pdf` | 已转写并编译 | 已用 `Tools/ingest_raw_pdfs_marker.py --mode single --force` 转成 `.tmp/marker-extractions/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks.md`，并回查补强 `Wiki/AI产品工程/生产级Agent产品工程.md`。 |
| PDF | `Raw/The-Founders-Playbook-05062026_v3 (1).pdf` | 已转写并编译 | 已用 `Tools/ingest_raw_pdfs_marker.py --mode single --force` 转成 `.tmp/marker-extractions/The-Founders-Playbook-05062026_v3 (1)/The-Founders-Playbook-05062026_v3 (1).md`，并回查补强 `Wiki/AI一人公司/AI原生创业生命周期.md`。 |
| 系统文件 | `Raw/.DS_Store` | 忽略 | 不作为知识材料处理。 |

PDF 标准流程以 `Tools/ingest_raw_pdfs_marker.py` 为准：Marker 转写到 `.tmp/marker-extractions/`，中间结果不是正式知识层；AI 读取 `.tmp/` 中间结果和原始 PDF 后，再把可复用内容编译进 `Wiki/`。
