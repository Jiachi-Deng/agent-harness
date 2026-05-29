# Clippings

这里保存浏览器、网页、视频转写、X / blog / GitHub 页面等抓取出的 Markdown 原文。`Clippings/` 和 `Raw/` 一样是 source of truth：正文不改写、不移动、不覆盖；维护时只更新 frontmatter 里的处理状态和去向。

## 当前状态快照

截至 2026-05-29，当前共有 20 个来源 clipping：

| 状态 | 数量 | 处理含义 |
| --- | ---: | --- |
| `compiled` | 19 | 已被吸收进 Wiki / Outputs，后续只在相关页面演进时回查证据。 |
| `unreviewed` | 1 | 已进入 Clippings，但尚未审片和编译。 |
| `partial` | 0 | 暂无只吸收一部分的 clipping。 |
| `triaged` | 0 | 暂无已分级但未编译的 clipping。 |

剩余价值分布：`high` 1 个、`medium` 18 个、`low` 1 个。`medium` 表示仍值得作为证据、二次 Output 或后续维护回查，但当前没有未编译主内容。

## 未编译队列

| 材料 | 状态 | 下一步 |
| --- | --- | --- |
| `Codex Full Course 2026 The NEW Best AI Coding Tool.md` | `unreviewed` | 先放 NotebookLM 审片，再判断它和已编译的 Codex CLI / Desktop 长课是否重复；若有增量，优先吸收 Codex 桌面 app、多任务、通用办公产物、iOS / launch video 等差异点。 |

## 候选池与后续采集

新搜索候选池：

- `.tmp/vibe-coding-source-candidates-2026-05-29.md`：继续补充 Vibe Coding 原始资料的候选来源，包含官方文档、中文视频教程、YouTube transcript / summary、论文 / PDF 和安全风险案例。该文件仍是候选池，不是 Raw / Clippings。
- `.tmp/youtube-vibe-coding-candidates-2026-05-29.md`：YouTube-only 候选池，按 Codex、Claude Code、Cursor、Replit、Lovable、Bolt、Firebase Studio、Antigravity、安全、TDD、SaaS、移动端等槽位覆盖。

## 本轮已完成编译

| 材料 | 已吸收去向 | 剩余价值 |
| --- | --- | --- |
| `CODEX FULL COURSE From Zero to Deployed App (2026).md` | 已合并进 `Codex新手Vibe Coding工作流`、`Vibe Coding全栈SaaS开发闭环`、`Vibe Coding调试与迭代框架` 和 `API包装型SaaS机会与风险`。 | `medium`：后续可生成 Codex CLI 零基础操作 SOP、AI 图像 API MVP 检查清单和 API key/额度保护卡片。 |
| `OpenAI Codex Full Course 4 Hours Build & Ship.md` | 已合并进 `Codex新手Vibe Coding工作流`、`Vibe Coding全栈SaaS开发闭环`、`Vibe Coding调试与迭代框架`；课程大纲归入 `Outputs/课程与训练营/Codex新手VibeCoding课程.md`。 | `medium`：后续可从 Wiki 生成 Codex Desktop 操作 SOP、skills/MCP/subagents 对比卡、Worktrees/Automations 教程。 |
| `Master 97% of Codex in 1 Hour (full course).md` | 已合并进 `Codex新手Vibe Coding工作流`、`Vibe Coding全栈SaaS开发闭环`、`Vibe Coding调试与迭代框架` 和 `Agent Skills仓库索引`。 | `medium`：后续可生成 Codex 一小时实操 SOP、dashboard 项目练习和 Browser QA 卡片。 |
| `The AI Offer You Can Sell Tomorrow Morning.md` | 已合并进 `AI原生创业生命周期`、`Vibe Coding商业化与定价包装` 和 `中文市场Vibe Coding获客路径`。 | `medium`：后续可生成 AI Operating System 一小时咨询 SOP、报价阶梯和获客话术。 |
| `Designing, Refining, and Maintaining Agent Skills at Perplexity.md` | 已扩展 `Agent Skills仓库索引`，并作为 `生产级Agent产品工程` 的 skills 旁证。 | `medium`：后续可生成 skill 设计 / eval / gotchas 检查清单。 |
| `Flow generation through natural language An agentic modeling approach (2026).md` | 已吸收到 `生产级Agent产品工程` 和 `从VibeCoding到AgenticEngineering`。 | `medium`：`published` metadata 疑似异常；强时效引用前回查原文。 |
| `OpenClaw Multi-Agent Guide Architecture, Configuration, and Collaboration Patterns.md` | 已吸收到 `生产级Agent产品工程`。 | `medium`：后续作为多 agent 模式和生产经验旁证。 |
| `Andrej Karpathy From Vibe Coding to Agentic Engineering.md` | 已继续补强 `从VibeCoding到AgenticEngineering`、Vibe Coding 路线图和 `生产级Agent产品工程`。 | `medium`：后续可生成观点解读和工程质量线卡片。 |
| `完整的多 Agent 多 Skill 小说改编影视流水线系统。.md` | 已继续扩写 `AI短剧与漫剧制作流水线`。 | `medium`：后续可生成短剧多 agent SOP 和检查清单。 |
| `中国天才们正在排队“崩开源”.md` | 已新增 `AI时代开源生态与商业化`。 | `medium`：观点立场强，只作行业观察和风险提醒。 |

## 下一批来源建议

当前仍有 1 个 Codex clipping 等待审片。下一轮还应从候选池里优先补：

- Codex / Claude Code / Cursor / Lovable / v0 的真实工具体验与失败点。
- Playwright、browser QA、失败测试和上线前回归材料。
- 中文市场 AI 服务成交、报价、交付和售后复盘。
- 生产级 agent 产品的事故、成本、观测性和数据飞轮案例。

## 使用规则

- 新 clipping 进入后先判断是否能被现有 Wiki 页面吸收；能合并就合并，不能承载且有输出价值才新建页。
- 合并不是 append：只吸收能增强主页面的判断、步骤、案例、prompt、检查清单、风险和证据，重复定义和低价值铺垫直接丢弃。
- 编译前先看 frontmatter 的 `compile_status`、`compiled_to`、`remaining_value`，避免把已经吸收过的材料重复做成新页。
- 文件名或标题与正文不一致时，保留原 clipping 文件，不改正文；在 frontmatter 或本 README 的队列里标注真实内容和归位方向。
- 正式 Outputs 不从 clipping 直接生成；先进入 Wiki，再由 Wiki 生成教程、SOP、模板、prompt、讲义或图文卡片。
