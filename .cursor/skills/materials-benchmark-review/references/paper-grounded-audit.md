# Triggered paper audit

Read paper only after at least one confirmed trigger:

- `SCIENTIFIC_CONFLICT`;
- `NECESSARY_INFORMATION_MISSING`;
- `GOLD_PROVENANCE_UNCERTAIN`;
- `EXPLICIT_REPRODUCTION_CLAIM`.

Bind the paper-grounded report to the preceding no-paper audit ID, all source
hashes, and the Review implementation hash. Paper-grounded E1 checks fidelity
and expected checker behavior; it does not claim that the scientific workflow
was executed.

## Reproduction type

- `EXACT_REPRODUCTION`: instruction explicitly fixes the paper system,
  conditions, method, and target result.
- `METHOD_REIMPLEMENTATION`: the paper method or scientific endpoint is
  implemented with scientifically equivalent choices. This is the default.
- `SCIENTIFIC_EXTENSION`: a new system, question, or endpoint is evaluated;
  paper values cannot be its sole Gold.

Equivalent software, versions, and solver-selected cutoff, mesh, convergence,
seed, or search parameters are allowed unless they change the defined system,
normalization, endpoint, or expected result; instruction may also explicitly
fix a choice. Missing detail is a defect only if the scored quantity becomes
undefined, valid input cannot be constructed, results cannot reasonably be
compared, or checker secretly relies on an undisclosed choice.

## Five paper dimensions

Record `PASS`, `WARNING`, `FAIL`, or `NOT_ASSESSABLE` for:

1. `instruction_fidelity`;
2. `data_fidelity`;
3. `method_fidelity`;
4. `gold_provenance`;
5. `checker_fidelity`.

PASS/WARNING/FAIL require an exact paper quote paired with an exact quote from
`instruction.md` or `tests/**`. `solution/**` cannot be paper evidence.
`NOT_ASSESSABLE` requires an empty evidence list and is temporary.

Gold provenance is mode-dependent: EXACT may compare paper values; METHOD may
use independent computation, physical constraints, or an equivalent reference;
EXTENSION needs independent scientific support and must not be forced to paper
numbers.

## Taxonomy

Preserve the pinned taxonomy snapshot and labels:

- one or more equal `computation_task` labels;
- one or more `research_domain` labels;
- one `material_system.primary` plus optional evidence-backed secondary tags.

Cluster and manifest values are not evidence. Every selected label needs an
exact quote from instruction or tests.

## Assessment shape

Write JSON outside the package:

```json
{
  "schema_version": "0.1",
  "paper_triggers": ["EXPLICIT_REPRODUCTION_CLAIM"],
  "reproduction_type": "METHOD_REIMPLEMENTATION",
  "dimensions": {
    "instruction_fidelity": {
      "status": "PASS",
      "rationale": "Evidence-backed rationale.",
      "evidence": [{
        "paper_quote": "Exact paper quote",
        "package_file": "instruction.md",
        "package_quote": "Exact instruction quote"
      }]
    },
    "data_fidelity": {"status": "PASS", "rationale": "...", "evidence": [{}]},
    "method_fidelity": {"status": "PASS", "rationale": "...", "evidence": [{}]},
    "gold_provenance": {"status": "PASS", "rationale": "...", "evidence": [{}]},
    "checker_fidelity": {"status": "PASS", "rationale": "...", "evidence": [{}]}
  },
  "taxonomy": {
    "computation_task": ["声子与晶格动力学"],
    "research_domain": ["基础材料研究与材料发现"],
    "material_system": {"primary": "金属与合金", "secondary": ["铜"]}
  },
  "taxonomy_evidence": []
}
```

Omitting `reproduction_type` defaults to METHOD. The runner rejects unknown
triggers, unsupported taxonomy labels, non-exact quotes, paper-as-package
evidence, and solution evidence.
