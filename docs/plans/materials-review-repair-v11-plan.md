# 材料 Benchmark 质检/修复 v11 重构计划

状态：草案（待确认）
适用 skills：`.cursor/skills/materials-benchmark-review`、`.cursor/skills/materials-benchmark-repair`
参考：`references/出题-质检-修复.md`、当前 `references/scoring-rubric.md`、用户提供的 C01–C07 指标示例与 LLM 语义审查表格图。

---

## 0. 一句话目标

把当前「只有 `PASS` / `CONDITIONAL` / `REJECT` / `ABANDONED` 的黑箱结论」升级为
**「七维可分析评分（C01–C07，每维 0–100%）+ 明确的确定性检查表 + 明确的 LLM 检查表 + 修复前后指标对比」**，
并产出一份用户能读懂的飞书文档，让每一步「做了什么、目的、结果、下一步」都清晰可追。

---

## 1. 背景与痛点

当前实现（v9/v10）已经能跑，但对使用者不透明：

1. 结论过粗：最终只暴露 verdict 和一个 0–100 总分，用户无法看出「哪一类问题拖了后腿、修复到底改善了什么」。
2. 五维内部维度（scientific validity / instruction answerability / checker-Gold / robustness / solution completeness）与用户心智模型（领域准入、契约完整、评分语义、泄漏、可复现…）不完全对应，难以按维度分析。
3. 分类依赖关键词词表预筛（`materials_prescreen`），对 instruction 的结构化语义（Problem background / Approach / Reproduction target）利用不足；`NON_MAT` 之外的 `MAT_WRAPPER`/`AMBIGUOUS` 被当成「排除」，与「Wrapper 也是一种任务」的意图不一致。
4. 每个检查项「读哪些文件」在 skill 文档里不够显式，使用者难以核对。

目标是：**保留现有确定性引擎与证据合同的严谨性，重新组织为可分析的七维评分与两层清晰流程，并显式声明每个检查项的输入文件。**

---

## 2. 目标产物（Deliverables）

1. **新评分模型 C01–C07**：七个维度（准入 1 + 确定性 3 + 科学性 3，其中 C07 跨两族），每维 `points_earned / max_points` 归一化为 0–100%，可单独展示、可做修复前后对比（delta，单位 pp）。
2. **确定性检查表（D 层）**：编号 / 名称 / 说明·关键文件 / 方法。全部可修复。
3. **LLM 检查表（A/L 层）**：编号 / 名称 / 判断方向 / 核心输入（关键文件）/ 说明，对齐用户图片表格写法与 `references/出题-质检-修复.md`。
4. **新流程图**：材料准入 → 确定性检查 → LLM 审查 → 打分/处置 →（CONDITIONAL）修复 → 复审。
5. **报告结构升级**：`audit_report.json` / `audit_report.md` 输出七维分数、每维 findings、修复前后对比块。
6. **飞书文档**：包含上述所有表格、流程图、判分依据、指标与数值评分依据。

---

## 3. 新评分模型 C01–C07（提案，待确认权重）

每个维度从满分起扣分，扣分沿用现有 severity 比例（`FATAL=1.0 / HIGH=0.4 / MEDIUM=0.2 / LOW=0.1` × 维度满分），
`normalized = points_earned / max_points`，展示为百分比。总分 = 各维 `points_earned` 之和，按权重归一到 0–100。

维度分两大家族：**确定性家族（D 层可机械判定，全部可修复）** 与 **科学性家族（A 层 Agent 判断 + 代码校验引用）**。
「题目设计是否完整、自洽」的**确定性部分**合并为单一维度 C02（原 C02 + C04）；其**科学性部分**（必要定义是否齐全、方法是否恰当）归入 C03。

| 编号 | 维度 | 家族 | 主要判定层 | 关键输入 | 说明 |
| --- | --- | --- | --- | --- | --- |
| C01 | 领域准入 | 准入 | **仅 A 判定**（取消 D 预筛） | instruction（Problem background / Approach / Reproduction target） | 是否真正材料任务；非材料直接放弃（Hard Gate），`MAT_WRAPPER` 视为合法任务参与后续评分 |
| C02 | 题目设计完整性与文件一致性 | 确定性 | D | instruction、tests/grading_spec.json、tests/checker.py、tests/test.sh、solution | 合并原 C02+C04：**机械可查的完整与自洽**——文件齐全、入口存在、权重归一、instruction 内部各节自洽、跨文件名字/格式/字段/路径对齐 |
| C03 | 科学有效性与方法可解性 | 科学性 | A | instruction（Approach / Reproduction target）、paper（必读） | **科学判断**：方法是否恰当、必要科学定义是否齐全（缺 k-mesh/超胞/单位/边界等是否属必要缺失，回归原文）、题目能否被独立且公平地解出 |
| C04 | 评分语义 | 确定性 | D + 动态 | tests/checker.py、grading_spec、动态探针 | checker 是否真评核心科学任务（读取、绑定、权重、返回值、方向） |
| C05 | 答案泄漏 | 科学性 | A + D | instruction、grading_spec、solution 边界 | instruction 是否泄漏数值答案（方法/公式不算泄漏）；solution 边界是否被 checker 依赖 |
| C06 | 可复现性 | 科学性 | A + D 资源 | paper（必读）、instruction、直接输入探针 | 是否忠实论文、必要直接输入是否可得、正确执行能否得高分。**直接输入探针**：对 instruction 显式点名、任务直接消费、不可或缺且无科学等价替代的外部输入/服务做可达性核查（`probe_resources.py`），只探这类对象；求解器应自生成的结构/轨迹/模型、常规 DFT/MD 参数、可替代软件、论文历史软件版本清单一律不探。永久不可得 → Hard Gate `INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE`；审查主机瞬时失败 → `NOT_ASSESSABLE` |
| C07 | 难度与可审计性 | 确定性+科学性 | 动态 + A | 动态区分度/等价探针、checker | 评分是否有区分度（单调/灵敏/饱和/特异/局部贡献），结果是否可审计 |

> 待确认：
> - 七维权重（示例：C01 10 / C02 20 / C03 20 / C04 20 / C05 10 / C06 10 / C07 10 = 100，可调）。
> - 是否保留旧五维作为内部计算中间层再映射到 C01–C07，还是直接以 C01–C07 为 finding 归属维度（建议：直接以 C01–C07 为归属维度，findings 重新映射，减少双层复杂度）。
> - 「答案泄漏 C05」「领域准入 C01」偏门禁类，是否既给百分比也给布尔门（建议：百分比用于分析，同时保留 Hard Gate 布尔用于处置）。

### 3.1 Hard Gate 与维度关系

四个 Hard Gate 保留，绑定到维度上，命中即 `REJECT`（但仍展示可评估的七维分数用于分析）：

- 非材料任务 → C01
- 科学目标无效 / 不可恢复必要定义 → C03
- checker 不评核心任务且不可修复 → C04
- 不可替代直接输入永久不可得 → C06

---

## 4. 新整体流程（提案）

```
题包
  │
  ▼
[Stage 0 材料准入]  A 读 Problem background / Approach / Reproduction target 权威判定（取消关键词预筛）
  │   ├─ NON_MAT ──────────────► fail-fast 直接放弃 REJECT（C01 Hard Gate），不读 paper
  │   └─ MAT_CORE / MAT_METHOD / MAT_WRAPPER / AMBIGUOUS → 继续（Wrapper 也算任务）
  ▼
[Stage 1 确定性检查 D 层，可修复]
  D1 输出文件声明一致
  D2 instruction 内部一致（Workflow steps / Output files / Output contract / Self-check）
  D3 评分器代码健康
  D4 权重归一化
  D5 题包文件完整（含 Harbor 入口 tests/test.sh）
  D6 Checker 核心任务映射审查（是否真评科学任务，静态）
  D7 动态鲁棒性与区分度（negative / discrimination / equivalence / component-isolation）
  │
  ▼
[Stage 2 LLM 审查 A 层，每项声明读取文件；默认 paper-grounded]
  A1 领域与能力目标一致   A2 科学有效性与方法可解（含必要定义齐全，必读 paper）
  A3 答案泄漏与身份泄漏   A4 论文忠实与可复现（必读 paper）   A5 Gold 可信度（必读 paper）
  │
  ▼
[Stage 3 打分与处置]  七维 C01–C07 归一化 + 加权总分 + Hard Gate + verdict + publishable
  │   ├─ PASS           ─► publishable=true，可发布
  │   ├─ CONDITIONAL    ─► 进入修复
  │   ├─ REJECT         ─► 放弃（分数<60 或命中 Hard Gate）
  │   └─ NOT_ASSESSABLE ─► 证据补齐后复审
  ▼
[Stage 4 修复（仅 CONDITIONAL）]  AUTO_FIX / ASSISTED_FIX / ABANDON
  │   隔离副本 → 应用补丁 → 回归 → 等深复审
  ▼
[Stage 5 复审与对比]  重跑 Review，输出修前/修后 C01–C07 与 delta；成功则 publishable=true
```

关键变化点：

1. **材料准入前置、纯 Agent 判定、放弃制**：取消关键词预筛；非材料直接 REJECT，不再进入后续；`MAT_WRAPPER` 不再被「排除」而是作为合法任务继续评分。
2. **确定性层集中在前**，明确「这些问题都可修复」，为修复阶段提供确定的、可回归的目标。
3. **LLM 层每个检查项显式声明输入文件**（见第 6 节表格）；A2/A4/A5 必读 paper，常规路径默认 paper-grounded E1。

---

## 5. 分类改造：用 instruction 结构化字段判定

现状：`materials_prescreen` 用关键词词表 + `has_term` 命中轴组合做预筛。
改造：**取消关键词预筛，分类完全由 Agent 读 instruction 结构化字段做权威判定**（不再保留 D 层词表兜底）。

- 读取字段：`## Problem background`、`## Approach`、`## Reproduction target`（如字段缺失，Agent 读全文判定并记 `AMBIGUOUS`，不再走关键词预筛）。
- Agent 输出：classification ∈ {MAT_CORE, MAT_METHOD, MAT_WRAPPER, NON_MAT, AMBIGUOUS} + 每类的原文引用（`package_file` + `package_quote`）。
- 处置：仅 `NON_MAT` 触发 C01 Hard Gate 放弃；其余全部继续（含 `MAT_WRAPPER` 与 `AMBIGUOUS`，`AMBIGUOUS` 可要求补证据后复审）。
- 代码职责收窄为「校验」而非「判定」：`materials_prescreen` 关键词分类逻辑移除；`validate_materials_qualification` 保留并强化——引用必须在 instruction 原文中、标签必须合法、三段字段的证据必须齐全。
- 影响：`audit_package.py` 中 `MATERIAL_TERMS` / `has_term` / `materials_prescreen` 分类分支删除；分类不再有确定性来源，Agent 未提供权威分类时该题 `NOT_ASSESSABLE`（不能凭词表放行）。

---

## 6. 检查表设计（写入 SKILL）

### 6.1 确定性检查（D 层，不调 LLM，全部可修复）

| 编号 | 名称 | 说明 / 关键文件 | 方法 |
| --- | --- | --- | --- |
| D1 | 输出文件声明一致 | instruction 的 `Output files` / `Output contract` 与 grading_spec `output_contract` 是否匹配；关键文件：`instruction.md`、`tests/grading_spec.json` | 正则抽取输出路径 + 集合比对 |
| D2 | instruction 内部一致 | `Workflow steps` 的 scored 输出 ↔ `Output files` ↔ `Output contract` ↔ `Self-check`（如有）四处声明一致；关键文件：`instruction.md` | 分节正则解析 + 文件名/字段/格式集合比对 |
| D3 | 评分器代码健康 | 语法、绑定评分函数是否含 always-pass / 字面除零 / 方向反转；关键文件：`tests/checker.py` | `ast.parse` + AST 模式识别 |
| D4 | 权重归一化 | 评分权重之和是否为 1、零权重项识别；关键文件：`tests/grading_spec.json`、`tests/checker.py` | 数值求和比对（容差 1e-6） |
| D5 | 题包文件完整（含 Harbor 入口） | 必要角色齐全可解析：`instruction.md` / `tests/checker.py` / `tests/grading_spec.json` / `tests/test.sh`（Harbor 入口）/ `solution` | 文件存在性 + `parse_status` |
| D6 | Checker 核心任务映射审查（静态） | 核心输出是否被读取/绑定/计分，是否只查存在或只比硬编码数值；关键文件：`instruction.md`、`tests/checker.py`、`tests/grading_spec.json` | 契约链正则映射 + AST 绑定分析 |
| D7 | 动态鲁棒性与区分度 | 真实运行 checker：negative（缺失/空/畸形/随机/重复/稀疏/非有限）、discrimination（质量梯度单调）、equivalence（等价表示不变）、component-isolation（单组件不能过）；关键文件：`tests/test.sh`、`tests/checker.py`、外部 fixture | 执行 `tests/test.sh` + reward 比较 |

### 6.2 LLM Agent 检查（A/L 层，agent 判断 + 代码校验引用）

| 编号 | 名称 | 判断方向 | 核心输入（关键文件） | 说明 |
| --- | --- | --- | --- | --- |
| A1 | 领域与能力目标一致 | 是否材料任务 + 声称能力 ↔ 实评是否一致 | instruction（Problem background / Approach / Reproduction target）+ tests | 分类 MAT_CORE/METHOD/WRAPPER/NON_MAT/AMBIGUOUS；能力目标与 checker 实评是否对齐 |
| A2 | 科学有效性与方法可解（含必要定义齐全） | 方法是否恰当、必要科学定义是否缺失、题目能否独立公平解出 | instruction（Approach / Reproduction target / Workflow steps）+ **paper（必读）** | 缺结构坐标/超胞/k-mesh/单位/边界等是否属「必要缺失」需**回归论文原文**确认原文是否给出；允许等价软件与求解器参数；信息是否足以唯一/公平作答 |
| A3 | 答案泄漏与身份泄漏 | instruction 是否暴露不该暴露的信息 | instruction + grading_spec + paper | 数值结果泄漏（方法公式不算）；论文标题/作者/专有名称等可追溯身份泄漏 |
| A4 | 论文忠实与可复现 | instruction/数据/参数/Gold 是否忠实论文、能否复现 | **paper（必读）** + instruction + 直接输入探针 | 复现类型 EXACT/METHOD（默认）/EXTENSION；对照论文核对方法、数据、样本、参数、软件版本；正确执行能否得高分 |
| A5 | Gold 可信度（参考标准 1.8） | Gold/容差/评分依据是否可信、是否独立于被测方法 | tests/grading_spec、tests/checker.py、**paper（必读）** | 见下方「A5 Gold 可信度判定清单」 |

> **取消 paper 触发开关**：不再用 SCIENTIFIC_CONFLICT / NECESSARY_INFORMATION_MISSING / GOLD_PROVENANCE_UNCERTAIN / EXPLICIT_REPRODUCTION_CLAIM 决定是否读 paper。改为**固定规则**：A2（必要定义齐全）、A4（论文忠实与可复现）、A5（Gold 可信度）**恒读 `paper/`**；A1、A3 以题包内文件为主，需要时可扩展至 paper。
> 因此本 skill 的常规审查路径**默认进入 paper-grounded E1**；唯一例外是 Stage 0 命中 Hard Gate（`NON_MAT` 非材料）时 fail-fast，不读 paper。
> 所有 A 层结论必须落到题包/论文原文引用，由确定性代码核验（引用存在、标签合法、哈希绑定），防止 agent 凭空发挥。

#### A5 Gold 可信度判定清单（参考标准 1.8）

审查 Gold Standard 的来源与质量，逐项对照论文原文标注：

- 是否来自真实实验；
- 是否由专家人工整理；
- 是否来自论文正文或补充材料；
- 是否由某个计算工具生成；
- 是否通过图表数字化获得；
- 是否存在测量误差或标注不确定性；
- 是否独立于被评价的方法；
- 评分容差是否有科学依据。

若 Gold 只是某软件的输出，则它更适合衡量「与该软件的一致性」，不一定代表真正的材料科学正确性，需显式标注。

对可能存在多个合理答案的任务，进一步判断 checker 是否支持：

- 数值容差；
- 集合级匹配；
- 排名评价；
- 证据链评价；
- 多个可接受解。

---

## 7. 维度 × 检查项映射（findings 归属）

| 维度 | 家族 | 主要 D 项 | 主要 A 项 |
| --- | --- | --- | --- |
| C01 领域准入 | 准入 | —（取消预筛） | A1 |
| C02 题目设计完整性与文件一致性 | 确定性 | D1, D2, D4, D5 | — |
| C03 科学有效性与方法可解性 | 科学性 | — | A2 |
| C04 评分语义 | 确定性 | D3, D6, D7 | A5（部分） |
| C05 答案泄漏 | 科学性 | D6（solution 边界） | A3 |
| C06 可复现性 | 科学性 | D5（资源）, 直接输入探针 | A4 |
| C07 难度与可审计性 | 确定性+科学性 | D7（区分度/等价） | A2/A5（部分） |

---

## 7.1 Stage 3 打分与处置（详）

Stage 0–2 产出的 findings 全部落到 C01–C07 后，Stage 3 做四步：**归一化 → 加权总分 → Hard Gate 覆盖 → verdict/publishable**。

### 步骤 1：逐维扣分与归一化

- 每维从满分起扣分，severity 比例沿用：`FATAL=1.0 / HIGH=0.4 / MEDIUM=0.2 / LOW=0.1`，扣分量 = `severity × 维度满分`，同维多 finding 累加且 clamp 到 `[0, max]`。
- `normalized(%) = points_earned / max_points × 100`，即报告里展示的每维百分比。

### 步骤 2：加权总分

- 总分 `= Σ (weight_i × normalized_i) / Σ weight_i`，落到 0–100（权重示例见 3 节，冻结后写入 `references/scoring-rubric.md`）。
- 兼容历史白名单：同时保留旧 0–100 总分字段，历史归档标注旧版口径。

### 步骤 3：Hard Gate 覆盖（优先于分数）

命中任一 Hard Gate 直接 `REJECT`，但仍展示七维分数用于分析：

- 非材料任务 → C01
- 科学目标无效 / 不可恢复必要定义 → C03
- checker 不评核心任务且不可修复 → C04
- 不可替代直接输入永久不可得 → C06

### 步骤 4：verdict 与 publishable 判定

| verdict | 触发条件 | publishable | 去向 |
| --- | --- | --- | --- |
| PASS | 总分 ≥ 80 且无未解决 HIGH/FATAL 且未命中 Hard Gate | true | 直接可发布 |
| CONDITIONAL | 总分 60–79，或存在**可修复**的 HIGH（有充分证据），未命中 Hard Gate | false（修复后可转 true） | 进入 Stage 4 修复 |
| REJECT | 总分 < 60，或命中任一 Hard Gate | false | 放弃 |
| NOT_ASSESSABLE | 关键证据暂缺（如缺 Harbor 入口导致动态探针不可跑、Agent 未给权威分类、必读 paper 缺失） | false | 证据补齐后复审，不得凭空放行 |

- 终态字段统一：`disposition: PASS|CONDITIONAL|REJECT|NOT_ASSESSABLE` + `publishable: bool` + `repair_state`，避免 `PASS` 与 `PUBLISHED` 语义分裂。
- 非关键维度（如 C07 部分区分度证据缺口）不得整体升级为 `NOT_ASSESSABLE`；只在其所属维度扣分。
- CONDITIONAL 与 REJECT 的分界由「是否存在证据充分的可修复路径」决定：无证据 / 需改核心科学定义 → 归 REJECT 或修复阶段 ABANDON。

---

## 8. 修复联动与指标对比

- 修复类别沿用：`AUTO_FIX` / `ASSISTED_FIX` / `ABANDON`（无人工介入档）。
- 可修复目标以 **D 层项** 为主（结构/一致性/健康/权重/入口/checker 覆盖），以及有充分证据的 A 层缺失定义补全。
- 修复后重跑 Review，输出修前/修后 **C01–C07 百分比与 delta（pp）**，形如：

  | 维度 | 指标 | 修前 | 修后 | 变化 |
  | --- | --- | --- | --- | --- |
  | C04 | 评分语义 | 14.6% | 68.0% | +53.4pp |
  | C02 | 题目设计完整性与文件一致性 | 2.8% | 28.1% | +25.3pp |
  | … | … | … | … | … |

- 终态字段统一：可发布状态用单一字段表示（建议 `publishable: true` + `disposition: PASS|CONDITIONAL|REJECT|NOT_ASSESSABLE` + `repair_state`），解决 `PASS` 与 `PUBLISHED` 不统一问题。

### 8.1 修复 skill 需要匹配的改动

Reviewer 改造后，Repair skill（`materials-benchmark-repair`）需同步以下几处，保证首尾一致：

1. **消费七维报告**：修复以 Reviewer 输出的 C01–C07 + findings 为输入，可修目标以 **C02/C04（确定性家族：结构/一致/健康/权重/入口/checker 覆盖）** 为主；C03/C06 的必要定义补全仅在有充分 paper 证据时做。
2. **终态字段对齐**：复审通过后写统一的 `disposition=PASS` + `publishable=true` + `repair_state`，不再产出 `PUBLISHED` 这类并行状态。
3. **修前/修后 delta 输出**：复审重跑 Review 后按 C01–C07 输出修前/修后百分比与 delta（pp），与第 8 节样例一致。
4. **证据精度匹配矩阵（关键防呆）**：`ASSISTED_FIX` 必须满足「证据支持的精度 ≥ 修改的精度」，防止 agent 为消除 finding 而给 checker/solution 私造题面从未定义的字段/协议：
   - 声称的本地 source **文件不存在 → `BLOCKED_EVIDENCE`**（不能只在文件存在时才校验 quote）；绝对路径限制在允许的证据根内并存哈希。
   - quote 存在但只支持「有此文件」时，**不得新增字段/类型/单位/必选性**；敏感操作需类型匹配证据：新增 JSON key/CSV 列→需字段级 schema；改 Gold/tolerance→需数值+单位+来源或可复核推导；改权重/阈值→需评分合同+数学证明。
   - 仅「加异常捕获 / 修 Harbor 路径合同」这类无需科学论文的操作，用崩溃栈与现有代码即可支撑。
5. **分类与放弃对齐**：`NON_MAT` 不进入修复；核心科学定义需改动或证据不足 → `ABANDON`（材料版放弃文案参考 `references/出题-质检-修复.md`）。
6. **过程文件不作 checker 必需项**：修复不得把过程/中间文件改成 checker 必检字段（防作弊交由 trace，另属他任务）；checker 仍聚焦 instruction 声明的核心输出。
7. **取消 `no_paper` 模式带来的证据规则调整**：现状 SKILL 里「paper 证据仅在 `paper_grounded` 审查里有效，`no_paper` 审查不能授权 paper 证据」的分支需改写——因为审查已默认 paper-grounded（唯一非 paper 路径是 `NON_MAT` fail-fast，且永不进修复）。改为：**paper 证据始终可用，但必须绑定 source audit 已哈希的那一个 `paper/**` 文件**（哈希不匹配或未绑定 → `BLOCKED_EVIDENCE`）。删除 `no_paper` 相关的判定与文案，`run_repair.py` 中按 paper 模式分支的逻辑相应简化。

### 8.2 「能修 / 放弃」对照表（操作类型 × 所需证据精度 × 判定）

依据「证据支持的精度必须 ≥ 改动的精度」。证据不足即降级为 `BLOCKED_EVIDENCE`（`ABANDON`），禁止改动即 `POLICY_VIOLATION`。

| 操作 / 改动类型 | 所需证据（精度） | 判定 |
| --- | --- | --- |
| 加异常捕获（防 checker 崩溃） | 崩溃栈 + 现有读取代码 | AUTO_FIX |
| 修正 Harbor 路径契约（容器路径对齐） | Harbor 路径契约 + 现有路径代码 | AUTO_FIX |
| 补缺失的 `solution/solve.sh`（整备完整性） | 现有题包结构 | AUTO_FIX |
| 跨文件字段名/格式/路径对齐（一致性） | `instruction.md` / `grading_spec` 原文 | AUTO_FIX |
| 权重归一化修正 | `grading_spec` / checker 权重字段 | AUTO_FIX |
| 修 JSON/YAML/TOML 语法错误、创建缺失输出目录（2.2） | 崩溃/解析栈 + 现有配置 | AUTO_FIX |
| 补输出字段的单位/排序/去重/缺失值规则（2.3） | 题面或论文明确规则 | ASSISTED_FIX；缺则不新增（`BLOCKED_EVIDENCE`） |
| 明确 REQUIRED/RECOMMENDED/ALLOWED/FORBIDDEN 与联网/等价工具许可（2.3） | 题面现有约束 + 论文方法边界 | ASSISTED_FIX |
| 补随机种子（2.3） | 题面明确或论文数值方法要求 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 将 DB 主页替换为具体 accession / 修失效官方链接 / 加稳定镜像（2.4，仅限 C06 会探测的不可或缺直接输入） | 可达且身份匹配的官方来源或镜像 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 固定数据/数据库版本、补 checksum 与文件大小（2.4） | 官方版本页 + 校验值 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 修软件包名/版本、补系统依赖/求解器、加 lock file/容器（2.4） | 现有 env 配置 + 官方包索引 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 修正明显不合理的时间/内存/存储预算（2.4） | 现有环境配置 + 运行/崩溃证据 | AUTO_FIX |
| 新增 JSON key / CSV 列检查 | 字段级 schema：字段名 + 类型 + 必选性 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 新增 NPY 检查 | shape + dtype + 维度语义 + 单位 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 修改 Gold / 目标值 | 明确数值 + 单位 + 来源，或完整可复核推导 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 修改 tolerance | 论文实验误差 / 数值方法误差 / 题面明确容差 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 修改评分权重 / 阈值 | 评分合同字段·值 + 数学证明 | ASSISTED_FIX；缺则 `BLOCKED_EVIDENCE` |
| 修正科学方法 | 论文或公开 instruction 对方法的明确要求 | ASSISTED_FIX；缺则 `ABANDON` |
| 声称的本地 source 文件不存在 | —（无法核验） | `BLOCKED_EVIDENCE` → `ABANDON` |
| 用 solution/Oracle 或 metadata 当科学/schema/评分证据 | —（证据根不合格） | `POLICY_VIOLATION` |
| 把过程/中间文件改成 checker 必检项 | —（本任务禁止，防作弊归 trace） | `POLICY_VIOLATION` / `ABANDON` |
| 改核心科学问题/端点/材料体系/复现类型 | —（`core_science_change`） | `ABANDON` |
| 猜参数/数值、无证据降阈值、拿 checker 通过当科学证据 | —（红线） | `POLICY_VIOLATION` / `ABANDON` |
| 不可替代的核心直接输入永久不可得 / 需未授权权限 / 无法合法获得（2.4） | —（Hard Gate C06） | `ABANDON` |
| Gold 来源无法验证 / 与论文明显冲突（2.7） | —（gold 身份问题，禁止复制论文 Gold 数值） | `ABANDON` |
| 存在多个合理答案但无法建立公平评分、或 checker 必须重定义任务才能修（2.7） | —（需重定义任务） | `ABANDON` |
| 同一 audit 的批量修复两次尝试仍未达 PASS / 修后仍存 FATAL（2.7） | —（收敛失败） | `ABANDON` / `ROLLED_BACK` |
| `NON_MAT` 题包 | —（不进修复） | 不受理 |

> 该表是 §8.1「证据精度匹配矩阵」的可查视图，落到 `run_repair.py` 的证据校验与 `materials-benchmark-repair/SKILL.md`。

### 8.3 与 `references/出题-质检-修复.md` §2.2–2.8 的对应

参考文档「修复」为第 2 章，其小节按文件实际顺序为：2.1 读取审查结果并制定修复计划、2.2 修复题包结构和配置、2.3 补充和规范 Instruction、2.4 修复数据/软件和环境问题、2.5 修复 Checker 的覆盖和评分问题、2.6 在隔离工作区中安全修复、2.7 无法可靠修复时直接放弃、2.8 修复后自动重新审查、2.9 固定保存修复结果。
本节目的：把 **Harbor 通用修复机制** 与 **材料科学内容约束** 分开——通用小节按机制复用、不从中重新推导材料规则；材料专属小节映射到本计划的可修/放弃边界。参考文档以生物学为例，材料域按同构语义映射（如 gene/protein ID 类型 → 材料的结构/相/体系标识；代谢模型 → DFT/MD 结构·轨迹·模型）。

#### 8.3.1 小节 → 类别映射

| 小节 | 一句话意图 | 类别 | 对应 plan 锚点 |
| --- | --- | --- | --- |
| 2.2 修复题包结构和配置 | 修路径 / 文件名一致 / 配置格式 / 权重 / 输出目录，不改科学目标 | Harbor 通用 | §8.2 结构·一致·权重·配置格式行、C02 |
| 2.3 补充和规范 Instruction | 不改任务含义下补输入输出 / 字段 / 单位 / 操作许可；无依据不猜造参数 | 通用机制 + 内嵌材料约束 | §8.2 instruction 规范行；约束 → §8.1 item 4、§8.3.3 |
| 2.4 修复数据、软件和环境问题 | 修 accession / 链接 / 镜像 / 版本 / checksum / 依赖 / 预算；核心数据不可得则放弃 | 通用机制 + 内嵌材料放弃边界 | §8.2 资源·环境行；放弃 → C06 Hard Gate |
| 2.5 修复 Checker 的覆盖和评分问题 | 修 checker 覆盖 / 绑定 / 方向 / 权重 / 鲁棒性，改动必配回归测试 | **材料直接复用** | C04 / C02（确定性家族）、§8.1 item 1、§8.2 checker 行 |
| 2.6 在隔离工作区中安全修复 | `.benchmark_repair_tmp` 隔离 → 测试通过才写回 → 失败回滚 | Harbor 通用（修复环境） | Stage 4「隔离副本→应用补丁→回归」 |
| 2.7 无法可靠修复时直接放弃 | 列举 ABANDON 触发 + 「不得强行 PASS」红线 | **材料专属决策** | §8.1 item 5–6、§8.2 放弃 / 红线行、§8.3.3 |
| 2.8 修复后自动重新审查 | 重跑 Auditor 比对修前 / 修后，产出 REPAIRED / … / ROLLED_BACK | Harbor 通用（复审闭环） | Stage 5、§8.1 item 3、§8 delta 表 |

#### 8.3.2 材料可修（CAN change）——通用机制 + 直接复用 2.5

- **直接复用 2.5**：checker 覆盖 / 评分修复整体映射到确定性家族 **C04（评分语义）+ C02（完整性）**，落在 §8.2 的 checker / 结构 / 权重行；每次改 checker 必加回归测试（§8.1 item 1、Stage 4 回归、2.8 复审闭环）。
- **通用机制可修**：结构 / 配置（2.2）、instruction 规范（2.3，仅在题面或论文有依据时）、资源 / 环境修复（2.4，且**仅针对 C06 会探测的不可或缺直接输入**——求解器应自生成的结构 / 轨迹 / 模型、常规 DFT/MD 参数、可替代软件、论文历史软件版本一律不修不探），均已在 §8.2 新增对应行。
- **材料专属可修（受证据精度矩阵约束，§8.1 item 4）**：补必要科学定义（k-mesh / 超胞 / 单位 / 边界条件）仅当论文原文给出；补单位 / 排序 / 去重 / 容差 / 随机种子仅当题面或论文明确。

#### 8.3.3 材料放弃（CANNOT change）——材料科学内容约束

来自 2.7（及 2.3 / 2.4 的放弃条款），与 §8.1 item 5–7、§8.2 放弃 / 红线行一致：

- **核心科学身份不可改**：核心科学问题、端点、材料体系、复现类型（EXACT / METHOD / EXTENSION）→ `core_science_change` → `ABANDON`。
- **Gold / 方法身份**：Gold 来源无法验证或与论文明显冲突 → `ABANDON`；不得复制论文 Gold 数值、不得读 solution / Oracle 或 metadata 充当科学 / schema / 评分证据（`POLICY_VIOLATION`）。
- **证据不足 / 类型不匹配**：无证据或「证据精度 < 改动精度」→ `BLOCKED_EVIDENCE` → `ABANDON`；红线包括猜参数 / 数值、无证据降阈值、拿 checker 通过当科学证据。
- **不可替代直接输入永久不可得 / 需未授权权限 / 无法合法获得** → C06 Hard Gate → `ABANDON`。
- **过程 / 中间文件不得改为 checker 必检项**（§8.1 item 6，防作弊归 trace，checker 仍聚焦 instruction 声明的核心输出）。
- **无法建立公平评分**：多个合理答案无法定义公平评分、或 checker 必须重定义任务才能修 → `ABANDON`。

#### 8.3.4 与统一约束的一致性

- **no_paper 模式已移除**：paper 证据始终可用，但每条 paper 证据必须绑定 source audit 已哈希的那一个 `paper/**` 文件，哈希不匹配 / 未绑定 → `BLOCKED_EVIDENCE`（§8.1 item 7）。这正是 2.3「无依据不编造」在材料域的确定性落地——「依据」即已哈希的论文 / 题包原文。
- **证据精度匹配矩阵**（§8.1 item 4 / §8.2）是 2.3「不改任务含义 / 不猜造参数」与 2.7 红线的机器可核验形式。
- **终态字段统一** `disposition + publishable + repair_state` 与 2.8 的四态对齐（批量语义见 §8.4）：`REPAIRED → disposition=PASS & publishable=true`（整包所有阻塞 finding 均解决）；`PARTIALLY_REPAIRED → 部分 finding 解决但仍有未解决 HIGH，disposition=CONDITIONAL & publishable=false`；`ABANDONED → REJECT 族 & publishable=false`；`ROLLED_BACK → 批量应用/回归失败，保持原始题包`。

#### 8.3.5 与用户小节假设的差异（记录）

- 用户假设 **2.2 / 2.3 / 2.4 / 2.6 / 2.7 / 2.8 全为 Harbor 通用、仅 2.5 材料复用**。
- 实读结论：**2.2 / 2.6 / 2.8 确为纯 Harbor 通用；2.5 确为材料直接复用**（与用户一致）。但——
  - **2.7 实为材料专属决策**：其 ABANDON 触发清单与「不得强行 PASS」红线正是材料 CANNOT-change 的核心，并非纯通用机制；已收入 §8.3.3。
  - **2.3 / 2.4 为混合**：修复「机制」是通用，但各自内嵌了材料相关约束 / 放弃条款（2.3「无依据不猜造参数」、2.4「核心数据不可得即放弃」），分别归入 §8.1 item 4 与 C06 Hard Gate。
- 本节按参考文件实际内容归类，未强行套用用户的纯通用假设。

### 8.4 批量修复流程（一次修完 Review 的全部问题，再整包深审）

**改动动机**：旧实现「一次一个 finding、每次整包等深复审」会对同一题包反复迭代很多轮，成本高。改为**一个 audit 的全部可修 finding 一次性修完 → 只做一次等深复审**。

- **计划粒度**：修复计划从「单 `finding_id`」改为「单 `audit_id` + `findings[]`」，每个 finding 各带 `repair_class`（AUTO_FIX / ASSISTED_FIX / ABANDON）、`operations[]`、`evidence[]`、`regression_tests[]`。ABANDON 类只记录理由、不产生 operations。
- **执行顺序**（隔离副本内一次跑完）：
  1. 冻结 core-contract digest、校验 audit 绑定与所有目标 finding 仍 open；
  2. 收集所有 AUTO_FIX/ASSISTED_FIX 的 operations，逐条按证据精度矩阵（§8.1 item 4）校验；**任一 operation 证据不合格 → 该 operation 记 `BLOCKED_EVIDENCE`，不阻断其余合格 operation**；
  3. 对 candidate 应用全部合格 operation，记录前后哈希与证据链；
  4. 跑全部回归（每个 operation 一条语义对应断言，修前失败/修后通过）；
  5. **只做一次**整包等深 Review CLI（同 paper 模式、同 E1 执行级）。
- **终态判定（批量）**：
  - **REPAIRED**：等深复审 `PASS` 且无未解决 HIGH/FATAL、身份不变、无越界改动 → `disposition=PASS`、`publishable=true`，原子换入发布；
  - **PARTIALLY_REPAIRED**：部分 finding 已解决但复审仍非 PASS（尚存未解决 HIGH，或某些 finding 为 BLOCKED_EVIDENCE/ABANDON）→ **不发布，保持原始题包**，`disposition=CONDITIONAL`、`publishable=false`，报告列出「已解决 / 未解决 / 放弃」清单；
  - **ABANDONED**：无任何可修 finding，或复审仍存 FATAL / 命中 Hard Gate / 需改核心科学定义 → `disposition=REJECT 族`、`publishable=false`；
  - **ROLLED_BACK**：批量应用或回归失败 → 恢复原始题包不变。
- **发布不变量**：只有整包复审 `PASS`（无未解决 HIGH/FATAL）才发布；「部分修好」绝不发布，避免带病入库。
- **尝试上限改为按 audit 批次**：同一 `audit_id` 的批量修复第一次未达 PASS = `ROLLED_BACK`，第二次未达 = `ABANDONED`（区别于旧的按 `finding_id` 计数）。
- **修前/修后 delta**：一次复审即可产出 C01–C07 修前/修后百分比与 delta（§8.1 item 3），不再按 finding 多轮累积。

> `PARTIALLY_REPAIRED` 在批量语义下才有意义（旧单 finding 模型只会出现全过或 ROLLED_BACK）。它表示「本轮已尽力修，但仍不满足发布门槛」，供后续人工/科学判断或下一批次处理，本轮不改动权威题包。

---

## 9. 报告与飞书文档

### 9.1 报告结构升级（`audit_report.json` / `.md`）

- 新增 `dimensions_v11`：C01–C07 的 `max / earned / normalized(%) / finding_ids`。
- 新增 `repair_delta`（复审时）：每维修前/修后/delta。
- 保留 findings 全字段（位置、观察事实、证据、影响、最小修复、复测）。

### 9.2 飞书文档结构（最终交付）

1. 概述与目标
2. 整体流程图（材料准入 → D 层 → A 层 → 打分/处置 → 修复 → 复审）
3. 确定性检查表（D1–D7，编号/名称/说明·关键文件/方法）
4. LLM 检查表（A1–A5，编号/名称/判断方向/核心输入/说明；标注 A2/A4/A5 必读 paper）
5. 七维评分模型 C01–C07：定义、权重、判分依据、Hard Gate 绑定
6. 数值评分依据：severity 扣分规则、归一化、总分、区分度/等价的数值判据
7. 修复流程与修前/修后指标对比样例
8. 每一步「做了什么 / 目的 / 结果 / 下一步」速查表

用飞书 CLI 生成流程图与表格（对齐既有 v10 飞书文档风格）。

---

## 10. 实施阶段与里程碑（建议开 issue 多任务）

- P0 设计冻结：确认 C01–C07 权重、维度映射、终态字段（本计划评审）。
- P1 分类改造：A 层读三段字段判定 + `MAT_WRAPPER` 纳入任务 + `NON_MAT` 放弃门。
- P2 D 层显式化：D1–D7 落到 SKILL 表格 + 补 D2 instruction 内部一致检查。
- P3 评分引擎：五维 → C01–C07 重映射，报告输出七维 + 归一化。
- P4 A 层显式化：A1–A5 声明输入文件（A2/A4/A5 必读 paper），对齐 `references/出题-质检-修复.md`。
- P5 修复联动：终态字段统一 + 修前/修后 delta 输出。
- P6 回归测试：更新/新增 `tests/` 覆盖新流程与评分。
- P7 飞书文档：生成最终交付文档与流程图。

每个 P 阶段对应一个 GitHub issue；简单子任务可用 5.6 Luna xhigh 子代理并行。

---

## 11. 受影响文件（预估）

Review：
- `.cursor/skills/materials-benchmark-review/SKILL.md`（两张表格 + 新流程 + 分类改造说明）
- `references/scoring-rubric.md`（C01–C07 模型）
- `references/no-paper-e1.md`、`references/paper-grounded-audit.md`（删除 paper 触发开关；改为 A2/A4/A5 恒读 paper 的固定规则 + A 层输入文件）
- `scripts/audit_package.py`（D2 instruction 内部一致 + 分类字段读取）
- `scripts/run_review.py`（分类改造、流程编排、材料准入放弃门）
- `scripts/finalize_audit_output.py`（七维评分、报告结构、修前/修后 delta）
- `scripts/dynamic_checker_probe.py`（维度归属，无需大改）

Repair：
- `.cursor/skills/materials-benchmark-repair/SKILL.md`（终态字段统一、C01–C07 维度对齐、证据精度矩阵、放弃文案材料化）
- `scripts/run_repair.py`（消费七维报告、复审输出修前/修后 delta、`publishable` 字段、证据精度匹配校验：本地 source 不存在即 `BLOCKED_EVIDENCE`、敏感操作需类型匹配证据）

测试：
- `tests/test_materials_*`（评分映射、分类、instruction 一致、终态字段）

---

## 12. 风险与开放问题（需用户确认）

1. C01–C07 的**权重**取值？（第 3 节给了一组示例）
2. 是否**直接以 C01–C07 为 finding 归属维度**（推荐），还是保留旧五维中间层再映射？
3. `AMBIGUOUS` 的处置：继续评分并要求补证据复审，还是等同 `MAT_WRAPPER` 直接继续？（建议前者）
4. `MAT_WRAPPER` 作为任务时，其上限分是否设天花板（因通常科学深度低）？
5. 终态字段命名：`publishable` + `disposition` + `repair_state` 是否可接受？
6. 百分比是否需要同时保留旧 0–100 总分以兼容历史白名单？（建议保留，历史归档标注旧版）
7. 是否本轮就要对历史 100 白名单按新模型回算指标，还是仅对新题启用？

---

## 13. 验收标准

- 每个题包审查产出 C01–C07 七维百分比 + 总分 + verdict + `publishable`。
- SKILL 内含 D 层、A 层两张表，且每个检查项显式声明关键文件。
- 修复产出修前/修后 C01–C07 与 delta。
- 飞书文档包含流程图、两张表、评分模型、数值依据、指标样例，用户可据此了解每步的做了什么/目的/结果/下一步。
- 全量 `tests/` 通过。
