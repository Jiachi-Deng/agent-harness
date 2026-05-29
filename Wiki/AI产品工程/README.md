# AI产品工程

这个主题沉淀“AI agent / AI 功能从 demo 走向生产产品”所需要的方法、架构取舍、数据飞轮、评估和运维经验。

它不做通用 AI 架构百科。只有当材料能解释真实产品怎么上线、怎么度量、怎么迭代、怎么控制成本和风险时，才进入这里。

## 当前主线

- [[生产级Agent产品工程|生产级Agent产品工程]]：从单 agent、skills、多 agent、tool calling、数据飞轮、评估、生产反馈和观测性，整理生产级 Agent 产品的落地框架。

## 和其它主题的边界

| 主题 | 负责什么 | 不负责什么 |
| --- | --- | --- |
| [[Wiki/Vibe Coding/README|Vibe Coding]] | 普通用户和小团队如何用 Codex / Claude Code / Cursor 做出 app、SaaS、调试、部署和商业化 | 不深入生产级模型训练、专有数据飞轮和企业 agent 架构 |
| [[Wiki/Vibe Coding/60-Agent Skills/Agent Skills仓库索引|Agent Skills]] | skills 作为 AI 编程工作流和个人/团队 SOP 的封装方式 | 不展开企业级 agent 产品系统的整体架构 |
| [[Wiki/AI行业判断/README|AI行业判断]] | 大方向、范式变化、长期判断 | 不承担具体产品工程检查清单 |
| [[Wiki/AI一人公司/README|AI一人公司]] | 创始人、独立开发和小团队如何用 AI 压缩创业生命周期 | 不维护企业级 agent 平台架构 |

## 材料归位规则

| 新材料主要讲什么 | 优先进入哪里 |
| --- | --- |
| 生产级 tool-calling agent、专有数据、训练/评估/反馈飞轮 | `生产级Agent产品工程` |
| 单 agent / 多 agent 架构模式、supervisor、router、pipeline、parallel、evaluator | `生产级Agent产品工程` |
| skills 的格式、description、eval、gotchas、渐进加载 | 先进入 `Vibe Coding/60-Agent Skills`，涉及生产系统时再反向补本主题 |
| AI 产品具体业务案例，如客服、工作流、Flow、coding、数据分析 | 进入本主题作为模式证据，再按业务主题回流 |
| 最新模型价格、API 变更、平台权限 | 进入强时效页或待核验队列，不在本主题写死 |

## 当前缺口

- 还缺真实线上 agent 产品的失败案例、成本账单、观测面板和事故复盘。
- 还缺中文团队/小团队如何把生产级 agent 工程方法缩小成可执行 SOP。
- Shopify Flow clipping 的 `published` metadata 疑似异常；需要做强时效引用时回查原始网页发布日期。

