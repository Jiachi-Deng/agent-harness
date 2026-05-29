---
type: wiki
status: compiled
area: AI视频制作
tags:
  - video-editing
  - motion-graphics
  - Remotion
  - Hyperframes
  - CapCut
  - Codex
  - Claude
updated: 2026-05-29
absorbed_from_title:
  - "Remotion与Hyperframes视频动画"
absorbed_on: 2026-05-28
---

# AI视频剪辑与动态图形工作流

## 解决什么问题

把一段口播、产品录屏或素材片段，做成能发布的视频，通常卡在三个地方：粗剪很耗时间，动态图形很难做，风格一致性靠手工记忆。Claude / Codex 加 Remotion、Hyperframes、CapCut 的价值，不是让 AI 一次做完整大片，而是把剪辑拆成可检查的阶段：

1. 先把原始视频转成带时间戳的 transcript。
2. 再剪掉停顿、口误、重复和 filler words。
3. 用 transcript 的词级时间点规划 motion beats。
4. 用 Remotion / Hyperframes 生成 overlay、动态图形、字幕、背景和转场。
5. 放进 CapCut / Premiere / Final Cut 做最后人工检查和发布版本。

## 适合谁

- 做 YouTube、B 站、小红书、课程视频的个人创作者。
- 做产品 launch video、功能更新视频、社媒短视频的独立开发者。
- 想把固定风格沉淀成模板，而不是每次从零剪辑的人。
- 已经会基本剪辑，但不会 After Effects / motion graphics 的用户。

不适合完全不看成片、只想一键批量发布的人。当前这类流程仍需要人工审片、改节奏、检查字幕和视觉遮挡。

## 先选路线

这页现在是 AI 视频剪辑和动态图形的主页面。Remotion / Hyperframes 不再单独维护为工具页，而是作为不同生产路线里的动效模块。

它负责“时间轴上的视频生产”：粗剪、字幕、motion beats、overlay、转场、render 和最终发布版。视频前期的讲解图、视觉稿、缩略图、landing page 视觉方向回到 [[Wiki/AI视频制作/讲解图与视觉画布工作流|讲解图与视觉画布工作流]]；角色图、场景图、短镜头生成工具回到 [[Wiki/AI视频制作/ComfyUI本地视频生成入门|ComfyUI本地视频生成入门]]；短剧剧情、分集和分镜规格回到 [[Wiki/AI视频制作/AI短剧与漫剧制作流水线|AI短剧与漫剧制作流水线]]。

| 任务 | 优先路线 | 关键判断 |
| --- | --- | --- |
| 口播短视频粗剪 + 动效 | Claude + video-use + Hyperframes | 先要 edited video 和词级 transcript，再做 motion beats |
| CapCut 里叠加高级素材 | Claude + Remotion + CapCut | AI 生成 LUT / SRT / overlay，CapCut 做最终时间线 |
| 产品发布或品牌 launch video | Codex + Remotion plugin | 先建 brand assets，再按 scene / sequence 做短片 |
| 只需要最终剪辑和发布版 | CapCut / Premiere / Final Cut | AI 只做素材和计划，不替代人工审片 |

## 三种可复用路线

### 路线 A：Claude + video-use + Hyperframes

适合把口播原片做成带动态图形的短视频。

基本流程：

1. 新建一个项目文件夹，放入 raw video。
2. 让 Claude / Claude Code 读取 video-use 和 Hyperframes 项目或 skill。
3. 第一轮只做粗剪：去掉停顿、口误、重复、filler words。
4. 检查导出的 edited MP4 和 transcript JSON。
5. 用语音或文字写 motion brief：第几秒出现什么卡片、图形、字幕、布局变化。
6. 先让 AI 出 plan，确认每个 beat 的时间、锚点词、位置和视觉风格。
7. 再生成 Hyperframes motion graphics。
8. 用 preview / screenshots / timeline editor 修遮脸、重叠、背景网格、裁切错误。
9. render 成最终视频，放入剪辑软件或发布流程。

关键点：一定要有词级时间戳。动态图形不是“好看就行”，而是要跟说话内容同步。

### 路线 B：Claude + Remotion + CapCut

适合做可导入 CapCut 的素材：LUT、SRT 数字动画、透明背景 overlay、搜索框、highlight、地图动画等。

基本流程：

1. 免费 Claude 可以先生成 `.cube` LUT 或 `.srt` 字幕素材。
2. 在 CapCut 里导入 LUT / SRT，调整强度、字体、颜色、速度和 compound clip。
3. 需要复杂动效时，切到 Claude Code / co-work，安装 Node.js 和 Remotion 项目。
4. 给 Claude 参考图和用途，让它生成 Remotion composition。
5. 用数值化反馈迭代：例如速度提升 3 倍、glow 降低 50%、尺寸放大 10%。
6. 需要 overlay 时要求透明背景，再 render 导入 CapCut。
7. CapCut 负责最后的时间线、剪辑、音乐、字幕和发布版本。

这条路线的强项是“AI 生成专业素材，CapCut 做最终编辑”。不要强行让 Claude 替代整个剪辑软件。

### 路线 C：Codex + Remotion plugin

适合做产品发布视频、社媒 motion graphic、品牌化 launch video。

基本流程：

1. 在 Codex 里新建视频项目，安装 Remotion plugin。
2. 从 `hello world` 开始，先确认本地 Remotion preview 能打开。
3. 把 logo、截图、品牌图形、音乐等素材放入项目 assets。
4. 先创建 brand assets composition：logo、渐变背景、品牌图形、mockup、常用颜色。
5. 再按 scene / sequence 写 prompt，逐段生成视频。
6. 用截图标注具体问题，要求 agent 改线条、icon、转场、文字动画。
7. 音乐可以先用 Suno 等工具生成，再作为 MP3 加入全片。
8. 最终在 Remotion 里 render 为 MP4。

关键点：先做品牌资产库，再做具体视频。这样后续每条 launch video 都能复用同一套视觉语言。

## Remotion / Hyperframes 使用判断

原来的 `Remotion与Hyperframes视频动画` 已并入本页。融合后的主结论是：Remotion / Hyperframes 不应该孤立成一个“生成动画”工具页，它们更适合放在视频生产线中段，作为动态图形、overlay、B-roll、产品演示和 launch video 的生成模块。

更稳妥的使用判断：

- 如果已有 Remotion 模板、React 代码基础或 Codex Remotion plugin，优先复用 Remotion。
- 如果追求更强 motion physics、timeline editor 或现成视觉能力，可以单独评估 Hyperframes。
- 不要把创作者口头说法直接当成通用结论；正式工具比较需要再查官方文档、价格、导出能力和实测结果。
- 它们不能替代最终剪辑软件。更合理的流程是：先生成 overlay / motion assets，再导入 CapCut / Premiere / Final Cut 做最终剪辑。

## 和视觉画布的边界

讲解图 / 视觉画布解决的是“画面结构是什么”，剪辑和动态图形解决的是“它什么时候出现、怎么动、怎么和音画同步”。

| 问题 | 进入视觉画布页 | 进入剪辑动效页 |
| --- | --- | --- |
| 一个概念怎么画成 3-5 张图 | 是 | 否 |
| landing page / 缩略图视觉方向 | 是 | 否 |
| 视频第 12 秒出现什么卡片、从哪飞入 | 否 | 是 |
| overlay 是否遮脸、字幕是否挡 UI | 否 | 是 |
| Remotion composition、scene、render | 否 | 是 |
| 输出 PNG / SVG / 视觉稿 | 是 | 否 |
| 输出 MP4 / 透明背景 overlay / 时间轴素材 | 否 | 是 |

适合的任务：

- 软件产品 launch video。
- iOS / Web app 的 UI 演示动画。
- YouTube 开场里的章节 outline。
- 视频中段的图形 overlay。
- B-roll 动效素材。
- 可复用的 motion template。

## 操作指令骨架

### 粗剪

```text
请只做第一阶段粗剪。

素材：
[raw video 文件名]

目标：
1. 分析 transcript。
2. 删除明显停顿、口误、重复、false start、filler words。
3. 尽量按 word boundary 裁切，保留自然呼吸。
4. 输出 edited MP4。
5. 同时输出带词级时间戳的 transcript JSON。

先不要添加动态图形。
```

### 动态图形 plan

```text
请先进入 planning，不要直接实现。

素材：
[edited video + transcript JSON]

我需要添加 motion graphics：
1. [第一个画面目标]
2. [第二个画面目标]
3. [第三个画面目标]

请输出：
- 每个 beat 的开始和结束时间
- 对应 transcript anchor word
- 画面位置，不能遮挡人物脸部
- 文案和字号
- 动画方式
- 需要我确认的问题
```

### 视觉修正

```text
这版 timing 基本正确，但视觉需要修：

1. [具体 beat] 遮挡了 [人物脸 / 字幕 / 产品 UI]，请缩小或移动。
2. [具体元素] 颜色太抢，请降低饱和度 40%。
3. [具体转场] 太慢，请把动画时间缩短到 0.6 秒。
4. 全片不要出现额外 grid / debug overlay。

请先截图自检，再给我 render。
```

### Remotion / Hyperframes overlay

```text
请用 Remotion / Hyperframes 做一个视频 overlay。

用途：
[YouTube 开场 / 产品演示 / B-roll / 章节 outline]

素材：
[脚本、截图、产品名称、7 个要点]

要求：
1. 创建一个新的 composition。
2. 在同一个 composition 里做 4 个 scene 变体。
3. 第一个参考我已有模板，其余三个可以更有创意。
4. 控制文字量，避免重叠。
5. 支持我用截图继续反馈修改。
6. 最终渲染成本地视频文件。
```

## 检查清单

- 原始素材和项目文件夹是否分开保存。
- 是否先粗剪，再做动效，而不是一次性全自动。
- transcript 是否带词级或至少句级时间戳。
- 每个 motion beat 是否有 anchor word。
- 动画是否遮挡脸、字幕、产品 UI。
- 是否有 brand assets / style markdown / reference composition。
- 是否把 API key 放进 `.env`，没有贴进聊天。
- 是否 render 前做过截图或 preview 检查。
- 是否保留可复用模板，而不是只导出一次性视频。
- 如果使用 Remotion / Hyperframes，是否先做短 overlay 或开场片段，而不是直接做完整长视频。
- 如果使用 Remotion / Hyperframes，是否理解 composition / scene / render 这些基本词，能给出精确反馈。

## 常见坑

- 把“AI 会剪辑”理解成不需要审片。当前流程最容易出错的是遮挡、裁切、字幕同步和节奏。
- 只说“做得高级一点”，不给参考图、时间点和用途。
- 没有先建立风格模板，导致每条视频风格漂移。
- 让 agent 直接 render 每一版，浪费 token 和时间。应该先 preview 和 plan。
- 使用地图、字体、logo、音乐时不检查授权和导出限制。
- 把 API key 粘进聊天记录，而不是 `.env`。
- 文字太多，动效再好也不好看。
- 把视觉画布问题误交给剪辑工具，导致只是“动起来”但结构仍然讲不清。
- 把时间轴问题误交给画布工具，导致视觉稿好看但不能和 transcript、字幕、口播节奏同步。

## 与其它页面的关系

- [[Wiki/AI视频制作/讲解图与视觉画布工作流|讲解图与视觉画布工作流]]：负责前期视觉结构、讲解图、缩略图和可编辑画布。
- [[Wiki/AI视频制作/ComfyUI本地视频生成入门|ComfyUI本地视频生成入门]]：负责生成角色图、场景图、B-roll、关键帧和短镜头素材。
- [[Wiki/AI视频制作/AI短剧与漫剧制作流水线|AI短剧与漫剧制作流水线]]：负责短剧故事、分集、剧本、分镜和镜头规格。

## 可生成 Outputs

- SOP：AI 口播视频从粗剪到动态图形的检查清单。
- 教程：用 Claude / Codex 做一个产品 launch video。
- 工具比较：Remotion、Hyperframes、CapCut、After Effects 的边界。
- 课程练习：同一段 raw video 做三版 motion style。

## 来源

- [[Clippings/Claude Video Editing Just Became Unrecognizable|Claude Video Editing Just Became Unrecognizable]]：提供 Claude + video-use + Hyperframes 的端到端口播剪辑流程、词级 transcript、motion beat planning、截图自检和 token 成本提醒。
- [[Clippings/Claude + CapCut Completely Changes Everything For Editors- Full Tutorial|Claude + CapCut Completely Changes Everything For Editors]]：提供 LUT、SRT 数字动画、Remotion overlay、透明背景导入 CapCut、数值化迭代等素材制作方法。
- [[Clippings/Codex Just Replaced 1,000 Hours of Video Editing Tutorials|Codex Just Replaced 1,000 Hours of Video Editing Tutorials]]：提供 Codex + Remotion plugin、brand assets、scene/sequence、音乐导入和 launch video 的案例。
- [[Clippings/Codex Build Your Full AI Marketing Team (Agents + Skills)|Codex: Build Your Full AI Marketing Team]]：Remotion & Hyperframes 模块展示了用时间点、composition、scene、截图反馈和 render 做视频动画的过程。
- 已吸收旧页标题：`Remotion与Hyperframes视频动画`。
