---
type: wiki
status: compiled
area: Vibe Coding
tags:
  - AgentSkills
  - AI编程
  - VibeCoding
  - ClaudeCode
  - Codex
updated: 2026-05-28
---

# Agent Skills仓库索引

## 这个专题维护什么

这个专题专门收集和比较可复用的 agent skills 仓库。它不把 skill 当成普通 prompt 库，而是当成一组可以沉淀工程流程、内容流程、调试流程和个人工作流的轻量“操作系统插件”。

后续凡是进入 `Clippings/` 或 `Raw/` 的 skill 仓库，优先在这里登记，再视材料质量拆成独立 Wiki 页面。

## 收录时看什么

每个 skill 仓库至少记录：

- 仓库定位：偏工程、内容、运营、设计、数据、个人效率，还是混合型。
- 安装方式：是否支持 `skills.sh`、Claude Code、Codex、手动复制。
- skill 数量和生命周期：正式、实验中、个人用、已废弃。
- 每个 skill 的用途、触发场景、输入、输出和注意事项。
- 是否有脚本、模板、参考文件、hooks、外部依赖。
- 是否适合新手直接使用，还是需要项目已有 issue tracker、测试、文档和 Git 习惯。
- 能否启发我们自建 skill，或者直接纳入自己的 Codex / Claude Code 全局技能库。

## 当前已收录

| 仓库 | 定位 | 当前判断 | 详细页 |
| --- | --- | --- | --- |
| `mattpocock/skills` | 面向真实软件工程的 agent skills：需求澄清、文档化、TDD、调试、架构、issue 拆分、handoff 等 | 高价值。更适合有真实项目、Git、issue tracker 和测试意识的用户；不是“一句话生成 app”的 vibe coding prompt，而是把 agent 拉回工程纪律 | [[Matt Pocock Skills仓库|Matt Pocock Skills仓库]] |
| `LearnPrompt/andrej-karpathy-skills` | 把 Karpathy 公开分享二次整理成 14 个核心方法 + 1 个总控路由，覆盖 agentic engineering、LLM wiki、vibe-to-agentic、理解审计、输出进化等 | 高价值，但要标注为 LearnPrompt 二次整理，不是 Karpathy 官方 skill 包。更适合做方法论、课程和 SOP，不如 Matt Pocock skills 那样贴近真实 repo 工程流程 | [[LearnPrompt Karpathy Skills仓库|LearnPrompt Karpathy Skills仓库]] |

## 内容型 skill 案例线索

| 线索 | 定位 | 当前判断 | 详细页 |
| --- | --- | --- | --- |
| `把Karpathy三年经验做成15个Skills` | 把权威人物长期观点拆成可教学、可调用的 skills 的内容产品案例 | 已定位到 `LearnPrompt/andrej-karpathy-skills`：实际是 14 个核心 skill + 1 个 `karpathy-methodology` 总控路由 | [[Wiki/Vibe Coding/60-Agent Skills/把Karpathy三年经验做成15个Skills|把Karpathy三年经验做成15个Skills]] |

## Skill 设计原则

Perplexity 的公开 guide 适合补成本专题的 skill 设计标准。它强调：skill 不是普通 prompt，也不是把 README 写长，而是一种会被 agent 在运行时选择、加载、按需展开的能力包。

`Master 97% of Codex in 1 Hour` 则提供了新手更容易理解的封装顺序：先让 Codex 手工完成一次 YouTube 评论抓取、分析和 Excel 报告；确认产物满意后，再要求它把这套流程变成 `YouTube comment insights` skill。也就是说，skill 最好来自已经跑通过的工作流，而不是凭空写一份“万能说明书”。

### 什么时候需要 skill

需要 skill 的情况：

- agent 没有专门上下文时会反复做错。
- 团队有稳定流程、标准判断、工具调用顺序或合规边界要复用。
- 某个工作需要 gotchas、负面例子和项目偏好，而不是通用知识。
- 产物需要跨会话、跨项目、跨模型保持一致。

不需要 skill 的情况：

- 只是模型本来就知道的命令或概念。
- 工具界面、价格、API 和文档变化很快，写进 skill 反而过期。
- 只是一次性 prompt，后续不会重复执行。
- 写出来只是为了“看起来有系统”，没有真实调用场景。

### 写 skill 的关键点

| 部分 | 判断 |
| --- | --- |
| `name` | 短、小写、稳定，和目录名一致 |
| `description` | 不是介绍 skill 做什么，而是告诉 agent 什么时候加载它；最好写成 `Load when...` 的触发条件 |
| body | 不写模型已经知道的常识，重点写流程、边界、失败模式和检查清单 |
| `references/` | 放长文档、规范、案例、背景资料，按需读取 |
| `scripts/` | 放确定性工具动作，不要让 agent 每次临场重写 |
| gotchas | 价值最高，记录 agent 曾经错过、误判、越界或过度执行的情况 |

### 维护飞轮

```text
发现 agent 做错
  -> 判断是 description 路由问题、正文缺规则，还是缺 gotcha
  -> 补正例 / 反例 / 禁止加载场景
  -> 跑 load / read / end-to-end eval
  -> 合并后继续观察
```

最重要的维护原则：description 是路由器，改它会影响所有 session；正文可以补 gotchas，但不要为了一个小失败就把 skill 改成越来越长的百科。

## 和 Vibe Coding路线图的关系

这类仓库主要挂在 [[Wiki/Vibe Coding/00-Overview/Vibe Coding专题路线图|Vibe Coding专题路线图]] 的 `Use skills created by others` 节点下。

它们也会反向补强这些节点：

- `Plan before you Code`：用 grill / PRD / issue 拆分减少需求误解。
- `Tech Stack and Coding`：用 setup、style、domain docs 固化项目偏好。
- `Debugging`：用 diagnose 建立可复现反馈回路。
- `Testing`：用 TDD 和 regression test 控制 agent 生成代码质量。
- `Master Version Control`：用 issue、handoff、pre-commit 和 git guardrails 降低破坏性操作风险。
- `AI产品工程`：生产级 agent 产品里，skills 是单 agent 扩能力和多 agent 分工的基础模块；详见 [[Wiki/AI产品工程/生产级Agent产品工程|生产级Agent产品工程]]。

## 后续维护规则

- 不为每个 skill 单独建页面，除非它已经被反复使用，或者材料足够支撑教程 / SOP。
- 仓库级页面必须包含完整 skill 表，而不是只摘 README 摘要。
- 如果仓库里有 `in-progress`、`personal`、`deprecated` 目录，要明确标注，避免误当成正式推荐。
- 如果仓库当前状态来自 GitHub 实时拉取，记录 commit 和日期；如果只来自 clipping，则标注可能过期。
- 新增或修改 skill 时优先补 eval 和 gotchas；不要把通用知识、易过期 UI 路径或远程工具当前状态硬塞进 skill 正文。

## 来源

- [[Clippings/mattpocockskills Skills for Real Engineers. Straight from my .claude directory.|mattpocock/skills]]：真实工程 skill 仓库样本。
- [[Clippings/Designing, Refining, and Maintaining Agent Skills at Perplexity|Designing, Refining, and Maintaining Agent Skills at Perplexity]]：skill 作为目录、格式、可调用能力和渐进上下文的设计与维护原则。
- [[Clippings/Master 97% of Codex in 1 Hour (full course)|Master 97% of Codex in 1 Hour]]：提供“先跑通手工 workflow，再封装成 skill，再升级为 automation”的新手案例。
