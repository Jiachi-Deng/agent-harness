---
type: output
output_type: command-prompt
status: compiled
target_reader: AI 编程新手 / 独立开发者 / 小团队技术负责人
use_case: 让 AI 按安全审计清单检查 vibe-coded Web App / SaaS 的上线风险
version_date: 2026-05-28
compiled: 2026-05-28
source_title: "VIBE CODING FULL COURSE: Gemini 3.1 + Antigravity (6 Hrs)"
source_prompt: "Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/prompts/Security For Vibe-Coded Apps (+ Prompt).md"
upstream_wiki:
  - "Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单.md"
  - "Wiki/Vibe Coding/30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代.md"
compiled_style: bilingual_editable
tags:
  - VibeCoding
  - Prompt
  - Security
  - Supabase
  - RLS
  - Webhook
---

# Vibe Coding安全审计Prompt中英对照

## 使用场景

这个 prompt 用于 AI 生成的 Web App / SaaS 上线前安全审计。它特别适合 `Next.js + Supabase + TypeScript`、有登录、数据库、API route、文件上传、支付或第三方 API 的项目。

它不是生产级安全认证，而是 Vibe Coding 新手上线前的最低安全闸门。

## 适合谁

- 用 Claude Code、Codex、Cursor、Gemini 等工具做 Web App 的新手。
- 做 Supabase / Firebase / Stripe / AI API 项目的独立开发者。
- 课程学员交作业前自查。
- 小团队给客户交付 demo 前做最低限度审计。

不适合直接替代：

- 正式渗透测试。
- 合规审计。
- 高风险金融、医疗、政务系统安全评审。

## 可替换变量

| 变量 | 用法 |
| --- | --- |
| `{STACK}` | 项目技术栈，例如 Next.js、Supabase、TypeScript |
| `{AUTH_PROVIDER}` | 认证方案，例如 Supabase Auth、Clerk、Firebase Auth |
| `{DATABASE}` | 数据库，例如 Supabase Postgres、Firebase、Prisma/Postgres |
| `{PAID_APIS}` | 高成本 API，例如 OpenAI、Anthropic、Stripe、邮件、短信 |
| `{DEPLOYMENT}` | 部署平台，例如 Vercel、Netlify、Cloudflare |
| `{SCOPE}` | 审计范围，例如 entire codebase、only API routes、only payment flow |

## Prompt结构中英对照

### 1. 角色 / Role

| English | 中文 |
| --- | --- |
| You are a senior application security engineer specializing in AI-generated codebases. You understand OWASP Top 10, common CWE patterns, and vulnerability patterns introduced by LLM coding tools. | 你是一名资深应用安全工程师，专门审查 AI 生成代码库。你理解 OWASP Top 10、常见 CWE 模式，以及 LLM 编程工具容易引入的安全漏洞。 |
| You are auditing a vibe-coded web application built mostly with AI coding assistants. Your job is to find practical, exploitable security gaps before launch. | 你正在审计一个主要由 AI 编程助手生成的 Web 应用。你的任务是在上线前找出实际可被利用的安全缺口。 |

### 2. 方法 / Methodology

| English | 中文 |
| --- | --- |
| Work in two passes. Pass 1: read the codebase and build an architecture map. Identify framework, database, auth provider, API layer, deployment config, entry points, and data flow. | 分两轮工作。第一轮：阅读代码库并建立架构地图。识别框架、数据库、认证方案、API 层、部署配置、入口点和数据流。 |
| Pass 2: audit every checklist item. For each item, output one verdict: PASS, FAIL, PARTIAL, or N/A. Do not skip checklist items. | 第二轮：逐项审计检查清单。每个条目都必须给出一个结论：通过、失败、部分覆盖或不适用。不要跳过条目。 |
| Prioritize real vulnerabilities over theoretical concerns. If uncertain, mark PARTIAL and explain what must be verified. | 优先处理真实可利用漏洞，而不是纯理论风险。如果不确定，标为部分覆盖，并说明还需要验证什么。 |

### 3. 结论格式 / Finding Format

| English | 中文 |
| --- | --- |
| For each FAIL finding, include: severity, category, location, CWE if relevant, what is wrong, why it matters, vulnerable code, fix, and estimated effort. | 每个失败项都要包含：严重程度、类别、位置、相关 CWE、问题说明、风险影响、脆弱代码、修复方式和预计工作量。 |
| Severity must be CRITICAL, HIGH, MEDIUM, or LOW. | 严重程度必须是 CRITICAL、HIGH、MEDIUM 或 LOW。 |
| The fix should be concrete and copyable when possible, but do not rewrite unrelated code. | 修复建议应尽量具体、可复制，但不要重写无关代码。 |

### 4. 检查清单 / Audit Checklist

| ID | English | 中文 |
| --- | --- | --- |
| 1.1 | Search for hardcoded secrets: API keys, tokens, passwords, connection strings, webhook URLs, Stripe keys, GitHub tokens, AWS keys, JWT-like strings, and long random strings. | 搜索硬编码密钥：API key、token、密码、连接串、webhook URL、Stripe key、GitHub token、AWS key、类似 JWT 的字符串和长随机字符串。 |
| 1.2 | Verify `.env`, `.env.local`, `.env.production`, and `.env*.local` are ignored. Check whether secrets were previously committed. | 确认 `.env`、`.env.local`、`.env.production` 和 `.env*.local` 已被忽略，并检查历史提交里是否泄露过密钥。 |
| 1.3 | Check public prefix leaks. Server secrets must not use `NEXT_PUBLIC_`, `VITE_`, or `REACT_APP_`. | 检查公开前缀泄露。服务端密钥不能使用 `NEXT_PUBLIC_`、`VITE_` 或 `REACT_APP_`。 |
| 1.4 | Check console logs and client-visible errors for leaked secrets or environment values. | 检查 console 日志和前端错误信息是否泄露密钥或环境变量。 |
| 1.5 | Check production source maps and build artifacts that may expose source code. | 检查生产环境 source map 和构建产物是否暴露源码。 |
| 1.6 | Verify required environment variables fail fast on startup when missing. | 确认必要环境变量缺失时应用会启动失败，而不是静默使用不安全默认值。 |
| 2.1 | For Supabase or client-accessible databases, verify RLS is enabled on every user-data table. | 对 Supabase 或客户端可访问数据库，确认所有用户数据表都启用了 RLS。 |
| 2.2 | Verify each RLS-enabled table has policies, not just the RLS toggle. | 确认每张启用 RLS 的表都有 policy，而不是只开了开关。 |
| 2.3 | Check INSERT and UPDATE policies include `WITH CHECK` clauses. | 检查 INSERT 和 UPDATE policy 是否包含 `WITH CHECK`。 |
| 2.4 | Verify policies use trusted identity such as `auth.uid()`, not user-editable metadata. | 确认 policy 使用可信身份来源，例如 `auth.uid()`，不要使用用户可修改的 metadata。 |
| 2.5 | Ensure service role keys are never imported into client components or browser code. | 确保 service role key 不会进入客户端组件或浏览器代码。 |
| 2.6 | Verify storage buckets have correct access policies. | 确认存储 bucket 有正确访问策略。 |
| 2.7 | Check raw SQL for string concatenation and SQL injection risk. | 检查原生 SQL 是否存在字符串拼接和 SQL 注入风险。 |
| 2.8 | Review `SECURITY DEFINER` functions for unintended privilege bypass. | 审查 `SECURITY DEFINER` 函数是否意外绕过权限。 |
| 3.1 | Verify auth middleware exists and covers protected routes. | 确认认证中间件存在，并覆盖受保护路由。 |
| 3.2 | Prefer default-deny routing: allowlist public routes instead of blocklisting protected routes. | 优先默认拒绝：用公开路由白名单，而不是只列出受保护路由黑名单。 |
| 3.3 | For Supabase, use `getUser()` for security-sensitive server operations, not only `getSession()`. | 对 Supabase，安全敏感的服务端操作应使用 `getUser()`，不要只用 `getSession()`。 |
| 3.4 | Verify auth callback routes exchange codes safely and do not leak tokens. | 确认认证回调路由安全交换 code，且不泄露 token。 |
| 3.5 | Store session tokens in httpOnly cookies when possible, not localStorage. | 尽量用 httpOnly cookie 存 session token，不要放 localStorage。 |
| 3.6 | Every API route handling user data must verify authentication. | 所有处理用户数据的 API route 都必须验证登录。 |
| 3.7 | OAuth flows must validate callback URLs and use state for CSRF protection. | OAuth 流程必须验证回调地址，并用 state 防 CSRF。 |
| 3.8 | Password reset tokens must expire, be single-use, and be transmitted securely. | 密码重置 token 必须过期、一次性使用，并安全传输。 |
| 4.1 | Validate all API route and server action inputs server-side with a schema library. | 所有 API route 和 server action 输入都要在服务端用 schema 库验证。 |
| 4.2 | User identity for writes must come from session/JWT, not request body `userId`. | 写操作的用户身份必须来自 session/JWT，不能信任请求体里的 `userId`。 |
| 4.3 | Sanitize user-generated HTML and check dangerous rendering APIs. | 清洗用户生成 HTML，并检查危险渲染 API。 |
| 4.4 | State-changing operations must not use GET. | 改变状态的操作不能使用 GET。 |
| 4.5 | Error responses must not leak stack traces, SQL errors, paths, or env names. | 错误响应不能泄露堆栈、SQL 错误、文件路径或环境变量名。 |
| 4.6 | Webhooks must verify signatures before processing. | Webhook 必须先验证签名再处理。 |
| 5.1 | Run package audit and report vulnerabilities by severity. | 运行依赖审计，并按严重程度报告漏洞。 |
| 5.2 | Check suspicious or hallucinated packages. | 检查可疑或 AI 幻觉生成的依赖包。 |
| 5.3 | Verify lockfile is committed. | 确认 lockfile 已提交。 |
| 5.4 | Check outdated packages, especially auth, crypto, and framework packages. | 检查过期依赖，尤其是认证、加密和框架包。 |
| 5.5 | Remove unused dependencies to reduce attack surface. | 移除未使用依赖，减少攻击面。 |
| 6.1 | Rate-limit expensive operations that call paid APIs. | 对调用付费 API 的高成本操作做限流。 |
| 6.2 | Rate-limit login, signup, password reset, and OTP endpoints. | 对登录、注册、密码重置和 OTP 接口做限流。 |
| 6.3 | Rate limiting must be server-side and use a reliable backing store. | 限流必须在服务端执行，并使用可靠存储。 |
| 7.1 | Restrict CORS on API routes intended only for your frontend. | 对只供自家前端使用的 API route 限制 CORS。 |
| 7.2 | Do not combine wildcard origins with credentials. | 不要把通配 origin 和 credentials 一起使用。 |
| 8.1 | Validate file type and size on the server. | 在服务端校验文件类型和大小。 |
| 8.2 | Separate public and private storage policies. | 区分公开文件和私密文件的存储策略。 |
| 8.3 | Uploaded files must not be executable on the server. | 上传文件不能在服务器上执行。 |

## 可复制精简版 Prompt

```text
EN:
Audit this vibe-coded web application for launch-blocking security issues.

Stack: {STACK}
Auth provider: {AUTH_PROVIDER}
Database: {DATABASE}
Paid APIs: {PAID_APIS}
Deployment: {DEPLOYMENT}
Scope: {SCOPE}

Work in two passes:
1. Read the codebase and map architecture, entry points, auth, database access, API routes, webhooks, storage, and deployment config.
2. Audit every checklist item below with PASS / FAIL / PARTIAL / N/A.

Checklist:
- Hardcoded secrets and public-prefix key leaks.
- `.env` and git history secret exposure.
- RLS enabled, policies present, `WITH CHECK`, trusted identity source, service role isolation.
- Auth middleware coverage, protected API routes, safe OAuth/callback/session handling.
- Server-side schema validation, user identity from session, XSS sanitization, no state-changing GET routes.
- Webhook signature verification.
- Package audit, hallucinated packages, committed lockfile, outdated and unused dependencies.
- Rate limiting for paid APIs and auth endpoints.
- CORS restrictions.
- File upload validation, storage permissions, execution prevention.

For every FAIL, output severity, category, location, impact, vulnerable code, fix, and estimated effort.
End with: security posture rating, critical/high findings, quick wins, remediation plan, what is already done right, and checklist summary.

Do not fix code yet. Report first.
```

```text
中文：
请对这个 AI 编程生成的 Web 应用做上线前安全审计。

技术栈：{STACK}
认证方案：{AUTH_PROVIDER}
数据库：{DATABASE}
付费 API：{PAID_APIS}
部署平台：{DEPLOYMENT}
审计范围：{SCOPE}

分两轮工作：
1. 先阅读代码库，梳理架构、入口点、认证、数据库访问、API route、webhook、存储和部署配置。
2. 再逐项审计下面的检查清单，每项给出 PASS / FAIL / PARTIAL / N/A。

检查清单：
- 硬编码密钥和公开前缀 key 泄露。
- `.env` 和 git 历史里的密钥泄露。
- RLS、policy、`WITH CHECK`、可信身份来源、service role 隔离。
- 认证中间件覆盖、API route 保护、OAuth/callback/session 安全。
- 服务端 schema 验证、用户身份来自 session、XSS 清洗、禁止 GET 改状态。
- Webhook 签名验证。
- 依赖审计、幻觉包、lockfile、过期和未使用依赖。
- 付费 API 和认证接口限流。
- CORS 限制。
- 文件上传校验、存储权限、禁止执行上传文件。

每个 FAIL 都要输出严重程度、类别、位置、影响、脆弱代码、修复建议和预计工作量。
最后输出：总体安全评级、Critical/High 问题、quick wins、修复优先级、已经做对的安全措施、检查清单摘要。

先报告，不要直接修代码。
```

## 使用建议

- 第一次审计用完整版，避免漏项。
- 修复阶段一次只修一个 HIGH/CRITICAL，不要让 AI 顺手重构。
- 每次新增支付、上传、公开 API、webhook、AI 生成接口后重新跑相关 section。
- 对 Supabase 项目，RLS policy 要实际用两个账号测试，不要只看 AI 报告。

## 证据锚点

- 原始 prompt：`Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/prompts/Security For Vibe-Coded Apps (+ Prompt).md`
- 上游 Wiki：`Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单.md`
- 相关 Output：`Outputs/SOP与模板/Vibe Coding SaaS上线检查清单.md`
