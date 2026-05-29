---
type: output
output_type: course-handout
status: review-ready
target_reader: AI 编程新手、独立开发者、小团队老板、想用 Vibe Coding 做 SaaS 原型的产品/运营
use_case: 作为 1-2 天工作坊或自学路线讲义，带学员从静态页走到可上线 SaaS 原型
version_date: 2026-05-28
updated: 2026-05-29
upstream_wiki:
  - "[[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]"
  - "[[Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单|Vibe Coding安全审计清单]]"
  - "[[Wiki/Vibe Coding/30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代|SaaS支付方案：Stripe积分订阅Webhook与国内替代]]"
  - "[[Wiki/Vibe Coding/30-Launch Safety/内容平台官方API与自动发布限制|内容平台官方API与自动发布限制]]"
  - "[[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架|Vibe Coding调试与迭代框架]]"
  - "[[Wiki/Vibe Coding/40-Business/Vibe Coding商业化与定价包装|Vibe Coding商业化与定价包装]]"
  - "[[Wiki/Vibe Coding/40-Business/中文市场Vibe Coding获客路径|中文市场Vibe Coding获客路径]]"
  - "[[Wiki/Vibe Coding/50-SaaS产品模式/线索挖掘SaaS产品模式|线索挖掘SaaS案例]]"
  - "[[Wiki/Vibe Coding/50-SaaS产品模式/AI缩略图生成SaaS产品模式|AI缩略图生成SaaS案例]]"
  - "[[Wiki/Vibe Coding/50-SaaS产品模式/内容自动化分发SaaS产品模式|内容自动化分发SaaS工作流]]"
related_outputs:
  - "[[Outputs/SOP与模板/Cinematic Landing Page Builder Prompt中英对照|Cinematic Landing Page Builder Prompt中英对照]]"
  - "[[Outputs/SOP与模板/Vibe Coding安全审计Prompt中英对照|Vibe Coding安全审计Prompt中英对照]]"
references:
  - "[[Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs)|VIBE CODING FULL COURSE transcript]]"
  - "[[Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review|NotebookLM 审片记录]]"
  - "[[Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/README|课程配套资产说明]]"
---

# Vibe Coding 全栈 SaaS 实战课讲义

这份讲义面向想用 AI 编程工具做真实产品的人。目标不是让学员记住某个工具按钮，而是学会一条完整闭环：从静态 Landing Page，到登录、数据库、权限、支付/积分、部署、安全审计，再到商业包装。

## 讲义维护备注

本讲义是课程交付版，不承担所有细节维护。后续新材料按 Wiki 主干回流：

- 课程结构、作业和训练营安排在本讲义维护。
- 项目开发闭环、风险判断和可复用方法回到 [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]。
- Landing Page 和安全审计 prompt 回到 `Outputs/SOP与模板/` 中英文对照页。
- 支付、平台 API、中文市场获客属于强时效和本地化判断，真实交付前必须回查对应 Wiki 和官方资料。

## 课程目标

学完后，学员应该能做到：

- 用自然语言把一个业务想法拆成页面、数据、权限和核心流程。
- 先做静态页面，再升级为可登录、可存数据的 SaaS 原型。
- 理解 `Next.js + Supabase + Netlify/Vercel` 这类 AI 友好技术栈的基本分工。
- 在新增数据库、上传、第三方 API、支付前主动跑安全检查。
- 知道如何把一个 AI 做出的项目包装成可演示、可交付、可定价的商品。

## 课程对象

适合：

- 想用 AI 做网站、小工具、SaaS 原型的独立开发者。
- 想把内部流程做成小系统的小企业老板和运营。
- 会用 AI，但不知道如何验收代码、权限、部署和安全的新手。
- 想把 Vibe Coding 变成课程、服务或产品化能力的人。

不适合：

- 已经要做严肃生产系统、合规系统或高并发平台的团队。
- 只想让 AI 一句话自动交付，不愿意手动测试和验收的人。
- 想直接抄海外 SaaS 定价和获客方式，不做本地化判断的人。

## 学习主线

| 阶段 | 学员要完成什么 | 关键验收 |
| --- | --- | --- |
| 1. 静态站 | 做一个能表达价值的 Landing Page | 首屏讲清用户、问题、结果和 CTA |
| 2. SaaS 骨架 | 加登录、Dashboard、数据库和基础权限 | 用户能注册、登录、保存自己的数据 |
| 3. 业务功能 | 做一个真实工作流，例如线索、缩略图或内容分发 | 用户输入、处理、结果、历史记录能闭环 |
| 4. 安全闸门 | 检查密钥、RLS、服务端验证、依赖和认证中间件 | 未登录不能访问私密数据，高成本 API 不暴露 |
| 5. 部署上线 | 配置线上环境变量、域名、构建命令和回调地址 | 线上可用，外部浏览器能跑完整流程 |
| 6. 商业包装 | 做演示、文档、功能清单、价格和售后边界 | 客户能理解、试用、付费或提出明确反馈 |

## 来源课程模块速览

原始长课不是按本讲义的 6 课结构组织，而是从工具、静态站、安全、全栈 SaaS、案例和商业化一路展开。本讲义保留其有效顺序，但把容易过时的工具按钮和 UI 路径降级为参考。

| 原始模块 | 课程价值 | 在本讲义里的归位 |
| --- | --- | --- |
| 工具与环境 | 建立 Antigravity / Gemini / Claude Code 的协作心智 | 只保留模型分工和多代理边界 |
| 静态作品集网站 | 训练 Landing Page、视觉参考和快速部署 | 第 1 课 |
| 安全 80/20 | 密钥、RLS、服务端验证、依赖和认证中间件 | 第 4 课 |
| 全栈客户仪表盘 | 登录、数据库、订单、设置和部署 | 第 2 课 |
| 线索挖掘 SaaS | API wrapper、线索、enrichment、CSV、合规 | 第 3 课 |
| AI 缩略图 SaaS | 上传、AI 图像、积分、Stripe、成本控制 | 第 3 / 4 课 |
| 内容自动化分发 SaaS | 多平台内容、voice profile、OAuth、发布边界 | 第 3 / 5 课 |
| 商业化 | 包装、定价、交付、售后和获客 | 第 6 课 |

## 第 1 课：从 Landing Page 开始

不要一开始就让 AI 做完整 SaaS。先训练它理解产品、用户和视觉方向。

最小输入：

- 品牌名和一句话用途。
- 目标用户是谁。
- 3 个核心价值主张。
- 访客下一步应该做什么。
- 参考风格或竞品截图。

练习：

```text
请先不要写复杂后端。
基于下面信息生成一个高质量 SaaS Landing Page：
1. 产品名：
2. 目标用户：
3. 用户现在的痛点：
4. 工具能帮他得到的结果：
5. 三个核心卖点：
6. CTA：
7. 参考风格：
要求页面能在本地运行，移动端可读，CTA 链接先指向 /signup。
```

验收重点：

- Hero 不要只写空泛口号，要让用户一眼知道这是给谁解决什么问题。
- Feature 不是技术列表，而是业务结果。
- 定价和 CTA 可以先是占位，但路径必须合理。
- 页面漂亮不等于产品成立，必须有下一步转化动作。

## 第 2 课：从静态站升级到 SaaS

SaaS 和静态站的区别不是多几个按钮，而是多了用户、数据、权限和状态。

最小 SaaS 骨架：

- Public pages：Landing Page、Pricing、Login、Signup。
- Private pages：Dashboard、Settings、History。
- Database：users/profile、items/jobs/orders。
- Auth：注册、登录、退出、受保护路由。
- Storage：需要上传图片或文件时再加。

开发指令：

```text
请基于当前 Landing Page，规划一个最小 SaaS 版本。
先输出：
1. 页面列表；
2. 数据表设计；
3. 登录和权限规则；
4. 第一版只做哪些功能；
5. 本地验证步骤。
等我确认后再实现。
```

验收重点：

- 未登录用户不能进 dashboard。
- 用户只能看到自己的数据。
- 刷新页面后数据仍然存在。
- 线上环境变量和本地 `.env` 分开配置。

## 第 3 课：选择一个产品练习题

课程里最适合复刻的三类 SaaS：

| 练习题 | 核心能力 | 难点 |
| --- | --- | --- |
| 线索挖掘 SaaS | 表单、第三方 API、结果清洗、CSV 导出 | 合规、限流、线索质量 |
| AI 缩略图 SaaS | 文件上传、AI 图像 API、积分制、下载 | 上传权限、生成成本、支付回调 |
| 内容自动化分发 SaaS | 内容输入、voice profile、多平台改写、排期 | 平台 API、OAuth、自动发布边界 |

建议顺序：

1. 先做 mock 数据版本，确认用户路径。
2. 再接一个真实 API，不要同时接多个平台。
3. 加历史记录和导出。
4. 最后再加积分、订阅或自动发布。

## 第 4 课：安全是上线前最低门槛

只要出现用户数据、数据库、第三方 API、上传或支付，就必须跑安全闸门。

必查 5 项：

- 密钥和环境变量：真实 secret 不进前端、不进公开仓库。
- Supabase RLS：用户数据表开启 RLS，并有正确 policy。
- 服务端验证：不能只靠前端校验表单和余额。
- 依赖包：确认包真实、官方、维护中，没有明显漏洞。
- 认证中间件：私密页面和 API route 都要检查登录状态。

安全审计指令：

```text
请对当前项目做上线前安全审计。
重点检查密钥暴露、Supabase RLS、服务端验证、依赖包、认证中间件、限流、CORS 和文件上传权限。
先输出问题清单、严重程度、涉及文件、修复建议和验证方式，不要直接大范围改代码。
```

## 第 5 课：调试与迭代

Vibe Coding 的核心能力不是“永远不出 bug”，而是快速复现、定位、约束修改和复测。

标准排错模板：

```text
我遇到了一个 bug。

操作步骤：

期望结果：

实际结果：

发生环境：本地 / 线上

浏览器 console：

终端日志：

请先判断可能原因和涉及文件，再给最小修复方案。
不要改无关 UI、路由、数据库字段。
修复后告诉我如何验证。
```

每轮修复后必须做：

- 看 diff，确认 AI 改了哪些文件。
- 只复测当前 bug 不够，还要测关联链路。
- 新增页面、接口、上传、支付后重新跑安全检查。
- 稳定版本及时 commit。

## 第 6 课：把项目包装成商品

AI 做出的项目不能直接丢给客户。交付前至少准备：

- 在线演示站。
- 功能清单。
- 使用文档。
- 部署文档。
- 安全检查结果。
- 版本记录和已知限制。
- 维护期、bug 修复和新功能报价边界。

三种变现方式：

| 模式 | 适合什么 | 注意点 |
| --- | --- | --- |
| 定制开发 | 企业网站、内部工具、垂直仪表盘 | 需求和售后边界必须写清 |
| 订阅 SaaS | 线索、内容、AI 生成、自动化工具 | 要处理获客、运维、客服、安全和续费 |
| 模板售卖 | Landing Page、后台模板、行业套件 | 同质化强，要靠场景和教程包装 |

## 结课作业

从下面三个方向选一个做 MVP：

1. 一个垂直行业线索工具。
2. 一个积分制 AI 生成工具。
3. 一个内容改写和分发工作台。

交付物：

- 产品 brief。
- 可运行本地项目。
- 线上演示地址。
- 数据库和权限说明。
- 安全检查清单。
- 3 分钟 demo 脚本。
- 下一轮迭代计划。

## 最小评分标准

| 维度 | 合格标准 |
| --- | --- |
| 产品清晰度 | 能讲清目标用户、痛点、结果和付费理由 |
| 功能闭环 | 至少一条核心用户路径能跑通 |
| 数据持久化 | 登录后数据能保存并按用户隔离 |
| 安全意识 | 跑过密钥、RLS、服务端验证、依赖和认证检查 |
| 调试能力 | 出错时能提供复现、日志和最小修复范围 |
| 商业包装 | 有演示、文档、边界和下一步获客动作 |

## 参考来源

- 上游 Wiki：`Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环.md`
- 上游 Wiki：`Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单.md`
- 上游 Wiki：`Wiki/Vibe Coding/30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代.md`
- 上游 Wiki：`Wiki/Vibe Coding/30-Launch Safety/内容平台官方API与自动发布限制.md`
- 上游 Wiki：`Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架.md`
- 上游 Wiki：`Wiki/Vibe Coding/40-Business/Vibe Coding商业化与定价包装.md`
- 上游 Wiki：`Wiki/Vibe Coding/40-Business/中文市场Vibe Coding获客路径.md`
- 原始材料：`Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md`
- 审片记录：`Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md`
