---
type: wiki
status: compiled
area: 知识库维护
topic: 教程采编
compiled: 2026-05-28
updated: 2026-05-28
tags:
  - 教程采编
  - NotebookLM
  - Clippings
  - Raw
  - Wiki
  - Outputs
absorbed_from_title:
  - "YouTube Vibe Coding教程采编验证"
absorbed_on: 2026-05-28
---

# 教程筛选到NotebookLM审片再到Wiki编译闭环

## 这个流程解决什么

这个流程解决的是“全网教程很多，但不知道哪些值得消化进知识库”的问题。它不是自动抓一堆资料做摘要，而是一个轻量、可追溯、有人判断的采编闭环：

```text
候选池
  -> NotebookLM / 人工审片
  -> Raw / Clippings 入库
  -> Wiki 编译 / 主干页维护
  -> Outputs: 教程 / SOP / 案例 / 发号施令 prompt / 知识召回 prompt
  -> Outputs 交付
  -> 反馈回流
```

目标是把视频、文章、课程、prompt pack、案例和工具文档变成能照做的中文教程、SOP、案例拆解和课程材料。

## 为什么要分层

| 层 | 作用 | 能不能改写 |
| --- | --- | --- |
| `.tmp/` 候选池 | 临时搜索结果、评分、待看列表 | 可以改 |
| `Clippings/` | 网页、blog、YouTube transcript、公众号等外部原文 | 正文不改，只可更新 frontmatter |
| `Raw/` | PDF、视频、截图、课程资产、NotebookLM 审片记录 | 原始材料不改写 |
| `Wiki/` | AI 编译后的知识层 | 可以持续更新 |
| `Outputs/` | 面向交付的教程、SOP、案例、课程 | 从 Wiki 生成 |

关键纪律：**不要从 Raw/Clippings 直接生成正式 Output。先编译进 Wiki，再从 Wiki 生成 Output。**

## 角色分工

| 角色 | 负责什么 |
| --- | --- |
| Codex | 搜索策略、候选初筛、目录规则、Wiki 编译、Output 生成、日志记录 |
| 用户 | 判断材料真实价值、用 NotebookLM 追问、确认是否值得入库 |
| NotebookLM | 视频/长文摘要、章节定位、问答、材料对比 |
| Vault | 保留 source of truth、知识层和交付层 |

## 试点经验如何进入标准流程

这个通用闭环来自第一轮 `YouTube + Vibe Coding` 采编试点。原来的 `YouTube Vibe Coding教程采编验证` 已并入本页，不再单独维护。

试点验证的关键判断：

- 搜索结果不能直接进入 `Raw/` 或 `Clippings/`，先进入候选池。
- 候选池只用于筛选和记录判断，不是 source of truth。
- 视频材料必须经过 NotebookLM / 人工审片，用户确认“值得 / 不值得 / 只作旁证”后再入库。
- 长课不是问题，关键是章节密度高、项目链路完整，能覆盖工具安装、真实项目、认证/数据库、安全、部署、调试和商业化。
- 摘要页和 transcript 适合初筛，最终质量判断必须来自用户追问和实际观看反馈。

这些经验已经吸收到下面的标准流程里：

| 试点经验 | 并入位置 |
| --- | --- |
| 搜索结果先进入候选池 | `1. 建候选池` |
| 用实操完整度、可复现性、工程质量、营销噪音评分 | `1. 建候选池` 的风险和缺口判断 |
| 用户用 NotebookLM 追问后再入库 | `2. 用户审片或深看` |
| NotebookLM 对话属于用户加工证据 | `4. 审片记录进入 Raw/NotebookLM` |
| 课程 prompt 和课件属于 CourseKit | `5. 课程资产进入 Raw/CourseKits` |
| 编译后还要检查旧 Wiki 和 Outputs | `9. 编译后的 Wiki 维护` |

当前样例候选池仍保留在：

```text
.tmp/youtube-vibe-coding-candidates-2026-05-27.md
```

候选评分维度：

| 维度 | 判断问题 |
| --- | --- |
| 实操完整度 | 是否从环境、项目、调试、部署跑完整流程？ |
| 可复现性 | 是否有命令、工具版本、文件结构、截图、清晰步骤？ |
| 真实项目密度 | 是否构建真实 app，而不是只做 landing page 或 toy demo？ |
| 坑和失败 | 是否展示错误、失败、调试、部署问题、安全问题？ |
| 工程质量 | 是否讲 Git、测试、数据库、权限、依赖、安全、生产化？ |
| 学习转化 | 能否转成 Wiki、SOP、工具比较、课程练习？ |
| 时效风险 | 工具版本是否过新、过期或很难复现？ |
| 营销噪音 | 是否强卖课、夸大收益、标题党？ |

NotebookLM 审片时优先问：

```text
1. 这个材料到底教我做出了什么具体东西？
2. 它有没有从 0 到可运行结果的完整步骤？
3. 它用了哪些工具、模型、平台和版本？
4. 视频里有没有出现报错、失败、调试和修复？
5. 哪些步骤是可以照做的？哪些只是口头建议？
6. 它对新手最大的价值是什么？
7. 它有什么明显营销、夸大或跳步？
8. 它和我已有 Wiki 相比，补了哪个缺口？
9. 如果只能抽 3 个知识点进 Wiki，应该是哪 3 个？
10. 这条材料值不值得进入 Raw / Clippings？为什么？
```

## 标准流程

### 1. 建候选池

候选材料先放 `.tmp/`，不要直接进 `Raw/` 或 `Clippings/`。

候选池记录：

- 标题。
- 来源链接。
- 作者 / 平台。
- 发布时间。
- 主题。
- 初筛理由。
- 可能补哪个 Wiki 缺口。
- 风险：标题党、过期、营销味、不可复现。

推荐命名：

```text
.tmp/<platform>-<topic>-candidates-YYYY-MM-DD.md
```

### 2. 用户审片或深看

候选进入 NotebookLM 或其他审片工具后，用户重点看：

- 它到底做出了什么。
- 是否有完整步骤。
- 是否展示失败、调试、部署、安全和成本。
- 是否能补现有 Wiki 缺口。
- 有没有真实案例和可复用 prompt。
- 是否值得进一步入库。

最小反馈格式：

```text
材料：
结论：值得 / 不值得 / 只作旁证
最有价值的点：
最大问题：
适合进入哪个 Wiki：
是否有配套文件：
下一步：
```

### 3. 原文进入 Clippings

以下材料进入 `Clippings/`：

- 网页文章。
- blog。
- YouTube transcript。
- X / Reddit / 小红书 / 公众号网页剪藏。
- 产品文档快照。

Clipping 保留原文。Codex 可以更新 frontmatter：

```yaml
compile_status: unreviewed | triaged | partial | compiled | reference | ignore
compiled_to:
remaining_value: high | medium | low
review_note:
```

### 4. 审片记录进入 Raw/NotebookLM

NotebookLM 对话、用户追问、人工判断不算外部原文，放：

```text
Raw/NotebookLM/<review-date>--<platform>--<topic>--<short-slug>.review.md
```

审片记录要说明：

- 这个材料为什么值得或不值得。
- 用户重点追问了什么。
- 哪些片段需要回原文核对。
- 哪些结论不能直接泛化。

### 5. 课程资产进入 Raw/CourseKits

课程作者给的 prompt、课件、示例项目、截图、配置文件放：

```text
Raw/CourseKits/<platform>--<topic>--<short-slug>/
  README.md
  prompts/
  assets/
```

`README.md` 记录：

- source URL。
- 对应 clipping。
- 对应 review note。
- 文件清单。
- 当前处理状态。

### 6. 编译进 Wiki

编译顺序：

1. 先看 `Raw/NotebookLM/*.review.md`，理解用户判断。
2. 再看 `Raw/CourseKits/**/README.md` 和 prompt/assets。
3. 需要核对细节时回到 `Clippings/` 原文。
4. 只把可复用的步骤、案例、模板、限制和坑写进 Wiki。
5. 如果材料里有高价值 prompt，先把它背后的任务逻辑、变量、步骤、风险和验收标准编译进 Wiki；正式 prompt 作为 `Outputs/` 产物生成。
6. 如果主题主要是 AI 擅长的通用知识，但用户不知道怎么问，Wiki 写成问题框架、讲解路径和证据缺口；需要交付时再生成知识召回 prompt Output，不要机械写成长篇百科。

Wiki 页面要回答：

- 解决什么实际问题。
- 适合谁，不适合谁。
- 输入、工具、步骤、输出。
- 可复用模板或检查清单。
- 真实来源证据。
- 常见坑、成本、限制和替代方案。
- 能生成哪些 Outputs。

### 6.1. 从 Wiki 生成发号施令 prompt Output

发号施令 prompt 负责让 AI 按要求把事情做出来。它是 Outputs 产物，不是 Wiki 页面。高价值 prompt 不应该只埋在普通 Wiki 页面里；满足下面条件时，先把任务逻辑整理进 Wiki，再单独生成发号施令 prompt Output：

- 有清晰角色、输入、步骤、约束和输出格式。
- 能直接支撑课程、SOP、模板或真实项目。
- 后续需要被用户修改、增删或迁移到不同工具。

推荐位置：

```text
Outputs/SOP与模板/<prompt-name>中英对照.md
```

发号施令 prompt Output 要包含：

- 使用场景。
- 适合谁，不适合谁。
- 上游 Wiki 页面。
- 参考 Raw / Clippings。
- 可替换变量。
- 中英文对照结构。
- 可复制精简版。
- 风险和验收。
- 来源锚点。

### 6.2. 从 Wiki 生成知识召回 prompt Output

知识召回 prompt 负责让 AI 把已经知道的东西讲出来。它是 Outputs 产物，不是 Wiki 页面。满足下面条件时，Wiki 先整理问题框架和讲解路径，再生成知识召回 prompt Output，而不是写完整百科页：

- 主题是 AI 完全熟悉、相对稳定、且不依赖真实用户体验的通用概念、基础机制、成熟方法论、学习路线第一问或常见决策入口。
- AI 大体能回答，但用户不知道如何开始问。
- 当前缺少本库独特案例、真实踩坑或强时效证据。
- 目标是让用户先建立第一层理解，并愿意继续追问。

如果主题依赖真实上手体验、界面交互、工具稳定性、生成质量、最新模型能力或市场反馈，不要做知识召回 prompt。尤其是 AI 编程工具、设计工具、内容工具的“怎么选 / 哪个好用 / 谁更强”，应进入真实体验复盘、工具能力台账、强时效 Wiki 或案例。

知识召回 prompt 必须是单一 prompt：

- 不拆成简单版 / 增强版。
- 不要求用户先填写变量。
- 先通俗解释大图，再给关键判断框架。
- 最后用一个自然钩子引导用户继续描述自己的情况。
- 明确哪些内容必须查官方文档、真实案例或用户自己的材料。
- 明确哪些使用结果值得回流到 Wiki。

面向用户的正式 Output 优先使用：

```text
Outputs/SOP与模板/知识召回prompt卡片模板.md
```

这个模板不是固定死格式。每完成 3-5 张知识召回 prompt 卡片后，要回看模板是否需要调整：哪些结构有效、哪些过于机械、哪些钩子能引导用户继续问、哪些核验点经常遗漏。模板修改也要记录到 `log.md`。

### 7. 从 Wiki 生成 Outputs

正式 Output 必须写清：

- 上游 Wiki 页面。
- 参考的 Raw / Clippings。
- 目标读者。
- 适用场景。
- 版本日期。

Output 类型：

- 教程。
- 案例拆解。
- 工具比较。
- SOP 与模板。
- 课程与训练营。
- 图文卡片。
- PPT 与讲义。

### 8. 更新日志和状态

每次编译或产出都要更新 `log.md`。

日志至少写：

- 处理了哪些材料。
- 新增或更新了哪些 Wiki。
- 新增或更新了哪些 Outputs。
- 哪些疑点未解决。
- 原始 clipping 的状态是否变化。

### 9. 编译后的 Wiki 维护

新增页面后，不要立刻结束。必须检查：

- 是否和已有 Wiki 页面重复。
- 是否改变了旧主干页的结论。
- 是否需要更新专题路线图或索引。
- 是否有旧页面需要标记 `needs_merge`、`needs_refresh` 或 `deprecated`。
- 是否有旧 Output 需要再生成。

这个维护动作本身也要写入 `log.md`。

## 材料分级

| 等级 | 说明 | 下一步 |
| --- | --- | --- |
| `must-compile` | 高质量教程、官方文档、真实案例、强方法论 | 进入 Wiki 主干 |
| `useful-evidence` | 可做旁证、案例片段、经验和技巧 | 进入相关 Wiki 证据段 |
| `link-only` | 只值得留链接和一句话 | 不急于编译 |
| `ignore-for-now` | 重复、低质、营销味重、过期 | 标记后暂不处理 |

## 质量闸门

不要编译：

- 只有概念，没有步骤。
- 只有结果截图，没有过程。
- 强卖课但没有可验证细节。
- 工具版本明显过期且没有长期价值。
- 单篇观点无法泛化，却包装成通用结论。

优先编译：

- 有真实项目。
- 有失败和调试。
- 有部署、安全、成本、权限。
- 有配套 prompt / 文件 / 示例。
- 能转成 SOP、课程练习或案例拆解。

## 可生成 Outputs

- `高质量教程采编闭环模板`
- `NotebookLM 审片问题清单`
- `全网 AI 教程入库前质量评分表`

## 证据锚点

- 已吸收旧页标题：`YouTube Vibe Coding教程采编验证`
- 试点候选池：`.tmp/youtube-vibe-coding-candidates-2026-05-27.md`
- 当前样例：`Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md`
- 当前样例：`Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/README.md`
