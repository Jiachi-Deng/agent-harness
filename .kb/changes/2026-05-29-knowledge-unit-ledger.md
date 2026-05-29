# 2026-05-29 — Knowledge Unit Ledger 初版

## 本次变更

建立 `.kb/` 作为机器可读的 Knowledge Unit Ledger，用于承接 Wiki 中高价值经验、坑点、判断规则、workflow、checklist 和 prompt pattern 的结构化沉淀。

这次没有推翻现有 Karpathy 风格 `Raw / Clippings -> Wiki -> Outputs` 流程，而是在它下面新增一层可计算结构：

```text
Raw / Clippings
  -> source segments
  -> knowledge unit candidates
  -> merge / variant / contradiction check
  -> Wiki modules
  -> Outputs
  -> AI Tutor / Website serving index
```

## 新增文件

- `.kb/README.md`
- `.kb/schemas/knowledge-unit.schema.md`
- `.kb/templates/knowledge-unit.json`
- `.kb/templates/source-segment.json`
- `.kb/templates/coverage-entry.json`
- `.kb/atoms/vibe-coding.seed.jsonl`
- `.kb/relations/vibe-coding.seed.jsonl`
- `.kb/coverage/vibe-coding.seed-coverage.jsonl`
- `.kb/verification/.gitkeep`
- `.kb/exports/.gitkeep`

## AGENTS.md 更新

`AGENTS.md` 已补入：

- `.kb/` 的目录角色。
- Knowledge Unit Ledger 规则。
- `atom / block / module_ref` 三种核心粒度。
- unit 生命周期：`candidate -> duplicate_check -> canonical / variant / evidence / contradiction / deprecated`。
- 合并、变体、冲突和 evidence 的处理规则。
- coverage 审计状态。
- Wiki / Outputs / `.kb` 的新默认工作流。
- 编译纪律中关于“不要把抽象句当成合格 unit”的要求。

## Vibe Coding seed units

本次先从现有 Vibe Coding 页面反向抽出第一批 canonical seed units，覆盖：

- 调试证据闭环。
- 项目 brief / issue 化。
- 上下文文件化和 compaction。
- 小步构建与测试。
- 生产环境变量。
- Worktrees / Automations / 多代理并行。
- 上线前安全审计 5 项。
- 安全审计 prompt 的结构化用法。
- Agent-friendly 技术栈。
- App + Skill + Database + Automation 的产品结构。
- Vibe Coding 全栈 SaaS 闭环。

## 下一步建议

1. 从 `Codex新手Vibe Coding工作流`、`Vibe Coding全栈SaaS开发闭环`、`Vibe Coding安全审计清单` 继续补齐 50-100 条 canonical units。
2. 补 `Codex 扩展能力分类` block：Plugins / Computer Use / Skills / MCP / Subagents。
3. 补安全加强项 atoms：rate limiting、CORS、文件上传服务端校验、service role 边界。
4. 给后续新教程编译增加 coverage 记录，避免小 tips 被平均摘要吞掉。
5. 网站 / AI Tutor 产品化前，再将 `.kb/*.jsonl` 同步到 PostgreSQL + pgvector。
