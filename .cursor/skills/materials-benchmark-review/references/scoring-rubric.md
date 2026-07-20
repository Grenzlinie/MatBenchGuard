# Authoritative scoring rubric

Authoritative scoring version: `materials-review-scoring/1.1` (seven-dimension
`dimensions_v11`). Legacy scoring version: `materials-review-scoring/1.0` (the
five-dimension `dimension_scores`, retained as a compatibility view). The Review
CLI is the only scoring authority. Batch and calibration tools may copy a
source-bound CLI scoring snapshot, but must reject manually supplied dimension
scores, totals, Hard Gates, or verdicts.

## Seven-dimension model C01–C07 (authoritative, `materials-review-scoring/1.1`)

Findings are attributed to exactly one of seven dimensions. Each dimension has a
fixed weight; the authoritative total is the weight-normalized percentage across
all seven dimensions on a 0–100 scale. The legacy five-dimension total is kept
as `legacy_total_score`.

| Dim | Title | Weight | Family | Key |
| --- | --- | --- | --- | --- |
| C01 | 领域准入 (domain admission) | 10 | admission | yes |
| C02 | 题目设计完整性与文件一致性 (task design completeness & file consistency) | 20 | deterministic | no |
| C03 | 科学有效性与方法可解性 (scientific validity & solvability) | 20 | scientific | yes |
| C04 | 评分语义 (scoring semantics) | 20 | deterministic | yes |
| C05 | 答案泄漏 (answer leakage) | 10 | scientific | no |
| C06 | 可复现性 (reproducibility) | 10 | scientific | yes |
| C07 | 难度与可审计性 (difficulty & auditability) | 10 | deterministic_scientific | no |

C05 答案泄漏 covers numeric-answer leakage in the instruction (a method or
formula is not leakage) and a solution boundary the checker depends on. C06
可复现性 covers paper fidelity, indispensable direct-input availability (the
direct-input probe), and whether correct execution earns a high score. C07
难度与可审计性 covers scoring discrimination (monotonicity / sensitivity /
saturation / specificity / single-component isolation) and auditability.

Per dimension, start at `weight` and deduct `weight × severity_fraction`
(`FATAL=1.0`, `HIGH=0.4`, `MEDIUM=0.2`, `LOW=0.1`), accumulating and flooring at
zero. `normalized = points_earned / weight × 100`. The authoritative
`total_score = Σ(weight × normalized%) / Σ(weight)`, rounded to 2 places.

A temporary evidence gap in a **key** dimension (C01, C03, C04, C06) makes that
dimension's `points_earned` and the authoritative `total_score` `null`
(`NOT_ASSESSABLE`). An evidence gap in a **non-key** dimension (C02, C05, C07)
only deducts within that dimension and never nulls the total.

### Hard Gate → dimension binding

The four Hard Gates bind to key dimensions: `NON_MATERIALS_TASK → C01`,
`SCIENTIFIC_TARGET_INVALID → C03`, `CHECKER_CORE_TASK_UNASSESSED → C04`,
`INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE → C06`. Each Hard Gate result carries its
bound `dimension`.

### Disposition and unified terminal fields

The verdict drives three unified terminal fields written to every report:
`disposition` (= `PASS | CONDITIONAL | REJECT | NOT_ASSESSABLE`), `publishable`
(`true` only when `disposition=PASS`), and `repair_state` (`NOT_REQUIRED` on the
Review side). The publication route is derived from the verdict
(`PASS → PUBLISH_CANDIDATE`, `CONDITIONAL → REPAIR_QUEUE`,
`REJECT → QUARANTINE`, `NOT_ASSESSABLE → EVIDENCE_PENDING`).

- `PASS`: authoritative total ≥ 80, no failed Hard Gate, no null key dimension,
  no unresolved repairable `HIGH`, and deterministic D1–D6 is `CLEAN`;
- `CONDITIONAL`: total 60–79 (no failed gate / null key dimension), or any
  unresolved repairable `HIGH`;
- `REJECT`: any failed Hard Gate, or total < 60;
- `NOT_ASSESSABLE`: a key dimension is null (temporary required evidence
  unavailable) and no Hard Gate forces rejection.

A legacy five-dimension total (`dimension_scores` / `legacy_total_score`) is
still computed internally and retained only as a compatibility field; it is not
the authoritative score and never overrides C01–C07. Every scored finding is
attributed to exactly one C01–C07 dimension.

## Robustness and discrimination (C07)

Schema-shaped attacks can assess negative robustness. Discrimination and
equivalence require an independently justified public valid fixture. The
solution Oracle is never that fixture. Without one, record both probe classes
as `NOT_ASSESSABLE` with `source_kind=NONE`, `oracle_used=false`, and empty
fixture hashes. Add the `MEDIUM` `INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE`
limitation finding (a C07 deduction of `0.2 × 10 = 2` points) and retain
completed positive, negative, error-handling, and static-checker evidence. Do
not claim that unexecuted discrimination or equivalence probes passed. C07 is a
non-key dimension: this limitation only deducts within C07 and never nulls the
authoritative total or forces the package verdict to `NOT_ASSESSABLE`.

Every deduction records a deterministic deduction ID, finding ID, point value,
severity, observed fact, and exact affected location. Classification as
`METHOD_REIMPLEMENTATION`, `EXACT_REPRODUCTION`, or `SCIENTIFIC_EXTENSION`
never adds or removes points.

## Finding assignment (C01–C07)

Each finding maps to exactly one dimension (`scored_dimension_v11_for`):

- **C01 领域准入**: `NON_MATERIALS_TASK`,
  `MATERIALS_ADMISSIBILITY_REQUIRES_ADJUDICATION`, and `MATERIALS_*` findings;
- **C02 题目设计完整性与文件一致性**: instruction internal inconsistency, output
  contract/declaration/scoring defects, missing/parse-error files, invalid
  weights, grading-spec schema defects, solution role/Oracle completeness
  (`SOLUTION_*`), and any otherwise-unattributed deterministic defect;
- **C03 科学有效性与方法可解性**: `SCIENTIFIC_TARGET_INVALID`,
  `UNRECOVERABLE_TASK_DEFINITION`, and `PAPER_{INSTRUCTION,DATA,METHOD}_*`
  paper findings;
- **C04 评分语义**: checker read/binding/return/threshold defects,
  always-zero/always-pass/divide-by-zero scorers, adversarial pass,
  `CHECKER_CORE_TASK_UNASSESSED`, Oracle-mock rejection, known-valid rejection,
  and `PAPER_*GOLD*` findings;
- **C05 答案泄漏**: `SOLUTION_BOUNDARY_VIOLATION`, `ANSWER_LEAKAGE`,
  `ORACLE_VALUE_LEAKED`, and `PAPER_*` leak/identity findings;
- **C06 可复现性**: `INDISPENSABLE_DIRECT_INPUT_*`, `RESOURCE_USABILITY`
  findings, `E2_SMOKE_FAILED`, and residual `PAPER_*` fidelity findings;
- **C07 难度与可审计性**: quality-gradient / invariance violations,
  `SINGLE_COMPONENT_CAN_PASS`, and `INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE`.

## Contract-role mapping and deductions

The authoritative report must include the following chain for each declared
workflow requirement:

`instruction requirement → Agent work → core output → checker read → checker
score`.

Complete/full models, structures, trajectories, prediction fields, and meshes
remain core despite a contradictory process annotation; escalate the role as
`UNCLASSIFIED` while retaining core checker analysis. Only non-load-bearing
audit/log/intermediate outputs are process-only. Process artifacts are contract-map-only:
they are never checker targets, weighted components, deductions, gates, or
dynamic probes. Do not emit `PROCESS_EVIDENCE_NOT_VERIFIED` or run an
anti-hacking trace.

Process evidence is not a dynamic fixture or checker target. Do not create a
`PROCESS_EVIDENCE_NOT_VERIFIED` deduction from dynamic fixture behavior, and do
not include process artifacts in any of the five top-level probe inputs.

An ignored or existence-only load-bearing artifact produces the severe
`CHECKER_CORE_TASK_UNASSESSED` finding. Its affected artifact is evidence for
one grouped core-task finding, not a separate deduction per file.

`INSTRUCTION_ONLY_OUTPUT` is reserved for an output that the instruction
requires as a final/scored result, but that has no structured contract or
checker reference. It does not apply to process evidence.

Static checks such as `largest_weight >= pass_threshold` establish only a
reachability risk. They do not prove `SINGLE_COMPONENT_CAN_PASS` and do not
deduct points until a component-isolation probe demonstrates that a
scientifically incomplete submission passes.

Run component isolation only when distinct contracted scoring components, an
independent non-Oracle source-bound fixture, and checker source/runtime bindings
make construction unambiguous. Oracle outputs are positive checker mocks only.
Otherwise record the probe as required but `NOT_RUN`; never promote the static
weight comparison to a bypass finding or mark crashed cases `ASSESSED`.
Apply one fail-closed usable-result predicate before every reward-derived
finding or coverage conclusion: the process must complete, reward must be
finite, breakdown must be a mapping, and `_errors` must be an empty mapping
(or absent). Non-empty or malformed `_errors`, including list/string payloads,
make positive, negative, discrimination, equivalence, component-isolation, and
task-family attack results unusable. Never publish a proven conclusion for a
probe class whose coverage is `NOT_ASSESSABLE`. Every component-isolation
status, including `NOT_ASSESSABLE`, must carry explicitly non-Oracle
provenance.

The checker mapping must separately report:

- file read status;
- runtime scorer binding;
- effective weight;
- whether the scorer returns a finite value;
- whether the scorer can be constant zero/one or divide by zero; and
- whether directionality and scientific-quality discrimination remain to be
  demonstrated dynamically.

If the Oracle producer completes but its isolated mock is rejected, the
finding belongs to checker/Gold alignment or checker runtime behavior. It is a
solution-completeness finding only when the producer fails to execute or does
not generate the declared outputs. Docker mount paths are not repair defects.

Findings with the same root cause share one deduction group. Multiple files,
components, or probe cases provide evidence breadth but must not multiply the
deduction. Grouping requires explicit or deterministic evidence of the shared
cause; temporal proximity or co-occurrence (for example, an Oracle rejection
beside a missing scorer return) is not sufficient.
Normalize ephemeral paths, UUIDs, common PID spellings, process identifiers,
and memory addresses before hashing repeated runtime failures. Include the
stable checker source frame and normalized dict/list/string/other error payload
so distinct defects remain distinct.

## Hard Gates

Exactly four Hard Gates exist:

1. `NON_MATERIALS_TASK`;
2. `SCIENTIFIC_TARGET_INVALID` (including an unrecoverable necessary task
   definition);
3. `CHECKER_CORE_TASK_UNASSESSED`;
4. `INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE`.

Each gate reports `PASS`, `FAIL`, or temporary `NOT_ASSESSABLE`, plus finding
IDs, exact evidence, and affected locations. A failed gate forces `REJECT` but
does not replace or hide an otherwise assessable 0–100 total.

## Verdict

- `PASS`: total at least 80 and no unresolved repairable `HIGH`;
- `CONDITIONAL`: total 60–79, or any unresolved repairable `HIGH`;
- `REJECT`: total below 60, or any failed Hard Gate;
- `NOT_ASSESSABLE`: temporary required evidence is unavailable and no
  definitive Hard Gate determines rejection.

A missing or statically unparseable required checker is a repairable structural
defect: keep the checker-core Hard Gate `NOT_ASSESSABLE` and route the scored
audit `CONDITIONAL` when no separate temporary evidence gap exists. A checker
that starts but cannot produce usable runtime evidence is instead a temporary
critical evidence gap and routes `NOT_ASSESSABLE`. Neither state may leave the
checker-core Hard Gate `PASS`.

## Deterministic repair publication

The source audit's deterministic contract is the repair plan's schema authority.
New deterministic plans bind the contract schema version, registry version,
contract digest, source audit identity, and the complete set of
`required_finding_ids`. An omitted OPEN blocking D1–D6 finding, unknown check
target, stale digest/schema, or stale source binding fails closed. Historical
unbound plan/bundle schema `0.1` records remain readable as evidence archives.

Repair runs fail-before and pass-after causal regressions, then invokes the
equal-depth E1 Review CLI exactly once. Only that re-audit may establish the
post-repair verdict and D1–D6 state. Atomic publication requires all of:

`PASS + deterministic CLEAN + no Hard Gate + preserved identity + allowed
mutation scope + every target finding resolved`.

Residual deterministic blockers are terminal and non-publishable; local repair
scores, heuristics, or regression results cannot promote a candidate.

## Report evidence

Every finding records an exact file plus line/quote when the source exists,
observed fact, impact, minimal repair, and retest. A missing file uses the exact
path with `line=null` and `quote=null`. Generic-only repair language is not a
valid authoritative finding.

`PASS` is also fail-closed under `materials-evidence-contract/1.0`:
authoritative materials qualification quotes instruction/tests evidence; every
scored C01–C07 dimension has non-empty evidence; the paper-grounded review
adjudicates the required paper-fidelity checks with cited paper/package
evidence (A2/A4/A5 always read `paper/`); every probe class records honest
status and provenance; assessed discrimination/equivalence uses an independent
non-Oracle fixture while unavailable classes explicitly record no fixture; and
solution completeness records only solve/positive-mock status, never Oracle
values. No findings is not positive evidence.

## Calibration migration

Artifacts produced under older scoring versions remain evidence archives, not
current scoring authority. Preserve their source hashes and findings, mark the
view as old scoring, then rerun the Review CLI from the frozen identity
manifest. Regenerate batch/index outputs from the new CLI reports; do not copy
old scores or verdicts into the rerun.
