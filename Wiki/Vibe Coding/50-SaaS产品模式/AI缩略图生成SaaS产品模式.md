---
type: wiki
status: compiled
area: Vibe Coding
topic: Vibe Coding
source_title: "VIBE CODING FULL COURSE: Gemini 3.1 + Antigravity (6 Hrs)"
source_clipping: "Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md"
review_note: "Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md"
compiled: 2026-05-28
tags:
  - VibeCoding
  - SaaS
  - AIImage
  - Thumbnail
  - Stripe
  - Credits
---

# AI缩略图生成SaaS产品模式

## 案例定位

这是课程里从“能用的 SaaS”升级到“能收费的 SaaS”的关键项目。它做的是 AI 缩略图生成工具：用户上传参考图和自己的脸图，输入生成提示词，系统调用 AI 图像 API 生成多个缩略图选项，用户选择、保存、下载，同时消耗积分。

它的教学价值不在缩略图本身，而在这几个能力的组合：登录、积分、支付、文件上传、AI API、结果保存、下载、移动端优化和安全审计。

## 用户与付费逻辑

目标用户是 YouTuber、自媒体团队、短视频运营、内容工作室。缩略图工具适合用积分制，因为每次生成都会产生明确 API 成本。

课程里梳理了三种付费模型：

| 模型 | 适合场景 | 课程判断 |
| --- | --- | --- |
| 一次性购买 | 模板、永久授权、小工具 | 简单，但不适合持续消耗 API 的产品 |
| 订阅制 | 持续访问 SaaS，按月/年收费 | 适合工具平台，但要设计权益 |
| 积分制 | 每次生成、抓取、调用 API 都有成本 | 最适合缩略图生成和线索抓取 |

## 核心用户流程

```text
Landing Page
  -> 注册/登录
  -> 选择积分包或套餐
  -> Stripe Checkout
  -> Webhook 更新用户积分
  -> 上传参考脸图/风格图
  -> 输入 prompt
  -> 生成 3 个缩略图候选
  -> 选择并保存
  -> 下载或继续生成
```

## 关键模块

| 模块 | 作用 | 验收标准 |
| --- | --- | --- |
| Landing Page | 讲清楚“零 Photoshop 做高点击缩略图” | CTA 能正确带上 plan 参数 |
| Auth | 用户注册、登录、私密 dashboard | 未登录不能进入 dashboard/generate/settings |
| Payment | Stripe checkout + webhook | 付款成功后积分正确入库 |
| Credits | 生成前检查积分，生成后扣减 | 0 积分用户跳转充值 |
| Settings | 上传脸图、保存默认 prompt | 刷新后配置仍存在 |
| Generate | 上传 inspiration thumbnail，输入 prompt，生成多个候选 | 结果可预览、选择、保存 |
| Library | 查看历史缩略图 | 用户只能看自己的结果 |
| Download | 下载选中的图片 | 链接权限正确，文件可用 |

## 课程里的真实调试点

这个项目非常适合做“AI 生成 SaaS 常见坑”案例：

- 登录页一开始只要 email，没有 password，和 Supabase Auth 不匹配。
- Stripe 支付成功后，应用无法把付款结果映射回用户，导致用户一直被送回 payment 页。
- 用户 0 credits 时没有被正确拦截。
- 上传脸图后刷新丢失，说明设置没有正确保存到数据库。
- 错误提示不准确，把缺少 reference face 报成缺少 inspiration image/prompt。
- 从本地到 Netlify 后，生成时间超过 serverless timeout，导致线上报错。
- 为修支付逻辑引入每页重复数据库请求，造成页面明显变慢，需要缓存/数据刷新策略。

## 安全重点

- Stripe secret key 和 webhook secret 必须在服务端环境变量中。
- Webhook 必须验证签名，不能信任前端告诉你“我付过钱”。
- 积分扣减必须服务端执行，不能让前端控制。
- 文件上传要校验类型、大小和权限。
- 用户只能访问自己的图片和生成记录。
- AI 图像 API 调用要限流，防止被刷。
- 生成成本、积分价格、失败退款/重试策略要提前设计。

## 产品化启发

缩略图 SaaS 的核心卖点不是“能生成图”，而是：

- 节省设计师时间。
- 降低每张图成本。
- 用 A/B 候选提升点击率。
- 保持创作者个人形象和频道风格一致。
- 从“上传参考 + 个性化 prompt + 批量候选”变成稳定生产流程。

课程后面定价模块用缩略图举例：如果用户原本每张缩略图要花钱或花 2 小时，工具能省下直接成本和机会成本，就可以按创造价值的一小部分定价，而不是按你的开发时间定价。

## 可生成 Outputs

- `积分制 AI 工具 SaaS 怎么设计`
- `Stripe + Supabase + AI API 的新手产品流程图`
- `AI 图片生成工具上线前安全检查清单`

## 证据锚点

- 原始 transcript：03:49:20-04:49:49，支付模型、Stripe、积分制、缩略图生成、线上 timeout、安全审计。
- NotebookLM 审片记录：模块五 `AI 缩略图生成 SaaS`。
