# Harbor 题包 contract

The 审计单元 is one `paper-{id}` Harbor 题包 directory. Cluster and theme
directories preserve identity but are not audit roots.

## Required roles

- `instruction.md` — public task and output contract.
- `steps.json` — structured workflow and load-bearing evidence declarations.
- `manifest.json` — identity and difficulty metadata.
- `resources.json` — declared tools, data, packages, and artifacts.
- `task.toml` — Harbor runtime and timeout configuration.
- `environment/Dockerfile` — declared container environment.
- `tests/grading_spec.json` — privileged scoring contract.
- `tests/checker.py` — privileged verifier implementation.
- `tests/test.sh` — privileged verifier entry point.

The baseline runner accepts harmless schema variation such as grading
`steps` versus `checks`, but reports missing or unparseable required roles.

## Runtime contract

The checker reads submissions from `/app/outputs`, reads its grading
specification from `/tests/grading_spec.json`, and writes:

- `/logs/verifier/reward.txt`
- `/logs/verifier/breakdown.json`

E1 copies only public and privileged review files into a solution-free
temporary runtime, patches these paths there, and executes the real checker. It
does not execute the scientific workflow.

## Evidence boundary

Auditor and Repairer may inspect `tests/`. They must not inspect or execute
anything under `solution/`.

Input hashing, root discovery, static scanning, checker probes, and reporting
must prune `solution/` before traversal. A report field claiming that solution
was not inspected is supporting metadata, not a substitute for this structural
rule.
