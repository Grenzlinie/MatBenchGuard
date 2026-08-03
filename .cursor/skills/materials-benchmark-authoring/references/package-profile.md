# Canonical Paper2Arm package profile

## Package tree

```text
candidate/
├── instruction.md
├── paper/
│   ├── paper.md
│   └── images_manifest.json
├── manifest.json
├── steps.json
├── resources.json
├── resources/                  # only when author-provided files are needed
├── task.toml
├── environment/Dockerfile
└── tests/
    ├── grading_spec.json
    ├── checker.py
    └── test.sh
```

Any `solution` path component anywhere under the candidate is prohibited. Authoring records, probes, source PDF, and Review outputs live beside `candidate/`, not inside it.

## Instruction section order

Use these stable sections:

1. title;
2. `Problem background`;
3. `Approach`;
4. `Reproduction target`;
5. `Assets`;
6. `Workflow steps`;
7. `Output files`;
8. `Output contract`;
9. optional unscored `Self-check before finishing`;
10. `How you are scored`.

The corpus study found this structure in about 98--100% of passed v2 packages. Treat it as a compatibility convention, while Review correctness gates remain authoritative.

## Environment defaults

Use:

```dockerfile
FROM dp-harbor-registry.cn-zhangjiakou.cr.aliyuncs.com/public/paper2arm-env:v1.0-20260708
WORKDIR /app
```

Use the same image in `task.toml`. Default values in the packaged template are:

- schema version `1.3` for the current Paper2Arm corpus profile;
- agent timeout `14400` seconds;
- verifier timeout `11400` seconds;
- `allow_internet = true`;
- build timeout `1800` seconds.

Keep these defaults unless the external authoring record gives a concrete compute/resource justification. Run current Harbor `harbor check` for compatibility because Harbor itself evolves beyond the corpus profile.

## Bundled resources

Historical v2 packages use inconsistent conventions. The authoring profile is stricter.

For each file:

```json
{
  "id": "stable_resource_id",
  "name": "Human-readable scientific identity",
  "type": "dataset",
  "access": {
    "method": "bundled",
    "filename": "input.csv",
    "notes": "Scientific role, schema, units, and provenance."
  }
}
```

At the same array index in `resources_mapping`:

```json
{
  "resource_type": "dataset",
  "resource_unique_key": "stable_resource_key"
}
```

Rules:

- Put the file at `candidate/resources/input.csv` during authoring.
- Mention only `input.csv` in `instruction.md`.
- Do not mention `/app/resources/input.csv`, `resources/input.csv`, Trisol IDs, Playground dataset IDs, mount paths, or pre-signed URLs in the instruction.
- Do not make Dockerfile resource copies part of authoring. Deployment owns materialization.
- Preserve positional alignment between `resources` and `resources_mapping`.
- Keep deployment IDs outside the public scientific contract; add them later to the deployment mapping without renaming the resource.

This separates scientific identity from authoring storage and runtime deployment.

## Derived file synchronization

`instruction.md` is authoritative for the public contract. Generate in this order:

```text
instruction.md
 -> steps.json
 -> manifest.json / resources.json / task.toml
 -> tests/grading_spec.json
 -> tests/checker.py
 -> tests/test.sh
```

Derived files may mirror but never add a scientific requirement.

Use `quality_tier = "RESULT_ENHANCED"` in `tests/grading_spec.json`. The legacy lowercase `scoring_tier` spelling is rejected so package-aware Review validation cannot silently skip tier consistency.

When `--authoring-record` is supplied, package validation closes the resource loop: every package resource must have a matching `resource_records` entry, and every ready or indispensable record must exist in `resources.json`; IDs, package types, mapping `resource_type`, bundled filenames, positional mappings, and actual files must agree.
