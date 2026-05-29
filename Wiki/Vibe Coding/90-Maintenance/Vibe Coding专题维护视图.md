---
type: wiki
status: living
area: Vibe Coding
updated: 2026-05-29
tags:
  - VibeCoding
  - Wiki维护
  - 维护队列
  - 路线图
---

# Vibe Coding专题维护视图

这个页面不是教程，也不是路线图本身。它是 Vibe Coding 专题的维护控制台：用来判断现有页面各自承担什么角色、哪些内容已经成熟、哪些地方正在腐烂、下一轮应该优先整理什么。

## 维护原则

- 不把 Wiki 写成 AI 百科。AI 完全熟悉、稳定、且不依赖真实用户体验的内容，优先整理成问题框架、讲解路径和核验点；需要交付时再生成知识召回 prompt Output。
- 依赖真实上手体验、界面交互、工具稳定性、生成质量、模型状态或市场反馈的内容，不只做知识召回 prompt，必须沉淀证据、案例、复盘或强时效台账。
- 每次编译新材料后，不只新增页面，还要检查入口页、路线图、旧结论、Outputs 和维护队列是否需要更新。
- 旧页面不急着删除。能保留证据价值的旧页，标注状态、降级为 reference 或挂到正确主干下。
- 只有涉及用户业务定位、课程读者定位、输出形态和私有材料时，才需要和用户讨论；链接、状态、重复合并、索引挂接由 AI 自主维护。

## 页面角色地图

| 角色 | 页面 | 当前判断 | 维护动作 |
| --- | --- | --- | --- |
| 专题入口 | [[../README|Vibe Coding README]] | 给用户快速进入专题，应该保持短而清楚 | 只放目录结构、主线入口和脆弱区，不塞长篇内容 |
| 路线图主干 | [[../00-Overview/Vibe Coding专题路线图|Vibe Coding专题路线图]] | living 主干页，负责节点、缺口和材料进入规则 | 新材料先回填节点，再决定拆页或合并 |
| 新手工作流 | [[../10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]、[[../10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]] | 已成熟，可继续生成入门教程和检查清单 | 后续只补真实新手卡点、UI 操作和失败案例 |
| SaaS 工作流 | [[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]] | 已成熟，是全栈课的骨架页 | 重点补测试、部署、权限、支付和线上回归证据 |
| 产品模式页 | [[Wiki/Vibe Coding/50-SaaS产品模式/线索挖掘SaaS产品模式|线索挖掘SaaS产品模式]]、[[Wiki/Vibe Coding/50-SaaS产品模式/AI缩略图生成SaaS产品模式|AI缩略图生成SaaS产品模式]] | 已能支撑案例集 Output | 后续补真实复刻、成本、失败点和中文市场反馈 |
| Agent Skills | [[../60-Agent Skills/Agent Skills仓库索引|Agent Skills仓库索引]]、[[../60-Agent Skills/Matt Pocock Skills仓库|Matt Pocock Skills仓库]]、[[../60-Agent Skills/LearnPrompt Karpathy Skills仓库|LearnPrompt Karpathy Skills仓库]] | 已从旧工具目录归位为 Vibe Coding 的能力封装分支 | 后续只吸收能解释 agent 可调用能力、skills 设计和复用边界的材料 |
| 业务判断页 | [[../50-SaaS产品模式/API包装型SaaS机会与风险|API包装型SaaS机会与风险]]、[[../40-Business/Vibe Coding商业化与定价包装|Vibe Coding商业化与定价包装]]、[[../40-Business/中文市场Vibe Coding获客路径|中文市场Vibe Coding获客路径]] | 商业化页负责包装/定价/交付边界；获客页负责渠道/话术/中文市场复盘；API wrapper 页负责方向判断 | 报价和交付边界进商业化页；成交路径和渠道复盘进获客页；具体项目沉淀为产品模式页 |
| 跨主题上游 | [[Wiki/AI产品工程/生产级Agent产品工程|生产级Agent产品工程]]、[[Wiki/AI一人公司/AI原生创业生命周期|AI原生创业生命周期]] | 分别负责生产级 agent 工程和 AI 原生创业生命周期 | 只把与 Vibe Coding 直接相关的实现、调试、部署、交付动作回流本专题 |
| 强时效页 | [[../30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代|SaaS支付方案]]、[[../30-Launch Safety/内容平台官方API与自动发布限制|内容平台官方API与自动发布限制]] | 已有官方资料和刷新日期 | 到 `refresh_after` 前后必须核验，不把旧结论当最新事实 |
| Prompt Outputs | [[Outputs/SOP与模板/Vibe Coding安全审计Prompt中英对照|安全审计 prompt]]、[[Outputs/SOP与模板/Cinematic Landing Page Builder Prompt中英对照|Landing Page prompt]]、[[Outputs/SOP与模板/什么是VibeCoding知识召回prompt卡片|什么是 Vibe Coding 卡片]]、[[Outputs/SOP与模板/后端选择知识召回prompt卡片|后端选择卡片]] | 从 Wiki 生成的交付产物，不承担 Wiki 主干结构 | 后续高价值 prompt 继续进 `Outputs/SOP与模板/`，不恢复顶层 Prompts，也不在 Wiki 下建 Prompts |
| 课程 Outputs | [[Outputs/课程与训练营/Codex新手VibeCoding课程|Codex新手VibeCoding课程]]、[[Outputs/课程与训练营/Vibe Coding全栈SaaS实战课讲义|Vibe Coding全栈SaaS实战课讲义]] | 课程编排、练习和评分标准属于交付层 | 后续课程材料先回流到 Topic 主干，再更新课程 Output |
| 视觉产物 | [[Outputs/图文卡片/vibe-coding-roadmap.excalidraw|路线图 Excalidraw]]、[[Outputs/图文卡片/vibe-coding-roadmap-clickable.excalidraw|可点击路线图]] | 可用，旧路径链接已修复 | 后续重新生成图时复查链接 |

## 主干拓扑

```text
基础理解
  -> Codex / AI 编程新手工作流
  -> 从静态站到 SaaS 的开发闭环
  -> 安全 / 调试 / 部署 / 测试
  -> API wrapper / 内容自动化 / AI 生成类 SaaS 案例
  -> 商业化 / 中文市场获客 / 输出课程与 SOP
```

维护时要避免两个方向的腐烂：

- 只往后堆案例，前面的基础理解、路线图和检查清单没有回收新判断。
- 只更新 Wiki，忘记旧 Outputs 已经受到影响。

## 当前成熟区

这些内容已经可以继续生成或维护正式 Output：

- 新手从 0 做 Web App：已有 Wiki 工作流、课程 Output、教程和检查清单。
- 全栈 SaaS 实战课：已有开发闭环、上线检查清单和课程讲义；课程编排在 Outputs 维护。
- 安全审计：已有安全清单和发号施令 prompt Output。
- Landing Page：提示词结构已沉淀进课程/工作流，正式 prompt 在 Outputs。
- API 包装型 SaaS：已有机会判断、三个案例和案例集 Output。
- 后端基础概念：已恢复为 Wiki 知识整理页，并有知识召回 prompt Output，不再补通用百科。

## 当前脆弱区

这些内容不能靠 AI 通用回答补，需要真实材料或定期刷新：

- AI 编程工具体验：Claude Code、Codex、Cursor、Windsurf、v0、Lovable 等工具的真实差异依赖版本、界面、模型状态和上手手感。
- 中文市场获客：已有框架，但缺真实成交、报价、交付边界、社群/短视频/私域复盘。
- 测试与浏览器验证：已有调试框架，但 Playwright、失败测试、截图/console/network 联合验证还弱。
- Codex 一小时项目闭环：已补 Browser Use QA、weekly automation 和 dashboard 项目，但仍缺更多非 YouTube 数据源案例。
- 部署与域名：Vercel / Netlify 有旁证，Cloudflare、自定义域名、环境变量、preview deploy、回滚和日志还弱。
- 内置 AI 能力与 API 成本：已有 Beauty Mirror / OpenRouter 图像 MVP 旁证，但仍需要官方资料、真实账单、限流、队列、缓存、失败重试和账单保护案例。
- 多端扩展：Electron、Tauri、Swift/iOS、PWA 仍然是概念级线索，不足以生成稳定教程。

## 维护队列

| 优先级 | 事项                                           | 类型          | 下一步                                                   | 是否需要问用户             |
| --- | -------------------------------------------- | ----------- | ----------------------------------------------------- | ------------------- |
| P0  | 到期刷新支付和平台 API 页                              | 强时效维护       | 到 `2026-06-28` 前后核验 Stripe、微信支付、支付宝、内容平台 API 和自动发布规则  | 不需要，除非涉及用户具体收款地区和业务 |
| P1  | 建 AI 编程工具真实体验台账                              | 证据台账        | 只记录真实上手、版本、场景、失败点和适用边界，不用知识召回 prompt 代替体验判断                  | 有用户实测材料时再问          |
| P1  | 补测试与浏览器验证工作流                                 | SOP / 工作流   | 吸收 Playwright、失败测试、console/network/screenshot 联合验证案例  | 不需要                 |
| P1  | 补数据 / Dashboard 型项目案例                            | 案例 / 工作流   | 在 YouTube 评论案例之外，继续吸收客户反馈、线索、客服、内容选题等数据看板案例 | 不需要                 |
| P1  | 补部署与域名材料                                     | 强时效 + UI 复盘 | 收集 Cloudflare / Vercel / Netlify 的真实部署界面、环境变量、回滚和日志案例 | 需要用户提供账号内截图时再问      |
| P1  | 补中文市场获客真实案例                                  | 案例 / 复盘     | 收集成交路径、报价包、失败话术、私域/社群/短视频复盘                           | 需要用户提供或确认真实业务材料     |
| P2  | 拆内置 AI 能力与 API 成本主干                          | 主题页         | 模型选择、API key、成本估算、限流、队列、缓存、账单保护                       | 不需要，若查最新价格需联网       |
| P2  | 拆多端扩展主干                                      | 主题页         | Web 转桌面 / iOS / PWA 的真实案例、工程边界和维护成本                   | 不需要                 |
| P2  | 复盘知识召回 prompt 模板                             | 模板维护        | 目前已有 2 张卡片，累计 3-5 张后回看模板是否需要修改                        | 不需要                 |

## 已完成维护记录

| 日期 | 事项 | 结果 |
| --- | --- | --- |
| 2026-05-28 | 修复可点击 Vibe Coding 路线图里的旧 `AI编程与WebCoding` 链接 | 已替换为当前 `Wiki/Vibe Coding/` 下的路线图、Codex 新手工作流、后端与数据库选择、AI 编程边做边学工作流 |
| 2026-05-28 | Prompt 迁出 Wiki | 将编译后的 prompt 定位为 Outputs 产物，`60-Prompts` 不再作为 Wiki 目录；后续 prompt 进入 `Outputs/SOP与模板/` |
| 2026-05-28 | Vibe Coding 目录重构 | 建立 `00-Overview`、`10-Getting Started`、`20-SaaS Build`、`30-Launch Safety`、`40-Business`、`50-SaaS产品模式`、`90-Maintenance`；删除临时导航页；将获客三法降级为 reference |
| 2026-05-28 | Landing Page 同粒度页面合并 | 将 `高质量LandingPage提示词结构` 的价值说明、修改建议、风险和验收并入 `Cinematic Landing Page Builder Prompt中英对照`，删除重复结构页 |
| 2026-05-28 | 获客同粒度页面合并 | 将 `Vibe Coding获客三法` 的海外 outbound / inbound / affiliate 框架并入 `中文市场Vibe Coding获客路径`，删除重复获客页 |
| 2026-05-28 | 商业化与获客边界收窄 | `Vibe Coding商业化与定价包装` 只维护包装、定价、交付和售后边界；获客动作细节统一进入 `中文市场Vibe Coding获客路径` |
| 2026-05-29 | Vibe Coding 主题归位 | 将 SaaS 开发闭环、内容自动化分发、线索挖掘、AI 缩略图案例收回 `Wiki/Vibe Coding/`；课程大纲和讲义转入 `Outputs/课程与训练营/`，Wiki 不再维护课程页 |
| 2026-05-29 | Wiki 扁平化为主题根目录 | `Wiki/` 下一层直接放主题名，旧 `Topics / Workflows / Cases / Tools / Courses` 职责迁移到主题页和 Outputs |
| 2026-05-29 | 当前 Wiki 低风险整理 | 统一 Vibe Coding、AI营销自动化、AI使用方法页面的 `area` 元数据；补齐 `60-Agent Skills` 入口；把 Wiki 内短 prompt 章节改名为操作指令骨架，避免和正式 Prompt Output 混淆 |
| 2026-05-29 | 未编译材料批量吸收 | 将 Codex 一小时课、AI Offer、Perplexity Skills、Shopify Flow、OpenClaw、Karpathy 余量、小说改短剧、开源生态和两个 PDF 分别融合进 Vibe Coding、AI产品工程、AI一人公司、AI视频制作和 AI行业判断 |
| 2026-05-29 | David Ondrej Codex 长课编译 | 将 Codex CLI 零基础起步、AGENTS/README 分工、截图输入、web search、Beauty Mirror AI 图像 MVP、OpenRouter 调试、Git 提交和 Vercel 部署合并进现有 Vibe Coding 主干 |

## Output 影响队列

| Output | 当前状态 | 维护判断 |
| --- | --- | --- |
| [[Outputs/教程/Codex新手从0做WebApp|Codex新手从0做WebApp]] | 可用 | 后续补真实新手失败案例后再更新 |
| [[Outputs/SOP与模板/Codex做WebApp检查清单|Codex做WebApp检查清单]] | 可用 | 测试/浏览器验证补强后应扩展 |
| [[Outputs/课程与训练营/Vibe Coding全栈SaaS实战课讲义|Vibe Coding全栈SaaS实战课讲义]] | 可用 | 中文市场获客和工具体验补证后可更新课程讨论题 |
| [[Outputs/SOP与模板/Vibe Coding SaaS上线检查清单|Vibe Coding SaaS上线检查清单]] | 可用 | 强时效页刷新后同步检查支付、平台 API 和安全项 |
| [[Outputs/案例拆解/API包装型SaaS案例集|API包装型SaaS案例集]] | 可用 | 补真实复刻案例后升级 |
| [[Outputs/工具比较/AI新手做WebApp后端怎么选|AI新手做WebApp后端怎么选]] | 已 superseded | 保留旧版，不再作为主要入口 |

## 下次维护检查清单

- 新材料是否改变了路线图节点状态？
- 是否应该更新专题 README 的主干和脆弱区？
- 是否影响已有 Output 的结论、检查项或读者定位？
- 是否属于 AI 完全熟悉的稳定知识，适合生成知识召回 prompt Output？
- 是否依赖真实体验、UI、价格、政策或平台能力，必须沉淀证据？
- 是否有旧页面应降级为 reference、合并、改名或移动？
- 是否有需要用户决策的业务定位、课程读者或输出形态问题？
