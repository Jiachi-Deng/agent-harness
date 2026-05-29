---
type: output
output_type: sop
status: review-ready
target_reader: Codex / Claude Code 新手、AI 编程课程学员
use_case: 检查新手第一个 Web App 是否跑通本地、保存版本、接后端、部署和调试
version_date: 2026-05-28
updated: 2026-05-28
upstream_wiki:
  - "[[Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流|Codex新手Vibe Coding工作流]]"
references:
  - "[[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]"
---

# Codex 做 WebApp 检查清单

维护备注：这份清单只覆盖新手第一条 Web App 链路。只要项目进入真实 SaaS 阶段，尤其出现用户数据、支付、上传、第三方 API、自动发布或客户交付，就改用 [[Vibe Coding SaaS上线检查清单|Vibe Coding SaaS 上线检查清单]]。

## 开工前

- [ ] 新建独立项目文件夹。
- [ ] 确认 Codex 当前工作目录就是这个项目。
- [ ] 写清 app 给谁用、解决什么问题。
- [ ] 让 Codex 创建 `my-idea.md` 保存产品 brief。
- [ ] 区分第一版必须有和以后再做的功能。

## 第一版本地 app

- [ ] Codex 已创建实际代码文件。
- [ ] 本地 preview 能打开。
- [ ] 手动测试核心交互。
- [ ] 让 Codex 说明运行命令和项目结构。
- [ ] 不满意的 UI 用截图反馈。

## GitHub 保存

- [ ] 创建 private GitHub repo。
- [ ] 让 Codex 上传当前项目。
- [ ] 每轮满意修改后 commit / push。
- [ ] commit 信息能看懂这次改了什么。

## 后端准备

- [ ] 判断是否需要登录。
- [ ] 判断是否需要 database。
- [ ] 判断是否需要 storage。
- [ ] 如果使用 Firebase，确认 Authentication / Firestore / Storage 已开启。
- [ ] 不把真正 secret、OpenAI API key、服务端密钥公开到前端或聊天记录里。
- [ ] 让 Codex 解释数据表 / collection 设计。

## 调试

- [ ] 出错时复制 console 日志。
- [ ] 记录复现步骤：我做了什么、期望什么、实际什么。
- [ ] 截图标出 UI 问题区域。
- [ ] 权限错误优先检查 auth、rules、写入路径、domain。
- [ ] 修复后重新手动验证。

## 数据验证

- [ ] 登录后能创建用户。
- [ ] 新增 item 后数据库里真的有记录。
- [ ] 上传截图后 storage 里真的有文件。
- [ ] 刷新页面后数据仍在。
- [ ] 换账号后权限符合预期。
- [ ] 如果是团队 app，能区分 my posts / all users。

## AI 功能

- [ ] 明确 AI 只做什么轻量任务，比如标题、摘要、分类。
- [ ] 说明输出长度和风格。
- [ ] 知道每次 API 调用有成本。
- [ ] API key 使用方式需要复查，不随便暴露。
- [ ] AI 输出要能被用户覆盖或修改。

## 部署

- [ ] 本地核心流程跑通后再部署。
- [ ] 部署到 Vercel 或其它平台。
- [ ] 获得 public URL。
- [ ] Firebase / 后端加入 authorized domain。
- [ ] 外部浏览器重新测试登录、读写、上传。
- [ ] 记录部署地址和环境变量位置。

## 多端扩展

- [ ] Web app 已经稳定。
- [ ] 先让 Codex 写转换计划，不直接实现。
- [ ] 明确 desktop、iOS 是否共享同一后端。
- [ ] Electron app 能登录并同步数据。
- [ ] iOS app 能在 Xcode simulator 里运行。
- [ ] 每端分别测试新增 item、读取 item、登录退出。

## 结束前

- [ ] 让 Codex 总结本轮改了哪些文件。
- [ ] 让 Codex 写下一步建议。
- [ ] commit / push 最终版本。
- [ ] 记录本轮踩到的 bug 和修法。
- [ ] 更新自己的 prompt / gotcha 列表。

## 常用 prompt

```text
请先不要写代码。
基于我的 app 想法，帮我拆出：
1. 第一版必须功能
2. 需要保存的数据
3. 是否需要登录
4. 是否需要数据库和文件存储
5. 本地验证步骤
6. 部署前检查
7. 风险和容易出错的地方
```

```text
我遇到了 bug。

我做了：
[步骤]

我期望：
[期望]

实际发生：
[结果]

console 日志：
[粘贴]

截图：
[如有]

请先判断可能原因，再给最小修复方案。修完后告诉我如何验证。
```

## 参考来源

- [[Clippings/Vibe Coding for Beginners (Full Course 2026)|Vibe Coding for Beginners]]：主来源，提炼其中项目、GitHub、Firebase、调试、Vercel、多端转换的检查点。
