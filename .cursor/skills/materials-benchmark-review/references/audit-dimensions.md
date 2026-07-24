# Required audit dimensions

All eight criteria are independent gates. Each is `PASS`, `FAIL`, or
`NOT_ASSESSABLE`; overall `PASS` requires all eight to be `PASS`.

## 2.1 Materials qualification

Establish a substantive materials object/system, materials data, scientific
operation, endpoint, and domain dependence. A materials-themed wrapper around
generic work does not pass.

## 2.2 Prompt completeness and consistency

Verify inputs, target, work, outputs, paths, formats, fields, types, units,
identifiers, reference versions, coordinates, missing values, duplicates, and
ordering. Workflow, output contract, grading description, and self-check must
agree. Every checker-required condition must be public. Separate final core
scientific outputs from recommended methods, optional/process artifacts,
traces, training logs, and intermediates. The latter are outside checker
coverage unless they are themselves the task's final scientific result.

## 2.3 Scientific validity and solvability

The target must be meaningful, the method appropriate, and the task solvable
independently from declared inputs. Compare instruction, data, method, fixed
parameters, and intended result with the paper. Apply the parameter policy in
`paper-grounded-audit.md`.

## 2.4 Checker assesses core science

For every final core scientific output trace only:

```text
public final-output requirement → checker read → scorer binding
→ positive weight → finite contribution → final reward
```

Existence, syntax, metadata, or unrelated constants alone are insufficient.
Do not require evidence that a prescribed/recommended method was followed, and
do not require a trace, training log, or intermediate artifact to be read.

## 2.5 Scoring discrimination

Correct/high-quality final results must score well; clearly wrong, invalid, or
missing final results must score poorly. Score must be monotonic with final
scientific quality, scientifically equivalent outputs must be treated
equivalently, and one easy component must not bypass missing core results.
Failure to prove that a specified process was followed is not a scoring defect
when the final core scientific result is fairly assessed.

## 2.6 Gold and tolerance credibility

Gold, equivalence rules, direction, thresholds, and tolerances must be supported
by the paper or another public authoritative source and consistent between the
grading specification and checker. Paper-sourced Gold is expected and does not
require an invented second Gold set. A method's own output must be described as
method agreement rather than independent truth unless externally validated.

## 2.7 No answer leakage or exploit

Leakage is judged ONLY against `instruction.md` — the sole file the solver
receives. Everything else (`paper/**`, `solution/**`, `tests/**`,
`resources.json`, `manifest.json`, `metadata`) is reviewer/harness-side or
human-reference material and is NOT delivered to the solver. Therefore Gold,
numeric results, hidden acceptance values, or tolerances appearing anywhere
outside `instruction.md` are by design and are NOT leakage. Do NOT open a
leakage finding or Hard Gate solely because an answer appears in the paper, the
solution, the checker, or a resource/metadata file.

Within `instruction.md`, the prompt must not disclose numeric answers, hidden
acceptance values, or paper identity that permits answer lookup instead of
scientific work. Methods and formulas are not leakage. A gameable or
trivially-bypassable checker is still a checker-quality defect under 2.5/C04 —
report it there, not as leakage.

## 2.8 Inputs and reproducibility ready

All prerequisite data, pretrained models/weights, indispensable software,
environment requirements, and legal access must be ready or explicitly not
required. Solver-generated models/structures/intermediates are outputs, not
missing prerequisites. See `resource-readiness.md`.

## C01–C07 score

| Dimension | Weight | Scope |
|---|---:|---|
| C01 | 10 | materials admission |
| C02 | 20 | prompt completeness and consistency |
| C03 | 20 | scientific validity and solvability |
| C04 | 20 | checker and Gold semantics |
| C05 | 10 | answer and identity leakage |
| C06 | 10 | inputs, paper fidelity, reproducibility |
| C07 | 10 | discrimination and auditability |

Each dimension has a 0–100 normalized score and positive evidence. Weighted
total is `sum(weight × normalized / 100)`. Attribute each finding to one
dimension only.

Exactly four Hard Gates exist:

- `NON_MATERIALS_TASK` → C01;
- `SCIENTIFIC_TARGET_INVALID` → C03;
- `CHECKER_CORE_TASK_UNASSESSED` → C04;
- `INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE` → C06.

`PASS` requires all eight criteria PASS, total ≥80, all Hard Gates PASS, all
applicable required probes pass, and no open confirmed repairable HIGH/FATAL.
`CONDITIONAL` requires no failed Hard Gate and either total 60–79 or a confirmed
repairable defect. `REJECT` follows a failed Hard Gate, total <60, or
unrecoverable FATAL. `NOT_ASSESSABLE` is only genuine temporary evidence loss.
