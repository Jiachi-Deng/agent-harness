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
  - LeadGeneration
  - Apify
  - Outbound
  - APIWrapper
---

# 线索挖掘SaaS产品模式

## 案例定位

这是课程里的第三个产品：一个面向 B2B 获客的线索挖掘 SaaS。它不是从零写爬虫，而是用一个漂亮、可登录、可配置、可导出、可收费的 SaaS 外壳，把 `Apify` 这类第三方爬虫服务、邮箱 enrichment 服务、大模型个性化文案能力包装起来。

它的商业价值在于：很多企业不缺“发邮件工具”，缺的是稳定获得目标客户线索、补全联系方式、生成足够个性化的 cold email 开场白。

## 目标用户

- 做海外 B2B outbound 的营销团队。
- 想找本地商家、垂直行业客户、LinkedIn/Google Maps 线索的销售团队。
- 独立开发者或自动化服务商，想把爬虫/线索 API 包装成可售卖工具。
- 不适合没有合规意识、想无脑群发垃圾邮件的人。

## 核心功能

| 功能 | 课程里的实现思路 | 用户价值 |
| --- | --- | --- |
| Landing Page | 讲清楚 scrape、enrich、personalize、export 的价值 | 获取注册和付费转化 |
| 登录/注册 | Supabase Auth 或等价 auth | 保存用户配置和订单历史 |
| API 配置页 | 用户输入 Apify、Anthropic/OpenAI、邮箱 finder 等 key | 允许用户用自己的额度跑任务 |
| Prompt 配置 | 用户自定义 icebreaker / personalization prompt | 控制个性化邮件语气和质量 |
| 线索抓取表单 | 输入行业、地区、职位、数量等条件 | 把自然语言需求变成爬虫过滤条件 |
| Enrichment | 补全邮箱、公司、职位等字段 | 提高线索可用率 |
| AI 个性化 | 为每条线索生成 1-2 句开场白 | 提高 cold email 回复率 |
| CSV 导出 | 下载结果表格 | 对接 CRM、邮件系统、人工二次筛选 |
| 历史订单 | 查看过去任务、参数、结果和下载链接 | 形成真实 SaaS 工作台 |

## 开发闭环

这个案例展示了一个典型 API wrapper SaaS 的闭环：

1. 先画粗略信息架构：落地页、注册页、配置页、抓取页、订单历史页。
2. 找一个同类或相邻产品页面，作为 AI 生成 landing page 和 dashboard 的视觉参考。
3. 先做可点击原型，用 mock 数据跑通登录、配置、抓取、订单历史。
4. 接入 `Apify` actor，把用户输入转成爬虫请求。
5. 接入 enrichment 和大模型 API，把原始线索补全并生成个性化字段。
6. 存入数据库，允许用户查看订单详情和下载 CSV。
7. 上线到 Netlify，绑定 GitHub，配置环境变量。
8. 跑安全审计，修复认证绕过、依赖幻觉、API route 权限和 RLS 问题。

## 关键洞察

### 1. 软件界面不是护城河

课程明确指出，很多短期机会来自“包装现成 API”。线索 SaaS 的核心不是你重新发明爬虫，而是把 `Apify`、邮箱查找、大模型 personalization、CSV 导出、历史记录、权限和计费打包成一个客户愿意用的 workflow。

### 2. 越接近钱，安全越重要

这个项目比前面的客户仪表盘危险得多，因为它会调用高成本第三方 API。课程安全审计发现过关键问题：未认证用户可能直接打付费 API route，造成用户绕过登录使用你的 Apify / Anthropic / OpenAI key。

### 3. Prompt 是产品的一部分

个性化邮件不是“调用一下 AI”就完了。系统要允许用户调整 personalization prompt，并把默认 prompt 设计成面向具体场景的销售 SDR 文案，而不是泛泛生成一句套话。

### 4. 线索质量比数量重要

讲师演示里强调 validated email、职位、行业、地区、公司规模、关键词排除等过滤项。这说明线索 SaaS 不能只宣传“抓 1 万条”，更要帮助用户抓到能用、能转化、能合规触达的线索。

## 安全与合规清单

- 第三方 API key 必须只在服务端使用，不能暴露到前端。
- 高成本 endpoint 必须要求登录、检查权限、检查余额或 plan。
- 所有抓取任务要限流，防止用户刷爆额度。
- 用户只能查看自己的抓取任务和结果。
- CSV 导出链接不能是公开无鉴权链接。
- 冷邮件场景要遵守目标市场反垃圾邮件规则、退订机制和平台 ToS。
- 不要承诺“自动群发一定有效”，应强调线索筛选和合规触达。

## 可迁移模板

这个案例可以迁移到任何“第三方数据/自动化 API + SaaS 外壳”的项目：

- Google Maps 商家线索工具。
- Shopify 店铺分析工具。
- YouTube / TikTok 创作者线索工具。
- 招聘候选人搜索工具。
- 竞品评论/价格抓取工具。

迁移时先问三个问题：

1. 第三方 API 是否稳定、合法、价格可控？
2. 用户拿到结果后下一步动作是什么？
3. 这个 workflow 是否能比用户手动操作节省明显时间或提高收入？

## 可生成 Outputs

- `如何用 AI 做一个线索挖掘 SaaS`
- `API Wrapper SaaS 产品拆解：从爬虫到 CSV`
- `B2B Outbound 线索工具安全检查清单`

## 证据锚点

- 原始 transcript：02:53:24-03:48:33，线索挖掘 SaaS、Apify actor、CSV、API wrapper、安全审计。
- NotebookLM 审片记录：模块三 `线索挖掘类垂直 SaaS 应用`。
