---
title: "OpenClaw Multi-Agent Guide: Architecture, Configuration, and Collaboration Patterns"
source: "https://www.heyuan110.com/posts/ai/2026-02-23-openclaw-multi-agent-guide/"
author:
  - "[[Bruce]]"
published: 2026-02-23
created: 2026-05-24
description: "A deep dive into multi-agent design inside the OpenClaw AI agent framework (2026). From single-agent bottlenecks to building agent teams, covering routing bindings, inter-agent communication, four collaboration patterns, and production best practices."
tags:
  - "clippings"
compile_status: compiled
compiled_to:
  - "Wiki/AI产品工程/生产级Agent产品工程.md"
remaining_value: medium
---
A deep dive into multi-agent design inside the OpenClaw AI agent framework (2026). From single-agent bottlenecks to building agent teams, covering routing bindings, inter-agent communication, four collaboration patterns, and production best practices.

深入探讨 OpenClaw AI 代理框架内的多代理设计（2026）。从单代理瓶颈到构建代理团队，涵盖路由绑定、代理间通信、四种协作模式和生产最佳实践。[Bruce](https://www.heyuan110.com/about/)

[

布鲁斯

](https://www.heyuan110.com/about/)[OpenClaw](https://www.heyuan110.com/tags/openclaw)

[

开爪

](https://www.heyuan110.com/tags/openclaw)[

Multi-Agent

多代理

](https://www.heyuan110.com/tags/multi-agent)[

AI Collaboration

人工智能协作

](https://www.heyuan110.com/tags/ai-collaboration)[

AI Architecture

人工智能建筑

](https://www.heyuan110.com/tags/ai-architecture)[AI Guides](https://www.heyuan110.com/categories/ai-guides)

[

人工智能指南

](https://www.heyuan110.com/categories/ai-guides)

3548 Words

3548 个字

2026-02-23

2026-02-23

---

Have you ever had this experience: your AI assistant starts “losing its mind” mid-conversation – you ask it to write a blog post, and it suddenly spits out code logic; you ask it to research competitors, and it starts correcting typos from last week?

你是否有过这样的经历：你的AI助手在对话中开始“失去理智”——你让它写一篇博文，它突然吐出代码逻辑；你要求它研究竞争对手，它从上周开始纠正拼写错误？

The AI didn’t get dumber. You’re just making one “brain” do too many jobs. It’s like asking the front desk receptionist to also handle accounting, HR, and engineering – nobody ends up doing anything well.

人工智能并没有变得更愚蠢。你只是让一个“大脑”承担了太多的工作。这就像要求前台接待员同时处理会计、人力资源和工程——最终没有人能做好任何事情。

The solution?

**

Build an AI team

**

– let different agents each handle their own specialty, just like a real company operates.

解决方案是什么？ 建立一个人工智能团队——让不同的代理人各司其职，就像真正的公司运作一样。

This article takes a deep dive into building a multi-agent collaboration system with

[

OpenClaw

](https://github.com/openclaw/openclaw)

. We’ll go beyond “how to configure” and explain “why to configure it this way,” plus how mainstream multi-agent architecture patterns work in practice.

本文深入探讨了使用 OpenClaw 构建多代理协作系统。我们将超越“如何配置”并解释“为什么要这样配置”，以及主流多代理架构模式在实践中如何工作。

## 1\. Why a Single Agent Isn’t Enough1. 为什么单一代理还不够

### 1.1 Three Bottlenecks of a Single Agent1.1 单一Agent的三大瓶颈

Most people use AI assistants in an “all-in-one” fashion: copywriting, coding, image generation, and research all crammed into one agent. This seems convenient, but as usage grows, three problems get progressively worse:

大多数人以“一体化”的方式使用人工智能助手：文案编写、编码、图像生成和研究都塞进一个代理中。这看起来很方便，但随着使用量的增加，三个问题变得越来越严重：

| Problem  问题 | Symptom  症状 | Root Cause  根本原因 |
| --- | --- | --- |
| **  Memory Bloat  内存膨胀  ** | Agent responses get slower over time  随着时间的推移，代理响应速度会变慢 | Memory files (USER.md, memory/, etc.) keep accumulating; every conversation loads massive history  内存文件（USER.md、memory/等）不断累积；每一次对话都承载着大量的历史 |
| **  Context Contamination  环境污染  ** | Answers “bleed” across domains, logic gets confused  答案跨领域“流血”，逻辑混乱 | Knowledge from different domains interferes – writing an article triggers code associations  不同领域的知识相互干扰——写文章触发代码关联 |
| **  Cost Spiral  成本螺旋  ** | Token consumption far exceeds expectations  代币消耗远超预期 | Every conversation carries all irrelevant background material, inflating input tokens  每个对话都包含所有不相关的背景材料，导致输入标记膨胀 |

A vivid analogy: a single agent is like a worker with 50 browser tabs open simultaneously – it looks like everything is being done, but nothing is being done well.

一个形象的比喻：单个代理就像一个同时打开 50 个浏览器选项卡的工作人员 – 看起来一切都在完成，但没有什么做得很好。

### 1.2 The Core Philosophy of Multi-Agent1.2 多Agent的核心理念

The core philosophy of multi-agent architecture is simple:

**

let specialists handle their specialties

**

.

多智能体架构的核心理念很简单：让专家处理他们的专业。

This isn’t a new concept. In software engineering, the Single Responsibility Principle has long told us: a module should have only one reason to change. Applied to the AI agent world:

这不是一个新概念。在软件工程中，单一职责原则早已告诉我们：一个模块应该只有一个改变的理由。应用于AI代理世界：

- A
	**
	writing agent
	**
	only cares about prose – its memory is filled with writing techniques and style templates
	写作代理只关心散文——它的记忆充满了写作技巧和风格模板
- A
	**
	coding agent
	**
	only cares about code logic – its workspace is filled with project code and technical docs
	编码代理只关心代码逻辑——它的工作区充满了项目代码和技术文档
- A
	**
	research agent
	**
	only cares about information gathering – it’s equipped with search tools and data organization abilities
	研究代理只关心信息收集——它配备搜索工具和数据组织能力

Each agent has its own independent “brain” (memory), “office” (workspace), and “work log” (session records), without any interference.

每个坐席都有自己独立的“大脑”（内存）、“办公室”（工作空间）和“工作日志”（会话记录），不受任何干扰。

> One person can be an army – provided you know how to arrange the troops.
> 
> 一个人可以成为一支军队——只要你知道如何安排军队。

## 2\. OpenClaw Multi-Agent Architecture Overview2.OpenClaw多代理架构概述

### 2.1 Architecture Core: Three-Layer Isolation2.1 架构核心：三层隔离

In OpenClaw, each agent isn’t just a name – it’s a

**

fully independent virtual employee

**

. Understanding this point is crucial:

在 OpenClaw 中，每个代理不仅仅是一个名字 - 它是一个完全独立的虚拟员工。理解这一点至关重要：

```fallback
~/.openclaw/agents/<agentId>/
├── agent/                    # Identity credentials
│   ├── auth-profiles.json    # Auth config (which API key to use)
│   └── models.json           # Model config (which model to use)
└── sessions/                 # Private journal
    ├── <session-id>.jsonl    # Independent chat history
    └── sessions.json         # Session index

~/.openclaw/workspace-<agentId>/
├── SOUL.md                   # Soul/personality definition
├── AGENTS.md                 # Agent behavior guidelines
├── USER.md                   # User information
├── PROMPT.md                 # Prompt templates
├── IDENTITY.md               # Identity definition
└── memory/                   # Memory storage
```

These three isolation layers correspond to:

这三个隔离层对应于：

| Layer  层 | Directory  目录 | Purpose  目的 | Analogy  类比 |
| --- | --- | --- | --- |
| **  Identity Layer  身份层  ** | `agents/<id>/agent/` | Determines which model and credentials to use  确定要使用的模型和凭据 | Employee badge  员工徽章 |
| **  State Layer  状态层  ** | `agents/<id>/sessions/` | Independent chat history and routing state  独立的聊天记录和路由状态 | Work journal  工作日记 |
| **  Workspace Layer  工作空间层  ** | `workspace-<id>/` | Independent files, prompts, and memory  独立的文件、提示、内存 | Personal office  个人办公室 |

The benefit of this isolation design is

**

physical-level context separation

**

. Your writing agent will never see the coding agent’s code files, and the coding agent won’t be distracted by the writing agent’s style guides.

这种隔离设计的好处是物理层面的上下文分离。您的写作代理永远不会看到编码代理的代码文件，并且编码代理不会因写作代理的风格指南而分心。

### 2.2 Route Binding: The Bindings Mechanism2.2 路由绑定：绑定机制

With independent agents in place, the next question is: when a message comes in, how does the system know which agent should handle it?

有了独立的代理，下一个问题是：当消息传入时，系统如何知道哪个代理应该处理它？

The answer is the

**

Bindings mechanism

**

– a set of deterministic routing rules. OpenClaw matches from highest to lowest priority:

答案是绑定机制——一组确定性路由规则。 OpenClaw 从最高优先级到最低优先级匹配：

```fallback
Priority 1: Exact peer match (DM/group ID)
Priority 2: Parent peer match (thread inheritance)
Priority 3: guildId + role (Discord-specific)
Priority 4: guildId standalone match
Priority 5: teamId (Slack-specific)
Priority 6: accountId match
Priority 7: Channel-level match
Priority 8: Default agent fallback
```

In simple terms:

**

the more specific the rule, the higher its priority

**

. If you assign a dedicated agent to a specific Feishu group, messages from that group will always route to that agent – no exceptions.

简单来说：规则越具体，其优先级越高。如果您将专用代理分配给特定的飞书群组，则来自该群组的消息将始终路由到该代理 – 无一例外。

Multi-condition bindings use

**

AND logic

**

– all conditions must be satisfied for a match. If multiple rules match at the same priority level, the

**

first one in the config file wins

**

.

多条件绑定使用 AND 逻辑 – 必须满足所有条件才能匹配。如果多个规则在同一优先级匹配，则配置文件中的第一个规则获胜。

### 2.3 Two Approaches: Clone Mode vs Independent Fleet2.3 两种方法：克隆模式与独立舰队

OpenClaw supports two multi-agent deployment approaches, each suited to different scenarios:

OpenClaw 支持两种多代理部署方法，每种方法适合不同的场景：

| Dimension  维度 | Clone Mode (Single Bot Routing)  克隆模式（单机器人路由） | Independent Fleet (Multiple Bots)  独立舰队（多个机器人） |
| --- | --- | --- |
| **  Implementation  实施  ** | One Feishu bot, routing to different agents via Bindings  一个飞书机器人，通过绑定路由到不同的代理 | Each agent has its own independent Feishu bot  每个代理都有自己独立的飞书机器人 |
| **  User Experience  用户体验  ** | Same bot appears in all groups, but “switches brains”  相同的机器人出现在所有组中，但“交换大脑” | Each bot has its own avatar and name  每个机器人都有自己的头像和名字 |
| **  Management Cost  管理成本  ** | Low, simple configuration  低配置、简单 | High, requires managing multiple bots  高，需要管理多个机器人 |
| **  Best For  最适合  ** | Personal use, efficiency-focused  个人使用，注重效率 | Team collaboration, role differentiation needed  团队协作，需要角色区分 |
| **  Reference PR  参考公关  ** | Supported by default  默认支持 | [  Feishu multi-bot PR #137  飞书多机器人 PR #137  ](https://github.com/m1heng/clawdbot-feishu/pull/137) |

For individual users,

**

Clone Mode is strongly recommended

**

– maximum flexibility with minimal configuration. This article focuses on this approach.

对于个人用户，强烈建议使用克隆模式——以最少的配置获得最大的灵活性。本文重点介绍这种方法。

## 3\. Hands-On Configuration: Building a Multi-Agent Team from Scratch3. 实践配置：从头开始构建多代理团队

### 3.1 Creating a New Agent3.1 创建新代理

Creating an isolated agent via the command line is straightforward:

通过命令行创建隔离代理非常简单：

```bash
# Create a writing agent named "writer" using the deepseek model
openclaw agents add writer \
  --model deepseek/deepseek-chat \
  --workspace ~/.openclaw/workspace-writer

# Create a brainstorming agent using glm-4.7
openclaw agents add brainstorm \
  --model zai/glm-4.7 \
  --workspace ~/.openclaw/workspace-brainstorm

# Create a coding agent using claude
openclaw agents add coder \
  --model anthropic/claude-sonnet-4-6 \
  --workspace ~/.openclaw/workspace-coder
```

Here’s a clever design detail:

**

different agents can use different models

**

. You can choose the most suitable “brain” based on task characteristics:

这里有一个巧妙的设计细节：不同的代理可以使用不同的模型。你可以根据任务特点选择最适合的“大脑”：

| Agent  代理 | Recommended Model  推荐型号 | Reason  原因 |
| --- | --- | --- |
| Brainstorm  头脑风暴 | glm-4.7  GLM-4.7 | Strong Chinese creative capabilities  强大的中国创造能力 |
| Writer  作家 | deepseek  深度搜索 | Great cost-effectiveness, stable logical output  性价比高，逻辑输出稳定 |
| Coder  编码员 | claude-sonnet  克劳德十四行诗 | Strong coding ability, deep understanding  编码能力强，理解深刻 |
| Researcher  研究员 | gpt-4o  GPT-4O | Good multimodal comprehension, suited for information synthesis  良好的多模态理解能力，适合信息合成 |

### 3.2 Giving Agents a Soul: Writing the “Onboarding Materials”3.2 赋予代理商灵魂：编写“入职材料”

Creating an agent only gives it a “body.” What truly makes it useful is its “soul files.”

创建一个代理只是给它一个“身体”。真正让它有用的是它的“灵魂文件”。

In each agent’s workspace directory, three core files need to be configured:

在每个代理的工作空间目录中，需要配置三个核心文件：

**SOUL.md**

– The agent’s personality definition:

SOUL.md – 特工的个性定义：

```markdown
# Writer Agent

## Role
You are an experienced content writing expert, skilled at dissecting
technology topics with sharp, authentic perspectives.

## Style
- Openings must use a compelling scene or counter-intuitive insight
- Paragraphs should be short and punchy, mobile-reading friendly
- Use analogies liberally so even a beginner can understand complex concepts
- Endings must include a call-to-action (CTA)

## Prohibitions
- Never use hollow phrases like "as everyone knows" or "it goes without saying"
- Don't stack jargon; explain every technical term on first appearance
```

**AGENTS.md**

– The agent’s behavior guidelines:

AGENTS.md – 代理的行为准则：

```markdown
# Work Guidelines

## Output Format
- All articles use Markdown format
- Heading levels should not exceed three (H2 > H3 > H4)
- Code blocks must specify the language type

## Workflow
1. Draft an outline first, then expand after confirmation
2. Keep each paragraph under 150 words
3. Self-check SEO elements after completion
```

**USER.md**

– User information:

USER.md – 用户信息：

```markdown
# User Information

## Identity
Blogger and tech content creator, focused on AI tools and productivity.

## Preferences
- Language style: Professional but not academic, with warmth
- Target readers: Tech enthusiasts and product managers interested in AI
- Publishing platforms: Blog + social media
```

> Writing “onboarding materials” for AI may sound surreal, but this is precisely what makes agent output stable and controllable.
> 
> **
> 
> The more carefully you define it, the more diligently it works.
> 
> **
> 
> 为人工智能编写“入职材料”可能听起来很超现实，但这正是使代理输出稳定可控的原因。 你定义得越仔细，它就越有效。

### 3.3 Setting Up Identity Markers3.3 设置身份标记

Give each agent a recognizable identity in chat groups:

为聊天组中的每个客服人员提供可识别的身份：

```bash
# Set display name and emoji for each agent
openclaw agents set-identity --agent writer --name "Writer" --emoji "✍️"
openclaw agents set-identity --agent brainstorm --name "Brainstormer" --emoji "💡"
openclaw agents set-identity --agent coder --name "Code Smith" --emoji "⚡"
```

### 3.4 Binding Message Channels 3.4 绑定消息通道

After creating agents, you need to bind them to specific message channels. OpenClaw supports multiple channels – here we’ll use

**

Feishu

**

and

**

Telegram

**

as examples.

创建代理后，您需要将它们绑定到特定的消息通道。 OpenClaw支持多种渠道，这里以飞书和Telegram为例。

#### Feishu Binding 飞书绑定

Create a dedicated group in Feishu for each agent and obtain the

**

group chat ID

**

(a string starting with

`oc_`

).

在飞书中为每个坐席创建一个专属群，并获取群聊ID（以 `oc_` 开头的字符串）。

Then configure the Bindings routing in

`openclaw.json`

:

然后在 `openclaw.json`:中配置Bindings路由。

```json
{
  "bindings": [
    {
      "agentId": "writer",
      "match": {
        "channel": "feishu",
        "peer": {
          "kind": "group",
          "id": "oc_abc123..."
        }
      }
    },
    {
      "agentId": "brainstorm",
      "match": {
        "channel": "feishu",
        "peer": {
          "kind": "group",
          "id": "oc_def456..."
        }
      }
    },
    {
      "agentId": "coder",
      "match": {
        "channel": "feishu",
        "peer": {
          "kind": "group",
          "id": "oc_ghi789..."
        }
      }
    }
  ]
}
```

**How it works**

: A single Feishu bot is added to three different groups. When messages come in from different groups, the Bindings mechanism routes them to the corresponding agent based on group ID. To the user, it looks like the same bot, but underneath it connects to completely different “brains.”

工作原理：将单个飞书机器人添加到三个不同的组中。当消息来自不同的组时，绑定机制根据组 ID 将它们路由到相应的代理。对于用户来说，它看起来像同一个机器人，但在它的下面连接着完全不同的“大脑”。

#### Telegram Binding 电报绑定

Telegram binding follows the same logic as Feishu, except

`channel`

becomes

`telegram`

and

`peer.id`

uses Telegram’s

**

Chat ID

**

(numeric format, typically negative for groups).

Telegram 绑定遵循与飞书相同的逻辑，只不过 `channel` 变为 `telegram` ，而 `peer.id` 使用 Telegram 的聊天 ID（数字格式，通常为负数）。

To get the Chat ID: add the bot to the group, then visit

`https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

and find the

`chat.id`

field in the returned JSON.

获取聊天ID：将机器人添加到群组，然后访问 `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` 并在返回的JSON中找到 `chat.id` 字段。

Configuration example:

配置示例：

```json
{
  "bindings": [
    {
      "agentId": "writer",
      "match": {
        "channel": "telegram",
        "peer": {
          "kind": "group",
          "id": "-1001234567890"
        }
      }
    },
    {
      "agentId": "coder",
      "match": {
        "channel": "telegram",
        "peer": {
          "kind": "group",
          "id": "-1009876543210"
        }
      }
    }
  ]
}
```

You also need to enable the Telegram channel in the

`channels`

section of

`openclaw.json`

:

您还需要在 `openclaw.json` 的 `channels` 部分启用 Telegram 频道。

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    }
  }
}
```

**Feishu vs Telegram Comparison**

:

飞书与 Telegram 对比：

| Dimension  维度 | Feishu  飞书 | Telegram  电报 |
| --- | --- | --- |
| **  peer.id Format  peer.id 格式  ** | String starting with  以 `oc_` 开头的字符串。  `oc_` | Numeric (negative for groups)  数字（组为负数） |
| **  Bot Creation  机器人创建  ** | Feishu Open Platform  飞书开放平台 | @BotFather  @BotFather |
| **  No-mention Mode  不提及模式  ** | Requires additional  `requireMention`  config  需要额外的 `requireMention` 配置。 | Set bot as group admin or use  `/`  commands  将机器人设置为组管理员或使用 `/` 命令。 |
| **  Best For  最适合  ** | Enterprise internal, team collaboration  企业内部、团队协作 | Personal use, cross-border communication  个人使用，跨境通讯 |

> You can absolutely
> 
> **
> 
> bind both channels simultaneously
> 
> **
> 
> – use Feishu groups for writing agents during daily work, and Telegram groups for coding agents to handle technical issues on the go. Multi-channel mixed usage is the true power of multi-agent architecture.
> 
> 你完全可以同时绑定两个渠道——在日常工作中使用飞书群来编写代理，使用 Telegram 群作为编码代理来处理旅途中的技术问题。多通道混合使用是多代理架构的真正威力。

### 3.5 Enabling No-Mention Mode 3.5 启用未提及模式

By default, the bot must be @mentioned in groups to trigger a response. If you want a group to become a “private office” with an agent, you can disable this restriction:

默认情况下，必须在组中@提及机器人才能触发响应。如果你想让一个群组成为一个有代理的“私人办公室”，你可以禁用这个限制：

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_a9f21xxxxx89bcd",
      "appSecret": "w6cPunaxxxxBl1HHtdF",
      "groups": {
        "oc_abc123...": { "requireMention": false },
        "oc_def456...": { "requireMention": false }
      }
    }
  }
}
```

You also need to enable the

`im:message.group_msg`

permission in the Feishu admin panel – both configurations must work together.

您还需要在飞书管理面板中启用 `im:message.group_msg` 权限 - 两种配置必须协同工作。

## 4\. Inter-Agent Communication: From Solo Work to Team Collaboration4. Agent间通信：从单独工作到团队协作

Setting up multiple agents is just the first step. The real value lies in making them

**

collaborate

**

– just like a company can’t function with employees who never communicate.

设置多个代理只是第一步。真正的价值在于让他们协作——就像公司无法与从不沟通的员工一起运作一样。

### 4.1 Core Mechanism: sessions\_send4.1 核心机制：sessions\_send

Inter-agent communication relies on OpenClaw’s built-in

`sessions_send`

tool. Think of it as an “internal phone line” between agents:

代理间通信依赖于 OpenClaw 的内置 `sessions_send` 工具。将其视为代理之间的“内部电话线”：

```fallback
User sends instruction → Supervisor Agent (main) receives
                ↓
         Determines task type
        ↙    ↓     ↘
  brainstorm  writer  coder
              ↓
        Collects results
                ↓
         Supervisor Agent returns to user
```

### 4.2 Configuring Agent-to-Agent Communication4.2 配置代理间通信

To make the “internal phone” work, you must explicitly enable permissions in the config file:

要使“内部电话”工作，您必须在配置文件中显式启用权限：

```json
{
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": ["main", "brainstorm", "writer", "coder"]
    }
  }
}
```

Key points:

要点：

- **
	Disabled by default
	**
	: Inter-agent communication must be explicitly enabled – this is a security-by-design choice
	默认禁用：必须显式启用代理间通信 - 这是设计安全性的选择
- **
	Allowlist mechanism
	**
	: The
	`allow`
	list explicitly defines which agents can communicate with each other
	白名单机制： `allow` 列表明确定义了哪些代理可以相互通信。
- **
	Principle of least privilege
	**
	: Not all agents need to communicate with each other – only enable it for the ones that need it
	最小权限原则：并非所有代理都需要相互通信 - 仅为需要的代理启用它

### 4.3 Designing the Supervisor Agent Role4.3 设计Supervisor代理角色

In my experience, the most effective pattern is setting up a

**

Supervisor Agent

**

(typically called

`main`

) whose job isn’t to do the work itself, but to receive and delegate tasks:

根据我的经验，最有效的模式是设置一个主管代理（通常称为 `main` ），其工作不是完成工作本身，而是接收和委派任务：

```markdown
# Main Agent - SOUL.md

## Role
You are the team's Chief Coordination Officer. Your core responsibilities:

1. **Receive requests**: Understand the user's original instruction
2. **Precise dispatch**: Determine task type and assign to the appropriate specialist agent
3. **Quality control**: Review specialist agent output, request revisions when needed
4. **End-to-end orchestration**: Ensure multi-step tasks don't drop the ball

## Dispatch Rules
- Brainstorming, creative divergence → @brainstorm
- Article writing, copy optimization → @writer
- Code writing, technical implementation → @coder
- Simple Q&A, casual chat → Handle yourself
```

The core significance of this design isn’t just division of labor – it’s

**

oversight and fault tolerance

**

: when a specialist agent gets stuck or errors out, the supervisor agent can intervene and ensure the process doesn’t break.

这种设计的核心意义不仅仅是分工，而是监督和容错：当专业代理陷入困境或出错时，主管代理可以进行干预并确保流程不会中断。

## 5\. Four Collaboration Patterns: A Deep Dive5. 四种协作模式：深入探讨

With the basics covered, let’s zoom out to the architecture level. Based on

[

LangChain’s multi-agent architecture research

](https://blog.langchain.com/choosing-the-right-multi-agent-architecture/)

and

[

Google’s eight design patterns

](https://www.infoq.com/news/2026/01/multi-agent-design-patterns/)

, mainstream multi-agent collaboration patterns can be grouped into four categories:

介绍完基础知识后，让我们关注架构级别。基于LangChain的多Agent架构研究和Google的八种设计模式，主流的多Agent协作模式可以分为四类：

### 5.1 Supervisor Pattern 5.1 主管模式

```fallback
┌─────────┐
   │  User    │
   │ Request  │
   └────┬────┘
        ↓
┌───────────────┐
│  Supervisor    │
│  (Main Agent)  │
└──┬─────┬───┬──┘
   ↓     ↓   ↓
┌───┐ ┌───┐ ┌───┐
│ A │ │ B │ │ C │
└───┘ └───┘ └───┘
   ↓     ↓   ↓
┌───────────────┐
│ Aggregate &   │
│    Output     │
└───────────────┘
```

**How it works**

: A central Supervisor receives all requests, breaks them into subtasks, assigns them to specialist agents, collects results, and produces consolidated output.

工作原理：中央主管接收所有请求，将其分解为子任务，将其分配给专家代理，收集结果并生成合并的输出。

**OpenClaw implementation**

: This is exactly the

`main`

agent pattern configured earlier. Through

`agentToAgent`

and

`sessions_send`

, the main agent can send instructions to any specialist agent and retrieve results.

OpenClaw 实现：这正是之前配置的 `main` 代理模式。通过 `agentToAgent` 和 `sessions_send` ，主代理可以向任何专业代理发送指令并检索结果。

**Best suited for**

:

最适合：

- Personal assistants needing a unified entry point
	个人助理需要统一的入口点
- Tasks requiring cross-domain collaboration (research first, then write, then format)
	需要跨领域协作的任务（先研究，然后编写，然后格式化）
- Scenarios needing quality oversight and result review
	需要质量监督和结果审核的场景

**OpenClaw configuration example**

:

OpenClaw配置示例：

```json
{
  "agents": {
    "list": [
      { "id": "main", "workspace": "~/.openclaw/workspace-main" },
      { "id": "writer", "workspace": "~/.openclaw/workspace-writer" },
      { "id": "coder", "workspace": "~/.openclaw/workspace-coder" }
    ]
  },
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": ["main", "writer", "coder"]
    }
  }
}
```

### 5.2 Router Pattern 5.2 路由器模式

```fallback
┌─────────┐
   │  User    │
   │ Request  │
   └────┬────┘
        ↓
┌───────────────┐
│    Router      │
│  (Dispatcher)  │
└──┬─────┬───┬──┘
   ↓     ↓   ↓      ← Parallel execution
┌───┐ ┌───┐ ┌───┐
│ A │ │ B │ │ C │
└───┘ └───┘ └───┘
   ↓     ↓   ↓
┌───────────────┐
│ Synthesize &  │
│    Output     │
└───────────────┘
```

**How it works**

: The Router classifies input and dispatches requests in parallel to multiple specialist agents, then synthesizes results for output. Routers are typically

**

stateless

**

.

工作原理：路由器对输入进行分类并将请求并行分派给多个专家代理，然后综合结果以进行输出。路由器通常是无状态的。

**Difference from Supervisor**

: The Supervisor does

**

sequential coordination

**

(do A, then B), while the Router does

**

parallel dispatch

**

(A and B simultaneously).

与 Supervisor 的区别：Supervisor 执行顺序协调（先执行 A，然后执行 B），而 Router 执行并行调度（同时执行 A 和 B）。

**OpenClaw implementation**

: Using the deterministic routing rules of Bindings, messages are automatically dispatched to the corresponding agent based on source (group/channel/user) – this is inherently the Router pattern.

OpenClaw 实现：使用 Bindings 的确定性路由规则，消息根据源（组/通道/用户）自动分派到相应的代理 - 这本质上是路由器模式。

**Best suited for**

:

最适合：

- Different channels needing different styles (Feishu in Chinese, Telegram in English)
	不同的渠道需要不同的风格（中文为飞书，英文为Telegram）
- Different user groups needing different expertise levels
	不同的用户群体需要不同的专业水平
- Fast response needed without cross-agent collaboration
	无需跨代理协作即可快速响应

### 5.3 Pipeline Pattern 5.3 管道模式

```fallback
┌─────────┐
│  User    │
│ Request  │
└────┬────┘
     ↓
┌──────────┐     ┌──────────┐     ┌──────────┐
│Researcher│ ──→ │  Writer  │ ──→ │ Reviewer │
└──────────┘     └──────────┘     └──────────┘
                                       ↓
                                 ┌──────────┐
                                 │  Final   │
                                 │  Output  │
                                 └──────────┘
```

**How it works**

: Tasks flow through agents like an assembly line. Each agent’s output becomes the next agent’s input.

工作原理：任务像装配线一样通过代理流动。每个智能体的输出成为下一个智能体的输入。

**OpenClaw implementation**

: Through

`sessions_send`

, the supervisor agent can orchestrate an execution chain: first have the research agent gather materials, pass the results to the writing agent for a draft, then hand it to the review agent for polishing.

OpenClaw实现：通过 `sessions_send` ，主管代理可以编排执行链：首先让研究代理收集材料，将结果传递给写作代理打草稿，然后交给审阅代理进行润色。

**Best suited for**

:

最适合：

- Content creation pipeline: research → draft → review → format
	内容创作流程：研究→草稿→审查→格式
- Code development pipeline: design → code → test → deploy
	代码开发流程：设计→代码→测试→部署
- Data processing pipeline: collect → clean → analyze → visualize
	数据处理流程：收集→清理→分析→可视化

**Practical example**

– A blog post production pipeline:

实际示例 - 博客文章制作流程：

```fallback
Step 1: @brainstorm "Brainstorm 5 topic ideas around AI coding productivity"
Step 2: After user picks a direction → @writer "Write an article based on: {brainstorm output}"
Step 3: After writing is done → @coder "Check if the code examples in the article are correct and runnable"
Step 4: Main agent consolidates all feedback and outputs the final version
```

### 5.4 Parallel Pattern 5.4 并行模式

```fallback
┌─────────┐
   │  User    │
   │ Request  │
   └────┬────┘
        ↓
┌──────────────┐
│ Task Splitter │
└──┬────┬────┬─┘
   ↓    ↓    ↓      ← Simultaneous execution
┌───┐ ┌───┐ ┌───┐
│ A │ │ B │ │ C │
└─┬─┘ └─┬─┘ └─┬─┘
  ↓     ↓     ↓
┌──────────────┐
│   Result     │
│  Aggregator  │
└──────────────┘
```

**How it works**

: A single task is split into multiple independent subtasks, processed by multiple agents simultaneously, with results aggregated at the end.

工作原理：单个任务被拆分为多个独立的子任务，由多个代理同时处理，最后汇总结果。

**Best suited for**

:

最适合：

- Competitive analysis: multiple agents researching different competitors simultaneously
	竞争分析：多个代理商同时研究不同的竞争对手
- Multi-angle review: having security, performance, and maintainability agents each review the same code
	多角度审查：让安全、性能和可维护性代理分别审查相同的代码
- Multi-language translation: translating the same content into multiple languages simultaneously
	多语言翻译：将相同内容同时翻译成多种语言

### 5.5 How to Choose the Right Pattern?5.5 如何选择正确的模式？

You don’t need to design a complex architecture from the start. According to

[

LangChain’s recommendation

](https://blog.langchain.com/choosing-the-right-multi-agent-architecture/)

, the optimal path is

**

progressive upgrade

**

:

您不需要从一开始就设计复杂的架构。根据浪链的建议，最优路径是渐进式升级：

```fallback
Single Agent + Tools
    ↓ (context contamination begins)
Single Agent + Skills
    ↓ (memory bloat, cost spiral)
Supervisor + 2-3 Specialist Agents
    ↓ (need more complex collaboration)
Pipeline / Parallel Hybrid Pattern
```

> **Core principle**
> 
> : Adding tools is preferable to adding agents. Only upgrade to multi-agent mode when you hit clear limitations.
> 
> 核心原则：添加工具胜于添加代理。仅当遇到明显限制时才升级到多代理模式。

## 6\. Production Environment Best Practices6. 生产环境最佳实践

### 6.1 Security Sandbox Configuration6.1 安全沙箱配置

Different agents should have different permissions. A writing agent doesn’t need code execution capabilities, and a research agent doesn’t need file write permissions:

不同的代理应该有不同的权限。写作代理不需要代码执行能力，研究代理不需要文件写入权限：

```json
{
  "agents": {
    "list": [
      {
        "id": "writer",
        "sandbox": { "mode": "all", "scope": "agent" },
        "tools": {
          "allow": ["read", "browser"],
          "deny": ["exec", "write"]
        }
      },
      {
        "id": "coder",
        "tools": {
          "allow": ["exec", "read", "write"],
          "deny": ["browser"]
        }
      }
    ]
  }
}
```

### 6.2 Flexible Model-Channel Pairing6.2 灵活的模型-通道配对

OpenClaw supports using different models across different channels, and even switching models for the same agent in different scenarios:

OpenClaw支持在不同渠道使用不同模型，甚至支持在不同场景下为同一代理切换模型：

| Channel  频道 | Recommended Model  推荐型号 | Reason  原因 |
| --- | --- | --- |
| Feishu (daily)  飞书（每日） | deepseek  深度搜索 | Cost-effective, fast response  高性价比、快速响应 |
| WhatsApp  WhatsApp | claude-sonnet  克劳德十四行诗 | Fast, accurate, mobile-friendly  快速、准确、适合移动设备 |
| Telegram (deep tasks)  Telegram（深度任务） | claude-opus  克劳德作品 | Deep thinking, suited for complex problems  深度思考，适合复杂问题 |

### 6.3 Skills Sharing Mechanism 6.3 技能共享机制

Multiple agents can share common skills while retaining their own specialized skills:

多个代理可以共享共同技能，同时保留自己的专业技能：

```gdscript3
~/.openclaw/skills/           # Globally shared skills
├── web-search/               # Search capability (shared by all agents)
├── file-tools/               # File operations (shared by all agents)
└── image-gen/                # Image generation (shared by all agents)

~/.openclaw/workspace-writer/skills/   # Writer-exclusive skills
├── seo-checker/              # SEO checking
└── article-template/         # Article templates

~/.openclaw/workspace-coder/skills/    # Coder-exclusive skills
├── code-review/              # Code review
└── test-runner/              # Test running
```

### 6.4 Monitoring and Debugging 6.4 监控与调试

Debugging a multi-agent system is more complex than a single agent. Recommendations:

调试多代理系统比调试单个代理更复杂。建议：

1. **
	Configure HEARTBEAT.md for each agent
	**
	: Periodically check whether agents are online and responding normally
	为每个代理配置HEARTBEAT.md：定期检查代理是否在线并正常响应
2. **
	Set log levels
	**
	: Enable detailed logging during development to observe inter-agent communication
	设置日志级别：在开发过程中启用详细日志记录以观察代理间通信
3. **
	Establish fallback mechanisms
	**
	: When a specialist agent is unresponsive, the supervisor agent should handle the task itself or notify the user
	建立后备机制：当专业代理无响应时，主管代理应自行处理任务或通知用户

## 7\. Common Questions and Pitfall Guide7. 常见问题和陷阱指南

### Q1: Are more agents always better?Q1：代理越多越好吗？

**No.**

Each additional agent increases communication overhead and management cost. My recommendations:

不会。每个额外的代理都会增加通信开销和管理成本。我的建议：

- **
	Personal use
	**
	: 3-5 agents are sufficient (supervisor + 2-4 specialists)
	个人使用：3-5名代理人就足够了（主管+2-4名专家）
- **
	Team use
	**
	: Divide by business line, 2-3 agents per line
	团队使用：按业务线划分，每线2-3名坐席
- **
	Key metric
	**
	: If two agents’ conversations are 80%+ the same task type, consider merging them
	关键指标：如果两个代理的对话 80% 以上是相同的任务类型，请考虑将它们合并

### Q2: Does inter-agent communication consume extra tokens?Q2：代理间通信是否会消耗额外的代币？

**Yes.**

Every

`sessions_send`

is an API call. Ways to reduce unnecessary communication:

是的。 每个 `sessions_send` 都是一个 API 调用。减少不必要沟通的方法：

- Have the supervisor agent assess task complexity first; handle simple tasks directly
	让主管代理首先评估任务复杂性；直接处理简单的任务
- Use
	[
	token optimization strategies
	](https://www.heyuan110.com/posts/ai/2026-02-14-openclaw-automation-pitfalls/)
	to reduce context length per communication
	使用令牌优化策略来减少每次通信的上下文长度
- Assign lighter-weight models to sub-agents
	将轻量级模型分配给子代理

### Q3: How to handle “understanding gaps” between agents?Q3：如何处理代理商之间的“理解差距”？

When Agent A’s output is handed to Agent B, misinterpretation can occur. Solutions:

当代理 A 的输出交给代理 B 时，可能会发生误解。解决方案：

- **
	Structured communication
	**
	: Pass structured JSON data between agents instead of free-form text
	结构化通信：在代理之间传递结构化 JSON 数据而不是自由格式文本
- **
	Templated instructions
	**
	: The supervisor agent uses standardized instruction templates to dispatch sub-agents
	模板化指令：主管座席使用标准化指令模板来调度子座席
- **
	Validation checkpoints
	**
	: Add review steps at critical points
	验证检查点：在关键点添加审核步骤

### Q4: Can agents collaborate across platforms?Q4：代理商可以跨平台协作吗？

**Absolutely.**

OpenClaw isn’t limited to Feishu – it supports Telegram, Discord, WhatsApp, and more. You can even have a Feishu group agent and a Telegram agent collaborate through

`sessions_send`

.

绝对地。 OpenClaw 不仅限于飞书 - 它支持 Telegram、Discord、WhatsApp 等。您甚至可以通过 `sessions_send` 让飞书群代理和Telegram代理协作..

## Conclusion

Multi-agent architecture isn’t some arcane technology. Its core philosophy is identical to managing a company:

1. **
	Hire the right people
	**
	(create appropriate agents, choose the right models)
2. **
	Divide responsibilities clearly
	**
	(write soul files, define role boundaries)
3. **
	Build communication channels
	**
	(configure routing bindings and inter-agent communication)
4. **
	Establish oversight
	**
	(set up a supervisor agent, build quality control)

Starting today, you no longer need an “omniscient but error-prone” AI assistant. What you need is a team of specialized, efficiently collaborating

**

AI agents

**

.

One final rule of thumb:

**

if you find yourself telling the AI “ignore that, focus on this,” it’s time to split into multiple agents

**

.

## Further Reading

- [
	OpenClaw Detailed Setup Tutorial: Beginner-Friendly with Pro Tips
	](https://www.heyuan110.com/posts/ai/2026-02-12-openclaw-usage-tutorial/)
- [
	Deconstructing OpenClaw’s Automation Architecture: The Complete Message-to-Execution Pipeline
	](https://www.heyuan110.com/posts/ai/2026-02-14-openclaw-architecture-deep-dive/)
- [
	OpenClaw Automation Pitfalls: Installing 3 Skills Doesn’t Mean They Actually Work
	](https://www.heyuan110.com/posts/ai/2026-02-14-openclaw-automation-pitfalls/)
- [
	OpenClaw Memory Strategy Analysis: Tool-Driven RAG and “On-Demand Recall”
	](https://www.heyuan110.com/posts/ai/2026-01-31-openclaw-memory-strategy/)
- [
	Claude Code Agent Teams Complete Guide: Multi-Agent Collaborative Development in Practice
	](https://www.heyuan110.com/posts/ai/2026-02-22-claude-code-agent-teams/)
- [
	Agent Skills: The Era of Programming in Plain Language
	](https://www.heyuan110.com/posts/ai/2026-01-19-agent-skills-new-programming/)

## Related Reading

- [
	OpenClaw vs CrewAI vs AutoGPT 2026: 6 AI Agent Frameworks Compared
	](https://www.heyuan110.com/posts/ai/2026-03-05-openclaw-vs-ai-agents/)
	— How OpenClaw multi-agent compares to other frameworks
- [
	OpenClaw Multi-Agent Setup: Build AI Teams That Work
	](https://www.heyuan110.com/posts/ai/2026-03-05-openclaw-multi-agent-setup/)
	— Practical setup guide for multi-agent configurations
- [
	Multi-Agent Orchestration: 4 Patterns That Actually Work
	](https://www.heyuan110.com/posts/ai/2026-02-26-multi-agent-orchestration/)
	— Design patterns for coordinating multiple agents
- [
	OpenClaw Memory Strategy: Tool-Driven RAG and On-Demand Recall
	](https://www.heyuan110.com/posts/ai/2026-01-31-openclaw-memory-strategy/)
	— How agents share and retrieve knowledge
- [
	OpenClaw 2026.3.1: WebSocket Streaming, Agent Routing, and K8s Support
	](https://www.heyuan110.com/posts/ai/2026-03-03-openclaw-2026-3-1-new-features/)
	— Latest features that enhance multi-agent support
