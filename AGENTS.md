# AI 应用落地 Vault — Codex Instructions

这个 vault 是 AI 应用落地知识库。目标不是讲抽象概念，而是搜罗、消化和产出能直接照做的教程、案例、技巧、工具比较和业务落地方案。

核心方向：

- AI 编程、WebCoding、网页 / 网站搭建。
- AI 做 PPT、Word、表格、报告、图文资料。
- AI 电商、外贸、小企业获客、客服、运营和自动化。
- AI 视频、短剧、漫剧、图像、脚本和内容流水线。
- AI 产品工程、生产级 agent、tool calling、评估、观测性和数据飞轮。
- AI 一人公司、独立开发、个人业务自动化。
- 全网优质教程、大 V 方法、真实落地案例、工具对比和避坑复盘。

## 核心原则

1. 采用 Karpathy 风格的轻流程：`Raw / Clippings -> Wiki -> Outputs`。
2. `Clippings/` 和 `Raw/` 是 source of truth：只新增，不改写，不移动，不覆盖。
3. `Wiki/` 是 AI 维护的主题知识层，负责把材料编译成可复用方法、案例、工作流、工具判断、证据锚点、坑和本库判断。
4. `Outputs/` 是面向交付的产物层：教程、案例拆解、工具比较、SOP、模板、课程大纲、训练营作业、评分标准、课程讲义、PPT、图文卡片和 prompt 卡片。
5. `.kb/` 是机器可读的 Knowledge Unit Ledger，负责记录知识单元、关系、覆盖审计、验证和未来网站 / AI Tutor 的 serving index；它不替代 Wiki。
6. 默认不要从 Raw / Clippings 直接生成正式 Output；先编译进 Wiki，必要时抽成 `.kb` knowledge units，再从 Wiki / units 生成 Output。
7. Wiki 不是替代 AI 的百科。AI 完全熟悉、相对稳定、且不依赖真实上手体验的通用知识，不要机械编译成长篇答案；需要交付时，从 Wiki 生成 `知识召回 prompt` Output。
8. AI 不稳定、不知道或不擅长的内容，才是 Wiki 和 `.kb` 的重点沉淀对象：真实案例、个人 know-how、踩坑复盘、NotebookLM 审片、UI 操作复盘、中文市场成交经验、依赖用户体验的工具判断、平台最新政策、价格、API 权限和证据冲突。
9. 高价值可执行 prompt 要先把方法、结构、变量、风险和验收逻辑整理进 Wiki，必要时抽成 `.kb` units，再生成 `发号施令 prompt` Output。
10. Wiki 的长期价值是三件事：组织好问题、保存证据、沉淀本库判断。`.kb` 的长期价值是三件事：给知识上身份证、保存关系、支持机器精准调用。
11. Wiki 维护采用“合并优先，新建克制，膨胀后再拆分”。同一粒度下讲同一件事的页面必须合并；禁止把旧页整篇 append 到尾部。
12. `.kb` 维护采用“canonical 优先，variant 克制，冲突显式记录”。同一知识点不要反复创建新 unit；先找 canonical unit，再判断是 merge、variant、evidence、contradiction 还是 new。
13. 技术名词可以保留英文，如 `Claude Code`、`Codex`、`Cursor`、`MCP`、`agent`、`workflow`、`prompt`。
14. 内容默认中文，面向普通用户、独立开发者、产品 / 运营、老板、小企业和课程学员。
15. 不追求大而全的理论页。每个 Wiki 页面都应该能支撑教程、案例、比较、SOP、知识召回 prompt Output、发号施令 prompt Output、课程讲义或 AI Tutor 上下文。
16. 收录材料时优先判断实用价值：能不能照做、有没有真实案例、步骤是否清晰、成本和坑是否可见。
17. 讲技术只服务于落地。底层 agent / harness / eval / MCP 只在解释工具边界、能力差异或实操风险时出现。
18. 每次编译、产出或结构维护都要在 `log.md` 记录：处理了哪些材料、更新了哪些 Wiki / Outputs / `.kb` 文件、留下什么疑点。

## 当前目录

```text
Clippings/   # 浏览器剪藏的 Markdown 文章 / blog / 网页快照，保留原样
Raw/         # PDF、视频、截图、repo dump、数据文件、NotebookLM review、CourseKits 等原始材料
Wiki/        # AI 编译后的主题知识库，人类可读
Outputs/     # 教程、案例、比较、SOP、课程、prompt、PPT、图文卡片等正式产物
.kb/         # Knowledge Unit Ledger，机器可读知识单元、关系、coverage、verification、exports
Tools/       # 轻量工具：digest、PDF/video 转写、视觉/OCR 辅助
AGENTS.md    # 本规则文件
index.md     # vault 首页
log.md       # 处理日志
```

## Clippings 规则

`Clippings/` 下的 Markdown 通常已经包含：

```yaml
title:
source:
author:
published:
created:
description:
tags:
compile_status:
compiled_to:
remaining_value:
```

这已经足够作为 Wiki 编译的来源元数据。不要为了形式再复制到 `Sources/`。

处理 clipping 时：

- 读取 frontmatter 和正文。
- 判断材料类型：教程、观点、案例、工具发布、研究、产品文档、营销软文。
- 判断质量等级：`must-compile`、`useful-evidence`、`link-only`、`ignore-for-now`。
- 只把值得复用的内容编译进 Wiki / `.kb`。
- Wiki 证据锚点用 clipping 文件路径、标题、原始 `source` URL 和发布时间。
- Clipping 正文不改写；frontmatter 可以追加或更新 `compile_status`、`compiled_to`、`remaining_value`、`kb_units`。
- `compile_status` 可用值：`unreviewed`、`triaged`、`partial`、`compiled`、`reference`、`ignore`。
- `remaining_value` 可用值：`high`、`medium`、`low`。

## Raw 规则

`Raw/` 用于非 clipping 原始资料，默认扁平化：

- PDF、电子书、报告、论文。
- 视频、录屏、课程。
- 截图、长图、界面图。
- repo 快照、clone 记录、commit 记录。
- 表格、JSON、数据文件。
- NotebookLM / 人工审片记录。
- CourseKits / prompt packs / 课程配套文件。

不要预先创建 `papers/`、`blogs/`、`repos/`、`videos/` 这类空分类目录。文件多到确实需要拆分时，再从材料自然长出少数目录。

大多数网页、YouTube transcript、X、小红书、Reddit、blog 的 Markdown 抓取应该进入 `Clippings/`，不是 Raw。PDF / 视频可以先用工具转成 `.tmp/` 中间结果，再由 AI 编译进 Wiki。中间结果不是知识层。

### NotebookLM / 人工审片记录

当用户把 YouTube、B 站、X、公众号等材料放进 NotebookLM 或其他 AI 工具后，和 AI 的对话、追问、总结、人工判断不属于外部网页 clipping，也不应该继续放在 `Clippings/`。

这类材料作为“人工审片记录”进入：

```text
Raw/NotebookLM/<review-date>--<platform>--<topic>--<short-slug>.review.md
```

规则：

- 原文 / transcript / 网页剪藏仍放 `Clippings/`。
- NotebookLM 对话和用户总结放 `Raw/NotebookLM/`。
- 编译时优先阅读 `Raw/NotebookLM/*.review.md`，因为它记录用户关注点和质量判断；只有需要核对原文、步骤、时间戳或证据时，再回到对应 clipping。
- 不要把 NotebookLM 对话误当成外部原文；它是用户加工后的审片证据。
- 如果历史文件已经误放在 `Clippings/对话与总结/`，不要删除；可以新增一份规范命名的 Raw/NotebookLM 副本，并在 clipping frontmatter 里用 `review_note` 指向它。

### 课程配套文件 / Prompt Packs

课程作者提供的 prompt 文件、Google Drive 课件、示例文件、截图、配置样例等，不属于 `Clippings/`，也不要恢复旧 `Prompts/` 层。

这类多文件课程资产进入：

```text
Raw/CourseKits/<platform>--<topic>--<short-slug>/
```

推荐结构：

```text
Raw/CourseKits/<platform>--<topic>--<short-slug>/
  README.md
  prompts/
  assets/
```

规则：

- Prompt 文件是课程原始材料，保持内容不改写。
- 如果原文件名清晰，保留原名；如果原文件名含糊，使用 `prompt-01--<purpose>.md` 这类规范名。
- `README.md` 负责记录 source URL、对应 clipping、NotebookLM review note、文件说明和处理状态。
- 编译时先看 `Raw/NotebookLM/*.review.md`，再看 `Raw/CourseKits/**/prompts/`，最后回查 `Clippings/` 原文。
- 不要把课程 prompt 直接做成正式 Output；先编译到 Wiki，再从 Wiki 生成 SOP、模板或课程讲义。

## Knowledge Unit Ledger 规则

`.kb/` 是机器可读知识单元层，服务去重、合并、关系、coverage、AI Tutor 和未来网站检索。它是 ledger，不是正式文章层，也不是 Raw 的替代品。

推荐结构：

```text
.kb/
  README.md
  schemas/knowledge-unit.schema.md
  templates/
  atoms/*.jsonl
  relations/*.jsonl
  coverage/*.jsonl
  verification/
  exports/
```

### 三种核心粒度

第一阶段只区分三种粒度，避免过度工程：

| 粒度 | 说明 | 例子 |
|---|---|---|
| `atom` | 最小行为改变单元。一个 action、rule、pitfall、tip、claim 或 checklist item。 | 调试时给 AI console、截图、日志和复现步骤。 |
| `block` | 多个 atoms 组成的 workflow、checklist、method family、playbook、pattern。 | Vibe Coding 上线前安全审计 5 项。 |
| `module_ref` | 指向 Wiki 页面的人类可读模块引用，通常只放 path、title、role 和上游 units。 | `Vibe Coding全栈SaaS开发闭环.md`。 |

块状经验不需要被打碎消灭。它可以作为 `block` 保存，同时用 `children` 或 `contains` 指向子 atoms。

### 什么时候创建 unit

凡是满足下面任意条件，都应该考虑抽成 knowledge unit：

- 会改变用户行为。
- 用户不知道会明显踩坑。
- 能被多个 Wiki 页面或 Outputs 复用。
- 是判断规则、反模式、流程、清单项、prompt pattern、UI 知识或排错线索。
- 有版本风险，需要单独标记 `freshness_risk`。
- 有证据冲突，需要单独记录 `contradicts`、`variant_of` 或 `evidence_against`。
- 是作者顺口提到但很实用的小 tip。

不要为纯百科定义、泛泛励志句、低信息密度标题党观点创建 unit。

### 单元生命周期

```text
candidate
  -> duplicate_check
  -> canonical / variant / evidence / contradiction / deprecated
  -> used_in Wiki modules
  -> verified / needs_refresh / superseded
```

每个新 unit 进入前必须先问：

1. 这个知识是否已经存在？
2. 它是旧 unit 的同义表达、变体、证据、反例，还是新知识？
3. 它应该更新哪个 Wiki 页面？
4. 它是否影响已有 Outputs？
5. 它的来源和证据跨度是什么？

### 合并与关系规则

- 如果只是同一行为建议、同一场景、同一失败风险的不同说法，合并到 canonical unit，用 `aliases` 保存旧表达。
- 如果核心原则相同，但工具、阶段、用户或市场环境不同，创建 `variant_of`。
- 如果来源给出相反建议，不要平均化；用 `contradicts` 显式记录，并在 Wiki 写清适用条件。
- 如果新资料只是支持旧判断，不要新建重复 unit；补到 `source_spans` 或 `evidence_for`。
- 如果工具更新导致旧结论过期，用 `updates` / `replaces`，并给旧 unit 标记 `deprecated` 或 `needs_refresh`。

推荐 relation 类型：

```text
part_of, contains, requires, prerequisite_of, enables, prevents, solves,
causes, variant_of, same_as, near_duplicate_of, contradicts, updates,
replaces, evidence_for, evidence_against, used_in, applies_to
```

### Coverage 规则

处理长教程、视频、NotebookLM review、课程 prompt pack 或重要 Wiki 页面时，必须尽量建立 coverage 记录，防止小 tips 漏掉。

每个 segment 必须有状态：

- `extracted`：已抽取 unit。
- `duplicate`：已有 canonical unit 覆盖。
- `context_only`：只是背景，不必抽成 unit。
- `noise`：广告、闲聊、低信息内容。
- `outdated`：明显过期。
- `uncertain`：可能有价值但暂未结构化。
- `needs_human_review`：需要用户或人工审片再判断。

coverage 的目标不是为了形式化，而是让遗漏变得可见。AI 不确定的小 tip，先放进 `uncertain` 或 candidate unit，不要悄悄丢弃。

## 发号施令 prompt

发号施令 prompt 负责“让 AI 按你的要求把事情做出来”。它属于 `Outputs/` 的交付产物，不属于 `Wiki/` 知识层。高价值 prompt 不应该只作为普通 Wiki 页面里的证据锚点；只要 prompt 具备可复用结构，能直接支撑课程、SOP、模板或真实项目交付，就应该先把它背后的任务逻辑、变量、步骤、风险和验收标准整理进 Wiki，再从 Wiki / `.kb` 生成发号施令 prompt Output。

推荐位置：

```text
Outputs/SOP与模板/<prompt-name>中英对照.md
Outputs/课程与训练营/<course-or-lesson-prompt>.md
```

规则：

- 不恢复废弃的顶层 `Prompts/` 目录，也不要在 Wiki 下创建 `Prompts/` 或 `<number>-Prompts/` 目录。
- 原始 prompt 仍保存在 `Raw/CourseKits/`，不改写、不覆盖。
- 编译后的 prompt 页属于 Outputs 交付层，不是 source of truth，也不是 Wiki 主干页。
- Wiki 负责沉淀 prompt 背后的任务模型：使用场景、输入、步骤、变量、风险、验收、来源证据和可复用结构。
- `.kb` 可记录 prompt pattern、风险点、检查项和可复用变量，但不要复制整段原始 prompt。
- Prompt Output 应包含：使用场景、适合谁、不适合谁、上游 Wiki、参考 Raw / Clippings、可替换变量、中英文对照结构、可复制精简版、扩展模块、风险和验收、来源锚点。

## 知识召回 prompt

不是所有 Wiki 都应该写成完整答案。对于 AI / LLM 本来完全熟悉、相对稳定、且不依赖真实用户体验的主题，Wiki 的价值不是重复写一篇百科，而是整理好“这个主题应该如何被理解、如何被提问、哪些表达和逻辑值得学习、哪些证据和案例需要本库补充”。当这个主题需要交付给用户使用时，再从 Wiki 生成一个高质量 prompt，让用户输入一次就能诱导 AI 生成完整解释、比较、方案和追问路径。

这类 Output 称为“知识召回 prompt”，负责“让 AI 把知道的东西讲出来”。

适合生成知识召回 prompt Output 的主题：

- 通用概念、基础机制、稳定原理、成熟方法论。
- 用户只缺第一层认知地图，而不是缺真实体验证据。
- 技术选型只限 AI 完全熟悉、变化慢、主要差异是基础原理和使用边界的领域。
- 用户没有基础概念，难以提出好问题的领域。
- AI 能回答大部分内容，但需要更好的上下文、变量、边界和追问顺序。
- 目前缺少本库独特案例或真实证据，不值得写成长篇结论页。

不适合生成知识召回 prompt Output 的主题：

- 依赖真实用户体验、上手手感、界面交互、生成质量或工具稳定性的判断。
- AI 编程工具、设计工具、内容工具等快速变化工具的“怎么选”“哪个好用”“谁更强”。
- 价格、权限、平台政策、模型能力、UI 路径和审核规则等强时效内容。
- 用户自己的业务定位、读者定位、输出形态和交付标准。

这些内容应沉淀为真实体验复盘、工具能力台账、强时效 Wiki、案例、`.kb` units 或发号施令 prompt Output，而不是让 AI 只凭已有知识召回。

生成面向用户的知识召回 prompt Output 时，优先使用 `Outputs/SOP与模板/知识召回prompt卡片模板.md` 的卡片结构。这个模板是 living 模板：每完成 3-5 张知识召回 prompt 卡片后，应回看实际效果并更新模板；模板只定骨架，具体 prompt 必须按主题重写，不能机械套壳。

## Wiki 新结构

Wiki 采用主题优先，并且主题直接放在 `Wiki/` 下一层。不要再创建 `Wiki/Topics/`、`Wiki/Workflows/`、`Wiki/Cases/`、`Wiki/Tools/`、`Wiki/Courses/` 这类按产物形态或材料类型划分的目录。

当前形态：

```text
Wiki/
  Vibe Coding/
  AI视频制作/
  AI知识库/
  AI营销自动化/
  AI产品工程/
  AI一人公司/
  AI行业判断/
  AI使用方法/
  知识库维护/
```

新材料进入 Wiki 时，先判断它能否并入已有主题；能并入就并入，不能并入才在 `Wiki/` 下一层新建主题目录。

`workflow`、`case`、`tool`、`course` 首先是 Output 形态或页面表达方式，不应该决定 Wiki 目录。Wiki 负责沉淀知识本身：概念、问题框架、证据、方法、产品模式、工具边界、坑和判断。Outputs 再根据目标用户和交付形态生成课程、案例拆解、workflow、SOP、工具比较、PPT、图文卡片等。

Wiki 页面应尽量包含：

- 这个方法 / 案例解决什么实际问题。
- 适合谁，不适合谁。
- 输入、步骤、工具、输出。
- 可复用模板或检查清单的知识依据。
- 真实案例或来源证据。
- 常见坑、成本、限制和替代方案。
- 能生成哪些 Outputs，包括教程、SOP、案例、课程讲义、prompt 卡片和图文/PPT。
- 可复用 `.kb` unit IDs，尤其是高频坑点、decision rule、workflow、checklist 和 prompt pattern。

Wiki 不负责维护正式课程编排。第几课教什么、配什么练习、学员做到什么算合格、讲义如何呈现，属于 `Outputs/课程与训练营/` 或 `Outputs/PPT与讲义/`。Wiki 只维护这些课程背后的主题知识、证据、判断和可复用方法。

如果页面主题属于 AI 完全熟悉、相对稳定、且不依赖真实用户体验的通用知识，不要为了填充 Wiki 机械写完整百科；优先整理成问题框架、讲解路径、关键判断、来源里值得学习的表达和本库需要补证据的地方。需要交付给用户时，再从 Wiki 生成知识召回 prompt Output；用户追问得到的真实案例、最新证据和本库判断再回流到 Wiki / `.kb`。

不要创建只有两三行定义的空页面。

## Outputs 新结构

Outputs 是交付层，可以按产物形态组织，也可以按目标用户画像生成不同版本。例如同一份 Wiki / `.kb` 知识，可以分别产出给投资人、程序员、普通人、白领、学生、小企业老板或课程学员看的版本。

当前目录先按产物形态组织：

```text
Outputs/教程/
Outputs/案例拆解/
Outputs/工具比较/
Outputs/SOP与模板/
Outputs/课程与训练营/
Outputs/图文卡片/
Outputs/PPT与讲义/
```

正式 Output 必须从 Wiki 生成，并在 frontmatter 或正文写明：

- 上游 Wiki 页面。
- 参考的 Raw / Clippings。
- 使用到的 `.kb` unit IDs，如有。
- 目标读者。
- 适用场景。
- 版本日期。

Outputs 不承担 Wiki 知识拓扑。它负责根据 Wiki / `.kb` 生成可交付内容：课程、案例拆解、workflow、SOP、工具比较、prompt、PPT、图文卡片，以及面向不同用户画像的改写版本。

## 默认工作流

```text
Clippings / Raw
  ↓
AI 读取、筛选、先找已有 Wiki 吸收
  ↓
必要时切 source segments，抽 knowledge unit candidates
  ↓
duplicate / variant / contradiction / evidence check
  ↓
并入已有 Wiki / 必要时新建 Wiki
  ↓
更新 .kb atoms / relations / coverage / verification
  ↓
主题膨胀后再拆分
  ↓
教程 / 案例 / 比较 / SOP / Prompt / 课程 / PPT / 图文卡片 / AI Tutor 上下文
  ↓
用户反馈 / 社区复现 / 最新动态
  ↺ 回流到 Wiki / Outputs / .kb
```

## Wiki 持续维护

Wiki 不是一次性编译结果，而是持续演化的知识层。每次新增 Wiki 后，都要检查它是否影响已有页面和 `.kb` units。

默认不要先问“要不要新建页面”，而要先问“哪条现有主干能吃掉这份材料”。新页面是最后手段，不是默认动作。

每次编译后，AI 默认自行检查并处理：

- 新材料应该并入哪个已有目录、主题或主页面？
- 新页面是否和已有页面重复，应该独立还是合并？
- 新页面是否与旧页面在同一粒度下讲同一件事？如果是，必须合并成一个主页面。
- 合并时是否已经选择、重排和融合旧页内容，而不是简单拼接或 append？
- 新材料是否改变了旧页面的结论？
- 是否需要更新专题路线图、索引页或相关 Outputs？
- 是否需要新增或更新 `.kb` atoms / relations / coverage？
- 是否有旧页面或旧 unit 应该标记为 `needs_merge`、`needs_refresh`、`deprecated`、`superseded`？

建议页面状态：

- `seed`：初始框架，证据少。
- `compiled`：已能支撑教程、SOP、案例或工具判断。
- `living`：主干页，会持续吸收新材料。
- `needs_merge`：与其他页面重复，需要合并。
- `needs_refresh`：依赖强时效信息，需要重新核验。
- `needs_decision`：目录走向、定位或结论取舍需要先和用户讨论。
- `deprecated`：结论过时或被新页面取代。

建议 unit 状态：

- `candidate`：候选 unit，尚未完成重复检查。
- `canonical`：标准 unit，可被 Wiki / Outputs 引用。
- `variant`：某个 canonical unit 的场景、工具或市场变体。
- `evidence`：支持或反驳某判断的证据单元。
- `contradiction`：显式记录冲突观点。
- `deprecated`：过时或被新 unit 替代。

维护 Wiki / `.kb` 的默认原则是：AI 能判断的事情，AI 先做；不要把内部整理问题丢给用户。

AI 应该自主处理：

- 判断新页面是否重复、独立、合并或补充旧页。
- 判断新材料是否改变旧结论，并据证据更新页面。
- 更新索引、路线图、反向链接和相关 Output 的来源说明。
- 标记 `needs_merge`、`needs_refresh`、`deprecated` 等页面状态。
- 识别高价值小 tips、坑点、decision rules、workflow、prompt patterns，并写入 `.kb`。
- 做 duplicate / variant / contradiction check，必要时更新 canonical unit。
- 做小到中等规模的页面合并、改名、移动和主干页扩写，并在 `log.md` 记录。
- 发现公开资料缺口后，优先自己用已有 Raw / Clippings 或联网核验补证。

只有遇到 AI 不擅长或不应擅自决定的事情，才进入交流与反馈环节。需要询问用户的典型情况：

- 需要用户提供私有、付费、账号内、人工审片后的材料。
- 需要决定业务目标、读者定位、课程方向、商业化优先级或内容风格。
- 目录结构会发生大范围重构，且存在多个合理方向。
- 证据冲突明显，AI 查证后仍无法判断哪个更符合用户目标。
- Output 形态会影响后续投入，例如先做课程、SOP、案例集、图文卡片还是 PPT。

需要讨论时，先给简洁的决策清单；不需要讨论时，直接维护并记录到 `log.md`。

每 5-10 篇新 Wiki，做一次专题整理：搜索重复页、合并重叠段落、更新主干页、清理索引、检查 Outputs 是否需要再生成，并在 `log.md` 记录结构变化。每 50-100 条新 units，做一次 `.kb` 整理：查重、合并 aliases、补关系、标记 needs_refresh、检查 coverage 缺口。

## 材料分级

- `must-compile`：高质量教程、官方文档、真实案例、可复用方法论、强参考价值文章。
- `useful-evidence`：观点、经验、案例片段、技巧、工具评测，可做旁证。
- `link-only`：只值得保存链接和一句话说明。
- `ignore-for-now`：低质、重复、营销味重、过期、不可验证。

## 编译纪律

- 不要机械摘要全文。
- 不要把单篇文章的观点伪装成通用结论。
- 不要只讲“AI 很强”，必须落到步骤、工具、输入输出、成本、坑。
- 不要把“合理规划”“提高效率”这类抽象句当作合格 unit；要拆成具体行为、适用场景、失败后果和来源。
- 多篇来源冲突时，在 Wiki 里写清差异和适用条件，在 `.kb` 中记录 `contradicts` 或 `variant_of`。
- 有强时效性的工具价格、功能、模型能力、UI 路径、平台政策，需要标注日期，并给页面或 unit 标记 `freshness_risk` / `refresh_after`。
- 如果用户明确要求抓取网页或验证最新信息，可以联网；否则优先使用用户已放入的 Clippings / Raw。
- 如果长教程中某段没有抽取价值，也要在 coverage 里说明原因，不能让片段凭空消失。

## 删除旧流程后的注意事项

- `Sources/`、`Prompts/`、`Reviews/`、`Evals/`、`Research/`、`Taxonomy/`、`Templates/` 已废弃。
- 不要重新创建这些目录，除非用户明确要求。
- Review 和 prompt 不再单独建顶层；prompt 产物放在 `Outputs/`，维护记录写在 Output 文件或 `log.md` 中。
- `.kb/templates/` 是 knowledge unit 的机器模板目录，不等于旧 `Templates/` 顶层目录，不要把它扩展成普通内容模板库。
- 分类不再依赖受控 `topics` 文件；用清晰中文目录、页面标题、自由标签和 `.kb` typed relations 解决。
