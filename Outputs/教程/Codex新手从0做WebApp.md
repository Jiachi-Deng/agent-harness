---
type: output
output_type: tutorial
status: review-ready
target_reader: Codex / Claude Code 新手、普通 AI 编程用户、想做 WebCoding 的产品和运营
use_case: 帮新手跑通第一个本地 Web App、GitHub 保存、后端接入、部署和多端计划
version_date: 2026-05-28
updated: 2026-05-28
upstream_wiki:
  - "[[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]"
related_outputs:
  - "[[Outputs/课程与训练营/Codex新手VibeCoding课程|Codex新手VibeCoding课程]]"
references:
  - "[[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]"
---

# Codex 新手从 0 做 WebApp

这篇适合完全没写过代码、但想用 Codex / Claude Code 类 AI 编程工具做出一个真实 Web App 的人。

先说清楚：不要把 vibe coding 理解成“说一句话，AI 自动交付产品”。更靠谱的理解是：你用自然语言指挥 AI 在一个项目文件夹里写代码、运行 app、修 bug、保存版本、接后端、部署上线。

维护备注：本篇是新手第一条链路，不承担完整 SaaS 上线、安全审计、支付、平台 API 和中文市场商业化。项目一旦涉及真实用户、数据库、上传、支付或第三方 API，应切到 [[Outputs/SOP与模板/Vibe Coding SaaS上线检查清单|Vibe Coding SaaS 上线检查清单]] 和 [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding 全栈 SaaS 开发闭环]]。

## 你先要懂的 4 件事

### 1. App 是一个文件夹

一个 app 首先是一个文件夹，里面有很多代码文件。Codex 做的事，就是在这个文件夹里创建和修改文件。

### 2. Localhost 不是互联网

Codex 帮你跑起来的本地预览，通常是 `localhost`。这个链接只能在你自己电脑上打开。要给别人用，需要部署。

### 3. GitHub 是保存版本

你可以先把 GitHub 理解成代码版云盘。Codex 在本地改了文件，不代表 GitHub 自动更新。你要让它 commit / push。

### 4. 后端负责保存数据

只存在浏览器里的数据，刷新或换设备可能就没了。真实 app 通常需要：

- 登录：知道谁在用。
- 数据库：保存文字、分类、状态。
- 存储：保存图片、截图、视频。

## 第一步：先做一个超简单 app

不要一上来就做复杂产品。先让 Codex 创建一个简单 web app，比如：

```text
请创建一个简单的 Microsoft Paint 风格 Web App，并在本地运行。
```

跑起来以后，手动测试它：

- 能不能画画。
- 颜色选择器能不能用。
- 橡皮、填充、undo 是否可用。

然后再让 Codex 改一版：

```text
请把顶部和底部栏改成更像 Apple 风格，并加入 undo 功能。
```

这一步的目的不是做画图软件，而是让你理解 AI 编程的基本循环：prompt -> 生成文件 -> 本地运行 -> 测试 -> 继续修改。

## 第二步：保存到 GitHub

当本地 app 能跑以后，建一个 private GitHub repo，然后告诉 Codex：

```text
我创建了一个新的 GitHub repo：
[repo 链接]

请把当前项目上传到这个 repo。
```

以后每做完一轮满意修改，就说：

```text
请 commit 并 push 当前修改到 GitHub。
```

这会帮你保留版本，避免本地项目越改越乱。

## 第三步：写产品 brief

复杂 app 不要直接一句话开工。先写清楚你要做什么。比如 Shared Brain 这种内部内容知识库，可以这样写：

```text
我想做一个内部 Web App，叫 Shared Brain。

它用来保存团队未来可能制作成内容的素材：
- X / Twitter 帖子
- YouTube 视频
- Instagram 内容
- 文章
- 截图
- loose ideas

每个 item 应该有标题、来源、平台、分类、状态、备注、计划拍摄日期。
它应该是一个视觉化 library，像私人的内容操作系统。
人可以用，AI agent 也可以读取和写入。
```

然后让 Codex 保存到项目里：

```text
请创建一个 my-idea.md，把上面的产品想法完整保存进去。
后续构建时请始终参考这个文件。
```

## 第四步：先准备后端

如果你要登录、多人使用、保存链接、上传截图，就需要后端。视频里使用 Firebase，你可以先理解成三件事：

- Authentication：Google 登录。
- Firestore：保存 item、用户、分类。
- Storage：保存截图和文件。

准备好后端后，再告诉 Codex：

```text
我已经创建了 Firebase 项目，并开启了 Authentication、Firestore 和 Storage。
请基于 my-idea.md 构建完整 app。
要求使用 Google Sign-In，数据保存到 Firestore，截图保存到 Storage。
```

正式项目里要特别注意密钥和权限。不要随意公开真正的 API key 或 secret；后端安全规则也必须检查。

## 第五步：第一版出来后立刻验证

不要只看 UI 好不好看。按这个顺序测：

- 能不能登录。
- 能不能新增 X / YouTube / Instagram 链接。
- 能不能上传截图。
- 刷新后数据还在不在。
- Firebase 里是否真的有用户和 item。
- Storage 里是否真的有图片。

如果保存失败，不要只说“坏了”。打开浏览器 Inspect / Console，把报错贴给 Codex。

```text
我在外部浏览器可以登录，但保存 item 失败。
页面提示 insufficient permission。
这是 console 日志：
[粘贴日志]

请判断是 Firestore rules、Storage rules、auth session 还是前端写入路径的问题。
修完后告诉我如何验证。
```

## 第六步：用截图改 UI

UI 问题最适合截图反馈。你可以截图圈出区域，然后说：

```text
这张截图里，YouTube 卡片的 overlay 很奇怪。
请改成红色 play button。
另外卡片没有形成 masonry grid，请修复布局。
```

如果要改搜索和筛选，也直接说清楚：

```text
请把 category、platform、user 都做成 search bar 右侧的 dropdown。
默认只显示我的 posts，但可以切换到 all users。
```

## 第七步：加一点 AI 功能

真实 app 可以调用模型 API 做轻量任务，比如自动给素材生成标题。

```text
请加入一个轻量 AI 标题生成能力。
当用户添加 X、YouTube、Instagram 或截图时，
自动生成一个短标题，少于 6 个字，尽量保守、准确、直白。
```

这里要注意成本和密钥管理。每次调用模型都会有成本；API key 不应该随意暴露。

## 第八步：部署到 Vercel

本地跑通以后，让 Codex 部署：

```text
请把这个 Web App 部署到 Vercel，并给我 public URL。
```

如果 Google 登录报 `unauthorized domain`，通常需要去 Firebase Authentication settings，把 Vercel 域名加入 authorized domains。

部署后重新测试：

- 外部浏览器能否打开。
- Google 登录能否成功。
- 数据是否还是同一份。
- 上传截图是否成功。

## 第九步：再考虑桌面和 iOS

Web app 跑顺以后，才考虑桌面和 iOS。可以先让 Codex 做计划：

```text
我想把这个 Web App 转成桌面 app 和 iOS app。
请先写一个 markdown 计划，不要直接实现。

要求：
- desktop 使用 Electron。
- iOS 使用 Swift / Xcode。
- 三端共享同一个 Firebase 后端。
- 说明项目目录应该如何组织。
- 说明每端需要分别测试什么。
```

确认计划后，再让它实现。不要一开始就同时追 Web、桌面、iOS，否则新手很难判断哪里出了问题。

## 最小成功标准

你的第一个 Codex Web App，不需要很复杂。达到这些就够了：

- 本地能跑。
- GitHub 有保存。
- 能登录。
- 数据真的进数据库。
- 图片真的进 storage。
- 能用 console 和截图让 AI 修 bug。
- 能部署到公网 URL。

先完成这条链路，比堆 20 个功能更重要。

## 参考来源

- [[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]：YouTube clipping，展示从简单 paint app、Shared Brain、Firebase、Vercel 到 Electron / iOS 的完整新手流程。
