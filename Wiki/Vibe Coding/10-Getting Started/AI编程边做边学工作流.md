---
type: wiki
status: compiled
area: Vibe Coding
tags:
  - AI编程
  - 学习工作流
  - Claude Code
  - Cursor
  - Codex
updated: 2026-05-23
---

# AI编程边做边学工作流

## 解决什么问题

AI 编程工具默认会把目标优化成“尽快关掉任务”：修 bug、生成代码、通过测试、提交 diff。这个目标本身没错，但如果用户每次都直接接受答案，长期会积累理解债：代码变了，自己的 mental model 没有变。

这套工作流的目标是同时追两件事：

- 交付：功能能跑，bug 被修掉，代码能合并。
- 学习：用户理解问题、方案、取舍和下次如何判断。

## 适合谁

适合：

- 用 Claude Code、Codex、Cursor、Windsurf 等工具做项目的人。
- 独立开发者、普通 AI 编程用户、转技术的产品 / 运营。
- 想提升速度，但不想长期变成“只能复制 AI 代码”的人。

不适合：

- 一次性脚本、低价值 glue code、临时数据清洗。
- 用户明确只想快速交付、未来不会维护的任务。

## 五步流程

### 1. 先写自己的假设

在问 AI 前，先写 2-3 句：

- 我认为问题在哪里？
- 可能的原因是什么？
- 我想先验证什么？

这一步防止 AI 的第一句话直接框住你的思路。

### 2. 先解释，后写代码

在陌生领域，不要第一句就说“帮我修”。先让 AI 解释：

- 这段代码现在如何工作。
- 可能有哪些修法。
- 每种修法的代价。
- 最小可验证修改是什么。

### 3. 像 review 初级工程师的 PR 一样 review AI 输出

不要因为测试过了就直接合并。至少检查：

- 它改了哪些文件？
- 有没有扩大范围？
- 有没有绕开根因？
- 有没有引入安全、性能、维护成本问题？

### 4. 让 AI 教你它刚做了什么

代码写完后追加问题：

- 这次修复依赖了哪些概念？
- 如果我要自己重写，步骤是什么？
- 下次遇到类似问题，应该先看哪里？

### 5. 把 gotcha 沉淀下来

如果 AI 犯错，或者你差点误合并，把它记录成一条 gotcha：

- 触发场景。
- 错误做法。
- 正确检查。
- 下次 prompt 里要提醒什么。

长期看，这个 gotcha 列表比一次性 prompt 更值钱。

## 常见失败模式

- 直接粘贴报错，让 AI 给补丁，自己不读。
- 不写假设，完全接受 AI 对问题的 framing。
- 只看测试，不看 diff。
- 让 AI 一次改太多文件。
- 没有复盘，下一次遇到类似问题仍然从零问。

## 行业判断补充

Karpathy 在 [[Wiki/AI行业判断/从VibeCoding到AgenticEngineering|从Vibe Coding到Agentic Engineering]] 里给了一个更高层的框架：`vibe coding` 提高所有人的软件创造下限，但 `agentic engineering` 要求人继续负责质量线、spec、taste、judgment 和 understanding。

这意味着边做边学不是保守派姿态，而是 AI 编程进入严肃应用后的必要能力。AI 可以处理大量 API 细节和代码填充，但人必须知道系统设计是否合理、权限是否安全、验证是否充分。

## 可生成 Outputs

- 教程：AI 编程不要只让 AI 代写。
- SOP：AI 改代码前后检查清单。
- 模板：边做边学 prompt 模板。
- 课程练习：同一个 bug 分别用“代写模式”和“学习模式”处理，对比结果。

## 来源

- [[Clippings/Don't Outsource the Learning|Don't Outsource the Learning]]：主来源，强调 AI 工具默认优化交付，而不是学习。
- [[Clippings/Designing, Refining, and Maintaining Agent Skills at Perplexity|Designing, Refining, and Maintaining Agent Skills at Perplexity]]：旁证，提供 gotchas flywheel 和负面样例沉淀思路。
- [[Clippings/Andrej Karpathy From Vibe Coding to Agentic Engineering|Andrej Karpathy: From Vibe Coding to Agentic Engineering]]：行业判断旁证，强调 vibe coding 与 agentic engineering 的区别，以及不能外包 understanding。
