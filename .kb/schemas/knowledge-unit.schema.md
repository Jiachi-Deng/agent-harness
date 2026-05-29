# Knowledge Unit Schema

这个 schema 规定 `.kb/atoms/*.jsonl` 中每条 knowledge unit 的推荐字段。第一版强调可维护性，不追求一次性做成数据库本体论。

## JSONL 约定

- 每行是一条完整 JSON object。
- 不要在 JSONL 中写注释。
- 中文为主，技术名词可保留英文。
- `id` 一旦被 Wiki / Outputs 引用，默认不改名；需要改名时用 `aliases` 和 `replaces` 过渡。

## 必填字段

```json
{
  "id": "VC-DEBUG-TIP-001",
  "title": "调试时提供证据，而不是只描述坏了",
  "grain": "atom",
  "type": "micro_tip",
  "canonical_statement": "当 AI coding 项目出现 bug 时，用户不应只描述坏了，而应提供 console 日志、截图、完整报错、复现步骤和最近改动。",
  "status": "canonical",
  "confidence": "high",
  "freshness_risk": "low",
  "last_reviewed_at": "2026-05-29"
}
```

## 字段说明

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | yes | 稳定 ID。建议格式：`VC-<DOMAIN>-<TYPE>-<NNN>`。 |
| `title` | yes | 人类可读标题。 |
| `aliases` | no | 同义标题、旧标题、用户常见问法。 |
| `grain` | yes | `atom` / `block` / `module_ref`。 |
| `type` | yes | 单元类型，见下方枚举。 |
| `canonical_statement` | yes | 标准表达。要具体、可执行、有边界。 |
| `why_it_matters` | no | 为什么重要。 |
| `action` | no | 用户可执行动作。可为数组或短段落。 |
| `failure_if_ignored` | no | 忽略后会发生什么。 |
| `applies_to` | no | 适用 domain、stage、audience、tools、project_type。 |
| `not_for` | no | 不适用场景。 |
| `source_spans` | no | 来源锚点，至少包含 path / section / source_id 中的一个。 |
| `used_in` | no | 引用它的 Wiki / Outputs。 |
| `relations` | no | 与其他 unit 的 typed relations。 |
| `children` | no | `block` 包含的子 units。 |
| `parent` | no | 所属 block / module。 |
| `prompt_pattern` | no | 如果该 unit 可转成 prompt pattern，放结构而不是整段魔法咒语。 |
| `verification` | no | 实测记录摘要。详细记录可进入 `.kb/verification/`。 |
| `status` | yes | `candidate` / `canonical` / `variant` / `evidence` / `contradiction` / `deprecated`。 |
| `confidence` | yes | `low` / `medium` / `high`。 |
| `freshness_risk` | yes | `low` / `medium` / `high`。 |
| `last_reviewed_at` | yes | 最近人工或 AI 审查日期。 |
| `next_review_after` | no | 强时效 unit 的建议复查日期。 |

## grain 枚举

| grain | 说明 |
|---|---|
| `atom` | 最小行为改变单元。一个 action、rule、pitfall、tip、claim 或 checklist item。 |
| `block` | 多个 atoms 组成的 workflow、checklist、method family、playbook、pattern。 |
| `module_ref` | 指向 Wiki 页面的人类可读模块引用，通常只放 path、title、role 和上游 units。 |

## type 枚举

第一版建议使用这些类型：

- `concept`
- `mental_model`
- `principle`
- `decision_rule`
- `workflow`
- `step`
- `checklist`
- `checklist_item`
- `micro_tip`
- `pitfall`
- `anti_pattern`
- `troubleshooting`
- `prompt_pattern`
- `ui_knowledge`
- `version_change`
- `method_family`
- `case_pattern`
- `evidence`
- `opinion`
- `module_ref`

## relation 类型

推荐先使用这些 typed relations：

- `part_of`
- `contains`
- `requires`
- `prerequisite_of`
- `enables`
- `prevents`
- `solves`
- `causes`
- `variant_of`
- `same_as`
- `near_duplicate_of`
- `contradicts`
- `updates`
- `replaces`
- `evidence_for`
- `evidence_against`
- `used_in`
- `applies_to`

## 好 unit 的判断标准

一个合格 unit 至少能回答：

1. 它是什么？
2. 什么时候用？
3. 谁适合用？
4. 怎么做？
5. 为什么重要？
6. 不这么做会怎样？
7. 它来自哪里，是否还有效？

如果只剩“合理规划项目结构”“善用 AI 提高效率”这种抽象句，应该拆分或丢弃。
