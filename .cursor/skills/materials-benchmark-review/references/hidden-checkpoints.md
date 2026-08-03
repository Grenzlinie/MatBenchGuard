# 最小结果检查

## Baseline 与 Enhancement 的边界

Baseline 可以只检查 paper Gold，只要：Gold/条件/容差正确、所有核心输出被读取、正确答案通过、明显错误失败。不能因为“还能被更精巧地 hacking”否决 Baseline。

只有真实 probe 暴露具体结果层风险时，才按需加入最小科学检查，并升级 `RESULT_ENHANCED`。已有 trace 检查承担过程真实性，不在结果 checker 中复制昂贵过程验证。

## 优先级

1. 直接比较 paper Gold；
2. 从已有最终表格重算廉价派生量；
3. 检查守恒、归一化、符号、排序、残差和跨输出关系；
4. 曲线少量代表点；
5. checker 外离线独立复算的可信隐藏 Gold。

Gold 占 60--80%，结果关系/不变量占 20--40%。公开新增结果必须写明 `/app/outputs` path、schema、单位、基数和含义。

## 禁止

- 用日志、迭代次数或“声称运行过”作为科学证据；
- 为减少引导而删除论文必要参数、公式或 Workflow step；
- 读取/逐帧比较完整大体积 MD 轨迹或原子级全轨迹 RMSD；
- checker 中重跑 MD、SCF、完整能带/DOS、训练或大规模搜索；
- 为 Enhanced 强制新增超出 32 CPU 核、单 GPU（型号必记且能力不超过 H100）或 600 秒的检查。

唯一可想到的 checkpoint 过于昂贵时，记录 `NO_AFFORDABLE_RESULT_CHECK`，保留 Baseline。
