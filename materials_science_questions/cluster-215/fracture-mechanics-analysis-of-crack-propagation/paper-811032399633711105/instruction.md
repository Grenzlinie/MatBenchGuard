# Fracture Mechanics: Crack Initiation Angle and Failure Stress from Analytical Model

## Problem background
When an elastic specimen containing a pre-existing crack is compressed, a new crack often initiates from the tip of the pre-existing crack at an obtuse angle (greater than 90°), eventually causing a triangular block to detach. Understanding this crack initiation mechanism is important for rock mechanics and tunnel engineering. This task implements an analytical model that predicts the new crack angle (γ) and the failure pressure (p) as functions of the pre-existing crack angle (β).

## Approach
The model is based on superposition of two stress fields: the far-field compressive stress and the stress induced by sliding displacement along the faces of the pre-existing crack. The sliding gives rise to a concentrated stress field near the crack tip, and the direction of the new crack is determined by maximizing the resulting tangential stress around the tip. This leads to a transcendental equation that relates the crack initiation angle γ to the pre-existing crack angle β, and to an expression for the failure pressure p that involves the solved γ and β.

Specifically, with given material constants (β₀ = 0, c₁ = 2.5, c₂ = 19.0), the model reduces to:
1. Solve for γ (in radians) from
   sin(2(β + γ)) = c₁ · cos β · cos γ.
2. Compute p (g/cm²) as
   p = c₂ · cot γ / sin(2(γ + β)).

The approach is to treat each required β value (0° to 90° in 10° steps) separately, numerically solve the transcendental equation for γ, then compute the corresponding p, and finally collect the results into a CSV file.

## Reproduction target
For pre-existing crack angles β = 0°, 10°, 20°, …, 90°, implement the analytical model described above. Solve the transcendental equation for γ, compute the failure pressure p, and save the results as a CSV file with three columns: beta (in degrees), gamma (in degrees), and p (in g/cm²). The goal is to produce these predicted values through the specified computation.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute crack initiation angle and failure stress
- Role: scored (load-bearing)
- Action: Implement the crack initiation model. For each pre-existing crack angle β in 0°, 10°, ..., 90°, numerically solve the equation sin(2(β+γ)) = 2.5·cos(β)·cos(γ) for γ (in radians). Then compute the failure pressure p = 19.0·cot(γ) / sin(2(γ+β)). Collect results as rows with columns beta (in degrees), gamma (in degrees), and p (in g/cm²). Save to crack_initiation_results.csv.
- Output file: `/app/outputs/crack_initiation_results.csv`
- Format: csv
- Contract: CSV with header: beta,gamma,p. Each row: beta (float, angle in degrees), gamma (float, predicted new crack angle in degrees), p (float, failure pressure in g/cm²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/crack_initiation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### crack_initiation_results.csv
- path: `/app/outputs/crack_initiation_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Predicted crack initiation angle γ and failure pressure p from the analytical model. The checker recomputes γ and p from the same equations and compares within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `beta`, `gamma`, `p`
  - `units`:
    - `beta`: degree
    - `gamma`: degree
    - `p`: g/cm^2

Notes: The task uses the constants β0=0, c1=2.5, c2=19.0 as specified in the paper. No external data is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "crack_initiation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta",
          "gamma",
          "p"
        ],
        "units": {
          "beta": "degree",
          "gamma": "degree",
          "p": "g/cm^2"
        }
      },
      "description": "Predicted crack initiation angle γ and failure pressure p from the analytical model. The checker recomputes γ and p from the same equations and compares within tolerances."
    }
  ],
  "notes": "The task uses the constants β0=0, c1=2.5, c2=19.0 as specified in the paper. No external data is required."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores each workflow stage's output artifact and combines them by weight into a final reward between 0 and 1. The verifier recomputes the model from scratch, compares your submitted gamma and p values to the expected values for each β, and awards partial credit accordingly. Reporting numbers you have not actually computed (e.g., copying them from a reference) is not sufficient; you must execute the required computation and produce the CSV file as described.
