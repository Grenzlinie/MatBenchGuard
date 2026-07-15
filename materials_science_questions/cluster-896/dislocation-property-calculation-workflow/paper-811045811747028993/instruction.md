# Compute dislocation nucleation parameters for small-angle boundaries

## Problem background
In deformed face-centered cubic metals, plastic deformation leads to a microstructure of cells separated by low-angle dislocation boundaries. The internal stresses from strain gradients in these cells can be partially relieved by nucleating new small-angle boundaries. The paper models this nucleation as a first-order transition: when the misorientation between cell ends exceeds a critical value, a new boundary with a finite misorientation appears. The model introduces a dimensionless parameter Q that depends on the Poisson ratio, a characteristic cell size-to-Burgers-vector ratio D/b, a dislocation density factor M, and a shape factor λ. From Q, one derives a critical misorientation X_c = (ln Q)/Q and a minimum nucleation angle Φ_min = 1/Q. The task is to compute these quantities for a given set of physical parameters.

## Approach
The model is based on an energy minimization argument. The total energy density in a cell is expressed as the sum of an elastic strain term and a dislocation energy term. Minimization leads to an equation whose solution determines the equilibrium boundary angle. For large enough cell-end misorientation X, the energy function F(Φ) = QΦ - ln Φ has a minimum at Φ = 1/Q, and the transition occurs when X > (ln Q)/Q. Therefore, the required computation reduces to evaluating Q from the input constants using Q = 2π(1−ν²)(D/b) / (3 M λ), then computing X_c = ln(Q)/Q, Φ_min = 1/Q, and the ratio X_c/Φ_min = ln Q. This is a purely analytical calculation; the agent should implement these formulas in code (e.g., Python) and write the results to a JSON file in /app/outputs.

## Reproduction target
Using the physical constants ν = 1/3, D/b = 500, M = 2, and λ = 3/2, compute the dimensionless parameter Q from the formula Q = 2π(1−ν²)(D/b) / (3 M λ). Then compute the critical misorientation X_c in radians: X_c = ln(Q)/Q, and the minimum nucleation angle Φ_min in radians: Φ_min = 1/Q. Convert both angles to degrees. Compute the ratio X_c/Φ_min = ln Q. Write all quantities to a JSON file /app/outputs/results.json with exactly these keys: Q (float), X_c_rad (float, radians), Phi_min_rad (float, radians), X_c_deg (float, degrees), Phi_min_deg (float, degrees), ratio_X_Phi (float, dimensionless).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Q and derive nucleation parameters
- Role: scored (load-bearing)
- Action: Compute the dimensionless parameter Q from the given physical constants (Poisson ratio ν=1/3, D/b=500, M=2, λ=3/2) using Q = 2π(1-ν²)(D/b)/(3 M λ). Then compute the critical misorientation X_c = ln(Q)/Q (radians) and the minimum nucleation angle Φ_min = 1/Q (radians). Convert both to degrees. Compute the ratio X_c/Φ_min (= ln Q). Write all computed quantities to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: Q (float, dimensionless), X_c_rad (float, radians), Phi_min_rad (float, radians), X_c_deg (float, degrees), Phi_min_deg (float, degrees), ratio_X_Phi (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed dislocation nucleation quantities: Q, critical misorientation and nucleation angle in radians and degrees, and their ratio.
- schema:
  - `type`: object
  - `required`:
    - `Q`: float
    - `X_c_rad`: float
    - `Phi_min_rad`: float
    - `X_c_deg`: float
    - `Phi_min_deg`: float
    - `ratio_X_Phi`: float

Notes: The checker recomputes expected values from the same input parameters using the exact formulas and compares each numeric field within tolerance. Internal consistency (X_c_rad ≈ ln(Q)/Q, Phi_min_rad ≈ 1/Q) is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "Q": "float",
          "X_c_rad": "float",
          "Phi_min_rad": "float",
          "X_c_deg": "float",
          "Phi_min_deg": "float",
          "ratio_X_Phi": "float"
        }
      },
      "description": "Computed dislocation nucleation quantities: Q, critical misorientation and nucleation angle in radians and degrees, and their ratio."
    }
  ],
  "notes": "The checker recomputes expected values from the same input parameters using the exact formulas and compares each numeric field within tolerance. Internal consistency (X_c_rad ≈ ln(Q)/Q, Phi_min_rad ≈ 1/Q) is also verified."
}
```

## How you are scored
For each scored step, a hidden verifier recomputes the expected reference values from the same input parameters using the exact formulas. It compares each numeric field in your results.json against those references with appropriate tolerances. Additionally, the verifier checks internal consistency: your reported X_c_rad must satisfy X_c_rad ≈ ln(Q)/Q, and Phi_min_rad ≈ 1/Q, given your reported Q. The final reward is a weighted sum of the scores of all fields. You do not need to match any specific paper-reported numbers; correct implementation of the formulas will yield a high score.
