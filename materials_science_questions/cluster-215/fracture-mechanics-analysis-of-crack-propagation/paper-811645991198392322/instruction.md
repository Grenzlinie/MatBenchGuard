# Bending and Torsion Fracture Stress Ratios for Hollow Cylinders

## Problem background
The task concerns the fracture of hollow cylinders made of a brittle material under bending and torsion. For a cylinder with outer diameter d0 and inner diameter d1, the inner/outer diameter ratio is γ1 = d1/d0. Under four-point bending, the normalized fracture stress ratio σ̄_A/σ_b (the mean tensile stress at fracture divided by the material tensile strength) is predicted to depend on γ1. A theoretical model proposes that for thick-walled cylinders (small γ1) the ratio follows a specific formula derived from a limit‑case criterion, while for thin‑walled cylinders (large γ1) the ratio approaches a constant corresponding to a mean‑stress criterion. Under torsion, the same model predicts that the normalized fracture stress ratio is independent of γ1. The objective is to compute these predicted ratios for a range of γ1 values covering both regimes.

## Approach
Implement the two‑regime bending model and the constant torsion model as follows:
- **Bending**: if γ1 > 0.65, the predicted normalized fracture stress ratio σ̄_A/σ_b = 1.0 (mean‑stress branch). If γ1 ≤ 0.65, the predicted ratio is given by (9π/32)*(1−γ1⁴)/(1−γ1³).
- **Torsion**: the predicted ratio σ̄_A/σ_b = 1.0 for all γ1.

Compute these ratios for a prescribed list of γ1 values and write the results to a CSV file.

## Reproduction target
For the γ1 values [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], compute the predicted normalized fracture stress ratios using the formulas above. Produce a CSV file `step_01_predictions.csv` with three columns: `gamma` (the inner/outer diameter ratio), `bending_predicted_ratio` (σ̄_A/σ_b for bending), and `torsion_predicted_ratio` (σ̄_A/σ_b for torsion). Each row corresponds to one γ1 value; sort the rows by γ1 ascending.

## Assets

- Python 3

## Workflow steps

### Step 1: Compute predicted fracture stress ratios
- Role: scored (load-bearing)
- Action: For the inner/outer diameter ratios γ₁ in [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], compute the predicted normalized bending fracture stress ratio σ̄_A/σ_b: if γ₁ > 0.65, ratio = 1.0; else ratio = (9π/32)*(1−γ₁⁴)/(1−γ₁³). Compute the predicted normalized torsion fracture stress ratio σ̄_A/σ_b = 1.0 for all γ₁. Write a CSV file with columns gamma, bending_predicted_ratio, torsion_predicted_ratio.
- Output file: `/app/outputs/step_01_predictions.csv`
- Format: csv
- Contract: CSV with three columns: gamma (float), bending_predicted_ratio (float), torsion_predicted_ratio (float). Example row: 0.0,0.883...,1.0
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_predictions.csv
- path: `/app/outputs/step_01_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Predicted normalized fracture stress ratios for hollow cylinders under bending and torsion at specified inner/outer diameter ratios.
- schema:
  - `type`: table
  - `required_columns`: `gamma`, `bending_predicted_ratio`, `torsion_predicted_ratio`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "gamma",
          "bending_predicted_ratio",
          "torsion_predicted_ratio"
        ]
      },
      "description": "Predicted normalized fracture stress ratios for hollow cylinders under bending and torsion at specified inner/outer diameter ratios."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier reads your CSV, extracts the gamma values, and independently recomputes the expected bending and torsion ratios using the same theoretical formulas. It compares your reported ratios to these recomputed values, checking that the bending regime switching is correctly implemented (for γ1 > 0.65 the ratio should be 1.0, and for γ1 ≤ 0.65 it should match the limit‑case formula). The final score is a weighted combination of the closeness of your bending ratios and torsion ratios to the expected values, within a small tolerance that accounts for floating‑point arithmetic. Reproducing the experimental measurements from the literature is not the goal; you must compute the theoretical predictions from the given model.
