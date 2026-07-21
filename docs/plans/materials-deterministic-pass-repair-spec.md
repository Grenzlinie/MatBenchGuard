# 材料题包 D1–D6 确定性 PASS 与 Repair 闭环规格

状态：已实现并验证

## Problem Statement

当前材料题包 Review 使用总分、Hard Gate 和“未解决的 repairable HIGH”决定是否 PASS。这个规则允许总分达到 80 的题包在仍有 MEDIUM 级确定性缺陷时发布，例如题面不同章节的输出声明不一致、结构化输出合同缺项或零权重评分项。

Review 与 Repair 也没有共享的 D1–D6 机器可读合同：Review 主要依赖 finding code 和 C02/C04 归属，Repair 只要求计划覆盖所选 findings。结果是 Repair 可以修完部分问题后发布，却没有独立证明 D1–D6 已全部通过。

用户需要的质量底线是：至少对可能 PASS 的题包，输出声明、题面内部一致性、checker 代码健康、评分权重、题包完整性，以及核心输出的读取与 scorer 接线均不存在已证实的非科学问题。

## Solution

建立一个由 Review 和 Repair 共同消费的 D1–D6 确定性合同。

Review 对每项检查产出稳定、机器可读的 `PASS / FAIL / BLOCKED / NOT_ASSESSABLE` 状态，并明确区分“已证实缺陷”和“仅提示风险”。只有已证实、仍 OPEN、可修复且阻断发布的 D1–D6 finding 会进入确定性 Repair；静态风险提示不会单独阻止 PASS。

处置顺序保持：

1. Hard Gate 命中时 `REJECT`；
2. 关键证据暂缺时 `NOT_ASSESSABLE`；
3. 总分低于 60 时 `REJECT`；
4. 总分至少 60、但存在 D1–D6 阻断 finding 时 `CONDITIONAL / REPAIR_QUEUE`；
5. 总分至少 80、无 Hard Gate、无关键证据缺口且 D1–D6 全部通过时，才允许 `PASS`。

进入 Repair Queue 的报告携带确定性修复 schema，列出必须覆盖的全部 blocking findings。Repair 对有唯一机械答案的修改使用 `AUTO_FIX`；涉及权重选择、评分语义或新 scorer 实现的修改使用 `ASSISTED_FIX`；需要重定义核心科学任务的缺陷保持 Hard Gate 或 `ABANDON`。

Repair 仅在一次等深双车道 重审同时满足总体 `PASS`、D1–D6 全部通过、无残留 blocking finding、无 Hard Gate、身份与修改范围保持有效时，才可原子发布。

## User Stories

1. As a benchmark reviewer, I want every D1–D6 check to have an explicit status, so that I can distinguish a passed check from an unexecuted or failed check.
2. As a benchmark reviewer, I want each deterministic finding to identify its D check, so that I do not infer check ownership from scattered finding-code lists.
3. As a benchmark reviewer, I want only proven defects to block PASS, so that advisory risks do not create false repair work.
4. As a benchmark reviewer, I want unresolved deterministic defects to block PASS at any severity, so that MEDIUM structural defects cannot be published merely because the total score remains high.
5. As a benchmark reviewer, I want sentence punctuation and equivalent path spelling normalized before comparison, so that valid output contracts do not receive false D1 findings.
6. As a benchmark reviewer, I want instruction outputs, structured output contracts and grading steps compared together, so that missing or extra scored files are detected deterministically.
7. As a benchmark reviewer, I want Workflow, Output files, Output contract and Self-check declarations compared, so that the public task has one coherent answer contract.
8. As a benchmark reviewer, I want checker syntax, return paths, constant scorers and literal divide-by-zero defects checked, so that mechanically broken grading code cannot PASS.
9. As a benchmark reviewer, I want all scoring weights to be finite and valid, so that malformed weight data cannot silently alter reward.
10. As a benchmark reviewer, I want every core scoring item to have positive effective weight, so that a declared core output is not present only cosmetically.
11. As a benchmark reviewer, I want required package roles and verifier entrypoints checked, so that an incomplete package cannot be published.
12. As a benchmark reviewer, I want every core output traced through content read, scorer binding, effective weight, finite return and final reward, so that existence-only checks cannot masquerade as scientific assessment.
13. As a benchmark maintainer, I want D1–D6 definitions in one shared module, so that Review and Repair cannot drift on what “deterministically clean” means.
14. As a benchmark maintainer, I want an audit to expose the complete deterministic repair queue, so that downstream automation cannot cherry-pick only easy findings.
15. As a repair planner, I want every repair target bound to its source audit finding and D check, so that a repair cannot substitute an unrelated edit.
16. As a repair planner, I want unambiguous structural changes classified as AUTO_FIX, so that routine contract defects can be repaired without scientific adjudication.
17. As a repair planner, I want changes to Gold, tolerance, threshold, scientific fields or scoring importance to require ASSISTED_FIX evidence, so that deterministic repair cannot invent scientific semantics.
18. As a repair planner, I want proportional weight normalization allowed only when all original weights are finite and positive, so that AUTO_FIX preserves relative scoring intent.
19. As a repair planner, I want missing entrypoint wrappers auto-fixed only when an existing unique implementation can be invoked, so that Repair does not fabricate a scientific producer.
20. As a repair planner, I want a missing scorer registration auto-fixed only when the intended existing scorer is unique, so that Repair does not guess code behavior.
21. As a repair planner, I want existence-only or ignored core outputs to require evidence-backed scorer work, so that Repair cannot add superficial file reads to satisfy D6.
22. As a benchmark owner, I want an unrecoverable core-task scoring gap to remain a Hard Gate, so that Repair cannot redefine the benchmark to make it pass.
23. As a benchmark owner, I want scores below 60 to remain REJECT even when deterministic defects exist, so that this change does not weaken the established rejection threshold.
24. As a benchmark owner, I want temporary key evidence gaps to remain NOT_ASSESSABLE, so that missing evidence is not mislabeled as a repairable defect.
25. As a benchmark owner, I want Repair to run exactly one equal-depth dual-lane re-audit, so that before/after evidence remains comparable.
26. As a benchmark owner, I want any remaining D1–D6 blocker to prevent atomic publication, so that partially repaired packages remain quarantined.
27. As a benchmark owner, I want successful repair to imply both overall PASS and deterministic CLEAN, so that downstream certification can rely on one invariant.
28. As a repository maintainer, I want existing non-deterministic repair plan 0.1 inputs to remain readable, so that historical repair bundles remain evidence archives.
29. As a repository maintainer, I want new deterministic repair plans to bind the source deterministic schema, so that stale plans fail closed.
30. As an agent implementing one ticket, I want a high-level Review seam and Repair seam for tests, so that behavior can be verified without coupling tests to internal helper functions.

## Implementation Decisions

- Introduce one deep deterministic-contract module whose interface accepts the normalized instruction contract, grading contract, checker analysis and package-role status, and returns the complete D1–D6 report.
- Treat the deterministic-contract interface as the shared seam for Review and Repair. Finding-code ownership, blocking policy, advisory exclusions and recommended repair class live behind this interface.
- Use these checks:
  - D1: scored output declaration consistency across instruction, structured output contract and grading steps.
  - D2: internal consistency across Workflow, Output files, Output contract and Self-check.
  - D3: statically proven checker code-health defects.
  - D4: weight validity, normalization and positive effective weight.
  - D5: required quality-role, parser and verifier-entrypoint completeness.
  - D6: core-output content read, scorer binding, effective weight, finite scorer return and inclusion in final reward.
- Give each D check `PASS`, `FAIL`, `BLOCKED` or `NOT_ASSESSABLE`. A D check may be `BLOCKED` by an earlier structural defect without creating duplicate deductions.
- Add `proven_defect` and `blocking` semantics. Static reachability warnings and unproven bypass risks are advisory and do not independently block PASS.
- Add a source-audit deterministic repair schema with `CLEAN`, `REQUIRED` and `NOT_APPLICABLE` states. `REQUIRED` contains every OPEN repairable blocking D1–D6 finding.
- Add a pre-repair lifecycle value indicating deterministic repair is required. It is distinct from terminal repair outcomes such as repaired, partially repaired, rolled back and abandoned.
- Preserve existing precedence for Hard Gates, key evidence gaps and scores below 60. The deterministic clean gate only changes PASS eligibility and the repair routing of otherwise repairable packages.
- Permit AUTO_FIX only when a unique transformation can be proven from the frozen contract:
  - synchronize an unambiguous stale output declaration;
  - normalize a path or structural representation;
  - wire an existing unique scorer to an existing step;
  - normalize finite positive weights while preserving their ratios;
  - restore a standard entrypoint around an existing unique implementation.
- Require ASSISTED_FIX for any operation that chooses or introduces scientific fields, units, Gold, tolerances, thresholds, scoring importance, scorer algorithms or ambiguous checker behavior.
- Never use solution/Oracle content as evidence for a public instruction or checker-science change.
- Keep unrecoverable core-output non-assessment as the existing checker-core Hard Gate.
- Extend the deterministic repair plan schema while continuing to validate historical 0.1 plans. A deterministic plan must cover the full source queue and bind each finding’s check identity.
- Require fail-before and pass-after causal regressions for every operation, followed by one equal-depth Review.
- Publish only when the re-audit is overall PASS and the shared deterministic-contract module returns CLEAN.
- Keep Review non-mutating. The caller invokes Repair after Review routes the package to the deterministic repair queue.

## Testing Decisions

- Test through the highest existing seams:
  - invoke the Review CLI and inspect the authoritative bundle for verdict, route and deterministic schema;
  - invoke the Repair CLI and inspect the equal-depth re-audit and publication outcome.
- Prefer fixture mutations that represent externally visible package defects rather than testing private helper branches.
- Add one focused direct test for normalization behavior where an end-to-end failure would not identify whether punctuation or contract comparison was wrong.
- Cover at least one proven blocking finding for every D1–D6 check.
- Verify that an advisory risk does not block PASS.
- Verify that a score of at least 80 with any OPEN D1–D6 blocker is CONDITIONAL and non-publishable.
- Verify that a score below 60 remains REJECT.
- Verify that a Hard Gate remains REJECT and does not enter deterministic Repair.
- Verify that Repair rejects a deterministic plan omitting any source blocking finding.
- Verify AUTO_FIX allowlisting for structural instruction/tests changes and rejection of semantic or unsupported modifications.
- Verify ASSISTED_FIX evidence precision for weight, scorer and scoring-contract changes.
- Verify schema 0.1 compatibility and deterministic schema stale-binding rejection.
- Verify `REPAIRED` implies the re-audit reports deterministic CLEAN.
- Reuse existing disposition, dual-lane review, safe repair, batch repair, assisted repair and certification test patterns.

## Out of Scope

- Changing C01–C07 weights or severity deduction fractions.
- Changing the four Hard Gates.
- Allowing a package below 60 to enter Repair instead of REJECT.
- Repairing D7 discrimination, equivalence or component-isolation limitations.
- Executing the full scientific workflow.
- Generating new Gold values, tolerances, thresholds, scientific fields or scorer algorithms without evidence.
- Modifying paper, metadata, environment or other non-quality roles.
- Rewriting historical audit artifacts to match the new schema.
- Automatically invoking Repair from inside Review.

## Further Notes

- The first implementation slice establishes the shared schema and routing seam. D1–D2, D3–D4, D5 and D6 then form independent tracer-bullet slices that can proceed in parallel.
- A final integration slice validates compatibility and the publication invariant after all D-specific slices land.
- The canonical proof obligation is intentionally one-way and fail-closed: every PASS must be deterministically clean; a deterministically clean package still needs to satisfy all scientific, evidence, score and Hard Gate requirements.

## Implementation Tickets

- Spec / parent: [#26](https://github.com/Grenzlinie/qa-review/issues/26)
- Foundation: [#27](https://github.com/Grenzlinie/qa-review/issues/27)
- D3–D4: [#28](https://github.com/Grenzlinie/qa-review/issues/28), blocked by #27
- D5: [#29](https://github.com/Grenzlinie/qa-review/issues/29), blocked by #27
- D1–D2: [#30](https://github.com/Grenzlinie/qa-review/issues/30), blocked by #27
- D6: [#31](https://github.com/Grenzlinie/qa-review/issues/31), blocked by #27
- Integration: [#32](https://github.com/Grenzlinie/qa-review/issues/32), blocked by #28–#31

## Completion Communication

After implementation and verification complete, update the authoritative Feishu
document at
`https://dptechnology.feishu.cn/docx/F5F5d3N9ooVcxPxZz5zcDTE8nuf` with the final
D1–D6 contract, Review/Repair state machine, repair policy, test evidence, and
the `PASS / REPAIRED ⇒ deterministic CLEAN` invariant.
