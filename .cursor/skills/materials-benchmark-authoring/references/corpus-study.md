# material_v2_question empirical study

This reference records conventions observed on 2026-08-03. It is descriptive evidence, not a replacement for current Review rules.

## Corpus sizes

- `material_v2_question`: 1,878 packages across 134 cluster/theme pairs.
- `material_v2_question_reviewed_passed`: 1,029 package directories across 126 cluster/theme pairs.
- Legacy final Review decisions found: 1,860.

## Stable package conventions

All 1,878 source packages contained:

- `instruction.md`;
- `paper/paper.md` and `paper/images_manifest.json`;
- `manifest.json`, `steps.json`, `resources.json`, and `task.toml`;
- `environment/Dockerfile`;
- `tests/grading_spec.json`, `tests/checker.py`, and `tests/test.sh`.

In the passed set, the standard instruction sections occurred in about 98--100% of packages. Most workflows had one to five steps. CSV and JSON dominated public outputs.

The base image was identical in all 1,878 source packages and 1,027 of 1,029 passed package directories:

`dp-harbor-registry.cn-zhangjiakou.cr.aliyuncs.com/public/paper2arm-env:v1.0-20260708`

## Legacy `solve.sh` evidence

All 1,878 source packages contained `solution/solve.sh`. The median script length was 32 lines. Overlapping implementation patterns included 709 scripts that directly emitted literal JSON/CSV/TXT, 526 with inline Python heredocs, and 482 that invoked extra files under `/solution`. Four contained explicit placeholder/no-output language. None referenced `/app/resources`, and the local corpus copies had no executable bit set.

Use this only as migration evidence. The new profile retains the common single-script/inline-Python shape but closes the legacy ambiguity: `solution/` contains only executable `solve.sh`; the file is a deterministic `CHECKER_FULL_SCORE_FIXTURE`; helper files, runtime installs, network access, checker introspection, and claims of real scientific execution are prohibited.

## Inconsistencies not to copy

- Resource `access.method` uses many ad hoc values.
- Historical `scoring_tier` and `target_policy` strings are not normalized; new Authoring packages use canonical `quality_tier = BASELINE_CORRECT` or `RESULT_ENHANCED`.
- Bundled resources are sometimes declared without files or mappings.
- `resources_mapping` is positional; it is not keyed by `resources[].id`.
- Some instructions hard-code `/app/resources/...`; others use root-relative files.

The new authoring profile normalizes these instead of selecting the most frequent historical spelling.

## Bundled-resource evidence

The source set contained 191 structurally declared bundled records; 29 had non-null positional mappings. The passed set contained 61 bundled records; 12 had non-null positional mappings. One complete passed example stored:

- authoring file: `resources/fused_silica_refractive_index.csv`;
- historical runtime declaration: `/app/resources/fused_silica_refractive_index.csv`;
- positional mapping: `resource_type = dataset`, `resource_unique_key = meas_data`.

The authoring profile keeps the useful pieces—local `resources/` storage and stable mapping identity—but deliberately changes the public instruction to filename-only references so deployment paths can change independently.

## Legacy failure signals

Across 1,860 legacy final decisions:

- verdicts: 1,055 PASS, 714 REJECT, 91 CONDITIONAL;
- failed hard gates included 546 `CHECKER_CORE_TASK_UNASSESSED`, 142 `INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE`, and 100 `SCIENTIFIC_TARGET_INVALID`;
- open findings were concentrated in checker/Gold coverage, parameter/workflow continuity, resource readiness, tolerance/numeric robustness, and scientific scope.

Legacy audits used an older policy and may include stronger process/anti-hacking expectations than current Baseline-first Review. Use the counts only to prioritize authoring prevention: select valid targets, close assets, freeze Gold before checker generation, and choose Enhanced only for a scientifically grounded, risk-targeted, discriminating, cost-compliant result check.
