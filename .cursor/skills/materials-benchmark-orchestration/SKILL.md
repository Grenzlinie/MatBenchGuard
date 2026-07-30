---
name: materials-benchmark-orchestration
description: 通过并行的审核与修复流水线处理整个 Harbor 材料科学问题包语料库，每个子 Agent 一次处理一个问题包，并使用基于锁的自主认领队列，确保任意两个 Agent 不会接触同一问题包。适用于对新问题包集合或目录进行规模化质量审核。提供基于 fcntl.flock 的队列、逐包 PLAYBOOK、编排循环（启动、补充、释放、隔离），以及洁净包发布和 Harbor 格式验证。兼容 Codex、Claude Code 和 Cursor 多 Agent 模式。
---

# 材料科学基准并行编排

并发地对整个 Harbor 问题包语料库运行 `materials-benchmark-review` 和 `materials-benchmark-repair`。每个工作单元都是一个子 Agent，一次从受共享锁保护的队列中认领一个问题包，依据 PLAYBOOK 端到端处理，标记完成后再认领下一个。编排 Agent 持续补充工作池，直到队列清空，然后汇总洁净且可发布的问题包。

本 skill 是规模化执行层。科学裁决规则位于 `materials-benchmark-review` 和 `materials-benchmark-repair`；也必须阅读这两个 skill，且每个工作 Agent 都必须遵守其规则。

## 适用场景

- 新的 Harbor 问题包目录或集合需要进行质量审核，包括审核与修复。
- 需要多个 Agent（Codex、Claude Code、Cursor 子 Agent，或多个独立会话）协同处理同一语料库，且不得冲突或重复处理。

## 文件

- `scripts/queue.py`：原子化认领、完成、释放、状态查询和过期回收，使用文件锁。
- `scripts/init_corpus.py`：扫描源目录并生成 `corpus_manifest.json` 和状态。
- `scripts/publish.py`：将洁净问题包汇总到 `_publish/`。
- `scripts/verify_harbor.py`：验证 `_publish/` 是否符合 Harbor 文件树。
- `assets/PLAYBOOK.md`：交付给每个工作 Agent 的逐包处理流程。

## 路径（两个根目录，通过环境变量一次性设置）

- `QA_SRC`：只读的源语料库根目录，即 Harbor 问题包所在位置；绝不修改。
- `QA_ROOT`：可写的工作与输出根目录，默认为 `/personal/qa_review`；保存 `corpus_manifest.json`、`state/`、逐包 `<pkg>/` 输出和 `_publish/`。

问题包标识是相对于 `QA_SRC` 的路径，例如 `cluster-x/theme/paper-y`，因此可一一映射到 `QA_SRC/<pkg>` 和 `QA_ROOT/<pkg>`。

## 并发与文件锁

`queue.py` 对 `QA_ROOT/state/queue.lock` 使用 `fcntl.flock(LOCK_EX)`，串行化所有状态变更。`claim` 选择第一个尚未认领且未完成的问题包，在 `assigned.json` 中记录 `{agent, ts}`，然后释放文件锁。因此，即使工作 Agent 位于不同会话或工具中，也不可能领取同一问题包。

过期认领是指未完成且早于 `QA_STALE_SEC` 的认领；默认超时时间为 2 小时。下次执行 `claim` 时会自动回收，因此崩溃的工作 Agent 不会永久占用问题包。`QA_ROOT/<pkg>/` 中的 `.done` 标记也会被视为已完成，使队列在重复运行和新语料库场景中保持幂等。

## 操作流程

### 1. 初始化队列（每个语料库仅一次）

```bash
export QA_SRC=/abs/path/to/source_corpus
export QA_ROOT=/personal/qa_review          # 或任意可写根目录
uv run --python 3.12 python <this>/scripts/init_corpus.py
uv run --python 3.12 python <this>/scripts/queue.py status   # {total, done, remaining}
```

在已有 `QA_ROOT` 上重新运行初始化是安全的：它会保留状态；新的或扩充后的语料库仅会新增尚未认领的问题包。

### 2. 启动工作 Agent 池

启动 N 个子 Agent，初始建议约 8–16 个，可自由扩容，文件锁会处理任意数量。为每个 Agent 分配全局唯一的 `AGENT_ID`。每个工作 Agent 的提示必须要求其完整阅读 `assets/PLAYBOOK.md` 和 Review skill 的 `references/check-responsibility-matrix.md`，然后运行自主认领循环，并导出 `QA_SRC`、`QA_ROOT` 以及审核和修复 skill 的路径。

多个用户或工具可以同时向同一队列增加工作 Agent；必须要求其使用不同的 `AGENT_ID`，且只能通过 `queue.py claim` 认领，不得手工选择问题包。

工作 Agent 提示模板：

> 你是质量审核与修复工作 Agent，`AGENT_ID` 为 `qa-<uniq>`。完整阅读
> `<this>/assets/PLAYBOOK.md` 及 Review skill 的
> `references/check-responsibility-matrix.md` 并严格遵循。Phase 0–2 先做
> `MECHANICAL` 低成本筛查；进入 Phase 3 后必须回看真实文件完成所有 `HYBRID`
> 检查，机械候选为零不能作为通过证据。运行自主认领循环：
> `queue.py claim qa-<uniq> 1`；若输出问题包，则严格依据 PLAYBOOK 处理
> （生成证据并验证 `agent_final_decision.json`；`PASS` 直接完成；不可修复
> 早期 `REJECT` 标记 `SCREENED_OUT` 且不进入 Repair；仅有 disposition
> `REPAIR` 且无决定性 `ABANDON` Hard Gate 时运行修复并验证
> `repair_report.json`；`NOT_ASSESSABLE` 释放等待补证；满足终态后执行
> `touch OUT/.done`；执行 `queue.py done <pkg>`）；若输出为空则停止。
> 最多处理 8 个问题包，然后报告并退出；必须完成已开始的问题包；
> 若受阻，执行 `queue.py release <pkg>`。

### 3. 持续补充工作池（编排循环）

- 每个工作 Agent 最多处理 8 个问题包后退出，以限制上下文规模。每次收到完成通知后，启动具有新 `AGENT_ID` 的工作 Agent，直到 `queue.py status` 显示 `remaining == 0` 且 `assigned_open == 0`。
- 随时可通过 `queue.py status` 查询进度。
- 工作 Agent **失败或停滞**时，例如 API 错误，或完成通知显示最后一步仍处于问题包处理中，应释放其遗留认领，使其他 Agent 可以重新接手：使用 `queue.py release <pkg>`，并通过 `assigned.json` 确定问题包；必要时可先清除部分生成的 `QA_ROOT/<pkg>/`。不得仅因工作 Agent 较慢就终止它；包含“修复前失败、修复后通过”和同等深度复审的修复可能需要 20 分钟以上。
- 如果某个问题包因与质量审核无关的原因反复导致工作 Agent 崩溃，例如同一问题包两次触发内容过滤误报，应将其**隔离**：写入 `done.json` 和 `state/quarantine.txt`，并添加 `QUARANTINE.txt` 说明，使工作池不再分配该包，同时标记为需要人工处理；不得计为 `PASS`。

### 4. 汇总可发布问题包

队列清空后运行：

```bash
uv run --python 3.12 python <this>/scripts/publish.py         # -> QA_ROOT/_publish
uv run --python 3.12 python <this>/scripts/verify_harbor.py   # 必须输出 RESULT: PASS
```

`_publish/<pkg>/` 保存洁净交付物：结论为 `PASS` 的问题包从源目录原样复制，结论为 `REPAIRED` 的问题包从 `QA_ROOT/<pkg>/candidate` 复制；不得包含审核文件，并移除核心范围内的 `__pycache__`。若缺少任何核心文件（包括 `tests/test.sh`）或泄露审核产物，`verify_harbor.py` 必须失败。`solution/` 若存在则原样携带，但完全不读取、不检查、不清理、不修改；修复时加入的输入或 Gold 数据文件属于合法问题包内容，可以保留。

## 多工具协作说明（Codex、Claude Code、Cursor）

- 队列本质上是文件与文件锁，与工具无关；任意组合的 Codex、Claude Code、Cursor Agent 以及每种工具的多个会话均可共享同一 `QA_ROOT`。协调完全通过 `queue.py` 完成。
- 唯一要求是：每个并发认领的工作 Agent 必须使用唯一 `AGENT_ID` 调用 `queue.py claim`，并将输出写入 `QA_ROOT/<pkg>/`。
- 如果独立会话正在同一队列上运行自己的工作池，其新认领会读取当前版本的 skill 和 PLAYBOOK；只有需要在运行中修改规则时，才停止相应会话。

## 实践注意事项

- 停滞不等于死亡：释放前先检查工作 Agent 的最后操作是否为“写入修复报告或标记完成”；释放并清除会丢失已完成的工作。
- `run_checker_probes` 会在文件树中留下 `tests/__pycache__`；`publish.py` 会将其移除，不得提交。
- 修复可能合理地新增已声明但缺失的必要输入或 Gold 文件，例如 CSV 或 JSON。这些文件属于问题包内容，应予保留。
- 每个工作 Agent 必须裁决 Review skill 的全部 `scientific_risk_patterns`；`tests/` 中随机、插值、拟合或 smoke 相关词法命中只能作为候选。缩小体系的 smoke 题若直接评分论文或权威来源支持、且有适用性依据的趋势/排序，可以通过；不得把拟合出的伪数值因“趋势看起来正确”而当作绝对 Gold。不得打开 `solution/`。
- 每个工作 Agent 必须遵循 Review skill 的检查责任矩阵。机械事实用于低成本筛查和定位；进入论文深审后必须执行真实文件 Hybrid 复核，并主动检查自动化未命中的同义表达、隐含定义和跨文件数据流。
- 每道模拟题进入 Phase 3 后必须全文阅读论文并生成 `simulation_parameter_matrix.json`，覆盖体系、坐标/对称性、模型、初始化、边界/加载、演化、采样、分析、派生参数和评分依赖。若论文复现缺少不可唯一推导的必要参数，必须以 `ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE` 终止为 `SCREENED_OUT`，不得进入 Repair。
- Review 后必须执行统一状态转换：`PASS → DONE`；决定性非修复型 `REJECT → SCREENED_OUT/DONE`；存在可修目标且无决定性 `ABANDON` Hard Gate → `REPAIR`；`NOT_ASSESSABLE → RELEASE`。`SCREENED_OUT` 保留已验证 Review 决策但不生成 candidate/repair report，发布脚本必须忽略它。
- 不得手工创建 `.done`。`queue.py done` 会先调用 `validate_lifecycle.py`，机器校验 Review/Repair 终态；模拟题还必须存在与决策参数项一致的完整 `simulation_parameter_matrix.json`。只有校验通过后才写入 `.done` 和队列完成状态。
- `queue.py status` 会统计 `.done` 标记，因此即使其他会话编辑了状态文件，其结果仍然准确。
