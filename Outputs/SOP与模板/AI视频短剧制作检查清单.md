---
type: output
output_type: sop
status: review-ready
target_reader: "AI 视频创作者、短剧账号操盘手、独立开发者、课程学员"
use_case: "用 AI 处理口播剪辑、动态图形、短剧分镜和视频生成"
version_date: 2026-05-28
updated: 2026-05-29
upstream_wiki:
  - "[[Wiki/AI视频制作/AI视频剪辑与动态图形工作流|AI视频剪辑与动态图形工作流]]"
  - "[[Wiki/AI视频制作/ComfyUI本地视频生成入门|ComfyUI本地视频生成入门]]"
  - "[[Wiki/AI视频制作/AI短剧与漫剧制作流水线|AI短剧与漫剧制作流水线]]"
references:
  - "[[Clippings/Claude Video Editing Just Became Unrecognizable|Claude Video Editing Just Became Unrecognizable]]"
  - "[[Clippings/Claude + CapCut Completely Changes Everything For Editors- Full Tutorial|Claude + CapCut Completely Changes Everything For Editors]]"
  - "[[Clippings/Codex Just Replaced 1,000 Hours of Video Editing Tutorials|Codex Just Replaced 1,000 Hours of Video Editing Tutorials]]"
  - "[[Clippings/Ultimate Beginner Guide to Learning ComfyUI (2026)|Ultimate Beginner Guide to Learning ComfyUI (2026)]]"
  - "[[Clippings/完整的多 Agent 多 Skill 小说改编影视流水线系统。|Supreme-Ultimate/novel-to-script-team]]"
  - "Bilibili 即梦AI提示词书写技巧：待补可回查 clipping；当前只作为来源线索，不作为已验证引用。"
---

# AI视频短剧制作检查清单

维护备注：本清单现在对齐三条上游主线：[[Wiki/AI视频制作/AI视频剪辑与动态图形工作流|AI视频剪辑与动态图形工作流]] 负责粗剪、动效、时间轴和 render；[[Wiki/AI视频制作/ComfyUI本地视频生成入门|ComfyUI本地视频生成入门]] 负责本地模型、节点、素材生成和放大；[[Wiki/AI视频制作/AI短剧与漫剧制作流水线|AI短剧与漫剧制作流水线]] 负责故事、分集、剧本、角色连续性和分镜。Remotion / Hyperframes 不再作为独立工具页维护，后续动态图形、overlay、B-roll、产品演示和 launch video 的新材料先回填到剪辑动效主页面。

## 1. 先选任务类型

- 口播剪辑：目标是去停顿、去口误、补字幕和动态图形。
- 产品发布视频：目标是品牌化 motion graphics、logo、mockup、音乐和短 CTA。
- 短剧/漫剧：目标是剧本、分镜、角色资产、场景资产和连续镜头。
- 素材生成：目标是角色图、场景图、B-roll、首帧/尾帧或 overlay。

## 2. 口播剪辑

- 原始视频已放进独立项目文件夹。
- 第一轮只做粗剪，不加复杂动效。
- 已导出 edited MP4。
- 已生成带时间戳 transcript。
- 动态图形按 beat 规划，而不是泛泛要求“更高级”。
- 每个 beat 有 anchor word、开始时间、结束时间和画面位置。
- render 前已检查遮脸、字幕遮挡、裁切错误、音量异常。

## 3. 动态图形

- 已决定用 Remotion、Hyperframes、CapCut，还是组合使用。
- 有参考图、品牌色、字体、logo 和素材目录。
- 已先创建可复用 brand assets / style reference。
- 如果用 Remotion / Hyperframes，先做 5-20 秒短 overlay、开场或 B-roll，不直接做完整长视频。
- 已理解 composition、scene、render、transparent background 这些基本交付词。
- 每次只改 1-3 个具体问题。
- 反馈尽量数值化：速度 2 倍、尺寸 +10%、饱和度 -50%。
- 需要叠加到剪辑软件时，已要求透明背景。
- render 前先用 preview / screenshot 检查遮挡、重叠和文字密度。
- 音乐、字体、logo 和地图素材已检查授权。

## 4. ComfyUI 素材

- 确认本地显卡或云 GPU 成本。
- 模型放在正确目录，能在下拉菜单里选到。
- Custom nodes 已安装并重启。
- 先用短帧数、低分辨率测试。
- 视频预览节点可用。
- 需要最终质量时再接 upscaler。
- 保存 workflow，不只保存输出文件。

## 5. 短剧/漫剧

- 原始故事已经做改编分析。
- 已拆分集，不是直接把全文塞给模型。
- 每集有开头钩子、核心冲突、结尾悬念。
- 已检查 Show Don't Tell。
- 已记录角色、称呼、道具、时间线和伏笔。
- 已拆角色、场景、道具提示词。
- 每个镜头都有景别、机位、动作、时长、首帧/尾帧要求。
- 生成失败和有效 prompt 已回写模板。

## 6. 提示词结构

图像/关键帧提示词优先按这个顺序写：

```text
风格 + 视角 + 主体 + 背景 + 细节 + 光影 + 质量词
```

额外检查：

- 重点词放在开头或结尾。
- 中间信息保持清晰，不堆长句。
- 有正向要求，也有反向排除。
- 多轮改图出现脸崩或细节漂移时，重开会话或重新固定参考图。

## 7. 最终发布前

- 看完整片，而不是只看单个生成片段。
- 检查字幕错字、口型、音量、转场、画面闪烁。
- 检查人物一致性和场景连续性。
- 检查素材授权、平台合规和敏感内容。
- 把有效流程沉淀到 Wiki 或项目模板。
