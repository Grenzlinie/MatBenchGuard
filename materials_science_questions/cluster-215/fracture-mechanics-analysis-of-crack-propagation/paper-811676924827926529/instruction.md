# Lamellar TiAl Yield and Fracture Stress Prediction

## Problem background
In lamellar TiAl intermetallic, the interfaces between γ and α₂ lamellae create internal mismatches that lead to strong plastic anisotropy. The yield stress and fracture stress under tension depend markedly on the orientation of the lamellae relative to the loading axis. A mechanistic model combining Schmid factors with Hall‑Petch grain‑size strengthening and Stroh crack‑nucleation analysis can predict the yield and fracture stresses for different tensile axes. Understanding this orientation dependence helps quantify how microstructural constraints govern mechanical performance.

## Approach
The yield stress σy is given by the Hall‑Petch relation σy = τ0/S + B/√ℓ, where τ0 is the critical resolved shear stress, S is the Schmid factor of the deformation system, B is the Hall‑Petch coefficient, and ℓ is the dislocation mean‑free path (lamellar thickness in hard mode, domain size in soft mode). The corresponding fracture stress σf follows the Stroh model, σf = (1/S)(τ0 + A/√ℓ), where A is a material constant. For each of five tensile axis orientations (A, B, C, D, N), you will evaluate all candidate slip and twin systems with known Schmid factors, dislocation types (perfect, twin, super), and soft/hard modes. From these, select the system that minimises σy, then compute the final σy and σf for that axis. Use the supplied material constants: τ0 = 40 MPa for perfect dislocations, 60 MPa for twins, 80 MPa for super dislocations; B = 0.2 MPa√m (soft mode) and 0.3 MPa√m (hard mode); ℓ = 40 μm (soft mode) and 1.2 μm (hard mode); and A = 0.15 MPa√m. The candidate systems and their parameters are:

| Tensile Axis | System                                           | Type    | Schmid Factor S | Mode |
|--------------|--------------------------------------------------|---------|-----------------|------|
| A            | [101](111) etc                                   | super   | 0.41            | hard |
| A            | [011](111) etc                                   | super   | 0.41            | hard |
| A            | [112](111) etc                                   | twin    | 0.47            | hard |
| B            | [110](111)                                       | perfect | 0.45            | soft |
| B            | [011](111)                                       | super   | 0.45            | hard |
| B            | [112](111)                                       | twin    | 0.38            | hard |
| C            | [110](111)                                       | perfect | 0.49            | soft |
| C            | [110](111)                                       | perfect | 0.49            | hard |
| D            | [110](111)                                       | perfect | 0.47            | hard |
| D            | [110](111)                                       | perfect | 0.35            | soft |
| D            | [101](111)                                       | super   | 0.35            | hard |
| N            | [112](111)                                       | twin    | 0.31            | hard |
| N            | [110](111) etc                                   | perfect | 0.27            | hard |
| N            | [101](111) etc                                   | super   | 0.27            | hard |

## Reproduction target
Compute the predicted yield stress σy (MPa) and fracture stress σf (MPa) for each tensile axis (A, B, C, D, N) and write them to /app/outputs/stress_predictions.csv. The CSV must have columns: tensile_axis (string), sigma_y (float, MPa), sigma_f (float, MPa). The check will compare your predictions against independently determined reference values derived from the model—no external datasets are required.

## Assets

- Python scientific computing stack: python

## Workflow steps

### Step 1: Compute yield and fracture stresses for lamellar orientations
- Role: scored (load-bearing)
- Action: Implement the Hall‑Petch (σy = τ0/S + B/ℓ^(1/2)) and Stroh (σf = (1/S)(τ0 + A/ℓ^(1/2))) equations. For each tensile axis (A, B, C, D, N), evaluate the candidate slip and twin systems listed in the paper (including their Schmid factors S, type (perfect/twin/super), and soft/hard mode). Use the correct τ0 for the system type (perfect 40 MPa, twin 60 MPa, super 80 MPa) and B (0.2 MPa√m soft mode, 0.3 MPa√m hard mode), ℓ (1.2 μm hard mode, 40 μm soft mode), and A = 0.15 MPa√m. Determine the system that minimises σy, compute the final σy and σf, and write the results to /app/outputs/stress_predictions.csv.
- Output file: `/app/outputs/stress_predictions.csv`
- Format: csv
- Contract: columns: tensile_axis (str, one of A,B,C,D,N), sigma_y (float, MPa), sigma_f (float, MPa)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_predictions.csv
- path: `/app/outputs/stress_predictions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted yield and fracture stresses for lamellar TiAl tensile orientations
- schema:
  - `type`: table
  - `required_columns`: `tensile_axis`, `sigma_y`, `sigma_f`
  - `units`:
    - `sigma_y`: MPa
    - `sigma_f`: MPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tensile_axis",
          "sigma_y",
          "sigma_f"
        ],
        "units": {
          "sigma_y": "MPa",
          "sigma_f": "MPa"
        }
      },
      "description": "Predicted yield and fracture stresses for lamellar TiAl tensile orientations"
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your stress_predictions.csv. For each tensile axis, it compares your reported sigma_y and sigma_f to the expected values (the paper’s computed predictions) within a predefined tolerance. The fraction of orientations where both sigma_y and sigma_f satisfy the tolerance gives your total score. Simply reporting the paper’s numbers is not sufficient; the verifier checks the actual values in your file.
