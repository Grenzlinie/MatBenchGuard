# Repair / Reauthor 工作流

## Stage A：Baseline Correctness

1. 冻结源包哈希，不读 `solution/**`。
2. 从 `paper.md` 恢复必要问题、方法、参数、公式和 Workflow。
3. 建参数表；论文未给唯一值但可搜索/收敛/优化的项标为 `SOLVER_SEARCHABLE`，不补值。
4. 同步 instruction -> 派生视图 -> tests。
5. 修复逐条件组 Gold、合理容差、核心输出覆盖和 obvious-wrong 拒绝。
6. 实跑五类 Baseline probe 与真实规模 checker 成本测试。
7. 独立 Review 必须得到可发布 `BASELINE_CORRECT`。

## Stage B：Result Enhancement

只接收独立复审过的 Baseline。增加最小、廉价、结果层检查；不得修改科学目标、paper Gold 中心、必要内容和 solver-searchable 自由度。完成后再做性能验收和独立 Review。

增强失败、超预算或损害 Baseline：`ROLLED_BACK`，发布 Baseline。

## Reauthor

只有论文支持的新任务与旧目标实质不同，或旧题加入论文不支持的研究方法而不能局部恢复时使用。Reauthor 从论文重新定义完整科学合同，并从空白 Review；不能把旧 checker/Gold 当事实来源。

Q0 纯信息/纯代数题可以标记 reauthor eligible，但原题仍为 `REJECTED`。
