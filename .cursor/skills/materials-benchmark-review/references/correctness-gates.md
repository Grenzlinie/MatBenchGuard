# 正确性门槛

## Q0--Q6：题目正确性

- Q0：核心任务是计算机可复现的非平凡科学问题；纯信息、纯代数、实验操作、简单实验换算拒绝。
- Q1：研究问题、方法和要求的过程来自同一 `paper.md`，不把文献阅读当任务。
- Q2：体系、物理状态、方法和条件可唯一辨认。
- Q3：论文能给出的必要参数/公式/步骤完整，跨步骤参数自洽，Workflow producer/consumer 连贯。
- Q4：全部 solver-visible 输出位于 `/app/outputs`，schema/单位/主键/基数完整。
- Q5：steps、manifest、task、resources 与 instruction 同步。
- Q6：不可替代数据、模型、势、特定原子构型/结构快照、特定代码可取得；普通可搜索参数及可由论文描述合理建模的结构缺少 CIF 不触发 Q6。

参数按 `PAPER_FIXED`、`SOLVER_SEARCHABLE`、`TARGET_DEFINING`、`INDISPENSABLE_ASSET` 分类。`SOLVER_SEARCHABLE` 可以显著影响结果，但论文未给唯一值时仍合法；题面要求 solver 搜索/收敛/优化/论证，checker 用容差、区间或关系接受合法选择。若 checker 暗中固定唯一值，修 checker。

结构不是天然资产。论文给出的成分、晶系/空间群、晶格参数和构造方法用于定义目标；未唯一规定的原子 realization 可由 solver 建模/优化。只有任务必须使用一个不可重建且不允许等价替代的固定原子构型时，才记录 `INDISPENSABLE_STRUCTURE_UNAVAILABLE`。

## A1--A6：答案正确性

- A1：checker 读取项全部来自公开输出合同。
- A2：Gold/关系为 `PAPER_DIRECT`、`UNIQUE_DERIVATION` 或有文本依据的 `PAPER_SUPPORTED_RELATION`。
- A3：Gold 与题面使用同一体系、方法、参数组、单位和坐标；不同组分别检查不同 Gold。
- A4：checker 读取所有核心输出和全部必需条件组。
- A5：正确答案通过；malformed、NaN/Inf、重复和明显 wrong-science 不通过。
- A6：合理容差及 inclusive/exclusive 边界与实际 reward 一致。

Baseline 只要求 A1--A6 的正确性，不要求高强度 anti-hacking。`minimal_fabrication`、`quality_gradient` 和复杂 cross-group attack 属于增强层；静态的逐组 Gold 映射和全组覆盖仍属于 Baseline。

## 路由

- 问题与答案均正确：`PASS + BASELINE_CORRECT`。
- 在 Baseline 上增加轻量结果检查并满足权重/探针：`PASS + RESULT_ENHANCED`。
- 同一科学目标可修：`REPAIR_REQUIRED`。
- 题面加入论文不支持的方法或必须重建目标：`REAUTHOR_REQUIRED`。
- Q0 硬拒绝或不可替代资产不可用：`REJECTED`。
- 当前证据无法判断 Gold/资源/关键条件：`BLOCKED`。

Checker 超预算不改变科学 verdict；单独令 `operational_status=FAIL`、`publishable=false`、`route=REPAIR_CHECKER_COST`。
