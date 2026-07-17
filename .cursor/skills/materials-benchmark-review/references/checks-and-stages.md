# Stages, checks, and terminal fields

## Stage flow (0 → 5)

```
[Stage 0 Materials admissibility]  Agent reads Problem background / Approach /
  Reproduction target and adjudicates (no keyword prescreen).
  ├─ NON_MAT ─────► fail-fast REJECT (C01 Hard Gate); paper is NOT read.
  └─ MAT_CORE / MAT_METHOD / MAT_WRAPPER / AMBIGUOUS → continue (Wrapper is a task).
[Stage 1 Deterministic D-layer]  D1–D7, all repairable.
[Stage 2 LLM A-layer]  A1–A5; each declares its input files; default paper-grounded.
[Stage 3 Score + disposition]  C01–C07 normalized + weighted total + Hard Gates +
  verdict + unified terminal fields.
  ├─ PASS           → publishable=true
  ├─ CONDITIONAL    → repair
  ├─ REJECT         → abandon (total < 60 or a Hard Gate)
  └─ NOT_ASSESSABLE → re-audit after evidence is restored
[Stage 4 Repair (CONDITIONAL only)]  AUTO_FIX / ASSISTED_FIX / ABANDON in isolation.
[Stage 5 Re-audit + compare]  Re-run Review; emit before/after C01–C07 and delta.
```

## Classification reform (Agent-adjudicated)

Classification is authoritative from the Agent reading the instruction's
structured fields `## Problem background`, `## Approach`, and
`## Reproduction target`; if fields are missing, the Agent reads the whole text
and records `AMBIGUOUS`. There is no keyword prescreen. The Agent emits a
classification in {MAT_CORE, MAT_METHOD, MAT_WRAPPER, NON_MAT, AMBIGUOUS} with an
exact `package_file` + `package_quote` per class. Only `NON_MAT` triggers the C01
Hard Gate (REJECT); every other class continues (`AMBIGUOUS` may require more
evidence and re-audit). Deterministic code only **validates** the Agent
classification (quotes exist in the instruction, labels legal, three-field
evidence complete); when no authoritative classification is supplied the package
is `NOT_ASSESSABLE`.

## D-layer (deterministic, repairable)

| # | name | key files | method |
|---|---|---|---|
| D1 | output-file declaration consistency | `instruction.md`, `tests/grading_spec.json` | extract output paths + set compare |
| D2 | instruction internal consistency | `instruction.md` (Workflow steps ↔ Output files ↔ Output contract ↔ Self-check) | section parse + name/field/format set compare |
| D3 | checker code health | `tests/checker.py` | `ast.parse` + AST pattern (always-pass / literal div-zero / direction reversal) |
| D4 | weight normalization | `tests/grading_spec.json`, `tests/checker.py` | sum weights (tol 1e-6), flag zero-weight |
| D5 | package file completeness (Harbor entry) | `instruction.md`, `tests/checker.py`, `tests/grading_spec.json`, `tests/test.sh`, `solution` | existence + parse_status |
| D6 | checker core-task mapping (static) | `instruction.md`, `tests/checker.py`, `tests/grading_spec.json` | contract-chain map + AST binding |
| D7 | dynamic robustness & discrimination | `tests/test.sh`, `tests/checker.py`, external fixture | run `tests/test.sh` + reward compare (negative / discrimination / equivalence / component-isolation) |

## A-layer (LLM, code-verified quotes)

| # | name | direction | key inputs | notes |
|---|---|---|---|---|
| A1 | domain & capability-goal consistency | is it a materials task + claimed vs. actually-scored capability | `instruction` (Problem background / Approach / Reproduction target) + `tests` | classify; align capability with checker |
| A2 | scientific validity & solvability (necessary definitions) | method adequacy, missing necessary definitions, fair solvability | `instruction` + **paper (always read)** | missing structure/supercell/k-mesh/unit → confirm against the paper text; equivalent software/solver params allowed |
| A3 | answer & identity leakage | does instruction expose forbidden info | `instruction` + `grading_spec` + paper | numeric-result leakage (formulas ok); traceable identity leakage |
| A4 | paper fidelity & reproducibility | are instruction/data/params/Gold faithful and reproducible | **paper (always read)** + `instruction` + direct-input probe | EXACT / METHOD (default) / EXTENSION |
| A5 | Gold credibility | is Gold/tolerance/scoring basis credible and method-independent | `tests/grading_spec`, `tests/checker.py`, **paper (always read)** | see A5 checklist in `paper-grounded-audit.md` |

There is no paper trigger switch: A2/A4/A5 always read `paper/`; A1/A3 are
package-first and may extend to the paper. The only path that skips the paper is
the Stage 0 `NON_MAT` fail-fast. Every A-layer conclusion cites an exact
package/paper quote verified by deterministic code.

## Dimension → check mapping and Hard Gates

| dim | family | main D | main A |
|---|---|---|---|
| C01 domain admissibility | admissibility | — | A1 |
| C02 design completeness & file consistency | deterministic | D1, D2, D4, D5 | — |
| C03 scientific validity & solvability | scientific | — | A2 |
| C04 scoring semantics | deterministic | D3, D6, D7 | A5 (part) |
| C05 answer leakage | scientific | D6 (solution boundary) | A3 |
| C06 reproducibility | scientific | D5 (resources), direct-input probe | A4 |
| C07 difficulty & auditability | deterministic + scientific | D7 (discrimination/equivalence) | A2/A5 (part) |

The four Hard Gates bind to dimensions: C01 (not a materials task / NON_MAT),
C03 (scientifically invalid or unrecoverable missing definition), C04 (checker
does not evaluate the core task and cannot be repaired without redefining it),
and C06 (an indispensable direct input is permanently unavailable with no
equivalent).

## Unified terminal fields

Every report and disposition carries `disposition` (PASS / CONDITIONAL / REJECT /
NOT_ASSESSABLE), `publishable` (bool), and `repair_state` (NOT_REQUIRED at
review time; REPAIRED / PARTIALLY_REPAIRED / ABANDONED / ROLLED_BACK after
repair). `publication_route` mirrors the legacy publishability route
(PUBLISH_CANDIDATE / REPAIR_QUEUE / QUARANTINE / EVIDENCE_PENDING).
