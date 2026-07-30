# Repair categories

## AUTO_FIX

Use only when intended behavior is unique and already source-bound:

- syntax/parse repair without semantic choice;
- broken path or declaration synchronization;
- existing scorer registration, binding, return, weight, or final-reward wiring;
- safe parser/path handling;
- finite-number rejection and field/type/format validation;
- missing-field, duplicate-identifier, and malformed-output rejection;
- standard entrypoint around an existing producer;
- ratio-preserving normalization of already-declared finite positive weights.

AUTO_FIX cannot choose science, Gold, tolerance, threshold, unit, field, model,
dataset, or target.

## ASSISTED_FIX

Use for semantic changes supported by exact paper/public evidence. Record source,
quote, identity/hash, applicability, derivation, and affected paths. Examples
include correcting paper-inconsistent units, fixed parameters, data identity,
Gold transcription, or evidenced tolerances.

Simulation parameter closure is `ASSISTED_FIX` only when every added value or
rule is paper-explicit, uniquely paper-derived, already package-defined, or a
proved representation-equivalent transform. Synchronize the full dependency
chain; do not patch one downstream step or Cartesian axis in isolation.

This category also covers `METHOD_REFERENCE_MISMATCH` and
`UNSUPPORTED_SYNTHETIC_GOLD` through either of these evidence-backed repairs:

1. restore a paper-consistent absolute-value task when the source uniquely
   determines the system, method, conditions, result, and tolerance; or
2. retain a reduced/smoke system and score a paper/authoritative-source-backed
   trend, ordering, sign, or qualitative relationship when that was already the
   core scientific endpoint and its transferability is justified.

Synchronize instruction, steps, resources/task configuration, Gold/relations,
grading, checker, and test entrypoint. Never replace synthetic Gold with paper
numbers while retaining a materially different system, and never silently
redefine an absolute-value endpoint as a trend task.

## ABANDON

Use only when the task cannot be restored without guessing, redefining the
endpoint, fabricating unavailable scientific data/model/Gold/target/tolerance,
or when the final core scientific result itself cannot be fairly scored. Parser
defenses, NaN/Inf rejection, type/field/format checks, duplicate handling, and
container-helper limitations are never sufficient reasons by themselves.

Always `ABANDON` `ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE`: a required
paper-reproduction parameter is missing from the paper, supplement, and
declared authoritative sources and cannot be uniquely derived. Repair must not
invent it.
