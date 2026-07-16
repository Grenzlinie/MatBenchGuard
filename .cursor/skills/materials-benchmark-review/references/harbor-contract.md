# Harbor review contract

The audit unit is one `paper-{id}/` directory.

## Quality roles

- `instruction.md` defines the public scientific task and answerability.
- `tests/**` defines the privileged checker, Gold, tolerances, and score.
- `solution/**` is privileged and may be copied into a disposable Oracle
  workspace only to generate one positive mock. Its values are never report
  evidence.
- `paper/**` is read only after a confirmed paper trigger.

No other package role is quality evidence. `manifest.json`, `resources.json`,
`steps.json`, `task.toml`, `environment/`, and directory labels cannot affect
the score or gates.

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

A complete model, structure, trajectory, prediction field, or other
load-bearing scientific artifact is a core output even when the instruction
labels it as process. Ignoring it or checking only file existence is
`CHECKER_CORE_TASK_UNASSESSED`.

## Checker runtime

The real checker runs in a disposable copy containing instruction and tests,
without solution or paper. Paths for `/app/outputs`, `/tests`, and
`/logs/verifier` are redirected inside that copy.

If `solution/solve.sh` exists, the complete solution role is first copied into
a separate disposable workspace. It receives `OUTPUT_DIR`; generated
contracted files may be copied to checker inputs, but file contents, stdout,
and Oracle values are not written to the report.

Oracle lifecycle evidence distinguishes attempt, setup attempt, prepared
environment, producer start, and execution. Only producer start/run sets
`solution_oracle_executed`; setup and virtualenv failures do not.

## Structural rules

Quality-role paths cannot escape the package or route through symlinks.
Input hashes cover instruction and tests only. Triggered paper hashes are
added only after the no-paper gate. Solution hashes are never published.
