---
type: output
output_type: tool-comparison
status: superseded
target_reader: AI 编程新手 / 独立开发者 / 产品和运营转 WebCoding 用户
use_case: 旧版后端选择横评参考；当前主入口已改为后端选择知识召回 prompt 卡片
version_date: 2026-05-28
updated: 2026-05-28
superseded_by: "Outputs/SOP与模板/后端选择知识召回prompt卡片.md"
upstream_wiki:
  - "[[Wiki/Vibe Coding/10-Getting Started/后端与数据库选择|后端与数据库选择]]"
  - "[[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]"
references:
  - "[[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]"
---

# AI 新手做 WebApp，后端怎么选？

维护备注：上游 [[Wiki/Vibe Coding/10-Getting Started/后端与数据库选择|后端与数据库选择]] 已恢复为 Wiki 知识整理页。本输出保留为旧版，不应当作最终工具横评；面向用户提问的一版见 [[Outputs/SOP与模板/后端选择知识召回prompt卡片|后端选择知识召回 prompt 卡片]]。

这是初版框架，不是最终横评。当前主要依据是 `Vibe Coding for Beginners` 里的 Firebase 案例，以及 Vibe Coding 路线图里的后端节点。Firebase / Supabase / Neon 的价格、限制和最佳实践后续还需要补官方资料和实测案例。

## 先问：你现在需要后端吗？

如果只是做一个前端 demo，比如计算器、画板、展示页、小游戏，可以先不要后端。先让 app 在本地跑起来，验证交互就够了。

当你遇到这些需求时，再接后端：

- 用户要登录。
- 数据刷新后不能丢。
- 多台设备要同步。
- 团队成员要一起用。
- 要上传图片、截图、视频、文件。
- 要控制谁能看、谁能改、谁能删。
- 要部署给别人长期使用。

## 后端三件套

新手不要一上来纠结产品名，先理解后端通常在解决三件事：

- `Authentication`：谁在用，比如 Google 登录。
- `Database`：保存文字和结构化数据，比如用户、item、分类、状态。
- `Storage`：保存文件，比如截图、图片、视频、PDF。

你做的 app 需要哪几件，决定了你选什么工具。

## Firebase / Supabase / Neon 初版判断

| 工具 | 更像什么 | 适合谁 | 新手主要坑 |
| --- | --- | --- | --- |
| Firebase | 登录 + NoSQL 数据库 + 文件存储一体化后端 | 想快速做出带登录、数据库、截图上传的原型 | rules、storage 权限、authorized domains、billing |
| Supabase | Postgres + auth + storage 的 app 后端 | 想学 SQL / 表结构 / 真实数据库模型的人 | RLS、policy、anon key / service role key、schema 设计 |
| Neon | 云 Postgres 数据库 | 已经有后端或框架，只缺数据库的人 | 不是完整后端；auth / storage 要另配 |

## 最简单的选择

如果你是 AI 编程新手：

- 只是 demo：先不用后端。
- 想最快做出可登录、可保存、可上传截图的 app：先用 Firebase。
- 想认真学数据库、SQL、长期产品结构：考虑 Supabase。
- 已经知道自己需要 Postgres，并且有服务端框架：考虑 Neon。

## 不要让 AI 替你跳过判断

不要直接说：

```text
帮我接一个后端。
```

更好的 prompt 是：

```text
请先不要写代码。
我的 app 是：[说明]
用户是：[自己 / 团队 / 公开用户]
需要保存：[数据和文件]
需要登录：[是 / 否]
需要多人协作：[是 / 否]

请判断我现在是否需要后端。
如果需要，请比较 Firebase、Supabase、Neon。
告诉我推荐哪个，为什么不选另外两个，以及第一版最小数据结构。
```

## 接后端后必须验证

不管选哪个，都要检查：

- 登录后是否真的创建用户。
- 新增数据后数据库里是否真的有记录。
- 刷新页面后数据是否还在。
- 换账号后权限是否正确。
- 上传文件后 storage 是否真的有文件。
- 部署后 auth domain / callback / 环境变量是否正确。
- API key / secret 没有错误暴露。

## 当前结论要保守

这一版只能作为新手决策框架。正式教程和强推荐之前，还要补：

- Firebase 官方规则和部署配置。
- Supabase RLS / storage / key 边界。
- Neon 的定位和连接方式。
- 三者价格、免费额度、部署平台适配。
- AI agent 生成权限规则时的常见错误。

## 参考来源

- [[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]：提供 Firebase 登录、Firestore、Storage、Vercel authorized domains 和调试案例。
- [[Wiki/Vibe Coding/10-Getting Started/后端与数据库选择|后端与数据库选择]]：本输出的上游 Wiki。
