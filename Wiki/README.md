# Wiki

这里是 AI 编译后的主题知识库，不是原文仓库，也不是交付货架。

Wiki 的目标是把 `Clippings/` 和 `Raw/` 里的教程、案例、课程、工具经验和人工判断，按主题整理成长期可演进的知识主干。课程、案例拆解、workflow、SOP、工具比较、PPT、图文卡片等正式产物放在 `Outputs/`。

## 主题入口

| 主题 | 负责什么 | 常用 Output |
| --- | --- | --- |
| [[Vibe Coding/README|Vibe Coding]] | AI 编程、Web App、SaaS 原型、调试、安全、支付、商业化 | 教程、课程、SOP、prompt、案例拆解 |
| [[AI视频制作/README|AI视频制作]] | 视频选题、脚本、分镜、剪辑、动态图形、短剧、讲解图 | SOP、图文卡片、视频流程、课程讲义 |
| [[AI知识库/README|AI知识库]] | 收藏、剪藏、Readwise、Obsidian、个人知识到内容选题 | SOP、模板、内容工作流 |
| [[AI营销自动化/README|AI营销自动化]] | 一人营销团队、素材、排期、商务邮件和日程 | 案例拆解、workflow、运营 SOP |
| [[AI产品工程/README|AI产品工程]] | 生产级 agent 产品、tool calling、skills、多 agent、评估、数据飞轮和观测性 | 架构选型卡、上线检查清单、工程 SOP |
| [[AI一人公司/README|AI一人公司]] | 创始人、独立开发、小团队如何用 AI 验证、MVP、Launch、Scale 和交付服务 | 创业路线图、咨询 SOP、服务报价模板 |
| [[AI行业判断/README|AI行业判断]] | 大 V / 公司 / 研究者对 AI 应用和软件范式的长期判断 | 观点解读、趋势卡片、课程导论 |
| [[AI使用方法/README|AI使用方法]] | 跨工具的学习方法、理解边界、prompt 思维和复盘原则 | 知识召回 prompt、学习 SOP |
| [[知识库维护/README|知识库维护]] | Raw / Clippings 到 Wiki 到 Outputs 的维护规则 | 采编 SOP、维护检查清单 |

## 目录原则

- `Wiki/` 下一层只放主题名，不放 `Topics`、`Tools`、`Cases`、`Workflows`、`Courses` 这类功能目录。
- 新材料先找已有主题吸收；只有现有主题无法承载时，才新建主题。
- 同一粒度讲同一件事的页面要合并；合并时选择、重排和融合，不整篇 append。
- 工具、案例、流程可以作为某个主题里的知识证据和判断材料，但正式工具比较、案例拆解、workflow 交付物放到 `Outputs/`。
- 课程大纲、训练营结构、作业、评分标准和讲义进入 [[Outputs/课程与训练营/README|Outputs/课程与训练营]]，不要在 Wiki 里新建课程页。

## 维护规则

- 每次编译新材料，要检查是否影响主题 README、主干页、旧结论和相关 Outputs。
- AI 已知的稳定通用知识不写百科长文，整理成问题框架、讲解路径和核验点；需要交付时再生成 prompt Output。
- 依赖真实体验、UI、价格、政策、工具能力和用户业务判断的内容，要沉淀证据、复盘、产品模式或强时效页。
- 每次编译或结构调整都要更新相关入口、Output 上游引用和 `log.md`。
