# AI编程与 Vibe Coding

这个专题收普通人、独立开发者、产品/运营和小团队如何用 AI 做出能运行、能保存、能上线、能维护的 app。

现在这个目录按知识主线排序，不再把课程、工作流、案例判断、强时效页和维护页分散到不同顶层目录。Prompt、课程大纲、练习和讲义作为交付产物放在 `Outputs/`，不再放进 Wiki 目录。

## 目录结构

```text
00-Overview/          # 主干路线图和专题定位
10-Getting Started/   # 新手入门、学习方法、基础概念
20-SaaS Build/        # 从静态页到 SaaS 的构建、调试和迭代
30-Launch Safety/     # 安全、支付、平台 API、上线前高风险事项
40-Business/          # 商业化、获客、中文市场本地化
50-SaaS产品模式/     # 可复刻 SaaS 方向、产品模式和机会判断
60-Agent Skills/      # agent skills、技能仓库、把经验封装成可调用能力
90-Maintenance/       # 专题维护、防腐、页面角色和队列
```

## 先读什么

| 目标 | 入口 | 下一步 |
| --- | --- | --- |
| 先理解 Vibe Coding | [[00-Overview/Vibe Coding专题路线图|Vibe Coding 专题路线图]] | [[10-Getting Started/AI编程边做边学工作流|AI 编程边做边学工作流]] |
| 做第一个 Web App | [[10-Getting Started/Codex新手Vibe Coding工作流|Codex新手 Vibe Coding 工作流]] | [[Outputs/课程与训练营/Codex新手VibeCoding课程|Codex 新手 Vibe Coding 课程]] |
| 判断要不要后端 | [[10-Getting Started/后端与数据库选择|后端与数据库选择]] | 只把真实项目选择、权限坑、价格变化回流到 Wiki |
| 从静态页升级 SaaS | [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding 全栈 SaaS 开发闭环]] | [[20-SaaS Build/Vibe Coding调试与迭代框架|Vibe Coding 调试与迭代框架]] |
| 做 Landing Page | [[Outputs/SOP与模板/Cinematic Landing Page Builder Prompt中英对照|Landing Page 发号施令 prompt]] | [[Outputs/课程与训练营/Vibe Coding全栈SaaS实战课讲义|Vibe Coding 全栈 SaaS 实战课讲义]] |
| 上线、演示或收费 | [[30-Launch Safety/Vibe Coding安全审计清单|Vibe Coding 安全审计清单]] | [[Outputs/SOP与模板/Vibe Coding SaaS上线检查清单|Vibe Coding SaaS 上线检查清单]] |
| 处理支付和平台发布 | [[30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代|SaaS 支付方案]] | [[30-Launch Safety/内容平台官方API与自动发布限制|内容平台官方 API 与自动发布限制]] |
| 找项目方向 | [[50-SaaS产品模式/API包装型SaaS机会与风险|API 包装型 SaaS 机会与风险]] | [[Wiki/Vibe Coding/50-SaaS产品模式/线索挖掘SaaS产品模式|线索挖掘 SaaS 产品模式]]、[[Wiki/Vibe Coding/50-SaaS产品模式/AI缩略图生成SaaS产品模式|AI 缩略图生成 SaaS 产品模式]] |
| 理解 Agent Skills | [[60-Agent Skills/Agent Skills仓库索引|Agent Skills 仓库索引]] | [[60-Agent Skills/Matt Pocock Skills仓库|Matt Pocock Skills 仓库]]、[[60-Agent Skills/LearnPrompt Karpathy Skills仓库|LearnPrompt Karpathy Skills 仓库]] |
| 做商业化 | [[40-Business/Vibe Coding商业化与定价包装|Vibe Coding 商业化与定价包装]] | [[40-Business/中文市场Vibe Coding获客路径|中文市场 Vibe Coding 获客路径]] |
| 做 AI 一人公司 | [[Wiki/AI一人公司/AI原生创业生命周期|AI 原生创业生命周期]] | 回到本专题处理 MVP、SaaS 开发、调试和交付边界 |
| 做生产级 Agent 产品 | [[Wiki/AI产品工程/生产级Agent产品工程|生产级 Agent 产品工程]] | 回到本专题处理 Codex / Claude Code 的实现和验证 |
| 维护这个专题 | [[90-Maintenance/Vibe Coding专题维护视图|Vibe Coding 专题维护视图]] | 每次新增材料后检查主干、旧页、Outputs 和维护队列 |

## 页面主次

- `00-Overview/Vibe Coding专题路线图.md` 是主干页，负责材料归位和路线图节点状态。
- `10-Getting Started/` 负责新手第一层理解和基础工作流。
- `20-SaaS Build/` 负责构建和迭代，不放支付、平台 API 这类高风险时效信息；Landing Page 的任务逻辑沉淀在开发闭环里，正式 prompt 在 `Outputs/SOP与模板/`。
- `30-Launch Safety/` 负责上线前高风险事项，里面的支付和平台 API 页必须定期刷新。
- `40-Business/Vibe Coding商业化与定价包装.md` 负责包装、定价、交付和售后边界，不展开获客动作。
- `40-Business/中文市场Vibe Coding获客路径.md` 是当前获客主页面，并已吸收海外课程的 outbound / inbound / affiliate 三法。
- `50-SaaS产品模式/API包装型SaaS机会与风险.md` 是机会判断总论，具体产品模式继续放在 `50-SaaS产品模式/` 下。
- `60-Agent Skills/` 负责沉淀 skills 仓库、方法封装和 agent 可调用能力，不做泛泛工具目录。
- `90-Maintenance/` 只服务 Wiki 维护，不是读者学习入口。

## 材料归位规则

| 新材料主要讲什么 | 优先进入哪里 |
| --- | --- |
| 新手从想法到第一个 Web App | `10-Getting Started/` |
| 静态站升级成 SaaS、调试、部署迭代 | `20-SaaS Build/` 或 `Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环` |
| 密钥、RLS、支付、平台 API、上线风险 | `30-Launch Safety/` |
| 报价、交付包、售后边界、产品包装 | `40-Business/Vibe Coding商业化与定价包装.md` |
| 获客渠道、话术、中文市场、成交复盘 | `40-Business/中文市场Vibe Coding获客路径.md` |
| API wrapper、AI 工具、内容自动化这类方向判断 | `50-SaaS产品模式/API包装型SaaS机会与风险.md` 或 `50-SaaS产品模式/` 下的具体产品模式页 |
| agent skills、技能仓库、把经验封装成可调用能力 | `60-Agent Skills/Agent Skills仓库索引.md` |
| 创始人阶段、Idea/MVP/Launch/Scale、AI 一人公司 | `Wiki/AI一人公司/` |
| 生产级 agent 产品、tool calling、评估、数据飞轮、多 agent 架构 | `Wiki/AI产品工程/` |

如果新材料覆盖多个方向，不拆原文；先把判断拆进对应主页面，再在来源 metadata 里链接多个去向。

## Wiki 整理与 Prompt 输出

| 类型 | 处理方式 | 例子 |
| --- | --- | --- |
| AI 完全熟悉、稳定、但用户不知道怎么问 | Wiki 整理问题框架、讲解路径和证据缺口；需要交付时生成知识召回 prompt Output | Vibe Coding 第一层理解、后端与数据库基础概念 |
| AI 能讲但容易过度乐观 | Wiki 只保留核验点、风险和真实反馈入口 | 安全、权限、支付、部署、调试 |
| AI 不擅长或变化快 | 沉淀证据、案例、截图、复盘和强时效页 | 工具真实体验、中文市场获客、平台 API 限制、UI 操作路径 |
| 高价值可执行 prompt | Wiki 沉淀任务模型和验收逻辑；Outputs 生成中英文对照发号施令 prompt | 安全审计、Landing Page 生成 |

## 当前脆弱区

这些方向不要靠 AI 通用回答补，要等真实材料、用户反馈或官方核验：

- AI 编程工具真实体验：Claude Code、Codex、Cursor、Windsurf、v0、Lovable 等。
- 测试与浏览器验证：Playwright、失败测试、console/network/screenshot 联合验证。
- 部署与域名：Cloudflare、Vercel、Netlify、自定义域名、环境变量、回滚和日志。
- 中文市场获客：真实成交、报价包、失败话术、私域/社群/短视频复盘。
- 内置 AI 能力与 API 成本：key 边界、限流、队列、缓存、账单保护。
- 多端扩展：Electron、Tauri、Swift/iOS、PWA 的真实工程边界。

具体队列见 [[90-Maintenance/Vibe Coding专题维护视图|专题维护视图]]。
