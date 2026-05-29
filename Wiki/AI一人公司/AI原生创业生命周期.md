---
type: wiki
status: compiled
area: AI一人公司
updated: 2026-05-29
tags:
  - AI一人公司
  - AI原生创业
  - Founder
  - MVP
  - GTM
  - AI服务
---

# AI原生创业生命周期

## 解决什么问题

AI 让一个人能做过去小团队才能做的事：研究市场、写代码、做 PPT、整理客户反馈、自动化运营、搭内部系统。但这不等于“有想法就马上做产品”。

AI 原生创业的核心变化是：技术执行成本下降了，验证、判断、定位、销售、交付边界和系统化能力变得更重要。

## 四个阶段

| 阶段 | 核心任务 | AI 能放大的部分 | 最大风险 |
| --- | --- | --- | --- |
| Idea | 证明问题真实、具体、频繁，找到问题-解决方案匹配 | 市场研究、竞品地图、访谈问题、反方质疑 | 把能做 demo 误认为已经验证 |
| MVP | 用最小产品证明用户能获得价值 | agentic coding、scope 文档、架构上下文、指标设计 | 零摩擦 scope creep、早期数据误读、安全经验不足 |
| Launch | 把早期牵引变成可重复增长和生产系统 | 代码审计、运营任务盘点、CRM/反馈/报告自动化 | 创始人成为瓶颈，技术债和安全债到期 |
| Scale | 把创始人脑内知识变成可审计、可传递的系统 | 知识库、skills、工作流、GTM 执行层 | 系统不可信、组织治理和合规跟不上 |

## Idea 阶段：不要用原型替代验证

Founder Playbook 里最值得吸收的警告是：agentic coding 把“有想法 -> 有产品”的距离压得太短，反而让创始人更容易跳过验证。

Idea 阶段要先回答：

- 谁具体有这个问题？
- 这个问题多久发生一次，痛到什么程度？
- 他们现在怎么解决，为什么不满意？
- 竞品和替代方案是什么？
- 你的方案解决的是实际问题，还是你想象的问题？

AI 在这里最适合做反方和研究助手：让它审查假设、生成访谈框架、整理竞品、找 disconfirming evidence。真正的证据仍然来自真实人的对话和行为。

可执行动作：

- 把问题陈述改成可测试假设，而不是“某件事很麻烦”这种泛观察。
- 让 AI 按直接竞品、间接竞品、潜在收购方、相邻玩家四层画竞争地图，并专门论证“为什么他们会赢、你会输”。
- 让 AI 从竞品评论、行业报告、社群讨论里提炼未被解决的抱怨。
- 访谈问题先自己写，再让 AI 标出诱导性、面向未来、太宽泛或容易得到礼貌答案的问题。
- 每 5 次访谈后，用 AI 分两栏整理“支持假设的证据”和“挑战假设的证据”，防止只看自己想看的信号。

## MVP 阶段：先写范围和上下文，再让 AI 写代码

AI 能快速生成代码，但 MVP 仍然要先写清：

- 产品做什么。
- 明确不做什么。
- 什么时候才允许加新功能。
- 未来 6 个月大概的用户量和风险假设。
- 技术栈、依赖和安全边界。
- 需要提前埋哪些 activation、retention、Day 7、Day 30 指标。

这些内容应该进入项目上下文文件，例如 `CLAUDE.md`、`AGENTS.md`、`spec.md` 或项目 brief。每次 AI 编程会话结束后，把新产生的架构决策和范围变化写回上下文。

MVP 阶段的关键动作：

- 在打开 Claude Code / Codex 前，先写 architecture context：用户、规模假设、依赖取舍、安全边界和已接受 tradeoff。
- 定义 scope 文档：MVP 做什么、不做什么、什么用户证据才允许加功能。
- 每次 agentic coding session 开始前重读 scope 和上下文，结束后补一条 session log：做了什么、做了哪些决策、引入了什么假设。
- 任何真实用户触碰前，先做安全审查：auth/session、API 数据暴露、输入校验、注入风险、依赖漏洞。
- 在 launch 前定义 activation、retention、Day 7、Day 30 和 false positive 指标，不要上线后才挑对自己好看的数据。
- 如果连续三轮迭代没有接近 PMF 指标，让 AI 做诊断：是否存在响应更好的细分人群、问题是 positioning 还是 product、当前路径是否仍现实。

## Launch 阶段：创始人要从亲自做事转向设计系统

Launch 阶段的关键变化是：产品已经有真实用户，创始人不能再靠“我都看着”维持运转。

要让 AI 帮忙审计三类系统：

- 技术系统：结构弱点、测试缺口、可维护性、安全和合规。
- 运营系统：支持、triage、反馈收集、周报、CRM、文档更新。
- 决策系统：哪些必须创始人判断，哪些可以自动化，哪些可以交给别人。

这里和 Vibe Coding 的连接很强：代码审计、上线安全、自动化巡检、GitHub Issues、worktrees、browser QA 都是 Launch 阶段把 demo 变成业务系统的必要动作。

Launch 阶段要补的系统：

- 技术债排序：让 agent 审计结构弱点、测试缺口和重构候选，再按 release / sprint / 可延后项排序。
- 创始人注意力审计：列出所有只有你亲自触发才发生的任务，分成自动化、可委派、必须创始人判断三类。
- 轻量产品管理系统：spec 模板、bug triage 决策树、sprint 节奏和每周指标 brief。
- 合规和企业采购资料：安全整改顺序、文档、控制项、支持流程和客户能审查的证据。

## Scale 阶段：把创始人知识变成系统资产

AI 一人公司真正可持续的地方，不是永远一个人做所有事，而是把创始人的领域经验变成可运行、可审计、可训练别人的系统。

需要沉淀：

- 行业术语、监管坑、客户常见误解、边缘案例。
- 创始人做判断的流程，例如如何审合同、如何判断线索质量、如何回复客户异议。
- 重复工作流对应的 skills、模板、脚本和检查清单。
- GTM 执行层：内容日历、outbound 序列、CRM hygiene、销售资料、demo 环境。

这些知识一旦变成结构化上下文和流程，就不只是“AI 帮我干活”，而是形成普通大模型无法直接复制的领域知识底座。

Scale 阶段的护城河不只来自代码，还来自三类积累：

- 领域边缘案例：找出通用竞争对手一定会错的垂直场景，把它做成 dedicated test case，长期累积成 moat map。
- 用户行为数据：哪些输出被接受、哪些被拒绝、哪些 workflow 反复出现，把这些高信号行为转成反馈飞轮。
- workflow lock-in：审计前 10 个客户把哪些自动化、集成、团队流程跑在你的产品上，判断切换成本来自哪里。

## Rung Zero：先卖小时，不急着卖大项目

`The AI Offer You Can Sell Tomorrow Morning` 提供了一条适合 AI 服务新手的商业化阶梯：

```text
免费教朋友 / 低价小时
  -> 付费诊断或 audit
  -> 聚焦项目
  -> retainer / 长期顾问
```

它的核心不是低价劳动力，而是降低信任门槛：先用一小时帮老板搭 AI Operating System、解释工具、连接数据、抽取业务 know-how、管理对方的焦虑。这个小时同时是训练、销售、发现需求和付费 scoping。

AI Operating System 的交付边界可以理解为：

- 捕捉业务数据。
- 捕捉老板或团队的 subject matter expertise。
- 把日常 workflow 放进一个可持续操作的 AI 工作台。
- 让业务不再完全堵在创始人或老板脑子里。

## 从小时转项目

不要在第一小时硬推项目。更好的路径是：

1. 先帮对方完成一个真实设置或小工作流。
2. 观察数据源、团队抱怨、重复动作、政治阻力和业务优先级。
3. 在第二或第三次会话里指出一个具体 workflow。
4. 说明它为什么值得做、可能产生什么业务影响、需要几周完成。
5. 对方自然意识到“自己学着做太慢”时，再给项目 proposal。

这条线应该和 [[Wiki/Vibe Coding/40-Business/Vibe Coding商业化与定价包装|Vibe Coding商业化与定价包装]]、[[Wiki/Vibe Coding/40-Business/中文市场Vibe Coding获客路径|中文市场Vibe Coding获客路径]] 联动：AI一人公司页负责创业生命周期和服务阶梯，Vibe Coding 页负责具体报价、包装、获客和交付边界。

## 适合生成的 Outputs

- AI 原生创业四阶段检查清单。
- 一人公司 Idea -> MVP -> Launch 路线图。
- AI Operating System 一小时咨询课 SOP。
- 从咨询小时到项目/retainer 的成交话术模板。
- 面向小企业老板的 AI 工作台搭建课讲义。

## 来源

- `Raw/The-Founders-Playbook-05062026_v3 (1).pdf` + `.tmp/marker-extractions/The-Founders-Playbook-05062026_v3 (1)/The-Founders-Playbook-05062026_v3 (1).md`：Anthropic founder playbook，提供 Idea / MVP / Launch / Scale 四阶段、创始人职责变化、Claude / Claude Code / Claude Cowork 分工、阶段练习和 AI-native startup 风险。
- [[Clippings/The AI Offer You Can Sell Tomorrow Morning|The AI Offer You Can Sell Tomorrow Morning]]：提供 AI 服务商业化阶梯、AI Operating System offer、一小时会话结构、找前 10 个客户和从小时转项目的路径。
- [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]：支撑 MVP / Launch 阶段的开发、部署、自动化和验证动作。
