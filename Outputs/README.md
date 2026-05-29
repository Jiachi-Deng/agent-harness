# Outputs

正式产物层。所有正式 Outputs 必须从 Wiki 生成，不直接从 `Clippings/` 或 `Raw/` 生成。

这里不是资料库，而是交付货架：教程、案例、检查清单、prompt、课程讲义、图文卡片都应该让用户能直接拿去用。

## 按场景进入

| 场景 | 主入口 | 配套产物 |
| --- | --- | --- |
| AI 编程新手做第一个 Web App | [[教程/Codex新手从0做WebApp|Codex新手从0做WebApp]] | [[SOP与模板/Codex做WebApp检查清单|Codex做WebApp检查清单]]、[[教程/AI编程不要只让AI代写：一套边做边学的实战工作流|AI编程边做边学工作流]] |
| 先理解 Vibe Coding 和后端选择 | [[SOP与模板/什么是VibeCoding知识召回prompt卡片|什么是 Vibe Coding 知识召回 prompt 卡片]] | [[SOP与模板/后端选择知识召回prompt卡片|后端选择知识召回 prompt 卡片]] |
| 从 Vibe Coding 项目走到 SaaS 上线 | [[课程与训练营/Vibe Coding全栈SaaS实战课讲义|Vibe Coding全栈SaaS实战课讲义]] | [[SOP与模板/Vibe Coding SaaS上线检查清单|Vibe Coding SaaS上线检查清单]]、[[SOP与模板/Vibe Coding安全审计Prompt中英对照|Vibe Coding安全审计 Prompt]] |
| 生成 Landing Page 或安全审计 prompt | [[SOP与模板/Cinematic Landing Page Builder Prompt中英对照|Landing Page 发号施令 prompt]] | [[SOP与模板/Vibe Coding安全审计Prompt中英对照|安全审计发号施令 prompt]] |
| 找 AI 工具 / API wrapper SaaS 方向 | [[案例拆解/API包装型SaaS案例集|API包装型SaaS案例集]] | [[工具比较/AI新手做WebApp后端怎么选|AI新手做WebApp后端怎么选]] 旧版参考 |
| 搭 AI 一人营销团队 | [[案例拆解/Codex搭建AI一人营销团队|Codex搭建AI一人营销团队]] | 后续可从 Wiki 生成 SOP、模板和课程练习 |
| 做 AI 视频、短剧、讲解图 | [[SOP与模板/AI视频短剧制作检查清单|AI视频短剧制作检查清单]] | [[图文卡片/vibe-coding-roadmap.excalidraw|Vibe Coding 路线图图卡]] |
| 维护资料采编和 prompt 模板 | [[SOP与模板/高质量教程采编闭环模板|高质量教程采编闭环模板]] | [[SOP与模板/知识召回prompt卡片模板|知识召回 prompt 卡片模板]] |

## 状态说明

| 状态 | 含义 |
| --- | --- |
| `review-ready` | 已能给用户使用，但后续可根据新证据继续更新 |
| `compiled` | 已整理完成，可作为稳定模板或 prompt 使用 |
| `living` | 模板会随实践迭代，不应视为一次定稿 |
| `superseded` | 已被新版 Output 替代，只保留为旧版参考 |

当前明确 `superseded` 的旧产物：

- [[工具比较/AI新手做WebApp后端怎么选|AI新手做WebApp后端怎么选]]：已被 [[SOP与模板/后端选择知识召回prompt卡片|后端选择知识召回 prompt 卡片]] 替代。

## 按产物形态浏览

- [[教程/README|教程]]：保姆级教程、步骤指南、实操文章。
- [[案例拆解/README|案例拆解]]：真实应用案例、大 V 方法拆解、公司 / 产品做法复盘。
- [[工具比较/README|工具比较]]：工具横评、场景选型、价格 / 能力 / 限制比较。
- [[SOP与模板/README|SOP与模板]]：可复制流程、prompt、检查清单、工作流模板。
- [[课程与训练营/README|课程与训练营]]：课节、作业、练习、训练营路线。
- [[图文卡片/README|图文卡片]]：知识卡、流程图、对比图、社媒图文。
- [[PPT与讲义/README|PPT与讲义]]：PPT、演讲稿、课程讲义、汇报材料。

## Output 必填信息

每个 Output 应写清：

- 上游 Wiki 页面。
- 参考的 Clippings / Raw。
- 目标读者。
- 使用场景。
- 版本日期。

## 维护规则

- Output 不直接从 Raw / Clippings 生成；先进入 Wiki，再从 Wiki 生成。
- 当 Wiki 页面被合并、改名、升为主干或降级为 reference，相关 Output 必须反向检查。
- 旧 Output 如果被知识召回 prompt、SOP 或新版讲义替代，保留但标记 `superseded`，不要混在主入口里误导读者。
- Output 只同步会影响读者使用的变化；普通证据补充优先留在 Wiki。
