---
type: wiki
status: compiled
area: Vibe Coding
tags:
  - AgentSkills
  - AndrejKarpathy
  - VibeCoding
  - AgenticEngineering
  - LLMWiki
updated: 2026-05-25
source_raw:
  - Raw/GitHub-LearnPrompt-andrej-karpathy-skills-19fc6870.md
  - Raw/Get笔记-AI大佬Andrej Karpathy三年经验提炼：15个核心技能解析.md
repo: https://github.com/LearnPrompt/andrej-karpathy-skills
commit: 19fc6870b1d2abc51562f2359a0c4805d9641e21
---

# LearnPrompt Karpathy Skills仓库

## 这个仓库是什么

`LearnPrompt/andrej-karpathy-skills` 是一个把 Andrej Karpathy 近几年公开分享二次整理成 agent skills 的仓库。它不是 Karpathy 官方仓库，而是 LearnPrompt 对 Karpathy 方法论的产品化整理。

仓库 README 说是 `14 个 Skill`，实际文件树里有 `15` 个 `karpathy-*` skill 目录：

- `14` 个核心方法。
- `1` 个总控路由：`karpathy-methodology`，用于根据任务选择合适的子 skill。

这正好解释了之前 Get笔记里“15个skills”的来源：更准确地说，是 `14 个核心 skill + 1 个 methodology router`。

## 为什么值得编译

它对这个 vault 的价值有三层：

- **AI 编程层**：把 vibe coding、agentic engineering、minimalism、supply-chain hygiene 组织成“想法到上线”的工程链路。
- **知识库层**：`llm-wiki` 和 `idea-files` 与当前 `Raw / Clippings -> Wiki -> Outputs` 工作流高度契合。
- **课程与内容层**：`education-first`、`output-evolution`、`system-prompt-learning` 可以直接转成课程练习、SOP、图文卡片和 prompt 模板。

## 4 条工作流

| 工作流 | 链路 | 适合谁 | 产出 |
| --- | --- | --- | --- |
| 想法到上线 | `idea-files -> agentic-engineering -> minimalism -> supply-chain-hygiene -> vibe-to-agentic` | 独立开发者、AI 编程新手、产品原型开发者 | spec、代码、测试、依赖审计、原型升级清单 |
| 研究到发布 | `autoresearch -> llm-wiki -> output-evolution -> education-first` | 内容创作者、研究型学习者、课程作者 | 实验记录、Wiki 页面、HTML / slides、教程 |
| 反偏见决策 | `llm-simulator -> understanding-first -> system-prompt-learning` | 做重要技术 / 产品 / 商业判断的人 | 多角色辩论、理解审计、沉淀后的 system prompt |
| 月度体检 | `meta-reflection -> understanding-first -> practice-environments -> education-first` | 长期使用 AI 的个人和团队 | 技能退化审计、练习环境、教学化复盘 |

## Skill 清单与落地价值

| Skill                             | 用中文怎么理解      | 什么时候用                              | 可沉淀到本 vault 的位置               |
| --------------------------------- | ------------ | ---------------------------------- | ----------------------------- |
| `karpathy-methodology`            | 总控路由         | 不知道该用哪个 Karpathy 方法时               | `Wiki/Vibe Coding/60-Agent Skills` 的入口页 |
| `karpathy-agentic-engineering`    | 代理工程         | 要让 agent 小步写代码、写 AGENTS.md、定义成功标准  | Vibe Coding 路线图、Vibe Coding SOP |
| `karpathy-llm-wiki`               | LLM 知识库      | 要把论文、文章、视频编译成 Wiki                 | AI知识库专题、本 vault 工作流           |
| `karpathy-llm-simulator`          | 模拟器思维        | 要让 AI 模拟专家辩论、反驳方案                  | 决策 SOP、产品方案评审                 |
| `karpathy-minimalism`             | 极简与少依赖       | 项目依赖过重、工具链太复杂                      | AI 编程质量线、依赖选择指南               |
| `karpathy-vibe-to-agentic`        | 从 vibe 原型到工程 | 已有能跑但不敢上线的原型                       | 原型升级检查清单                      |
| `karpathy-autoresearch`           | 自主研究循环       | 要跑多轮实验、prompt 优化、竞品矩阵测试            | 研究工作流、实验记录模板                  |
| `karpathy-output-evolution`       | 输出形态进化       | 要从纯文本变成 HTML、PPT、dashboard         | Outputs 生产流程                  |
| `karpathy-understanding-first`    | 理解优先         | AI 已经生成结果，但人不确定自己懂不懂               | 不外包学习、代码 review、学习 SOP        |
| `karpathy-idea-files`             | 想法文件优先       | 还没实现前，先把 idea 写成 spec              | PRD、issue、agent 任务说明          |
| `karpathy-meta-reflection`        | 元反思          | 每月检查 AI 使用后自己的能力变化                 | 个人 AI 能力复盘                    |
| `karpathy-supply-chain-hygiene`   | 供应链安全        | npm / pip 依赖太多，准备上线前审查             | 安全检查清单                        |
| `karpathy-education-first`        | 教育优先         | 把项目、代码、经验做成新手可学教程                  | 教程、课程、训练营                     |
| `karpathy-system-prompt-learning` | 系统提示学习       | 要把经验写成稳定可复用的 prompt / agent 规则     | skill 写作、AGENTS.md、系统 prompt  |
| `karpathy-practice-environments`  | 练习环境         | 要给 agent 或人建立可反复试错的 eval / sandbox | eval、练习题、训练营作业                |
|                                   |              |                                    |                               |

## 最适合先复用的 5 个

对当前“AI 应用落地 vault”来说，优先级最高的是：

1. `karpathy-llm-wiki`：可以直接强化当前 `Raw / Clippings -> Wiki -> Outputs` 流程。
2. `karpathy-idea-files`：适合把用户想法变成 agent 可执行 spec。
3. `karpathy-vibe-to-agentic`：适合把“AI 搓出来的 demo”升级成可交付项目。
4. `karpathy-understanding-first`：和“不要外包你的学习”同一条主线。
5. `karpathy-output-evolution`：能把 Wiki 转成 HTML、PPT、图文卡片等交付品。

## 使用时的判断

这个仓库适合当“可执行方法库”，不适合当权威原文。

使用建议：

- 如果要写教程，可以引用它的 skill 结构，但关键观点最好回查 Karpathy 原始 X / Gist / 访谈。
- 如果要装到 Codex，要注意 `install.sh` 默认写入 `~/.clacky/skills`，不是 `~/.agents/skills`。
- 如果要改造成自己的 skill，不要照搬标题；要把触发场景、输入、步骤、输出、验证和边界改成本 vault 的使用方式。
- 如果用来教新手，先用工作流，不要让用户一次面对 15 个入口。

## 可生成的 Outputs

- 工具比较：`Karpathy Skills vs Matt Pocock Skills：一个偏方法论，一个偏工程纪律`。
- SOP：`把大 V 方法论拆成 agent skill 的流程`。
- 课程模块：`从 Vibe Coding 到 Agentic Engineering 的 5 个练习`。
- 图文卡片：`14 + 1 Karpathy Skills 地图`。
- 指令模板：`理解审计 / idea file / 原型升级 / 输出进化`。

## 来源

- GitHub 仓库：<https://github.com/LearnPrompt/andrej-karpathy-skills>
- 本地 Raw 快照：[[Raw/GitHub-LearnPrompt-andrej-karpathy-skills-19fc6870|GitHub-LearnPrompt-andrej-karpathy-skills-19fc6870]]
- 触发线索：[[Raw/Get笔记-AI大佬Andrej Karpathy三年经验提炼：15个核心技能解析|Get笔记：AI大佬Andrej Karpathy三年经验提炼]]
