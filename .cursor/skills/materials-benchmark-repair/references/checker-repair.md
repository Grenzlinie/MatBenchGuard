# Checker repair

Before changing checker logic, prove the defect with a minimal failing case and
trace the intended behavior to instruction, paper/public evidence, and grading
contract.

After repair test valid positive, missing/empty/malformed, random/constant,
duplicates, NaN/Inf, minimal exploit, quality gradient, semantic equivalence,
component isolation, and relevant task-specific attacks.

Verify every final core scientific output is read, bound to a scorer, positively weighted,
finite-returning, and included in final reward. Process artifacts remain
process-only and need not be read. Correct/high-quality final output must score
well; clearly wrong, invalid, or missing final output must not pass. A checker
need not prove that the solver followed a requested or recommended process.

Treat NaN/Inf, wrong types, missing fields, duplicate identifiers, invalid
formats, and unsafe parsing as `AUTO_FIX` checker defenses whenever intended
rejection is uniquely determined by the public contract. Test that these cases,
empty/malformed outputs, random/constants, and task-specific clearly wrong final
results receive zero or remain below the passing threshold.
Also require valid final-result fixtures to keep the same or a more reasonable
score before and after repair.

Interpret all paths using the declared Docker/container layout and mounts. A
missing host path, failed path rewrite, or helper without container-layout
support is `AUTOMATION_LIMITATION`, unless evidence proves the declaration or
in-container path itself is invalid.

Never loosen a checker just to make one candidate pass, encode hidden scientific
choices, or replace missing scientific evidence with thresholds tuned to Gold.
