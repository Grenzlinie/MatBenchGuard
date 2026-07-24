# Repair policy

Work only on an isolated candidate. Preserve the source and record every change.
Each mutation must map to one current `CONFIRMED` finding and type-matched
evidence. Missing, conflicting, or ambiguous evidence means no mutation.

Allowed mutation scope is normally `instruction.md`, `tests/**`, and
`solution/**`. Treat `paper/**`, source data, metadata, and environment as
read-only unless the user explicitly broadens scope.

Do not invent Gold, targets, tolerances, thresholds, formulas, units, scientific
parameters, fields, producers, pretrained models, datasets, or scorer semantics.
Paper/public primary evidence is required for scientific changes.

Paper-sourced Gold is by design. Repair it only for wrong/absent citation,
paper/package mismatch, grading/checker mismatch, misdeclared reproduction
intent, or fabricated tolerance—not merely because it comes from the paper.

Every applied change requires fail-before/pass-after regression evidence and an
equal-depth Review. Local regression success alone never authorizes publication.
Mechanical evidence before and after repair is retained as observation; only
the Agent may decide whether a candidate fact resolves the scientific finding.

A Review decision that confirms `SCIENTIFIC_REASONING_ABSENT` with disposition
`ABANDON` terminates the lifecycle before Repair. Do not remove supplied
parameters or formulas, add process requirements, or alter the checker to turn
such a task into a different scientific task.

Only write mutations under
`/personal/qa_review/<cluster>/<theme>/<paper>/candidate`; keep the original
Harbor package unchanged. Preserve an immutable snapshot, candidate hashes or
patches, and fail-before/pass-after evidence for each change.
