---
name: materials-benchmark-repair
description: Repair one audited materials-science Harbor 题包 by fixing all fixable findings from one audit in a single isolated, tested, equal-depth batch, then re-auditing exactly once. Use only after materials-benchmark-review routes a package to REPAIR_QUEUE.
---

# Materials Benchmark Repair

Repair one Harbor 题包 per source audit. Review supplies evidence and owns no
mutations. The Agent writes an external, evidence-backed **batch** plan that
lists every OPEN blocking D1–D6 finding from that audit; Repair validates and
executes it in one isolated pass, then runs the equal-depth Review CLI exactly
once. The re-audit is the sole post-repair authority.

## Public seam

Keep the plan outside the 题包 and run:

```sh
python scripts/run_repair.py <Harbor题包目录> \
  --plan <repair-plan.json> \
  --audit-attestation <immutable-external-attestation.json> \
  --audit-dir <external-source-audit/benchmark_audit> \
  --repair-output-dir <external-record-directory>
```
The source audit may also live in an external sibling record directory; the
Harbor 题包 must not receive generated audit or repair-report files.
`--repair-output-dir` stores the re-audit, repair bundle, and attempt history
outside the package. The equal-depth re-audit invokes Review with only the
candidate and its Agent-quality assessment; Review generates all synthetic
probe cases inside the external re-audit workspace.

Deterministic plans use
`materials-deterministic-repair-plan/1.0` and bind the source deterministic schema, registry, digest,
and complete queue. A deterministic plan must carry one `audit_id` plus a
`findings[]` list containing every source `required_finding_id`; omission,
unknown D1–D6 ownership, stale schema/digest, or a stale source binding fails
closed before mutation. Each finding carries its own decision, operations,
precise evidence links, and causal regressions; `run_repair.py` enforces the
complete schema.

There is no human approval state. The closed decision classes are autonomous:

- For D1–D6, `AUTO_FIX` is narrowly limited to restoring existing
  contract/scoring wiring with a unique source-bound answer: synchronize an
  existing output declaration/path, restore an existing scorer
  registration/binding/return or final-reward connection, restore a standard
  Harbor entrypoint around one unique existing producer, or normalize already
  declared finite positive weights while preserving their proven ratios.
- D1–D6 `AUTO_FIX` must not introduce or choose Gold values, targets,
  tolerances, thresholds, formulas, scorer algorithms, fields, units,
  scientific parameters, or science semantics. It also must not fabricate a
  producer or make an ignored core output appear scored through a superficial
  read.
- `AUTO_FIX` operations require `core_science_change=false`, source-bound
  proof, and one causal fail-before/pass-after regression. A passing
  regression is not scientific evidence.
- `ASSISTED_FIX` makes an Agent-authored evidence-backed scientific or scoring
  correction; every operation must link one or more plan evidence IDs. Each
  linked item must declare `source_kind` as `PACKAGE_PAPER`,
  `PACKAGE_DIRECT_SOURCE`, or `AUTHORITATIVE_PRIMARY_WEB`, carry an exact quote,
  an `exact_quote`, matching source hash, applicability, derivation, and
  `core_science_change=false`. Package paper/direct-source evidence must bind
  the source-audit hash. Web evidence additionally requires an HTTPS `url`,
  `retrieved_at`, non-empty `retrieval_metadata`, and an explicit approval
  object with `approved=true`, `primary=true`, an authoritative source class,
  and an approval reference. Conflicting, ambiguous, or type-mismatched
  evidence is `BLOCKED_EVIDENCE`; Repair never guesses.
- Agent-quality findings never receive D1–D6 ownership and can never be
  reclassified as deterministic `AUTO_FIX`. Changes outside the narrow D1–D6
  automatic boundary require `ASSISTED_FIX` only when the evidence precision is
  sufficient.
- `ABANDON` records a reason only and carries no operations.

If evidence cannot support the requested semantic choice, record
`BLOCKED_EVIDENCE` and abandon that operation rather than guessing. Oracle or
solution content and metadata cannot support a public contract, schema,
scoring, or science change; Oracle values must never enter repair evidence.

## Batch flow (one pass, one re-audit)

1. Freeze the core-contract digest over `instruction.md`, `tests/**`, and
   `solution/**` (including `tests/test.sh`), authenticate the external audit
   attestation, verify the source-audit binding, and confirm every non-ABANDON
   target finding is still OPEN.
2. Classify each finding. Finding-level policy violations block that finding;
   an operation that fails the evidence-precision matrix is recorded
   `BLOCKED_EVIDENCE` **without blocking its sibling operations or findings**.
3. Copy the package to an isolated `snapshot/` and `candidate/`, run every
   causal regression against the snapshot (fail-before), apply all valid
   operations to the candidate in one pass (recording before/after hashes and
   evidence links), then run the regressions against the candidate (pass-after).
   Each operation needs one exact operation-semantic regression assertion.
4. Run the canonical Review CLI **exactly once** at the source audit's paper
   mode and E1 execution level. Emit the before/after C01–C07 normalized
   percentages and Δ(pp) from that single re-audit. No local score, finding
   heuristic, or regression result can publish a candidate.

## Terminal states and unified fields

The batch resolves to one of five states, mapped to the unified terminal fields
`disposition` / `publishable` / `repair_state`:

| repair_state | when | disposition | publishable | package |
|---|---|---|---|---|
| `REPAIRED` | the one equal-depth E1 re-audit is PASS, D1–D6 is CLEAN, no Hard Gate exists, identity and allowed mutation scope are preserved, and every batch finding is resolved | `PASS` | `true` | atomically published |
| `PARTIALLY_REPAIRED` | some findings resolved but re-audit not PASS, or some `BLOCKED_EVIDENCE`/`ABANDON` remain | `CONDITIONAL` | `false` | original preserved |
| `ABANDONED` | nothing fixable, or re-audit still FATAL / hits a Hard Gate / needs a core-science change | `REJECT` | `false` | original preserved |
| `ROLLED_BACK` | batch apply or regression failed | source verdict | `false` | restored unchanged |
| `INFRASTRUCTURE_BLOCKED` | a deterministic control failure occurs, one control fingerprint repeats twice, or three control failures occur in one environment scope | source verdict | `false` | restored unchanged |

**Publish invariant:** for a deterministic or assisted plan, atomic publication
requires `PASS + total_score >= 80 + deterministic CLEAN + no Hard Gate + no
unresolved HIGH/FATAL finding + identity preserved + allowed mutation scope +
all target findings resolved`, with `reaudit_count=1` at E1.
Any residual deterministic blocker is a non-published
`PARTIALLY_REPAIRED`/`ABANDONED`/`ROLLED_BACK`/
`INFRASTRUCTURE_BLOCKED` result. Never publish a
partially-fixed package.

## Attempt limit

The limit is per `audit_id` batch, not per finding, and counts only completed
equal-depth semantic re-audits. Setup, Docker, regression
harness, apply, or Review invocation failures are `CONTROL_FAILURE` rollbacks
with `attempt_consumed=false`; they never exhaust the package's semantic
budget. They have a separate circuit breaker: deterministic attestation and
evidence failures block immediately; the same transient
fingerprint blocks on its second occurrence; rotating transient failures block
on the third occurrence in one scope. A blocked control state is
`INFRASTRUCTURE_BLOCKED` with `retryable=false` and is returned without creating
more histories. The scope binds the audit, Review/Repair implementation,
Dockerfile, configured image identity, and therefore resets only after a
relevant environment or implementation change. The first completed re-audit
that does not reach PASS is
`PARTIALLY_REPAIRED`; a second unresolved completed re-audit, or a post-repair
FATAL, converges to `ABANDONED`. Later calls return the existing `ABANDONED`
state and never create a third semantic candidate.

## Allowed changes

Only `instruction.md`, `tests/**`, and `solution/**` are modifiable. `paper/**`
and every metadata/environment role are read-only. Supported operations are
`write_file`, `replace_text`, `json_set`, and `delete_file`; `write_file` may
create a missing `solution/solve.sh` with its executable bit, so a missing or
broken solution entrypoint is repairable, not an automatic rejection. Supported
regressions are `file_exists`, `file_absent`, `file_executable`, `text_contains`,
`text_not_contains`, `json_path_equals`, and argv `command`.

Regression specifications of type `command` run through the shared disposable
`qa-checker` Docker sandbox, using the same image and operator preflight as
Review. Build the image once with
`.cursor/skills/materials-benchmark-review/scripts/sandbox/build_qa_checker.sh`;
Docker/image/cache setup failures abort the repair operation rather than being
recorded as a package regression result.

## Materials repair scope

Repair **can**:

- restore structure/config integrity (missing entrypoint, malformed JSON/CSV),
- normalize the public instruction to the frozen scientific contract with
  paper/instruction evidence,
- reuse the audit's 2.5 checker-coverage finding only to restore existing
  C04/C02 contract or scoring wiring,
- fix Harbor-path or add exception handling (no scientific paper required).

Repair **cannot**:

- redefine the core scientific question, endpoint, material system, or claimed
  reproduction type (`core_science_change` must be `false`);
- guess a scientific parameter, Gold value, tolerance, weight, or threshold
  without exact, type-matched evidence;
- treat a passing checker alone as scientific evidence.

Resource/data/software/environment repairs apply **only** to C06-probed
indispensable direct inputs. Do **not** probe or repair solver-generated
structures/trajectories/models, routine DFT/MD parameters (k-mesh, cutoffs,
convergence, seeds, supercells), substitutable software, or the paper's
historical software/version/parameter list.

## Evidence-precision matrix (no fabrication)

- A claimed local source file that does not exist → `BLOCKED_EVIDENCE`, even
  before any file is written.
- Package evidence sources must be local files under an allowed evidence root,
  with a stored `source_hash`; absolute paths, symlinks, and traversal are
  rejected. URLs are accepted only for the explicitly approved
  `AUTHORITATIVE_PRIMARY_WEB` form described below.
- The quote's precision must be at least as specific as the change. A quote that
  only proves "the file exists" may not add fields, types, units, or
  requiredness.
- Sensitive operations need type-matched evidence: a new JSON key / CSV column
  needs a field schema; changing a Gold value or tolerance needs a numeric value
  with unit and a source or reproducible derivation; changing weights or
  thresholds needs the scoring-contract field/value plus a mathematical proof.
- Paper evidence is always available but must bind the exact `paper/**` file the
  source audit hashed; a hash mismatch or unbound paper file → `BLOCKED_EVIDENCE`.
- A package direct source is limited to source-audit-hashed `data/**`,
  `direct_sources/**`, `inputs/**`, `reference(s)/**`, `resources/**`,
  `sources/**`, `instruction.md`, or `resources.json`. Web evidence is not
  fetched during Repair: its quoted content hash, URL, retrieval metadata, and
  explicit primary-source approval must already be present and consistent.
- Oracle/solution and metadata content cannot support scientific, schema, or
  scoring changes, and solution content cannot become public instruction text.

## Abandon triggers (deterministic)

Repair is not entered when the source Review total is below 60. A re-audit
total below 60 abandons the candidate and cannot start another semantic
attempt; 60–79 may remain `PARTIALLY_REPAIRED`. Repair abandons (or rolls back)
when the Gold source is unverifiable or conflicts with the paper, when multiple
valid answers lack a fair scoring scheme, when the checker must redefine the
task to be fixable, when the same audit batch is unresolved after two attempts,
or when a post-repair FATAL finding remains.

## Isolated execution and publication

Require a read-only external attestation that binds the exact manifest, report,
disposition, and assessment hashes; the package-local manifest cannot
authenticate itself. Authenticate every manifest-declared audit output and
require the manifest's Review implementation hashes to match the installed
Review. Plan-provided assessment hashes are not authoritative. On a full
re-audit PASS, write the fixed repair bundle (`repair_plan.json`, `changes.json`,
`unresolved.json`, `regression_results.json`, `re_audit_comparison.json`,
`patch.json`, `evidence.json`, `repair.log`, `history.json`), rebase generated
Review paths, and atomically replace the authoritative package. Every published,
partial, abandoned, and rolled-back attempt archives the full snapshot,
candidate, plan, and a complete, self-validating history bundle.

## Completion

A batch repair is complete when its terminal state and unified terminal fields
are written, the equal-depth re-audit ran exactly once, the before/after C01–C07
delta is recorded, package identity is preserved, and the history bundle
validates. Publication happens only in the `REPAIRED` state.
