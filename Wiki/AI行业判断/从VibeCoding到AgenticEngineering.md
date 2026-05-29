---
type: wiki
status: compiled
area: AI行业判断
tags:
  - Andrej Karpathy
  - VibeCoding
  - AgenticEngineering
  - Software3.0
  - verifiability
  - AI编程
updated: 2026-05-28
---

# 从Vibe Coding到Agentic Engineering

## 为什么这篇值得编译

这篇访谈不是教程，也没有直接给出“怎么做一个 app”的步骤。但它来自 Andrej Karpathy 这种长期站在 AI 和软件交叉前沿的人，适合当作方向性框架：

- 判断 AI 编程到底是短期工具，还是新的软件范式。
- 判断哪些应用会先被自动化。
- 判断新手 vibe coding 和专业 agentic engineering 的区别。
- 判断人在 AI 工作流里还负责什么。
- 判断这个 vault 为什么要做 Wiki，而不是只囤原文。

因此它不作为课程、工具比较或教程产物维护，而归入 `AI行业判断` 主题，同时反向影响 `Vibe Coding` 主题。

## 核心观点

### 1. Software 3.0：context 变成新的编程接口

Karpathy 的 Software 3.0 框架大意是：

- Software 1.0：人直接写规则和代码。
- Software 2.0：人组织数据、目标和神经网络训练。
- Software 3.0：人通过 prompt、context、文档、环境和工具调用来“编程”LLM。

这对 AI 应用落地的启发是：以后很多“产品能力”不一定体现为传统代码，而体现为你能不能给 agent 一个正确的上下文、权限、工具和验证闭环。

### 2. Agentic workflow 是一次明显跃迁

他提到自己在某个时间点后明显感觉模型生成的代码块变得可靠，开始持续要求更多任务，并越来越信任系统。这解释了为什么 vibe coding 会突然从玩具感变成生产力现象。

但这个判断不能被理解成“AI 已经可以无脑代替工程”。更准确的结论是：agentic coherent workflow 开始成立，普通人能做出更多东西，专业工程的质量门槛也随之提高。

### 3. Vibe coding 提高下限，Agentic engineering 保住上限

这是这篇最适合进入 Vibe Coding 专题的观点：

- `vibe coding`：提高所有人的软件创造下限，让非工程师也能做 app。
- `agentic engineering`：在使用 agent 加速的同时，不牺牲安全、设计、可维护性和专业质量线。

所以这个 vault 不能只做“新手如何 prompt AI 写 app”。更重要的是要逐步补：

- spec 怎么写。
- 如何验证。
- 如何看 diff。
- 如何处理安全和权限。
- 如何做部署和回归检查。
- 如何判断 AI 生成代码是否只是“能跑但很脏”。

### 4. 可验证性决定自动化速度

Karpathy 的一个核心判断是：LLM 更容易自动化那些输出可验证的领域。代码、数学、测试、编译、网页是否能运行，都属于更容易建立验证回路的领域。

对应用落地的含义：

- AI 编程会特别快，因为可以跑测试、看错误、部署、点击验证。
- 运营、营销、写作也能自动化，但验证更难，往往需要人类品味、业务指标或 LLM judges。
- 如果一个业务流程能被拆成输入、动作、输出、检查，就更适合 agent 化。

这直接支持当前 Wiki 方向：每个教程和 SOP 都应该写“如何验证”，而不是只写“如何生成”。

### 5. LLM 是 jagged intelligence，不是稳定员工

他强调模型能力是 jagged 的：它可能能重构大型代码库，却在常识小题上出错。这说明 agent 很强，但不能被当成稳定、完整、具备动机的人类智能。

落地含义：

- 高风险流程必须有人类检查点。
- 工具输出必须有回查证据。
- 对安全、权限、支付、用户数据不能“看起来能跑就上线”。
- 课程里要教用户识别 AI 的不稳定边界。

### 6. 人还负责 taste、judgment、spec 和 understanding

Karpathy 的判断是，agent 现在像很强的 intern：细节和 API 可以交给它，但人仍然要负责：

- 审美和产品 taste。
- 工程 judgment。
- 详细 spec。
- 数据模型的关键设计，比如不能用 email 去关联资金账户。
- 对系统的理解。

这和 [[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]] 是同一条线：可以把 thinking 外包一部分，但不能把 understanding 外包掉。

### 7. Agent-native infrastructure 会重写很多工具

他提到很多文档和工具仍然是写给人的，但 agent 世界需要的是“我应该复制什么给 agent”“agent 能否自己配置、部署、调试”。这对后续选题很重要：

- Vercel / Firebase / Supabase / Cloudflare 这类平台，未来要看 agent-native 程度。
- 好工具不只是 UI 好用，还要 agent 可读、可配置、可验证。
- 文档、模板、安装流程、错误信息都应该面向 agent 友好。

### 8. Agent 可能会替代一部分传统安装器和 UI

Karpathy 用 OpenClaw 安装和 Menu Gen 的例子说明了一件事：Software 3.0 不只是“用 AI 写代码”，还会改变软件被安装、配置和使用的方式。

以前的安装器倾向于写复杂 shell script，覆盖各种平台和环境。agent-native 的方式是给 agent 一段指令，让它查看当前电脑、执行命令、遇到错误自己调试。对用户来说，真正的问题变成：什么内容应该复制给 agent，agent 需要哪些权限，失败后怎么验证和回滚。

Menu Gen 例子则提醒我们：有些传统 app 可能会被“直接给模型一个 raw prompt”替代。不是所有功能都值得做成完整产品；如果用户只需要一次性视觉处理或轻量计算，模型本身可能已经足够。

这会影响本库判断 AI 产品机会：

- 如果一个功能只是一句 raw prompt 就能稳定完成，做成 SaaS 的价值要重新评估。
- 如果一个流程需要账号、权限、状态、协作、审计、数据沉淀和自动化，app / agent / skill 组合仍然有价值。
- 工具文档未来要越来越 agent-readable：少写“你点击哪里”，多提供 agent 能执行、能验证、能回滚的步骤。

### 9. LLM knowledge bases 是理解增强工具

这点和当前 vault 的方向高度一致。Karpathy 提到自己喜欢用 LLM 基于文章构建 wiki，因为换一种投影方式会帮助理解。

这给当前 `Clippings / Raw -> Wiki -> Outputs` 的流程提供了很强的方向旁证：我们不是在囤资料，而是在把资料重编译成可以提问、组合、复用和生成产物的知识层。

### 10. 生产级 AI 产品的护城河会转向数据和反馈

Shopify Flow 的生产案例补强了 Karpathy 的 verifiability 判断：可验证任务不仅更容易被 AI 自动化，也更容易形成模型、工具和数据飞轮。

当一个产品有真实用户、真实 workflow、真实激活数据和专家标注，它就能把闭源模型 API 变成更具体的产品能力：

- 从生产 workflow 反推用户意图。
- 构造 tool trajectory。
- 用更适合模型的中间表示训练。
- 小流量上线后用生产反馈修正 benchmark 盲点。
- 把高质量线上样本回流训练池。

这说明严肃 AI 产品不是“接入最新模型”就结束。长期差异会来自专有数据、评估系统、工具接口、反馈速度和生产运维能力。具体产品工程框架见 [[Wiki/AI产品工程/生产级Agent产品工程|生产级Agent产品工程]]。

## 对本 vault 的处理原则

这类大牛访谈应该这样处理：

- 不当作教程，不直接生成“照做步骤”。
- 不拆成过多空页。
- 提炼成少数高层判断，作为后续教程和工具比较的判断框架。
- 进入 `AI行业判断`，并链接到相关应用主题。
- 如果某个观点已经能指导具体操作，再下沉到 `AI编程与Vibe Coding`、`AI知识库`、`Workflows`。

## 会影响哪些已有页面

- [[Wiki/Vibe Coding/00-Overview/Vibe Coding专题路线图|Vibe Coding专题路线图]]：补充 `Agentic Engineering` 和验证优先的方向。
- [[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]]：补充“不能外包理解”的行业级旁证。
- [[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]：提示 vibe coding 只是入口，正式产品还需要质量线。
- [[Wiki/AI知识库/个人知识库到内容选题|个人知识库到内容选题]]：补充 LLM knowledge base 对理解的价值。
- [[Wiki/AI产品工程/生产级Agent产品工程|生产级Agent产品工程]]：把 verifiability、agent-native infrastructure 和生产反馈飞轮落到具体工程判断。

## 可生成 Outputs

- 观点解读：Karpathy 说的 Agentic Engineering 到底是什么。
- 图文卡片：Vibe Coding vs Agentic Engineering。
- 课程开篇：为什么 AI 编程不是“不学代码”，而是换一种工程能力。
- 工具比较标准：什么叫 agent-native 工具。

## 来源

- [[Clippings/Andrej Karpathy From Vibe Coding to Agentic Engineering|Andrej Karpathy: From Vibe Coding to Agentic Engineering]]：主来源，Sequoia AI Ascent 2026 访谈。
- [[Clippings/Flow generation through natural language An agentic modeling approach (2026)|Shopify Flow generation through natural language]]：作为生产级 agent 产品和反馈飞轮旁证；其 `published` metadata 疑似异常，强时效引用前需回查原文。
