---
type: output
output_type: sop-template
status: compiled
target_reader: AI 编程新手 / 独立开发者 / 产品和运营
use_case: 用一个 prompt 让 AI 通俗解释后端选择的大图，并用钩子引导用户继续描述项目
version_date: 2026-05-28
upstream_wiki:
  - "[[Wiki/Vibe Coding/10-Getting Started/后端与数据库选择|后端与数据库选择]]"
  - "[[Wiki/Vibe Coding/00-Overview/Vibe Coding专题路线图|Vibe Coding专题路线图]]"
references:
  - "[[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]"
---

# 后端选择知识召回 prompt 卡片

这张卡片不是后端工具横评。它的作用是：当你不知道该怎么问 AI 时，用一个 prompt 把 AI 已经知道的后端选择知识召回出来，先获得最初步的大图，再被一个自然钩子引导继续追问。

## 什么时候用

- 你有一个 Web App 想法，但不知道要不要接后端。
- 你听过 Firebase、Supabase、Neon、Convex，但不知道怎么选。
- 你准备从纯前端 demo 升级到有登录、数据库、上传或多人协作的产品。
- 你不想先读一堆工具文档，只想让 AI 先给出项目级判断。

## 直接复制这个 prompt

这张卡片只有一个 prompt。它不要求你先填表，也不要求你已经有完整项目方案。它会先讲清楚最基础的大图，最后用一个钩子引导你继续追问。

```text
我想先对“Web App 后端和数据库怎么选”有一个最初步但靠谱的理解。

我可能还没有具体项目，也可能只有一个模糊想法。请你不要先让我填一堆信息，也不要写代码。请你像一个耐心的 AI 编程教练，用普通人能听懂的话给我讲清楚。

请按这个顺序回答：

1. 先用一个生活化比喻解释：什么是后端，什么是数据库，为什么有些 Web App 可以先不用后端。
2. 用非常通俗的话解释这些词分别解决什么问题：Authentication、Database、Storage、Server/API routes、Realtime、Payment / credits。
3. 用一张简单表格比较：Firebase、Supabase、Neon、Convex、Airtable/Notion/Google Sheets。不要做深度横评，只讲“它像什么、适合谁、最容易踩什么坑”。
4. 给 3 个小例子：
   - 一个可以先不用后端的 app；
   - 一个适合 Firebase / Supabase 这类完整后端的 app；
   - 一个只需要数据库或轻量表格工具的 app。
5. 告诉我 AI 编程新手最容易误判的 5 件事，比如什么时候过早接后端、什么时候把 secret 放错地方、什么时候以为有数据库就等于安全。
6. 告诉我哪些信息 AI 可以先帮我判断，哪些信息必须查官方最新文档或真实项目验证，例如价格、免费额度、API 限制、部署配置和权限规则。
7. 最后请用一个很自然、很吸引人的问题作为钩子，引导我继续追问。这个问题应该让我只需要用一句话描述自己的 app 想法，你就能继续帮我判断要不要后端、选什么方案、第一步怎么做。

要求：
- 不要堆术语；
- 不要一上来让我做复杂选择；
- 不要假装价格、平台规则和 API 限制一定是最新的；
- 重点是让我获得第一层理解，并愿意继续问下去。
```

## 必须核验

AI 的回答只能作为第一版方向。以下内容要查官方文档或用真实项目验证：
- 最新免费额度、计费、地区限制和产品限制。
- Auth、RLS、security rules、storage policy 的默认行为。
- 前端可暴露 key 与服务端 secret 的边界。
- Vercel、Netlify、Cloudflare 的环境变量和 callback domain。
- AI API、爬虫、邮件、文件存储、支付 webhook 的滥用成本。
- 客户数据、支付数据、用户数据是否涉及合规要求。

## 回流到 Wiki 的内容

不要把 AI 的通用回答整篇复制回 Wiki。值得回流的是：

- 真实项目背景和最终选择。
- 为什么没有选另一个工具。
- 实际踩到的权限、部署、billing、RLS、rules、storage 坑。
- 官方文档或价格变化。
- 经过验证的数据模型和上线检查清单。
- AI 回答错了、漏了或过度自信的地方。

## 上游

- 上游 Wiki：`Wiki/Vibe Coding/10-Getting Started/后端与数据库选择.md`
- 参考课程：`Clippings/Vibe Coding for Beginners (Full Course 2026).md`
