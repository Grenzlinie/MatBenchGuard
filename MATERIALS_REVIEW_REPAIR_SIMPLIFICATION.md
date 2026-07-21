# Materials Review/Repair 简化改造说明

## 1. 文档目的

本文交给 Codex，用于把当前 Materials Benchmark Review/Repair 从“多层
Hash 交叉绑定”改造成“主 Agent 分配 + 独立 run 目录 + 状态机 + 单一
AuditRoot”的本地工作流。

目标不是降低题包质量门槛，而是删除不必要的一致性基础设施。D1–D6、
Agent 论文审查、Hard Gates、评分、Repair 证据规则和原子发布规则必须保留。

## 2. 当前情况

当前流程已经具备：

- `deterministic_core` 与 `agent_quality` 双通道；
- Agent 必须阅读 `paper/**`，仅确认 `NON_MAT` 时跳过；
- schema-derived checker probes；
- 受限的 D1–D6 Agent contract fallback；
- `AGENT_CONTRACT_PENDING` pause/resume；
- 外部 audit/repair 管理目录；
- Repair 完整队列、证据精度、允许修改范围和原子发布门禁；
- 同一输出目录的 Review 原子锁、唯一临时目录及 attestation 后只读。

但一致性层同时维护：

- package/input/source-role/file hashes；
- package identity manifest hash；
- core contract digest；
- machine/effective deterministic contract digest；
- Review implementation 每文件 hash 与 aggregate hash；
- audit output hashes、bundle hash；
- manifest/report/disposition/artifact hashes；
- attestation bundle digest；
- assessment、static、probe、request、pending workspace hashes；
- source audit directory hash；
- plan 中多组复制的 package/audit/contract/evidence hash；
- operation before/after hashes；
- repair、history、re-audit 的文件 hash 与 bundle digest；
- Docker、control scope 和 failure fingerprint。

这些字段分别有合理来源，但被同时用作 freshness gate 后，形成了过度绑定。

## 3. 已观察到的问题

实际批量测试出现过以下非题包故障：

1. Review 实现文件改变后，旧 audit 因逐字节 implementation hash 不一致而失效。
2. pending workspace 搬迁改变 assessment 文件，但关联 hash 未同步。
3. re-audit rebase/promote 后，外部 bundle hash 与 manifest 内嵌 hash 更新顺序不一致。
4. 非 PASS workspace 清理前未保留完整 re-audit bundle。
5. malformed probe 文件扩展名为 `.json`，被路径重写逻辑误当权威 JSON 解析。
6. 两个 Review 并发使用同一临时目录，attestation 后又出现未绑定文件。
7. post-attestation implementation hash 刷新导致 report、manifest 与 attestation 不一致。
8. legacy Repair plan 可绕过 current schema、contract digest 和完整 required queue。

部分 Hash 检查成功阻止了错误发布，但大量故障来自“可变 artifact + 多层 Hash +
多进程写入”的组合，而不是题包质量。

## 4. 采用的前提

新方案建立在以下运行模型上：

- 一个主 Agent 是唯一调度者和 tracking/assignment 文件写者；
- 主 Agent 在启动 Subagent 前完成题包分配；
- 一个题包同时只允许一个 Review/Repair lifecycle；
- 每个题包运行在独立 run 目录；
- Review 完整结束后 Repair 才读取结果；
- 不考虑恶意篡改；
- 不支持把任意旧 audit、plan 或 pending workspace 重新接入新运行；
- 不考虑跨机器传递和中断后长期恢复；
- 仍需防止程序误写、并发写入和拿错 run。

## 5. 调度与目录

### 5.1 主 Agent 分配

新增由主 Agent 独占写入的 assignment CSV，例如：

```text
review_records/assignments.csv
```

字段：

```text
package_id,run_id,assigned_agent,status,record_dir,started_at,completed_at,
review_verdict,repair_status
```

规则：

- 启动 Subagent 前先原子写入 `ASSIGNED`；
- Subagent 不得自行领取下一题，不得直接修改 CSV；
- 主 Agent收到结果后更新终态；
- CSV 用于协调，不承担内容完整性；
- 若未来允许多个主 Agent，需要另加真正的原子数据库/文件锁，不能把 CSV 当并发锁。

### 5.2 仓库级管理目录

所有管理产物统一迁移到：

```text
review_records/
  <cluster-id>/
    <theme>/
      <paper-id>/
        lock.json
        runs/
          <run-id>/
            status.json
            snapshot/
            audit/
            audit_root.txt
            plan.json
            candidate/
            reaudit/
            repair_result.json
```

Harbor package 内不得出现 audit、repair、probe、pending 或 history 文件。

修改 `review_path_policy.py`，从 package 相对
`materials_science_questions/` 的 `<cluster>/<theme>/<paper-id>` 映射到上述目录。
同步修改 Review/Repair CLI、两个 SKILL、引用文档和测试。

## 6. 状态机

最小状态：

```text
ASSIGNED
→ REVIEWING
→ REVIEWED
→ REPAIRING
→ REPAIRED | NOT_REQUIRED | ABANDONED | FAILED
```

如果仍保留 Agent contract pause：

```text
REVIEWING → AGENT_CONTRACT_PENDING → REVIEWED
REPAIRING → AGENT_CONTRACT_PENDING → REPAIRING
```

状态文件必须使用临时文件加 atomic rename。状态转换必须校验前置状态，不能跳转。

Repair 只接受：

```bash
python run_repair.py --run-dir review_records/.../runs/<run-id>
```

不再由调用者任意组合 `--audit-dir`、`--audit-attestation` 和
`--repair-output-dir`。

## 7. 最小 Hash 模型

只保留一种内容完整性机制：`AuditRoot`。

### 7.1 AuditRoot

```text
AuditRoot =
H(
  audit_root_schema_version,
  run_id,
  package_id,
  review_contract_version,
  sorted(relative_path, file_mode, H(file_bytes))
)
```

计算范围：

```text
snapshot/
  instruction.md
  tests/**
  solution/**
  paper/**
  Review 实际读取的直接输入

audit/
  deterministic_core/**
  agent_quality/**
  agent_contract/**
  audit_report.json
  findings.jsonl
  disposition.json
  probe results
```

`audit_root.txt` 自身不参与计算。

源 Review 得到 `A0`；最终 re-audit 若需长期保存，使用同一算法得到 `A1`。
这仍然是一种 Hash 机制，不是两套协议。

### 7.2 删除为独立门禁的 Hash

删除或降级为普通诊断字段：

- package snapshot root；
- package identity manifest hash；
- core contract digest；
- machine/effective contract digest；
- Review implementation per-file/aggregate freshness gate；
- report、manifest、disposition 独立 hash；
- attestation bundle digest；
- assessment、static、probe、request、pending workspace hashes；
- source audit directory hash；
- plan binding digest；
- operation before/after hash；
- repair/re-audit/history 的多层 bundle hash；
- finding fingerprint 完整性门禁。

如果保留叶子 Hash 用于错误定位，它们不得再成为独立 freshness gate。

### 7.3 Review contract version

用稳定的语义版本替代 Review 实现逐字节一致：

```text
review_contract_version = materials-review-contract/1
```

只有以下变化升级版本：

- D1–D6 语义；
- C01–C07 评分或 Hard Gate；
- Agent contract adjudication 资格；
- Repair publication invariant；
- audit artifact 的必需字段语义。

重构、注释、测试、文档或等价实现变化不得让旧 audit stale。
exact implementation hash 可以保留为 provenance，但不得阻止 Repair。

## 8. Review 与 Agent 行为保持不变

Hash 简化不得改变双通道边界：

```text
deterministic_core
  → instruction/tests/grading_spec/runtime probes

agent_quality
  → paper/instruction/tests
  → Gold、checker、数据、方法、单位、公式、阈值的科学合理性
```

Agent contract fallback 仍只处理 contract/wiring：

- 输出声明是否一致；
- checker 是否读文件；
- scorer 是否绑定；
- 权重是否有效；
- 是否返回有限值；
- 是否进入最终 reward。

它不能用 paper、Oracle、Gold、公式或阈值来覆盖机器已证明的 FAIL。

## 9. Repair 规则保持不变

必须保留：

- current batch plan schema；
- 完整 required finding queue；
- `AUTO_FIX` / `ASSISTED_FIX` / `ABANDON`；
- evidence precision；
- 允许修改范围；
- fail-before/pass-after regressions；
- score ≥ 80；
- effective D1–D6 CLEAN；
- 无 Hard Gate；
- 无 HIGH/FATAL；
- exactly one equal-depth re-audit；
- atomic publication；
- 非 PASS 保留原题包。

这些通过 schema、状态机和实际文件比较执行，不依赖多层 Hash。

操作范围验证可直接比较 `snapshot/` 与 `candidate/` 的文件树和字节；无需持久化
多套 operation before/after hash。

## 10. 并发与原子性

即使不考虑恶意篡改，也必须保留：

- per-package 原子锁；
- 每次运行唯一 temp/run 目录；
- 不同题包可并行，同一题包 fail-fast；
- canonical run 目录只允许原子发布；
- 已完成 audit 不允许原地刷新；
- 新实现需要新 audit，不允许重写旧记录；
- crash cleanup 只能删除当前 run 自己的 temp。

这些是并发正确性，不是 Hash 完整性。

## 11. Codex 实施顺序

1. 增加 repo-level `review_records` 路径解析与测试。
2. 增加 assignment CSV 初始化、原子更新和主 Agent 工作说明。
3. 将 Review 输出、pending、Repair history 迁入独立 run 目录。
4. 将 Review/Repair CLI 收敛为 `package + run-dir`。
5. 建立状态机及合法转换测试。
6. 实现单一 `AuditRoot`，覆盖 snapshot 与完整 audit。
7. 将 exact implementation hash 改为 provenance，增加
   `review_contract_version`。
8. 删除或降级重复 Hash 门禁。
9. 保留并重新接线 D1–D6、Agent paper、Repair evidence 和 publication gates。
10. 删除 legacy output 兼容路径，不迁移旧 audit。
11. 更新两个 SKILL、`AGENTS.md`、reference docs 和模板。
12. 重写测试，覆盖并发、状态转换、AuditRoot、双通道和原子发布。
13. 清空旧审计记录，重新初始化 tracking。
14. 完整执行 Materials 与全仓测试后，再重新审计样本题包。

## 12. 验收标准

- 同一题包的两个并发 Review 中，一个获得锁，另一个在 Probe 前失败；
- 不同题包可并行；
- Harbor package 中无管理产物；
- Review 结束后 Repair 只通过同一 `run-dir` 读取；
- 修改 snapshot 或 audit 任一字节时，唯一 AuditRoot 校验失败；
- Review 等价代码重构不会让 audit stale；
- Review contract version 不兼容时 Repair fail closed；
- Agent paper 审查与 deterministic lane 保持隔离；
- proven FAIL 不能被 Agent contract 覆盖；
- Repair 仅在全部 publication invariants 满足时修改题包；
- 非 PASS 保留原题包并保存完整 run 记录；
- assignment CSV 与 tracking 只有主 Agent 写入；
- 不存在旧 `review_outputs`、package-local audit 或 legacy hash 兼容入口；
- Materials 测试和全仓测试全部通过，无新增 skip。

## 13. 非目标

- 不支持恶意攻击者修改本地记录；
- 不提供跨机器 artifact 认证；
- 不恢复或迁移历史 audit；
- 不改变科学评分模型；
- 不放宽 Repair 证据或发布门槛；
- 不把 assignment CSV 当作多主 Agent 并发数据库。
