---
type: wiki
status: compiled
area: Vibe Coding
tags:
  - Codex
  - VibeCoding
  - WebCoding
  - Firebase
  - Vercel
  - GitHub
  - CodexDesktop
  - Skills
  - MCP
  - Automations
updated: 2026-05-29
---

# Codex新手Vibe Coding工作流

## 解决什么问题

这套工作流面向没有工程背景、但想用 Codex / Claude Code 类 AI 编程工具做出真实 app 的用户。它不是教用户从语法开始学编程，而是先建立一套能跑通的产品交付路径：

```text
想法 -> 项目文件 -> 本地预览 -> Git/GitHub 保存 -> 后端 -> 调试 -> 部署 -> 自动化 / 并行迭代
```

核心目标是让新手理解：AI 编程不是“输入一句话然后结束”，而是围绕文件、运行、测试、报错、保存和部署不断循环。

## 新手必须先理解的 9 个概念

### 1. App 本质上是一组文件

对新手最重要的 mental model 是：app 不是神秘物，它首先是一个文件夹，里面有一堆代码文件。Codex 做的事，就是在这个文件夹里创建、编辑、删除文件。

### 2. Localhost 只在自己电脑上能打开

本地运行的 app 可以通过 `localhost` 预览，但这个链接不能直接发给别人。要让别人访问，需要部署到互联网上。

### 3. GitHub 是保存版本的地方

对非技术用户，可以先把 GitHub 理解成“代码版 Google Drive”：本地文件改了，不代表 GitHub 自动更新；需要 commit / push 才算保存到远端。

### 4. 后端解决登录、数据和文件

只在浏览器里保存的数据很容易丢。真实 app 通常需要：

- Authentication：用户登录。
- Database：保存文字、状态、分类、用户数据。
- Storage：保存截图、图片、视频、文件。

视频里用 Firebase 做这三件事。也可以换成 Supabase、Neon、Convex 等后端方案。

### 5. 调试要把证据交给 AI

不要只说“坏了”。更有效的是给 Codex：

- 浏览器 console 报错。
- 403 / permission denied / unauthorized domain 等错误信息。
- 截图和圈注。
- 你刚才做了什么、期望是什么、实际发生什么。

### 6. 三端 app 要共享同一个后端

Web、Electron 桌面、Swift iOS 如果要像同一个产品，就要共享同一套 authentication、database、storage，而不是各做各的数据。

### 7. Codex Desktop 是本地工作台，不只是聊天框

`OpenAI Codex Full Course 4 Hours: Build & Ship` 这门课强调的关键差异是：网页版 ChatGPT / Claude 更像“给建议”，Codex Desktop 更像“坐在你的电脑前执行”。它能读取项目文件、运行终端命令、打开本地预览、调用插件和技能，并把这些动作放在同一个项目线程里。

因此新手不要只把 Codex 当成“问答工具”，而要把它当成一个围绕项目文件夹工作的本地代理：

- 每个项目最好对应一个清晰文件夹。
- 重要上下文应该落到文件里，而不是只留在聊天历史。
- 每次生成、修复、部署都要回到文件、命令、日志、diff 和可运行结果。

### 8. Context、compaction 和语音输入会影响工作质量

长项目会消耗上下文窗口。文件内容、对话、终端输出、插件/技能信息都会占用 token。课程里把 `compaction` 作为长线程继续工作的关键机制：线程过长时需要压缩上下文，保留当前目标、已完成事项、关键文件和下一步。

语音输入的价值不是“更酷”，而是能让用户一次性说出更完整的需求、约束和背景。对新手来说，比起短促地输入“帮我改一下”，更好的方式是用语音把目标、现象、限制和验收标准说清楚。

### 9. 插件、Computer Use、Skills、MCP、Subagents 是五种不同扩展

这门 Codex 长课把 Codex 的能力扩展拆成五类：

| 能力 | 适合什么时候用 | 新手理解 |
| --- | --- | --- |
| Plugins | 已有官方/内置连接，如 Notion、Google Drive、Figma、Slack | 先用现成插座 |
| Computer Use | 需要真实操作本机软件、浏览器、App UI | 让 Codex 看屏幕、点按钮 |
| Skills | 你有重复工作流、个人 SOP、项目习惯 | 把“怎么做事”写成可复用操作手册 |
| MCP | 外部系统提供标准协议连接，或团队要共享连接能力 | 给 Codex 接一条标准数据管道 |
| Subagents | 可拆成多个互不冲突的并行研究、审查、开发任务 | 临时开多个小助手并行干活 |

不要一开始就全用。新手优先从项目文件、Git、运行和调试打基础；当某个动作重复出现，再考虑把它封装成 skill 或 automation。

## 标准流程

### 1. 建一个独立项目

不要把新 app 混在旧文件夹里。新建项目目录，让 Codex 在这个目录里工作。

第一步可以先让 Codex 创建一个简单 app，比如 paint app，目的是理解：

- AI 会创建哪些文件。
- 如何本地运行。
- 如何打开 preview。
- 如何让 AI 修改 UI。
- 如何测试按钮、undo、绘图等行为。

### 2. 把产品想法先写成 Markdown

复杂 app 不要直接一句话开工。先让 Codex 在项目里创建 `my-idea.md`，保存完整产品 brief。

好的 brief 应该包含：

- 这个 app 给谁用。
- 核心使用场景。
- 要保存什么数据。
- 用户怎么登录。
- 视觉感觉。
- 是否给人和 agent 同时使用。
- 哪些功能是第一版必须有，哪些可以后做。

### 3. 先设置后端，再让 Codex 构建

如果 app 需要登录、多人、图片、跨设备同步，就先准备后端。视频里的 Shared Brain 使用 Firebase：

- Firestore：保存条目、用户、分类、状态。
- Storage：保存截图和文件。
- Google Sign-In：用户登录。

注意：视频里把 Firebase 信息类比为密码；实际项目里需要区分公开配置和真正 secret。更关键的是安全规则、权限边界和不要泄露 OpenAI API key 等真正敏感密钥。

### 4. 第一次构建后马上测试

不要让 AI 连续做 10 个功能。第一版出来后，马上测试：

- 能不能登录。
- 能不能新增一条数据。
- 刷新后数据还在不在。
- Firebase 里是否真的出现用户和 item。
- 图片 / 截图是否进入 storage。

### 5. 用 console、截图和真实数据反馈

出错时，把证据交给 Codex：

```text
我在外部浏览器可以登录，但保存 item 失败。
我看到 insufficient permission。
这是 console 日志：
[粘贴日志]
```

UI 不满意时，用截图圈出区域：

```text
这张截图里，YouTube card 的 overlay 很奇怪。
请把它改成红色 play button，并修复 masonry grid 的布局。
```

### 6. 用 queue 和 steer 管理修改节奏

如果当前任务还在跑，后续 prompt 可以排队；如果发现方向不对，就直接 steer 进去纠偏。

适合 queue 的内容：

- 下一个独立 UI 调整。
- 另一个不冲突的小改动。

适合 steer 的内容：

- 当前方向明显错了。
- UI 重叠、权限规则、运行命令正在走偏。
- 需要立即改变 agent 的判断。

### 7. 部署到 Vercel

本地 app 没法给别人用。部署到 Vercel 后，要记得处理 auth domain：

- 本地 `localhost` 默认通常可以用。
- Vercel 域名需要加入 Firebase authorized domains。
- 自定义域名也要加入。

部署完成后，要重新测试登录、数据读取、数据写入和图片上传。

### 8. 再考虑桌面和 iOS

Web app 跑顺后，再让 Codex 规划桌面和 iOS：

- Electron：把 web app 包成桌面 app。
- Swift / Xcode：做 iOS app。
- 共享同一个 Firebase 后端。
- 在同一个项目里用 `apps/` 管理 web、desktop、ios。

不要一开始就同时做三端。先让 web app 证明核心体验成立。

## Codex Desktop 进阶工作流

`OpenAI Codex Full Course 4 Hours: Build & Ship` 补充了一条更完整的 Codex Desktop 工作流，适合已经能做第一个 Web App 后继续升级：

```text
项目文件夹
  -> Git repo / first commit
  -> 产品构思与计划
  -> GitHub Issues 拆任务
  -> 本地实现与测试
  -> Worktrees 并行开发
  -> Automations 定时巡检/更新
  -> Vercel 部署
  -> Issues / PR / 线上反馈继续迭代
```

这条线的重点不是换一个工具名，而是把“AI 写代码”变成一个可管理的工程系统：

| 环节 | Codex 怎么帮忙 | 人要守住什么 |
| --- | --- | --- |
| Git / GitHub | 初始化 repo、提交、分支、PR、解释 diff | 每个稳定点都要 commit，不要在脏乱工作区继续大改 |
| GitHub Issues | 把产品计划拆成 issue、更新状态、关联实现 | issue 必须可验证，不要写成愿望清单 |
| Automations | 定时跑进度汇总、bug 巡检、数据刷新 | 自动化上线前必须手动 run now 验证一次 |
| Worktrees | 并行处理多个独立功能或 bug | 分支边界要清晰，避免多个 agent 改同一片代码 |
| Skills | 复用项目规划、内容处理、发布、数据处理等流程 | skill 只写模型容易做错或需要稳定复用的规则 |
| Subagents | 并行读多个模块、做安全/架构/性能审查 | 子代理会消耗额度，适合可并行拆开的任务 |

## Codex 1 小时课补充的最小项目闭环

`Master 97% of Codex in 1 Hour` 的价值不在于“又一个 YouTube dashboard”，而在于它把新手第一小时应该理解的 Codex 形态压成了一个完整闭环：

```text
项目文件夹
  -> 读取本地上下文
  -> 写 AGENTS.md
  -> 规划 API 连接
  -> 生成 Excel / 数据报告
  -> 把成功流程封装成 skill
  -> 用 dashboard 可视化
  -> GitHub + Vercel 部署
  -> automation 定时刷新
  -> browser QA 点击验收
```

这里有三个值得放进新手页的判断：

1. Codex 项目本质上还是一个本地文件夹。用户可以让 Codex 读取其它本地目录做背景研究，但真正要长期保存的项目目标、上下文和规则要写回 `AGENTS.md` 或项目文档。
2. 不知道 API 怎么接时，先用 Plan Mode 让 Codex 研究并解释方案。YouTube 没有默认 plugin，就需要在 API key、OAuth 和数据范围之间做取舍。
3. 先让 Codex 完成一次手工工作流，等产物满意后再说“把刚才这套流程变成 skill / automation”。不要一上来就让 AI 写一个抽象自动化。

这个案例也提醒新手：AI 自动化不是创建后就不用管。第一次 automation 必须手动 `run now`，看它是否卡在权限、打开的文件、错误模型、推送失败或 Vercel 部署失败上。

## David Ondrej 课补充的 CLI 到部署闭环

`CODEX FULL COURSE: From Zero to Deployed App (2026)` 的增量价值不在于重新解释什么是 AI 编程，而是把完全新手在终端里第一次用 Codex 的路径讲得很细。它适合补到“第一天上手 Codex”的操作层：

```text
独立项目文件夹
  -> Node.js / Codex CLI
  -> 登录与额度确认
  -> 选择当前最强正式模型和合适 reasoning
  -> 写 AGENTS.md / README.md
  -> 用截图和 web search 补上下文
  -> 让 Codex 先问 4 个 MVP 问题
  -> 一次生成 V1
  -> 接 AI 图像 API / .env
  -> 本地调试
  -> Git 提交
  -> Vercel 部署
```

这条线有几个适合长期保留的判断：

1. **CLI 入门要先管住工作目录。** 新手可以先从终端启动，但必须在具体项目文件夹里运行 Codex，不能在用户根目录、桌面或一堆杂文件目录里开工。
2. **模型、订阅和价格是强时效信息。** 视频里的具体模型名、订阅档位和价格只作为 2026-04-11 的课程证据。Wiki 保留的原则是：用当前可用的强模型，简单任务用中高 reasoning，疑难 bug / 大重构再升到更高 reasoning；实际名称、价格和额度以官方界面为准。
3. **`AGENTS.md` 和 `README.md` 要分工。** 课程里把项目目标、受众、视觉参考和技术选择同步写进两个文件。长期项目里更稳的做法是：`AGENTS.md` 放稳定规则、禁止事项、固定命令和安全边界；`README.md`、`docs/` 或项目 brief 放会变化的产品背景、MVP 决策、调研结果和 API 文档。
4. **截图输入不是装饰，是上下文。** UI 参考图、报错截图、控制台错误、竞品布局都可以直接喂给 Codex。新手不要只用文字描述“像 Pinterest”，应同时给截图、指出要复用的是布局、密度、卡片比例还是动线。
5. **Web search 适合快速补用户研究和最新文档。** 课程里让 Codex 搜索常见面部医美项目，把调研结果写入 `README.md`。这类搜索适合做浅层行业扫描、竞品词汇和官方 API 格式核对；涉及价格、权限、模型能力和政策时仍要回官方源二次核验。
6. **一键生成前先让 Codex 问问题。** 比“直接做完整 app”更稳的是让 Codex 根据已有 `AGENTS.md` / `README.md` 先问 3-5 个缺口问题，例如是否真实调用 AI、是否需要账号、数据存哪里、第一版最看重什么。

适合新手复用的操作指令骨架：

```text
请先阅读 AGENTS.md 和 README.md。
在写代码前，问我 4 个必须澄清的问题：
1. 第一版是否需要真实调用 AI / 第三方 API？
2. 是否需要账号、数据库和文件存储？
3. 用户数据第一版保存在哪里？
4. 第一版最重要的验收标准是什么？

我回答后，请把决策写回 README.md 或 docs/brief.md，再开始实现。
```

## 技术栈不是唯一答案

早期新手课使用 Firebase 来解释 authentication、database、storage。Codex 4 小时课使用的是另一套适合 agentic coding 的 Web 栈：

```text
Next.js -> Convex -> Vercel
```

两者的启发不同：

| 方案 | 适合吸收的判断 |
| --- | --- |
| Firebase | 适合解释登录、数据库、存储三件套，和多端共享后端的基础概念 |
| Supabase | 适合 SQL、RLS、auth、storage 和上线安全训练 |
| Convex | 适合 TypeScript 全栈、减少迁移/SQL 摩擦、让前后端更贴近 agent 可编辑代码 |
| Vercel | 适合 Next.js 部署、预览 URL、GitHub push 后自动构建 |
| OpenRouter / AI 图像 API | 适合快速验证 AI 图片、缩略图、形象预览等 MVP，但必须处理密钥、额度上限、失败重试、延迟和隐私 |

Wiki 不需要把后端选型写成固定答案。更重要的是让用户知道：任何技术栈都要能被 AI 解释清楚、能本地运行、能部署、能验证数据和权限。

## 项目 brief 骨架

这是 Wiki 内的任务描述骨架，用来说明新手第一步应该让 Codex 先拆问题、再写代码。正式可复制的检查清单和 prompt 产物放在 Outputs 里维护。

```text
我想用 Codex 从 0 构建一个真实 Web App。

请先不要直接写完整代码。先帮我把项目拆成：
1. 前端页面和核心交互
2. 需要保存的数据
3. 是否需要 authentication
4. 是否需要 database
5. 是否需要 storage
6. 本地验证步骤
7. 部署前检查

然后请在项目里创建一个 my-idea.md，保存完整产品 brief。
等我确认后，再开始生成第一版 app。
```

## 常见坑

- 把 `localhost` 当成可分享网站。
- 本地改了 app，却忘了 commit 到 GitHub。
- 没有先验证数据库，结果只是前端假数据。
- 把 API key 直接放在前端或聊天里，缺少密钥管理意识。
- 只看 UI，不检查 Firebase / 后端是否真的写入。
- 一次让 AI 做 Web、桌面、iOS、支付、发布，范围失控。
- 出错时只说“不能用”，不给 console、截图和复现步骤。
- 不手动检查 diff，就让 Codex 一直改下去。
- 自动化任务没有先手动触发验证，就直接定时运行。
- 把 `AGENTS.md` 写成会快速过期的项目目录说明，反而误导模型。
- 把视频里的具体模型名、订阅价格和额度当成当前事实，使用前不核验官方界面。
- 在陌生项目或未提交代码的脏工作区里开 `--yolo` / full access。
- 把 OpenRouter、OpenAI、Stripe 等 API key 放进前端代码或提交到 Git。
- AI 图片生成一次串行跑 20 个请求，任何一个失败就卡住整个任务；更稳的是独立请求、并行/队列、失败可重试。

## 与其它页面的关系

- [[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]]：这页偏交付路线，边做边学页偏学习和判断力。
- [[Wiki/AI知识库/个人知识库到内容选题|个人知识库到内容选题]]：Shared Brain 这个例子本质上也是给人和 agent 共用的内容知识库。
- [[Wiki/AI营销自动化/AI一人营销团队#Gen Media|AI一人营销团队：Gen Media]]：两者都强调人和 agent 共用一个 app / 数据库。

## 可生成 Outputs

- 教程：Codex 新手从 0 做 WebApp。
- SOP：Codex 做 WebApp 检查清单。
- Prompt Output：Codex 新手项目 brief 发号施令 prompt。
- 课程 Output：Codex 新手 VibeCoding 课程大纲。
- 图文卡片：localhost、GitHub、Firebase、Vercel 的关系图。

## 来源

- [[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]：主来源，展示从简单 paint app 到 Shared Brain web app，再到 Vercel 部署、Electron 桌面和 Swift iOS 的完整流程。
- [[Clippings/OpenAI Codex Full Course 4 Hours Build & Ship|OpenAI Codex Full Course 4 Hours: Build & Ship]] + [[Raw/NotebookLM/2026-05-29--youtube--OpenAI Codex Full Course 4 Hours Build & Ship|NotebookLM 审片记录]]：补充 Codex Desktop、plugins、Computer Use、skills、MCP、subagents、GitHub Issues、automations、worktrees、Next.js + Convex + Vercel 和 Creator Carousel Studio 实战。
- [[Clippings/Master 97% of Codex in 1 Hour (full course)|Master 97% of Codex in 1 Hour]]：补充 YouTube comment intelligence 项目、API 接入、Excel 报告、skill 封装、weekly automation、GitHub / Vercel 和 Browser Use QA 的一小时闭环。
- [[Clippings/CODEX FULL COURSE From Zero to Deployed App (2026)|CODEX FULL COURSE: From Zero to Deployed App (2026)]] + [[Raw/NotebookLM/2026-05-29--youtube--CODEX FULL COURSE From Zero to Deployed App (2026)|NotebookLM 审片记录]]：补充 Codex CLI 零基础安装、项目目录、AGENTS/README 分工、截图输入、web search、AI 图像 API MVP、Cursor/IDE、Git 高频提交和 Vercel 部署。
