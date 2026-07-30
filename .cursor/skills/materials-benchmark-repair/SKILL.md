---
name: materials-benchmark-repair
description: 根据 Agent 主导的审核结果修复材料科学论文问题包。使用已确认的 2.1–2.8 缺陷、论文或公开证据、隔离候选包、检查器回归测试和同等深度复审。不得修复已排除的模式误报，也不得臆造科学参数、Gold、模型、数据或容差。
---

# 材料科学基准修复

在不重新定义科学任务的前提下修复已确认缺陷。只有经 Agent 对照当前公开文件核验后，审核证据才具有权威性。

`solution/` 完全不属于 Repair 范围：不得读取、执行、哈希、扫描、引用或修改。复制源包形成 candidate 时可以随包原样携带，但任何修复和证据均不得涉及其内容。不得仅为满足内部模式而修改有效的问题包。

修复范围是对最终核心科学结果进行公平、可用且可复现的评分。不得仅因检查器未读取指定方法、轨迹、训练日志或中间产物而修复检查器。审核 Docker 路径时，应依据问题包声明的容器布局，而非宿主机路径是否恰好一致。

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

- 求解者直接收到的题面只有 `instruction.md`，所需资源在其中的 `assets` 中声明；仅依据 `instruction.md` 修复公开合同和泄露问题。
- `resources.json` 是出题方和 Playground 的上游资源定位/部署声明，不交付给求解者。Repair 不调用 Playground 拉取资源，不验证平台部署或挂载，也不把资源内容作为泄露面；但必须轻量检查声明中明确 HTTP(S) URL 的状态，避免保留稳定的 `404/410`。
- 输入修复处理 `instruction.md` 的 `assets` 声明、其与题包内 `resources.json` 的标识/版本/角色/映射一致性，以及经 Review 确认失效且有来源依据的 URL；不得猜测替代地址。
- `solution/` 是可选目录，但完全排除在 Review/Repair 范围外；若存在，只随题包原样保留，不读取、不运行、不扫描、不引用、不修改。
- `tests/` 对求解者不可见；`checker.py`、`grading_spec.json`、`test.sh` 和其中的 Gold 文件共同定义评分。`tests/test.sh` 是核心格式必需的标准评分入口；`environment/`、图片清单或其他扩展文件可以存在。
- `paper/`、`manifest.json`、`steps.json` 和 `task.toml` 用于溯源或运行时，不会交付给求解者。

修复候选包必须保留这一必需结构。

## 必读参考资料

修复前必须阅读：

- [repair-policy.md](references/repair-policy.md)；
- [repair-categories.md](references/repair-categories.md)；
- 涉及检查器或评分变更时阅读 [checker-repair.md](references/checker-repair.md)；
- [abandonment.md](references/abandonment.md)；
- [report-schema.md](references/report-schema.md)。

还必须阅读审核 skill 中的审核维度、论文规则、检查器审核和资源就绪规则。候选包必须通过相同的完整审核。
必须同时阅读并执行审核 skill 的 [检查责任矩阵](../materials-benchmark-review/references/check-responsibility-matrix.md)：机械结果只用于定位，修复前缺陷发现和候选包完整复审都必须对决定性真实文件执行 Hybrid 检查。

## 必需输入

必须提供源问题包、已验证的 `agent_final_decision.json`、已确认缺陷及其支持证据。忽略分类为 `DISMISSED_FALSE_POSITIVE` 或 `AUTOMATION_LIMITATION` 的诊断。

## Repair 准入 Gate

仅当源 Review 为 `CONDITIONAL` 或 `REJECT`、至少存在一项 disposition 为 `REPAIR` 的已确认 finding/Hard Gate，且不存在足以决定最终结论的非修复型 `ABANDON` Hard Gate 时，才进入 Repair。

- `PASS`：无需 Repair；
- `NOT_ASSESSABLE`：等待补证，不得用 Repair 猜测缺失信息；
- 早期筛查已确认不可修复 Hard Gate，或所有 finding 均为 `ABANDON`：终态为 `SCREENED_OUT`，不创建 candidate，不运行 Repair，也不生成 `repair_report.json`；
- 同时存在可修 finding 和决定性 `ABANDON` Hard Gate：仍为 `SCREENED_OUT`，因为局部修复不能使题包通过。

Repair 的 `ABANDONED` 仅表示题包已经合法进入 Repair，但在修复或等深复审中发现无法安全修复；它不用于包装本应在 Review 早停的题。

## 工作流程

1. 先执行 Repair 准入 Gate，再验证源决策仍为当前版本，且每个修复目标仍未关闭。源决策必须已经使用原始 probe observations 完成交叉验证；历史 schema、缺少任务特定探针或存在“决策 PASS、原始证据 `NOT_ASSESSED`”时，必须先重新 Review，不能直接进入 Repair。任何足以决定最终结论且 disposition 为 `ABANDON` 的 Hard Gate 均不得进入修复流程。
2. 按“仅限最终结果”的边界重新裁决现有发现，并执行一次**修复前独立缺陷发现轮次**，不得只复述源决策。使用论文、题面、`steps.json`、`grading_spec.json`、checker 和资源重新搜索遗漏问题，并重新裁决审核 skill 定义的全部 `scientific_risk_patterns`。对模拟题必须重新建立 `simulation_parameter_matrix.json`，沿“体系/初态 → 前序参数 → 派生参数 → 后序步骤 → 分析 → Gold/容差 → checker”检查闭包；坐标问题只是该依赖链的一种表现。移除仅基于未读取的过程或轨迹产物，或仅基于宿主机与容器路径不一致的发现。将其余每项已确认缺陷分类为 `AUTO_FIX`、`ASSISTED_FIX` 或 `ABANDON`。
3. 在 Harbor 问题包之外，将源包复制为不可变的 `snapshot/` 和可编辑的 `candidate/`。
4. 构建最终核心输出评分映射、`scientific_claim_matrix.md`、`simulation_parameter_matrix.json` 和 `probe_plan.json`。对快照运行审核 skill 的机械收集器，核对 `instruction.md` 的 `assets` 与题包内 `resources.json` 的声明一致性；存在明确 HTTP(S) URL 时使用 `--probe-urls` 做轻量状态检查，并运行所有适用 checker 探针。不得调用 Playground 拉取资源或下载资源正文。若存在 `ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE`，立即终止：该包本应为 `SCREENED_OUT`，不得创建或继续 candidate。运行每项目标回归测试，并要求出现预期失败，作为“修复前失败、修复后通过”证据中修复前失败的一半。仅能在容器中复现、而本地无法复现的行为应记录为自动化限制，不得认定为缺陷。
5. 为每个拟修改字段建立影响矩阵：

   ```text
   论文/公开证据 → 体系与初始状态 → instruction/前序步骤
   → 派生参数 → 后序步骤 → 分析协议
   → resources/task 配置 → grading_spec/Gold/容差 → checker
   ```

   只允许以下闭包动作：复制论文明确值；按论文信息唯一推导并记录公式、输入、单位；同步题包已有定义；以物理不变量或显式变换保留表示等价；以收敛/不变性证据保留 solver-selectable 参数。禁止只把 `z` 改成 `x`、凭经验补值、采用软件默认值/其他论文值、放宽容差或修改 checker 掩盖欠定合同。

   合同修复必须按科学与公开证据决定，不能仅把题面改成迎合现有 checker。任何受影响文件未同步或未明确证明无需修改，都视为未完成。
6. 仅应用有证据支持且映射到已确认缺陷的变更。唯一确定的检查器防御、路径声明同步、奖励接线和公开评分契约一致性均属于可修复范围。修复若需要选择晶体学定义、物理条件、Gold 或容差，必须使用论文/权威公开证据并归类为 `ASSISTED_FIX`；证据不能唯一决定时不得猜测。对于方法—论文绝对值错配或合成 Gold，可选择两条证据化路径：把题面、输入、Gold 和 checker 一起修正为论文一致的绝对值复现；或在原核心科学目标本来就是比较趋势/排序时，改为直接评分论文或权威来源支持、且对缩小体系仍有适用依据的关系。不得只替换 Gold 数字、用拟合数值冒充计算真值，或未经授权把绝对值任务改成不同的关系任务。
7. 记录变更路径、变更前后哈希、理由、证据、影响矩阵和补丁。
8. 对候选包运行相同的收集器、目标回归测试和探针；要求修复后通过，并保留前后证据对比。通用样例必须保留，同时为每个核心自变量、主键、坐标、单位、边界和评分敏感参数依赖运行任务特定变体。适用时至少包含 `semantic_equivalence:rotated-frame`、`minimal_exploit:wrong-physical-direction` 和 `component_isolation:upstream-choice`。
   非有限数值、错误类型、缺失字段、空或格式错误的输出、重复标识符、不安全格式、随机或常量结果，以及与任务相关且明显错误的最终结果，必须得到零分或保持在通过阈值以下。此前有效的最终输出必须保持相同分数或获得更符合科学合理性的分数。
9. 对候选包执行一次**从空白结论开始的完整复审**，不得复制源决策的 criterion/probe/pattern rationale。复审必须重新阅读论文，重建模拟参数矩阵，按检查责任矩阵重新执行所有 Hybrid 检查，并重新评估全部 2.1–2.8、C01–C07、六个硬门槛、全部科学问题 pattern、四类参数、Gold/容差、评分链和资源；机械候选为零不构成通过证据。使用候选包新生成的 observations；仍不得读取或检查 `solution/`。
10. 使用审核验证器和所有候选 observations 验证新的 `agent_final_decision.json`：

    ```bash
    python .cursor/skills/materials-benchmark-review/scripts/validate_agent_decision.py \
      <path>/reaudit_agent_final_decision.json \
      --probe-observations <path>/candidate_checker_observations.json \
      --probe-observations <path>/candidate_task_specific_observations.json
    ```

11. 使用随附模板编写 `repair_report.json` 并进行验证：

    ```bash
    python .cursor/skills/materials-benchmark-repair/scripts/validate_repair_report.py \
      <path>/repair_report.json
    ```

    只有独立完整复审结论为 `PASS`、原始证据与决策状态一致、所有修复目标和新发现均关闭，且 `repair_report.json` 验证通过的 `REPAIRED` 候选包才可发布；否则必须保留原始包及全部证据。所有修改必须位于 `/personal/qa_review/<cluster>/<theme>/<paper>/candidate`；源 Harbor 问题包保持不变。

兼容既有自动检查的英文表述：每个回归必须保留 `fail-before/pass-after` 证据；只有
equal-depth Review is
    `PASS`
且上述独立复审和原始探针同时满足时，候选包才可发布。

## 结果类型

- `REPAIRED`：复审为 `PASS`，所有修复目标均已解决，回归测试通过。
- `PARTIALLY_REPAIRED`：复审为 `CONDITIONAL`，没有硬门槛失败，未解决问题已明确列出；不得发布。
- `ABANDONED`：复审为 `REJECT`，或安全修复需要猜测或重定义任务。
- `ROLLED_BACK`：修改或验证失败；原始包保持不变。
- 真正的 `NOT_ASSESSABLE` 仍可恢复处理，不等同于放弃。

面向用户的回复必须说明结果类型、已修复问题或阻塞问题，以及候选包、证据和报告的位置。
