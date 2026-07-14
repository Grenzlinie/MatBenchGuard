# Paper-grounded audit

Complete all no-paper gates first.

## Task relationship to the paper

Classify:

- `EXACT_REPRODUCTION`: historical inputs, methods, versions, and curation must be fixed.
- `METHOD_REIMPLEMENTATION`: equivalent tools are allowed, but equivalence and tolerance must be defined.
- `SCIENTIFIC_EXTENSION`: the task asks a new question; exact paper numbers cannot be the sole gold.

## Evidence to inspect

Read the complete methods and relevant results, figures, tables, supplements, code, model files, initialization files, and data records. For PDF-derived values, inspect the rendered pages and figure axes visually.

## Fidelity checks

Verify:

- method order, preprocessing, software, solver, parameters, thresholds, statistics, multiple testing, training, and evaluation;
- accession, species, strain, tissue, cell, time point, treatment, control, sample count, exclusions, build, annotation, and split;
- manual curation, visual inspection, expert selection, unpublished settings, private databases, GUI steps, and supplementary models;
- current versus historical database or software drift;
- whether the requested result can actually be derived from disclosed materials.

## Gold provenance chain

For every gold value or artifact record:

```text
gold
→ local reference file
→ generating method or script
→ paper figure, table, supplement, or public data
→ sample, unit, parameter, and version
```

Flag transcription errors, undisclosed cleaning, figure-digitization uncertainty, mixed versions, and gold that cannot be produced by the public instruction.

Do not infer paper fidelity from community convention. Use only paper evidence or an explicit benchmark deviation.
