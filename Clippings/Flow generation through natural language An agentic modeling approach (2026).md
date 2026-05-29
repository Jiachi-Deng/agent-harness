---
title: "Flow generation through natural language: An agentic modeling approach (2026)"
source: "https://shopify.engineering/fine-tuning-agent-shopify-flow"
author:
  - "[[Ted Chaiwachirasak 特德·柴瓦奇拉萨克]]"
published: 2001-04-22
created: 2026-05-22
description: "We fine-tuned Qwen3-32B into a tool-calling agent that generates Flow automations: 2.2x faster, 68% cheaper, with a weekly retraining flywheel."
tags:
  - "clippings"
compile_status: compiled
compiled_to:
  - "Wiki/AI产品工程/生产级Agent产品工程.md"
  - "Wiki/AI行业判断/从VibeCoding到AgenticEngineering.md"
remaining_value: medium
triage_note: "published 元数据疑似异常；编译强时效判断前需回查原文发布日期。"
---
If you're building AI products on top of closed models, anyone with an API key can get similar capabilities. Lasting differentiation comes from proprietary data, the training recipe, the infrastructure, and the speed of iteration.

如果您在封闭模型之上构建人工智能产品，那么任何拥有 API 密钥的人都可以获得类似的功能。持久的差异化来自专有数据、训练方法、基础设施和迭代速度。

Shopify has something most companies don't: a product surface where millions of merchant interactions directly signal whether the model's output is any good. That feedback loop is the foundation, but only if you keep learning from it.

Shopify 拥有大多数公司所没有的东西：在产品表面上，数以百万计的商家互动直接表明该模型的输出是否良好。反馈循环是基础，但前提是你不断从中学习。

We fine-tuned a tool-calling agent to turn natural language into a Shopify Flow for

[

Sidekick

](https://www.shopify.com/ca/sidekick "Shopify Sidekick")

, our AI commerce assistant. It's 2.2x faster, 68% cheaper, and outperforms closed models.

我们对工具调用代理进行了微调，将自然语言转换为我们的 AI 商务助手 Sidekick 的 Shopify 流程。它的速度提高了 2.2 倍，成本降低了 68%，并且性能优于封闭模型。

Along the way, we found lessons no paper warned us about. Data preprocessing decisions, from representation design to formatting details, that compound to swing accuracy by double digits. Silent infrastructure failures that degrade your model with zero warnings and take days to trace. Benchmark parity that masks a 35% gap once real users show up.

一路走来，我们发现了没有任何论文警告过我们的教训。数据预处理决策，从表示设计到格式细节，使挥杆精度提高了两位数。无声的基础设施故障会在零警告的情况下降低模型的性能，并且需要数天的时间才能追踪。一旦真实用户出现，基准平价就会掩盖 35% 的差距。

This post covers the problems we faced, how we fixed them, and what to look for if you're doing the same.

这篇文章介绍了我们遇到的问题、我们如何解决这些问题，以及如果您也遇到了同样的问题，需要注意什么。

![Data pipeline > Flywheel](https://cdn.shopify.com/s/files/1/0779/4361/files/image2_a0d3c058-3cb2-4b24-87df-8ea9685879f7.png?v=1776796283)

## Building the training dataset 构建训练数据集

Shopify Flow is an automation platform where store owners build workflows from triggers, conditions, and actions. For store owners who aren't engineers, building the right workflow from a blank canvas is daunting. Sidekick generates it from plain English.

Shopify Flow 是一个自动化平台，商店所有者可以在其中根据触发器、条件和操作构建工作流程。对于不是工程师的店主来说，从空白画布构建正确的工作流程是一项艰巨的任务。 Sidekick 从简单的英语生成它。

![Shopify Admin showing Flow](https://cdn.shopify.com/s/files/1/0779/4361/files/image7.png?v=1776796370)

### The cold start problem 冷启动问题

Fine-tuning required training data, but since the feature hadn't been deployed yet, there were no production conversations to learn from.

微调需要训练数据，但由于该功能尚未部署，因此没有可供学习的生产对话。

We reverse-engineered user intent from existing production workflows. Thousands of anonymized store owners had already built workflows manually in Flow. We sampled those and filtered for quality: workflows that had run at least once in the last seven days, from merchants with two or more qualifying workflows, with one example per descriptor to ensure diversity across workflow types.

我们从现有的生产工作流程中对用户意图进行逆向工程。数千名匿名店主已经在 Flow 中手动构建了工作流程。我们对这些工作流程进行了抽样并筛选质量：过去 7 天内至少运行过一次的工作流程，来自具有两个或多个合格工作流程的商家，每个描述符都有一个示例，以确保工作流程类型之间的多样性。

With a set of validated workflows, we worked backwards:

通过一组经过验证的工作流程，我们进行了逆向工作：

1. **
	Sample a workflow.
	**
	Pick a popular, validated workflow from production.
	工作流程示例。 从生产中选择一个流行的、经过验证的工作流程。
2. **
	Generate a user query.
	**
	Use a stronger LLM to produce a plausible natural-language request that would lead to this workflow.
	生成用户查询。 使用更强大的法学硕士来生成合理的自然语言请求，从而实现此工作流程。
3. **
	Construct the tool trajectory.
	**
	Build the full multi-turn sequence of tool calls that an ideal agent would execute to arrive at this workflow. This was the bulk of the engineering effort.
	构造刀具轨迹。 构建完整的多轮工具调用序列，理想代理将执行这些序列来实现此工作流程。这是工程工作的大部分。

We fine-tuned Qwen3-32B on this synthetic dataset and evaluated it against a benchmark of 300 hand-crafted examples covering the breadth of expected Flow usage. An

[

LLM evaluation framework

](https://shopify.engineering/building-production-ready-agentic-systems "LLM judge on Shopify Engineering Blog")

compares the generated workflow against the expected one for semantic correctness, and validates syntactic correctness programmatically.

我们在此综合数据集上对 Qwen3-32B 进行了微调，并根据涵盖预期 Flow 使用范围的 300 个手工制作示例的基准对其进行了评估。 LLM 评估框架将生成的工作流程与预期的工作流程进行语义正确性比较，并以编程方式验证语法正确性。

We looked at three metrics:

我们研究了三个指标：

- **
	Semantic correctness:
	**
	Does the generated workflow do what it's supposed to? An LLM judge compares the output against the expected workflow.
	语义正确性：生成的工作流程是否按照预期执行？法学硕士法官将输出与预期工作流程进行比较。
- **
	Syntactic correctness:
	**
	Are there errors that would cause it to fail? Malformed conditions, incorrect references, invalid configurations. Checked programmatically.
	语法正确性：是否存在会导致失败的错误？格式错误的条件、不正确的引用、无效的配置。以编程方式检查。
- **
	Latency:
	**
	Time from request to workflow delivery.
	延迟：从请求到工作流交付的时间。

If you're building an agent without interaction data, start with the output artifacts your users already produce and work backwards from them. That is often the right first step before your metrics have caught up. As shown in the table above, there is still a meaningful gap to close. Our second lesson, which we discuss below, is that teaching the model to generate Flows in Python can help narrow that gap further.

如果您正在构建没有交互数据的代理，请从用户已经生成的输出工件开始，并从它们开始逆向工作。在您的指标赶上之前，这通常是正确的第一步。如上表所示，仍然存在明显的差距需要弥合。我们的第二课（我们将在下面讨论）是，教授模型在 Python 中生成流可以帮助进一步缩小这一差距。

### Training in-distribution: the Python DSL分布式培训：Python DSL

Shopify Flow workflows are represented internally in a JSON-based domain-specific language (DSL) designed for backend parsing, validation, and execution. That format is ideal for production systems, but it's a poor fit for LLMs. Conditional, program-like logic that would normally appear as code is embedded in deeply nested JSON, a pattern that's rare in pretraining data.

Shopify Flow 工作流程在内部以基于 JSON 的领域特定语言 (DSL) 表示，专为后端解析、验证和执行而设计。这种格式非常适合生产系统，但不太适合法学硕士。通常以代码形式出现的类似程序的条件逻辑嵌入到深度嵌套的 JSON 中，这种模式在预训练数据中很少见。

Rather than forcing the model to learn Flow's native format from scratch, we reformulated the task in a representation closer to the model's training distribution. Workflows are programs, so we taught the model to write them as Python.

我们没有强迫模型从头开始学习 Flow 的原生格式，而是以更接近模型训练分布的表示形式重新表述了任务。工作流是程序，因此我们教模型将它们编写为 Python。

A transpiler converts the JSON DSL into semantically equivalent Python:

转译器将 JSON DSL 转换为语义上等效的 Python：

Same workflow, same semantics, but the model now generates Python instead of a data format. Python is far closer to code and logical reasoning, and it makes up a large share of pretraining data. The fine-tuned model draws on familiar patterns: decorators, if/else logic, variables, for loops, and function calls.

相同的工作流程、相同的语义，但模型现在生成 Python 而不是数据格式。 Python 更接近代码和逻辑推理，并且它占预训练数据的很大一部分。微调的模型借鉴了熟悉的模式：装饰器、if/else 逻辑、变量、for 循环和函数调用。

With the same training data, switching from the JSON DSL to the Python DSL improved syntactic correctness by 22 points and semantic correctness by 13 points. Moving the target format from out-of-distribution to in-distribution turned the problem from "learn a new language and the task" into "learn the task."

使用相同的训练数据，从 JSON DSL 切换到 Python DSL 将语法正确性提高了 22 点，语义正确性提高了 13 点。将目标格式从分布外转移到分布内，将问题从“学习新语言和任务”转变为“学习任务”。

Making this work required building a round-trip transpiler between Python and Flow's JSON representation to handle the full complexity of Flow logic without losing meaning in either direction.

要完成这项工作，需要在 Python 和 Flow 的 JSON 表示之间构建一个往返转译器，以处理 Flow 逻辑的全部复杂性，而不会失去任何方向的意义。

Reliability was backed with extensive tests. We round-trip tested every workflow merchants created through Sidekick in production: converting from JSON to Python and back to JSON, then verifying the output matched the original exactly. Any mismatch was caught before it could reach training data. This process ran continuously across all production workflows, giving us confidence the transpiler handled the full range of real-world patterns.

可靠性得到了广泛测试的支持。我们对商家在生产中通过 Sidekick 创建的每个工作流程进行了往返测试：从 JSON 转换为 Python，然后再转换回 JSON，然后验证输出与原始内容是否完全匹配。任何不匹配都会在到达训练数据之前被捕获。这个过程在所有生产工作流程中持续运行，让我们有信心转译器能够处理各种现实世界的模式。

At inference time, the model writes Python. The transpiler converts it to JSON for the Flow backend. Store owners never see Python, and the backend never has to understand it. Python is the model's internal language.

在推理时，模型编写 Python。转译器将其转换为 JSON 以供 Flow 后端使用。商店老板从来没有见过Python，后端也永远不需要理解它。 Python 是模型的内部语言。

Prior work has explored Python as an intermediate representation (

[

SPEAC

](https://arxiv.org/pdf/2406.03636 "SPEAC")

,

[

LLMLift

](https://arxiv.org/pdf/2406.03003 "LLMLift")

,

[

WorkflowLLM

](https://arxiv.org/pdf/2411.05451 "WorkflowLLM")

), but via prompting or without a round-trip transpiler. What distinguishes this approach is the full loop: fine-tuning on Python combined with a transpiler back to the production DSL, without changing any downstream systems.

之前的工作已经探索了 Python 作为中间表示（ SPEAC 、 LLMLift 、 WorkflowLLM ），但通过提示或没有往返转译器。这种方法的独特之处在于完整的循环：在 Python 上进行微调，并结合转译器返回到生产 DSL，而无需更改任何下游系统。

If you're training a model on a custom DSL, consider translating it into a language the model already knows. This helps separate learning the format from learning the task. As the results show, the gap narrows, but there is still room for improvement. At that point, the next step is to bring the system into production, learn from real usage, and incorporate real user feedback.

如果您正在自定义 DSL 上训练模型，请考虑将其翻译成模型已知的语言。这有助于将学习格式与学习任务分开。结果显示，差距缩小，但仍有改进的空间。届时，下一步是将系统投入生产，从实际使用中学习，并纳入真实的用户反馈。

### Mirroring the production environment镜像生产环境

Representation was one half of the data problem. The other half was making sure the model's training data matched exactly what it would see in production.

表示是数据问题的一半。另一半是确保模型的训练数据与其在生产中看到的数据完全匹配。

We knew training data should match production. What we didn't expect was how sensitive the model is to the

*

degree

*

of match. Every difference we closed, no matter how minor, improved eval scores:

我们知道训练数据应该与生产相匹配。我们没想到的是模型对匹配程度有多敏感。我们消除的每一个差异，无论多么微小，都会提高评估分数：

- **
	Tool naming and ordering:
	**
	Training data used the full prefixed name
	`flow_app_agent_task_search`
	. At inference, the same tool was called
	`task_search`
	. Functionally identical, but the model treated them as different tools. Removing the prefix from training data to match inference improved accuracy. The order in which the tools appeared in the system prompt also mattered. Shuffle the order between training and serving, and performance drops.
	工具命名和排序：训练数据使用完整的前缀名称 `flow_app_agent_task_search` 。据推断，同一个工具被称为 `task_search` 。功能相同，但模型将它们视为不同的工具。从训练数据中删除前缀以匹配推理提高了准确性。工具在系统提示符中出现的顺序也很重要。打乱训练和发球的顺序，成绩就会下降。
- **
	Tool response format:
	**
	Tool responses return JSON objects with multiple fields. In the training data, we sorted keys alphabetically. If production returned them in a different order, or included an extra field, the model noticed. Any drift between what the training data showed and what production APIs actually returned degraded accuracy.
	工具响应格式：工具响应返回具有多个字段的 JSON 对象。在训练数据中，我们按字母顺序对键进行排序。如果生产以不同的顺序返回它们，或者包含额外的字段，模型会注意到。训练数据显示的内容与生产 API 实际返回的内容之间的任何偏差都会降低准确性。
- **
	System prompt and tool descriptions:
	**
	Tool descriptions in production changed frequently as the product team iterated on behavior. Every update had to be reflected in the training data, or the model's behavior drifted. Keeping both in sync was an ongoing process, not a one-time fix.
	系统提示和工具描述：随着产品团队对行为的迭代，生产中的工具描述经常发生变化。每次更新都必须反映在训练数据中，否则模型的行为就会发生偏差。保持两者同步是一个持续的过程，而不是一次性修复。

None of these are about the logic of the task. They are formatting details. The model treats every token as a signal, whether you intended it or not.

这些都与任务的逻辑无关。他们正在格式化详细信息。该模型将每个标记视为一个信号，无论您是否有意这样做。

### Optimizing the tool-calling stack优化工具调用堆栈

When an agent calls tools, every response becomes part of the context. Context grows, latency grows, cost grows. Worse, irrelevant context dilutes the signal. The model reasons less accurately when it’s processing information it won't use.

当代理调用工具时，每个响应都成为上下文的一部分。上下文增长、延迟增长、成本增长。更糟糕的是，不相关的上下文会削弱信号。当模型处理不使用的信息时，其推理不太准确。

We restructured our tool interfaces to minimize context at each step. Instead of returning full details for every result upfront, tools return lightweight summaries first. The model scans the summaries, selects what it needs, then retrieves full details only for those necessities. Two cheap calls instead of one expensive one.

我们重组了工具界面，以最大限度地减少每个步骤的上下文。工具不会预先返回每个结果的完整详细信息，而是首先返回轻量级摘要。该模型会扫描摘要，选择所需内容，然后仅检索这些必需品的完整详细信息。两次便宜的通话，而不是一次昂贵的通话。

For example, Flow has hundreds of available triggers, conditions, and actions. A search might return 100 matches. Rather than loading the full configuration schema for each one,

`task_search`

returns just names and descriptions. The model picks the 2-3 it actually needs, then calls

`task_configuration`

to get the full schema only for those. The context stays small, the reasoning stays focused.

例如，Flow 有数百个可用的触发器、条件和操作。搜索可能会返回 100 个匹配项。 `task_search` 不加载每个配置的完整配置模式，而是仅返回名称和描述。该模型选择它实际需要的 2-3，然后调用 `task_configuration` 仅获取这些的完整架构。上下文保持较小，推理保持集中。

![Merchant request > Shopify Flow workflow created](https://cdn.shopify.com/s/files/1/0779/4361/files/image1_92d92421-357a-4ef5-805f-569ab8a67ad0.png?v=1776796570)

## Making training fast 加快训练速度

As our data pipeline grew, so did a tension: more training data improved accuracy but slowed each run. Slower runs meant fewer iterations, and fewer iterations meant slower improvement. We needed a way to use all the data and still retrain weekly.

随着我们的数据管道的增长，压力也随之增加：更多的训练数据提高了准确性，但降低了每次运行的速度。运行速度越慢意味着迭代次数越少，迭代次数越少意味着改进速度越慢。我们需要一种方法来使用所有数据并且仍然每周重新训练。

We built the infrastructure to make both possible. Qwen3-32B trains on two nodes of H200 GPUs with Fully Sharded Data Parallel (FSDP). A full training run takes 12 hours, fast enough for weekly retraining with multiple experimental runs in between.

我们构建了基础设施，使这两者成为可能。 Qwen3-32B 在具有完全分片数据并行 (FSDP) 的 H200 GPU 的两个节点上进行训练。完整的训练运行需要 12 小时，足够快以进行每周的再训练，并在其间进行多次实验运行。

The full pipeline, from data collection through training, evaluation, and deployment, runs on

[

Tangle

](https://shopify.engineering/tangle "Tangle on Shopify Engineering Blog")

, Shopify's open-source ML experimentation platform. Tangle composes each step into a single reproducible workflow with intelligent caching. Only the affected steps re-run when one part changes.

从数据收集到训练、评估和部署的完整流程都在 Shopify 的开源 ML 实验平台 Tangle 上运行。 Tangle 通过智能缓存将每个步骤组合成一个可重复的工作流程。当某一部分发生更改时，仅会重新运行受影响的步骤。

![Tangle dashboard: Shopify Flow](https://cdn.shopify.com/s/files/1/0779/4361/files/image3_1a0e8f26-d7ba-4ff9-a63d-39bf8454449f.png?v=1776796646)

CometML tracks every run. HuggingFace hosts datasets and checkpoints. CentML serves the model in production. Weekly retraining runs without manual intervention.

CometML 跟踪每次跑步。 HuggingFace 托管数据集和检查点。 CentML 为生产中的模型提供服务。每周进行再训练，无需人工干预。

![Tangle pipeline](https://cdn.shopify.com/s/files/1/0779/4361/files/image5.png?v=1776796678)

## Evaluation: benchmarks aren't ground truth评估：基准不是事实

Synthetic data got us to parity on offline benchmarks. By every metric we tracked, the fine-tuned model was ready for production. We deployed it to 1% of traffic to see how it held up.

综合数据让我们在离线基准测试中达到同等水平。根据我们跟踪的每个指标，经过微调的模型已准备好投入生产。我们将其部署到 1% 的流量，看看它的表现如何。

At 1% traffic, the fine-tuned model's workflow activation rate (whether store owners actually turn on the workflows Sidekick generates) came in 35% lower than the prompt-based agent. The benchmark covered what we expected merchants to ask. It didn't cover what they actually asked: editing existing workflows, handling email configurations, working with third-party integrations, and asking questions about Flow without intending to create a workflow.

在流量为 1% 时，微调模型的工作流激活率（无论商店所有者是否实际打开 Sidekick 生成的工作流）比基于提示的代理低 35%。该基准涵盖了我们期望商家提出的要求。它没有涵盖他们实际要求的内容：编辑现有工作流程、处理电子邮件配置、使用第三方集成以及询问有关 Flow 的问题而不打算创建工作流程。

The model performed well in-domain, but real traffic quickly surfaced out-of-distribution requests that our synthetic data had not covered. The low-traffic early deployment showed us exactly where to focus next. Activation rate was our first production signal, but it turned out to be noisy: it reflects merchant behavior, not model quality. We therefore optimized for a domain-expert-calibrated

[

LLM judge

](https://shopify.engineering/building-production-ready-agentic-systems "LLM Judge")

, which we describe next, while keeping activation rate as a guardrail to ensure we did not regress.

该模型在域内表现良好，但实际流量很快就出现了我们的合成数据未涵盖的分布外请求。早期的低流量部署向我们展示了下一步的重点。激活率是我们的第一个生产信号，但事实证明它很嘈杂：它反映了商家行为，而不是模型质量。因此，我们针对领域专家校准的 LLM Judge 进行了优化，我们接下来将对此进行描述，同时保持激活率作为护栏，以确保我们不会倒退。

## Flywheel: from catching up to pulling ahead飞轮：从追赶到领先

### Closing the gap 缩小差距

The 1% deployment showed us exactly where the model was falling short. We needed a system that could diagnose those gaps, fix them, and retrain fast. Not once, but continuously.

1% 的部署准确地向我们展示了该模型的不足之处。我们需要一个能够诊断这些差距、修复它们并快速重新训练的系统。不是一次，而是持续不断。

We built an LLM-based judge that scores each conversation across the workflow lifecycle: whether the assistant correctly understood the merchant's intent, chose a Flow solution only when appropriate, selected the right components, and gave clear next steps. The judge grades each facet separately rather than treating quality as a single pass/fail outcome. To calibrate it, we collected human annotations on hundreds of conversations and tuned it until its scores aligned with human judgment, then validated against production activation rate.

我们构建了一个基于 LLM 的法官，对整个工作流程生命周期中的每个对话进行评分：助理是否正确理解了商家的意图，仅在适当时选择 Flow 解决方案，选择了正确的组件，并给出了明确的后续步骤。法官对每个方面分别进行评分，而不是将质量视为单一的通过/失败结果。为了校准它，我们收集了数百个对话的人工注释并对其进行调整，直到其分数与人类判断一致，然后根据生产激活率进行验证。

A tagging system classifies every workflow along multiple dimensions: which triggers it uses, what conditions it checks, which actions it invokes, and whether it involves third-party integrations. Comparing performance across tagged slices pinpoints exactly where the model struggles. When performance drops on a particular slice, we know what kind of data to add.

标记系统沿多个维度对每个工作流程进行分类：它使用哪些触发器、它检查什么条件、它调用哪些操作以及它是否涉及第三方集成。比较标记切片的性能可以准确找出模型的问题所在。当特定切片的性能下降时，我们知道要添加哪种数据。

The judge and tagging system together form the diagnostic layer. The fixes were concrete:

判断和标记系统共同构成诊断层。修复措施是具体的：

- Email workflows accounted for 25% of failures, so we added email-specific examples
	电子邮件工作流程占失败的 25%，因此我们添加了特定于电子邮件的示例
- Diverse condition patterns accounted for 16%
	多样化的状况模式占16%
- Workflow editing, which was something synthetic data had never covered
	工作流程编辑，这是合成数据从未涵盖的内容

The following diagram shows our progress in Flow modeling, with quality improving steadily over time as measured by our LLM judge:

下图显示了我们在流程建模方面的进展，根据我们的法学硕士评委的衡量，质量随着时间的推移稳步提高：

![LLM judge score over each month](https://cdn.shopify.com/s/files/1/0779/4361/files/LLM_Judge_score_over_each_month.png?v=1776860795)

### Continuous improvement 持续改进

Closing the gap was the first test. Staying ahead is the real goal.

缩小差距是第一个考验。保持领先才是真正的目标。

Every production conversation becomes a training signal. We sample high-quality examples: conversations where merchants actually activated the workflow afterwards. The judge scores them, and high-scoring conversations are routed into the training pool automatically. Low-scoring ones are quarantined for review.

每一次生产对话都成为一个培训信号。我们采样高质量的示例：商家随后实际激活工作流程的对话。评委给他们打分，高分的对话会自动进入训练池。低分者将被隔离以供审查。

The loop runs weekly:

该循环每周运行一次：

1. Ingest production conversations
	摄取生产对话
2. Score with the LLM judge
	与LLM评委打分
3. Route high-quality examples into training; quarantine low-quality for review
	将高质量示例纳入培训；检疫低质量待审查
4. Identify gaps through tagged slice analysis
	通过标记切片分析识别差距
5. Retrain and deploy
	重新训练和部署

The system improves as production traffic shifts, freeing the team to focus on expanding coverage and fixing systematic gaps rather than hand-curating data. The approach is similar in spirit to Karpathy's

[

Autoresearch

](https://shopify.engineering/autoresearch "Autoresearch on Shopify Engineering Blog")

, an automated loop that evaluates, keeps what works, discards what doesn't, and iterates—but applied to production data curation rather than training code.

该系统随着生产流量的变化而改进，使团队能够专注于扩大覆盖范围和修复系统差距，而不是手动管理数据。该方法在本质上与 Karpathy 的 Autoresearch 类似，这是一种自动循环，可以评估、保留有效的内容、丢弃无效的内容并进行迭代，但应用于生产数据管理而不是训练代码。

## What's next 接下来是什么

The flywheel is running, but the race between in-house and closed-source models doesn't stop. Every few months, a new frontier model raises the bar. The only way to stay ahead is to keep compounding: better data, better training, better evaluation, faster iteration. Here's where we're pushing next.

飞轮正在运转，但内部模型和闭源模型之间的竞争并没有停止。每隔几个月，就会有新的前沿模型提高标准。保持领先的唯一方法是不断复合：更好的数据、更好的训练、更好的评估、更快的迭代。这就是我们接下来要努力的地方。

**Simulation environments.**

A sandbox where the model can generate workflows and receive structured feedback on whether they would succeed, without impacting real merchants. The model writes test cases and runs them against a simulated Flow environment, creating a setting for verifiable rewards. This opens the door to distillation from stronger teacher models and on-policy optimization.

模拟环境。 模型可以在沙箱中生成工作流程并接收有关其是否成功的结构化反馈，而不会影响真正的商家。该模型编写测试用例并在模拟的 Flow 环境中运行它们，从而创建可验证奖励的设置。这为从更强大的教师模型和策略优化中提炼打开了大门。

**From off-policy to on-policy.**

Everything so far is off-policy: the model learns from curated examples collected after the fact. With verifiable rewards from the simulation environment, the next step is policy optimization where the model learns from its own generated trajectories. The goal is a model that discovers better strategies, not one that only replicates what it's seen.

从离政策到在政策。 到目前为止，一切都是偏离策略的：模型从事后收集的精选示例中学习。有了来自模拟环境的可验证奖励，下一步是策略优化，模型从自己生成的轨迹中学习。我们的目标是建立一种能够发现更好策略的模型，而不是仅仅复制所看到的策略。

**From manual calibration to self-improving evaluation.**

Today, the LLM judge is calibrated against human annotations and production activation rate. But merchant behavior shifts, new integrations launch, and new workflow patterns emerge faster than manual recalibration can keep up. Automating judge calibration against live production signals is the next evaluation challenge.

从手动校准到自我改进评估。 如今，法学硕士法官根据人工注释和生产激活率进行校准。但商家行为的转变、新集成的启动以及新工作流程模式的出现速度比手动重新校准的速度要快。根据现场制作信号自动进行判断校准是下一个评估挑战。

## Results in production 生产结果

The fine-tuned Flow agent now serves the majority of our production traffic.

经过微调的 Flow 代理现在服务于我们的大部分生产流量。

No single technique got us here. Each stage built on the last. Synthetic data generation needed the Python DSL to close the accuracy gap. The DSL needed production mirroring to hold up in the real environment. Production mirroring needed infrastructure stable enough to trust. And when benchmarks said we were ready but production said otherwise, the flywheel closed the gap in two weeks.

没有单一的技术让我们走到这一步。每个阶段都建立在最后一个阶段之上。合成数据生成需要 Python DSL 来缩小准确性差距。 DSL 需要生产镜像才能在真实环境中运行。生产镜像需要足够稳定且值得信赖的基础设施。当基准测试表明我们已经准备好，但生产情况却相反时，飞轮在两周内缩小了差距。

## When does this generalize? 这什么时候才能普遍化呢？

This approach applies when:

此方法适用于以下情况：

1. **
	The task requires tool calling.
	**
	The model must reason, act, and incorporate external results, not just generate text.
	该任务需要调用工具。 该模型必须推理、行动并结合外部结果，而不仅仅是生成文本。
2. **
	The output format is a custom DSL
	**
	that doesn't appear in pretraining data, and its semantics can be expressed in a language the model already knows.
	输出格式是自定义的 DSL，不会出现在预训练数据中，其语义可以用模型已知的语言来表达。
3. **
	A round-trip transpiler is feasible
	**
	between the in-distribution representation and the production format.
	分发内表示和生产格式之间的往返转译器是可行的。
4. **
	A production feedback loop is available.
	**
	Synthetic data gets you started, but real-world data is what gets you to production quality.
	可以使用生产反馈回路。 合成数据可以帮助您入门，但真实世界的数据可以帮助您达到生产质量。

Within Sidekick, this pattern is already being applied to other skills. The recipe is the same: isolate the skill, fine-tune the tool-calling model, and build the loop for continuous improvement.

在 Sidekick 中，这种模式已经应用于其他技能。秘诀是一样的：隔离技能，微调工具调用模型，并构建持续改进的循环。

Six months ago, this system ran on a frontier model we didn't control. Now it runs on a model we trained, on infrastructure we own, improving from data only we have, at 68% lower cost. The version running right now is already worse than the one retraining behind it.

六个月前，这个系统运行在我们无法控制的前沿模型上。现在，它在我们训练的模型上运行，在我们拥有的基础设施上运行，仅根据我们拥有的数据进行改进，成本降低了 68%。现在运行的版本已经比后面重新训练的版本差了。

We started on rented ground. This is what the first mile of owned ground looks like.

我们从租来的场地开始。这就是拥有土地的第一英里的样子。

---

This article contains contributions from Nicolas Bertagnolli, Joe Lin, Han Li, Mingyu Zhao, Jason Liu, LinKai Ma, Yuxuan Wang, Matt Koenig, Lingyun Wang, Agentic Foundation Modeling Team.

本文包含来自 Agentic Foundation 建模团队 Nicolas Bertagnolli、Joe Lin、Han Li、Mingyu Zhao、Jason Liu、LinKai Ma、Yuxuan Wang、Matt Koenig、Lingyun Wang 的贡献。
