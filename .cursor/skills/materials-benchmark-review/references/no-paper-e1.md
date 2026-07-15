# No-paper E1 interpretation

This slice asks whether a Harbor 题包 independently defines a coherent,
machine-checkable materials task. It does not compare the task with its paper.

## Evidence produced

- Harbor 题包 role parse status.
- Lexical materials relevance evidence for object, data, operation, and
  endpoint axes.
- Cross-file sets for instruction, workflow, output contract, and grading
  references.
- Grading weight and pass-threshold checks.
- Real checker rewards for missing, empty, random, minimal-shaped, duplicate,
  and non-finite submissions.
- An optional independently justified known-valid public submission.

## Initial verdict

- `REJECT` when a FATAL static or dynamic finding exists.
- `CONDITIONAL` when no FATAL exists but a HIGH or MEDIUM finding remains.
- `PASS` when only LOW findings or no findings remain.
- `NOT_ASSESSABLE` when the checker cannot produce usable E1 evidence.

This is an initial no-paper policy. Later slices replace the coarse score with
the complete weighted material audit dimensions and Hard gates.

## Claim boundaries

- E1 proves checker behavior only for the executed probes.
- E1 does not prove resource reachability or scientific workflow execution.
- `no_paper` does not establish fidelity to the source paper or Gold
  provenance.
- A lexical materials prescreen supplies evidence for Agent adjudication; it is
  not an authoritative scientific classifier.
- A generated schema-shaped submission is not a known-valid scientific result.
  Only a separately justified public fixture may exercise the known-valid case.
