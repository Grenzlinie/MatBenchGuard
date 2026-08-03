# 科学评分、容差与轻量成本

## Gold 先于增强

Baseline 首先保证同一论文条件的 Gold/关系正确。不同参数组分别使用不同 Gold；禁止用 A 组 Gold 检查 B 组结果。改变体系/条件时不能仍要求论文绝对值；明确 smoke 才使用论文支持的趋势/关系。

`SOLVER_SEARCHABLE` 差异不能仅因论文未写唯一网格、cutoff、timestep、初值或算法而 Reauthor。保持 paper value 中心，用下列依据设置容差：

1. `reported_uncertainty`
2. `reported_precision`
3. `digitization`（必须保存可审计过程）
4. `independent_recompute`
5. `convergence`
6. `cross_implementation`
7. `reviewer_reasoned`（明确单位、尺度和接受边界）

每个 numeric target 有独立 tolerance record，实跑 `T-epsilon/T/T+epsilon`。不能移动 Gold 中心、按现有答案反推或随手填百分比。

图像 Gold：solver 和运行时 checker 不应读论文图。只有制题侧已保存且可审计的数字化 reference 可用；若当前论文资源没有图片且文本无对应数值，Gold provenance 被阻塞，而不只是容差问题。

## Baseline 评分

允许 Gold-only。所有核心输出都被读取，正确答案过阈值，明显错误不过阈值。高级 fabrication 风险作为限制或 Enhancement 候选，不反向否决科学正确性。

## Enhanced 评分

Gold 60--80%；廉价结果关系/不变量 20--40%。优先基于已有最终表格，不增加昂贵计算。允许离线生成隐藏 reference；运行时 checker 只比较抽样值并做轻量公式/关系检查。

## 成本预算

- CPU 最多 32 核，或最多单 GPU；GPU 型号必须记录且能力不超过 H100；
- 单题 checker wall time 不超过 600 秒；
- 默认 CPU 轻量检查；
- 不读完整大体积 MD 轨迹，不重新执行主科学计算；
- 必须用真实规模输出测量时间、峰值内存和读取字节数。

超预算只导致 `operational_status=FAIL` 和 `publishable=false`；修 checker 成本后再发布，不改变问题/答案的科学 verdict。
