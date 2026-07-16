# Authoritative scoring rubric

Scoring version: `materials-review-scoring/1.0`.

The Review CLI is the only scoring authority. Batch and calibration tools may
copy a source-bound CLI scoring snapshot, but must reject manually supplied
dimension scores, totals, Hard Gates, or verdicts.

## Formula

Start each dimension at its fixed maximum:

- scientific validity: 35;
- instruction answerability: 20;
- checker/Gold alignment: 25;
- robustness and discrimination: 15;
- solution completeness: 5.

Each scored finding is assigned to exactly one dimension. Deduct that
dimension's maximum multiplied by the finding fraction: `FATAL=1.0`,
`HIGH=0.4`, `MEDIUM=0.2`, `LOW=0.1`. Multiple deductions accumulate and floor
the dimension at zero. A missing or broken solution Oracle deducts all 5
solution-completeness points. For each dimension:

`points_earned = max(0, max_points - sum(deductions))`

`normalized_score = points_earned / max_points`

The total is the sum of all five `points_earned` values and is displayed on a
0–100 scale. A temporary evidence gap in a critical dimension
(`scientific_validity`, `instruction_answerability`, or
`checker_gold_alignment`) makes that dimension and the total `null`; it does
not create a scientific defect. Non-critical dimensions remain scored from the
available evidence and limitations.

Schema-shaped attacks can assess negative robustness. Discrimination and
equivalence require an independently justified public valid fixture. The
solution Oracle is never that fixture. Without one, record both probe classes
as `NOT_ASSESSABLE` with `source_kind=NONE`, `oracle_used=false`, and empty
fixture hashes. Add the `MEDIUM`
`INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE` limitation finding, deduct 3 of the
15 robustness points, and retain completed positive, negative, error-handling,
and static-checker evidence. Do not claim that unexecuted discrimination or
equivalence probes passed. This non-critical limitation does not null the total
or force the package verdict to `NOT_ASSESSABLE`.

Every deduction records a deterministic deduction ID, finding ID, point value,
severity, observed fact, and exact affected location. Classification as
`METHOD_REIMPLEMENTATION`, `EXACT_REPRODUCTION`, or `SCIENTIFIC_EXTENSION`
never adds or removes points.

## Finding assignment

- solution role or Oracle completeness → solution completeness;
- checker crashes, unusable rewards, adversarial passes, quality-gradient
  failures, invariance failures, or solution-boundary failures → robustness
  and discrimination;
- known-valid rejection, checker/Gold paper findings, and defects in `tests/`
  contracts → checker/Gold alignment;
- instruction/data/method paper findings and scientific-target defects →
  scientific validity;
- instruction omissions, answerability defects, and unrecoverable public task
  definitions → instruction answerability.

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

## Report evidence

Every finding records an exact file plus line/quote when the source exists,
observed fact, impact, minimal repair, and retest. A missing file uses the exact
path with `line=null` and `quote=null`. Generic-only repair language is not a
valid authoritative finding.

`PASS` is also fail-closed under `materials-evidence-contract/1.0`:
authoritative materials qualification quotes instruction/tests evidence; all
five dimensions have non-empty evidence; no-paper review adjudicates all four
paper triggers with package evidence; every probe class records honest status
and provenance; assessed discrimination/equivalence uses an independent
non-Oracle fixture while unavailable classes explicitly record no fixture; and
solution completeness records only solve/positive-mock status, never Oracle
values. No findings is not positive evidence.

## Calibration migration

Artifacts produced under older scoring versions remain evidence archives, not
current scoring authority. Preserve their source hashes and findings, mark the
view as old scoring, then rerun the Review CLI from the frozen identity
manifest. Regenerate batch/index outputs from the new CLI reports; do not copy
old scores or verdicts into the rerun.
