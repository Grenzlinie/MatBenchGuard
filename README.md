# 材料科学基准质量保障

本仓库包含用于审查和修复 Harbor 格式材料科学基准题包的质量保障规范、测试与参考资料。

## 目录结构

- `CONTEXT.md`：领域术语与审查政策的权威定义。
- `AGENTS.md`：在本仓库中工作的 Agent 操作说明。
- `docs/agents/`：Issue 跟踪、分诊标签和领域文档规范。
- `tests/`：审查与修复政策的仓库级测试。
- `references/`：参考技能、报告模板与辅助说明。
- `materials_science_questions/`：本地材料科学 Harbor 格式题包及审阅结果语料。

## 本地题包语料

`materials_science_questions/` 有意不纳入 Git：其中保存本地题包语料与审阅产物。已跟踪的 `.gitkeep` 文件用于在克隆仓库后保留空目录；不得将该目录中的题包或审阅结果加入 Git。

在检出的工作区中，Agent 可以读取该目录。由于它被 Git 忽略，需要显式检索：

```bash
rg --no-ignore --files materials_science_questions
```

## 工作约定

- 将每个 `paper-{id}/` 目录视为独立的 Harbor 题包和审计单元。
- 在报告、Issue、测试和修复产物中，使用 `CONTEXT.md` 定义的术语和判定规则。
- 审计、修复、候选和证据产物必须放在原始 Harbor 题包之外。
- 保留原始题包；修复应在隔离副本中进行，且仅在相关回归测试和复审通过后发布。

## 材料基准技能

本仓库提供以下三个互补的材料基准技能：

- `materials-benchmark-review`：面向单个 Harbor 材料题包的审查技能。它结合论文核验、科学有效性、任务说明完整性、评分器覆盖与区分度、Gold 可信度、资源可用性以及安全性检查，形成有证据支撑的审查结论。
- `materials-benchmark-repair`：面向已确认缺陷的修复技能。它依据审查证据在隔离副本中实施不改变核心科学契约的修复，保留修复前后回归证据，并以同等深度复审决定是否可以发布修复后的题包。
- `materials-benchmark-orchestration`：面向大型题包集合的编排技能，用于协调多个工作者并行执行审查与修复。使用时仍须遵守本仓库的人工协调和语料跟踪约定，不将调度状态、审计结果或修复产物写入原始 Harbor 题包。

开始审查或修复题包前，请先阅读 `AGENTS.md`，再阅读 `CONTEXT.md`。
