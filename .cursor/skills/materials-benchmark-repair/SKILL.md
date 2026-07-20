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
  --audit-attestation <immutable-external-attestation.json>
```

Historical plans use schema `0.1` and remain readable as evidence archives.
New deterministic plans use
`materials-deterministic-repair-plan/1.0` (the transitional wire spelling
`0.2` is accepted) and bind the source deterministic schema, registry, digest,
and complete queue. A deterministic plan must carry one `audit_id` plus a
`findings[]` list containing every source `required_finding_id`; omission,
unknown D1–D6 ownership, stale schema/digest, or a stale source binding fails
closed before mutation. Each finding carries its own decision, operations,
evidence, and regressions:

```json
{
  "schema_version": "materials-deterministic-repair-plan/1.0",
  "audit_id": "authoritative audit id",
  "deterministic_contract": {
    "schema_version": "materials-deterministic-contract/1.0",
    "registry_version": "materials-deterministic-check-registry/1.0",
    "contract_digest": "sha256:...",
    "audit_id": "authoritative audit id",
    "required_finding_ids": ["every OPEN blocking finding"]
  },
  "source_audit": { "audit_id": "...", "input_hashes": {}, "paper_mode": "paper_grounded", "execution_level": "E1", "core_contract_digest": "..." },
  "core_contract_digest": "frozen digest",
  "findings": [
    {
      "finding_id": "one open finding id",
      "repair_class": "AUTO_FIX, ASSISTED_FIX, or ABANDON",
      "justification": "why this repair resolves the finding",
      "core_science_change": false,
      "evidence": [{ "id": "e1", "source": "paper/paper.md or benchmark_audit:<finding>", "quote": "verifiable text", "source_hash": "sha256:..." }],
      "operations": [],
      "regression_tests": []
    }
  ]
}
```

A legacy single-finding plan (top-level `finding_id`/`operations`) and an
unbound `0.1` batch are still accepted for historical compatibility. They are
not evidence that the D1–D6 contract was assessed; a new deterministic
publication must use the bound schema above.

There is no human approval state. The closed decision classes are autonomous:

- `AUTO_FIX` is deterministic and needs no scientific interpretation.
- `ASSISTED_FIX` makes an evidence-backed scientific or checker correction;
  every operation must link one or more plan evidence IDs.
- `ABANDON` records a reason only and carries no operations.

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

The batch resolves to one of four states, mapped to the unified terminal fields
`disposition` / `publishable` / `repair_state`:

| repair_state | when | disposition | publishable | package |
|---|---|---|---|---|
| `REPAIRED` | the one equal-depth E1 re-audit is PASS, D1–D6 is CLEAN, no Hard Gate exists, identity and allowed mutation scope are preserved, and every batch finding is resolved | `PASS` | `true` | atomically published |
| `PARTIALLY_REPAIRED` | some findings resolved but re-audit not PASS, or some `BLOCKED_EVIDENCE`/`ABANDON` remain | `CONDITIONAL` | `false` | original preserved |
| `ABANDONED` | nothing fixable, or re-audit still FATAL / hits a Hard Gate / needs a core-science change | `REJECT` | `false` | original preserved |
| `ROLLED_BACK` | batch apply or regression failed | source verdict | `false` | restored unchanged |

**Publish invariant:** for a deterministic plan, atomic publication requires
`PASS + deterministic CLEAN + no Hard Gate + identity preserved + allowed
mutation scope + all target findings resolved`, with `reaudit_count=1` at E1.
Any residual deterministic blocker is a non-published
`PARTIALLY_REPAIRED`/`ABANDONED`/`ROLLED_BACK` result. Never publish a
partially-fixed package. The old `PUBLISHED` state remains readable only for
legacy certification archives.

## Attempt limit

The limit is per `audit_id` batch, not per finding. The first batch that does
not reach PASS is `ROLLED_BACK`/`PARTIALLY_REPAIRED`; a second unresolved batch,
or any post-repair FATAL that remains, converges to `ABANDONED`. Later calls
return the existing `ABANDONED` state and never create a third candidate.

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
- reuse the audit's 2.5 checker-coverage finding to fix C04/C02 checker gaps,
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
- Evidence sources must be local package files under an allowed evidence root,
  with a stored `source_hash`; absolute paths, URLs, symlinks, and traversal are
  rejected.
- The quote's precision must be at least as specific as the change. A quote that
  only proves "the file exists" may not add fields, types, units, or
  requiredness.
- Sensitive operations need type-matched evidence: a new JSON key / CSV column
  needs a field schema; changing a Gold value or tolerance needs a numeric value
  with unit and a source or reproducible derivation; changing weights or
  thresholds needs the scoring-contract field/value plus a mathematical proof.
- Paper evidence is always available but must bind the exact `paper/**` file the
  source audit hashed; a hash mismatch or unbound paper file → `BLOCKED_EVIDENCE`.
- Oracle/solution and metadata content cannot support scientific, schema, or
  scoring changes, and solution content cannot become public instruction text.

## Abandon triggers (deterministic)

Repair abandons (or rolls back) when the Gold source is unverifiable or conflicts
with the paper, when multiple valid answers lack a fair scoring scheme, when the
checker must redefine the task to be fixable, when the same audit batch is
unresolved after two attempts, or when a post-repair FATAL finding remains.

## Isolated execution and publication

Require a read-only external attestation that binds the exact manifest, report,
disposition, fixture, and assessment hashes; the package-local manifest cannot
authenticate itself. Authenticate every manifest-declared audit output and
require the manifest's Review implementation hashes to match the installed
Review. Plan-provided fixture/assessment hashes are not authoritative. On a full
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
