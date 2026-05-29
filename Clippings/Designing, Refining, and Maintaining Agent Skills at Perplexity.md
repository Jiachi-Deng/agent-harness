---
title: Designing, Refining, and Maintaining Agent Skills at Perplexity
source: https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity
author:
published: 2026-04-30
created: 2026-05-22
description: Perplexity Research advances our mission to transform how we navigate the internet and the wider world through frontier research in search, reasoning, agents, and systems.
tags:
  - clippings
compile_status: compiled
compiled_to:
  - "Wiki/Vibe Coding/10-Getting Started/AI编程边做边学工作流.md"
  - "Wiki/AI使用方法/不要外包你的学习.md"
  - "Wiki/Vibe Coding/60-Agent Skills/Agent Skills仓库索引.md"
  - "Wiki/AI产品工程/生产级Agent产品工程.md"
  - "Outputs/教程/AI编程不要只让AI代写：一套边做边学的实战工作流.md"
remaining_value: medium
---
Perplexity’s frontier agent products rest on a foundation of know-how and domain expertise packaged in modular

[

Agent Skills

](https://agentskills.io/home)

. We maintain a carefully curated library of Skills across our technical environments. These Skills include many of the general-purpose utilities powering

[

Perplexity Computer

](https://www.perplexity.ai/products/computer)

; vertical-specific capabilities in areas such as finance, law, and health; and a very long tail of modules for addressing user needs. Some Skills are infrequently invoked but critical

*

when

*

invoked. To ensure a consistently excellent user experience, Perplexity’s Agents team prioritizes Skill quality just as much as code quality.

Perplexity 的前沿代理产品建立在模块化代理技能中的专业知识和领域专业知识的基础上。我们在整个技术环境中维护着一个精心策划的技能库。这些技能包括许多为 Perplexity Computer 提供支持的通用实用程序；金融、法律和卫生等领域的垂直特定能力；以及用于满足用户需求的很长的模块尾部。有些技能很少被调用，但在调用时却很关键。为了确保始终如一的卓越用户体验，Perplexity 的代理团队将技能质量与代码质量一样放在首位。

The intuitions and best practices required to develop a high-quality Skill differ significantly from those required to build traditional software. The Agents team reviews many pull requests from excellent engineers who develop Skills in the course of their work. The result is almost always numerous comments and suggestions for revision. This is because many useful patterns for writing code become antipatterns in Skill creation.

开发高质量技能所需的直觉和最佳实践与构建传统软件所需的直觉和最佳实践有很大不同。代理团队审查了来自优秀工程师的许多拉取请求，这些工程师在工作过程中开发了技能。结果几乎总是有大量的意见和修改建议。这是因为许多有用的代码编写模式在技能创建中变成了反模式。

For example, if you take some of the aphorisms from

[

PEP20 – The Zen of Python

](https://peps.python.org/pep-0020/)

, it quickly becomes clear that writing good Python code is unlike writing good Skills. Of the 20 lines of wisdom, at least half are fully wrong or actively misleading when writing Skills. Here are five of them:

例如，如果您引用 PEP20 – Python 之禅中的一些格言，很快就会发现编写好的 Python 代码与编写好的技能不同。在这 20 条智慧之言中，至少有一半在撰写《技能》时是完全错误的或具有积极误导性。以下是其中五个：

| **Zen of Python**  **  Python之禅  ** | **Zen of Skills**  **  技能禅  ** |
| --- | --- |
| Simple is better than complex  简单胜于复杂 | A Skill is a folder, not a file. Complexity is the feature.  技能是一个文件夹，而不是文件。复杂性是其特点。 |
| Explicit is better than implicit  显式优于隐式 | Activation is implicit pattern matching. Progressive disclosure.  激活是隐式模式匹配。渐进式披露。 |
| Sparse is better than dense  稀疏优于密集 | Context is expensive. Maximum signal per token.  上下文是昂贵的。每个令牌的最大信号。 |
| Special cases aren’t special enough to break the rules  特殊情况还不足以违反规则 | Gotchas ARE the special cases (they're the highest-value content).  陷阱是特殊情况（它们是最高价值的内容）。 |
| If the implementation is easy to explain, it may be a good idea  如果实现很容易解释，这可能是个好主意 | If it's easy to explain, the model already knows it. Delete it.  如果很容易解释，则模型已经知道了。删除它。 |

This guide is the document that engineers across Perplexity use when developing and reviewing Skills. We’re also releasing this guide to the public so that our discoveries and learnings can benefit the broader community. Whether you’re an engineer designing production Skills in your day-to-day work, a Computer user looking to develop your own Skill in an area you know best, or both, this guide is for you.

本指南是 Perplexity 工程师在开发和审查技能时使用的文档。我们还向公众发布了本指南，以便我们的发现和学习能够造福更广泛的社区。无论您是在日常工作中设计生产技能的工程师，还是希望在您最了解的领域发展自己的技能的计算机用户，或者两者兼而有之，本指南都适合您。

## What is a Skill? 什么是技能？

When you write a Skill, you aren’t writing plain old software (even though Skills are now part of the main logical engines for agent systems). Rather, you're building context for models and their environments. A Skill has different constraints and different design principles. If you write a Skill like you do code, you will fail.

当您编写技能时，您并不是在编写普通的旧软件（尽管技能现在是代理系统主要逻辑引擎的一部分）。相反，您正在为模型及其环境构建上下文。一项技能有不同的约束和不同的设计原则。如果你像编写代码一样编写技能，你就会失败。

A Skill is at least four things, especially in the context of how we build them at Perplexity.

技能至少包含四件事，特别是在我们如何在 Perplexity 中构建它们的背景下。

### A Skill is a Directory技能是一个目录

A Skill is not just a single

`SKILL.md`

file. In many cases, a Skill includes several files. Under the directory named after your Skill, you might have:

技能不仅仅是单个 `SKILL.md` 文件。在许多情况下，一项技能包含多个文件。在以您的技能命名的目录下，您可能有：

- `SKILL.md`
	: frontmatter and instructions
	`SKILL.md` ：前言和说明。
- `scripts/`
	: code the agent runs, not reinvents
	`scripts/` ：代理运行的代码，而不是重新发明。
- `references/`
	: heavy docs, loaded conditionally
	`references/` ：大量文档，有条件加载。
- `assets/`
	: templates, schemas, and data
	`assets/` ：模板、模式和数据。
- `config.json`
	: first-run user setup
	`config.json` ：首次运行用户设置。

This hub-and-spoke pattern allows you to keep Skills very focused and tight, and one can use the folder structure in a very creative way. Sometimes, particularly intricate Skills benefit from multiple levels of hierarchy to help the model navigate better. Suppose a Skill requires knowledge across 300 topics, groupable into 20 subject matter areas. Reliably choosing the right topic among 300 is an unsolved challenge even for today’s best frontier models. It’s a much easier choice problem for a model to hone in on one of 20 areas, than among the 15 topics within that area.

这种中心辐射型模式使您可以使技能保持非常集中和紧密，并且可以以一种非常有创意的方式使用文件夹结构。有时，特别复杂的技能受益于多个层次结构，以帮助模型更好地导航。假设一项技能需要 300 个主题的知识，可分为 20 个主题领域。即使对于当今最好的前沿模型来说，从 300 个主题中可靠地选择正确的主题也是一个尚未解决的挑战。对于模型来说，在 20 个领域中的一个领域进行磨练比在该领域的 15 个主题中进行选择要容易得多。

As one example of how multilevel hierarchy provides value, our team employed three levels of topical nesting within the Skills powering Computer’s U.S. income tax capabilities this past tax season. This hierarchy was absolutely indispensable given the complexity of tax law: in our early tests, presenting the model with a single folder containing all 1,945 sections of the U.S. Internal Revenue Code resulted in worse performance than not loading the Skill at all. Organizing the information into logical subdivisions was indispensable for ensuring high-precision read operations.

作为多级层次结构如何提供价值的一个例子，我们的团队在上个纳税季节的计算机美国所得税功能的技能中采用了三个级别的主题嵌套。考虑到税法的复杂性，这种层次结构是绝对不可或缺的：在我们的早期测试中，向模型提供包含美国国税局所有 1,945 个部分的单个文件夹会导致比根本不加载技能更糟糕的性能。为了确保高精度的读取操作，将信息组织成逻辑细分是必不可少的。

Yet this hierarchy did not come free. Increasing levels of hierarchy require increasing levels of curation across the information architecture to manage the resulting indirection. We devised quick reference guides, custom search utilities, and other tools to support the model in locating information with a minimum of indirection. In this case, doing the hard work of curation ultimately produced a positive end result: a Skill that allowed models to perform tax-related tasks much more capably than using general tools alone.

然而这种等级制度并不是免费的。层次结构级别的增加需要整个信息架构的管理级别不断提高，以管理由此产生的间接关系。我们设计了快速参考指南、自定义搜索实用程序和其他工具来支持模型以最少的间接方式定位信息。在这种情况下，艰苦的管理工作最终产生了积极的最终结果：这种技能使模型能够比单独使用通用工具更有效地执行与税务相关的任务。

![](https://framerusercontent.com/images/StL77jSrvpQypM4nJ5omvZdkHQ.png?width=1600&height=928)

### A Skill is a Format技能是一种格式

A Skill is a format. The core root

`SKILL.md`

file must have both a name and a description. Furthermore, the Skill needs to exactly map to the directory name in which the Skill is located. The name must be all lower-case characters, have no spaces, and can use hyphens. The description is the routing trigger. This is a common failure point: the description is not internal documentation for what the Skill does. It amounts to instructions for the model for when to load the Skill. So, you will frequently see “Load when,” not “This Skill does.” This is important because of the way that most implementations inject the description into the model context.

技能是一种格式。核心根 `SKILL.md` 文件必须同时具有名称和描述。此外，技能需要准确映射到技能所在的目录名称。名称必须全部为小写字符，不含空格，并且可以使用连字符。描述是路由触发器。这是一个常见的失败点：描述不是技能用途的内部文档。它相当于模型何时加载技能的指令。因此，您会经常看到“加载时间”，而不是“此技能执行”。这很重要，因为大多数实现将描述注入模型上下文的方式。

Within the frontmatter, there is also “

`depends:`

”, which allows you to create hierarchical Skill dependencies, and “

`metadata:`

”, which is used for reviews and evaluations. Different agent systems can even define their own frontmatter fields, to be used in a manner specific to those systems. As an alternative, Skill-specific metadata can be packaged in an auxiliary JSON or YAML configuration file. This is desirable when building agent systems that need to facilitate different types of runtime behavior per Skill without polluting the model’s context with minutiae. Finally, similar behavior is obtainable through stripping Skill frontmatter on read. Computer employs this methodology, which allows configuration to be preserved in the root

`SKILL.md`

file. Careful attention to detail is required in the parsing logic, and one might wish to implement conditional stripping if there are certain fields that are useful to have within the model context.

在 frontmatter 中，还有“ `depends:`”，它允许您创建分层技能依赖关系，以及“ `metadata:`”，用于评论和评估。不同的代理系统甚至可以定义自己的 frontmatter 字段，以特定于这些系统的方式使用。作为替代方案，特定于技能的元数据可以打包在辅助 JSON 或 YAML 配置文件中。当构建需要促进每个技能不同类型的运行时行为而不用细节污染模型上下文的代理系统时，这是可取的。最后，通过在读取时剥离 Skill frontmatter 可以获得类似的行为。计算机采用这种方法，允许将配置保留在根 `SKILL.md` 文件中。解析逻辑中需要仔细注意细节，如果模型上下文中存在某些有用的字段，人们可能希望实现条件剥离。

### A Skill is Invocable 技能是可以调用的

A Skill is invocable. The agent loads a Skill at runtime. Importantly, Skills aren’t always bundled into the context. By default, most agent systems unfold Skills progressively upon specific need.

技能是可以调用的。代理在运行时加载技能。重要的是，技能并不总是与环境捆绑在一起。默认情况下，大多数代理系统会根据特定需要逐步展开技能。

There are at least three tiers of context costs in the way that we've implemented Skills in Computer. Here is the process:

我们实施计算机技能的方式至少存在三层上下文成本。这是过程：

1. Computer calls
	计算机拨打 `load_skill(name="...")` 。
	`load_skill(name="...")`
2. Computer copies the Skill directory into the isolated execution sandbox
	计算机将Skill目录复制到隔离执行沙箱中
3. Computer recursively auto-loads dependencies in the “
	`depends:`
	” tag
	计算机递归地自动加载“ `depends:`”标签中的依赖项。
4. Computer then strips the frontmatter and the agent thus only sees the body and the additional files
	然后，计算机剥离 frontmatter 和代理，因此只能看到正文和附加文件

Different agent systems can choose to expose Skill content in different ways. As an example, some systems might choose not to expose the file hierarchy at all, leaving it to the model to discover the hierarchy through filesystem operations. Other systems may choose to give the model a mapping of the entire filetree up to a certain truncation and/or depth limit. To keep context clean, Computer omits full file hierarchies from the invocation context; however, this is overridable on a per-Skill basis.

不同的代理系统可以选择以不同的方式公开技能内容。例如，某些系统可能选择根本不公开文件层次结构，而让模型通过文件系统操作来发现层次结构。其他系统可能会选择为模型提供整个文件树的映射，直至一定的截断和/或深度限制。为了保持上下文干净，计算机从调用上下文中省略了完整的文件层次结构；然而，这对于每项技能都是可以覆盖的。

### A Skill is Progressive 技能是渐进的

Skills are progressive. In Computer, there are three different tiers of context costs, and we incur all three at various stages:

技能是渐进的。在计算机中，存在三个不同级别的上下文成本，并且我们在不同阶段产生所有三个级别：

| **Tier**  **  等级  ** | **What loads**  **  加载什么  ** | **Budget**  **  预算  ** | **When you pay**  **  当你付款时  ** |
| --- | --- | --- | --- |
| Index  索引 | `name: description`  for every non-hidden Skill  `name: description` 对于每个非隐藏技能。 | ~100 tokens per Skill  每个技能约 100 个代币 | Every session, every user, always paid  每个会话、每个用户始终付费 |
| Load  负载 | Full  `SKILL.md`  body  完整的 `SKILL.md` 主体。 | ~5,000 tokens  约 5,000 个代币 | ~5,000 tokens  约 5,000 个代币 |
| Runtime  运行时 | Files in  `scripts/`  ,  `references/`  ,  `assets/`  , subskills,  `FORMATTING.md`  ,  `SPECIAL_CASES.md`  文件位于 `scripts/` 、 `references/` 、 `assets/` 、子技能、 `FORMATTING.md` 、 `SPECIAL_CASES.md` 中。 | Unbounded  无界 | Only when the agent reads them  仅当代理读取它们时 |

Computer builds a Skill index that has the name and the description for every available Skill. The budget for this is around 100 tokens per Skill (shorter is even better). It’s so tight because you're paying this cost in every session, for every user. This is injected into the system prompt at the very beginning of the conversation. The model has access to a bunch of named Skills and descriptions so that it can decide whether to call “

`load_skill()`

”. The bar to getting into this index is extremely high. Your Skill needs to be very useful, and the description needs to be extremely dense and terse because everyone is paying the cost all the time.

计算机构建一个技能索引，其中包含每个可用技能的名称和描述。每个技能的预算约为 100 个代币（越短越好）。它是如此紧张，因为您要在每个会话中为每个用户支付这笔费用。这会在对话一开始就被注入到系统提示符中。该模型可以访问一堆命名技能和描述，以便它可以决定是否调用“ `load_skill()` ”。进入该指数的门槛非常高。你的技能需要非常有用，并且描述需要非常密集和简洁，因为每个人一直在付出成本。

After the agent system loads the Skill, there’s the full

`SKILL.md`

body. Ideally, the body text does not exceed 5,000 tokens. Even then, you want every sentence to matter because once you load a Skill, the rest of the conversation has to pay that until you hit the compaction boundary. Many threads load anywhere between three and five different Skills, multiplying this cost. Skills with a lot of fluff will almost certainly degrade other Skills as well as overall agentic capabilities. In short, if your Skill loads and it doesn't do the right thing, that's wasted context.

代理系统加载技能后，就有完整的 `SKILL.md` 主体。理想情况下，正文不超过 5,000 个标记。即便如此，你也希望每句话都很重要，因为一旦你加载了一项技能，剩下的对话就必须付出代价，直到你达到压缩边界。许多线程会加载三到五种不同的技能，从而使成本成倍增加。含有大量废话的技能几乎肯定会降低其他技能以及整体代理能力。简而言之，如果你的技能加载后却没有做正确的事情，那就是浪费了上下文。

The final level of progression is scripts or special cases, like subskills or formatting. This is where you want to put unbounded conditional branched logic. The agent will only use it when it needs to, meaning there's a much lower bar for what you want to put in here.

最后的进展级别是脚本或特殊情况，例如子技能或格式。这是您想要放置无限制条件分支逻辑的地方。代理只会在需要时使用它，这意味着您要在此处放置的内容的门槛要低得多。

In the index, every token is important. The loaded Skill body is more relaxed, and the runtime is the most relaxed. This could be 20,000 tokens or zero tokens. This is the level at which you might think about expanding the context of the model in a progressive fashion.

在指数中，每个代币都很重要。加载的技能本体比较轻松，运行时也是最轻松的。这可能是 20,000 个代币或零个代币。在这个级别上，您可能会考虑以渐进的方式扩展模型的上下文。

## When do you need a Skill?你什么时候需要技能？

The Agents team is often asked to opine on whether a Skill is truly needed for a given domain or use case. Very rarely do we have a definitive answer from first principles alone. The only way to really figure this out is to start with your agent without the Skill, run several hero queries, and then figure out whether the agent is doing a good job.

代理团队经常被要求就给定领域或用例是否真正需要某项技能发表意见。仅凭第一原理我们很少能得到明确的答案。真正弄清楚这一点的唯一方法是从没有技能的代理开始，运行几个英雄查询，然后确定代理是否做得很好。

### When you need a Skill当你需要一项技能时

There are many tasks that are in distribution for trained models. You only need to apply a Skill if you want to change that behavior in some specific way that you can't with say, one sentence in your prompt. So, you need a Skill when the agent will get it wrong without special context, or if there's some inconsistency or non-determinism that you need to be extremely consistent across runs.

有许多任务是为经过训练的模型分配的。如果您想以某种特定方式改变该行为，而您无法通过提示中的一句话来改变该行为，则只需应用技能即可。因此，当代理在没有特殊上下文的情况下出错时，或者如果存在一些不一致或不确定性，您需要在运行中保持极其一致时，您就需要一项技能。

It could be that your knowledge is durable but not in the training data. There could be cutoffs or enterprise specific workflows, or it could be a matter of taste. For example, we have several design-related Skills in Computer written by Henry Modisett (our head of design). The reason that every token exists in those Skills is because Henry has very good taste when it comes to designing websites and PDFs. Henry specifies which fonts to use and which fonts not to use, how those fonts

*

feel

*

, and other matters of judgment that the model can't learn from training data alone.

您的知识可能是持久的，但不在训练数据中。可能存在中断或企业特定的工作流程，或者可能是品味问题。例如，我们有一些由亨利·莫迪塞特（我们的设计主管）撰写的与计算机设计相关的技能。这些技能中存在每个标记的原因是因为 Henry 在设计网站和 PDF 方面具有非常好的品味。 Henry 指定了使用哪些字体、不使用哪些字体、这些字体的感觉如何，以及模型无法仅从训练数据中学习的其他判断问题。

### When you don’t need a Skill当你不需要技能时

We see many Skills in which engineers have written a series of git commands that need to be executed in order. That’s unnecessary because the model already knows how to do that, meaning it makes for great documentation but a poor Skill.

我们看到很多技能中工程师都编写了一系列需要按顺序执行的git命令。这是不必要的，因为模型已经知道如何做到这一点，这意味着它可以提供很好的文档，但技能却很差。

We see examples where Skills recapitulate instructions from the system prompt. You don't need a Skill for that. Knowledge relevant for the majority of requests should be included in global context, not in a conditionally loaded Skill

我们看到技能重述系统提示符中的指令的示例。你不需要为此拥有技能。与大多数请求相关的知识应包含在全局上下文中，而不是包含在有条件加载的技能中

If there's something that's changing faster than you can maintain it, you don't need a Skill. For example, if you're hitting some remote MCP endpoint and its tools or the versions of those tools are changing frequently, you shouldn't inject those into a Skill. If you do, you’ll just end up with drift and the model will make mistakes.

如果某些事物的变化速度快于您的维护速度，那么您就不需要技能。例如，如果您正在访问某些远程 MCP 端点及其工具，或者这些工具的版本经常更改，则不应将它们注入技能中。如果这样做，最终就会出现漂移，模型也会出错。

### Every Skill is a tax每项技能都是一种税

Here’s a useful test you can apply to every sentence in your Skill: “Would the agent get this wrong without this instruction?” If the sentence does not need to be there, it cannot afford to be there because everyone is paying this cost every single time. When you are deciding whether to add a Skill or not, remember this tax wherein every session and every user costs tokens.

这是一个有用的测试，您可以将其应用于技能中的每个句子：“如果没有此指令，代理会出错吗？”如果句子不需要在那里，它就不能在那里，因为每个人每次都付出这个成本。当您决定是否添加技能时，请记住这种税收，其中每个会话和每个用户都需要花费代币。

The following famous quote, which sounds much better in French, roughly translates to “I have only made this letter longer because I have not had the time to make it shorter.”

下面这句名言用法语听起来要好得多，大致翻译为“我只是把这封信写得更长，因为我没有时间把它写得更短。”

> « Je n’ai fait celle-ci plus longue que parce que je n’ai pas eu le loisir de la faire plus courte. » — Blaise Pascal, Lettres Provinciales, 1657
> 
> « Je n'ai fait celle-ci plus longue que parce que je n'ai pas eu le loisir de la faire plus Courte. » — 布莱斯·帕斯卡，《省文学》，1657 年

Just like Pascal, you need to invest time in every Skill. It is hard to write a short Skill. If your Skill is easy to write, it is probably too long or shouldn’t exist. A good Skill is as short as it can be.

就像帕斯卡一样，你需要在每项技能上投入时间。写一个简短的技能是很困难的。如果您的技能很容易编写，则它可能太长或不应该存在。好的技能越短越好。

If you find yourself trying to one-shot Skill generation and putting up PRs in five minutes, the results will almost certainly be subpar. In fact, early research has

[

shown

](https://arxiv.org/abs/2602.12670)

that if you're using LLMs to write Skills, the LLM will probably not benefit from it: “Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming.”

如果您发现自己尝试一次性生成技能并在五分钟内获得 PR，那么结果几乎肯定会低于标准。事实上，早期研究表明，如果你使用法学硕士来编写技能，法学硕士可能不会从中受益：“平均而言，自我生成的技能没有提供任何好处，这表明模型无法可靠地编写它们从消费中受益的程序知识。”

## How to build a Skill如何培养技能

Put another way, you need to inject your opinion into any Skill that you write. Follow these steps.

换句话说，您需要将您的意见注入到您编写的任何技能中。请按照以下步骤操作。

### Step 0: Write the Evals第 0 步：编写评估

Write some of the evals first. You can source evaluation cases from:

首先写一些评估。您可以从以下来源获取评估案例：

- Real user queries: sample from production or your brain trust
	真实用户查询：来自生产或您的智囊团的样本
- Known failures: The agent failed because the Skill didn't exist
	已知失败：代理失败，因为技能不存在
- Neighbor confusion: Close to your domain boundary but routes to another Skill
	邻居混乱：靠近您的领域边界，但路由到另一个技能

At the very least, you should be making sure that you're testing that the Skill loads when needed. Ideally, you sample some of these, maybe from a production environment. You might also consider known error cases: maybe the whole reason that you set out to write the Skill is because of a specific failure you noticed or maybe you're refactoring and there's some confusion in two close domains that are covered by one Skill.

至少，您应该确保在需要时测试技能是否加载。理想情况下，您可以从生产环境中对其中一些进行采样。您还可以考虑已知的错误情况：也许您开始编写技能的全部原因是您注意到的特定故障，或者您可能正在重构，并且一项技能涵盖的两个紧密领域存在一些混乱。

Start with similar negative and positive examples. Negative examples are extremely powerful and can matter more than positive examples.

从类似的反面和正面例子开始。负面例子非常有力，比正面例子更重要。

### Step 1: The Description 第 1 步：描述

This is the hardest line in the Skill. It’s a routing trigger, not documentation. To get the name and the description right, you don't care about the content of the Skill. You only care about whether the Skill is loaded and injected at the right points and is free of off-target side effects, which is the number one failure mode. Every time you add an additional Skill, you risk making every

*

other

*

Skill slightly worse, so you need to make sure that you're minimizing regression.

这是技能中最难的一行。这是一个路由触发器，而不是文档。为了获得正确的名称和描述，您不必关心技能的内容。你只关心技能是否在正确的点加载和注入，并且没有偏离目标的副作用，这是第一个失败模式。每次添加额外的技能时，您都会冒着使其他技能稍微变差的风险，因此您需要确保最大限度地减少回归。

Again, a bad description describes what the Skill does or why it is useful. A good description says when the agent should load the Skill. For example, say you have something for monitoring pull requests. Don't write what the Skill does. Write what engineers say when they're frustrated and they want you to make sure that their PR works, like “babysit” or “watch CI” or “make sure this lands.”

同样，错误的描述描述了技能的用途或为何有用。一个好的描述会说明代理应该何时加载技能。例如，假设您有一些用于监视拉取请求的东西。不要写技能的作用。写下工程师在感到沮丧并希望你确保他们的公关有效时所说的话，例如“保姆”或“观看 CI”或“确保这落地”。

Here’s a quick checklist:

这是一个快速清单：

- Starts with "Load when..."
	以“加载时...”开头
- Target 50 words or fewer
	目标字数不超过 50 个
- Describes the user’s intent, ideally from real queries
	描述用户的意图，最好来自真实的查询
- Does not summarize the workflow
	没有总结工作流程

Real queries are what you can cover in an 80-20. Usually, two or three examples work well. It's not easy to add exactly and only as much as you need.

真正的查询是您可以在 80-20 中涵盖的内容。通常，两个或三个示例就可以发挥作用。准确地添加您需要的量并不容易。

### Step 2: Write the Body第二步：写正文

Next, write the content of the Skill itself. Notice this is not Step 0 or Step 1.

接下来，写技能本身的内容。请注意，这不是步骤 0 或步骤 1。

Communicating workflows to an LLM is completely different to communicating workflows to a colleague, or even to your runtime system. When learning a new software tool, an engineer might need to read the documentation, get a walkthrough from someone with experience, and learn how to use the tool. Meanwhile, for almost any software tool that has been around at least a year, you just need to mention its name and the LLM has all the information it needs.

与 LLM 沟通工作流程与与同事甚至运行时系统沟通工作流程完全不同。在学习新的软件工具时，工程师可能需要阅读文档、从有经验的人那里获得演练，并学习如何使用该工具。同时，对于几乎任何已经存在至少一年的软件工具，您只需提及其名称，法学硕士即可获得其所需的所有信息。

When you are writing the body, skip the obvious things. Many engineers have plenty of experience writing readme.md files that list out every command someone needs to run. It's easy to fall back into that when you're writing a Skill because it feels like you're writing documentation, but if you do that, your Skill will be garbage. So, don't write out a series of commands.

当你写正文时，跳过明显的事情。许多工程师在编写 readme.md 文件方面拥有丰富的经验，这些文件列出了需要运行的每个命令。当您编写技能时，很容易陷入这种情况，因为感觉就像您在编写文档，但如果您这样做，您的技能将是垃圾。因此，不要写出一系列命令。

For example, you don’t need to write, “

`git log # find the commit; git checkout main; git checkout -b <clean-branch>; git cherry-pick <commit>;`

”

例如，您不需要写“ `git log # find the commit; git checkout main; git checkout -b <clean-branch>; git cherry-pick <commit>;`”。

Instead, write, “Cherry-pick the commit onto a clean branch. Resolve conflicts preserving intent. If it can't land cleanly, explain why.”

相反，你可以这样写：“将提交挑选到一个干净的分支上。解决保留意图的冲突。如果它不能干净地落地，请解释原因。”

The model will do a much better job with the latter than with the former’s overly prescriptive series of commands, especially when things go wrong. Don't railroad, or be overly prescriptive, which is fragile, and instead be flexible where multiple approaches can work. Again, good documentation for humans is most often bad documentation for models.

该模型对后者的处理效果比对前者过于规范的一系列命令的处理效果要好得多，尤其是当出现问题时。不要循规蹈矩，也不要过于规范，这是脆弱的，而要在多种方法可行的情况下保持灵活性。同样，对人类来说好的文档通常对模型来说是糟糕的文档。

Next, focus on the gotchas or negative examples. These are extremely high-signal content because they often guide the model in terms of what not to do. If you add a line every time the agent trips up, you’ll learn by running it and the gotchas will grow organically.

接下来，关注陷阱或负面例子。这些都是非常重要的内容，因为它们经常指导模型不要做什么。如果每次代理出错时都添加一行，您将通过运行它来学习，并且陷阱将有机增长。

Lastly, if there’s any portion that's conditional or extremely heavy in content, take it out of the

`SKILL.md`

, which is the hub, and put it into one of the spokes. Put it into an accessory file that can be progressively loaded, which we’ll dive into next.

最后，如果有任何部分是有条件的或内容非常繁重，请将其从 `SKILL.md` （即中心）中取出，并将其放入其中一个辐条中。将其放入可以逐步加载的附件文件中，我们接下来将深入探讨该文件。

### Step 3: Use the Hierarchy第 3 步：使用层次结构

Make use of the Skill hierarchy when you've got a script, references, or you’re using some specific tool:

当您拥有脚本、参考资料或正在使用某些特定工具时，请利用技能层次结构：

| `scripts/`  Deterministic logic the agent would reinvent every run  代理每次运行都会重新发明确定性逻辑 | Give it code to compose, not reconstruct  给它代码来组合，而不是重构 |
| --- | --- |
| `references/`  Heavy docs loaded only when a condition is met  仅在满足条件时加载大量文档 | "Read  `api-errors.md`  if API returns non-200"  “如果 API 返回非 200，则读取 `api-errors.md` ”。 |
| `assets/`  Output templates the agent copies and fills  代理复制并填写的输出模板 | `report-template.md`  , output schemas  `report-template.md` ，输出模式。 |
| `config.json`  First-run user setup  首次运行用户设置 | Ask for the Slack channel, save, and reuse next time  求Slack频道，保存，下次再用 |

For anything that's conditional or branching from the main Skill, break it out into a folder. Remember, also, that multilevel hierarchy can be used for particularly intricate Skills. For these, you’ll want to give careful thought to whether the functionality should be implemented monolithically or as a collection of Skills (perhaps with

`depends:`

based loading relationships).

对于任何有条件的或从主要技能分支的内容，请将其分解到一个文件夹中。另请记住，多级层次结构可用于特别复杂的技能。对于这些，您需要仔细考虑该功能是否应该整体实现还是作为技能的集合（可能使用基于 `depends:` 的加载关系）。

### Step 4: Iterate 第 4 步：迭代

Next, do a bunch of iterations on a branch. Start on the main branch with no Skill, do some iterations, build your hero query set, and run a slew of evals. Anyone reviewing your Skill code will thank you for submitting a single changeset complete with an evaluation set. Reviewing consecutive incremental changes (except a new gotcha) is very hard, so try to minimize it.

接下来，在分支上进行一系列迭代。从没有技能的主分支开始，进行一些迭代，构建英雄查询集，并运行大量评估。任何审查您的技能代码的人都会感谢您提交包含评估集的单个变更集。审查连续的增量更改（除了新的陷阱）非常困难，因此请尽量减少它。

You’ll likely do many small word changes. Small word changes in descriptions can have an outsized impact on routing (including spillover effects on other Skills), so do all that work before Step 5.

您可能会做许多小的单词更改。描述中的微小文字更改可能会对路由产生巨大影响（包括对其他技能的溢出效应），因此请在步骤 5 之前完成所有工作。

### Step 5: Ship 第 5 步：发货

Ship it.

运送它。

## How to Maintain a Skill如何保持技能

Now that you’ve written a Skill, you have to maintain it.

现在您已经编写了一项技能，您必须维护它。

### The Gotchas Flywheel 飞轮的陷阱

From this point on, your list of gotchas tends to grow or change a lot. We often see engineers who make PRs that are un-evaled, for example, change the description. If you're changing the description after your Skill has been merged, you are off track. If you're making changes to the thing that decides whether to route your Skill, you need to write some evals that support the changes.

从现在开始，你的陷阱清单往往会增加或改变很多。我们经常看到工程师做出未经评估的 PR，例如更改描述。如果您在技能合并后更改描述，那么您就偏离了轨道。如果您要对决定是否路由您的技能的事物进行更改，则需要编写一些支持更改的评估。

Skills are append-mostly. The gotchas section accrues the most value over time:

技能主要是附加的。随着时间的推移，陷阱部分会产生最大的价值：

- Agent fails at something → Add a gotcha
	代理在某件事上失败 → 添加陷阱
- Agent loads the Skill off target → Tighten description and add negative evals
	代理加载技能偏离目标→收紧描述并添加负面评估
- Agent doesn't load the Skill when it should → Add keywords and positive evals
	代理在应该加载技能时却没有加载 → 添加关键字和积极评价
- System prompt changes → Check for contention or duplication
	系统提示更改→检查是否存在争用或重复

It's easy to notice a single failure case in internal testing or in production and add a gotcha. It’s a negative example so it’s not really changing explicit guidance, but it lets the model know, “Hey, there's this known failure.”

在内部测试或生产中很容易注意到单个故障案例并添加陷阱。这是一个反面例子，因此它并没有真正改变明确的指导，但它让模型知道，“嘿，有一个已知的失败。”

As you move from the 80-20 to getting to a 99.9% or 99.99% success rate, it's easy to grow this gotcha list. As you see these negative examples, you should be appending mostly to the gotcha section. You shouldn't be adding longer instructions or changing the description.

当您从 80-20 提高到 99.9% 或 99.99% 的成功率时，这个陷阱列表很容易增加。当您看到这些负面示例时，您应该将大部分内容附加到陷阱部分。您不应该添加更长的说明或更改描述。

### Eval Suites 埃瓦尔套房酒店

At Perplexity, we run many eval suites to check for different things. There are Skill loading and Skill file reads, which checks the precision, recall, and forbidden checks of the Skill loading itself. Will the agent route your Skill when it's supposed to? These ensure new Skills don’t break existing boundaries.

在 Perplexity，我们运行许多评估套件来检查不同的事情。有技能加载和技能文件读取，检查技能加载本身的精确度、召回率和禁止检查。特工会在应该的时候传送你的技能吗？这些确保新技能不会打破现有界限。

There are also evals that can check for proper progressive loading. The agent might load the Skill, but does it read the accessory file or files? For example, if you have a finance Skill for finance queries, does it read the special

`FORMATTING.md`

file?

还有一些评估可以检查是否正确的渐进加载。代理可能会加载技能，但它会读取附件文件吗？例如，如果您有财务查询的财务技能，它是否会读取特殊的 `FORMATTING.md` 文件？

There are also evals for Skills that test for end-to-end task completion within domains. We run the full agent loop and use an LLM judge to grade the results based on a rubric of well-defined criteria.

还有用于测试域内端到端任务完成情况的技能评估。我们运行完整的代理循环，并使用法学硕士法官根据明确定义的标准对结果进行评分。

Finally, it’s important to run these evals against different models. Computer supports at least three different orchestration model families: GPT, Claude Opus, and Claude Sonnet. You want to run your Skill loading and the domain Skills against these different agent orchestrators to ensure that you don't get different behavior. Sonnet and GPT behave quite differently when it comes to Skills.

最后，针对不同模型运行这些评估非常重要。计算机支持至少三种不同的编排模型系列：GPT、Claude Opus 和 Claude Sonnet。您希望针对这些不同的代理协调器运行技能加载和域技能，以确保不会出现不同的行为。 Sonnet 和 GPT 在技能方面的表现截然不同。

### Final thoughts and takeaways 最后的想法和要点

The more Skills you build, the better you will get at building them. If you're not automating or trying to make more reproducible tasks that you're doing on a day-to-day basis using Skills, start immediately.

您培养的技能越多，您就越能更好地培养它们。如果您不打算使用技能实现日常任务的自动化或尝试执行更多可重复的任务，请立即开始。

The act of building Skills makes you better at building more Skills, but also, they're extremely good at automating business processes. If you can describe something you do every week before your standup, at the end of every sprint, or anything that you do as an engineer on a daily, weekly, or even quarterly basis, you should be writing a Skill to buy back your time.

构建技能的行为可以让您更好地构建更多技能，而且它们非常擅长自动化业务流程。如果您可以描述您每周在站会之前、每次冲刺结束时所做的事情，或者您作为工程师每天、每周甚至每季度所做的事情，那么您应该编写一项技能来买回您的时间。

Can you automate postmortems? Can you review pull requests? Any task that you can do, you can at least have the first pass be an Agent Skill. It will save you significant time.

你能自动化事后分析吗？您可以审查拉取请求吗？任何你能做的任务，至少第一关可以是特工技能。这将为您节省大量时间。

That said, remember that a Skill isn’t easy or even always necessary. Less is more. A few other takeaways:

也就是说，请记住，技能并不容易，甚至总是必要的。少即是多。其他一些要点：

1. Write evals before the Skill. Include negative examples and forbidden loads for adjacent but distinct skills.
	在技能之前写下评估。包括负面示例和相邻但不同技能的禁止负载。
2. The description is the hard part. "Load when..." (every word costs attention).
	描述是困难的部分。 “加载时......”（每个词都需要注意）。
3. Gotchas are extremely high-value content. Start thin, grow as the agent fails.
	陷阱是价值极高的内容。从精简开始，随着代理失败而增长。

Remember that it is easy to break other pre-existing Skills by adding a new Skill, even though you didn’t touch it (beware of action at a distance).

请记住，通过添加新技能很容易破坏其他预先存在的技能，即使您没有接触它（注意远距离动作）。

Use all the available tools every time you’re writing and maintaining a Skill. If you want to learn more, the

[

Agent Skills

](https://agentskills.io/home)

website has plenty of good examples, and both our internal repository and the public ecosystem contain many examples of well-designed Skills.

每次编写和维护技能时，请使用所有可用的工具。如果您想了解更多信息，代理技能网站有很多很好的示例，我们的内部存储库和公共生态系统都包含许多精心设计的技能示例。

解释
