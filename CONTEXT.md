# Materials Benchmark Quality Assurance

本文件定义当前 Review/Repair 使用的核心术语。具体 Gate、schema 和 validator 以两个材料 Skill 为准。

## 核心文件角色

**Harbor 题包**：以 `paper-{id}/` 为根目录的独立 benchmark 包。

**公开科学合同**：`instruction.md` 是 solver 唯一可见题面；它必须直接提出自包含科学问题，并公开全部输入角色、Workflow 和 outputs。若 Enhanced 增加结果检查，其 artifact 也必须公开；Baseline 不强制 checkpoint。

**论文证据**：`paper/paper.md` 只供 Author/Review/Repair 使用，决定科学事实、Gold、关系、必要参数和适用条件；solver 不可见。

**隐藏评分**：`tests/**` 实现 Gold、精确容差和 checker，但不能增加题面未公开的提交要求。

**派生视图**：`steps.json`、manifest、task、environment 和 resources 只能镜像或实现题面，不能反向补题。

**排除范围**：`solution/**` 完全不读、不执行、不哈希、不引用、不修改。

## 准入与正确性

**计算科学准入**：核心评分工作必须可由计算机复现，并需要材料科学建模、分析、验证或判断。纯信息提取、纯代数代入/直接解方程、真实实验操作和简单实验数据换算均拒绝。

**题目正确性**：题面忠于论文、相关论文信息覆盖完整、参数跨步骤一致、Workflow producer/consumer 连贯、输出合同完整且必需资产可获得。

**答案正确性**：Gold/关系来自论文或唯一推导，适用于题面体系与条件；每个数值目标有合理容差；checker 接受正确答案并拒绝明显错误。高级 fabrication 风险属于可选 Enhancement。

## 参数与容差

**paper-reported 必要信息**：论文已给且定义目标、连接 Workflow、产生必要中间产物或影响评分的参数、公式、步骤和数据；题面漏写时必须补齐。

**SOLVER_SEARCHABLE 参数**：论文未报告唯一值、但可通过 mesh search、扫描、优化、收敛或合理算法选择确定的数值/执行项。它们即使影响结果也不构成不可复现证据，不得由 Review/Repair 猜值或被 checker 暗中固定。

**TARGET_DEFINING 参数**：决定材料体系、物理状态或研究条件；缺失后无法判断研究对象时题目失败。

**参数冲突**：同一物理量在相同作用域内出现不兼容值、单位、符号或含义。合法阶段变化、显式换算和不同材料/构型分支不是冲突。

**Gold provenance**：`PAPER_DIRECT`、`UNIQUE_DERIVATION` 或 `PAPER_SUPPORTED_RELATION`。前两者可定义绝对/数值目标；relation 可作为有适用依据的 smoke/改条件 CORE。

**合理容差**：优先使用论文不确定度、有效数字、可审计图像数字化、独立复算误差、实际收敛或跨实现校准；也可记录 reviewer 的明确单位/尺度/边界理由。solver 差异优先修容差，不能移动 Gold 中心或直接 Reauthor。

## 资源

**必需资产**：不可替代的数据集、特定代码、模型、势函数或不可重建的固定原子构型/结构快照。它必须通过 bundled file、公开 URL、运行时供给或合法等价物获得；没有任何取得方式时题包拒绝。结构文件不是默认必需资产：论文给出成分、晶系/空间群、晶格参数或建模方法，solver 能合理构建/优化时，缺少 CIF 不构成失败。

**可独立重实现代码**：论文公开方法足以由 solver 实现时，原作者代码不是必需资产，不能仅因无仓库链接拒绝。

**资源状态**：确认 404/410 且无替代物为不可用；临时 DNS/TLS/timeout 只记 Blocked。

## 结论与语料

Review verdict：

- `PASS`：题目与答案满足 Baseline 正确性；是否达到 Enhanced 由 `quality_tier` 单独说明。
- `REPAIR_REQUIRED`：保持论文支持的同一科学目标即可局部修复题面、Gold、容差、checker 或跨文件合同。
- `REAUTHOR_REQUIRED`：现有题面的方法或科学目标不受论文支持，必须从论文重新抽取并整体重写问题，不能靠局部 Repair 修成原题。
- `REJECTED`：原题触发 Q0 准入拒绝，或存在不可修复的必要资产缺口；未来可另出新题，但不改变原题被拒绝的事实。
- `BLOCKED`：当前缺少判断 Gold、资源或关键条件所需的证据；证据恢复后重新 Review，不把未知写成科学错误。

PASS 另分 `BASELINE_CORRECT` 与 `RESULT_ENHANCED`。checker 成本作为独立 operational gate：最多 32 CPU 核或单卡 H100、600 秒，不读完整大体积轨迹，不重跑主要科学计算。超预算不改变科学 verdict，但不可发布。

v2 源题包不可变；Review/Repair/candidate/evidence 留在题包外；v3 只保存独立 Review 为 PASS 的 candidate。`corpus_review_tracking.json` 是唯一 corpus 进度记录，不使用 dispatcher、lock 或第二套 lifecycle 状态。
