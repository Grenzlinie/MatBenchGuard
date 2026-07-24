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

## ABANDON

Use only when the task cannot be restored without guessing, redefining the
endpoint, fabricating unavailable scientific data/model/Gold/target/tolerance,
or when the final core scientific result itself cannot be fairly scored. Parser
defenses, NaN/Inf rejection, type/field/format checks, duplicate handling, and
container-helper limitations are never sufficient reasons by themselves.
