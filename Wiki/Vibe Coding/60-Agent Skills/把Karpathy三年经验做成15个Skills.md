---
type: wiki
status: compiled
area: Vibe Coding
tags:
  - AndrejKarpathy
  - AgentSkills
  - AI编程
  - 内容选题
  - 知识产品
updated: 2026-05-25
source_raw:
  - Raw/Get笔记-AI大佬Andrej Karpathy三年经验提炼：15个核心技能解析.md
  - Raw/GitHub-LearnPrompt-andrej-karpathy-skills-19fc6870.md
---

# 把Karpathy三年经验做成15个Skills

## 这个案例解决什么问题

这条材料最初来自 Get笔记保存的视频号卡片，后来已定位到对应仓库：`LearnPrompt/andrej-karpathy-skills`。

它不是 Karpathy 官方仓库，而是 LearnPrompt 对 Karpathy 近几年公开分享的二次整理：把 AI、agent、vibe coding、Software 3.0、knowledge base 等主题，重新拆成一组可复用的 `skills`。

它对这个 vault 的价值不在于“已经拿到了 15 个 skill 的全文”，而在于提供了一个可复用的知识产品包装方式：

```text
权威人物 / 高质量长期内容
  -> 提取反复出现的方法和判断
  -> 拆成可命名、可调用、可教学的 skills
  -> 做成视频号 / 课程 / 知识库 / skill 包
```

## 当前证据能确认什么

来源包括两层：

- Get笔记对视频号卡片的保存，原始链接为 `https://weixin.qq.com/sph/AjwKRO0TUk`。
- GitHub 仓库 `LearnPrompt/andrej-karpathy-skills`，快照 commit 为 `19fc6870b1d2abc51562f2359a0c4805d9641e21`。

能确认的信息：

- 主题：`把Andrej Karpathy这三年做成了15个skills`。
- 实际仓库结构：`14` 个核心 skill，加 `1` 个总控路由 `karpathy-methodology`，因此视频号里的 `15个skills` 可以理解为 `14 + 1`。
- 标签：`#Agent`、`#skill`、`#AI工具`、`#AI教程`、`#Karpathy`、`#AI学习`、`#OpenClacky`、`#知识库`、`#人工智能`。
- 发布时间：2026年5月25日。
- 互动数据：点赞 283、转发 268、评论 195、收藏 27。
- 作者 / 账号线索：`卡尔的AI沃茨`。

仍需谨慎的信息：

- 这是 LearnPrompt 的二次整理，不是 Karpathy 官方 skill 包。
- 每个 skill 对应的 X 帖、点赞数和上下文仍需要按需回查原始来源。
- README 说 `14 个 Skill`，文件树有 `15` 个目录；这个差异来自 `karpathy-methodology` 是总控路由。

仓库级详细编译见：[[Wiki/Vibe Coding/60-Agent Skills/LearnPrompt Karpathy Skills仓库|LearnPrompt Karpathy Skills仓库]]。

## 可复用的方法框架

如果后续要把它发展成教程或课程，可以按下面流程操作。

### 1. 先收集 Karpathy 原始材料

优先收这些材料，而不是只看二次剪辑：

- `Software 3.0` 相关演讲、访谈和文章。
- `Vibe Coding`、`Agentic Engineering` 相关访谈。
- Karpathy 关于 `LLM OS`、`jagged intelligence`、`verifiability`、`context engineering` 的公开内容。
- 他的 repo、课程、tweet / X 长帖、YouTube 讲解。

这些材料进入 `Clippings/` 或 `Raw/` 后，再编译到 [[Wiki/AI行业判断/从VibeCoding到AgenticEngineering|从Vibe Coding到Agentic Engineering]] 和 Vibe Coding 路线图。

### 2. 把观点拆成 skill 候选

拆 skill 时不要按“概念”拆，而要按“用户能不能照做”拆。

好的 skill 候选应该能回答：

- 触发场景：用户什么时候会用它？
- 输入：需要给 agent 什么材料？
- 步骤：agent 应该按什么流程处理？
- 输出：最后应该交付什么？
- 验证：怎么知道结果不是胡编？
- 边界：什么时候不能自动化，需要人判断？

仓库已经把候选方向落成了以下核心 skill：

| Skill 方向 | 可能解决的问题 | 对本 vault 的价值 |
| --- | --- | --- |
| `karpathy-agentic-engineering` | 如何给 agent 明确上下文、成功标准和小步 diff | 补强 AI 编程质量线 |
| `karpathy-vibe-to-agentic` | 如何从能跑 demo 进入可上线工程 | 对接 Vibe Coding 路线图 |
| `karpathy-llm-wiki` | 如何把长文和视频重编译成可问可用的 Wiki | 直接对接当前 vault 工作流 |
| `karpathy-understanding-first` | 人在 AI 工作流里保留哪些理解与判断 | 对接“不要外包你的学习” |
| `karpathy-output-evolution` | 如何把文本输出升级成 HTML、PPT、dashboard | 对接 Outputs 生产 |

### 3. 把 skill 做成可交付产物

这个案例最终可以导向三类产物：

- `Wiki/Vibe Coding/60-Agent Skills`：整理 `Karpathy 风格 AI Skills` 的候选清单和边界。
- `Outputs/SOP与模板`：生成“把大 V 方法论拆成 agent skills 的 SOP”。
- `Outputs/课程与训练营`：做一个“从 Karpathy 思想到 AI 应用落地技能”的课程模块。

## 适合谁

适合：

- 想把 AI 大佬观点翻译成普通人可执行教程的人。
- 想设计自己 `SKILL.md`、agent workflow 或课程练习的人。
- 想做 AI 编程 / agent skills 内容选题的人。
- 想把零散视频、访谈、文章沉淀成知识库和课程的人。

不适合：

- 想把它当成 Karpathy 官方 skill 包的人。
- 想只看一条视频或一个二次整理仓库就得出完整方法论的人。
- 需要严格引用 Karpathy 原话的正式文章；当前仓库仍需要回查原始 X / Gist / 访谈来源。

## 常见坑

- 把“15 个 skills”的标题当成已经验证的技能清单。
- 用 Karpathy 背书二次作者的所有观点，导致权威错配。
- 只做概念总结，不写输入、步骤、输出和验证。
- 直接生成 Outputs，而没有先把原始材料编译进 Wiki。
- 忽略时效性：这条视频号发布于 2026年5月25日，互动数据和链接可访问性都可能变化。

## 后续深挖清单

- 继续回查每个 skill 对应的 Karpathy 原始 X / Gist / 访谈，区分原始观点与二次整理。
- 把 15 个 skill 与现有 [[Wiki/Vibe Coding/60-Agent Skills/Agent Skills仓库索引|Agent Skills仓库索引]] 对照，判断哪些是工程 skill，哪些是内容 / 学习 / 知识库 skill。
- 把可验证的 skill 候选补进 [[Wiki/Vibe Coding/00-Overview/Vibe Coding专题路线图|Vibe Coding专题路线图]] 的 `Use skills created by others`、`Prompting Best Practices` 和 `Context` 节点。

## 来源

- [[Raw/Get笔记-AI大佬Andrej Karpathy三年经验提炼：15个核心技能解析|Get笔记：AI大佬Andrej Karpathy三年经验提炼：15个核心技能解析]]
- [[Raw/GitHub-LearnPrompt-andrej-karpathy-skills-19fc6870|GitHub：LearnPrompt/andrej-karpathy-skills]]
- [[Wiki/Vibe Coding/60-Agent Skills/LearnPrompt Karpathy Skills仓库|LearnPrompt Karpathy Skills仓库]]
