---
name: materials-benchmark-authoring
description: Create a paper-grounded enhanced materials-science Harbor task from a local or public PDF. Use when an Agent must parse a paper with UniParser, select a non-trivial computational-science question, preserve paper Gold and parameter provenance, close bundled-resource dependencies, generate the Paper2Arm package files and lightweight checker, and drive an independent materials-benchmark-review to PASS + RESULT_ENHANCED without using solution/.
---

# Materials Benchmark Authoring

Author one review-ready task from a paper. Treat this as evidence-backed compilation, not prompt improvisation.

## Non-negotiable outcome

Target `PASS + RESULT_ENHANCED` from an independent `materials-benchmark-review`.

- Keep the paper Gold center.
- Require a non-trivial computational-science task.
- Require at least one affordable result-layer checkpoint before selecting a candidate.
- Keep checker weights at Gold 60--80% and result checks 20--40%.
- Keep all solver outputs under `/app/outputs`.
- Never create, read, scan, run, hash, or cite `solution/`.
- Keep authoring records and evidence outside the Harbor candidate package.

If no candidate satisfies all gates, return `NO_ENHANCED_CANDIDATE`; do not emit a weak package merely to finish.

## Required dependencies

1. Use the `uniparser` Skill for PDF to Markdown conversion.
2. Read the sibling Review contract before authoring:
   - `../materials-benchmark-review/references/harbor-package-contract.md`
   - `../materials-benchmark-review/references/correctness-gates.md`
   - `../materials-benchmark-review/references/hidden-checkpoints.md`
   - `../materials-benchmark-review/assets/instruction_template.md`
3. Use Harbor's current `create-task` guidance for generic task structure. When scaffolding with Harbor, always pass `--no-solution`.
4. Use `materials-benchmark-review` as an independent final gate. Do not use Repair as the normal authoring loop.

## Workflow

### 1. Create an external authoring workspace

From the repository root, run:

```bash
python3 .cursor/skills/materials-benchmark-authoring/scripts/init_authoring_workspace.py \
  --pdf <paper.pdf> \
  --output-root <processing-root> \
  --paper-id <stable-paper-id> \
  --task-name <org/task-name>
```

Freeze the PDF SHA-256. Put source, evidence, candidate, and review material under the processing root. Do not publish from this step.

### 2. Parse the PDF with UniParser

Use digital text extraction (`textual=3`) for a digital-native PDF. Use high-quality OCR (`2`) for scanned or layout-heavy text, equations, and tables. Save the formatted Markdown as `candidate/paper/paper.md`; save token, flags, PDF hash, and parse-quality observations in the external `authoring_record.json`.

Do not let missing formulas, tables, captions, units, or figure-linked Gold pass silently. Resubmit with better flags or mark `BLOCKED_SOURCE_PARSE`.

### 3. Build a paper evidence map before writing the question

Read [paper-evidence-and-candidate-selection.md](references/paper-evidence-and-candidate-selection.md). Record:

- computational research questions;
- systems, methods, equations, fixed conditions, units, and workflow dependencies;
- `PAPER_FIXED`, `SOLVER_SEARCHABLE`, `TARGET_DEFINING`, and `INDISPENSABLE_ASSET` items;
- candidate Gold as `PAPER_DIRECT`, `UNIQUE_DERIVATION`, or `PAPER_SUPPORTED_RELATION`;
- complete condition signatures and source locators;
- indispensable resource identities and availability.

Every claim used by the task must have a locator into `paper/paper.md` or a documented independent derivation.

### 4. Enumerate and gate multiple task candidates

Generate at least three candidates when the paper permits. Reject candidates whose scored core is pure information extraction, pure algebra, required experimental operation, or trivial experimental reduction.

Select only a candidate with:

- Q0 admission;
- paper-supported method and scientific target;
- at least one core Gold record with matching condition group;
- closed indispensable assets;
- a complete producer/consumer workflow;
- an affordable, non-arbitrary result checkpoint based on final outputs.

Use `NO_ENHANCED_CANDIDATE` when none qualifies. Read [pipeline-and-gates.md](references/pipeline-and-gates.md) for exact gates and outcomes.

### 5. Author the public scientific contract

Start from the Review instruction template. Make `instruction.md` self-contained after removing `paper/`.

- Include all paper-reported facts, equations, parameters, methods, and steps necessary to define the target.
- Mark paper-unreported execution choices as solver-searchable; never invent unique values.
- Treat composition, crystal system/space group, lattice data, and paper construction rules as the public structure definition. Do not require a CIF merely because the paper did not provide one; only a non-reconstructible fixed atomic realization is an indispensable structure asset.
- Declare every output path, format, schema, unit, primary key, cardinality, enum, and condition group.
- Refer to bundled inputs by stable filename only, never by `/app/resources/...`, package-relative path, dataset ID, or platform mount.
- Do not leak Gold values unless the scientific task itself requires a public target value; never score a publicly disclosed answer as the sole core result.

Then synchronize `instruction.md -> steps.json/manifest.json/resources.json/task.toml -> tests` in that order.

### 6. Close resources without binding the instruction to deployment

Read [package-profile.md](references/package-profile.md).

- Store each author-provided indispensable file at `candidate/resources/<filename>`.
- For an inherited Harbor package whose established layout stores the file under
  `assets/`, preserve that layout only when `access.package` gives a safe
  package-relative locator ending in the same `access.filename`; do not create
  a duplicate second source of truth under `resources/`.
- In `instruction.md`, mention only `<filename>` and its scientific role.
- In `resources.json`, use `access.method = "bundled"`, `access.filename = "<filename>"`, and a positional non-null `resources_mapping` entry with `resource_type` plus `resource_unique_key`.
- Do not add a Dockerfile `COPY` for authoring-time resources. Deployment may later materialize the resource through Playground/Bohrium; a local runner may receive an explicit resource root from a human.
- Keep the standard environment image and task defaults unless the external authoring record contains a justified override.

### 7. Freeze Gold, tolerance, and enhancement design

Read [gold-checker-enhancement.md](references/gold-checker-enhancement.md).

Before writing the checker, freeze:

- Gold policy, value/relation, units, applicability, condition groups, provenance, and independent check;
- tolerance basis and inclusive boundary behavior;
- public output-to-hidden target mapping;
- result checks and weights;
- expected real-scale output size and checker budget.

Do not use the checker, an old answer, or a prior solution as Gold provenance.

### 8. Generate and probe the checker

The checker may read hidden Gold and solver final outputs only. It must not rerun the main DFT, MD, training, or large search.

Run at least:

- `valid_positive`;
- `tolerance_boundary` with `T-epsilon/T/T+epsilon`;
- `missing_or_malformed`;
- `non_finite_and_duplicate`;
- `wrong_science`;
- one risk-matched enhancement probe: `minimal_fabrication`, `quality_gradient`, or `cross_condition_group_mismatch`.

Measure cost on real-scale output. Require at most 32 CPU cores or one H100, at most 600 seconds, no full large trajectory scan, and no new primary simulation.

### 9. Validate the authoring record and package

```bash
python3 .cursor/skills/materials-benchmark-authoring/scripts/validate_authoring_record.py \
  <processing>/authoring_record.json --stage review-ready
python3 .cursor/skills/materials-benchmark-authoring/scripts/validate_package.py \
  <processing>/candidate \
  --authoring-record <processing>/authoring_record.json
harbor check <processing>/candidate  # when Harbor is installed
```

The local validators are structural guardrails, not scientific approval.

### 10. Request independent Review and publish only after PASS

Run `materials-benchmark-review` on the candidate with `solution/` excluded. A successful authoring outcome requires:

- `verdict = PASS`;
- `publishable = true`;
- Baseline question and answer gates pass;
- enhanced result checks and checker-cost gate pass.

Record the review artifact in `authoring_record.json`, then validate with `--stage publish`. If Review fails, revise inside the authoring workspace from the cited evidence. Use Repair only for already-published or inherited packages when explicitly requested.

The publish validator reads the JSON at `independent_review.artifact_path`, runs the real Review 3.3 validator (including package-aware tier, weight, and tolerance checks), and then matches its verdict, quality tier, and publishability against the summary. A four-field stub is not a Review artifact. Do not copy a favorable summary without retaining the complete Review artifact outside the candidate package.

## Packaged references and tools

- [pipeline-and-gates.md](references/pipeline-and-gates.md): stage gates, failure routing, and state transitions.
- [paper-evidence-and-candidate-selection.md](references/paper-evidence-and-candidate-selection.md): evidence ledger and candidate ranking.
- [package-profile.md](references/package-profile.md): canonical Paper2Arm files, environment defaults, and resource semantics.
- [gold-checker-enhancement.md](references/gold-checker-enhancement.md): Gold, tolerance, weights, probes, and cost.
- [authoring-record-schema.md](references/authoring-record-schema.md): external record fields and invariants.
- [corpus-study.md](references/corpus-study.md): empirical conventions and failure signals from `material_v2_question`.
- `assets/authoring_record_template.json`: record template.
- `assets/package-template/`: solution-free package scaffold.
- `scripts/init_authoring_workspace.py`: immutable-source and candidate scaffold.
- `scripts/validate_authoring_record.py`: semantic authoring gate validator.
- `scripts/validate_package.py`: package/resource/static-checker validator.
