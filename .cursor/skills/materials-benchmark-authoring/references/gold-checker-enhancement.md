# Gold, checker, and result enhancement

## Gold records

Every core target must include:

- stable `target_id`;
- condition group IDs;
- `PAPER_DIRECT`, `UNIQUE_DERIVATION`, or `PAPER_SUPPORTED_RELATION`;
- value or relation kept outside the public instruction when it is the answer;
- units and coordinate/sign convention;
- exact applicability;
- paper locator and independent check;
- hidden reference filename when needed.

The paper is the scientific source. A checker value, historical answer, or generated solution cannot establish Gold.

## Condition groups

Use one public stable ID per required group. A condition signature must include every target-defining value needed to distinguish Gold applicability. The checker must reject missing, duplicate, or swapped groups.

## Tolerances

Choose evidence in this order:

1. reported uncertainty;
2. reported precision;
3. auditable digitization;
4. independent recomputation;
5. convergence evidence;
6. cross-implementation evidence;
7. explicit reviewer/author physical-numerical rationale.

Record metric, `atol`, `rtol`, units, inclusive/exclusive boundary, and `T-epsilon/T/T+epsilon` observations. Never move the Gold center to fit a candidate output.

## Enhanced result checks

Enhancement is optional. Select it only when the record documents all four gates: a paper/physics/materials-model/independent-reference basis, a concrete fabrication risk, an explanation of how the check discriminates wrong materials science, and checker-cost compliance. A cheap format or self-consistency check is not sufficient. Otherwise keep the complete task at `BASELINE_CORRECT`.

Prefer checks that reuse required final outputs:

- recomputed derived quantities;
- conservation or normalization;
- sign, ordering, monotonicity, boundedness, or symmetry;
- residuals against the stated model;
- cross-file or cross-condition consistency;
- a few representative curve points;
- checker-external offline reference with provenance.

Do not score logs, iteration counts, claims of execution, or full process traces as scientific results. Do not rerun the primary computation.

## Weighting

- Baseline: Gold 1.0, result checks 0.0.
- Gold: 0.60--0.80.
- Enhanced result checks: 0.20--0.40.
- Total: 1.0.

Distribute Gold weight across all core outputs and condition groups. Do not let a cosmetic file dominate a load-bearing scientific result.

## Required probes

Baseline:

- `valid_positive`;
- `tolerance_boundary`;
- `missing_or_malformed`;
- `non_finite_and_duplicate`;
- `wrong_science`.

Enhanced: add at least one probe that matches the selected checkpoint:

- `minimal_fabrication`;
- `quality_gradient`;
- `cross_condition_group_mismatch`.

Record per-component rewards, not only total reward.

## Checker cost

Measure on real-scale expected output:

```json
{
  "hardware_class": "CPU",
  "cpu_cores": 1,
  "gpu_count": 0,
  "gpu_type": null,
  "h100_equivalent_or_less": null,
  "measured_wall_seconds": 0.1,
  "peak_memory_mb": 20,
  "input_bytes_read": 1000,
  "uses_full_trajectory": false,
  "performs_new_simulation": false,
  "real_scale_input": true,
  "cost_rationale": "Measured on full expected outputs.",
  "status": "PASS"
}
```

Hard limits: 32 CPU cores or one H100, 600 seconds, no full large trajectory scan, and no new main simulation/training/search.
