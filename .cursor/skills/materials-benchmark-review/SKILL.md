---
name: materials-benchmark-review
description: Audit materials-science questions authored from papers for mandatory 2.1–2.8 acceptance, paper fidelity, scientific correctness, prompt consistency, checker coverage and discrimination, trustworthy Gold, leakage, security, and ready data/models/software. Use for Harbor question packages. The Agent adjudicates semantics; automation validates records and supplies fallible diagnostics.
---

# Materials Benchmark Review

Audit one paper-authored materials question before admission. The Agent is the
scientific and verdict authority. Deterministic diagnostics are hypotheses until
verified against primary files or usable runtime evidence.

Never use hidden answers or solution implementation as validity evidence. The
solution may only be executed in isolation to test whether a positive submission
can be produced and accepted. Scope checker quality to the final core scientific
results requested by the public task. Do not require the checker to read or
prove methods, traces, training logs, or intermediate artifacts.

## Required references

Read these before deciding:

- [audit-dimensions.md](references/audit-dimensions.md): mandatory 2.1–2.8,
  C01–C07 scoring, Hard Gates, and verdicts;
- [paper-grounded-audit.md](references/paper-grounded-audit.md): paper fidelity,
  reproduction intent, and the materials-parameter exception;
- [checker-audit.md](references/checker-audit.md): static mapping and required
  runtime probes;
- [resource-readiness.md](references/resource-readiness.md): data, pretrained
  models, software, environment, and access readiness.
- [mechanical-evidence.md](references/mechanical-evidence.md): conservative
  package/contract/AST/resource collectors and checker probe runner.

Read as applicable:

- [materials-gate.md](references/materials-gate.md);
- [task-types-and-leakage.md](references/task-types-and-leakage.md);
- [security-audit.md](references/security-audit.md);
- [report-schema.md](references/report-schema.md).

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

Roles and delivery contract:
- `instruction.md` is the ONLY file delivered to the solver. Judge leakage,
  solvability, and completeness solely against it.
- `solution/` is the reference solution used ONLY for Harbor self-check. It is
  never delivered to the solver and is never validity evidence; execute it only
  in isolation to confirm a positive submission can be produced/accepted.
- Grading runs `tests/test.sh` (which invokes `checker.py`/`grading_spec.json`)
  in an environment the solver cannot see; the solver never reads `tests/`.
- `paper/`, `resources.json`, `manifest.json`, `steps.json`, `task.toml`,
  `environment/` are authoring/reviewer/runtime provenance, not delivered to the
  solver.

## Inputs and scope

Locate functional equivalents of the instruction, paper/supplements, checker,
grading contract, public fixtures, test entrypoint, declared resources, and
environment. Names/layouts may vary; build a role map before judging.

Read the complete instruction and paper. For A2/A4/A5-equivalent judgments
(scientific validity, paper fidelity, Gold), paper reading is mandatory unless
the task is already proven `NON_MAT`.

Keep all audit artifacts outside the Harbor question package. Review never
mutates it.

## Workflow

1. Run the mechanical evidence collector. Review its `facts`, `candidates`, and
   `limitations`; it has no authority to create findings.
2. Classify materials qualification and reproduction intent.
3. Extract the scientific target, required inputs, fixed parameters,
   solver-selectable parameters, **final core scientific outputs**, answer type,
   and claimed capability. Explicitly exclude recommended methods, execution
   traces, training logs, and intermediate artifacts from the core-output map.
4. Check prompt self-consistency across workflow, output contract, grading, and
   self-check.
5. Compare instruction, data, method, parameters, and Gold with the paper.
6. Trace every final core scientific output:

   ```text
   public final-output requirement → checker read → scorer
   → effective weight → finite contribution → final reward
   ```

   Never add a process/trace-read requirement to this chain.
7. Run the mechanical checker probes (execution is mandatory), supply
   Agent-built valid/gradient/
   equivalence/component cases, and adjudicate all applicable classes under
   `checker-audit.md`.
8. Verify each required data/model/software/environment/access item is ready;
   distinguish prerequisites from outputs the solver must generate.
9. Audit leakage, security, feasibility, and reproducibility.
10. Assess 2.1–2.8 independently, score C01–C07, adjudicate all four Hard Gates,
   and record findings with exact evidence.
11. For every automated diagnostic use `CONFIRMED`,
    `DISMISSED_FALSE_POSITIVE`, or `AUTOMATION_LIMITATION`. Only confirmed
    defects affect the verdict.
    A local helper's inability to reproduce declared container paths is
    `AUTOMATION_LIMITATION`, unless evidence proves that the declared container
    layout, mount, or path itself is invalid.
12. Write `agent_final_decision.json` from
    `assets/agent_final_decision_template.json`, then run:

    ```bash
    python .cursor/skills/materials-benchmark-review/scripts/validate_agent_decision.py \
      <path>/agent_final_decision.json
    ```

## Non-negotiable publication rule

`PASS` is legal only when all 2.1–2.8 pass, score is at least 80, every Hard
Gate passes, required applicable probes pass, all readiness categories are
ready/not-required, and no open confirmed repairable HIGH/FATAL remains.

Do not return `NOT_ASSESSABLE` because a helper rejected a schema or layout.
If automation cannot assess a valid alternate representation, inspect it as the
Agent and record the limitation or false positive.
Do not finalize Review without executing applicable checker probes. An explicit
`--no-execute` run is diagnostic only and leaves checker criteria unassessed.

## Completion

Complete only when the decision validator passes, every required evidence item
is present, actual probe results are recorded honestly, and the user-facing
response states verdict, decisive evidence, confirmed repair needs, and the
decision-file location.
