# Task answerability, split integrity, and failure attribution

## Answerability

Confirm that the public task fixes every choice needed for a valid result or explicitly permits alternatives. Distinguish:

- `REQUIRED`
- `RECOMMENDED`
- `ALLOWED`
- `FORBIDDEN`

Check whether the task specifies inputs, biological conditions, reference versions, outputs, success criteria, networking, installation, external APIs, equivalent methods, randomness, and acceptable variation.

## Biological split integrity

Generic duplicate detection is insufficient. Audit task-specific relatedness:

- proteins: sequence identity, family, domain, and structural similarity;
- single-cell: donor, patient, sample, batch, and cell-line leakage;
- genomics: sample, study, cohort, individual, and locus leakage;
- medical imaging: patient-level separation;
- drug discovery: scaffold and target-family separation;
- microbiome: cohort, site, and study separation;
- phylogeny: clade and taxonomic dependence.

A split may be invalid even when files are not byte-identical.

## Failure attribution

Where possible, require distinct statuses:

- `SUCCESS`
- `DATA_UNAVAILABLE`
- `ENVIRONMENT_FAILURE`
- `EXECUTION_FAILURE`
- `INVALID_OUTPUT`
- `SCIENTIFIC_MISMATCH`
- `CHECKER_ERROR`
- `RESOURCE_EXCEEDED`

Do not interpret a transient data outage or checker crash as lack of scientific ability.

## Difficulty profile

Report separate difficulty axes instead of one vague label:

- biological reasoning;
- data engineering;
- software environment;
- compute;
- debugging;
- interpretation;
- openness or ambiguity.
