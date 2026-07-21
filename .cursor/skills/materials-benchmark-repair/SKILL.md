---
name: materials-benchmark-repair
description: Repair one audited materials-science Harbor package in one isolated, tested batch and exactly one equal-depth Review re-audit, publishing only a fully verified REPAIRED result.
---

# Materials Benchmark Repair

Repair one Harbor package from one immutable Review audit. Review owns
evidence and no mutations; Repair validates an external batch plan, applies all
valid operations once in isolation, and invokes the canonical Review CLI
exactly once. The re-audit is the sole post-repair authority.

## Public seam and output policy

Plans, attestations, audit bundles, repair bundles, snapshots, candidates, and
histories stay outside the Harbor package:

```sh
python scripts/run_repair.py <Harbor题包目录> \
  --plan <repair-plan.json> \
  --audit-attestation <immutable-external-attestation.json> \
  --audit-dir <external-source-audit/benchmark_audit> \
  --repair-output-dir <external-record-directory>
```

The source audit and `--repair-output-dir` are external siblings. The package
must not receive generated audit or repair-report files. Review generates all
synthetic probes inside the external re-audit workspace.

Repair holds the same canonical source-output lock for its full lifecycle, so
Review cannot replace the source audit during pending, resume, re-audit, or
publication. The source bundle's byte digest is recorded and rechecked at
each boundary; any change fails closed and requires a fresh audit.

If equal-depth Review returns `AGENT_CONTRACT_PENDING`, preserve the candidate
and workspace without consuming an attempt. Resume the exact `repair_id`:

```sh
python scripts/run_repair.py <Harbor题包目录> \
  --plan <repair-plan.json> \
  --audit-attestation <immutable-external-attestation.json> \
  --audit-dir <external-source-audit/benchmark_audit> \
  --repair-output-dir <external-record-directory> \
  --resume-repair-id <repair-id> \
  --agent-contract-assessment <assessment.json>
```

Pending has `status=AGENT_CONTRACT_PENDING`,
`repair_state=AGENT_CONTRACT_PENDING`, `review_verdict=NOT_ASSESSABLE`,
`publishability=EVIDENCE_PENDING`, `publishable=false`, and
`attempt_consumed=false`. Resume validates package, plan, request, machine
contract, probe, and workspace bindings; it reuses probes and creates no
semantic attempt.

## Plan, assessment, and AUTO_FIX contract

Deterministic plans use `materials-deterministic-repair-plan/1.0` and bind the
source schema, registry, digest, audit ID, and complete
`required_finding_ids` queue. Every finding carries its decision, operations,
evidence links, and causal regressions. Omission, unknown D1-D6 ownership, or
stale binding fails closed before mutation.
Active Repair accepts no legacy plan aliases and every plan is a batch.
Historical 0.1/0.2 plans are readable only as archived bundle evidence.

The machine contract remains authoritative. A contract-only assessment may
overlay only an eligible unavailable (`BLOCKED`/`NOT_ASSESSABLE`) check. It
cannot override machine `FAIL`, proven facts, blockers, missing-input
failures, runtime contradictions, Hard Gates, or Agent-quality findings.
Accepted evidence is only `instruction.md`, `tests/**/grading_spec` (with an
optional extension), and deterministic probe artifacts. It cannot use paper,
solution, Oracle, metadata, Gold, targets, tolerances, formulas, units,
thresholds, or science-quality evidence.

The autonomous decision set is `AUTO_FIX`, `ASSISTED_FIX`, `ABANDON`; there is
no human approval state. `AUTO_FIX` is limited to unique, source-bound
restoration of existing D1-D6 contract/scoring wiring:

- synchronize an existing output declaration/path;
- restore existing scorer registration, binding, return, or final-reward links;
- restore a standard Harbor entrypoint around one existing producer;
- normalize already-declared finite positive weights without changing ratios.

`AUTO_FIX` cannot introduce or choose Gold, targets, tolerances, thresholds,
formulas, scorer algorithms, fields, units, scientific parameters, producers,
or science semantics. It cannot make an ignored core output appear scored.
Each operation requires `core_science_change=false`, source-bound proof, and a
causal fail-before/pass-after regression; a passing regression is not science
evidence.

`ASSISTED_FIX` is Agent-authored and evidence-backed; every operation links
plan evidence IDs. Each item records `source_kind`, `exact_quote`, and
`source_hash`. Local paper/direct-source evidence must bind the source audit.
Approved primary-web evidence additionally needs HTTPS URL, `retrieved_at`,
`retrieval_metadata`, applicability, derivation, and explicit primary approval.
Missing, conflicting, ambiguous, or type-mismatched evidence is
`BLOCKED_EVIDENCE`; never guess. Agent-quality findings never receive D1-D6
ownership. `ABANDON` has no operations. Oracle, solution, and metadata content
cannot support a public contract or science change. `ABANDON` is available for
every required D1-D6 finding, but it still binds the complete current queue,
source audit, source hashes, package identity, contract digest, and current
Review implementation.

Detailed evidence, scope, and lifecycle rules are in
[references/repair-protocol.md](references/repair-protocol.md).

## One-pass isolated flow

1. Authenticate the read-only external attestation, source audit, package
   identity, and Review implementation hashes.
2. Freeze the core digest over `instruction.md`, `tests/**`, and `solution/**`
   (including `tests/test.sh`); confirm every target, including `ABANDON`,
   remains `OPEN`.
3. Copy isolated `snapshot/` and `candidate/` trees. Run all regressions
   fail-before, apply valid operations once with before/after hashes, then run
   all regressions pass-after.
4. Run Review exactly once at the source audit's paper mode and dual-lane
   depth. Emit C01-C07 before/after normalized scores and delta (pp).

The equal-depth Review uses its own unique run workspace and atomic publication
lock. It never reuses or deletes another run's temporary workspace. A
source-attested audit is immutable: Repair may authenticate it but may not
rewrite, rebase, or refresh its manifest hashes.

No local score, finding heuristic, or regression result can publish a
candidate. Retain complete candidate, snapshot, re-audit, unresolved,
comparison, evidence, and history data for every non-pending outcome.

## Terminal states and atomic publication

All results use `disposition`, `publishable`, and `repair_state`:

| repair_state | disposition | publishable | package |
|---|---|---|---|
| `REPAIRED` | `PASS` | `true` | atomically published |
| `PARTIALLY_REPAIRED` | `CONDITIONAL` | `false` | original preserved |
| `ABANDONED` | `REJECT` | `false` | original preserved |
| `ROLLED_BACK` | source verdict | `false` | restored unchanged |
| `INFRASTRUCTURE_BLOCKED` | source verdict | `false` | restored unchanged |

Atomic publication requires PASS, score ≥80, effective deterministic CLEAN,
no Hard Gate, preserved identity, allowed mutation scope, no unresolved
HIGH/FATAL finding, every target resolved, and exactly one equal-depth
re-audit. Any residual deterministic blocker is non-published.

The semantic attempt limit is two completed re-audits per `audit_id`.
Setup/Docker/regression/apply/Review control failures do not consume it and
use the circuit breaker in `run_repair.py`. A second unresolved semantic
re-audit or post-repair FATAL converges to `ABANDONED`.

## Allowed package changes and regressions

Only `instruction.md`, `tests/**`, and `solution/**` may change.
`paper/**`, metadata, and environment roles are read-only. Supported
operations are `write_file`, `replace_text`, `json_set`, and `delete_file`;
`write_file` may create an executable `solution/solve.sh`.

Regression types are `file_exists`, `file_absent`, `file_executable`,
`text_contains`, `text_not_contains`, `json_path_equals`, and argv `command`.
Command regressions run through the shared disposable `qa-checker` Docker
sandbox, using the same image and preflight as Review:

```sh
.cursor/skills/materials-benchmark-review/scripts/sandbox/build_qa_checker.sh
```

Docker/image/cache setup failures abort the operation as control failures.
Do not probe or repair solver-generated structures/trajectories/models,
routine DFT/MD parameters, substitutable software, or historical software
versions. C06 resource repair is limited to indispensable direct inputs.

## Completion

A nonexistent claimed source is `BLOCKED_EVIDENCE` before writing. Evidence
paths must be allowed local files without traversal, absolute paths, or
symlinks, and must store source hashes. Quote precision must support the
change's precision: new fields/columns need schemas; Gold/tolerance changes
need value, unit, source or derivation; weights/thresholds need contract value
and proof. Paper evidence binds the exact hashed `paper/**` file. Web content
is not fetched during Repair. Solution/Oracle values cannot enter evidence.

Repair is not entered below source score 60. A re-audit below 60 abandons;
60–79 may remain partial. Unverifiable Gold, conflicting paper evidence,
multiple fair answers without scoring, required core-science changes, or
unresolved severe findings trigger abandon/rollback.

Completion requires terminal fields, exactly one equal-depth re-audit,
before/after C01-C07 delta, preserved identity, allowed scope, and a
self-validating history bundle. Publication happens only in `REPAIRED`.
