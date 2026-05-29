---
type: raw_github_repo_snapshot
repo: LearnPrompt/andrej-karpathy-skills
url: https://github.com/LearnPrompt/andrej-karpathy-skills
commit: 19fc6870b1d2abc51562f2359a0c4805d9641e21
captured_at: 2026-05-25
license: MIT
status: compiled
compile_status: compiled
compiled_to:
  - "Wiki/Vibe Coding/60-Agent Skills/LearnPrompt Karpathy Skills仓库.md"
  - "Wiki/Vibe Coding/60-Agent Skills/把Karpathy三年经验做成15个Skills.md"
  - "Wiki/Vibe Coding/60-Agent Skills/Agent Skills仓库索引.md"
remaining_value: medium
tags:
  - AgentSkills
  - Andrej Karpathy
  - Vibe Coding
  - Agentic Engineering
---

# GitHub Snapshot: LearnPrompt/andrej-karpathy-skills

来源：<https://github.com/LearnPrompt/andrej-karpathy-skills>  
快照 commit：`19fc6870b1d2abc51562f2359a0c4805d9641e21`

## 仓库定位

README 将该项目定位为：

- 从 Andrej Karpathy 近三年公开分享中，提炼出每天能用的 AI 工作方法。
- 不是语录摘抄，而是把工作习惯整理成 Agent 能执行的 `Skill` 指南。
- README 写作口径是 `14 个 Skill`，但仓库实际包含 `15` 个 `karpathy-*` 目录：`14` 个核心方法，加 `karpathy-methodology` 总控路由。
- 这些 skill 被组织成 4 条工作流：
  - 代码开发：`idea-files -> agentic-engineering -> minimalism -> supply-chain-hygiene -> vibe-to-agentic`
  - 内容创作：`autoresearch -> llm-wiki -> output-evolution -> education-first`
  - 头脑风暴 / 决策：`llm-simulator -> understanding-first -> system-prompt-learning`
  - 月度职业健康自查：`meta-reflection -> understanding-first -> practice-environments -> education-first`

## 文件树

```text
LICENSE
README.md
install.sh
karpathy-agentic-engineering/SKILL.md
karpathy-autoresearch/SKILL.md
karpathy-education-first/SKILL.md
karpathy-idea-files/SKILL.md
karpathy-llm-simulator/SKILL.md
karpathy-llm-wiki/SKILL.md
karpathy-meta-reflection/SKILL.md
karpathy-methodology/SKILL.md
karpathy-methodology/references/index.md
karpathy-minimalism/SKILL.md
karpathy-output-evolution/SKILL.md
karpathy-practice-environments/SKILL.md
karpathy-supply-chain-hygiene/SKILL.md
karpathy-system-prompt-learning/SKILL.md
karpathy-understanding-first/SKILL.md
karpathy-vibe-to-agentic/SKILL.md
```

## Skill 清单

| Skill | 仓库内标题 | 核心用途 | 工作流 |
| --- | --- | --- | --- |
| `karpathy-methodology` | Karpathy Methodology — 14 Core Skills | 总控路由：不知道用哪个方法时从这里进入 | 路由 |
| `karpathy-agentic-engineering` | Agentic Engineering（代理工程） | 用成功标准、上下文和小步 diff 指挥 agent 编码 | A 想法到上线 |
| `karpathy-llm-wiki` | LLM Wiki / Personal Knowledge Base（LLM知识库） | 把探索材料沉淀成 LLM 可维护的个人 Wiki | B 研究到发布 |
| `karpathy-llm-simulator` | LLM as Simulator（LLM模拟器思维） | 让 LLM 模拟多方专家争论，减少单一回答的讨好偏差 | C 反偏见决策 |
| `karpathy-minimalism` | Minimalism & Agent-Native Design（极简主义 + 代理原生设计） | 减依赖、降复杂度、让工具更 agent-native | A 想法到上线 |
| `karpathy-vibe-to-agentic` | Vibe Coding -> Agentic Leap（Vibe编码 -> 代理跃迁） | 把“能跑的原型”升级成可验证、可维护的工程 | A 想法到上线 |
| `karpathy-autoresearch` | AutoResearch（自主研究循环） | 让 agent 在 git 分支上跑实验、记录指标、提出下一轮假设 | B 研究到发布 |
| `karpathy-output-evolution` | Output Evolution（输出形式进化） | 从纯文本输出升级到 Markdown、HTML、slides、dashboard | B 研究到发布 |
| `karpathy-understanding-first` | Understanding > Outsourcing（理解 > 外包） | 审计自己是否真正理解 AI 生成的东西 | C / D |
| `karpathy-idea-files` | Idea Files / Gist-First Sharing（想法文件优先） | 先写想法 spec 和成功标准，再交给 agent 或他人实现 | A 想法到上线 |
| `karpathy-meta-reflection` | Meta-Reflection（元反思） | 每月检查哪些能力在退化、哪些需要继续练 | D 月度体检 |
| `karpathy-supply-chain-hygiene` | Supply Chain & Security Hygiene（供应链安全卫生） | 审查依赖、pin version、减少供应链攻击面 | A 想法到上线 |
| `karpathy-education-first` | Education-First Mindset（教育至上） | 把项目和经验做成新手能学的 nano-project / 教程 | B / D |
| `karpathy-system-prompt-learning` | System Prompt Learning（系统提示学习范式） | 把策略写进 system prompt，像写教材一样训练 agent 行为 | C 反偏见决策 |
| `karpathy-practice-environments` | LLM Textbook + Practice Environments（LLM教科书 + 练习环境） | 为 agent 建立可试错、可反馈、可评估的练习环境 | D 月度体检 |

## 安装脚本观察

`install.sh` 默认安装到：

```bash
~/.clacky/skills
```

这不是当前 Codex 会话加载个人 skill 的 `~/.agents/skills`。如果要给 Codex 使用，需要手动复制这些 `karpathy-*` 目录到 `~/.agents/skills`，或使用支持 Codex 目标目录的 skill 安装器。

## 来源与限制

- README 声称这些方法来自 Karpathy 2023-2026 年公开分享、X 高赞帖、LLM Wiki Gist，以及相关社区 repo。
- 这是 LearnPrompt 的二次整理，不等同于 Karpathy 官方发布的 skill 包。
- 多个 skill 依赖 X 帖作为来源，链接、点赞数和上下文都具有时效性。
- 仓库 license 为 MIT。
