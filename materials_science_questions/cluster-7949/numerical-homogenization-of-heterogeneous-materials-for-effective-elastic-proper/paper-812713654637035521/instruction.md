# Multiscale Homogenization of Cement Paste for Elastic and Transport Properties

## Problem background
Predicting the effective elastic moduli and chloride diffusivity of Portland cement paste is essential for assessing concrete durability and service life. The paste's microstructure evolves during hydration, and its macroscopic stiffness and transport properties are governed by the water‑to‑cement ratio (w/c) and the hydration degree (α). This task implements an engineering multiscale homogenization model that estimates both properties from the evolving volume fractions of clinker, hydrates, and capillary pores, providing a computational tool to explore these structure‑property relationships.

## Approach
The effective properties are obtained by a two‑level analytical homogenization. At the first level, a hydrate foam is treated as a disordered mixture of hydration products (modelled as oblate spheroids) and capillary pores (modelled as prolate spheroids); its stiffness and diffusivity are estimated with a self‑consistent scheme that captures percolation effects. At the second level, the cement paste is described as a matrix‑inclusion composite: the hydrate foam forms the matrix, and spherical anhydrous clinker grains are embedded using the Mori‑Tanaka scheme. The volume fractions of clinker, hydrates, and capillary pores as functions of w/c and α are computed from Powers' hydration model under conditions where external water is available, supplying the maximum attainable hydration degree. The required phase properties (elastic moduli, diffusion coefficients, and aspect ratios) are taken from published Portland cement data.

## Reproduction target
For a water‑to‑cement ratio of 0.4, compute the drained Young's modulus as a function of hydration degree α (from 0 up to the maximum attainable α). For mature pastes (α at its maximum), compute the normalized effective chloride diffusivity D/D_bulk over a range of w/c from 0.23 to 0.80. Output two CSV files containing the computed curves, with the column schema specified in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute volume fractions from Powers' hydration model
- Role: process
- Action: Compute volume fractions for cement paste as functions of water‑to‑cement ratio (w/c) and hydration degree (α) according to Powers' hydration model. Use model constants ρ_a=3.13, κ_w=1.31, κ_h=2.13 and the maximum hydration degree formula for externally available water. Produce a CSV covering w/c ∈ [0.23, 0.80] and α from 0 to α_max in a reasonable step. For each (w/c, α), output: wc_ratio, hydration_degree, f_a (clinker), f_h (hydrates), f_cp (capillary pores), phi = f_cp/(f_cp+f_h).
- Evidence: `/app/outputs/volume_fractions.csv`

### Step 2: Compute Young's modulus vs hydration for w/c=0.4
- Role: scored (load-bearing)
- Action: For w/c = 0.4, iterate over hydration degree α from 0 to α_max using the volume fractions from step_01. At each α, compute the drained Young’s modulus of cement paste by first solving the self‑consistent elasticity equations for the hydrate foam, then applying the Mori‑Tanaka scheme to embed spherical anhydrous clinker inclusions. Phase properties: hydrate E_h = 25.3 GPa, ν_h = 0.29, aspect ratio ω_h = 0.013; capillary pores zero stiffness, ω_cp = 6; clinker E_a = 135 GPa, ν_a = 0.3. Output a CSV with hydration_degree and young_modulus_GPa.
- Output file: `/app/outputs/youngs_modulus_vs_hydration.csv`
- Format: csv
- Contract: Columns: hydration_degree (float), young_modulus_GPa (float)
- Scoring: scored by hidden verifier

### Step 3: Compute normalized chloride diffusivity vs w/c for mature pastes
- Role: scored
- Action: For w/c from 0.23 to 0.80, determine α_max using Powers’ model with external water. At α = α_max, use volume fractions from step_01 to compute the normalized effective chloride diffusivity D/D_bulk of mature paste. At level I, solve the self‑consistent diffusion equation for the hydrate foam: hydrate diffusivity D_h = 5.04×10⁻⁴ D_bulk, ω_h = 0.013; capillary pore diffusivity D_cp = D_bulk, ω_cp = 6. Then apply the Mori‑Tanaka scheme to embed non‑diffusive spherical clinker inclusions. Output a CSV with wc_ratio and normalized_diffusivity.
- Output file: `/app/outputs/diffusivity_vs_wc_mature.csv`
- Format: csv
- Contract: Columns: wc_ratio (float), normalized_diffusivity (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/youngs_modulus_vs_hydration.csv`
- `/app/outputs/diffusivity_vs_wc_mature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### youngs_modulus_vs_hydration.csv
- path: `/app/outputs/youngs_modulus_vs_hydration.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Young's modulus curve for w/c=0.4
- schema:
  - `type`: table
  - `required_columns`: `hydration_degree`, `young_modulus_GPa`
  - `units`:
    - `hydration_degree`: dimensionless
    - `young_modulus_GPa`: GPa

### diffusivity_vs_wc_mature.csv
- path: `/app/outputs/diffusivity_vs_wc_mature.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Diffusivity vs. water-to-cement ratio for mature pastes
- schema:
  - `type`: table
  - `required_columns`: `wc_ratio`, `normalized_diffusivity`
  - `units`:
    - `wc_ratio`: dimensionless
    - `normalized_diffusivity`: dimensionless (D/D_bulk)

Notes: All outputs are scored using metric_recompute: the verifier independently computes reference values for the same conditions and assesses the agent’s output values. Young’s modulus is scored by directional percentage error (meeting or beating 5% error earns full credit), diffusivity by directional relative error (meeting or beating 10% error earns full credit).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "youngs_modulus_vs_hydration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "hydration_degree",
          "young_modulus_GPa"
        ],
        "units": {
          "hydration_degree": "dimensionless",
          "young_modulus_GPa": "GPa"
        }
      },
      "description": "Young's modulus curve for w/c=0.4"
    },
    {
      "file": "diffusivity_vs_wc_mature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wc_ratio",
          "normalized_diffusivity"
        ],
        "units": {
          "wc_ratio": "dimensionless",
          "normalized_diffusivity": "dimensionless (D/D_bulk)"
        }
      },
      "description": "Diffusivity vs. water-to-cement ratio for mature pastes"
    }
  ],
  "notes": "All outputs are scored using metric_recompute: the verifier independently computes reference values for the same conditions and assesses the agent’s output values. Young’s modulus is scored by directional percentage error (meeting or beating 5% error earns full credit), diffusivity by directional relative error (meeting or beating 10% error earns full credit)."
}
```

## How you are scored
A hidden verifier independently re‑implements the same engineering model using the same parameters and recomputes the expected output values for the specified conditions. It compares your submitted CSV data against these independent reference computations. Scoring is based on directional error metrics: for each quantity, a result that meets or exceeds the reference quality earns full credit, while larger deviations receive progressively lower credit. The final reward is the weighted combination of the scores from the two scored artifacts.
