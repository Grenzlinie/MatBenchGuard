# Stages, checks, and terminal fields

## Stage flow (0 → 5)

```
[Stage 0 Materials admissibility]  Requires a validated paper Agent assessment
  in the run (`agent_assessment.json`). Missing/invalid assessment pauses as
  AGENT_ASSESSMENT_PENDING with no A0 or formal audit. Agent reads Problem
  background / Approach / Reproduction target and adjudicates; deterministic
  code does not infer it.
  ├─ NON_MAT ─────► fail-fast REJECT (C01 Hard Gate); paper is NOT read.
  └─ MAT_CORE / MAT_METHOD / MAT_WRAPPER / AMBIGUOUS → continue (Wrapper is a task).
[Stage 1 Deterministic core lane]  machine D1–D6 contract plus code-defined
  runtime probes.
  ├─ CLEAN ───────► continue
  ├─ REQUIRED ────► score, then CONDITIONAL / REPAIR_QUEUE when eligible
  └─ NOT_APPLICABLE ─► persist contract request and return
      AGENT_CONTRACT_PENDING until an external contract assessment is supplied.
[Stage 1b Contract-only Agent overlay]  eligible unavailable checks may receive
  PASS; D6 alone may receive REPAIR_REQUIRED. NOT_PROVEN remains pending.
[Stage 2 Agent quality lane]  scientific justification and quality results.
  Repairable Agent findings become first-class OPEN queue entries
  (`lane: agent_quality`, `repair_lane` / `repair_scope`); never assign a
  fabricated D1–D6 check. Normalized `repair_findings` are CLI-validated.
[Stage 3 Score + disposition]  C01–C07 normalized + weighted total + Hard Gates +
  verdict + unified terminal fields.
  ├─ PASS           → publishable=true only when effective D1–D6=CLEAN and no
  │                   OPEN repairable Agent-quality finding remains
  ├─ CONDITIONAL    → repair (including D CLEAN + OPEN repairable Agent finding
  │                   → REPAIR_QUEUE)
  ├─ REJECT         → abandon (total < 60 or a Hard Gate)
  └─ NOT_ASSESSABLE → re-audit after evidence is restored
[Stage 4 Repair (CONDITIONAL only)]  AUTO_FIX / ASSISTED_FIX / ABANDON in isolation.
  Later Repair tickets bind an Agent repair assessment across the complete
  dual-lane queue. Direct deterministic publication is limited to unique D
  wiring; Agent checker-fairness / science / direct-input / paper-grounded
  instruction repairs require equal-depth re-audit.
[Stage 5 Re-audit + compare]  Re-run Review with the inherited paper assessment;
  emit before/after C01–C07 and delta. Absence/invalid/stale inheritance pauses
  as AGENT_ASSESSMENT_PENDING and does not consume a semantic attempt.
```

Repair is never a second scoring authority. It runs the canonical Review CLI
at equal dual-lane depth after the isolated candidate pass. A normal run
finalizes in one invocation. If Review first returns
`AGENT_CONTRACT_PENDING`, the prepared re-audit is resumed with the external
contract assessment without rerunning its persisted probes; that completed
re-audit is still the sole post-repair authority for verdict, D1–D6 state,
Hard-Gate result, and target resolution. Re-audit never silently falls back to
deterministic-only Review when the paper assessment is missing.

## Classification reform (Agent-adjudicated)

Classification is authoritative from the Agent reading the instruction's
structured fields `## Problem background`, `## Approach`, and
`## Reproduction target`; if fields are missing, the Agent reads the whole text
and records `AMBIGUOUS`. No lexical fallback is used. The Agent emits a
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
warnings and unproven reachability risks are advisory. The machine deterministic
repair summary is `CLEAN`, `REQUIRED`, or `NOT_APPLICABLE`, and `REQUIRED`
contains the complete source queue, never a selected subset.

The complete Review OPEN repair queue also includes repairable Agent-quality
findings as first-class entries (`lane: agent_quality`). They carry
`repair_lane` / `repair_scope` rather than a fabricated `deterministic_check`.
Allowed scopes include `DETERMINISTIC_WIRING`, `CHECKER_ROBUSTNESS`,
`INSTRUCTION_CONTRACT`, `SCORING_SEMANTICS`, `DIRECT_INPUT_REFERENCE`, and
`SCIENCE_SEMANTICS`. Machine D1–D6 statuses, evidence, and source bindings stay
authoritative and are not altered by Agent-quality queue entries. When D1–D6 is
`CLEAN` but an OPEN repairable Agent finding remains, disposition is still
`CONDITIONAL` / `REPAIR_QUEUE`.

Malformed, full-integration, partial, and all-wrong runtime cases are
schema/step-derived code checks. The Agent does not author their files or
interpret their values scientifically. Gold, target, unit, formula, tolerance,
threshold, and scoring-direction justification belongs only to the Agent
quality lane and requires source evidence.

### Machine contract, contract-only Agent assessment, and effective contract

The machine contract is authoritative and is persisted in
`deterministic_core/report.json` and the report's `deterministic_contract`.
It contains the D1–D6 statuses, machine findings, blocking queue, registry
version, and `contract_digest`. An external `agent_contract_assessment` never
rewrites that artifact.

The contract-only Agent assessment uses schema
`materials-agent-contract-assessment/1.1`, lane `deterministic_core`, and
machine schema/registry/digest bindings. It contains D1 through D6 in order;
each check is `PASS` or `NOT_PROVEN` with a rationale; `REPAIR_REQUIRED` is
legal only for an eligible unavailable D6. Its provenance is
`EXTERNAL_AGENT_ASSESSMENT`. Accepted evidence is limited to:

- `instruction.md` (`source_kind=INSTRUCTION`);
- `tests/**/grading_spec` with an optional extension
  (`source_kind=GRADING_SPEC`); and
- `tests/checker.py` only for D6 scoring-chain facts
  (`source_kind=CHECKER_SOURCE`); and
- deterministic probe artifacts under `deterministic_core/` or
  `deterministic_probe_artifacts/` (`source_kind=DETERMINISTIC_PROBE_ARTIFACT`).

Evidence claim scope is only `CONTRACT_WIRING` or
`DETERMINISTIC_CONTRACT`. The assessment must not use `paper/`, `solution/`,
Oracle output, metadata, or science-quality evidence, and
must not adjudicate Gold, targets, tolerances, formulas, units, thresholds, or
scoring direction. `quality_results` and `agent_quality` findings are never
merged into this lane.

`NOT_APPLICABLE` is a deterministic repair-summary state, not an Agent check
status. The Agent may directly overlay only a machine check whose status is
`BLOCKED` or `NOT_ASSESSABLE`, with no proven finding, blocking finding,
dependency failure, missing input, Hard Gate, or usable runtime contradiction.
An Agent `PASS` can make that eligible unavailable check effectively `PASS`.
For D6, conclusive evidence items carry exactly one canonical `claim`:
`content_read`, `scorer_binding`, `positive_effective_weight`, `finite_return`,
or `final_reward`, plus an exact quote/excerpt and sha256 binding. PASS covers
all five PROVEN states; REPAIR_REQUIRED covers every FAILED state.
`REPAIR_REQUIRED` preserves machine UNKNOWN/NOT_ASSESSABLE, adds a stable
source-bound Agent repair finding, and makes the effective repair state
`REQUIRED`; it never fabricates machine FAIL. Its default scope is
`SCORING_SEMANTICS`, lane `agent_quality`, and publication requires re-audit;
an Agent claim never receives `UNIQUE_SCORING_WIRING`.
Machine `FAIL`, any proven machine fact, runtime contradiction, Hard Gate, and
quality finding cannot be overlaid. `NOT_PROVEN` leaves the check unavailable.
Machine findings and blockers remain preserved in the effective artifact.

The additive effective artifact has schema
`materials-effective-deterministic-contract/1.0` and is persisted as
`effective_deterministic_contract` in the report and as `effective_contract` in
`deterministic_core/report.json`. It records machine and effective statuses,
the assessment digest, eligibility and applied-check lists, and an effective
repair summary. It may change only an eligible unavailable check from
`BLOCKED`/`NOT_ASSESSABLE` to `PASS`; it cannot suppress machine findings or
change a machine `FAIL`. `NOT_PROVEN` remains `NOT_ASSESSABLE` /
`EVIDENCE_PENDING` and keeps the same prepared run resumable.

Review persists `agent_contract/request.json` only when the machine summary is
`NOT_APPLICABLE` and the assessment is not yet supplied. The request has schema
`materials-agent-contract-request/1.1`, status `AGENT_CONTRACT_PENDING`, and
the run-local A0 ContentRoot. Static/probe hashes remain diagnostic provenance;
Review implementation byte hashes are not freshness gates. A pending result is
`NOT_ASSESSABLE`, not publishable, includes `request_path`, and resumes when
the same Review Agent writes `agent_contract/assessment.json` in the run.

## Checker execution precondition

Dynamic dual-lane checker cases and Repair argv command regressions run through the
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

The Agent lane always reads `paper/` for A2/A4/A5; A1/A3 are package-first and
may extend to the paper. The only path that skips the paper is
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

An atomic repair publication is permitted only when the single equal-depth
dual-lane re-audit reports overall `PASS`, effective deterministic `CLEAN`, no failed Hard Gate,
preserved package identity, allowed mutation scope, and resolution of every
target finding. Residual deterministic blockers map to a non-published
terminal state.

Repair retains a complete external re-audit/history bundle for non-PASS
outcomes, including partial, abandoned, and rolled-back attempts. The retained
candidate/snapshot, re-audit report, unresolved findings, regression results,
comparison, evidence, and history metadata preserve severe residuals as stable
findings; they are not discarded or replaced by a score-only summary.

## Score versus deterministic gate

`summary.total_score` is the authoritative weighted C01–C07 total on a 0–100
scale. It is not a verdict and does not by itself make a package publishable.
The current artifacts do not emit `quality_score` or `pre_gate_score`; do not
invent or consume those names.

The finalizer first computes the C01–C07 score and then applies Hard Gates,
evidence availability, and the deterministic contract gate. The report's
`summary.final_verdict` (also the canonical top-level `review_verdict`) is the
final result. `summary.machine_deterministic_status` is the machine summary;
`summary.effective_deterministic_status` and `summary.deterministic_status`
identify the contract used by the final gate. The publication route is separate:
`summary.publication_route`, top-level `publishability`, and
`disposition.json.route` contain `PUBLISH_CANDIDATE`, `REPAIR_QUEUE`,
`QUARANTINE`, or `EVIDENCE_PENDING`.

The effective deterministic state can turn an otherwise passing score into
`CONDITIONAL` when it is `REQUIRED`, or into `NOT_ASSESSABLE` when it is not
complete. Only a valid `CLEAN` state permits a scored `PASS` to remain PASS,
and only when no OPEN repairable Agent-quality finding remains in
`repair_findings` / `repair_queue`.

## Unified terminal fields

Every report and disposition carries `disposition` (PASS / CONDITIONAL / REJECT /
NOT_ASSESSABLE), `publishable` (bool), and `repair_state` (NOT_REQUIRED at
review time; REPAIRED / PARTIALLY_REPAIRED / ABANDONED / ROLLED_BACK after
repair). `publication_route` records the current publishability route
(PUBLISH_CANDIDATE / REPAIR_QUEUE / QUARANTINE / EVIDENCE_PENDING).

The top-level canonical fields are `review_verdict`, `publishability`,
`repair_decision`, and `repair_status`. `summary.disposition` is the verdict;
it is not the publication route. A Review preparation pause is returned as
`AGENT_CONTRACT_PENDING` with `review_verdict=NOT_ASSESSABLE`,
`publishability=EVIDENCE_PENDING`, and `publishable=false`; it is not a final
audit bundle.

There is no E1–E4 evidence-tier routing and no no-paper route. The dual-lane
path is mandatory; only an authoritative Stage 0 `NON_MAT` classification
skips `paper/`.
