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

本仓库提供两个互补的材料基准技能：

- `materials-benchmark-review`：先审题目/答案正确性并给出 `BASELINE_CORRECT`，再可选评估 `RESULT_ENHANCED`；checker 成本是独立发布门槛，不让高级 hacking 风险反向否决正确题包。
- `materials-benchmark-repair`：Stage A 先修到独立复审的 Baseline；Stage B 才能增加轻量结果关系、分层评分和按实际风险选择的探针。增强失败回退 Baseline。

现行 v3.3 流程和五类案例见 [`output/pdf/materials-benchmark-v3-five-case-study/jiedu.pdf`](output/pdf/materials-benchmark-v3-five-case-study/jiedu.pdf)。

语料进度只由 `materials_science_questions/corpus_review_tracking.json` 记录并由人工 prompt 协调；仓库不提供第二套 lifecycle/orchestration dispatcher。

开始审查或修复题包前，请先阅读 `AGENTS.md`，再阅读 `CONTEXT.md`。
