# Angular Distribution of Singular Stresses under Antiplane Shear in Orthotropic Solids

## Problem background
In the study of fracture mechanics, the stress distribution near a crack tip under dynamic loading determines how cracks may grow. When a horizontally polarized shear (SH) wave impinges on a finite crack in an orthotropic solid, the singular stress field near the tip deviates from the classical isotropic pattern. The orthotropic nature of the material — characterized by a dimensionless parameter κ that captures the ratio of two elastic wave speeds — alters the angular dependence of the stresses. This reproduction task asks you to compute the angular distribution functions R_c(κ,θ) and R_s(κ,θ) that govern the singular antiplane shear stresses, for a representative set of κ values. By evaluating these functions across a full angular range, you will quantify how orthotropy modifies the crack‑tip stress field, providing insight into the conditions that produce the most severe loading on the material.

## Approach
The analysis of the problem reduces to an antiplane elasticity formulation. By solving the governing wave equation with the appropriate mixed boundary conditions on the crack, one can extract the singular part of the stresses. The angular variation factorizes into two dimensionless functions, R_c(κ,θ) and R_s(κ,θ), that depend only on the orthotropic parameter κ and the polar angle θ. These functions can be written in closed form using elementary trigonometric operations and a square root. The symmetry of the crack geometry and the boundary conditions imposes the relation R_s(κ,θ) = R_c(κ, 180° – θ), so that only one independent function needs to be computed. You will implement these analytical expressions directly; no numerical solution of an integral equation is required for the angular functions. The output will be a table of values over a prescribed grid of κ and θ.

## Reproduction target
Produce a CSV file named angular_functions.csv in the directory /app/outputs. The file must contain columns: kappa (float), theta_deg (int), R_c (float), R_s (float). Compute values for kappa in the set {0.2, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0} and for theta_deg from 0 to 180 degrees inclusive in 1‑degree steps (181 angles per kappa). For each (kappa, theta_deg) compute R_c using the definition given in the Action of Workflow Step 1, and then set R_s = R_c(kappa, 180 – theta_deg). The verifier will independently recompute these values and compare them to your entries.

## Assets

- Python 3 standard library (math module): https://www.python.org/

## Workflow steps

### Step 1: Compute angular distribution functions
- Role: scored (load-bearing)
- Action: Implement the analytic expressions for the angular stress distribution functions R_c(κ,θ) and R_s(κ,θ). Use the definitions: R_c = sqrt((sqrt(cos²θ + κ² sin²θ) + cosθ) / (2 (cos²θ + κ² sin²θ))), and R_s(κ,θ) = R_c(κ,180°−θ), where θ is in radians. Compute values for κ in {0.2, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0} and θ from 0° to 180° in 1-degree increments. Write the results as a CSV file with columns kappa, theta_deg, R_c, R_s.
- Output file: `/app/outputs/angular_functions.csv`
- Format: csv
- Contract: kappa:float, theta_deg:int, R_c:float, R_s:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/angular_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### angular_functions.csv
- path: `/app/outputs/angular_functions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angular distribution functions R_c and R_s evaluated for a prescribed set of orthotropic parameters κ and angles θ.
- schema:
  - `type`: table
  - `required_columns`: `kappa`, `theta_deg`, `R_c`, `R_s`
  - `units`: object

Notes: The agent must not simply copy the paper's figures; it must recompute the formulas. The hidden checker will independently evaluate the same analytic expressions and compare each row within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "angular_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "kappa",
          "theta_deg",
          "R_c",
          "R_s"
        ],
        "units": {}
      },
      "description": "Angular distribution functions R_c and R_s evaluated for a prescribed set of orthotropic parameters κ and angles θ."
    }
  ],
  "notes": "The agent must not simply copy the paper's figures; it must recompute the formulas. The hidden checker will independently evaluate the same analytic expressions and compare each row within a tolerance."
}
```

## How you are scored
Your submission is evaluated automatically by a hidden verifier. For the angular distribution step, the verifier reads angular_functions.csv and recomputes the exact expected R_c and R_s for every row using the same analytic formulas with high precision. It checks that each of your values agrees with the recomputed value within a fixed absolute tolerance. In addition, it independently verifies the symmetry relation R_s(κ,θ)=R_c(κ,180°−θ) for a subset of entries. The score for this step is based on the fraction of rows that pass the tolerance and symmetry checks. This score is combined with scores from any other workflow stages to produce a final reward between 0 and 1. Reporting numbers you believe to be correct (even if obtained from an external source) without actually executing the computation will not satisfy the tolerance requirement and will result in a low score.
