---
type: wiki
status: compiled
area: Vibe Coding
topic: Vibe Coding
source_title: "VIBE CODING FULL COURSE: Gemini 3.1 + Antigravity (6 Hrs)"
source_clipping: "Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md"
review_note: "Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md"
compiled: 2026-05-28
updated: 2026-05-29
tags:
  - VibeCoding
  - SaaS
  - Workflow
  - Supabase
  - Netlify
  - Codex
  - Convex
  - Vercel
  - Worktrees
---

# Vibe Coding全栈SaaS开发闭环

## 这个流程解决什么

它解决的是从“AI 帮我做一个好看的页面”升级到“AI 帮我做一个能登录、能存数据、能上线、能维护的 SaaS 原型”的问题。

静态网站像广告牌：只展示内容，风险相对低。SaaS 像真实店铺：有用户、订单、资料、接口和权限，必须多出数据库、认证、安全审计、部署配置和长期维护。

## 标准闭环

| 步骤 | 人要做什么 | AI 要做什么 | 验收重点 |
| --- | --- | --- | --- |
| 1. 需求与参考 | 说清楚用户、场景、页面、核心流程，找 Dribbble / 竞品 / 截图参考 | 把自然语言需求转成页面、数据表和模块计划 | 需求不能只写“做个 SaaS”，要有用户流程 |
| 2. 项目初始化 | 确认技术栈、项目文件夹、依赖原则 | 搭 Next.js / Tailwind 等基础框架，生成目录和页面骨架 | 依赖必须来自官方稳定包，不能让 AI 随便编包名 |
| 3. 数据库与 RLS | 明确要存什么数据、谁能看谁的数据 | 对接 Supabase，创建用户/订单/内容表，配置 RLS | 用户只能访问自己的数据，不能只“连上数据库”就算完成 |
| 4. 登录与权限 | 定义公开页面、私密页面、管理员/普通用户权限 | 做登录注册、认证中间件、服务端验证 | 未登录访问私密页必须被拦截，表单不能只靠前端验证 |
| 5. 核心业务功能 | 逐个描述仪表盘、订单、设置、线索、内容处理等功能 | 写页面、接口、数据库读写、状态流转 | 每个功能都能走通真实用户路径 |
| 6. 本地测试与安全审计 | 像真实用户一样注册、登录、提交、查看、退出 | 修 bug，跑安全审计清单 | 本地通过后仍不能直接上线，要先查密钥/RLS/权限/依赖 |
| 7. 部署上线 | 在 Netlify 等平台配置环境变量和域名 | 辅助构建、部署、修路径和重定向问题 | 线上环境变量要单独配置，本地 `.env` 不会自动上传 |
| 8. 线上迭代 | 收集 bug 和新需求，划定改动范围 | 小步修复、局部迭代、生成更新说明 | 改一点测一点，每次改动后重新做安全复查 |

## 人的角色

Vibe Coding 里人不是“完全不懂也能躺着收结果”，而是产品负责人和验收人：

- 定目标：谁用、解决什么问题、成功结果是什么。
- 给参考：截图、竞品、页面风格、字段、流程。
- 划边界：哪些文件/模块可以改，哪些不能动。
- 做验收：本地、线上、无痕浏览器、移动端、不同账号都要测。
- 抓安全：只要涉及账号、数据库、接口、上传、支付，就要跑安全审计。

## 模型分工

课程里反复出现的可复用分工：

- **Gemini**：视觉、页面、布局、Landing Page、动画、快速样式调整。
- **Claude Code**：后端逻辑、数据库、接口、权限、安全、调试。
- **多代理并行**：只适合模块边界清晰的大项目。小项目开太多代理会增加成本和冲突。

多代理并行时必须先给全局规则：

- 每个代理只负责自己的模块。
- 不跨模块改文件。
- 开发后输出修改文件和自测结果。
- 最后由一个主代理或人工做联调。

## 项目递进

这门课的项目不是随机堆砌，而是按复杂度递进：

1. 静态作品集：练 AI 生成界面和快速部署。
2. 客户仪表盘：加入登录、数据库、RLS、订单和设置页。
3. 线索挖掘 SaaS：加入爬虫、第三方 API、邮件发送和复杂调试。
4. AI 缩略图 SaaS：加入文件上传、AI 图像接口、存储权限。
5. 内容自动化分发 SaaS：加入任务队列、多平台适配、多代理开发和长期维护。
6. Creator Carousel Studio：用 Codex Desktop、Next.js、Convex、Vercel、skills 和 GitHub Issues，从产品构思走到线上部署，并继续用 issue / PR 迭代。

## Codex Desktop 版闭环

`OpenAI Codex Full Course 4 Hours: Build & Ship` 把 SaaS 开发闭环进一步工程化：不是只让 AI 写页面，而是把产品计划、任务拆解、实现、部署、自动化和并行开发都纳入 Codex Desktop。

### 1. 先从产品问题拆到 Issues

课程里先用 ideation / planning 类 skill 讨论要做什么，再把项目拆进 GitHub Issues。这样做的价值是：

- 新功能不再散落在聊天记录里。
- 每个 issue 都能变成一个可执行、可验证的小任务。
- 后续 automation 可以围绕 issue backlog 做巡检和更新。

适合本库吸收的原则是：**复杂 SaaS 不要只靠一条长 prompt 驱动，应该把目标拆进文件和 issue。**

### 2. 技术栈要对 agent 友好

这门课的实战栈是：

| 层 | 工具 | 为什么适合 agentic coding |
| --- | --- | --- |
| Frontend | Next.js | 文件结构清晰、生态大、Vercel 部署顺 |
| Backend / Database | Convex | TypeScript 端到端，减少 SQL migration 摩擦 |
| Hosting | Vercel | GitHub 连接后部署路径短，适合频繁预览 |

这不替代 Supabase / Firebase 路线。它补充的是：如果目标是让 Codex 在同一语言和同一 repo 里快速理解前后端，Convex 这类 TypeScript-first 后端会降低 agent 的上下文切换成本。

### 3. Worktrees 让多个任务并行

Worktree 适合在同一 repo 上并行处理多个互不冲突的任务，例如：

- 一个 worktree 修 UI。
- 一个 worktree 做后端 schema。
- 一个 worktree 做导出功能。
- 一个 worktree 做 bugfix 或 code review。

但前提是 issue 边界清晰、环境能启动、分支能回滚。否则多个 agent 同时改同一块代码，会放大混乱。

### 4. Automations 负责重复巡检，不负责无人监督上线

Codex automations 可以定时做：

- 每日 standup / repo summary。
- bug backlog 巡检。
- 数据刷新。
- 简单 issue 初步处理。

但自动化任务上线前必须先手动触发一次，确认它能访问项目、网络、环境变量、插件、skills 和 GitHub。不能因为“能创建 automation”就假设它能稳定长期运行。

### 5. App + Skill 可以共同构成产品

Creator Carousel Studio 的关键启发是：有些工作既需要网页 UI，也需要本地 agent / skill。网页给非技术用户操作，skill 给技术用户或 agent 批量导入、生成、更新数据。

这类结构适合一人公司或小团队：

```text
Web app 给人使用
  + skill/CLI 给 agent 使用
  + database 存共享状态
  + automation 做定时维护
```

## 数据 / Dashboard 型项目闭环

`Master 97% of Codex in 1 Hour` 里的 YouTube comment intelligence 系统提供了一类很适合新手练习的 SaaS 原型：不是先做复杂账号系统，而是先把“数据获取 -> 分析 -> 可视化 -> 定时刷新”跑通。

这类项目的可复用闭环是：

| 环节 | 输出 | 验收 |
| --- | --- | --- |
| 连接数据源 | YouTube Data API、业务数据库、CSV、表格或本地文件 | API key / OAuth 权限明确，密钥不进 Git |
| 生成分析产物 | Excel、CSV、Markdown report、JSON 数据 | 数据量、去重、字段、时间范围可解释 |
| 生成 Web dashboard | 本地 localhost 预览，筛选、图表、链接、详情页 | 真实数据能显示，空状态和错误状态可用 |
| 推到 GitHub | repo、commit、忽略 `.env` 和临时文件 | 没有密钥泄露，diff 可读 |
| 部署到 Vercel | 公网页面和部署记录 | 手机上能访问，刷新后数据一致 |
| 定时更新 | weekly automation 或仓库脚本 | 手动 run now 通过，重复数据不会无限追加 |
| 浏览器 QA | click、filter、search、external link、mobile | Codex / Browser Use 找到的问题被回修 |

这个闭环适合很多一人公司和小企业场景：YouTube 评论分析、客户反馈看板、线索表格、客服问题聚类、内容选题池、广告素材表现复盘。它的关键不是 dashboard 好不好看，而是让同一份数据同时服务人类 UI、agent skill 和 automation。

## AI 图像编辑 MVP 闭环

`CODEX FULL COURSE: From Zero to Deployed App (2026)` 的 Beauty Mirror 案例适合补一类更轻的 MVP：先不做完整 SaaS，而是把“上传图片 -> 调用 AI 图像模型 -> 展示多个候选结果 -> 部署上线”的核心体验跑通。

课程里的第一版设计是：

| 维度 | V1 做法 | Wiki 判断 |
| --- | --- | --- |
| 用户 | 面部美容 / 形象预览需求用户 | 这是课程案例，不应未经验证就推广为通用商业结论 |
| 产品形态 | Web app | 适合快速演示和部署，移动端体验后续再验证 |
| 核心功能 | 上传一张脸图，生成 15-20 种微调预览 | API 成本、延迟、失败率和隐私提示必须提前设计 |
| 视觉参考 | Pinterest 画廊布局 | 用截图给 Codex，比只写“做得好看”更有效 |
| 后端 | V1 无账号，`localStorage` 保存 | 只能算本机 demo；跨设备、历史记录和付费都需要后端 |
| AI 能力 | OpenRouter + 图像模型 | API key 必须在服务端或受控环境，且设置额度上限 |

可复用闭环：

```text
想法和目标用户
  -> 截图参考和视觉规则
  -> Web search 做需求词汇/选项列表
  -> 4 个 MVP 澄清问题
  -> 一次生成 V1
  -> .env + API 文档写入 docs/
  -> 本地运行和浏览器调试
  -> 调整 API 调用方式
  -> Git commit
  -> Vercel 部署
```

这类 MVP 的边界要写清楚：它验证的是“用户愿不愿意上传、等待、比较结果并觉得有用”，不是已经证明 SaaS 成立。要升级成真实产品，至少还要补：

- 图片上传隐私、删除机制和用户同意。
- 账号、历史记录、跨设备同步和文件存储。
- AI API 成本、额度、失败重试、并发控制和账单保护。
- 生成结果的质量验收和人工 fallback。
- 敏感场景的伦理、合规和广告文案边界。

## 常见失败点

- 把 SaaS 当静态站做，只关注 UI，不处理用户数据和权限。
- 本地能跑就直接部署，忘了线上环境变量、路径和重定向。
- 让 AI 一次性改太多文件，结果越修越乱。
- 只靠前端校验表单，没有服务端验证。
- Supabase 开了 RLS 但没写策略，导致查询空结果，误以为是普通 bug。
- 新增功能后忘记重新安全审计。
- 只建自动化，不检查它是否有权限、环境变量和网络访问。
- 用 worktree 并行开发，但没有 issue 边界和启动脚本，导致多个分支都跑不起来。
- 数据刷新 automation 过度 agent 化，本来一个 repo script 就能解决，却每周重新让 agent 从头推理一遍。
- 把 Excel / CSV / 数据文件打开着不关，导致 automation 无法覆盖或写入。
- 生成类 MVP 只看页面能不能出图，不检查 API key 是否泄露、额度上限是否设置、失败时是否能局部重试。

## 可生成 Outputs

- `Vibe Coding 从静态站到 SaaS 的 8 步 SOP`
- `AI 新手做 SaaS 上线前检查清单`
- `Next.js + Supabase + Netlify 项目实操课讲义`

## 证据锚点

- NotebookLM 审片记录：全栈 SaaS 应用开发流程、03:16:50 后部署收尾、多代理和调试模块。
- 原始 transcript：00:56、01:02:40、02:42:50、03:16:50 之后的项目和部署段落。
- [[Clippings/OpenAI Codex Full Course 4 Hours Build & Ship|OpenAI Codex Full Course 4 Hours: Build & Ship]]：03:03:23 GitHub Issues、03:07:57 Automations、03:16:24 Next.js + Convex + Vercel、03:23:55 Worktrees、03:33:19 Creator Carousel Studio、03:44:57 之后的持续迭代。
- [[Clippings/Master 97% of Codex in 1 Hour (full course)|Master 97% of Codex in 1 Hour]]：YouTube comments -> Excel insights -> Web dashboard -> GitHub / Vercel -> weekly automation -> Browser Use QA 的完整项目闭环。
- [[Clippings/CODEX FULL COURSE From Zero to Deployed App (2026)|CODEX FULL COURSE: From Zero to Deployed App (2026)]] + [[Raw/NotebookLM/2026-05-29--youtube--CODEX FULL COURSE From Zero to Deployed App (2026)|NotebookLM 审片记录]]：Beauty Mirror 从图片上传、Pinterest 画廊、OpenRouter 图像 API、本地调试到 Vercel 部署的轻量 AI 图像 MVP。
