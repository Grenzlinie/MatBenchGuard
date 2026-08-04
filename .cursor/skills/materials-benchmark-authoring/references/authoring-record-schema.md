# External authoring record schema

`authoring_record.json` is the source of truth for authoring decisions. Keep it outside the candidate Harbor package.

## Top-level fields

- `schema_version`: `materials-benchmark-authoring/1.1`.
- `authoring_id`: stable local ID.
- `status`: authoring state.
- `source`: PDF path, SHA-256, UniParser metadata, and Markdown path.
- `parse_quality`: load-bearing text/equation/table/caption assessment.
- `candidate_records`: candidates, admission, evidence, Gold, resource, and checkpoint references.
- `selected_candidate_id`: one accepted candidate.
- `parameter_records`: four-class parameter ledger and uniqueness booleans.
- `condition_group_records`: complete signatures and required targets.
- `resource_records`: role, indispensability, filename/locator, availability.
- `gold_records`: policy, applicability, provenance, and hidden reference.
- `tolerance_records`: evidence and boundaries.
- `workflow_records`: producer/consumer edges.
- `output_contract`: public outputs.
- `enhancement`: weights, result checks, and affordability.
- `probe_records`: baseline and enhancement probes.
- `checker_cost_record`: real-scale resource measurement.
- `oracle_validation`: full-score-fixture purpose, no-scientific-execution attestation, Harbor Oracle reward/components, command, and external evidence.
- `package_path`: candidate path.
- `independent_review`: final Review result and artifact.
- `blockers`: unresolved blockers.

## Validation stages

### `draft`

Checks schema, source hash, candidate IDs, enum values, and cross-references. Incomplete scientific evidence may remain.

### `review-ready`

Additionally requires:

- selected candidate accepted and Q0-pass;
- parse quality pass;
- no blockers;
- all indispensable resources ready;
- all target and condition references closed;
- Gold provenance and tolerance records complete;
- public output paths under `/app/outputs`;
- Gold/result weights in range and summing to 1;
- at least one enhanced result check;
- five Baseline probes plus one enhancement probe;
- real-scale checker cost pass.
- the only `solution/` entry is executable `solve.sh`, and its `CHECKER_FULL_SCORE_FIXTURE` has passed Harbor Oracle with reward `1.0`, every component full, and retained evidence outside the candidate package.

### `publish`

Additionally requires an independent, complete `materials-core-review/3.3` JSON artifact with `verdict = PASS`, `publishable = true`, and `quality_tier = RESULT_ENHANCED`. The publish validator reads `artifact_path`, requires it to stay outside the candidate package, runs the actual Review 3.3 schema and package-aware validator, and then matches the summary fields. A copied four-field summary cannot replace the real Review artifact.

## Invariants

- Candidate, parameter, condition, resource, target, workflow, output, and result-check IDs are unique.
- Every referenced ID exists.
- Every condition group maps to at least one core target.
- Every core target maps to at least one condition group and one public result.
- Every `INDISPENSABLE_ASSET` points to a ready resource record.
- The candidate package contains `solution/solve.sh`; Review artifacts remain outside the entire candidate package.
- `oracle_validation.purpose = CHECKER_FULL_SCORE_FIXTURE` and `scientific_execution_performed = false`.
- `oracle_validation.status = PASS`, `expected_reward = actual_reward = 1.0`, `all_components_full_score = true`, and non-empty evidence are required before Review.
- Every output path is canonical under `/app/outputs`; `..`, backslashes, and directory-only paths are invalid.
- `paper_id` is one safe path component, never a path.
- `resource_records`, `resources.json`, positional mappings, and bundled files agree by resource ID, type, and filename.
- Package and Review use `quality_tier = RESULT_ENHANCED`, not the legacy lowercase `scoring_tier` alias.
- A GPU cost record uses `hardware_class = SINGLE_GPU`, names exactly one GPU, and explicitly attests `h100_equivalent_or_less = true`.
- Real-scale cost requires non-negative finite wall time, peak memory, and bytes read plus a non-empty measurement rationale; booleans are not numeric measurements.
- An authoring record may describe failure faithfully; only `review-ready` and `publish` stages demand success.
