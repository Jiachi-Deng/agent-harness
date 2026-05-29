---
type: wiki
status: compiled
area: Vibe Coding
topic: Vibe Coding
subtopic: AI内容自动化
source_title: "VIBE CODING FULL COURSE: Gemini 3.1 + Antigravity (6 Hrs)"
source_clipping: "Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md"
review_note: "Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md"
compiled: 2026-05-28
tags:
  - VibeCoding
  - ContentAutomation
  - SaaS
  - MultiAgent
  - Workflow
---

# 内容自动化分发SaaS产品模式

## 这个工作流解决什么

内容创作者最大的问题不是没有内容，而是同一份内容要反复改写成不同平台格式：X thread、LinkedIn post、Blog、短视频脚本、小红书笔记、邮件、公众号。大多数工具只做“分发”或只做“改写”，很容易产出平台味不对、语气不像本人、质量低的 AI 文案。

课程里的 `Splinter` 案例试图解决：一份 pillar content 进入系统，经过 voice/tone 配置和平台适配，生成多个平台可复制、可发布、可排期的内容。

## 输入与输出

| 类型 | 示例 |
| --- | --- |
| 输入 | blog post、article、transcript、notes、URL、未来可扩展 YouTube URL / 音频 |
| 配置 | 品牌语气、写作样例、默认 system prompt、目标平台 |
| 输出 | LinkedIn post、X thread、blog excerpt、短视频脚本、平台专属摘要 |
| 状态 | draft、generated、scheduled、published、failed |
| 商业动作 | 免费试用、积分消耗、订阅升级、API access |

## 模块拆分

这个案例的重点是复杂项目不要一锅炖。可以拆成 8 个模块：

| 模块 | 责任 | 优先模型 |
| --- | --- | --- |
| Landing Page | 价值主张、定价、案例、交互演示 | Gemini |
| Onboarding | 选择平台、设置 voice、输入样例 | Gemini + Claude Code |
| Content Ingestion | 粘贴文本、URL 抓取、未来音频/视频转写 | Claude Code |
| Voice Profile | 保存用户语气、写作样例、默认 prompt | Claude Code |
| Generation Engine | 按平台生成不同格式内容 | Claude Code |
| Platform Connections | LinkedIn 等平台 OAuth / API | Claude Code |
| Scheduling & Library | 内容库、排期、状态管理 | Claude Code |
| Billing & API Access | Stripe、订阅、积分、API key、webhook | Claude Code |

## 标准开发流程

1. **先做 Landing Page**：用强视觉 prompt 建一个能说明产品价值的外壳，不要一开始就让 AI 同时做复杂后端。
2. **让另一个模型写 spec**：包括技术栈、数据库、定价、认证、onboarding、voice model、API/webhook 架构。
3. **删掉不必要范围**：课程里就主动决定先不做完整 calendar 和所有平台连接，避免范围爆炸。
4. **先跑一条核心链路**：粘贴内容 -> 生成 LinkedIn/X/Blog 输出 -> 展示结果。
5. **再加入平台连接**：至少要求连接一个真实平台，验证 OAuth、redirect URI 和发布行为。
6. **加入计费/积分/订阅**：免费试用可以保留，但要在合适节点要求升级。
7. **补 API access 和 webhook**：给高级用户或 agent 调用能力。
8. **移动端优化 + 安全审计**：上线前最后处理可用性和安全。

## 关键产品判断

### 1. 免费试用要产生 wow moment

课程里保留了一个免费生成体验：用户可以先看到“我的内容真的被改成像样的 LinkedIn 文案”，再进入付费。这是 SaaS 转化里很重要的动作：先让用户感到价值，再让他付费。

### 2. Voice/tone 是护城河

普通改写工具会输出 AI 味很重的内容。这个案例把 voice profile、writing examples、system prompt 放在核心位置，说明真正的价值不是“多平台输出”，而是“像你本人一样输出”。

### 3. 平台接口会变，长期维护是产品能力

内容分发 SaaS 不是一次开发完就结束。LinkedIn、X、小红书、抖音、YouTube 等平台的 API、OAuth、发布规则、风控都会变。产品必须有“平台规则台账”和模块化适配能力。

### 4. Copy/paste 可能比全自动发布更稳

课程演示里有平台发布、webhook、API access，但对很多中文平台而言，完全自动发布可能受限。一个更稳的 MVP 可以先做“高质量生成 + 一键复制 + 排期提醒”，再逐步接官方 API。

## 安全与合规

- 平台 OAuth redirect URI 要区分 localhost 和线上域名。
- 每个平台连接状态要明确，不要把“可复制内容”和“已发布内容”混在一起。
- 用户生成内容、voice profile、平台 token 都是敏感数据。
- API key 和 webhook 必须鉴权，不能用示例域名或假 endpoint。
- 删除账号必须有确认弹窗和真正的数据处理逻辑。
- 内容自动发布要尊重平台 ToS，避免违规批量营销。

## 高频 Bug

- Onboarding 完成后跳转 dashboard 报错。
- 平台 redirect URI 仍指向 localhost。
- 生成内容成功但 credits 没扣。
- 显示“已发布”，实际只是生成了可复制文本。
- 用户设置保存后刷新丢失。
- Webhook 没发送，或发送到错误域名。
- API access 示例 URL 不是线上真实域名。
- 支付成功后没有更新订阅状态。

## 可迁移方向

- 小红书/抖音/公众号内容再加工工作台。
- 长视频转短视频脚本和标题工具。
- 播客/直播转多平台内容工具。
- 企业品牌内容审批与分发系统。
- 课程讲师“一课多发”内容流水线。

## 可生成 Outputs

- `内容自动化分发 SaaS 产品蓝图`
- `一份内容变多平台内容的 AI 工作流`
- `内容工具从免费试用到付费转化的设计`

## 证据锚点

- 原始 transcript：04:50:50-05:53:32，Splinter 产品、pillar content、多平台输出、onboarding、平台连接、支付、API、webhook、安全审计。
- NotebookLM 审片记录：模块六 `内容自动化分发 SaaS`。
