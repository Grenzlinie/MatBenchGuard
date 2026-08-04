---
name: materials-benchmark-repair
description: 根据 v3.3 Review 分两阶段修复论文型材料科学题包：Stage A 先得到 BASELINE_CORRECT，独立复审后 Stage B 才可做轻量结果增强；保持论文 Gold 中心，限制 checker 成本；保留题包中的 Harbor Oracle full-score fixture solution/，但完全不检查或修复它。
---

# 材料科学题包 Repair（Baseline First）

## 固定工作流

```text
source
  -> Stage A BASELINE_CORRECTNESS
  -> independent Review: BASELINE_CORRECT
  -> optional Stage B RESULT_ENHANCEMENT
  -> checker cost acceptance
  -> independent Review
  -> publish enhanced, or fall back to baseline
```

完整题包中的 `solution/` 必须随 source 复制并保留在 candidate 中，但 Repair 将它视为不透明的 Oracle full-score fixture：不得读取、运行、扫描、哈希、引用、修改、删除或重建，也不得把任何 `solution/**` 路径写入 finding、change 或 evidence。该 fixture 的满分不代表真实科学执行。Repair 不负责判断其缺失、正确性或质量；若 Authoring/Harbor Oracle 报告 solution 问题，应路由回 Authoring，而不是在 Repair 中处理。源题包不可变；candidate、Review、Repair、evidence 都在题包外。必须先改 `instruction.md`，再同步派生文件，最后改 tests。

## 必读资料

- Review 的 [题包角色](../materials-benchmark-review/references/harbor-package-contract.md)
- Review 的 [正确性门槛](../materials-benchmark-review/references/correctness-gates.md)
- Review 的 [最小结果检查](../materials-benchmark-review/references/hidden-checkpoints.md)
- [科学评分与容差设计](references/scientific-scoring-and-tolerance-design.md)
- [Repair/Reauthor 工作流](references/repair-and-reauthor.md)

## processing 结构

```text
<processing>/<cluster>/<theme>/<paper>/
├── source_review/
├── baseline/
│   ├── candidate/
│   ├── evidence/
│   ├── candidate_core_review.json
│   └── core_repair.json
└── enhancement/
    ├── candidate/
    ├── evidence/
    ├── candidate_core_review.json
    └── core_repair.json
```

发布库只保存当前最佳 candidate。增强失败、超预算或损害 Baseline 时回退 `baseline/candidate`。

## Stage A：`BASELINE_CORRECTNESS`

负责：

- 补回论文已给的问题、方法、公式、参数和必要 Workflow；
- 修复跨步骤参数冲突、producer/consumer 断裂和派生文件不一致；
- 按 Review 四类参数分类；将论文未给但可扫描/优化/收敛/论证的项标成 `SOLVER_SEARCHABLE`，不补值；
- 删除 tests 中对该类参数的猜测唯一值；
- 对缺失的不可替代数据、模型、势、特定原子构型/结构快照或特定代码 fail closed；普通论文建模描述不因缺少 CIF 失败；
- 修复 Gold、条件组映射、容差和全部核心输出覆盖；
- 用五类 Baseline probe 验证正确答案通过、明显错误失败；
- 获得独立 Review 的 `PASS + BASELINE_CORRECT`。

允许动作包括 `RESTORE_PAPER_BACKED_CONTENT`、`FIX_PARAMETER_CONFLICT`、`RESTORE_WORKFLOW_DEPENDENCY`、`MARK_SOLVER_SEARCHABLE`、`REMOVE_GUESSED_EXECUTION_PARAMETER`、`FIX_GOLD_APPLICABILITY`、`FIX_CONDITION_GROUP_COVERAGE`、`FIX_TOLERANCE`、`FIX_CHECKER`、`SYNC_DERIVED`。

不得移动 paper Gold 中心、猜补论文未报告执行值或把不可替代资产伪装成参数搜索。solver 合法差异优先用合理容差吸收。论文必要内容完整后若仍为纯提取/纯代数，原题拒绝；不能删公式来制造难度。

结构修复时先问“是否必须复现同一个原子级 realization”。若论文只给成分、晶系/空间群、晶格参数或建模方法，补齐这些论文信息，把其余构型生成/弛豫选择标为 `SOLVER_SEARCHABLE`，不得虚构 CIF 或因此拒绝。只有 Gold/checker 必须绑定不可重建的固定快照时，才要求结构资源；若 checker 暗中绑定未公开结构，优先修 checker/容差/评分关系。

## Stage B：`RESULT_ENHANCEMENT`

输入必须是独立 Review 已确认可发布的 `BASELINE_CORRECT` candidate。

允许：

- 从已有最终输出重算廉价派生量；
- 检查关系、不变量、守恒量、残差、排序和跨文件一致性；
- 曲线少量代表点或轻量摘要；
- Gold 60--80%、结果检查 20--40% 的分层权重；
- 按实际风险增加最小 probe。

禁止：

- 修改科学目标、论文 Gold 中心或 Baseline 正确性；
- 删除论文必要参数、公式或 Workflow step；
- 固定 `SOLVER_SEARCHABLE` 参数；
- checker 重跑完整 DFT/MD/训练/大规模搜索；
- 读取或逐帧比较完整大体积 MD trajectory；
- 新增超过 32 CPU 核、单 GPU（型号必记且能力不超过 H100）或 600 秒的检查。

如果没有低成本、非任意 checkpoint，记录 `NO_AFFORDABLE_RESULT_CHECK`，发布 Baseline。Stage B 失败的 outcome 是 `ROLLED_BACK`，不能覆盖 Baseline。

## 容差与离线 Gold

容差依次使用论文不确定度/精度、可审计数字化、独立复算、收敛、跨实现或明确 reviewer 理由。必须保存 `T-epsilon/T/T+epsilon` 边界证据，Gold 中心不变。

昂贵 reference 可在 checker 之外离线生成并保存 provenance；运行时只读隐藏 reference 和 solver 最终输出。离线 reference 仍须由论文公式、同一条件和独立实现支撑，不能把旧 checker 输出自证为真。

## Regression evidence

每个 finding 都要绑定具体 change、typed evidence 和 regression。Stage A 使用真实 `FAIL_BEFORE_PASS_AFTER` 闭包，并至少覆盖 correct positive、tolerance boundary、missing/malformed、non-finite/duplicate、wrong-science。Stage B 的 Baseline 本来就正确，必须记录 `QUALITY_GRADIENT`（Baseline 与 Enhanced 对同一缺陷结果的 reward 关系），不得虚构 fail-before/pass-after。

性能证据必须来自真实规模输出；空文件/微型 fixture 不能证明 `checker_cost_record`。

不要求 Harbor+Codex 端到端。

## 验证与发布

复制 [core_repair_template.json](assets/core_repair_template.json)，运行：

```bash
python .cursor/skills/materials-benchmark-repair/scripts/validate_core_repair.py <processing>/core_repair.json --verify-files
```

outcome：`BASELINE_REPAIRED`、`RESULT_ENHANCED`、`BLOCKED`、`ROLLED_BACK`。发布时明确说明题目/答案正确性、参数与 Workflow、Gold/容差、checker 成本、独立 Review，以及是否只是 Baseline。
