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
`instruction.md` 定义求解者可见的公开任务，`tests/` 实现对最终核心科学结果的隐藏评分，`paper/` 用于论文忠实度、科学定义和 Gold 溯源。`solution/` 完全不在 Review/Repair 范围内。
_Avoid_: 用 solution、metadata、environment、resources 或 cluster 代替核心科学证据

**论文审查模式**:
双车道默认路径：确定性代码检查 + Agent 读 `paper/`。仅当材料资格已确立 `NON_MAT` 时可跳过论文。论文读取没有回退开关或两阶段绑定。按 instruction 意图判定复现类型：明确逐项复现才是 `EXACT_REPRODUCTION`，新问题或新终点是 `SCIENTIFIC_EXTENSION`，其余默认 `METHOD_REIMPLEMENTATION`。
_Avoid_: 论文读取回退、模糊时默认 EXACT、把科学扩展强制匹配论文精确值

**受限评测资产**:
Auditor 和 Repairer 可读取的 `tests/grading_spec.json`、`tests/checker.py`、相关测试文件，以及 `solution/` 中专门用于 checker 验证的 Oracle；它们对解题 Agent 保持隐藏。Oracle 只能在隔离环境中生成 mock 输出并验证其能否通过 checker，不能把 Oracle 数值当作论文一致性、科学正确性或 Gold provenance 的证据，也不能向解题 Agent 或公开审查产物泄露。`solution/` 中与该目的无关的内容仍不进入质检和修复判断。
_Avoid_: 使用 Oracle 数值证明论文复现正确、把隐藏答案泄露给解题 Agent

**题包元数据**:
`manifest.json`、`resources.json`、`steps.json`、`task.toml` 和 `environment/` 承担身份、上游资源部署、运行和人工说明角色。求解者只收到 `instruction.md` 题面，资源在其 `assets` 中声明；出题方/Playground 根据 `resources.json` 部署资源。Review/Repair 不调用 Playground 拉取资源、不下载资源正文、不审核平台部署机制，也不把资源内容作为泄露面；核对 `assets` 与 `resources.json` 的声明完整性和内部一致性，并轻量检查其中明确 HTTP(S) URL 的状态以识别稳定 `404/410`。Agent 应自行生成的结构、轨迹、模型和 solver 收敛参数不属于直接输入。
_Avoid_: 把 resources.json 当求解者题面、通过 Playground 拉取资源、下载正文、审核 Playground 部署、把暂时网络失败当资源缺陷

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
仅有六项可覆盖总分：①非材料任务；②科学目标无效；③最终任务缺少实质科学推理；④ checker 未评价核心任务且无法在不重定义题目的前提下修复；⑤不可替代直接输入永久不可用且无等价来源；⑥论文复现必需的执行/目标/评分参数在论文、补充材料和声明权威来源中均缺失且不可唯一推导。第⑥项必须 `REJECT + ABANDON`，不得用经验值、软件默认值或其他论文补齐。格式、NaN、容差、等价表示、部分分、缺失或损坏 Oracle 等可修实现问题不属于 Hard Gate。
_Avoid_: 任意 FATAL 或低分自动升级为 Hard Gate

**审查结论**:
质量总分按 C01–C07 的 10/20/20/20/10/10/10 权重计算；`solution/` 完全不进入审核或评分。`PASS` 为至少 80 且无未解决可修复 HIGH；`CONDITIONAL` 为 60–79 或存在可修复问题；`REJECT` 为低于 60 或触发六项 Hard Gate。`NOT_ASSESSABLE` 只表示关键证据临时无法取得，补齐后必须重审，不能把证据不足写成科学错误。
_Avoid_: metadata 参与加权、把临时环境故障直接判 REJECT

**模拟参数闭包**:
Agent 在 Phase 3 全文阅读论文后，对 MD、DFT、MC、相场、有限元等模拟题建立 `simulation_parameter_matrix`，覆盖体系、坐标/对称性、模型、初始化、边界/加载、演化、采样、分析、派生参数和评分依赖。只固定执行必需、目标定义或评分敏感参数；允许有证据的表示等价与 solver-selectable 参数。上游自由选择不得被下游固定数值、方向、公式或论文 Gold 暗中锁定。
_Avoid_: 只改坐标轴标签、机械零命中即通过、无来源补参数

**拒绝归档**:
对 `REJECT` 题包的非破坏性处置：保留原始题包和完整审查证据，将其移出可发布集合并放入隔离归档。
_Avoid_: 物理删除、继续留在可发布 corpus

**审查路径**:
材料题包按从便宜到昂贵的 Phase Gate 审核。Phase 0–2 先做 deterministic 筛查；只有保留实质科学目标且没有不可修复早期 Hard Gate 的题才升级到 Phase 3 论文深审。深审采用 `MECHANICAL + HYBRID + AGENT` 责任矩阵：Agent 必须回看真实题包文件并主动检查机械工具未命中的问题。审查与等深复审都执行 Harbor `tests/test.sh` 探针，但不声称科学工作流已复现。
_Avoid_: 把机械候选或零命中直接当 verdict、把 checker 探针视为科学流程已复现

**确定性修复**:
有唯一、可测试且不改变核心科学契约的修复对应 `AUTO_FIX`；有 instruction/tests/solution 或按需 paper 证据支持的解释性修复对应 `ASSISTED_FIX`；证据不足或会重定义核心科学契约时对应 `ABANDON`。前两者都可由 Agent 在隔离副本自主应用、回归并同深度复审；禁止猜科学参数、泄露答案、降低阈值或重定义核心科学任务。
_Avoid_: 每项修复都要求人工审批、无证据追阈值

**百题试评**:
沿用已冻结的原始 100 个 `cluster/theme/paper` 身份。先按新合同完成 10 题并由材料负责人校准，再审剩余 90 题；100 题原始审查全部完成并冻结基线之前不得进入修复。identity manifest 只固定样本身份，不携带旧 verdict 或 evidence。
_Avoid_: 边审边修、把旧候选 verdict 当新审查证据
