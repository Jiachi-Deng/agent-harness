---
type: output
output_type: case-breakdown
status: review-ready
target_reader: 个人创作者 / 独立开发者 / 小团队运营
use_case: 拆解一个人如何用 agent workspace、skills、mini apps 和人工审批搭出内容营销系统
version_date: 2026-05-28
updated: 2026-05-29
upstream_wiki:
  - "[[Wiki/AI营销自动化/AI一人营销团队|AI一人营销团队]]"
  - "[[Wiki/AI视频制作/YouTube研究与脚本模仿|YouTube研究与脚本模仿]]"
  - "[[Wiki/AI知识库/个人知识库到内容选题|个人知识库到内容选题]]"
  - "[[Wiki/AI视频制作/讲解图与视觉画布工作流|讲解图与视觉画布工作流]]"
  - "[[Wiki/AI视频制作/AI视频剪辑与动态图形工作流|AI视频剪辑与动态图形工作流]]"
references:
  - "[[Clippings/Codex Build Your Full AI Marketing Team (Agents + Skills)|Codex: Build Your Full AI Marketing Team]]"
---

# Codex 搭建 AI 一人营销团队：案例拆解

这篇拆的是一个创作者把日常内容和营销工作迁到 Codex / Claude Code 类 agent workspace 里的做法。它的价值不在于“某个工具很强”，而在于它把营销拆成了 8 个可复用模块。

注意：这是基于 YouTube clipping 的案例拆解，里面涉及的具体工具能力、API、价格和产品可用性需要后续单独验证。

## 当前 Wiki 关系

本案例的上游主干是 [[Wiki/AI营销自动化/AI一人营销团队|AI一人营销团队]]。它负责整体编排：研究、选题、脚本、视觉、媒体、商务和分发如何串起来。

各模块的细节不再堆回本 Output：

- YouTube transcript、Readwise 选题、Excalidraw、Remotion / Hyperframes 等进入对应主题页。
- Gen Media、Email Manager、Buffer Publisher 已回收进 [[Wiki/AI营销自动化/AI一人营销团队|AI一人营销团队]] 主页面的模块落地细节；后续只有材料持续膨胀时再拆页。
- 如果后续出现新工具实测、价格变化、UI 操作复盘，先回填 Wiki，再判断是否需要更新本案例。

## 一句话结论

不要试图做一个“全自动营销 agent”。更可复刻的做法是：先把营销拆成研究、选题、脚本、图表、视频、媒体、商务、发布 8 个小模块，再逐个做成 skill、mini app 或 automation。

## 8 个模块

| 模块 | 它真正负责什么 | 适合先复刻吗 |
| --- | --- | --- |
| [[Wiki/AI视频制作/YouTube研究与脚本模仿|YouTube Researcher]] | 拉取视频字幕，分析创作者表达结构，生成 hook、开头、脚本和解释版本 | 适合 |
| [[Wiki/AI知识库/个人知识库到内容选题|Readwise CLI]] | 读取个人收藏和第二大脑，生成带来源链接的内容选题 | 适合 |
| [[Wiki/AI视频制作/讲解图与视觉画布工作流|Excalidraw Diagrams]] | 生成手绘风讲解图、流程图、课程大纲图 | 适合 |
| [[Wiki/AI视频制作/讲解图与视觉画布工作流#Paper 视觉画布|Paper]] | 做更专业的交互式图表、品牌视觉、落地页原型和缩略图 | 中等 |
| [[Wiki/AI视频制作/AI视频剪辑与动态图形工作流|Remotion + Hyperframes]] | 做视频开场、产品演示动画、B-roll、图形覆盖层 | 中等偏难 |
| [[Wiki/AI营销自动化/AI一人营销团队#Gen Media|Gen Media]] | 用 FAL API 等生成图片 / 视频，并沉淀为人和 agent 都能用的素材 mini app | 难 |
| [[Wiki/AI营销自动化/AI一人营销团队#Email Manager|Email Manager]] | 筛选商务合作邮件、判断优先级、结合日历建议会议时间 | 难，需要权限边界 |
| [[Wiki/AI营销自动化/AI一人营销团队#Buffer Publisher|Buffer Publisher]] | 把研究和想法同步到社媒排期工具，避免 idea 丢失 | 适合轻量复刻 |

## 8 个模块的操作细节

### YouTube Researcher：外部风格 grounding

它不是简单总结视频，而是把目标创作者的 transcript 变成脚本参考。可复刻动作是：拉取目标创作者最近视频字幕，分析开头、节奏、例子和解释方式，再为你的主题生成多个 hook。

风险是过度模仿。应该学习结构，不复制原句，也不要冒充对方声音。

### Readwise CLI：个人兴趣 grounding

它把你最近保存的推文、文章、高亮和备注变成选题。关键细节是每个选题必须带原始来源链接，否则后续制作时无法回查。

最小可复刻版本是“过去 7 天收藏 -> 30 个选题 -> 每个选题带来源链接”。稳定后再每天早上自动生成。

### Excalidraw Diagrams：把概念变成可讲的图

它适合做视频里的讲解图和课程大纲图。案例里更有意思的是它会组合 YouTube Researcher 和 Readwise：一个提供表达风格，一个提供个人知识库上下文，再用 sub agents 并行提取信息。

输出要少字、多结构、方便全屏讲解。默认文字过多时，要直接修改 skill 偏好。

### Paper：更专业的视觉设计画布

Paper 更像 AI 版 Figma，适合做互动图、动画解释图、品牌视觉、落地页原型和缩略图。它的重点不是一次生成完美稿，而是 live steering：看到重叠就截图反馈，让 agent 继续在画布上修。

适合中期复刻，因为它比 Excalidraw 重，但能承接更专业的视觉产物。

### Remotion + Hyperframes：视频里的动态素材

它们负责开场动画、产品 demo、B-roll、章节 outline 和图形 overlay。可复刻的关键不是“做完整视频”，而是先做 5-20 秒的可复用片段。

案例里提到的有效反馈方式包括：指定第几秒 zoom、飞入、旋转、改颜色；截图指出 overlap；在一个 composition 里做多个 scene 变体；最后 render 到本地。

维护备注：Remotion / Hyperframes 的独立工具页已并入 [[Wiki/AI视频制作/AI视频剪辑与动态图形工作流|AI视频剪辑与动态图形工作流]]，后续相关证据先回填到那条主工作流，等工具比较资料足够多后再考虑拆分。

### Gen Media：人和 agent 共用的素材 mini app

这是整篇里最有价值但也最难复刻的部分。它不是简单的生图 prompt，而是一个本地素材工作台：人能用，agent 也能用；生成结果进入 grid 和本地数据库；人物照片、品牌元素、参考缩略图可以复用。

它体现的是“AI 做前 90%，人做最后 10%”：agent 批量生成候选，人挑图、改字、调背景、定稿。

### Email Manager：高权限商务助理

它能读取 Gmail，过滤品牌合作，按优先级生成表格，再结合 Calendar 建议会议时间。这个模块的价值很高，但权限风险也高。

默认只允许 AI 读、整理、建议和起草。发送邮件、创建会议、承诺价格和档期都必须人工确认。

### Buffer Publisher：idea queue，而不是自动发布器

这个模块最适合轻量复刻。它只把最近聊天、研究和 memory 里的候选想法加到 Buffer 或内容看板里，防止好点子丢失。

第一版只做 idea 入库，不做自动发布。每条 idea 要带标题、角度、来源、适合平台和下一步动作。

## 最值得先复刻的 3 个

### 1. YouTube Researcher

这是最直接能产生价值的模块。你可以先选一个目标创作者，让 AI 拉取或读取 transcript，再生成：

- 5 个视频开头。
- 3 个短视频脚本。
- 一个长视频大纲。
- 一个“用某种讲法解释复杂概念”的版本。

关键不是抄句子，而是学习结构：如何开场、如何转折、如何举例、如何把抽象概念讲得清楚。

上游 Wiki：[[Wiki/AI视频制作/YouTube研究与脚本模仿|YouTube研究与脚本模仿]]

### 2. Readwise CLI

这个模块解决的是“我收藏了很多，但不知道怎么转成内容”。可复刻的最小版本是：

```text
读取我过去 7 天保存的内容，按共同主题生成 30 个选题。
每个选题都必须附原始来源链接。
```

这件事做稳定以后，再升级成每日或每周自动化。

上游 Wiki：[[Wiki/AI知识库/个人知识库到内容选题|个人知识库到内容选题]]

### 3. Excalidraw Diagrams

这个模块比 Paper、Remotion 更轻，能马上服务视频和课程。先让 AI 把一个主题变成 3-5 张低文本密度的讲解图，再手动改成你能讲的版本。

上游 Wiki：[[Wiki/AI视频制作/讲解图与视觉画布工作流|讲解图与视觉画布工作流]]

### 4. Buffer Publisher

它不负责创作，只负责防止想法丢失。让 agent 把最近聊天、研究和保存材料里的候选 idea 同步到 Buffer、Notion、Obsidian 或任何内容看板里。

这个模块适合轻量实现，因为风险小：只入库，不自动发布。

上游 Wiki：[[Wiki/AI营销自动化/AI一人营销团队#Buffer Publisher|AI一人营销团队：Buffer Publisher]]

## 不建议一开始就复刻的部分

Gen Media、Remotion / Hyperframes 和 Email Manager 都很有价值，但不适合作为第一步。

原因很现实：

- Gen Media 需要 API、素材库、本地数据库和人工二次编辑界面。
- Remotion / Hyperframes 需要视频模板、时间轴概念和反复视觉调试。
- Email Manager 涉及 Gmail、Calendar、品牌合作和自动发信，权限风险更高。

这些可以等 YouTube Researcher、Readwise、Buffer 这三个轻模块跑顺后，再逐步加。

## 这个案例真正有启发的地方

第一，它把 grounding 放在最前面。无论是 YouTube transcript，还是 Readwise 收藏，本质都是让 AI 不再凭空生成。

第二，它强调 skill 的演化方式：先做一次，满意后固化成 skill；多次稳定后，再变成 automation。

第三，它没有把人移出流程。Gen Media 的 mini app 思路尤其重要：AI 批量生成候选，人做最后 10% 的判断和微调。

第四，它把营销里的“重复劳动”和“品味判断”分开。重复劳动交给 agent，品味判断留给人。

## 可以立刻照做的最小版本

1. 建一个 `YouTube Researcher` prompt：给视频 URL 或频道，让 AI 总结表达结构并生成 5 个 hook。
2. 建一个 `Second Brain Ideas` prompt：读取最近收藏，生成带来源链接的 30 个选题。
3. 建一个 `Idea Inbox`：把选题同步到 Obsidian、Notion、Buffer 或简单 Markdown 文件。
4. 每周人工筛选 5 个进入脚本。
5. 把最好用的 prompt 固化成 skill。

## 参考来源

- [[Clippings/Codex Build Your Full AI Marketing Team (Agents + Skills)|Codex: Build Your Full AI Marketing Team]]：YouTube clipping，提供 8 个营销 skill / plugin / automation 的案例。
