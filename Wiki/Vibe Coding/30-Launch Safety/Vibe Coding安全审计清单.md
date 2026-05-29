---
type: wiki
status: compiled
area: Vibe Coding
topic: Vibe Coding
source_title: "VIBE CODING FULL COURSE: Gemini 3.1 + Antigravity (6 Hrs)"
source_clipping: "Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md"
review_note: "Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md"
prompt_file: "Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/prompts/Security For Vibe-Coded Apps (+ Prompt).md"
compiled: 2026-05-28
tags:
  - VibeCoding
  - Security
  - Supabase
  - RLS
  - SaaS
---

# Vibe Coding安全审计清单

## 这个页面解决什么

Vibe Coding 最大的错觉是：页面能跑，就以为产品完成了。只要项目涉及用户、数据库、接口、文件上传、邮件、AI API 或支付，真正的验收标准就必须包含安全。

这门课把新手最容易踩的安全坑压缩成 5 个 80/20 项：密钥、RLS、服务端验证、依赖包、认证中间件。它不是完整安全体系，但足够作为 AI 编程新手的上线前最低门槛。

## 5 个必查项

| 项目 | 大白话解释 | 为什么危险 | 验收问题 |
| --- | --- | --- | --- |
| 密钥与环境变量 | 不要把 API key、数据库 key、支付 key 写在公开代码里 | 别人可以盗刷额度、读数据、调用你的服务 | 代码里能否搜到真实 key？线上平台是否单独配置环境变量？ |
| Supabase RLS | 数据库每一行都要按用户上锁 | 不开 RLS 或策略错误会导致用户互看、互改、互删数据 | 每张用户数据表是否启用 RLS？是否有正确 policy？ |
| 服务端验证 | 不要只相信前端表单检查 | 攻击者能绕过前端，直接请求 API | 关键提交是否在 server/action/API route 再验证？ |
| 依赖与包 | AI 可能编不存在的包名，也可能用过期包 | 攻击者会注册恶意同名包，旧包可能有已知漏洞 | 依赖是否真实、官方、维护中？是否检查过漏洞？ |
| 认证中间件 | 私密页面和 API 必须检查登录状态 | 没登录的人可能访问 dashboard、settings、admin、API | 受保护路由是否统一被 middleware 或 server auth 拦截？ |

## 加强项

| 场景                          | 额外检查                                      |
| --------------------------- | ----------------------------------------- |
| 调用 OpenAI、邮件、爬虫、AI 绘图等高成本接口 | 加 rate limiting，避免被刷爆账单                   |
| 自己暴露 API route              | 检查 CORS，只允许可信来源调用                         |
| 文件上传                        | 服务端校验文件类型、大小和存储权限，不能只看扩展名                 |
| 多租户 SaaS                    | 普通用户和管理员权限分离，RLS policy 不要混用 service role |
| 线上部署                        | Netlify/Vercel/Cloudflare 后台必须配置生产环境变量    |

## 什么时候必须跑审计

- 第一次从静态站升级到 SaaS。
- 新增登录、数据库、订单、用户资料、文件上传、支付、邮件、爬虫或 AI API。
- 每次部署到公网前。
- 每次 AI 大范围修改后。
- 每次线上出现权限、数据、接口或环境变量相关 bug 后。

## 审计 Prompt 的正确用法

课程配套的安全 prompt 很长，价值在结构，不在照抄神奇咒语。使用时保留这几个部分：

1. **角色**：让 AI 以应用安全工程师身份审查 AI 生成代码。
2. **发现阶段**：先读项目结构、依赖、环境变量、路由、数据库访问方式。
3. **系统检查表**：逐项检查密钥、RLS、服务端验证、依赖、认证中间件、限流、CORS、上传。
4. **输出格式**：按严重程度列问题，给证据、影响、修复建议和验证方式。
5. **修复节奏**：先报告，后小步修；不要让 AI 一次性重构全项目。

更适合新手的短指令：

```text
请对这个项目做上线前安全审计。重点检查：
1. 是否有密钥/API key 暴露在公开代码或前端包里；
2. Supabase 用户数据表是否启用 RLS，并且有正确 policy；
3. 所有表单、API route、数据库写入是否有服务端验证；
4. 依赖包是否真实、官方、维护中，是否存在明显漏洞；
5. 私密页面和 API 是否有认证中间件保护；
6. 高成本 API 是否有限流，文件上传是否有服务端类型和大小校验。

先输出发现和修复计划，不要直接大范围改代码。每个问题都标注严重程度、涉及文件、修复建议和验证方式。
```

## 不要误解

- 安全审计 prompt 不是法律保证，也不是生产安全认证。
- AI 审计擅长抓常见模式，可能漏掉业务逻辑漏洞和跨文件复杂漏洞。
- Supabase anon key 本身可能是公开设计，重点不是“绝对不能出现 anon key”，而是是否开启了正确 RLS。
- RLS 开关和 RLS policy 是两件事：只开开关但没 policy，常见结果是数据查不到。

## 可生成 Outputs

- `Vibe Coding 新手上线前安全检查清单`
- `Supabase RLS 小白解释卡`
- `AI 写代码后必须追问的 10 个安全问题`

## 证据锚点

- 原始 transcript：00:44:20 安全模块。
- NotebookLM 审片记录：用户重点追问安全五项和 SaaS 开发闭环。
- Prompt file：`Security For Vibe-Coded Apps (+ Prompt).md`，包含完整安全审计 prompt 和检查表结构。

