# Repair Policy

## Evidence hierarchy

Use evidence in this order:

1. deterministic audit results and current file contents;
2. public benchmark instructions and declared resources;
3. official accession metadata, software documentation, and immutable releases;
4. paper Methods, figures, tables, supplements, and public code when paper-grounded;
5. documented community standards only when the task explicitly permits equivalent methods.

Never use hidden solution artifacts to infer intended behavior.

## Semantic-change rule

A repair changes task semantics when it modifies the biological question, accepted endpoint, samples, labels, Gold, scientific threshold, scoring target, or allowed method class. Apply such a change only when uniquely supported by public evidence. Otherwise abandon.

## Atomic change rule

Keep each patch small and linked to finding IDs. Record:

- path;
- before and after SHA-256;
- reason;
- finding IDs;
- tests;
- result;
- rollback status.

## No score chasing

Do not accept a repair solely because the total score rises. Confirm that the repaired benchmark better measures its declared capability and that exploit scores decrease while valid-output scores remain high.
