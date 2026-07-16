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

## Checker runtime

The real checker runs in a disposable copy containing instruction and tests,
without solution or paper. Paths for `/app/outputs`, `/tests`, and
`/logs/verifier` are redirected inside that copy.

If `solution/solve.sh` exists, the complete solution role is first copied into
a separate disposable workspace. It receives `OUTPUT_DIR`; generated
contracted files may be copied to checker inputs, but file contents, stdout,
and Oracle values are not written to the report.

## Structural rules

Quality-role paths cannot escape the package or route through symlinks.
Input hashes cover instruction and tests only. Triggered paper hashes are
added only after the no-paper gate. Solution hashes are never published.
