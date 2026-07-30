# Abandonment rules

Abandon only when public contracts and evidence cannot uniquely determine a
repair, or the final core scientific result cannot be fairly scored. Qualifying
cases are:

- non-materials task;
- `SCIENTIFIC_REASONING_ABSENT` confirmed during Review (already `REJECT` with
  disposition `ABANDON`; do not route it into Repair);
- scientifically invalid or unanswerable target;
- missing target-defining parameter that cannot be sourced;
- `ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE`: the paper-based simulation
  requires an execution/target/scoring parameter absent from all allowed
  sources and not uniquely derivable;
- indispensable data or pretrained model permanently unavailable and no valid
  equivalent is allowed;
- Gold/tolerance cannot be verified or contradicts the paper;
- checker cannot assess the core task without redefining it;
- multiple valid answers cannot be scored fairly;
- repair requires invented science, data, model, target, or endpoint;
- equal-depth re-audit retains a Hard Gate or unrecoverable FATAL.

Do not abandon for a transient network failure, replaceable dependency, helper
schema limitation, dismissed false positive, or recoverable formatting defect.
Specifically, unread methods/traces/training logs/intermediates, host/container
path mismatch, failed local path rewriting, NaN/Inf, wrong types, missing
fields, duplicate identifiers, invalid formats, and unsafe parsing are not
independent abandonment grounds. Re-adjudicate prior `ABANDONED` results and
remove findings based only on those reasons.
