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
`instruction.md` 对公开任务的定义、`tests/` 对该定义的评分实现，以及 `solution/` 中仅用于正例 mock 的 Oracle 链路。质量证据只来自这三处；`paper/` 仅在触发条件成立时用于消歧和溯源。
_Avoid_: 用 metadata、environment、resources 或 cluster 形成质量分

**论文审查模式**:
默认只看 `instruction.md`、`tests/` 和受限 Oracle。仅在四种情况读取 `paper/`：三者存在科学或数值矛盾；公开任务疑似缺少影响科学有效性或可答性的必要信息；Gold、容差或评分依据来源可疑；instruction 明确声称复现论文体系、条件、结果或特定数值。按 instruction 意图判定复现类型：明确逐项复现才是 `EXACT_REPRODUCTION`，新问题或新终点是 `SCIENTIFIC_EXTENSION`，其余默认 `METHOD_REIMPLEMENTATION`。
_Avoid_: 每题默认读论文、模糊时默认 EXACT、把科学扩展强制匹配论文精确值

**受限评测资产**:
Auditor 和 Repairer 可读取的 `tests/grading_spec.json`、`tests/checker.py`、相关测试文件，以及 `solution/` 中专门用于 checker 验证的 Oracle；它们对解题 Agent 保持隐藏。Oracle 只能在隔离环境中生成 mock 输出并验证其能否通过 checker，不能把 Oracle 数值当作论文一致性、科学正确性或 Gold provenance 的证据，也不能向解题 Agent 或公开审查产物泄露。`solution/` 中与该目的无关的内容仍不进入质检和修复判断。
_Avoid_: 使用 Oracle 数值证明论文复现正确、把隐藏答案泄露给解题 Agent

**题包元数据**:
`manifest.json`、`resources.json`、`steps.json`、`task.toml` 和 `environment/` 只承担身份、运行和人工说明角色，不是质检对象，不进入质量分或 Hard Gate。只有 `instruction.md` 明确要求、完成任务不可替代且没有科学等价来源的直接输入/服务才验证可用性；Agent 应自行生成的结构、轨迹、模型和 solver 收敛参数不属于直接输入。
_Avoid_: 核心科学证据、资源声明即阻塞

**科学等价性**:
只阻塞会改变体系定义、科学目标、归一化或被评分结果的实质差异。允许等价软件、版本和 solver 自选收敛参数，除非 instruction 明确固定，或 checker 暗中依赖某个未公开选择。不同超胞、边界条件或参数若改变 Gold，则不是等价实现。
_Avoid_: 因 VASP/QE、FHI-aims/ORCA 等软件替换本身拒绝题包

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
仅有四项可覆盖总分：①不是真正的材料科学任务；②任务科学上无效或缺少不可恢复的必要定义；③ checker 根本未评价核心任务且无法在不重定义题目的前提下修复；④ instruction 要求的不可替代直接输入永久不可用且无等价来源。格式、NaN、容差、等价表示、部分分、缺失或损坏 Oracle 等可修实现问题不属于 Hard Gate。
_Avoid_: 任意 FATAL 或低分自动升级为 Hard Gate

**审查结论**:
质量总分为 100：科学有效性 35、instruction 可答性 20、checker/Gold 对齐 25、鲁棒性与区分度 15、solution 完整性 5。`PASS` 为至少 80 且无未解决可修复 HIGH；`CONDITIONAL` 为 60–79 或存在可修复问题；`REJECT` 为低于 60 或触发四项 Hard Gate。`NOT_ASSESSABLE` 只表示关键证据临时无法取得，补齐后必须重审，不能把证据不足写成科学错误。
_Avoid_: metadata 参与加权、把临时环境故障直接判 REJECT

**拒绝归档**:
对 `REJECT` 题包的非破坏性处置：保留原始题包和完整审查证据，将其移出可发布集合并放入隔离归档。
_Avoid_: 物理删除、继续留在可发布 corpus

**执行等级**:
质检证据深度从静态审查 `E0`、动态攻击评分器 `E1`、最小科学流程启动 `E2`、缩小体系完整复现 `E3` 到全量复现 `E4` 逐级增加。每个审计单元至少完成 E1；风险触发时升到 E2，E3/E4 需要显式算力预算与审批。
_Avoid_: 把 E1 视为科学流程已复现

**确定性修复**:
有唯一、可测试且不改变核心科学契约的修复对应 `SAFE_AUTO_FIX`；有 instruction/tests/solution 或按需 paper 证据支持的解释性修复对应 `ASSISTED_FIX`。两者都可由 Agent 在隔离副本自主应用、回归并同深度复审；证据不足时放弃，禁止猜科学参数、泄露答案、降低阈值或重定义核心科学任务。
_Avoid_: 每项修复都要求人工审批、无证据追阈值

**百题试评**:
沿用已冻结的原始 100 个 `cluster/theme/paper` 身份。先按新合同完成 10 题并由材料负责人校准，再审剩余 90 题；100 题原始审查全部完成并冻结基线之前不得进入修复。identity manifest 只固定样本身份，不携带旧 verdict 或 evidence。
_Avoid_: 边审边修、把旧候选 verdict 当新审查证据
