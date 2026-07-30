# 检查责任矩阵

本表用于区分低成本机械筛查与进入深审后的人工语义核验。机械结果用于缩小阅读范围，
不得替代对决定结论的真实文件、上下文和数据流的检查。

## 责任类型

| 类型 | 责任主体 | 可以直接产出 | 不可以直接产出 |
|---|---|---|---|
| `MECHANICAL` | 收集器、解析器、探针运行器、validator | 文件存在性、解析结果、哈希、AST/词法命中、运行退出码、原始 reward、记录一致性 | 科学缺陷、criterion/pattern 状态、Gold 可信度、最终 verdict |
| `HYBRID` | Agent 使用机械结果定位后检查真实文件和运行证据 | 对候选的确认、排除或自动化限制；跨文件合同和数据流结论 | 只凭关键词、AST 摘要或 `OBSERVED` 状态作科学裁决 |
| `AGENT` | 读题 Agent | 论文忠实度、科学有效性、参数适用性、Gold/容差依据、探针预期、修复分类和 verdict | 用无法定位到题包/论文/运行证据的印象代替结论 |

`solution/**` 不属于任何一类检查责任；不得读取、执行、哈希、扫描、引用或修改。

## 从便宜到昂贵的阶段责任

| Phase | `MECHANICAL` 先做什么 | `HYBRID` 必须回看什么 | `AGENT` 裁决什么 | 升级或停止条件 |
|---|---|---|---|---|
| 0 结构与版本 | 核心文件、解析状态、角色、大小、哈希、`tests/test.sh` 可执行性 | 对 limitation、别名布局和跨文件角色冲突检查实际路径与文件头；确认收集器处理的是目标版本 | 缺失或异常是否为真实包缺陷、等价布局还是自动化限制 | 不可识别包、非材料任务或无法取得必需审查文件时停止；可修结构问题继续记录 |
| 1 资源与预算 | 提取 `instruction.md` 的 `assets`、`resources.json` 的标识/版本/角色/映射、明确 URL、资源限制和超时；对 URL 做轻量状态探测 | 核对两份声明是否完整、明确且内部一致；复核 `404/410` 与暂时性/权限性失败的分类；不调用 Playground 或下载正文 | 资源声明是否足以定义必需输入、明确 URL 是否已确认失效，以及任务预算是否现实 | 必需输入未声明、声明含糊/矛盾、内部映射错误或唯一 URL 确认 `404/410` 时停止；平台部署不在范围内 |
| 2 题面与 checker 静态审计 | 提取输出、单位、时间窗、权重、阈值、AST 读取/奖励链和 Gold 来源词法候选 | 全文检查 `instruction.md`（含 `assets`）、`steps.json`、`resources.json`、`tests/grading_spec.json`、`tests/checker.py`、`tests/test.sh`；沿真实代码追踪相关 Gold/数据进入 acceptance truth 的路径 | 合同矛盾、核心输出覆盖、投机路径和 Gold 候选是否成立 | 仅当任务具有实质科学目标，且不存在已确认的不可修复早期 Hard Gate，才投入 Phase 3 |
| 3 论文精读 | 提供 Phase 0–2 的候选位置、重复参数和评分链索引 | 全文阅读 `paper/paper.md`，并按每项论文主张回看题面、steps、资源、Gold、grading 和 checker；对模拟题建立完整 `simulation_parameter_matrix`，即使机械零命中也覆盖体系、坐标、模型、初始化、边界/加载、演化、采样、分析、派生参数和评分依赖 | 复现意图、方法适用性、参数闭包、Gold、容差、科学定义和全部 scientific patterns；区分目标定义参数、派生耦合、表示等价和 solver-selectable | 可修且有来源的缺陷进入完整 Repair；论文缺少不可替代的必要模拟参数且无法唯一推导时触发 `ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE`，`REJECT + ABANDON` |
| 4 动态验证 | 执行通用及 Agent 提供的任务特定 probes，记录原始 observation | 阅读 `tests/test.sh` 和 checker 路径，核对每个 case 的输入、实际评分链、reward/breakdown 与路径改写限制 | 正例、梯度、等价、组件隔离和攻击的预期结果是否科学合理 | 适用 probe 未执行或不可解释时不得完成 Review |
| 5 证据一致性 | validator 检查 schema、分数、Gate、finding、case ID 和 verdict 派生 | 将决定性引用与真实文件版本、原始 observation 和未关闭 finding 对照 | 处理误报、限制和冲突，签发最终 verdict | 仅验证通过且证据闭合时完成 |

## Phase 3 深审清单

进入 Phase 3 表示该题值得投入论文阅读成本。Agent 必须同时使用机械结果和主动阅读，
不得把“收集器没有候选”当成通过证据。

1. 建立“论文主张 → 题面目标 → 固定/可选参数 → 最终输出 → Gold/容差 → checker”
   的逐项映射。
2. 主动检查机械工具难以可靠发现的同义表达、隐含单位、坐标/晶体学约定、边界条件、
   结构生成流程、统计定义、适用范围和图表中的参考关系。
3. 对每个模拟步骤追踪参数生产者、依赖和下游消费者；不得把“论文未提”自动当作无问题，
   也不得把纯坐标表示或已证明收敛的数值自由误判为目标缺参。
4. 对每个机械候选记录 `CONFIRMED`、`DISMISSED_FALSE_POSITIVE` 或
   `AUTOMATION_LIMITATION`，引用真实文件路径、定位和上下文。
5. 对每个必查 scientific pattern 即使没有机械候选也作独立判断；`PASS` 必须来自实际
   阅读，而不是来自“零命中”。
6. 对大型表格、轨迹或二进制文件不要求逐字阅读，但必须检查与评分有关的 schema、单位、
   provenance、统计特征和 checker 实际读取部分；必要时使用确定性脚本分析完整数据。

## 每项 Hybrid 检查的最低证据

Hybrid 结论至少记录：

- 检查项或 pattern；
- 使用的机械 observation/candidate；若无候选，明确写 `none`；
- 回看的真实文件路径和精确 locator；
- 原文、代码行为或运行结果；
- 候选与原文件是否一致；
- Agent 的结论和理由。

机械结果与真实文件冲突时，以当前真实文件和可复现运行证据为准，并将冲突记录为工具
limitation；不得静默采用机械摘要。
