# Repair policy

Work only on an isolated candidate. Preserve the source and record every change.
Each mutation must map to one current `CONFIRMED` finding and type-matched
evidence. Missing, conflicting, or ambiguous evidence means no mutation.

Allowed mutation scope is normally `instruction.md` and `tests/**`. Treat
`paper/**`, source data, metadata, and environment as read-only unless the user
explicitly broadens scope. `solution/**` is excluded even when present: do not
read, execute, hash, scan, cite, or modify it.

Do not invent Gold, targets, tolerances, thresholds, formulas, units, scientific
parameters, fields, producers, pretrained models, datasets, or scorer semantics.
Paper/public primary evidence is required for scientific changes.

Do not preserve random, perturbed, interpolated, fitted, smoke, dummy, or
placeholder values found in in-scope grading files as absolute Gold merely
because they look plausible. Keyword presence is not a defect; trace whether
the code actually defines acceptance truth without consulting `solution/`.

A paper-aligned repair may either restore source-supported absolute values or
retain a reduced/smoke system with a source-supported relational target such as
trend, ordering, sign, or qualitative regime. The latter requires documented
applicability to the reduced system and must score the relation directly rather
than invented pseudo-values. Update all affected files together; changing only
the Gold number is incomplete, and changing an absolute endpoint into a
relational endpoint requires that this remain within the authorized core task.

Paper-sourced Gold is by design. Repair it only for wrong/absent citation,
paper/package mismatch, grading/checker mismatch, misdeclared reproduction
intent, or fabricated tolerance—not merely because it comes from the paper.

Every applied change requires fail-before/pass-after regression evidence and an
equal-depth Review. Local regression success alone never authorizes publication.
Mechanical evidence before and after repair is retained as observation; only
the Agent may decide whether a candidate fact resolves the scientific finding.

Before mutation, perform an independent fresh-defect pass rather than limiting
scope to the source decision. For every intended change record its cross-file
impact across instruction, steps, resources/task configuration,
grading/Gold/checker.
Never resolve a scientific-contract mismatch merely by rewriting the prompt to
match the existing checker.

A Review decision that confirms `SCIENTIFIC_REASONING_ABSENT` with disposition
`ABANDON` terminates the lifecycle before Repair. Do not remove supplied
parameters or formulas, add process requirements, or alter the checker to turn
such a task into a different scientific task.

Only write mutations under
`/personal/qa_review/<cluster>/<theme>/<paper>/candidate`; keep the original
Harbor package unchanged. Preserve an immutable snapshot, candidate hashes or
patches, and fail-before/pass-after evidence for each change.
