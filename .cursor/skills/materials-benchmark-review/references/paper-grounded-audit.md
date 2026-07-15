# Paper-grounded audit

Use this branch only after completing the no-paper checks. It compares the
public task and privileged tests with the bundled paper without inspecting
`solution/`.

## Classify the task

Choose exactly one:

- `EXACT_REPRODUCTION` — the task claims to reproduce the paper's result with
  the same method, inputs, versions, and scientific scope.
- `METHOD_REIMPLEMENTATION` — the task implements a paper method or a
  deliberately scoped specialization; equivalent implementations are allowed.
- `SCIENTIFIC_EXTENSION` — the task applies the paper's method to a new system,
  question, or analysis. Exact paper values cannot be its sole Gold.

## Assess five dimensions

For every dimension, record `PASS`, `WARNING`, `FAIL`, or `NOT_ASSESSABLE` and
a concise rationale. PASS/WARNING/FAIL require at least one evidence pair;
NOT_ASSESSABLE uses an empty evidence list and explains what is unavailable.
Each evidence pair must contain an exact quote from
`paper/paper.md`, an exact quote from a public or privileged package file, and
that package file's relative path.

The package side may reference only the Harbor roles listed in
`harbor-contract.md`. It cannot reference the paper itself, generated audit
artifacts, or `solution/`; otherwise one source could masquerade as both sides
of the comparison.

1. `instruction_fidelity` — scope, requested endpoint, required operation, and
   claims match the selected reproduction type.
2. `data_fidelity` — materials, structures, samples, constants, units,
   conditions, versions, and exclusions have supportable provenance.
3. `method_fidelity` — equations, method choices, order, parameters, and
   equivalence rules match the paper or clearly state a justified adaptation.
4. `gold_provenance` — Gold is experimental, curated, recomputed, transcribed,
   or digitized as claimed; uncertainty and multiple valid answers are handled.
5. `checker_fidelity` — the checker enforces the paper-grounded scientific
   target rather than file shape, public constants, or an unrelated proxy.

`FAIL` creates a FATAL paper finding. `WARNING` creates a HIGH finding. Use
`NOT_ASSESSABLE` rather than inventing a quote or conclusion.

## Apply the pinned taxonomy

Read [materials-taxonomy.json](materials-taxonomy.json). Select:

- one or more equal `computation_task` labels;
- one or more `research_domain` labels;
- one `material_system.primary` and optional free-text secondary tags.

For every selected label, add one or more exact package quotes under
`taxonomy_evidence`. Evidence uses a dimension name, selected label, Harbor
role, and exact quote. Secondary material-system labels also require evidence.

Cluster and manifest discipline are hints only. Base labels on the task's
scientific content and scored operations. The runner rejects category labels
that are absent from the pinned taxonomy and records its Feishu URL and
revision in the report.

## Assessment shape

Write a JSON object outside the Harbor 题包:

```json
{
  "schema_version": "0.1",
  "reproduction_type": "METHOD_REIMPLEMENTATION",
  "dimensions": {
    "instruction_fidelity": {
      "status": "PASS",
      "rationale": "Why the evidence supports this status.",
      "evidence": [{
        "paper_quote": "Exact quote from paper/paper.md",
        "package_file": "instruction.md",
        "package_quote": "Exact quote from the named package file"
      }]
    },
    "data_fidelity": {"status": "PASS", "rationale": "...", "evidence": []},
    "method_fidelity": {"status": "PASS", "rationale": "...", "evidence": []},
    "gold_provenance": {"status": "PASS", "rationale": "...", "evidence": []},
    "checker_fidelity": {"status": "PASS", "rationale": "...", "evidence": []}
  },
  "taxonomy": {
    "computation_task": ["声子与晶格动力学"],
    "research_domain": ["基础材料研究与材料发现"],
    "material_system": {"primary": "金属与合金", "secondary": ["铜"]}
  },
  "taxonomy_evidence": [{
    "dimension": "computation_task",
    "label": "声子与晶格动力学",
    "package_file": "instruction.md",
    "package_quote": "Exact quote supporting this label"
  }, {
    "dimension": "research_domain",
    "label": "基础材料研究与材料发现",
    "package_file": "instruction.md",
    "package_quote": "Exact quote supporting this label"
  }, {
    "dimension": "material_system.primary",
    "label": "金属与合金",
    "package_file": "instruction.md",
    "package_quote": "Exact quote supporting this label"
  }, {
    "dimension": "material_system.secondary",
    "label": "铜",
    "package_file": "instruction.md",
    "package_quote": "Exact quote supporting this label"
  }]
}
```

Replace every placeholder and ensure every dimension has evidence before
running the review. The runner verifies that quotes occur in the named files,
that evidence never references `solution/`, and that taxonomy labels belong to
the pinned revision.

For `no_paper`, submit only `schema_version`, `taxonomy`, and
`taxonomy_evidence`. The runner rejects reproduction types or paper dimensions
in that mode and keeps paper consistency `NOT_ASSESSED`.
