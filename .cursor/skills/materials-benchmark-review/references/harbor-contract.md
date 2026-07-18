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

Process evidence is not a dynamic fixture or checker target. Never copy it from
a known-valid fixture, transform it for discrimination/equivalence, or create a
read-trace checker case. Its dynamic probe class is always `NOT_APPLICABLE`.
Process evidence being absent from `output_contract` is not itself a defect.

## Checker runtime

`tests/test.sh` is Harbor's verifier entrypoint. E1 invokes that entrypoint in
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

An independent known-valid fixture must be outside every package/audit role and
carry `fixture_manifest.json`. The manifest explicitly marks it public,
non-Oracle, and independent; binds immutable fixture hashes to the current
instruction/tests hashes; and is itself hashed into probe provenance.

Oracle lifecycle evidence distinguishes attempt, setup attempt, prepared
environment, producer start, and execution. Only producer start/run sets
`solution_oracle_executed`; setup and virtualenv failures do not.

## Structural rules

Quality-role paths cannot escape the package or route through symlinks.
Input hashes cover instruction and tests only. Triggered paper hashes are
added only after the no-paper gate. Solution hashes are never published.
