---
name: materials-benchmark-review
description: 审核论文型材料科学 Harbor 题包。先判计算科学准入，再分别审查题目/答案正确性、可选结果增强和 checker 资源成本；固定 /app/outputs，solution/ 完全排除。
---

# 材料科学题包 Review（Baseline First）

## 唯一判定顺序

1. 题面是否把论文研究问题抽成自包含的计算科学问题；
2. 题目、方法、论文能给出的参数和必要 Workflow 是否忠于 `paper.md`；
3. Gold/关系及其条件映射是否来自论文或唯一推导，正确答案能否被合理接受；
4. checker 是否在最多 32 CPU 核或单 GPU、10 分钟内完成轻量结果检查；GPU 型号必须记录，能力上限按单卡 H100；
5. 最后才评估 checkpoint、分层评分和附加抗 hacking。

高级 hacking 风险不影响 `BASELINE_CORRECT`。增强失败只能降级，不能把题目和答案都正确的题包改判为科学失败。

`solution/` 完全排除：不得读取、运行、哈希、扫描或引用。

## 必读资料

- [Harbor 题包与文件角色](references/harbor-package-contract.md)
- [正确性门槛](references/correctness-gates.md)
- [最小结果检查](references/hidden-checkpoints.md)
- [检查责任矩阵](references/check-responsibility-matrix.md)
- 写题面时使用 [instruction 模板](assets/instruction_template.md)

本 Skill、上述 references、`core_review_template.json` 和 validator 是唯一现行规则。

## 文件角色

```text
paper/paper.md -> instruction.md -> steps/manifest/task/resources
       |               |
       +-> Gold/关系   +-> 公开输出合同 -> tests
```

- `instruction.md` 是唯一 solver-visible 题面；必须通过“拿走论文测试”。
- 题面不是“读原文并复述”，不得写“查看 Fig./Table/Section/paper.md”。
- `tests/` 可隐藏 Gold、精确容差和实现，不能隐藏提交要求。
- 所有提交位于 `/app/outputs`。

## Phase 0：Q0 计算科学准入

以下核心被评分工作直接 `REJECTED`：

- `PURE_INFORMATION_EXTRACTION`
- `PURE_ALGEBRAIC_COMPUTATION`
- `EXPERIMENTAL_OPERATION_REQUIRED`
- `TRIVIAL_EXPERIMENTAL_DATA_REDUCTION`

模型选择、收敛、优化、结构/轨迹分析、非平凡拟合、误差分析、候选比较和机理判断可以通过。题目必须可用计算机复现，不要求实际实验操作。

## Phase 1：题目正确性与参数分类

逐项建立 `parameter_records`：

| `parameter_class` | 含义 | 合法 `selection_policy` |
|---|---|---|
| `PAPER_FIXED` | 论文已报告、题面必须保留 | `PAPER_VALUE` |
| `SOLVER_SEARCHABLE` | 论文未给唯一值，可扫描、优化、收敛或论证 | `MESH_SEARCH` / `CONVERGENCE` / `OPTIMIZATION` / `SOLVER_JUSTIFIED` |
| `TARGET_DEFINING` | 决定体系、物理状态或研究条件 | 通常 `PAPER_VALUE` |
| `INDISPENSABLE_ASSET` | 不可由论文描述或合理建模重建的数据集、模型、势、特定原子构型/结构快照、特定代码等输入 | `RESOURCE` |

每条还必须记录：

```json
{
  "paper_reports_unique_value": false,
  "instruction_requires_unique_value": false,
  "checker_requires_unique_value": false
}
```

规则：

- 论文已给且与任务相关的参数、公式、方法、信息和必要步骤必须保留或补齐。
- `SOLVER_SEARCHABLE` 即使结果敏感，也不得因论文没有唯一值而失败；checker 不能暗中固定它。
- `INDISPENSABLE_ASSET` 无交付、链接、运行时供给或合法替代时失败；不可把资产伪装成“可搜索参数”。
- `TARGET_DEFINING` 缺失后无法辨明体系或条件时失败。
- 建立 `parameter_conflicts` 与 `workflow_continuity`；跨步骤值、单位、符号、作用域和 producer/consumer 必须一致。
- 论文必要步骤不能为了减少引导而删。只删重复说明或非必要 solution recipe；若完整保留后仍是纯提取/纯代数，回到 Q0 拒绝。

多条件组必须逐组绑定完整 condition signature、公开行/键、Gold 和容差；不能缩成“任选一组”。

### 结构输入的专门判定

没有 CIF/POSCAR/结构文件本身不构成失败。多数论文只报告成分、晶系/空间群、晶格常数、Wyckoff 信息、超胞/缺陷/界面构造方法或弛豫流程；只要这些是论文实际给出的全部结构定义，题面完整保留后，solver 可据此建模、优化或论证合理构型：

- 成分、晶系、空间群、晶格参数和论文构造规则属于 `TARGET_DEFINING` 或 `PAPER_FIXED`；
- 未唯一规定的原子放置、超胞实现、表面终止、缺陷位置、初始扰动和预弛豫选择通常属于 `SOLVER_SEARCHABLE/SOLVER_JUSTIFIED` 或 `OPTIMIZATION`；
- checker 用合理容差、关系、排序或区间接受由合法建模选择产生的差异，不得暗中要求某个未公开 CIF。

只有当评分目标明确依赖一个无法从论文描述合理重建、也不允许等价构型的特定原子级 realization 时，结构才是 `INDISPENSABLE_ASSET`，例如固定的无定形快照、无序占位 decoration、特定缺陷/界面 registry、实验精修坐标、冻结的亚稳态构型或指定结构数据集。此时必须提供该精确输入；“论文没有附 CIF”不能单独作为拒绝理由。

## Phase 2：答案正确性（Baseline）

`BASELINE_CORRECT` 要求：

- Gold 为 `PAPER_DIRECT`、`UNIQUE_DERIVATION` 或有文本依据的 `PAPER_SUPPORTED_RELATION`；
- paper-direct 数值绑定同一体系、方法和条件组；改变条件时不能继续要求论文绝对值；
- 所有核心输出都被 checker 读取；
- 正确答案在合理容差内通过，明显错误、malformed、NaN/Inf 和重复键不能通过；
- 容差可来自论文不确定度/精度、可审计数字化、独立复算、收敛、跨实现或 reviewer 明确物理/数值理由；不能移动 Gold 中心。

论文图中的数值若已保存为隐藏 Gold，仍需能审计其来源；若当前 `paper.md` 只有不可用图片且文本无数值，不能要求 solver 或 checker 读图，也不能把未核实数字当作 `PAPER_DIRECT`。

Baseline 所需实际 probe 只有：`valid_positive`、`tolerance_boundary`、`missing_or_malformed`、`non_finite_and_duplicate`、`wrong_science`。没有附加 checkpoint 仍可 PASS。

## Phase 3：可选 `RESULT_ENHANCED`

只有 Baseline 已 PASS 才评估增强：

- Gold 权重 60--80%；结果关系/不变量 20--40%；
- 基于实际攻击探针，按需增加最小科学检查；
- 优先复用最终表格，检查廉价派生量、守恒/归一化/符号/排序、跨输出关系或曲线少量代表点；
- 使用 `minimal_fabrication`、`quality_gradient`、`cross_condition_group_mismatch` 等与实际风险相符的探针。

有 trace 检查时，不追求穷举过程攻击。增强只检查结果层；不能用过程日志、迭代次数或“声称运行过”评分。

## Phase 4：checker 资源门槛

真实规模输出上测量 `checker_cost_record`：

```json
{
  "hardware_class": "CPU | SINGLE_GPU",
  "cpu_cores": 1,
  "gpu_count": 0,
  "gpu_type": null,
  "measured_wall_seconds": 0.1,
  "peak_memory_mb": 20,
  "input_bytes_read": 1000,
  "uses_full_trajectory": false,
  "performs_new_simulation": false,
  "real_scale_input": true,
  "cost_rationale": "...",
  "status": "PASS"
}
```

发布要求：CPU `<=32`；GPU `<=1` 且必须记录型号，单卡计算能力不得超过 H100；wall time `<=600 s`；不逐帧读取完整大体积 MD 轨迹；不重新运行主要 MD/DFT/训练/大规模搜索。validator 机械拒绝多卡或缺失型号；Reviewer 结合型号和实测记录确认不超过 H100 等级。超预算时科学 verdict 可仍为 `PASS`，但 `operational_status=FAIL`、`publishable=false`，route=`REPAIR_CHECKER_COST`。

## 领域轻量检查

- MD：只读能量/温压/应力摘要、漂移率、RDF/MSD/扩散等降维结果或少量抽样帧。
- DFT：只读总能、力、应力、带隙、DOS 摘要、少量 k/能带点和收敛摘要；不重跑 SCF。
- ML/势：只读已有指标、预测摘要、小规模固定样本或离线 reference；不重训、不对完整大数据集推理。

若唯一 checkpoint 超预算，保留 Baseline，不做 Enhancement。

## 结论与 schema

- `PASS + BASELINE_CORRECT`
- `PASS + RESULT_ENHANCED`
- `REPAIR_REQUIRED`
- `REAUTHOR_REQUIRED`
- `REJECTED`
- `BLOCKED`

复制 [core_review_template.json](assets/core_review_template.json)，运行：

```bash
python .cursor/skills/materials-benchmark-review/scripts/validate_core_review.py <review>/core_review.json --package <candidate-package>
```

传入 `--package` 时 validator 还会核对 grading tier、Gold/结果权重和 `tolerance_contract`；科学结论仍必须由 Agent 阅读真实文件并签发。
