---
type: output
output_type: sop
status: review-ready
target_reader: AI 编程新手、独立开发者、小团队技术负责人、课程学员
use_case: Vibe Coding 项目从本地原型进入公网演示、客户试用或收费前的逐项检查
version_date: 2026-05-28
updated: 2026-05-28
upstream_wiki:
  - "[[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]"
  - "[[Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单|Vibe Coding安全审计清单]]"
  - "[[Wiki/Vibe Coding/30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代|SaaS支付方案：Stripe积分订阅Webhook与国内替代]]"
  - "[[Wiki/Vibe Coding/30-Launch Safety/内容平台官方API与自动发布限制|内容平台官方API与自动发布限制]]"
  - "[[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架|Vibe Coding调试与迭代框架]]"
  - "[[Wiki/Vibe Coding/50-SaaS产品模式/AI缩略图生成SaaS产品模式|AI缩略图生成SaaS案例]]"
  - "[[Wiki/Vibe Coding/50-SaaS产品模式/内容自动化分发SaaS产品模式|内容自动化分发SaaS工作流]]"
references:
  - "[[Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs)|VIBE CODING FULL COURSE transcript]]"
  - "[[Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review|NotebookLM 审片记录]]"
  - "[[Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/prompts/Security For Vibe-Coded Apps (+ Prompt)|安全审计 prompt]]"
---

# Vibe Coding SaaS 上线检查清单

这份清单用于 AI 编程项目上线前最后一轮验收。适用范围是有登录、数据库、文件上传、第三方 API、积分、订阅、支付或内容发布能力的 SaaS 原型。

维护备注：支付、OAuth、自动发布、平台 API、Webhook 和国内替代方案都属于强时效条目。正式上线前必须回查对应 Wiki、官方文档和当前平台规则；本清单只作为验收框架，不替代最新政策核对。

## 0. 上线前判断

- [ ] 这不是纯静态展示页，而是涉及用户、数据、接口或付费的 SaaS。
- [ ] 已经有一条真实用户路径能从注册走到核心结果。
- [ ] 本地版本已稳定，不再处于“刚生成完还没手测”的状态。
- [ ] 当前版本已保存到 Git，能回滚。
- [ ] 已区分 demo、测试环境和正式环境。

## 1. 产品路径

- [ ] Landing Page 能讲清目标用户、痛点、结果和 CTA。
- [ ] Signup/Login 路径可用。
- [ ] 新用户登录后知道第一步要做什么。
- [ ] Dashboard 不只是空页面，至少能展示核心任务或历史记录。
- [ ] Settings 中的关键配置刷新后不会丢失。
- [ ] 退出登录后不能继续访问私密页面。
- [ ] 移动端核心路径可读、可点、可提交。

## 2. 数据库和权限

- [ ] 用户数据表已开启 RLS 或等价行级权限。
- [ ] 普通用户只能读写自己的数据。
- [ ] 管理员权限和普通用户权限分离。
- [ ] 数据写入时绑定真实 `user_id`，不是前端随便传。
- [ ] 换账号测试后，看不到上一个账号的数据。
- [ ] 历史记录、订单、生成结果、上传文件都有归属用户。
- [ ] 删除、更新、导出操作都检查权限。

## 3. 密钥和环境变量

- [ ] 代码中搜不到真实 secret key、service role key、支付 secret、AI API key。
- [ ] 前端只暴露允许公开的 key，例如配置过权限的 anon key。
- [ ] `.env` 没有提交到公开仓库。
- [ ] 线上平台单独配置生产环境变量。
- [ ] 本地、预览、正式环境的 callback URL 和 webhook URL 不混用。
- [ ] 高成本 API key 只在服务端调用。

## 4. 服务端验证

- [ ] 表单提交在服务端重新验证字段、长度、类型和权限。
- [ ] 余额、积分、套餐状态由服务端检查，不能只靠前端按钮禁用。
- [ ] 数据库写入前验证当前用户身份。
- [ ] API route 对未登录用户返回拒绝。
- [ ] 重要业务动作有错误处理和明确提示。
- [ ] 用户输入不会直接拼接进危险查询或命令。

## 5. 支付、积分和订阅

- [ ] 支付成功不能只信前端跳转结果。
- [ ] Webhook 验证签名。
- [ ] Webhook 能把付款事件映射到正确用户。
- [ ] 积分增加、扣减、退款或失败重试都有记录。
- [ ] 0 积分或无订阅用户会被拦截到充值/升级页面。
- [ ] 重复 webhook 不会重复加积分或重复开通权益。
- [ ] 定价页、结账页、后台权益显示一致。

## 6. 文件上传和存储

- [ ] 服务端校验文件类型、大小和数量。
- [ ] 不只依赖文件扩展名判断类型。
- [ ] 上传文件归属当前用户。
- [ ] 下载链接不应绕过鉴权。
- [ ] 用户不能访问、替换或删除别人的文件。
- [ ] 大文件、失败上传和重复上传有清晰提示。

## 7. 第三方 API 和自动化

- [ ] 第三方 API 调用在服务端执行。
- [ ] 高成本接口有登录检查、余额检查和 rate limit。
- [ ] 处理超时、限流、失败和重试。
- [ ] API 返回结果先清洗再入库。
- [ ] 平台 OAuth redirect URI 使用线上真实域名。
- [ ] 自动发布、群发、抓取类功能已核对平台规则。
- [ ] 如果官方 API 不稳定或受限，产品文案不承诺全自动。

## 8. 部署和线上环境

- [ ] 构建命令正确。
- [ ] 线上环境变量完整。
- [ ] 线上数据库、Auth、Storage 指向正确项目。
- [ ] 支付 webhook 指向线上地址。
- [ ] OAuth callback 域名加入平台白名单。
- [ ] 外部浏览器和无痕模式能跑完整流程。
- [ ] 404、重定向、私密路由刷新都正常。
- [ ] 线上日志可查看。

## 9. 调试和回滚

- [ ] 当前版本有清晰 commit。
- [ ] 记录已知 bug 和暂不支持功能。
- [ ] 有最小复现步骤模板。
- [ ] 每次修复只改一个明确问题。
- [ ] 修复后重新测试登录、数据、权限、支付和上传。
- [ ] 有回滚方案，不依赖“让 AI 再修一下”。

## 10. 交付包装

- [ ] 有在线演示地址。
- [ ] 有普通用户使用说明。
- [ ] 有部署和环境变量说明。
- [ ] 有功能清单和版本日期。
- [ ] 有安全检查结果摘要。
- [ ] 有售后边界：bug 修复、维护期、新功能报价。
- [ ] 如果面向客户演示，准备 1-3 分钟 demo 脚本。

## 上线前安全审计 Prompt

```text
请对当前 SaaS 项目做上线前安全审计。

重点检查：
1. 密钥、API key、支付 secret、service role key 是否暴露；
2. 用户数据表是否开启 RLS 或等价权限，policy 是否正确；
3. 表单、API route、数据库写入、积分扣减是否有服务端验证；
4. 私密页面和 API 是否有认证中间件保护；
5. 文件上传是否校验类型、大小和用户权限；
6. 高成本 API 是否有限流、余额检查和错误处理；
7. 支付 webhook 是否验证签名，是否能防止重复入账；
8. 依赖包是否真实、官方、维护中，是否有明显漏洞。

先输出问题清单，不要直接大范围改代码。
每个问题都要给严重程度、涉及文件、风险说明、修复建议和验证方式。
```

## Bug 反馈模板

```text
我在上线前测试中发现问题。

环境：本地 / 线上
账号：
操作步骤：
期望结果：
实际结果：
console 日志：
server 日志：
最近改动：

请先判断最可能原因和涉及文件。
只修复这个问题，不要顺便重构。
修复后告诉我需要重新测试哪些路径。
```

## 参考来源

- 上游 Wiki：`Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单.md`
- 上游 Wiki：`Wiki/Vibe Coding/30-Launch Safety/SaaS支付方案：Stripe积分订阅Webhook与国内替代.md`
- 上游 Wiki：`Wiki/Vibe Coding/30-Launch Safety/内容平台官方API与自动发布限制.md`
- 上游 Wiki：`Wiki/Vibe Coding/20-SaaS Build/Vibe Coding调试与迭代框架.md`
- 上游 Wiki：`Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环.md`
- 原始材料：`Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md`
- 配套 prompt：`Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/prompts/Security For Vibe-Coded Apps (+ Prompt).md`
