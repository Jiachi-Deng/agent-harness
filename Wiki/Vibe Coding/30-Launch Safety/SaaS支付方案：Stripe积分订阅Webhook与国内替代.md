---
type: wiki
status: compiled
area: Vibe Coding
topic: Vibe Coding
compiled: 2026-05-28
verified: 2026-05-28
refresh_after: 2026-06-28
refresh_reason: "支付地区、接口、订阅/webhook 事件、微信支付和支付宝签约要求变化快"
tags:
  - VibeCoding
  - SaaS
  - Payments
  - Stripe
  - Credits
  - Webhooks
  - WeChatPay
  - Alipay
upstream_wiki:
  - "Wiki/Vibe Coding/50-SaaS产品模式/AI缩略图生成SaaS产品模式.md"
  - "Wiki/Vibe Coding/50-SaaS产品模式/API包装型SaaS机会与风险.md"
  - "Wiki/Vibe Coding/40-Business/Vibe Coding商业化与定价包装.md"
official_refs:
  - "https://docs.stripe.com/payments/checkout/how-checkout-works"
  - "https://docs.stripe.com/payments/checkout/build-subscriptions"
  - "https://docs.stripe.com/billing/subscriptions/webhooks"
  - "https://stripe.com/global"
  - "https://pay.wechatpay.cn/doc/v3/merchant/4012791897"
  - "https://open.alipay.com/module/webApp"
  - "https://opendocs.alipay.com/open/270/105899"
---

# SaaS支付方案：Stripe积分订阅Webhook与国内替代

## 这个页面解决什么

Vibe Coding 做到 SaaS 阶段后，最容易误判的是支付：页面跳到收银台不等于商业化完成。真正要解决的是：

- 用户付了多少钱。
- 购买的是一次性积分、月订阅还是套餐权益。
- 支付成功后，系统如何可靠开通权益。
- 失败、退款、重复通知、取消订阅时怎么处理。
- 中国大陆用户是否能顺利付款，开发者是否能合规收款。

结论先放前面：**海外 SaaS 优先用 Stripe Checkout + Webhook；有明确消耗成本的 AI/API 工具优先做积分制；长期访问权益可以做订阅；面向中国大陆收款时，Stripe 不是默认答案，要评估微信支付、支付宝或合规服务商方案。**

## 三种常见计费模型

| 模型 | 适合产品 | 用户感受 | 技术重点 |
| --- | --- | --- | --- |
| 一次性购买 | 模板、课程、报告、固定交付包 | 买一次拿结果 | 订单表、下载权限、退款 |
| 积分制 | AI 生图、线索抓取、转写、数据补全、邮件发送 | 用多少扣多少 | 积分流水、余额检查、失败回滚 |
| 订阅制 | 内容工作台、自动化平台、团队 SaaS、持续服务 | 按月/年持续访问 | 订阅状态、续费失败、取消和客户门户 |

判断规则：

- 每次调用都有明确 API 成本，用积分制。
- 用户付费买持续访问，用订阅制。
- 交付物固定、没有持续成本，用一次性购买。
- 可以组合：订阅给每月额度，超额再买积分包。

## Stripe 推荐架构

Stripe 官方 Checkout 支持一次性付款和订阅，可以用托管页、嵌入页或自定义组件收款。对 Vibe Coding 新手来说，优先用 Checkout 托管页，减少自己处理卡号、3DS、错误状态和支付方式的风险。

标准链路：

```text
Pricing Page
  -> 服务端创建 Checkout Session
  -> 用户跳转 Stripe Checkout
  -> Stripe 收款
  -> Webhook 通知应用
  -> 应用验证签名
  -> 更新 order / credits / subscription
  -> 用户回到 success page
```

不要用 success page 的前端跳转直接开通权益。前端只能提示“支付处理中”，最终权益以 webhook 和数据库为准。

## 积分制设计

适合课程里的 AI 缩略图、线索挖掘、内容生成 API 这类产品。

### 最小数据表

| 表 | 作用 | 关键字段 |
| --- | --- | --- |
| `credit_packages` | 积分包配置 | `id`, `name`, `credits`, `price_id`, `active` |
| `orders` | 支付订单 | `id`, `user_id`, `stripe_session_id`, `status`, `amount`, `package_id` |
| `credit_ledger` | 积分流水 | `id`, `user_id`, `delta`, `reason`, `source_id`, `created_at` |
| `usage_jobs` | 消耗任务 | `id`, `user_id`, `cost_credits`, `status`, `provider_cost` |

### 积分扣减规则

- 生成前先检查余额。
- 扣减在服务端完成。
- 高成本任务建议先冻结积分，再在成功后确认扣减。
- 失败任务要有退款或重试规则。
- 每一笔增减都进 `credit_ledger`，不要只维护一个余额数字。

### 必须防的坑

- 支付 webhook 重试导致重复加积分。
- 用户 0 积分时绕过前端直接打生成 API。
- 生成失败但积分被扣。
- 同时打开多个页面并发扣积分导致余额为负。
- 用 Stripe session 的前端返回结果直接加积分。

## 订阅制设计

Stripe 官方订阅集成建议用 Checkout 创建订阅，并用 webhook 处理 `checkout.session.completed`、`invoice.paid`、`invoice.payment_failed` 等事件。订阅状态会异步变化，不能只在用户支付完成那一刻写一次数据库。

### 最小数据表

| 表 | 作用 | 关键字段 |
| --- | --- | --- |
| `plans` | 套餐 | `id`, `name`, `stripe_price_id`, `monthly_credits`, `features` |
| `subscriptions` | 用户订阅状态 | `user_id`, `stripe_customer_id`, `stripe_subscription_id`, `status`, `current_period_end` |
| `entitlements` | 功能权益 | `user_id`, `feature`, `source`, `expires_at` |
| `webhook_events` | 幂等记录 | `stripe_event_id`, `type`, `processed_at` |

### 状态处理

- `active`：允许访问套餐权益。
- `trialing`：按试用规则开通。
- `past_due`：提示更新付款方式，可保留短 grace period。
- `canceled` / `unpaid`：撤销或降级权益。
- `invoice.paid`：续费成功，延长权益。
- `invoice.payment_failed`：续费失败，通知用户并引导到 customer portal。

## Webhook 是支付系统的核心

Webhook 不是可选增强项，而是支付系统的事实来源。

最低要求：

- 验证 webhook 签名。
- 记录 `event_id` 防重复处理。
- 根据事件类型分支处理。
- 先查订单/用户，再开通权益。
- 所有失败写日志，允许人工补单。
- 不要在 webhook 里做太慢的生成任务，只做状态变更和入队。

推荐处理顺序：

```text
收到 webhook
  -> 验证签名
  -> 检查 event_id 是否处理过
  -> 解析 checkout/session/invoice/subscription
  -> 找到本地 user/order/subscription
  -> 在事务中更新权益或积分流水
  -> 标记 event processed
  -> 返回 2xx
```

## 中国大陆收款的现实判断

Stripe 官方全球可用地区列表包含 Hong Kong 等地区，但不等于中国大陆主体能直接开 Stripe 账户收款。面向中国大陆用户时，不能默认用 Stripe 解决所有问题。

### 微信支付

微信支付官方 V3 文档提供 JSAPI/小程序下单能力，适合微信内网页、小程序和公众号场景。官方接口要求商户号、appid、签名认证、订单号、金额、通知地址等。

适合：

- 微信生态内购买。
- 小程序、公众号、企微私域导流后的付款。
- 面向中国大陆小企业客户的人民币收款。

注意：

- 需要商户资质和商户号。
- 需要处理签名、证书、公钥、回调通知。
- 微信 JSAPI 更适合微信内打开，不是所有浏览器场景都顺。
- 订阅式自动扣费、分账、退款等能力要逐项核对是否已开通。

### 支付宝

支付宝开放平台提供网页和移动应用接入入口，常见方向包括电脑网站支付、手机网站支付、当面付、小程序支付等。实际接入前必须根据自己的主体、产品和收款场景确认可签约产品。

适合：

- PC 网站和移动网页付款。
- 中国大陆用户更熟悉的支付宝收银台。
- 课程、模板、工具、服务类产品的一次性付款。

注意：

- 需要开放平台应用、商户签约、密钥和回调配置。
- 不同支付产品的 API、风控和签约要求不同。
- 境外主体、跨境收款和人民币结算要单独核对。

### 不建议走的路

- 个人收款码伪装成 SaaS 支付系统。
- “免签约”支付、Cookie 代付、逆向收款。
- 付款截图人工开通但没有订单流水。
- 没有发票、退款、争议处理和客户身份记录。

这些方案短期看快，长期会让产品无法规模化，也很难支撑课程、客户交付或正式 SaaS。

## 新手推荐选型

| 场景 | 推荐 |
| --- | --- |
| 海外用户、信用卡、订阅 SaaS | Stripe Checkout + Webhook + Customer Portal |
| AI/API 消耗型工具 | Stripe 积分包，或国内微信/支付宝积分包 |
| 中国大陆用户、小程序/公众号入口 | 微信支付 JSAPI/小程序支付 |
| 中国大陆用户、网页工具/课程/模板 | 支付宝网页支付 + 微信支付 H5/Native 备选 |
| 不确定产品是否成立 | 先人工收款或表单报价，等有真实需求再自动化 |

## 可生成 Outputs

- `积分制 AI 工具支付设计模板`
- `Stripe + Supabase 支付安全检查清单`
- `中国大陆 SaaS 收款方案选择表`

## 证据锚点

- Stripe Checkout 官方文档：`https://docs.stripe.com/payments/checkout/how-checkout-works`
- Stripe 订阅 Checkout 官方文档：`https://docs.stripe.com/payments/checkout/build-subscriptions`
- Stripe 订阅 Webhook 官方文档：`https://docs.stripe.com/billing/subscriptions/webhooks`
- Stripe 全球可用地区：`https://stripe.com/global`
- 微信支付 JSAPI/小程序下单官方文档：`https://pay.wechatpay.cn/doc/v3/merchant/4012791897`
- 支付宝开放平台网页/移动应用入口：`https://open.alipay.com/module/webApp`
- 原课程案例：`Wiki/Vibe Coding/50-SaaS产品模式/AI缩略图生成SaaS产品模式.md`
