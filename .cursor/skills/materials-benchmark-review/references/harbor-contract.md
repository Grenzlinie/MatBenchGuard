# Harbor review contract

The audit unit is one `paper-{id}/` directory.

## Quality roles

- `instruction.md` defines the public scientific task and answerability.
- `tests/**` defines the privileged checker, Gold, tolerances, and score.
- `solution/**` is privileged and may be copied into a disposable Oracle
  workspace only to generate one positive mock. Its values are never report
  evidence.
- `paper/**` is always read by the Agent lane, except when an authoritative
  `NON_MAT` classification has already ended the review.

No other package role is quality evidence. `manifest.json`, `resources.json`,
`steps.json`, `task.toml`, `environment/`, and directory labels cannot affect
the score or gates.

## Deterministic contract artifacts

The machine D1–D6 contract is authoritative for deterministic checks. Review
persists it under `deterministic_contract` and in
`deterministic_core/report.json`, including the machine statuses, findings,
repair summary, registry version, and `contract_digest`.

When the machine repair summary is `NOT_APPLICABLE`, Review may persist
`agent_contract/request.json` with schema
`materials-agent-contract-request/1.0` and status
`AGENT_CONTRACT_PENDING`. The request binds the package, Review implementation,
static/probe artifacts, and machine contract. A supplied assessment uses schema
`materials-agent-contract-assessment/1.0`, lane `deterministic_core`, D1–D6 in
order, and per-check status `PASS` or `NOT_PROVEN`. It must bind the machine
schema, registry, and digest.

This is a contract-only Agent seam, separate from the paper-grounded
`agent_quality` lane. Its evidence may come only from `instruction.md`,
`tests/**/grading_spec` (with an optional extension), or deterministic probe
artifacts under `deterministic_core/` or
`deterministic_probe_artifacts/`. Its claim scope is `CONTRACT_WIRING` or
`DETERMINISTIC_CONTRACT`. It must not use `paper/`, `solution/`, Oracle output,
metadata, `tests/checker.py`, or science-quality evidence, and must not
adjudicate Gold, targets, tolerances, formulas, units, thresholds, or scoring
direction.

The Agent can overlay only an unavailable machine check (`BLOCKED` or
`NOT_ASSESSABLE`) that has no proven or blocking finding, dependency failure,
missing input, Hard Gate, or usable runtime contradiction. It cannot overlay a
machine `FAIL`, machine facts, runtime contradictions, Hard Gates, or quality
findings. `NOT_PROVEN` leaves the check unavailable. The additive effective
contract uses schema `materials-effective-deterministic-contract/1.0`, preserves
machine findings and blockers, and can change only an eligible unavailable check
to effective `PASS`.

## Output roles inside instruction.md

An instruction may deliberately name intermediate process artifacts in addition
to final submission files. Reviewers must preserve this distinction:

- `scored_output`: final output read by the checker and contributing to a
  weighted grading component;
- `process_evidence`: intermediate output used to verify the declared workflow
  or prevent hard-coded/output-only submissions, with no independent score
  weight;
- `unclassified`: output whose role is not explicit and requires adjudication.

For each role, record the complete mapping:

`instruction requirement → Agent work → core output → checker read → checker score`.

Static filename, loader, binding, and return-path matches are conservative
candidates, not runtime proof. Reports must preserve unknown/not-run states for
missing or unparseable checkers and distinguish declared weights from
runtime-proven effective weights.

The chain covers every parsed workflow requirement. A requirement with no
recognized output still appears with `unclassified` output role and explicit
unknown read/score states. Process artifacts remain contract-map-only: their
absence from `output_contract`, lack of checker reads, or lack of validation
cannot affect score, gate, route, or verdict. Do not run an anti-hacking trace
or emit `PROCESS_EVIDENCE_NOT_VERIFIED`.

Process evidence is not a dynamic fixture or checker target. Never copy it from
a known-valid fixture, transform it for discrimination/equivalence, or create a
read-trace checker case. Its dynamic probe class is always `NOT_APPLICABLE`.
Process evidence being absent from `output_contract` is not itself a defect.

## Checker runtime

`tests/test.sh` is Harbor's verifier entrypoint. Dual-lane review invokes that entrypoint in
a disposable copy containing instruction and tests, without solution or paper.
Paths for `/app/outputs`, `/tests`, and `/logs/verifier` are mounted at their
canonical Docker paths without changing the source package.

Every checker result records runtime provenance as `sandbox`. Review invokes
`tests/test.sh` from the prebuilt `qa-checker` image in a disposable container.
The image contains the common scientific stack; long-tail dependencies are
supplied through the sandbox's cached `uv run --with` fallback. The sandbox is
not a claim that the full Harbor image is equivalent.

Docker daemon readiness, the local `qa-checker` image, and a writable uv cache
are operator preconditions. A missing precondition aborts Review or Repair with
the one-time image-build command. Once the sandbox is ready, a dependency
installation failure or checker crash is package evidence and must not be
reclassified as `not-assessable`. Direct `checker.py` execution, when used for
a narrow diagnostic, remains an audit harness and is not a separate runtime
provenance label.
Process artifacts are contract-map-only and are not a top-level probe class.
Complete/full models, structures, trajectories, prediction fields, and meshes
remain core even when mislabeled process; record the contradiction as
`UNCLASSIFIED` while retaining core checker analysis. Only non-load-bearing
logs/intermediates are process-only. Ignoring a core output or checking only
file existence is `CHECKER_CORE_TASK_UNASSESSED`.

If `solution/solve.sh` exists, the complete solution role is first copied into
a separate disposable workspace. It receives `OUTPUT_DIR`; generated
contracted files may be copied to checker inputs. The Oracle positive case
persists only sanitized status, runtime provenance, and non-value diagnostics:
raw reward/breakdown, stdout/stderr, file contents, and Oracle values never
enter `checker_tests.json` or the final report.

Review accepts no independent known-valid fixture or external result directory.
Malformed, partial, full, and all-wrong cases are generated from the declared
schema and grading steps and stored only in the external audit workspace.

Oracle lifecycle evidence distinguishes attempt, setup attempt, prepared
environment, producer start, and execution. Only producer start/run sets
`solution_oracle_executed`; setup and virtualenv failures do not.

## Structural rules

Quality-role paths cannot escape the package or route through symlinks.
Input hashes cover instruction and tests only. Paper hashes are included on
the dual-lane path unless an established `NON_MAT` skip applies. Solution
hashes are never published.
