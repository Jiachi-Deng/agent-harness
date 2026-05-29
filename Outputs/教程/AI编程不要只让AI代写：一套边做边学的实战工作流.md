---
type: output
output_type: tutorial
status: review-ready
target_reader: 普通 AI 编程用户 / 独立开发者
use_case: 在使用 Codex、Claude Code、Cursor 等工具时，同时完成交付和理解积累
version_date: 2026-05-28
updated: 2026-05-28
upstream_wiki:
  - "[[Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流|AI编程边做边学工作流]]"
  - "[[Wiki/AI使用方法/不要外包你的学习|不要外包你的学习]]"
references:
  - "[[Clippings/Don't Outsource the Learning|Don't Outsource the Learning]]"
  - "[[Clippings/Designing, Refining, and Maintaining Agent Skills at Perplexity|Designing, Refining, and Maintaining Agent Skills at Perplexity]]"
---

# AI 编程不要只让 AI 代写：一套边做边学的实战工作流

AI 可以帮你写代码，但你不能把理解也外包出去。

现在的 AI 编程工具默认很擅长一件事：把任务关掉。你贴需求、贴报错，AI 给补丁，测试通过，你合并。短期看效率很高；长期看，如果你每次都跳过理解，代码变了，你的判断力没有变。

这篇不是劝你少用 AI，而是给你一套“交付 + 学习”的双目标工作流。

维护备注：本输出对齐 [[Wiki/AI使用方法/不要外包你的学习|不要外包你的学习]] 主页面。它是一条跨工具原则，不承载具体工具体验；具体工具、项目和 Vibe Coding 课程内容继续回流到对应 Wiki。

## 适合谁

适合正在用 Claude Code、Codex、Cursor、Windsurf 做项目的人，尤其是普通 AI 编程用户、独立开发者、刚开始做 WebCoding 的产品 / 运营。

不适合一次性脚本、临时 glue code、以后不会维护的小任务。那种任务可以直接让 AI 代写，没必要强行学习。

## 5 步工作流

### 1. 问 AI 前，先写自己的判断

不要一上来就把报错丢给 AI。先写 2-3 句：

```text
我认为问题可能出在：
我想先验证：
我不确定的是：
```

这一步的价值是防止 AI 的第一版解释直接框住你。你要用 AI 验证自己的判断，而不是让它替你拥有判断。

### 2. 先要解释，再要代码

陌生领域里，第一句不要说“帮我修”。先让 AI 解释：

```text
请先不要写代码。
解释这个问题可能的原因、可选修法、每种修法的代价，以及最小可验证修改。
```

你看懂后，再让它改。

### 3. 像 review PR 一样 review AI

AI 写完后，不要只看“能不能跑”。至少问：

- 它改了哪些文件？
- 有没有扩大修改范围？
- 有没有绕开根因？
- 有没有引入安全、性能、维护成本问题？
- 如果这是一个初级工程师的 PR，我会直接合并吗？

测试通过只是底线，不是理解完成。

### 4. 让 AI 反过来教你

任务完成后追加一轮：

```text
请复盘你刚才做的修改：
1. 关键改动是什么？
2. 依赖了哪些概念？
3. 如果我下次自己做，步骤是什么？
4. 这次有哪些坑应该记下来？
```

这一轮通常只花一分钟，但决定你这次 session 是“关掉任务”，还是“涨一点能力”。

### 5. 建一个 gotcha 列表

每次 AI 犯错，或者你差点误合并，都记一条：

```text
场景：
错误倾向：
检查方式：
下次提醒：
```

不要写成长篇文档。gotcha 的价值在于短、准、下次能用。

## 完整 prompt 模板

```text
我想用 AI 完成这个编程任务，但不想把理解外包出去。

任务 / 报错：
[贴这里]

我自己的初步判断：
[写 2-3 句]

请先不要写代码。先帮我：
1. 判断我的理解哪里对、哪里可能错。
2. 列出 2-3 个可能原因。
3. 说明应该先验证什么。
4. 给出最小修改方案、风险和验证方式。

等我确认后，再进入代码修改。
```

## 一个真实使用示例

你在做 Next.js 页面，发现登录后偶尔跳回首页。

代写模式是：

```text
这个 bug 怎么修？
```

边做边学模式是：

```text
我怀疑是 auth state 初始化和 redirect 时机冲突。
请先不要写代码。帮我检查这个判断是否合理，
列出可能原因，告诉我应该先看 middleware、client state 还是 session refresh。
最后给一个最小验证步骤。
```

第二种慢一点，但你会知道问题为什么发生。下次遇到类似 auth / redirect / hydration 问题，你不再只是重新贴报错。

## 常见误区

- 误区 1：只要 AI 修好了，就算我会了。
- 误区 2：测试通过就不用 review diff。
- 误区 3：AI 写得快，所以 scope 可以一直加。
- 误区 4：学习模式只适合学生，不适合生产。
- 误区 5：gotcha 太小，不值得记录。

## 最后检查

每次 AI 编程 session 结束，只问两个问题：

```text
我交付了什么？
我学会了什么？
```

如果连续很多次只有第一个答案，没有第二个答案，你不是在提效，而是在借债。

## 参考来源

- [[Clippings/Don't Outsource the Learning|Don't Outsource the Learning]]：Addy Osmani 关于 AI 编程中 cognitive debt、shipping vs learning 的文章。
- [[Clippings/Designing, Refining, and Maintaining Agent Skills at Perplexity|Designing, Refining, and Maintaining Agent Skills at Perplexity]]：Perplexity 关于 gotchas、负面样例和可复用经验沉淀的文章。
