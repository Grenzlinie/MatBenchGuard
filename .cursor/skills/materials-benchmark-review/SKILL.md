---
name: materials-benchmark-review
description: 审核基于论文编写的材料科学问题，检查强制性 2.1–2.8 验收项、论文忠实度、科学正确性、提示一致性、检查器覆盖度与区分能力、Gold 可信度、答案泄露、安全性，以及数据、模型和软件的就绪状态。适用于 Harbor 问题包。Agent 负责语义裁决；自动化仅验证记录并提供可能出错的诊断。
---

# 材料科学基准审核

在准入前审核一个基于论文编写的材料科学问题。Agent 是科学判断与结论的权威。确定性诊断在通过原始文件或可用的运行时证据验证前，只能视为假设。

`solution/` 完全不属于 Review 范围：不得读取、执行、哈希、扫描、引用或用其内容支持/否定任何结论。检查器质量的审核范围仅限公开任务要求的最终核心科学结果。不得要求检查器读取或证明方法、轨迹、训练日志或中间产物。

本文所称“最终核心科学结果”与英文规则中的 `final core scientific outputs` 含义相同。

## 必读参考资料

作出结论前，必须阅读：

- [audit-dimensions.md](references/audit-dimensions.md)：强制性 2.1–2.8、C01–C07 评分、硬门槛和审核结论；
- [paper-grounded-audit.md](references/paper-grounded-audit.md)：论文忠实度、复现意图和材料参数例外；
- [checker-audit.md](references/checker-audit.md)：静态映射和必需的运行时探针；
- [resource-readiness.md](references/resource-readiness.md)：数据、预训练模型、软件、环境和访问就绪状态；
- [scientific-defect-patterns.md](references/scientific-defect-patterns.md)：跨步骤矛盾、方法—Gold 错配、合成 Gold、缺参和定义歧义等必查问题模式；
- [mechanical-evidence.md](references/mechanical-evidence.md)：保守的包、契约、AST、资源收集器及检查器探针运行器。
- [check-responsibility-matrix.md](references/check-responsibility-matrix.md)：从低成本筛查到论文深审的 `MECHANICAL`、`HYBRID`、`AGENT` 检查责任和升级条件。

按需阅读：

- [materials-gate.md](references/materials-gate.md)；
- [task-types-and-leakage.md](references/task-types-and-leakage.md)；
- [security-audit.md](references/security-audit.md)；
- [report-schema.md](references/report-schema.md)。

## 题包格式要求

```
paper-xxx/
├── manifest.json          # 元数据
├── task.toml              # 任务配置（资源限制、超时）
├── resources.json         # 数据源列表
├── steps.json             # 分步骤定义
├── instruction.md         # Agent 题面
├── paper/
│   └── paper.md           # 论文全文
├── tests/
│   ├── grading_spec.json  # 评分规范
│   ├── checker.py         # 评分脚本
│   ├── test.sh            # 标准评分入口
│   └── *.bed / *.csv      # Gold standard 参考文件
└── solution/ (optional)
    └── solve.sh           # 参考解法（Review/Repair 完全忽略）
```

文件角色与交付契约：

- `instruction.md` 和 `resources.json` 会交付给求解者。应结合两者判断任务完整性；答案泄露仅依据 `instruction.md` 判断。
- `resources.json` 是资源及其定位信息的声明，不代表资源内容会自动交付。审核 2.8 时应结合 `instruction.md` 使用；不得为了检查泄露而访问定位地址或公共资源。
- `solution/` 是可选目录，但完全排除在 Review/Repair 范围外；若存在，只随题包原样保留，不读取、不运行、不扫描、不引用。
- `tests/` 对求解者不可见；`checker.py`、`grading_spec.json`、`test.sh` 和其中的 Gold 文件共同定义评分。`tests/test.sh` 是核心格式必需的标准评分入口；`environment/`、图片清单或其他扩展文件可以存在。
- `paper/`、`manifest.json`、`steps.json` 和 `task.toml` 用于编写、审核或运行时溯源，不会交付给求解者。

## 输入与范围

定位与任务说明、论文及补充材料、检查器、评分契约、公开夹具、测试入口、已声明资源和环境功能等价的文件。名称和布局可以不同；判断前先建立文件角色映射。

完整阅读任务说明、`resources.json` 和论文。对于与 A2/A4/A5 等价的判断（科学有效性、论文忠实度和 Gold），除非任务已被证明为 `NON_MAT`，否则必须阅读论文。

所有审核产物必须保存在 Harbor 问题包之外。审核不得修改问题包。

## 工作流程

审核采用从便宜到昂贵的分阶段 Gate，并为每一阶段保留独立证据：

- **Phase 0 · 结构与版本**：全部核心文件（包括 `tests/test.sh`）的存在性、可解析性、角色映射、跨文件输出合同和文件哈希；
- **Phase 1 · 资源与预算**：必要资源的身份、版本、可达性、许可、算力、时间和存储预算；
- **Phase 2 · 题面与 checker 静态审计**：输入/输出合同、评分链、重复键、坐标、单位、权重和能力声明；
- **Phase 3 · 论文精读**：晶体学/物理定义、方法与固定参数、Gold、容差和论文忠实度；
- **Phase 4 · 动态验证**：有效正例、通用负例、任务特定攻击、质量梯度、语义等价和组件隔离；
- **Phase 5 · 证据一致性**：决策 JSON、原始探针、发现、分数、硬门槛和发布结论的交叉校验。

每个阶段必须遵循 [检查责任矩阵](references/check-responsibility-matrix.md)。Phase 0–2 先使用机械结果做低成本筛查；机械事实可以复用，但候选和“零命中”都不能替代真实文件检查。只有任务仍具有实质科学目标且未触发不可修复的早期硬门槛时，才投入 Phase 3。进入 Phase 3 后，Agent 必须全文阅读论文，并按责任矩阵对题面、steps、资源、Gold、grading、checker 和 `tests/test.sh` 做 Hybrid 复核，包括主动搜索机械检查未覆盖的问题。

任何阶段发现不可修复硬门槛时可以提前停止昂贵执行，但必须保留已执行阶段、停止理由和缺失证据；可修复缺陷不得用于跳过后续阶段并提前缩小修复范围。

1. 运行机械证据收集器。检查其 `facts`、`candidates` 和 `limitations`；收集器无权直接生成缺陷结论。网络允许且存在必要外部资源时必须使用 `--probe-urls`，但资源内容不得作为泄露判断依据。
2. 判定材料科学资格与复现意图。
3. 提取科学目标、必需输入、固定参数、求解者可选参数、**最终核心科学输出**、答案类型和所声称的能力。生成 `evidence/scientific_claim_matrix.md`，逐项记录“公开声明 → 论文证据 → 必需参数 → 最终输出 → checker 观察量 → 动态测试”。判断该能力是否需要实质性科学推理，而非纯信息抽取或纯代数计算。明确将推荐方法、执行轨迹、训练日志和中间产物排除在核心输出映射之外。
4. 检查工作流程、输出契约和评分之间的提示自洽性。逐项裁决 `scientific-defect-patterns.md`，尤其比较各步骤重复出现的分析时间窗、温度、载荷、单位、坐标、截断、采样区间和输出行数；例如“最后 15 ns”与“最后 5 ns”必须作为 `CROSS_STEP_PARAMETER_CONTRADICTION` 处理，不能以步骤独立为由忽略。
5. 对照论文核验任务说明、数据、方法、参数和 Gold。先明确评分目标是绝对数值、容差区间、相对排序、单调趋势还是定性关系，再判断证据是否支持该目标。如果题目改变了原论文的体系、方法或条件，却仍要求匹配论文绝对数值，裁决 `METHOD_REFERENCE_MISMATCH`。缩小体系、缩短轨迹或 smoke 计算不自动构成缺陷：若 checker 只评价论文或权威来源支持、且对声明体系有适用依据的趋势/排序，不伪装成绝对值复现，则可以通过。`tests/` 中的随机、拟合、插值、smoke/dummy 等词法命中只能作为 provenance 候选；只有其被当作无可靠依据的真值、阈值或趋势时，才裁决 `UNSUPPORTED_SYNTHETIC_GOLD`。不得打开或检查 `solution/`。
6. 追踪每个最终核心科学输出：

   ```text
   公开的最终输出要求 → 检查器读取 → 评分器
   → 有效权重 → 有限贡献 → 最终奖励
   ```

   不得在该链路中增加对过程或轨迹的读取要求。
7. 先编写 `evidence/probe_plan.json`，把每个核心科学自变量、主键、坐标、单位、边界、容差和能力声明映射到至少一个正例或攻击。随后实际运行机械探针。所有十一类均允许 Agent 提供任务特定变体，例如 `--case minimal_exploit:wrong-time-axis=<dir>`；通用样例不得替代任务特定攻击。
8. 结合 `instruction.md` 与 `resources.json`，确认每项必需的数据、模型、软件、环境和访问条件均为必要、声明充分且在审核时可验证。网络允许时必须探测必要定位地址；确认的 `404/410`、身份不匹配或内容不足属于资源缺陷，瞬时网络失败才属于自动化限制。
9. 审核泄露、安全性、可行性和可复现性。核对能力声明与最终可观察结果：如果查值、硬编码或极小合成输出可与真实科学工作同分，必须在 2.5/2.7 或 `SCIENTIFIC_REASONING_ABSENT` 中处理，不能以“不审核过程”为由忽略。
10. 独立评估 2.1–2.8，给出 C01–C07 评分，裁决全部五个硬门槛和全部必查科学问题模式，并用精确证据记录发现。每个失败 pattern 必须对应一项已确认 finding；不适用的 pattern 必须说明原因。
11. 对每项自动化诊断使用 `CONFIRMED`、`DISMISSED_FALSE_POSITIVE` 或 `AUTOMATION_LIMITATION`。只有已确认缺陷会影响审核结论。
    本地辅助工具无法复现声明的容器路径时，应标记为 `AUTOMATION_LIMITATION`；只有证据证明声明的容器布局、挂载或路径本身无效时，才可认定为缺陷。
12. 使用 `assets/agent_final_decision_template.json` 编写 `agent_final_decision.json`，然后将所有原始探针文件交给验证器：

    ```bash
    python .cursor/skills/materials-benchmark-review/scripts/validate_agent_decision.py \
      <path>/agent_final_decision.json \
      --probe-observations <path>/checker_observations.json \
      --probe-observations <path>/task_specific_observations.json
    ```

## 不可违反的发布规则

只有在 2.1–2.8 全部通过、总分至少为 80、所有硬门槛均通过、所有必需且适用的探针均通过、所有就绪类别均为已就绪或无需就绪，且不存在未关闭的已确认、可修复 `HIGH`/`FATAL` 缺陷时，才允许给出 `PASS`。

不得因辅助工具拒绝某种模式或布局而返回 `NOT_ASSESSABLE`。如果自动化无法评估有效的替代表示，应由 Agent 人工检查，并记录为自动化限制或误报。

未执行适用的检查器探针时，不得完成可发布审核。显式使用 `--no-execute` 的运行仅用于诊断，检查器相关标准仍属于未评估状态。唯一例外是 Phase 0–2 已确认 disposition 为 `ABANDON` 的不可修复早期 Hard Gate：可以在 Phase 3/4 前停止并形成验证通过的 `REJECT` 筛查记录；Orchestration 将其标记为 `SCREENED_OUT`。该状态不是新的 Review verdict，不得 `PASS`、不得进入 Repair、不得发布。

决策中声明的每个适用探针必须引用原始 observation 的实际 `case_id`。验证器必须拒绝“决策写 PASS、原始证据为 `NOT_ASSESSED`/`UNUSABLE`”的状态矛盾。

## 完成条件

仅当决策验证器通过、所有必需证据均已提供、实际探针结果得到如实记录，并且面向用户的回复明确说明审核结论、决定性证据、已确认的修复需求和决策文件位置时，方可完成可发布审核。早期 `SCREENED_OUT` 只完成低成本筛查：必须保留停止阶段、决定性 `ABANDON` Hard Gate、未执行证据和验证通过的 `REJECT` 决策。
