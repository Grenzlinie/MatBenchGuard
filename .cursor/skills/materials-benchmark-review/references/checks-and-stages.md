# Stages, checks, and terminal fields

## Stage flow (0 → 5)

```
[Stage 0 Materials admissibility]  Agent reads Problem background / Approach /
  Reproduction target and adjudicates (no keyword prescreen).
  ├─ NON_MAT ─────► fail-fast REJECT (C01 Hard Gate); paper is NOT read.
  └─ MAT_CORE / MAT_METHOD / MAT_WRAPPER / AMBIGUOUS → continue (Wrapper is a task).
[Stage 1 Deterministic core lane]  D1–D6 plus code-defined runtime probes.
[Stage 2 Agent quality lane]  scientific justification and quality results.
[Stage 3 Score + disposition]  C01–C07 normalized + weighted total + Hard Gates +
  verdict + unified terminal fields.
  ├─ PASS           → publishable=true only when D1–D6=CLEAN
  ├─ CONDITIONAL    → repair
  ├─ REJECT         → abandon (total < 60 or a Hard Gate)
  └─ NOT_ASSESSABLE → re-audit after evidence is restored
[Stage 4 Repair (CONDITIONAL only)]  AUTO_FIX / ASSISTED_FIX / ABANDON in isolation.
[Stage 5 Re-audit + compare]  Re-run Review; emit before/after C01–C07 and delta.
```

Repair is never a second scoring authority. It runs the canonical Review CLI
exactly once at equal E1 depth after the isolated candidate pass. That one
re-audit controls the post-repair verdict, D1–D6 state, Hard-Gate result, and
target resolution.

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
| D7-quality | dynamic robustness & discrimination | `tests/test.sh`, `tests/checker.py`, Agent quality assessment | quality results remain separate and never assign D1–D6 ownership |

Each D1–D6 check emits exactly one of `PASS`, `FAIL`, `BLOCKED`, or
`NOT_ASSESSABLE`. Proven, OPEN, repairable D1–D6 findings are blocking; static
warnings and unproven reachability risks are advisory. The deterministic repair
summary is `CLEAN`, `REQUIRED`, or `NOT_APPLICABLE`, and `REQUIRED` contains
the complete source queue, never a selected subset.

Malformed, full-integration, partial, and all-wrong runtime cases are
schema/step-derived code checks. The Agent does not author their files or
interpret their values scientifically. Gold, target, unit, formula, tolerance,
threshold, and scoring-direction justification belongs only to the Agent
quality lane and requires source evidence.

## Checker execution precondition

Dynamic E1 checker cases and Repair argv command regressions run through the
disposable prebuilt `qa-checker` Docker sandbox. Build it once with
`.cursor/skills/materials-benchmark-review/scripts/sandbox/build_qa_checker.sh`.
Docker daemon reachability, the local image, and a writable uv cache are
operator preconditions; a missing precondition aborts the run with the build
hint. After preflight succeeds, dependency-install failures and checker
crashes are package findings rather than `not-assessable` runtime results.
Runtime provenance is always `sandbox`; the isolated Oracle is only a positive
mock source and generated probe cases live only in the external audit workspace.
No human- or Agent-authored result directory is accepted.

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
| C04 scoring semantics | deterministic + quality | D3, D6 | Agent quality results and A5 (part) |
| C05 answer leakage | scientific | D6 (solution boundary) | A3 |
| C06 reproducibility | scientific | D5 (resources), direct-input probe | A4 |
| C07 difficulty & auditability | deterministic + quality | quality results (discrimination/equivalence) | A2/A5 (part) |

The four Hard Gates bind to dimensions: C01 (not a materials task / NON_MAT),
C03 (scientifically invalid or unrecoverable missing definition), C04 (checker
does not evaluate the core task and cannot be repaired without redefining it),
and C06 (an indispensable direct input is permanently unavailable with no
equivalent).

An atomic repair publication is permitted only when the single equal-depth E1
re-audit reports overall `PASS`, deterministic `CLEAN`, no failed Hard Gate,
preserved package identity, allowed mutation scope, and resolution of every
target finding. Residual deterministic blockers map to a non-published
terminal state.

## Unified terminal fields

Every report and disposition carries `disposition` (PASS / CONDITIONAL / REJECT /
NOT_ASSESSABLE), `publishable` (bool), and `repair_state` (NOT_REQUIRED at
review time; REPAIRED / PARTIALLY_REPAIRED / ABANDONED / ROLLED_BACK after
repair). `publication_route` records the current publishability route
(PUBLISH_CANDIDATE / REPAIR_QUEUE / QUARANTINE / EVIDENCE_PENDING).
