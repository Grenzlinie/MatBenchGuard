---
name: materials-benchmark-repair
description: Repair materials-science paper question packages from an Agent-led review. Use confirmed 2.1–2.8 findings, paper/public evidence, isolated candidates, checker regressions, and equal-depth re-audit. Never repair dismissed schema false positives or invent scientific parameters, Gold, models, data, or tolerances.
---

# Materials Benchmark Repair

Repair confirmed defects without redefining the scientific task. Review evidence
is authoritative only after the Agent verifies it against current public files.

Never use hidden answers or solution content to choose scientific values. Never
modify a valid package merely to satisfy an internal schema.

Repair scope is the fair, usable, reproducible scoring of final core scientific
results. Do not repair a checker merely because it does not read a prescribed
method, trace, training log, or intermediate artifact. Audit Docker paths using
the package's declared container layout, not host-path coincidence.

## Harbor package structure and roles

A Harbor question package has exactly this required layout:

```
<paper-id>/
├── instruction.md
├── task.toml
├── manifest.json
├── steps.json
├── resources.json
├── environment/Dockerfile
├── paper/paper.md
├── paper/images_manifest.json
├── solution/solve.sh
└── tests/
    ├── checker.py
    ├── grading_spec.json
    └── test.sh
```

- `instruction.md` is the ONLY file delivered to the solver; repair solvability,
  completeness, and leakage against it alone.
- `solution/` is the Harbor self-check reference only — never delivered to the
  solver, never validity evidence.
- Grading runs `tests/test.sh` (invoking `checker.py`/`grading_spec.json`) in a
  solver-invisible environment; the solver never reads `tests/`.
- `paper/`, `resources.json`, `manifest.json`, `steps.json`, `task.toml`,
  `environment/` are provenance/runtime, not delivered to the solver.

The repaired candidate must preserve this required structure.

## Required references

Read before repair:

- [repair-policy.md](references/repair-policy.md);
- [repair-categories.md](references/repair-categories.md);
- [checker-repair.md](references/checker-repair.md) for checker/grading changes;
- [abandonment.md](references/abandonment.md);
- [report-schema.md](references/report-schema.md).

Also read the Review skill's audit dimensions, paper policy, checker audit, and
resource readiness rules. The candidate must pass the same full Review.

## Required input

Require the source package, validated `agent_final_decision.json`, confirmed
findings, and supporting evidence. Ignore diagnostics classified
`DISMISSED_FALSE_POSITIVE` or `AUTOMATION_LIMITATION`.

## Workflow

1. Verify the source decision is current and every repair target remains open.
2. Re-adjudicate existing findings under the final-result-only boundary. Remove
   findings based only on unread process/trace artifacts or host/container path
   mismatch. Classify every remaining confirmed finding as `AUTO_FIX`,
   `ASSISTED_FIX`, or `ABANDON`.
3. Copy the source to immutable `snapshot/` and editable `candidate/` outside
   the Harbor package.
4. Build the final-core-output scoring map. Run the Review mechanical collector
   and applicable probes on the snapshot; run each target regression and require
   the expected failure as the fail-before half of the retained
   fail-before/pass-after evidence. Container-only behavior that cannot be reproduced
   locally is a recorded automation limitation, not a defect.
5. Apply only evidence-backed changes mapped to confirmed findings.
   Uniquely determined checker defenses, Docker path-declaration synchronization,
   reward wiring, and public scoring-contract consistency are eligible repairs.
6. Record changed paths, before/after hashes, rationale, evidence, and patch.
7. Run the same collector, target regressions, and probes on the candidate;
   require pass-after and retain a before/after evidence comparison. Rerun
   relevant valid/invalid, gradient, equivalence, security, and readiness checks.
   Non-finite values, wrong types, missing fields, empty/malformed outputs,
   duplicate identifiers, unsafe formats, random/constant results, and
   task-relevant clearly wrong final results must receive zero or remain below
   the passing threshold. Previously valid final outputs must retain the same or
   a more scientifically reasonable score.
8. Perform exactly one equal-depth Review of the candidate, including the paper,
   all 2.1–2.8 criteria, C01–C07 score, four Hard Gates, parameter assessment,
   Gold/tolerances, the final-output reward chain, checker probes,
   data/model/software readiness, and Docker declarations.
9. Validate the new `agent_final_decision.json` with the Review validator.
10. Write `repair_report.json` from the bundled template and validate it:

    ```bash
    python .cursor/skills/materials-benchmark-repair/scripts/validate_repair_report.py \
      <path>/repair_report.json
    ```

    Publish only a validated `REPAIRED` candidate whose equal-depth Review is
    `PASS`; otherwise preserve the original and all evidence. All mutations stay
    in `/personal/qa_review/<cluster>/<theme>/<paper>/candidate`; the source
    Harbor package remains unchanged.

## Outcomes

- `REPAIRED`: re-audit is `PASS`, all targets resolved, regressions pass.
- `PARTIALLY_REPAIRED`: re-audit is `CONDITIONAL`, no Hard Gate, unresolved
  findings explicit; never publish.
- `ABANDONED`: re-audit is `REJECT` or safe repair requires guessing/redefinition.
- `ROLLED_BACK`: mutation or validation failed; original remains unchanged.
- Genuine `NOT_ASSESSABLE` remains resumable and is not abandonment.

In the user response state the outcome, repaired or blocking issues, and
candidate/evidence/report locations.
