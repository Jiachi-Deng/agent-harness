---
type: wiki
status: compiled
area: Vibe Coding
tags:
  - AgentSkills
  - MattPocock
  - ClaudeCode
  - Codex
  - AI编程
  - VibeCoding
updated: 2026-05-25
source_clipping: "Clippings/mattpocockskills Skills for Real Engineers. Straight from my .claude directory..md"
source_url: "https://github.com/mattpocock/skills/blob/main/README.md"
verified_commit: "b8be62ffacb0118fa3eaa29a0923c87c8c11985c"
verified_commit_date: 2026-05-20
license: MIT
---

# Matt Pocock Skills仓库

## 当前判断

`mattpocock/skills` 是一套偏“真实工程纪律”的 agent skills 仓库。它的核心价值不是让 AI 更会写代码，而是让 agent 在真实项目里更少乱来：先问清楚、用项目语言说话、按 issue / PRD / TDD / 调试 / 架构 review 这些反馈回路工作。

它特别适合：

- 已经在用 Claude Code、Codex、Cursor、Windsurf 等工具做真实项目的人。
- 有 Git、issue tracker、测试、文档、ADR、代码 review 习惯的团队或独立开发者。
- 觉得普通 vibe coding 太容易失控，想把 agent 拉回“小步、可验证、可回滚”的工程流程的人。

不太适合：

- 只想生成一次性 demo 的新手。
- 没有 Git / issue / 测试习惯，也不愿意先做项目设置的人。
- 希望一个大型框架接管整个开发流程的人。这套仓库更像小工具箱，不是 GSD / BMAD / Spec-Kit 那种重流程。

## 来源和快照

- Clipping：[[Clippings/mattpocockskills Skills for Real Engineers. Straight from my .claude directory.|mattpocock/skills: Skills for Real Engineers]]
- GitHub：`https://github.com/mattpocock/skills`
- 本次核对快照：`b8be62ffacb0118fa3eaa29a0923c87c8c11985c`，commit 日期 `2026-05-20`
- License：MIT
- 安装入口：README 推荐 `npx skills@latest add mattpocock/skills`

注意：README 的 Reference 主要列出 `engineering`、`productivity`、`misc`。本页按仓库文件树把 `deprecated`、`in-progress`、`personal` 也列出，但会标清状态。

## 仓库结构

| 目录 | 状态 | 数量 | 怎么理解 |
| --- | --- | ---: | --- |
| `skills/engineering` | 核心工程 skill | 10 | 日常写代码、调试、架构、TDD、issue / PRD 管理的主力 |
| `skills/productivity` | 通用效率 skill | 4 | 适合非代码场景：压缩表达、追问需求、handoff、写 skill |
| `skills/misc` | 杂项工具 | 4 | 作者保留但不常用，偏安全钩子、课程脚手架、pre-commit、测试数据迁移 |
| `skills/in-progress` | 进行中 | 4 | 还在开发，可能有粗糙边界、破坏性变更或被废弃 |
| `skills/personal` | 个人环境 | 2 | 绑定作者自己的写作和 Obsidian 习惯，不适合直接照搬 |
| `skills/deprecated` | 已废弃 | 4 | 作者不再使用，适合学习设计思路，不建议直接作为正式流程 |

## 核心工程 Skills

| Skill | 干嘛的 | 什么时候用 | 怎么用 | 产出 / 注意点 |
| --- | --- | --- | --- | --- |
| `setup-matt-pocock-skills` | 给当前 repo 建立这些 skill 依赖的上下文配置：issue tracker、triage 标签、domain docs | 第一次在某个 repo 用这套工程 skill 前；或 agent 不知道 issue/标签/文档位置时 | 运行后让 agent 检查 `AGENTS.md` / `CLAUDE.md`、`CONTEXT.md`、`docs/adr/`、Git remote，再逐项确认配置 | 会更新 `AGENTS.md` 或 `CLAUDE.md` 的 `Agent skills` 区块，并生成 `docs/agents/` 说明；这是后续 `triage`、`to-issues`、`to-prd` 的前置基础 |
| `grill-with-docs` | 围绕一个计划持续追问，同时把领域词汇写入 `CONTEXT.md`，把重要决策写成 ADR | 开新功能、重构、架构方案还不清楚时 | 让 agent 一个问题一个问题追问；能从代码回答的就先查代码；术语确定后立即写入文档 | 适合防止“你以为 AI 懂了，其实没懂”；会改变项目文档，使用前要接受文档随讨论增长 |
| `diagnose` | 硬 bug / 性能问题的纪律化排查流程 | 报错反复修不好、性能退化、非确定性 bug、agent 开始猜的时候 | 先建可运行反馈回路，再复现、列假设、加定向日志或探针、修复、补回归测试、清理日志 | 重点是先有 pass/fail loop；如果不能复现，它会要求补日志、HAR、录屏或环境访问，而不是继续瞎猜 |
| `tdd` | 让 agent 用 red-green-refactor 做功能或 bug 修复 | 行为可测试、需要控制回归风险、想让 AI 小步实现时 | 先确认 public interface 和关键行为；一次只写一个失败测试，再写最小代码通过，然后循环 | 反对一次性写一堆测试再写一堆实现；更适合真实业务行为测试，不适合纯临时脚本 |
| `to-prd` | 把当前对话和代码理解整理成 PRD，并发布到 issue tracker | 已经讨论了一段需求，想沉淀成可执行 PRD 时 | 不再大规模访谈，而是综合当前上下文、代码结构、模块影响、测试决定 | 输出 PRD issue，包含问题、方案、用户故事、实现决定、测试决定和 out of scope |
| `to-issues` | 把计划 / PRD 拆成可独立领取的 issues | PRD 已有，准备让人或 agent 分批实现时 | 按 vertical slice 拆分，而不是按前端/后端/数据库横切；让用户确认粒度和依赖后发布 | 每个 issue 都应能独立验证；会标注 HITL / AFK，帮助判断哪些能交给 agent |
| `triage` | 通过状态机管理 issue：分类、补信息、准备 agent 接手、关闭 | 有一堆 bug / feature request，需要判断优先级和可执行性时 | 读取 issue、评论、标签和代码上下文；推荐 category + state；必要时进入 grilling | 依赖 `setup` 里的标签映射；会给 issue 加 triage 说明或 agent brief，适合维护队列 |
| `improve-codebase-architecture` | 找代码里的架构摩擦和“浅模块”，提出深模块化机会 | agent 做久了代码变乱、模块难测、改一处牵一片时 | 读取 `CONTEXT.md` 和 ADR，探索代码，生成 HTML 架构报告，再让用户选一个候选继续追问 | 不是自动重构；它先做诊断和候选报告。适合周期性运行，防止 AI 加速代码腐化 |
| `zoom-out` | 让 agent 上升一层解释某块代码在系统里的位置 | 不熟悉某个模块、准备动代码前需要地图时 | 触发后要求 agent 用项目领域词汇说明相关模块、调用方和整体关系 | 适合改代码前“先看全局”；该 skill 本身很短，像一个强制切换视角的提醒 |
| `prototype` | 做可丢弃原型，用来回答设计问题 | 数据模型、状态机、UI 方向拿不准，需要先玩一下时 | 根据问题分支：逻辑问题做终端小程序；UI 问题做可切换的多方案页面 | 原型从第一天就应标明可删除；结束后只保留结论，别让临时代码腐烂在项目里 |

## Productivity Skills

| Skill | 干嘛的 | 什么时候用 | 怎么用 | 产出 / 注意点 |
| --- | --- | --- | --- | --- |
| `grill-me` | 通用版需求追问，不依赖代码文档 | 产品想法、文章想法、方案设计还模糊时 | 让 agent 一次问一个问题，并给推荐答案，直到决策树走清楚 | 适合非代码场景；如果是代码项目且要更新文档，优先用 `grill-with-docs` |
| `caveman` | 超短表达模式，减少废话和 token | 用户明确要求少说、短答、caveman mode 时 | 触发后持续用极短句回答，直到用户关闭 | 适合高频工程对话；安全提醒、不可逆操作、多步骤澄清时会临时恢复清晰表达 |
| `handoff` | 把当前会话压缩成下一位 agent 可接手的交接文档 | 长任务中断、换 agent、需要保留现场时 | 说明下一次会话用途；agent 在系统临时目录写 handoff，并列出建议使用的 skills | 会引用已有 PRD、issue、diff、文档路径，避免重复；需要遮蔽敏感信息 |
| `write-a-skill` | 帮用户创建新的 agent skill | 一个流程反复出现，想固化成 `SKILL.md` 时 | 先问适用任务、触发场景、是否需要脚本/参考材料，再生成 skill 结构 | 适合把满意的一次 agent 工作沉淀为可复用资产；复杂内容应拆到 references / scripts |

## Misc Skills

| Skill | 干嘛的 | 什么时候用 | 怎么用 | 产出 / 注意点 |
| --- | --- | --- | --- | --- |
| `git-guardrails-claude-code` | 给 Claude Code 配安全 hook，拦截危险 Git 命令 | 担心 agent 执行 `git push`、`reset --hard`、`clean` 等破坏性命令时 | 选择项目级或全局级，复制 hook 脚本，写入 `.claude/settings.json` 或 `~/.claude/settings.json` | 只针对 Claude Code hook 机制；Codex 需要另行设计等价 guardrail |
| `setup-pre-commit` | 配 Husky、lint-staged、Prettier、typecheck、test 的 pre-commit | JS/TS 项目想在提交前自动格式化和跑检查时 | 识别包管理器，安装依赖，初始化 Husky，写 pre-commit 和 lint-staged 配置 | 适合已有 npm/pnpm/yarn/bun 项目；对大型测试套件要注意 commit 速度 |
| `migrate-to-shoehorn` | 把测试里的 `as` 类型断言迁移到 `@total-typescript/shoehorn` | TypeScript 测试里为了造数据到处 `as Type` 时 | 安装 `@total-typescript/shoehorn`，按对象场景替换成 `fromPartial()` 或 `fromAny()` | 只用于测试代码；不应该进 production code |
| `scaffold-exercises` | 生成课程练习目录、problem / solution / explainer 结构 | 做课程、练习题、训练营内容时 | 按编号和命名规范创建 exercise 目录，并保证 readme 不空、lint 可过 | 强绑定作者课程仓库习惯，对普通 app 项目价值有限 |

## In-progress Skills

| Skill | 干嘛的 | 什么时候用 | 怎么用 | 产出 / 注意点 |
| --- | --- | --- | --- | --- |
| `review` | 从某个 commit / branch 起，按 Standards 和 Spec 两条线 review diff | PR / 分支 / WIP 想检查是否符合规范和需求时 | 指定固定点，如 `main` 或 commit；它找 spec、找 standards，然后用并行 sub-agents 分别审查 | 还在开发中。思路很值得学：把“符合项目规范”和“符合需求”拆开，不互相掩盖 |
| `writing-fragments` | 通过追问收集写作碎片，先不强行组织结构 | 作者有想法但还没形成文章时 | 让 agent 持续追问并把可用片段追加进同一个 Markdown 文件 | 偏写作工作流，不是工程 skill；适合知识库材料积累 |
| `writing-shape` | 把一堆 raw material 逐段塑造成文章 | 已有素材堆，需要变成可发布文章时 | 读完整 raw file，先选开头，再一段一段写入文章文件，过程中讨论格式选择 | 对我们的 `Clippings -> Wiki -> Outputs` 有启发，但当前是实验状态 |
| `writing-beats` | 把文章当成 beat-by-beat 的旅程来写 | 想写叙事型、体验型文章，不是论证型文章时 | 每次只写一个 beat，用户从 2-3 个下一步中选择方向 | 更像写作教练；适合内容创作，不适合工程任务 |

## Personal Skills

| Skill | 干嘛的 | 什么时候用 | 怎么用 | 产出 / 注意点 |
| --- | --- | --- | --- | --- |
| `edit-article` | 按信息依赖关系重排并润色文章 | 有文章草稿，需要更清晰、更紧凑时 | 先按标题分 section，确认顺序，再逐段改写，要求段落很短 | 个人写作偏好明显；可借鉴，但不应原样套到所有中文文章 |
| `obsidian-vault` | 管理作者自己的 Obsidian vault | 在作者固定 vault 路径里找笔记、建索引、建 wikilink 时 | 用固定路径、Title Case 文件名、扁平索引规则操作笔记 | 强绑定作者本地路径，不适合直接安装；对我们知识库的启发是“索引页 + wikilinks” |

## Deprecated Skills

| Skill | 原本干嘛 | 为什么仍值得记录 | 替代方向 |
| --- | --- | --- | --- |
| `design-an-interface` | 并行生成多个模块接口设计，再比较取舍 | 体现了“不要接受第一个接口”的设计思想 | 当前可用 `prototype` 或 `improve-codebase-architecture` 的 interface exploration 思路替代 |
| `qa` | 让用户口头报 bug，agent 轻量澄清并创建 GitHub issue | 适合学习“QA 会话转 issue”的流程 | 更正式的 issue 流程应看 `triage` |
| `request-refactor-plan` | 访谈式生成 refactor plan，并拆成很小的 commits | 对“重构要小步提交”有价值 | 现在可用 `to-prd`、`to-issues`、`improve-codebase-architecture` 组合替代 |
| `ubiquitous-language` | 从对话提取 DDD glossary，写入 `UBIQUITOUS_LANGUAGE.md` | 说明 shared language 对 agent 很关键 | 现在这部分能力被 `grill-with-docs` 和 `CONTEXT.md` 吸收 |

## 使用顺序建议

### 新项目第一次接入

```text
setup-matt-pocock-skills
  -> grill-with-docs
  -> to-prd
  -> to-issues
  -> tdd / diagnose / triage
```

### bug 修复

```text
zoom-out
  -> diagnose
  -> tdd
  -> handoff
```

### 代码开始变乱

```text
zoom-out
  -> improve-codebase-architecture
  -> grill-with-docs
  -> to-issues
```

### 自建 skill

```text
先手动跑通一次流程
  -> handoff 总结经验
  -> write-a-skill 固化
  -> 放入自己的全局或项目 skills
```

## 对我们的知识库有什么启发

1. Skill 不是越大越好。它应该把一个高频、可复用、可验证的工作流压缩成清晰触发条件。
2. 工程类 skill 最有价值的不是“让 AI 写更多代码”，而是给 AI 加反馈回路：issue、spec、test、logs、domain docs、ADR。
3. 未来我们收其他 skill 仓库时，要区分“正式推荐”和“仓库里碰巧存在的实验/个人/废弃 skill”。
4. 对 Vibe Coding 新手来说，最值得先学的是 `grill-with-docs`、`diagnose`、`tdd`、`handoff`、`write-a-skill` 这几类方法，而不是一次性安装所有 skill。

## 可生成的 Outputs

- 教程：如何把一个真实项目接入 Matt Pocock Skills。
- SOP：AI 编程项目的 `setup -> PRD -> issues -> TDD -> diagnose` 工作流。
- 工具比较：Matt Pocock Skills vs BMAD / Spec-Kit / GSD。
- 图文卡片：从 vibe coding 到 real engineering 的 skill 组合路线。
