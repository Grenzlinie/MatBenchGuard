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
unknown read/score states. Static process-evidence references remain candidates;
they do not prove either verification or non-verification.

Process non-verification is established only by a completed, safe in-process
open/stat trace using an independent positive fixture that contains the declared
process files. A traced access leaves semantic validation unknown; unsafe or
failed instrumentation remains unknown/not-run.
Listing or scanning the outputs directory is not per-file access and cannot
establish that a declared process artifact was read or validated.

Process evidence being absent from `output_contract` is not by itself a defect.
If it is declared as necessary anti-hacking evidence but the checker never
reads or validates it, report one grouped `PROCESS_EVIDENCE_NOT_VERIFIED`
finding. Do not turn it into repeated `INSTRUCTION_ONLY_OUTPUT` deductions.

## Checker runtime

`tests/test.sh` is Harbor's verifier entrypoint. E1 invokes that entrypoint in
a disposable copy containing instruction and tests, without solution or paper.
Paths for `/app/outputs`, `/tests`, and `/logs/verifier` are redirected inside
that copy without changing the source package's canonical Docker paths.

Every checker result records runtime provenance as `Harbor-equivalent`,
`audit-host-copy`, or `not-assessable`. An audit-host copy is not evidence that
the Harbor container is equivalent. Direct `checker.py` execution, when used
for a narrow diagnostic, is an audit harness and must never be labeled as a
Harbor-equivalent verifier run.

The Docker image is the Agent's task environment, not a declaration that every
instruction dependency is preinstalled. A missing audit-host package, a
dependency supplied by `environment/Dockerfile`, or a dependency installed by
`tests/test.sh` is not a package defect. If the audit host cannot execute the
verifier for one of those reasons, record `not-assessable`; do not emit checker
crash/alignment findings from that host limitation.

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
