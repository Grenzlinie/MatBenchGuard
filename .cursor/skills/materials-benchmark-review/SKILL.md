---
name: materials-benchmark-review
description: Audit one materials-science Harbor package at E1 using instruction, tests, an isolated solution Oracle positive mock, and conditionally triggered paper evidence.
---

# Materials Benchmark Review

Audit one `paper-{id}/` Harbor 题包 and publish the authoritative
`benchmark_audit/` bundle inside it.

## Quality evidence boundary
Review only:

- `instruction.md`;
- all relevant files under `tests/`;
- `solution/` only to execute its Oracle in isolation and ask whether the
  generated mock passes the real checker;
- `paper/` only when one or more paper triggers apply.

Do not inspect or score `manifest.json`, `resources.json`, `steps.json`,
`task.toml`, `environment/`, cluster names, or other metadata. They may locate
the package but cannot change a quality score, verdict, or Hard Gate.

Oracle outputs are privileged positive mocks. Never include their values in an
audit artifact and never use them as scientific correctness, paper fidelity,
or Gold-provenance evidence. Missing or broken `solution/solve.sh` is a
repairable completeness finding, not evidence that the task science is wrong.

Read [references/harbor-contract.md](references/harbor-contract.md) and
[references/no-paper-e1.md](references/no-paper-e1.md).

## Contract-role mapping
Do not treat every path under `/app/outputs` as a scored answer. Build and
publish this mapping for every workflow requirement:

```text
Instruction requirement
  → Agent work/action
  → declared core output
  → checker actually reads
  → checker actually scores
```

The mapping has three output roles:

- `scored_output` — a final submission that contributes to a rubric component;
- `process_evidence` — an intermediate artifact used to verify the workflow or
  prevent hard-coded/output-only submissions, with no independent rubric weight;
- `unclassified` — a declaration that needs human adjudication before scoring.

An instruction may legitimately list process evidence separately from final
submission files. A process artifact missing from the scoring contract is not
`INSTRUCTION_ONLY_OUTPUT` and must not reduce instruction answerability merely
because it has no score weight. If the instruction declares it as anti-hacking
evidence and the checker never reads or validates it, emit one grouped
`PROCESS_EVIDENCE_NOT_VERIFIED` finding, with all affected files as locations.
Static loader or filename evidence is only a read candidate: preserve
`UNKNOWN`/`CANDIDATE` unless a dynamic probe establishes non-verification.
The generic dynamic seam may emit `PROCESS_EVIDENCE_NOT_VERIFIED` only when an
independent positive fixture contains the process files and a safe in-process
Python open/stat trace completes without accessing them. Access proves only
that the file was touched, not that its semantics were validated. Unsafe,
external, missing-fixture, or failed tracing remains `UNKNOWN`/`NOT_RUN`.

For every `scored_output`, record whether the checker:

1. loads the file or otherwise reads its contents;
2. binds it to a runtime scoring function;
3. gives it a non-zero effective weight; and
4. uses it in the final reward rather than only checking existence or format.

Missing links are checker/Gold or robustness findings, not generic
instruction-omission findings. The report must expose the mapping even when a
link cannot be established statically. Source-pattern matches are only static
candidates; label them separately from runtime-proven reads, scorer returns,
and effective weights. Missing or unparseable checkers remain unknown/not-run
and can never imply that all scoring items are runtime-bound.
Every parsed workflow requirement receives a chain row even when it declares no
recognized output; use an unclassified output and unknown read/score states.

## Checker anti-hacking audit
The checker audit must combine static contract mapping with isolated dynamic
probes. Inspect for:

- core outputs that are never read;
- intermediate evidence that is declared but never verified;
- file-existence or schema-only checks that ignore the scientific result;
- small hard-coded targets that bypass prediction/model outputs;
- ignored model files, predictions, or load-bearing logs;
- scoring components with zero weight, no runtime binding, or no return value;
- always-pass, always-zero, exception-swallowed, division-by-zero, and
  direction-reversal behavior;
- positive valid outputs receiving a high score;
- malformed, incomplete, random, or scientifically wrong but
  format-valid outputs receiving a low score.

`largest_weight >= pass_threshold` is only a static reachability risk. It is
not proof of `SINGLE_COMPONENT_CAN_PASS`; prove that finding with a
component-isolation probe. Do not deduct points for the static risk alone.
Construct isolation cases only from source-bound contracted components,
verified checker source/runtime bindings, and an independently justified public
positive fixture. The Oracle positive mock is never an isolation fixture. If
that cannot be done safely, record
`component_isolation` as required but `NOT_RUN` with the reason.
Every reward-derived conclusion uses the shared usable-result predicate. A
finite reward with malformed breakdown or non-empty/malformed `_errors` is
unusable.

If an isolated Oracle producer runs successfully but the checker rejects its
mock, attribute the rejection to checker/Gold alignment or checker runtime
behavior. Only attribute it to solution completeness when the producer failed
to run or failed to generate the declared outputs. Docker paths such as
`/solution` and `/app/outputs` are valid Harbor paths and must not be rewritten
in the package.

Findings caused by the same contract defect are grouped into one deduction.
Multiple affected files or output names are evidence locations, not automatic
additional deductions.

## Trigger paper review
Read `paper/` only for these four triggers:

1. `SCIENTIFIC_CONFLICT` — instruction, tests, and Oracle behavior conflict;
2. `NECESSARY_INFORMATION_MISSING` — a missing definition may make the scored
   scientific quantity undefined, incomparable, or secretly checker-dependent;
3. `GOLD_PROVENANCE_UNCERTAIN` — Gold, tolerance, or scoring rationale lacks a
   credible basis;
4. `EXPLICIT_REPRODUCTION_CLAIM` — instruction claims a paper-specific system,
   condition, result, or value.

For a triggered review, read
[references/paper-grounded-audit.md](references/paper-grounded-audit.md).
Classify intent as `EXACT_REPRODUCTION`, `METHOD_REIMPLEMENTATION`, or
`SCIENTIFIC_EXTENSION`; default to `METHOD_REIMPLEMENTATION`, never EXACT.
Equivalent software, versions, and solver-selected convergence parameters are
allowed unless instruction fixes them or the checker secretly depends on them.

## Run E1
Write any taxonomy or triggered paper assessment outside the package, then run:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --paper-mode no_paper \
  --execution-level E1 \
  --agent-assessment <optional-taxonomy-assessment.json>
```

For a triggered paper assessment:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --paper-mode paper_grounded \
  --execution-level E1 \
  --agent-assessment <assessment.json>
```

An independently justified non-Oracle output may additionally be supplied with
`--known-valid-output`. It is used only for discrimination and equivalence
probes and requires an external public `fixture_manifest.json` bound to current
instruction/tests hashes; it never replaces the isolated Oracle positive mock.

Every no-paper assessment must also adjudicate all four paper triggers
individually with instruction/tests quotes. A triggered item routes the package
to paper-grounded evidence; it cannot remain a no-paper `PASS`.

Every E1 run records coverage for these probe classes:

- positive — isolated Oracle mock only;
- negative — missing, empty, malformed, random, duplicate, sparse, and
  non-finite attacks;
- discrimination — an independently justified public fixture and scientifically
  worse outputs must not score better;
- equivalence — scientifically equivalent ordering or serialization must not
  change reward, using the same independent public fixture;
- component isolation — independently sourced one-component submissions;
- process evidence — safe dynamic access tracing when supportable.

Execute checker cases through `tests/test.sh` and label runtime provenance as
`Harbor-equivalent`, `audit-host-copy`, or `not-assessable`. The audit-host
copy is not Harbor-equivalent. Missing host dependencies, dependencies supplied
by `environment/Dockerfile`, and verifier-time dependency installation are
runtime limitations, not package defects.

## Direct inputs
Read [references/materials-resource-policy.md](references/materials-resource-policy.md).
Probe only a direct input or service that instruction explicitly marks as
indispensable and without an equivalent. Do not probe resources metadata,
solver-generated structures/trajectories/models, ordinary solver parameters,
or replaceable software.

## Score and disposition
Read [references/scoring-rubric.md](references/scoring-rubric.md). The Review
CLI is the sole scoring authority; batch and calibration layers only aggregate
an identity- and source-hash-bound CLI report. Never accept manually supplied
dimension scores, total score, Hard Gates, or verdict.

The five quality dimensions and fixed weights are:

- scientific validity: 35%;
- instruction answerability: 20%;
- checker/Gold alignment: 25%;
- robustness and discrimination: 15%;
- solution completeness: 5%.

Only four Hard Gates override the score:

1. not a substantive materials-science task;
2. scientifically invalid or missing an unrecoverable necessary definition;
3. checker does not evaluate the core task and cannot be repaired without
   redefining it;
4. an indispensable direct input is permanently unavailable with no equivalent.

Each report emits points earned/max points, normalized score, deduction and
finding IDs, and exact evidence for all five dimensions. The displayed total is
the sum of earned points on a 0–100 scale, including assessable Hard-Gate
rejections. `METHOD_REIMPLEMENTATION`, `EXACT_REPRODUCTION`, and
`SCIENTIFIC_EXTENSION` are classification only and never change points.

`PASS` is at least 80 with no unresolved repairable HIGH; `CONDITIONAL` is
60–79 or has a repairable HIGH; `REJECT` is below 60 or hits a Hard Gate.
Use `NOT_ASSESSABLE` only for temporary evidence unavailability and re-audit
after the evidence is restored.

`PASS` additionally requires the fail-closed evidence contract: authoritative
materials qualification, non-empty evidence for all five dimensions, complete
no-paper trigger adjudication when applicable, honest status and provenance for
all probe classes, and Oracle-safe solution status only. Assessed
discrimination/equivalence must use an independent non-Oracle fixture; when no
such fixture exists, keep both probes unavailable, deduct the documented
non-critical robustness limitation, and continue scoring the total. No
findings never substitutes for positive evidence.

Preserve the pinned three-axis taxonomy labels and exact package evidence. The
versioned runtime source is
[references/materials-taxonomy.json](references/materials-taxonomy.json).

## Batch
Read [references/fast-e1-batch.md](references/fast-e1-batch.md). The candidate
manifest freezes identities only. Finish and freeze the complete original
review baseline before any repair begins.

## Completion

The run is complete when the fixed bundle validates, Oracle values are absent,
quality files are limited to instruction/tests plus the isolated Oracle role,
paper hashes appear only for a triggered review, every checker case records
class/reward/status/exit code, the five weights sum to one, exactly four Hard
Gates are present, and taxonomy labels remain unchanged.
