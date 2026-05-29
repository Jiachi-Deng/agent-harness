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
  - Debugging
  - Iteration
  - ClaudeCode
  - Gemini
  - Codex
  - Automations
  - Subagents
  - Worktrees
---

# Vibe Coding调试与迭代框架

## 这个框架解决什么

Vibe Coding 不是“AI 一次生成完就结束”。真实项目里，AI 会理解错需求、写出 bug、遗漏权限、部署失败，甚至修一个问题带出三个新问题。

这门课里最值得复用的调试原则是：人不需要逐行手修代码，但必须学会复现问题、提供证据、限制 AI 改动范围，并且改一点测一点。

## 5 类常见 Bug

| 类型 | 用户看到的现象 | 优先交给谁 | 常见原因 |
| --- | --- | --- | --- |
| UI / 样式 bug | 排版错位、按钮变形、图片不显示、动画失效 | Gemini | CSS、响应式、图片路径、组件结构 |
| 交互 / 业务逻辑 bug | 点击没反应、表单不提交、页面跳错 | Claude Code | handler、route、状态流、表单逻辑 |
| 数据库 bug | 登录后看不到数据、数据不入库、看到别人数据 | Claude Code | Supabase 连接、RLS、表结构、用户 id 绑定 |
| 部署 / 环境 bug | 本地能跑，Netlify 上 404、密钥失效、资源丢失 | Claude Code + 人工核对平台配置 | 环境变量、路径、重定向、构建命令 |
| 第三方接口 bug | 爬虫、邮件、AI 绘图、支付调用失败 | Claude Code | API key、请求格式、限流、服务商变更 |

## 排错五步

### 1. 复现并记录

不要说“坏了”。要记录：

- 操作步骤。
- 出错页面或功能。
- 期望结果和实际结果。
- 本地还是线上。
- 浏览器 console、终端日志、网络请求、截图。

### 2. 看日志缩小范围

优先看三类证据：

- Terminal：构建、运行、数据库、依赖、接口错误。
- Browser console / Network：前端异常、请求失败、状态码。
- Changes / diff：上一轮 AI 到底改了哪些文件。

### 3. 下达带约束的修复指令

每次修 bug 都要限制 AI：

```text
请只排查并修复【具体模块/功能】。
先说明你认为的原因、涉及文件和修复方案，再动手。
只做增量修改，不要全局重构，不要改无关 UI、路由、数据库字段。
修复后说明我应该怎么验证。
```

### 4. 改一点，测一点

不要让 AI 一口气“顺便优化”。一轮只解决一个明确问题：

1. AI 给方案。
2. 人确认范围。
3. AI 小改。
4. 人立刻复测。
5. 如果失败，把新现象继续反馈。

### 5. 全量复测并存档

修复当前问题后，还要测关联链路：

- 登录/退出。
- 数据读取/写入。
- 私密页面访问。
- 移动端/无痕模式。
- 线上环境变量。
- 安全审计清单。

通过后用 Git commit 或版本标记保存稳定点。

## 迭代功能也按同一套流程

新增功能不是“让 AI 加一下”。标准流程：

1. 先写清楚功能目标、用户路径和验收标准。
2. 划定修改范围，要求不动稳定模块。
3. 让 AI 先出方案和文件清单。
4. 分模块开发和测试。
5. 新增页面、接口、表单、数据表后重新跑安全审计。
6. 本地通过后再部署。

## Codex Desktop 的迭代机制

Codex 4 小时课补充了更系统的迭代方式：把“修 bug / 加功能 / 部署 / 回查”都变成可观察、可回滚、可并行的流程。

| 机制 | 能解决什么 | 使用边界 |
| --- | --- | --- |
| Review UI / diff | 看清 Codex 改了哪些文件 | 不看 diff 就不要合并大改 |
| Git commit / branch / PR | 保存稳定点、隔离功能、支持回滚 | 每个稳定功能都应 commit |
| GitHub Issues | 把待办、bug、功能拆成可追踪任务 | issue 要有验收标准 |
| Subagents | 并行做代码阅读、模块审查、安全/性能检查 | 会消耗额度，适合可拆分任务 |
| Worktrees | 多分支并行开发，互不污染主工作区 | 需要启动脚本和环境变量管理 |
| Automations | 定时做巡检、总结、数据刷新、简单 bug triage | 必须先手动 run now 验证 |
| Computer Use | 操作真实 UI、浏览器、本地 app，做视觉和交互验证 | 适合没有 API 或必须看界面的场景 |

### Browser QA 要变成默认验收动作

`Master 97% of Codex in 1 Hour` 里最值得吸收的一点是：dashboard 做完后，不应该只让 AI 自查代码。要让它打开真实浏览器，点击 tab、filter、search、external link、空状态和移动端布局，尝试把页面用坏。

适合交给 Browser Use / Playwright / Computer Use 的验收动作：

- 点击每个 tab、按钮、链接和筛选器。
- 搜索不存在的关键词，检查空状态。
- 检查外链能不能打开，是否跳错目标。
- 改变数据范围，确认图表和列表同步。
- 用移动端尺寸看文字、卡片和按钮是否溢出。
- 把发现的问题转成修复计划，而不是直接大改。

这类 QA 可以写进 skill 或项目规则里：在 dashboard、game、landing page、表单、后台页面返回给用户之前，先完成一次浏览器走测，并说明通过项、失败项和仍需人工确认的项。

### 权限和 guardrail 是调试的一部分

课程里强调 `default permissions` 和 `full access` 的取舍：默认权限更安全，但会频繁打断；full access 更顺滑，但可能误删、误改或执行危险命令。

可复用原则：

- 新手先用默认权限，理解 Codex 会运行哪些命令。
- 重度项目可以用 full access，但要配合 destructive command guard、Git 稳定点和备份。
- 涉及删除、重置、批量移动文件、数据库写入、线上部署前，必须让 Codex 先说明计划和影响范围。

### AI API / 图像生成类错误要同时看三层

David Ondrej 的 Codex 课用 OpenRouter 图像模型做 Beauty Mirror，暴露了生成类 app 的典型调试方式：不能只看前端按钮有没有反应，要同时看浏览器、服务端和供应商 API 文档。

排查顺序：

1. 浏览器 console / network：请求有没有发出、状态码是什么、前端是否把错误吞掉。
2. 本地终端日志：服务端 route 是否拿到 `.env`，请求体是否符合 API 格式，模型返回的错误是什么。
3. 供应商文档：图片传参、base64 / URL、模型 slug、并发限制、文件大小和鉴权格式是否已经变化。

可复用做法：

- 把当前供应商 API 的关键调用格式摘进 `docs/<vendor>-api-notes.md`，让 Codex 修 bug 时先读文档。
- 给 API key 设置额度上限，测试期只充值小额，避免循环调用烧钱。
- 生成 15-20 个候选图时，不要让一个失败拖死全部结果；用独立任务、并行/队列、局部失败状态和可重试按钮。
- 报错修复后，至少验证“成功生成、单个失败、全部失败、额度不足、无图片上传”五种状态。

### AGENTS.md 不要写成过期地图

NotebookLM 记录里有一个重要提醒：`AGENTS.md` 不应该盲目写很多目录结构、表结构和易变细节。它更适合放稳定规则，例如：

- 项目必须使用某个 Python / Node 版本。
- 不允许使用某些包或命令。
- 测试、构建、部署的固定命令。
- 本项目特殊的安全边界。

如果把会变化的目录、表、功能清单全写进 `AGENTS.md`，后续反而会误导模型。

## 7 个高频误区

- 只说“这个不好用”，不提供复现步骤。
- 把截图给 AI，却不贴 console 和终端日志。
- 一次让 AI 修 bug、改 UI、加功能、重构结构。
- 不看 diff，不知道 AI 改了哪里。
- 本地通过后不测线上环境。
- 修了功能但没测权限和 RLS。
- 没有 Git 稳定点，越改越回不去。
- 使用 subagents / worktrees 并行，但没有把任务拆到互不冲突的文件和模块。
- 自动化跑失败后只看结果，不检查权限、环境变量、网络和插件/skill 访问。
- 页面看起来能打开，但没有让浏览器代理真实点击、筛选、搜索和测试空状态。
- automation 长时间卡住时不及时打断询问原因，导致 token 和时间被浪费在本可人工快速解决的阻塞上。
- AI API 调用失败时只反复让 Codex 改代码，不回查供应商文档、请求格式、额度、限流和服务端日志。

## 可生成 Outputs

- `Vibe Coding 排错五步卡片`
- `AI 修 Bug 提示词模板`
- `本地能跑但线上失败排查 SOP`

## 证据锚点

- NotebookLM 审片记录：模块四 `Vibe Coding 通用调试、迭代框架`。
- 原始 transcript：03:13:10 之后的调试、部署和后续项目排错段落。
- [[Clippings/OpenAI Codex Full Course 4 Hours Build & Ship|OpenAI Codex Full Course 4 Hours: Build & Ship]]：权限与 guardrail、AGENTS.md、subagents、Git/GitHub、Issues、Automations、worktrees 和 Creator Carousel Studio 迭代段落。
- [[Clippings/Master 97% of Codex in 1 Hour (full course)|Master 97% of Codex in 1 Hour]]：Browser Use QA、weekly automation run-now、模型/推理设置、Excel 文件锁定和自动化瘦身经验。
- [[Clippings/CODEX FULL COURSE From Zero to Deployed App (2026)|CODEX FULL COURSE: From Zero to Deployed App (2026)]]：截图输入、OpenRouter 图像 API 调试、`.env`、供应商文档、串行/并行生成和 `--yolo` 权限提醒。
