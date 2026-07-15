# Materials Benchmark Quality Assurance

This context defines the language used to design, evaluate, and repair Harbor-format materials-science benchmark packages.

## Language

**Harbor 题包**:
一个以 `paper-{id}/` 为根目录、包含任务说明、工作流、资源声明、运行环境和评分器契约的独立 benchmark 包。它是接收、质检、修复和处置的基本对象。
_Avoid_: 题目、paper

**审计单元**:
一次质检所处理的单个 Harbor 题包；cluster、theme 和整个 corpus 只用于组织或批量调度，不作为一次质检的根目录。
_Avoid_: cluster、corpus

**材料题包**:
科学正确性实质依赖材料对象、材料数据、材料计算或材料性质终点的 Harbor 题包。计算化学、凝聚态物理、光子学等边界领域在满足该条件时属于材料题包；只借用材料名词的通用计算或软件任务不属于材料题包。
_Avoid_: 由 `manifest.discipline` 单独定义的材料题

**核心科学契约**:
`instruction.md` 对公开任务的定义与 `tests/` 对该定义的评分实现，以及两者相对于原论文科学内容的正确性关系。质检以此为主，判断出题是否正确、评分器是否鲁棒并保持 ground truth。
_Avoid_: 仅凭 metadata 或 cluster 判定题目正确

**论文审查模式**:
`no_paper` 判断题包能否仅凭公开 instruction、资源、环境和 tests 独立成立，论文一致性标为 `NOT_ASSESSED`；`paper_grounded` 先完成全部 no-paper 检查，再核对论文正文、方法、图表、补充材料、数据和 Gold provenance。后者区分严格复现、方法重实现和科学扩展。默认先运行 no-paper gate；未触发不可修复 Hard gate 的题再进入 paper-grounded，最终结论以后者为准。
_Avoid_: no-paper 模式声称论文忠实性、把科学扩展强制匹配论文精确数值

**受限评测资产**:
Auditor 和 Repairer 可读取的 `tests/grading_spec.json`、`tests/checker.py` 与相关测试文件，用于验证核心科学契约；它们对解题 Agent 保持隐藏。`solution/` 与隐藏参考解只可确认存在，不能用于质检或修复判断。
_Avoid_: 使用 solution 证明题包正确

**题包元数据**:
`manifest.json`、`resources.json`、`steps.json` 和 `task.toml` 中用于描述身份、资源、流程和运行配置的信息。它们需要一致且可用，但不能代替对核心科学契约的逐题审查。
_Avoid_: 核心科学内容

**三维覆盖标签**:
质检时附加的 `computation_task`、`research_domain` 和 `material_system` 分类。`computation_task` 是主要组织维度，一个题包可有多个同等标签；材料研究领域和材料体系用于衡量覆盖度，不决定质检结论。标签写入审查报告和 corpus 级索引，不修改原始 `manifest.json`。
_Avoid_: cluster 标签、准入结论、原题包 metadata

**分类词表快照**:
三维覆盖标签在仓库中的版本化事实源，记录飞书原文 URL 和 revision。质检运行只读取该快照；词表更新通过显式版本变更完成。
_Avoid_: 每次运行实时读取飞书

**Workflow cluster**:
按计算 workflow 聚合论文的历史分组，以 `cluster-id` 标识，可作为判断计算任务类别的参考。它不是材料准入、科学正确性或评分器可信度的证据。
_Avoid_: 审计单元、质检结论

**修复副本**:
保留原始 `cluster-id/paper-id` 目录身份并与原题包可追溯对照的完整工作副本。修复在 `.benchmark_repair_tmp/<repair_id>/` 中进行，成功通过回归测试和同级复审后才原子发布；失败时恢复快照，历史修复产物归档。
_Avoid_: 无快照的原地修改、只隔离修复报告

**Hard gate**:
覆盖加权总分的致命准入条件；材料准入、核心科学契约、资源可用性、任务可答性、评分器有效性和适用时的论文一致性属于关键维度。任一 FATAL 或关键维度低于 0.50 时，题包不能通过。
_Avoid_: 可由其他维度高分抵消的问题

**审查结论**:
`PASS` 表示总分至少 0.80、无 FATAL、无未解决 HIGH 且所有关键维度至少 0.50；`CONDITIONAL` 表示总分为 0.60–0.79 或存在可修复 HIGH；`REJECT` 表示总分低于 0.60、触发 FATAL 或关键维度低于 0.50；`NOT_ASSESSABLE` 表示关键证据不足。
_Avoid_: 仅按总分处置

**拒绝归档**:
对 `REJECT` 题包的非破坏性处置：保留原始题包和完整审查证据，将其移出可发布集合并放入隔离归档。
_Avoid_: 物理删除、继续留在可发布 corpus

**执行等级**:
质检证据深度从静态审查 `E0`、动态攻击评分器 `E1`、最小科学流程启动 `E2`、缩小体系完整复现 `E3` 到全量复现 `E4` 逐级增加。每个审计单元至少完成 E1；风险触发时升到 E2，E3/E4 需要显式算力预算与审批。
_Avoid_: 把 E1 视为科学流程已复现

**确定性修复**:
有唯一、可测试且不改变核心科学契约的修复，对应 `SAFE_AUTO_FIX`。`CONDITIONAL` 后可自动规划、应用和复审；需要科学解释或可能影响契约的 `ASSISTED_FIX` 必须先取得人工批准。
_Avoid_: 自动执行所有建议修复

**百题试评**:
材料质检与修复 skills 完成后的首轮人工校准：抽取约 60 个覆盖 workflow 与三维标签的题包、20 个 checker/Gold 高风险题包、10 个边界领域题包和 10 个明确可修复候选，逐题质检、按权限修复并复审，再以 Cursor Canvas 汇总审查结论、findings、三维覆盖标签、证据和修复前后变化，由材料负责人核对。
_Avoid_: 只验证脚本能运行、以 checker 自身作为 skill 真值
