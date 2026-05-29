---
type: wiki
status: living
area: Vibe Coding
tags:
  - VibeCoding
  - 路线图
  - roadmap.sh
  - Codex
  - Claude Code
  - AI编程
updated: 2026-05-29
---

# Vibe Coding专题路线图

## 这个专题解决什么

`Vibe Coding` 不是只收“怎么让 AI 写代码”，而是收普通人、独立开发者、运营/产品和小团队如何用 AI agent 做出能运行、能保存、能上线、能维护的 app。

这个专题的核心问题是：

- 新手如何从一个想法开始，让 AI 做出第一个 web app？
- 如何避免只会复制 AI 输出，却不理解 app 的基本运行方式？
- 如何把 demo 做成有登录、有数据库、有部署的真实产品原型？
- 如何用截图、console、日志、测试和 GitHub 控制 AI 编程质量？
- 如何判断什么时候该扩展到桌面、iOS、支付、团队协作和商业化？
- 如何从 `vibe coding` 进入更专业的 `agentic engineering`：既提高速度，又保住质量、安全和可维护性。

## 路线图骨架

这是一份采集骨架，不是最终教程，也不是固定目录。后续用户把文章、视频、案例、工具文档放进 `Clippings/` 或 `Raw/` 后，优先按下面的节点归档、编译和补证。

迭代规则：

- 路线图节点可以随着新材料和讨论随时合并、拆分、改名、升降级。
- 如果某个节点长期只有零散观点，不急着建独立页面，先作为本页采集槽保留。
- 如果某个节点积累出可照做的教程、案例、SOP 或工具判断，再拆成独立 Wiki 页面。
- 如果后续材料证明 roadmap.sh 原始顺序不适合我们的中文学习路径，以本知识库的实际使用场景为准。
- 每次明显调整路线图结构，都要在 `log.md` 记录调整原因和影响范围。

来源锚点：

- `roadmap.sh/vibe-coding`：提供当前路线图的节点层级和视觉布局参考。
- [[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]：提供 Codex 新手实操课的第一批证据。
- [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]：吸收 YouTube 全栈 SaaS 课程里的开发闭环、安全、调试、多代理和商业化知识。
- [[Wiki/AI行业判断/从VibeCoding到AgenticEngineering|从Vibe Coding到Agentic Engineering]]：提供从 vibe coding 走向 agentic engineering 的行业判断。
- [[Clippings/Master 97% of Codex in 1 Hour (full course)|Master 97% of Codex in 1 Hour]]：补充 Codex 一小时项目闭环、skills、automations、dashboard、GitHub / Vercel 和 Browser QA。
- [[Clippings/CODEX FULL COURSE From Zero to Deployed App (2026)|CODEX FULL COURSE: From Zero to Deployed App (2026)]]：补充 Codex CLI 零基础安装、AGENTS/README 项目上下文、截图输入、web search、AI 图像 API MVP、Git 和部署。

维护视图：

- [[../90-Maintenance/Vibe Coding专题维护视图|Vibe Coding专题维护视图]]：记录页面角色、脆弱区、维护队列和 Output 影响队列。路线图负责材料归位，维护视图负责防腐和下一步整理。

### 1. 基础理解

| 节点                     | 中文采集名           | 当前状态        | 适合收什么材料                   |
| ---------------------- | --------------- | ----------- | ------------------------- |
| What is vibe coding?   | 什么是 Vibe Coding | 已有 Wiki + Prompt Output | 定义、边界、适用/不适用场景、真实案例       |
| The vibe coder mindset | Vibe Coder 心态   | 已有旁证        | 不外包理解、快速试错、人工判断、taste、质量线 |

挂接页面：

- [[Wiki/AI行业判断/从VibeCoding到AgenticEngineering|从Vibe Coding到Agentic Engineering]]
- [[Wiki/AI使用方法/不要外包你的学习|不要外包你的学习]]

### 2. AI Assisted Coding Tools

| 节点          | 中文采集名          | 当前状态    | 适合收什么材料                                            |
| ----------- | -------------- | ------- | -------------------------------------------------- |
| Claude Code | Claude Code    | 待补      | 官方教程、实战项目、subagents、rules / CLAUDE.md、调试案例         |
| Gemini      | Gemini         | 待补      | 长上下文、代码辅助、和 Google 生态结合的案例                         |
| Codex       | Codex          | 已有主干 + 多门长课 | Codex CLI / desktop / cloud、skills、plugins、MCP、subagents、automations、worktrees、调试、部署 |
| Cursor      | Cursor         | 待补      | IDE 内 AI 编程、rules、repo 级上下文、对比案例                   |
| Windsurf    | Windsurf       | 待补      | agentic IDE、项目级编辑、多人/团队案例                          |
| Copilot     | GitHub Copilot | 待补      | IDE 补全、Agent mode、GitHub 工作流                       |
| v0          | v0             | 待补      | UI 生成、Next.js、shadcn、落地页和后台界面                      |
| Lovable     | Lovable        | 待补      | AI app builder、Supabase、原型到产品的边界                   |

挂接页面：

- [[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]
- [[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]
- [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]

### 3. Plan before you Code

| 节点                                | 中文采集名                   | 当前状态    | 适合收什么材料                             |
| --------------------------------- | ----------------------- | ------- | ----------------------------------- |
| Plan what you need to develop     | 先拆 MVP 与阶段              | 已有 seed | 需求澄清、MVP 分期、功能列表、PRD / spec 案例      |
| Work step by step                 | 小步实现                    | 已有 seed | 一次只做一个 vertical slice、小步验证、避免大爆炸修改  |
| Illustrate AI with examples       | 给 AI 参考图和样例             | 待补      | mockup、截图、参考站、代码样例、设计图如何喂给 AI       |
| Implement Spec-Driven Development | Spec-Driven Development | 待补      | spec-first、验收标准、任务拆分、从 spec 到 tests |

挂接页面：

- [[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]
- [[Outputs/SOP与模板/Codex做WebApp检查清单|Codex做WebApp检查清单]]

### 4. Tech Stack and Coding

| 节点                                | 中文采集名                   | 当前状态    | 适合收什么材料                                       |
| --------------------------------- | ----------------------- | ------- | --------------------------------------------- |
| Pick a popular tech stack         | 选主流技术栈                  | 已有 seed | Next.js、Vite、Firebase、Supabase、Vercel 等新手稳定组合 |
| Document style/coding preferences | 记录代码风格偏好                | 待补      | AGENTS.md、CLAUDE.md、Cursor rules、项目规范         |
| Keep code modular                 | 保持模块小                   | 待补      | 文件拆分、组件边界、service/helper 分层、反模式               |
| Ask AI to review/refactor         | 让 AI 定期 review/refactor | 已有旁证    | refactor prompt、代码审查、复杂度降低、重构前后对比             |
| Use skills created by others      | 复用别人写好的 skills          | 已有 seed | skill 安装、skill 评估、适配和安全边界                     |

挂接页面：

- [[Wiki/Vibe Coding/10-Getting Started/后端与数据库选择|后端与数据库选择]]
- [[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]]
- [[Wiki/Vibe Coding/60-Agent Skills/Agent Skills仓库索引|Agent Skills仓库索引]]
- [[Wiki/Vibe Coding/60-Agent Skills/Matt Pocock Skills仓库|Matt Pocock Skills仓库]]
- [[Wiki/Vibe Coding/60-Agent Skills/LearnPrompt Karpathy Skills仓库|LearnPrompt Karpathy Skills仓库]]

### 5. Security Best Practices

| 节点 | 中文采集名 | 当前状态 | 适合收什么材料 |
| --- | --- | --- | --- |
| Ask AI to perform security audit | 让 AI 做安全审计 | 已有主干 | auth、RLS、CORS、输入校验、依赖漏洞、上线前审计 |
| Never hardcode credentials | 不要硬编码密钥 | 已有主干 | env vars、secret 管理、前后端 key 边界、泄露轮换 |

挂接页面：

- [[Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单|Vibe Coding安全审计清单]]

未来适合生成：

- Output：Vibe Coding 新手安全检查清单。
- Wiki：AI 编程中的 API Key 与环境变量。

### 6. Prompting Best Practices

| 节点                           | 中文采集名          | 当前状态    | 适合收什么材料                                         |
| ---------------------------- | -------------- | ------- | ----------------------------------------------- |
| Ask for one task at a time   | 一次只交代一个任务      | 已有 seed | prompt 拆分、scope 控制、避免一次做五件事                     |
| Be specific                  | 具体描述目标         | 已有 seed | 好坏 prompt 对比、验收标准、UI 细节、错误复现                    |
| Tell AI what not to do       | 告诉 AI 不要做什么    | 待补      | 负面约束、不要重构、不要换库、不要删数据                            |
| Give mockups/reference files | 给 mockup 和参考文件 | 已有主干    | screenshot、Figma、Excalidraw、示例代码、竞品链接           |
| Use “act as” framing         | 使用角色 framing   | 已有旁证    | act as reviewer / architect / UX researcher 的边界 |
| Update context document      | 更新上下文文档        | 已有旁证    | AGENTS.md、CLAUDE.md、rules 文件、项目记忆               |
| Tell AI to think/brainstorm  | 复杂问题先思考        | 待补      | plan mode、方案比较、风险清单、先问问题再实现                     |

挂接页面：

- [[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]]
- [[Outputs/SOP与模板/Codex做WebApp检查清单|Codex做WebApp检查清单]]
- [[Outputs/SOP与模板/Cinematic Landing Page Builder Prompt中英对照|Cinematic Landing Page Builder Prompt中英对照]]

### 7. Context

| 节点 | 中文采集名 | 当前状态 | 适合收什么材料 |
| --- | --- | --- | --- |
| Use long context when needed | 必要时使用长上下文 | 待补 | 大 repo、长文档、设计上下文、成本和漂移问题 |
| If AI fails after 3 prompts, start fresh | 三轮失败就新开会话 | 待补 | 卡住案例、上下文污染、重新最小复现 |
| Clean/start new sessions for unrelated tasks | 无关任务清上下文 | 待补 | 多任务切换、上下文管理、会话边界 |
| Use subagents if possible | 使用 subagents | 待补 | 任务分工、researcher/reviewer/debugger、并行代理 |

### 8. Debugging

| 节点 | 中文采集名 | 当前状态 | 适合收什么材料 |
| --- | --- | --- | --- |
| Prompt the error message | 把错误信息交给 AI | 已有主干 | console、stack trace、build error、auth callback、CORS |
| Ask AI for possible causes | 让 AI 列可能原因 | 已有主干 | hypothesis list、排查树、最小复现 |
| Ask AI to add logs | 让 AI 加日志定位 | 已有主干 | instrumentation、server/client logs、feature flags |
| Use MCP / Playwright when possible | 使用 MCP / Playwright 验证 | 待补 | 浏览器自动化、截图验证、交互测试、回归测试 |

挂接页面：

- [[Outputs/SOP与模板/Codex做WebApp检查清单|Codex做WebApp检查清单]]
- [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架|Vibe Coding调试与迭代框架]]

### 9. Master Version Control

| 节点 | 中文采集名 | 当前状态 | 适合收什么材料 |
| --- | --- | --- | --- |
| Commit regularly | 经常提交 | 已有 seed | AI 每完成一步就 commit、commit message、检查 diff |
| Start each feature with clean Git slate | 新功能前保持干净工作区 | 待补 | 分支、stash、dirty tree、多人协作 |
| Revert with Git | 用 Git 回滚 | 待补 | revert、reset 风险、恢复文件、避免 AI 原生回滚 |
| Ask AI to handle Git/GitHub CLI tasks | 让 AI 辅助 Git/GitHub CLI | 待补 | issue、PR、branch、release、changelog |

### 10. Testing

| 节点 | 中文采集名 | 当前状态 | 适合收什么材料 |
| --- | --- | --- | --- |
| Ask AI to write tests | 让 AI 写测试 | 已有 seed | 单测、E2E、组件测试、测试覆盖缺口 |
| Consider TDD | 考虑 TDD | 待补 | red-green-refactor、AI 辅助 TDD、适用边界 |
| Ask AI to write breaking test then fix | 先写失败测试再修 bug | 待补 | bug reproduction、regression test、修复验收 |
| Refactor once tests are in place | 有测试后再重构 | 待补 | 安全重构、复杂代码拆分、性能优化 |

### 11. 对应视觉产物

- [[Outputs/图文卡片/vibe-coding-roadmap.excalidraw|Vibe Coding 路线图 Excalidraw 可编辑版]]
- [[Outputs/图文卡片/vibe-coding-roadmap-clickable.excalidraw|Vibe Coding 路线图 Excalidraw 可点击版]]

## 已有主干

### 1. Codex 新手从 0 到 Web App

入口：[[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]

这条主干解决新手的完整交付路径：

```text
项目文件 -> 本地运行 -> GitHub -> 后端 -> 调试 -> 部署 -> 多端扩展
```

对应产物：

- [[Outputs/教程/Codex新手从0做WebApp|Codex新手从0做WebApp]]
- [[Outputs/SOP与模板/Codex做WebApp检查清单|Codex做WebApp检查清单]]
- [[Outputs/课程与训练营/Codex新手VibeCoding课程|Codex新手VibeCoding课程]]

### 2. AI 编程边做边学

入口：[[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]]

这条主干解决长期能力问题：不要把理解外包给 AI。它适合和所有实操教程搭配使用。

对应产物：

- [[Outputs/教程/AI编程不要只让AI代写：一套边做边学的实战工作流|AI编程不要只让AI代写]]

### 3. 从 Vibe Coding 到 Agentic Engineering

入口：[[Wiki/AI行业判断/从VibeCoding到AgenticEngineering|从Vibe Coding到Agentic Engineering]]

这条主干提供行业级判断：vibe coding 提高软件创造下限，但严肃产品需要 agentic engineering 来保住质量线。它会影响本专题里的调试、验证、安全、spec、部署和工程评审标准。

### 4. Vibe Coding 全栈 SaaS 开发闭环

入口：[[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]

这条主干来自用户已审片的 YouTube 长课，但在 Wiki 中不再维护成课程页，而是沉淀为主题知识骨架，覆盖：

```text
静态站 -> SaaS -> 安全 -> 部署 -> 多代理 -> 调试 -> 商业化
```

当前已拆出的可复用页面和相关 Outputs：

- [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]
- [[Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单|Vibe Coding安全审计清单]]
- [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架|Vibe Coding调试与迭代框架]]
- [[Outputs/SOP与模板/Cinematic Landing Page Builder Prompt中英对照|Cinematic Landing Page Builder Prompt中英对照]]
- [[Wiki/Vibe Coding/40-Business/Vibe Coding商业化与定价包装|Vibe Coding商业化与定价包装]]
- [[Wiki/Vibe Coding/50-SaaS产品模式/线索挖掘SaaS产品模式|线索挖掘SaaS产品模式]]
- [[Wiki/Vibe Coding/50-SaaS产品模式/AI缩略图生成SaaS产品模式|AI缩略图生成SaaS产品模式]]
- [[Wiki/Vibe Coding/50-SaaS产品模式/内容自动化分发SaaS产品模式|内容自动化分发SaaS产品模式]]
- [[Wiki/Vibe Coding/50-SaaS产品模式/API包装型SaaS机会与风险|API包装型SaaS机会与风险]]
- [[Wiki/Vibe Coding/30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代|SaaS支付方案：Stripe积分订阅Webhook与国内替代]]
- [[Wiki/Vibe Coding/30-Launch Safety/内容平台官方API与自动发布限制|内容平台官方API与自动发布限制]]
- [[Wiki/Vibe Coding/40-Business/中文市场Vibe Coding获客路径|中文市场Vibe Coding获客路径]]
- [[Outputs/SOP与模板/Vibe Coding安全审计Prompt中英对照|Vibe Coding安全审计Prompt中英对照]]
- [[Outputs/SOP与模板/Cinematic Landing Page Builder Prompt中英对照|Cinematic Landing Page Builder Prompt中英对照]]

## 自然生长的子节点

这些不是预设分类，而是从当前材料里已经长出来、后续值得继续补材料的节点。

| 子节点 | 当前状态 | 适合收什么材料 | 未来产物 |
| --- | --- | --- | --- |
| Codex / Claude Code 入门 | 已有 seed | 新手完整课、界面讲解、项目管理、skill / plugin 使用 | 入门课、术语卡、第一小时指南 |
| Web App 从 0 到上线 | 已有 seed | 从 idea 到 localhost、GitHub、Vercel 的案例 | 保姆级教程、项目模板 |
| 后端与数据库 | 已有 Wiki + Prompt Output | 真实项目选择、权限坑、官方变化、部署问题、成本复盘 | 知识召回 prompt 卡片、真实踩坑案例、上线验证清单 |
| 调试与验证 | 已有主干 | console、logs、screenshot、browser inspect、测试、回归检查 | SOP、debug checklist |
| 部署与域名 | 已有旁证 | Vercel、Cloudflare、Netlify、authorized domains、环境变量 | 部署教程、上线检查表 |
| 内置 AI 能力 | 已有 seed | OpenAI / OpenRouter / Anthropic API、轻量模型、图像生成、成本、key 管理 | API 接入教程、成本表 |
| 支付与计费 | 已有主干 | Stripe、积分、订阅、webhook、微信支付、支付宝 | 支付检查清单、积分制模板 |
| 平台 API 与内容发布 | 已有主干 | YouTube、B站、公众号、小红书、抖音、LinkedIn、X | 平台接入表、半自动发布 SOP |
| 中文市场获客 | 已有主干 | 私域、社群、短视频、案例、分销、渠道 | 冷启动 SOP、话术模板 |
| Prompt Outputs | 已有 Outputs | 安全审计、Landing Page、调试、项目规划、获客话术 | 中英文对照模板、Prompt Pack |
| 多端扩展 | 待生长 | Electron、Tauri、Swift、React Native、PWA | Web 转桌面 / iOS 路线比较 |
| 人和 agent 共用的 app | 已有相关页 | agent-readable database、skills、mini app、shared workspace | 工作流、案例拆解 |
| Agentic Engineering | 已有 seed | spec、verification、security、quality bar、AI-native engineering | 观点解读、工程检查清单 |
| 生产级 Agent 产品工程 | 已有主干 | tool-calling agent、skills、多 agent、eval、数据飞轮、观测性 | agent 产品上线清单、架构选型卡 |
| Vibe Coding 商业化 | 已有主干 | 定价、包装、交付、售后边界 | 变现路线图、报价模板、交付包 |
| AI 一人公司 | 已有主干 | Idea/MVP/Launch/Scale、AI OS、创始人知识系统化、咨询到项目 | 创业阶段检查清单、一小时 AI 咨询 SOP |
| API 包装型 SaaS | 已有主干 | Apify、Stripe、AI API、第三方接口、积分、限流 | 选题检查表、API wrapper 案例拆解 |
| 内容自动化 SaaS | 已有主干 | 内容改写、多平台分发、任务队列、平台 API、热更新 | 内容流水线教程、SaaS 蓝图 |

相关页面：

- [[Wiki/AI营销自动化/AI一人营销团队#Gen Media|AI一人营销团队：Gen Media]]
- [[Wiki/AI知识库/个人知识库到内容选题|个人知识库到内容选题]]

## 材料进入规则

以后新的 clipping / raw 如果属于 AI 编程 / Vibe Coding，先问它更像哪个节点：

- 如果是新手全流程课，进入 `Codex / Claude Code 入门` 或 `Web App 从 0 到上线`。
- 如果主要讲 Firebase / Supabase / Neon 的通用概念，优先并入 `后端与数据库` 的问题框架和核验点；需要交付给用户时再生成知识召回 prompt Output。真实案例、踩坑、官方变化、价格限制或部署复盘进入证据层。
- 如果主要讲报错、console、截图反馈、测试，进入 `调试与验证`。
- 如果主要讲 Vercel / Cloudflare / 域名 / 环境变量，进入 `部署与域名`。
- 如果主要讲 OpenAI API、模型调用、成本、key，进入 `内置 AI 能力`。
- 如果主要讲报价、交付包、售后边界、产品包装，进入 `Vibe Coding 商业化`。
- 如果主要讲 outbound / inbound / affiliate、社群、短视频、私域、话术、成交复盘，进入 `中文市场获客`。
- 如果主要讲 API wrapper、第三方接口、积分、限流和 SaaS 机会判断，进入 `API 包装型 SaaS`。
- 如果主要讲 Electron / Tauri / iOS / mobile，进入 `多端扩展`。
- 如果主要讲 agent 能读写 app / database / workspace，进入 `人和 agent 共用的 app`。
- 如果主要讲 vibe coding、agentic engineering、Software 3.0、verifiability，进入 `AI行业判断`，再反向链接到本专题。
- 如果主要讲生产级 agent 产品、tool calling、eval、训练数据、反馈飞轮和多 agent 架构，进入 [[Wiki/AI产品工程/README|AI产品工程]]。
- 如果主要讲创始人阶段、AI 一人公司、AI Operating System、咨询小时到项目/retainer，进入 [[Wiki/AI一人公司/README|AI一人公司]]，再把具体开发/交付动作回流到本专题。

如果一个材料覆盖多个节点，不要拆散原文；在 Wiki 里拆观点，并在 clipping 的 `compiled_to` 里链接多个页面。

## 何时新建页面

不要因为表格里有节点就立刻建空页面。新页面至少要满足一个条件：

- 有一篇高质量 clipping 能支撑完整结构。
- 有多篇材料都在反复讲同一个问题。
- 已经能写出输入、步骤、输出、常见坑和检查清单。
- 已经能生成一个教程、SOP、比较或课程练习。

否则先把它留在路线图里，等材料继续长出来。

## 当前缺口

### 1. 后端与数据库不再补通用百科

[[Wiki/Vibe Coding/10-Getting Started/后端与数据库选择|后端与数据库选择]] 已改回 Wiki 知识整理页，并生成 [[Outputs/SOP与模板/后端选择知识召回prompt卡片|后端选择知识召回 prompt 卡片]]。Firebase / Supabase / Neon / Convex 的通用比较不再扩写成百科，后续重点补真实证据和核验点。

后续只补这些增量：

- 真实项目为什么选某个后端。
- AI 自动生成 auth / RLS / rules / schema 的失败案例。
- 官方价格、免费额度、地区、API 和部署限制变化。
- 从纯前端 demo 升级到后端时的 UI 操作和配置复盘。
- 与支付、AI API、文件存储、队列、用户权限相关的真实坑。

### 2. 部署与域名还不够

已有 Netlify / Vercel 旁证，但还需要补 Cloudflare Pages / Workers、Netlify 深入、自定义域名、环境变量、serverless function、preview deploy、回滚和日志材料。

### 3. 测试、浏览器验证和回归机制仍需补强

现在已有调试循环，并已从 Codex 一小时课补入 Browser Use QA，但对 TDD、失败测试、Playwright/browser 验证、上线前回归和 bug 复现用例的材料还不够。后续应该补“让 AI 写失败测试再修复”“前端交互自动验证”“截图/控制台/网络请求一起看”的案例。

### 4. 内置 AI 能力和 API 成本需要单独深挖

课程已经触及 OpenAI / Anthropic / 图像生成 / Apify 等第三方 API，但还没有形成稳定的“AI 功能接入”主干。需要补模型选择、API key 边界、成本估算、限流、队列、缓存、失败重试和账单保护。

### 5. 多端扩展还只是概念级

Electron 和 Swift/iOS 只是从视频里抽到一条案例，尚不足以生成稳定教程。需要更多真实项目案例和官方/工程材料。

### 6. 中文市场获客需要真实案例校验

已有 [[Wiki/Vibe Coding/40-Business/中文市场Vibe Coding获客路径|中文市场Vibe Coding获客路径]] 作为本地化策略页，但还缺真实成交案例、社群/短视频/私域复盘、价格包、失败话术和服务交付边界。

### 7. 强时效页需要定期刷新

[[Wiki/Vibe Coding/30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代|支付方案]] 和 [[Wiki/Vibe Coding/30-Launch Safety/内容平台官方API与自动发布限制|平台 API 限制]] 已补官方资料，但支付、平台 API、权限、价格和审核政策变化快，必须保留 `verified` 和 `refresh_after` 机制。

## 近期编译优先级

1. 中文市场真实案例：定制服务、陪跑、SaaS 账号、模板/源码和分销的成交路径。
2. 最新工具边界：Claude Code、Codex、Antigravity、Cursor、v0、Lovable 的真实可用性和失败点。
3. UI 操作复盘：真实界面、配置后台、部署控制台、平台审核流程和人工操作路径。
4. 强时效政策：平台 API、支付、模型能力、价格、权限、封号规则。
5. 高价值 prompt Outputs：发号施令 prompt 和知识召回 prompt 的持续打磨。
6. 测试与浏览器验证：Playwright、失败测试、回归检查、上线前走测。

## 来源

- [[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]：提供 Codex 新手从项目、本地运行、GitHub、Firebase、Vercel 到多端扩展的主干案例。
- [[Clippings/Andrej Karpathy From Vibe Coding to Agentic Engineering|Andrej Karpathy: From Vibe Coding to Agentic Engineering]]：提供 vibe coding、agentic engineering、Software 3.0、可验证性和理解不可外包的行业判断。
- [[Clippings/Don't Outsource the Learning|Don't Outsource the Learning]]：提供“不要把理解外包出去”的学习边界。
- [[Clippings/Designing, Refining, and Maintaining Agent Skills at Perplexity|Designing, Refining, and Maintaining Agent Skills at Perplexity]]：提供 gotchas / 负面样例沉淀的旁证。
- [[Clippings/Master 97% of Codex in 1 Hour (full course)|Master 97% of Codex in 1 Hour]]：提供 Codex 从本地项目、YouTube API、Excel 报告、skill、dashboard、Vercel、automation 到 Browser QA 的一小时闭环。
- [[Clippings/CODEX FULL COURSE From Zero to Deployed App (2026)|CODEX FULL COURSE: From Zero to Deployed App (2026)]]：提供 Codex CLI 零基础起步、Beauty Mirror AI 图像 MVP、OpenRouter API、Cursor/IDE、Git 高频提交和 Vercel 部署旁证。
