---
type: wiki
status: compiled
area: AI产品工程
updated: 2026-05-29
tags:
  - Agent
  - AI产品工程
  - ToolCalling
  - MultiAgent
  - AgentSkills
  - Evaluation
  - DataFlywheel
---

# 生产级Agent产品工程

## 解决什么问题

很多 AI 产品 demo 能跑，但一到真实用户、真实数据、真实成本和真实失败场景就崩。本页整理的是从“让 agent 做一次任务”升级到“让 agent 长期稳定地服务产品”的工程判断。

核心问题不是“要不要多 agent”，而是：

- 这个任务有没有真实业务价值和可验证结果？
- 单 agent + skills 能不能先解决？
- 什么时候才值得引入 supervisor、router、pipeline、parallel 或 evaluator？
- 模型输出如何连接真实系统、工具、权限和日志？
- 评估和训练数据如何从生产反馈里持续变好？

## 先从最小可工作的 agent 开始

Anthropic 的 agent 架构材料和 OpenClaw 多 agent 指南都指向同一个判断：不要因为多 agent 看起来高级就一开始上多 agent。

更稳的演进路径是：

```text
单 agent
  -> 加工具和受控权限
  -> 加 skills / 标准流程
  -> 加评估和日志
  -> 遇到明确瓶颈后再拆 supervisor / router / pipeline / parallel
  -> 接入生产反馈飞轮
```

单 agent 适合：

- 开放式但边界清楚的任务。
- 需要调用多个工具，但仍能由一个上下文掌控。
- 任务复杂度还没有到必须拆角色的程度。
- 需要快速验证 ROI、用户价值和失败模式。

不要急着多 agent 的原因：

- 每个 agent 都会带来新的上下文、路由、沟通和调试成本。
- agent 之间会产生理解差、重复工具调用和 token 成本。
- supervisor 也可能变成上下文瓶颈。
- 如果连单 agent 的日志、评估、权限和回滚都没做好，多 agent 只会放大混乱。

## Skills 是加能力，不是堆说明书

Perplexity 的 skill 设计材料补上了一个关键视角：skill 不是普通 prompt，也不是把文档塞给模型。它是一种渐进加载的能力包。

生产系统里 skills 的价值在于：

- 把稳定流程、领域规则、工具调用步骤和 gotchas 变成可复用模块。
- 让单 agent 在不拆成多 agent 的情况下拥有专业能力。
- 让不同 agent 共享同一套标准，而不是各自凭上下文临场发挥。
- 降低 prompt 膨胀，把详细参考资料放进按需读取的文件。

但每个 skill 都是税。只有当模型在没有专门上下文时会反复做错、或者团队需要稳定复用某个流程时，才值得写 skill。否则优先删掉。

## 多 agent 的四种常用模式

| 模式 | 适合什么 | 风险 |
| --- | --- | --- |
| Supervisor | 一个主 agent 分派任务、收集结果、综合输出 | supervisor 容易成为上下文和质量瓶颈 |
| Router | 先判断请求类型，再分派给对应专家 | 路由错会直接把任务送进错误上下文 |
| Pipeline | 研究 -> 草稿 -> 审核 -> 发布这类顺序流程 | 上游错误会传递到下游，回改成本高 |
| Parallel | 多个 agent 同时从不同角度分析或审查 | 成本高，结果合并和冲突处理要清楚 |

选型原则：

- 能被单 agent + skill 做好的，不拆 agent。
- 需要明确责任链、可审计和业务规则时，用 supervisor 或 sequential pipeline。
- 输入类型多、处理路径差异大时，用 router。
- 需要多角度审查、风险评估、代码安全/性能/可维护性并行 review 时，用 parallel。
- 需要生成后反复打磨质量时，用 evaluator-optimizer。

## 架构选择的四个问题

Marker 转写后的 Anthropic PDF 保留了更完整的决策框架。选 agent 架构前，先问四个问题，而不是从模式名出发。

| 问题 | 倾向选择 | 原因 |
| --- | --- | --- |
| 需要多强控制？ | 高控制用 single agent / sequential；中等控制用 hierarchical；低控制研究探索才考虑 collaborative | 金融、合规、交易和安全场景必须能解释决策链 |
| 问题域有多复杂？ | 单一可重复任务用 single agent；多域但可预测用 workflow；开放复杂问题才用 multi-agent | 架构复杂度要匹配问题复杂度 |
| 资源约束是什么？ | 预算有限先 single agent；时间紧先上线单 agent 并预留演进接口；长期项目再做模块化扩展 | 多 agent token 和调试成本显著更高 |
| 是否需要深领域能力？ | 单领域先 single agent + specialized skills；多领域协作再拆 specialist agents | Skills 往往能先解决专业性，不必马上拆 agent |

一个实用演进例子：

```text
Phase 1：单 agent 处理客户咨询，先证明价值
Phase 2：router 区分订单状态、产品问题、投诉
Phase 3：每类问题有 specialist agent，共享上下文
Phase 4：库存、支付、物流等多 agent 协调
Phase 5：evaluator agent 做质量保证和持续改进
```

这补强了本页的核心原则：最好的架构不是最复杂的架构，而是满足今天需求、并给明天能力留演进路径的最简单架构。

## 生产级 tool-calling agent 的数据飞轮

Shopify Flow 案例提供了比通用 agent 架构更具体的生产经验：他们不是只靠闭源模型 API，而是把用户真实 workflow、合成数据、tool trajectory、生产反馈和每周再训练连接成飞轮。

可复用框架：

```text
已有生产行为
  -> 反推用户意图
  -> 构造理想 tool trajectory
  -> 训练 / 微调 tool-calling agent
  -> 小流量上线
  -> 用真实用户行为和专家 judge 评估
  -> 高质量样本回流训练池
  -> 每周迭代
```

几个关键经验：

- 冷启动时可以从已有人工 workflow 反推用户请求，而不是凭空编数据。
- 输出如果是自定义 DSL，最好转换成模型更熟悉的表示，再转回生产 DSL。
- 训练数据里的工具名、工具顺序、返回字段、system prompt 和生产环境必须对齐，细小 drift 也会降低效果。
- offline benchmark 不是事实。小流量上线后，真实用户会提出 benchmark 没覆盖的编辑、配置、集成和解释类请求。
- 评估最好拆成多个维度，比如是否理解意图、是否该创建 workflow、组件是否选对、下一步是否清楚。

这个案例对本库最重要的启发是：生产级 AI 产品的护城河不只是“用了哪个大模型”，而是专有数据、表示方式、工具接口、评估系统和迭代速度。

## 观测性和治理

生产 agent 必须能解释自己，不然一出问题只能靠猜。

至少要有：

- 工具调用日志：调用了什么、参数是什么、返回了什么、失败在哪里。
- 决策日志：为什么选择某条路线、为什么升级到多 agent、为什么触发人工确认。
- 成本记录：每次运行的模型、token、工具调用和外部 API 成本。
- 质量评估：离线 eval、线上成功率、人工抽检、用户反馈。
- 安全边界：哪些工具可写、哪些只读、哪些动作必须人工批准。
- 回滚路径：错误写入数据库、文件、CRM、发布系统后如何恢复。

## 适合生成的 Outputs

- 生产级 Agent 产品上线前检查清单。
- 单 agent 到多 agent 的架构选型卡。
- Tool-calling agent 数据飞轮 SOP。
- Agent Skills 设计与评估清单。
- AI 产品工程课程中的“demo 到 production”章节。

## 来源

- `Raw/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks.pdf` + `.tmp/marker-extractions/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks.md`：Anthropic agent 架构模式、单 agent / 多 agent / hierarchical / sequential / parallel / evaluator / network、决策框架和“从简单开始、可观测、按业务价值演进”的判断。
- [[Clippings/Flow generation through natural language An agentic modeling approach (2026)|Shopify Flow generation through natural language]]：Sidekick / Shopify Flow 的 tool-calling agent、合成数据、Python DSL、生产环境镜像、评估和每周训练飞轮。该 clipping 的 `published` metadata 疑似异常，做强时效引用前需要回查原文。
- [[Clippings/OpenClaw Multi-Agent Guide Architecture, Configuration, and Collaboration Patterns|OpenClaw Multi-Agent Guide]]：单 agent 瓶颈、三层隔离、bindings、agent-to-agent 通信、supervisor / router / pipeline / parallel 和生产环境注意事项。
- [[Clippings/Designing, Refining, and Maintaining Agent Skills at Perplexity|Designing, Refining, and Maintaining Agent Skills at Perplexity]]：skills 的格式、渐进加载、description、eval、gotchas 和维护飞轮。
- [[Clippings/Andrej Karpathy From Vibe Coding to Agentic Engineering|Andrej Karpathy: From Vibe Coding to Agentic Engineering]]：verifiability、agent-native infrastructure、vibe coding 与 agentic engineering 的边界。
