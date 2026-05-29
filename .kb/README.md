# Knowledge Unit Ledger

`.kb/` 是这个 vault 的机器可读知识单元层。它不替代 `Wiki/`，也不替代 `Raw/` / `Clippings/`。

它的作用是把已经进入 Wiki 的高价值经验、坑点、判断规则、工作流和 checklist 拆成可追踪、可去重、可合并、可检索、可服务 AI Tutor 的结构化单元。

一句话：

> `Wiki/` 负责让人读懂，`.kb/` 负责让机器准确调用。

## 和现有流程的关系

现有主流程保持不变：

```text
Raw / Clippings -> Wiki -> Outputs
```

新增知识单元层以后，推荐流程升级为：

```text
Raw / Clippings
  -> source segments
  -> knowledge unit candidates
  -> merge / variant / contradiction check
  -> Wiki modules
  -> Outputs
  -> AI Tutor / Website serving index
```

其中：

- `Raw/` 和 `Clippings/` 仍然是 source of truth，不改写原文。
- `Wiki/` 仍然是主题知识层，负责叙事、综合、路线图、主页面和本库判断。
- `Outputs/` 仍然是交付层，负责教程、SOP、课程、prompt 卡片和案例拆解。
- `.kb/` 是 ledger，不是文章层，也不是正式交付层。

## 目录建议

```text
.kb/
  README.md
  schemas/
    knowledge-unit.schema.md
  templates/
    knowledge-unit.json
    source-segment.json
    coverage-entry.json
  atoms/
    vibe-coding.seed.jsonl
  relations/
    vibe-coding.seed.jsonl
  coverage/
    vibe-coding.seed-coverage.jsonl
  verification/
    .gitkeep
  exports/
    .gitkeep
```

## 三种核心粒度

第一阶段只区分三种粒度，避免过度工程：

| 粒度 | 说明 | 例子 |
|---|---|---|
| `atom` | 最小行为改变单元。能独立改变用户操作、判断或检查动作。 | 调试时给 AI console、截图、日志和复现步骤。 |
| `block` | 由多个 atoms 组成的可复用方法块、清单、workflow、playbook 或 method family。 | Vibe Coding 上线前安全审计 5 项。 |
| `module_ref` | 指向 Wiki 里的完整人类可读模块页。通常不在 `.kb/` 里重写全文。 | `Vibe Coding全栈SaaS开发闭环.md`。 |

一个块状经验不需要被打碎消灭。它可以作为 `block` 保存，同时用 `contains` 指向子 atoms。

## 什么时候应该创建 unit

凡是满足下面任意条件，都应该考虑抽成 knowledge unit：

- 会改变用户行为。
- 用户不知道会明显踩坑。
- 能被多个 Wiki 页面或 Outputs 复用。
- 是一个判断规则、反模式、流程、清单项、prompt pattern 或排错线索。
- 有版本风险，需要单独标记 `freshness_risk`。
- 有证据冲突，需要单独记录 `contradicts` 或 `variant_of`。
- 是作者顺口提到但很实用的小 tip。

不要为纯百科定义、泛泛励志句、低信息密度标题党观点创建 unit。

## 单元生命周期

```text
candidate
  -> duplicate_check
  -> canonical / variant / evidence / contradiction / deprecated
  -> used_in Wiki modules
  -> verified / needs_refresh / superseded
```

每个新 unit 进入前必须先问：

1. 这个知识是否已经存在？
2. 它是旧 unit 的同义表达、变体、证据、反例，还是新知识？
3. 它应该更新哪个 Wiki 页面？
4. 它是否影响已有 Outputs？
5. 它的来源和证据跨度是什么？

## 数据库关系

现在不要求立刻上数据库。

第一阶段：

```text
Markdown + JSONL + Git + Obsidian
```

产品化阶段再同步到：

```text
PostgreSQL + pgvector + full-text search
```

Redis 可以作为缓存、队列、限流或短期会话层，不建议作为长期知识主库。

## 当前状态

本次改动只建立第一版骨架和 Vibe Coding seed units。下一步应从 3 个现有页面反向抽取 50 到 100 条 canonical units：

- `Wiki/Vibe Coding/10-Getting Started/Codex新手Vibe Coding工作流.md`
- `Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环.md`
- `Wiki/Vibe Coding/30-Launch Safety/Vibe Coding安全审计清单.md`
