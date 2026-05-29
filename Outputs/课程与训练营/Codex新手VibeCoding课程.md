---
type: output
output_type: course-outline
status: review-ready
target_reader: AI 编程新手、不会写代码但想用 Codex 做真实 app 的普通用户、独立开发者、产品/运营和课程学员
use_case: 作为 Codex 新手入门课大纲，组织课节、练习和评审标准
version_date: 2026-05-29
upstream_wiki:
  - "[[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]"
  - "[[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]]"
  - "[[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]"
references:
  - "[[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]"
  - "[[Clippings/OpenAI Codex Full Course 4 Hours Build & Ship|OpenAI Codex Full Course 4 Hours Build & Ship]]"
tags:
  - Codex
  - VibeCoding
  - WebCoding
  - 课程结构
  - 新手入门
  - CodexDesktop
  - Skills
  - Automations
updated: 2026-05-29
---

# Codex新手VibeCoding课程

## 课程定位

这门课面向“不会写代码，但想用 AI 做出真实 app”的普通用户、独立开发者、产品 / 运营和课程学员。

课程不从语法讲起，而是从真实构建流程讲起：项目、文件、本地运行、GitHub、后端、调试、部署和多端扩展。

## 学完应该会什么

学员完成后应该能：

- 用 Codex 创建一个独立项目。
- 理解 app、项目文件、localhost、GitHub repo 的关系。
- 写出一个能让 AI 执行的产品 brief。
- 用 Firebase / 类似后端给 app 加登录、数据库和文件存储。
- 用 console、截图、错误信息让 AI 修 bug。
- 把 web app 部署到 Vercel。
- 判断什么时候适合扩展到桌面 / iOS。

## 课程模块

### 第 1 课：AI 编程不是魔法，是文件循环

目标：建立最小 mental model。

内容：

- app = 文件夹 + 代码文件 + 运行命令。
- Codex 在项目目录里创建和修改文件。
- local preview 是本机运行，不是互联网网站。

练习：

- 创建一个简单 paint app。
- 让 Codex 加一个 undo 功能。
- 本地打开并手动测试。

### 第 2 课：GitHub 保存你的 app

目标：理解 repo、commit、push。

内容：

- GitHub 可以先理解成代码版云盘。
- 本地修改和远端 repo 不是一回事。
- 什么时候需要 commit。

练习：

- 创建 private GitHub repo。
- 让 Codex 上传项目。
- 修改 UI 后再 commit 一次。

### 第 3 课：把想法写成产品 brief

目标：让 AI 有稳定上下文。

内容：

- 为什么复杂 app 要先写 `my-idea.md`。
- brief 应包含用户、场景、数据、权限、视觉、agent 使用方式。
- “一句话需求”和“可执行 brief”的区别。

练习：

- 写一个 Shared Brain 类 app brief。
- 让 Codex 把 brief 保存进项目。

### 第 4 课：后端三件套：登录、数据库、存储

目标：理解 Firebase / 后端为什么必要。

内容：

- Authentication：谁在用。
- Database：保存文字、状态、分类、用户。
- Storage：保存图片、截图、视频。
- 安全规则和密钥边界。

练习：

- 建 Firebase 项目。
- 开启 Firestore、Storage、Google Sign-In。
- 让 Codex 接入后端。

### 第 5 课：从能跑到能用

目标：学会真实测试。

内容：

- 测登录。
- 测新增 item。
- 测刷新后数据是否还在。
- 去 Firebase console 查数据。
- 上传截图并验证 storage。

练习：

- 保存 X / YouTube / Instagram 链接。
- 上传截图。
- 检查 Firebase 中的数据和文件。

### 第 6 课：用证据驱动 Codex 修 bug

目标：学会调试协作。

内容：

- Inspect Element / Console。
- 403、permission denied、unauthorized domain。
- 截图反馈和局部圈注。
- queue vs steer。

练习：

- 故意触发一个权限错误。
- 复制 console 给 Codex。
- 用截图要求修 UI 重叠或 card 样式。

### 第 7 课：给 app 加 AI 能力

目标：理解 API 和成本。

内容：

- 为什么 app 需要 OpenAI / Anthropic / 其它模型 API。
- API key、调用成本和轻量模型。
- 用 AI 自动生成短标题、分类、摘要。

练习：

- 给 item 自动生成 6 个字以内标题。
- 比较 AI title 和原始 metadata title。

### 第 8 课：部署到互联网

目标：让别人能打开。

内容：

- localhost 和 public URL 的区别。
- Vercel 部署。
- Firebase authorized domains。
- 部署后重新测试登录和数据。

练习：

- 部署到 Vercel。
- 添加 Vercel 域名到 Firebase。
- 用外部浏览器登录并确认数据同步。

### 第 9 课：从 Web 到桌面和 iOS

目标：理解多端扩展边界。

内容：

- 先 web 后桌面 / iOS。
- Electron 是 web app 的桌面包装路径之一。
- Swift / Xcode / Simulator 用于 iOS。
- 三端共享同一个后端。

练习：

- 让 Codex 先写多端转换计划。
- 评审计划后再执行。
- 验证 web 和 desktop 数据同步。

## 进阶补充课：Codex Desktop 系统课

`OpenAI Codex Full Course 4 Hours: Build & Ship` 更适合作为本课程的进阶补充，而不是替代前 9 课。前 9 课解决“新手第一次做出真实 app”，这门 4 小时课解决“如何把 Codex Desktop 当成长期工作台”。

可吸收为 8 个进阶模块：

| 进阶模块 | 学员要掌握什么 | 对应 Wiki 去向 |
| --- | --- | --- |
| Codex Desktop 基础 | 项目、线程、文件树、终端、模型、reasoning、权限 | `Codex新手Vibe Coding工作流` |
| Context 与语音输入 | context window、compaction、语音 prompt、长线程续航 | `AI编程边做边学工作流` / Codex 工作流 |
| 五大能力扩展 | plugins、Computer Use、skills、MCP、subagents 的区别 | `Codex新手Vibe Coding工作流` / `Agent Skills仓库索引` |
| Git / GitHub | repo、commit、branch、PR、review UI、diff | Codex 工作流 / 调试框架 |
| 产品规划 | 用 ideation / planning skills 把想法拆成方案和任务 | Vibe Coding 全栈 SaaS 闭环 |
| Issues 与 Automations | 用 GitHub Issues 管理 backlog，用 automation 做定时巡检 | 全栈 SaaS 闭环 / 调试框架 |
| Worktrees | 多分支、多工作区并行开发，配合启动脚本和环境变量 | 全栈 SaaS 闭环 |
| Creator Carousel Studio | 用 Next.js + Convex + Vercel 做社交媒体轮播图生成工具 | 全栈 SaaS 闭环 / 案例拆解候选 |

教学取舍：

- 不把订阅价格、模型版本、UI 按钮位置写成长期结论；这些属于强时效内容，后续需要按日期刷新。
- 保留可复用的工作流：文件夹项目、Git 稳定点、issues、skills、automations、worktrees、部署验证。
- 对 `AGENTS.md` 的讲法要谨慎：只写稳定规则，不写会快速过期的目录地图。
- 对 full access 的讲法要加安全边界：新手先默认权限，重度使用再配合 destructive command guard 和 Git 回滚点。

## 评审标准

一个学员项目合格，不是看“AI 写了多少代码”，而是看：

- 能本地运行。
- 有 GitHub 版本保存。
- 有真实后端数据。
- 能解释 auth / database / storage 的作用。
- 出错时能提供 console、截图和复现步骤。
- 部署后能在外部浏览器使用。
- 没有把敏感 key 随意暴露。

## 可生成 Outputs

- 教程：Codex 新手从 0 做 WebApp。
- SOP：Codex 做 WebApp 检查清单。
- 课程作业：做一个 Shared Brain 类内部工具。
- PPT：VibeCoding 入门训练营第一课。

## 来源

- [[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]：主来源，提供完整课程案例和步骤顺序。
- [[Clippings/OpenAI Codex Full Course 4 Hours Build & Ship|OpenAI Codex Full Course 4 Hours: Build & Ship]]：进阶来源，提供 Codex Desktop、skills、MCP、subagents、GitHub Issues、automations、worktrees 和 Next.js + Convex + Vercel 实战。
- [[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]：本课程从该工作流整理而来。
