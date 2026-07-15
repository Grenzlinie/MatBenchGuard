# GMTS Fracture Initiation Angle Prediction for Mixed-Mode I/II Loading

## Problem background
In brittle materials such as limestone, cracks often propagate under a mixture of opening (mode I) and sliding (mode II) loading. The direction in which a crack initiates—the fracture initiation angle—can depend on the specimen geometry and size, not just on the relative amount of mode I and mode II present. Conventional fracture criteria based only on the stress intensity factors \(K_{\mathrm{I}}\) and \(K_{\mathrm{II}}\) predict a unique initiation angle for a given mode mixity, but experiments on centre-cracked circular disc (CCCD) and semi-circular bend (SCB) specimens of Guiting limestone reveal that the angle differs with specimen shape and specimen size. A generalized maximum tangential stress (GMTS) criterion incorporates an additional constant stress term—the T‑stress—and a material-dependent critical distance \(r_c\) to capture these effects. The task is to compute the fracture initiation angles predicted by the GMTS criterion for various mode mixities, specimen types, and specimen sizes, using provided values of \(K_{\mathrm{I}}\), \(K_{\mathrm{II}}\), and \(T\).

## Approach
The GMTS criterion states that fracture initiates at the angle \(\theta_0\) where the tangential stress, given by a series expansion including the T‑stress, attains its maximum at a critical distance \(r_c\) from the crack tip. This leads to the equation

\[
K_{\mathrm{I}} \sin\theta_0 + K_{\mathrm{II}}(3\cos\theta_0 - 1) - \frac{16T}{3}\sqrt{2\pi r_c} \,\cos\theta_0 \sin\frac{\theta_0}{2} = 0.
\]

The critical distance \(r_c\) for the limestone is taken as 2.3 mm.

For each experimental condition (specimen type, size, mode mixity), the corresponding \(K_{\mathrm{I}}, K_{\mathrm{II}}, T\) are supplied in an input CSV. The solver must find the root \(\theta_0\) in the range \([0,\pi]\) radians that satisfies the equation, convert it to degrees, and write the result to a CSV file. A hidden verifier will later compare the computed angles to a reference set to assess correctness.

## Reproduction target
Produce a CSV file, `/app/outputs/theta0_predictions.csv`, that contains one row for every row in the provided input CSV `gmts_inputs.csv`. Each output row must include the columns `specimen`, `size`, `M_e`, and `theta0_deg`, where `theta0_deg` is the fracture initiation angle (in degrees) obtained by solving the GMTS equation above with \(r_c = 2.3\) mm. The input columns are `specimen` (string: “CCCD” or “SCB”), `size` (integer: 1 or 2), `M_e` (float: 1.0, 0.75, 0.5, 0.25, 0.0), `K_I` (MPa√m), `K_II` (MPa√m), and `T` (MPa). No other output files are required.

## Assets

- GMTS input data (K_I, K_II, T)
- SciPy: scipy
- NumPy: numpy
- pandas: pandas

## Workflow steps

### Step 1: Solve GMTS equation for fracture initiation angles
- Role: scored
- Action: Read the provided gmts_inputs.csv containing columns: specimen, size, M_e, K_I, K_II, T. For each row, solve the generalized maximum tangential stress (GMTS) equation: [K_I * sin(θ0) + K_II * (3*cos(θ0) - 1)] - (16*T/3) * √(2π * r_c) * cos(θ0) * sin(θ0/2) = 0, with r_c = 2.3 mm. Use a root-finding method (e.g., scipy.optimize.fsolve) to find θ0 in radians within [0, π] and convert to degrees. Output a CSV file theta0_predictions.csv with columns: specimen, size, M_e, theta0_deg.
- Output file: `/app/outputs/theta0_predictions.csv`
- Format: csv
- Contract: Columns: specimen (string: 'CCCD' or 'SCB'), size (int: 1 or 2), M_e (float: 1.0, 0.75, 0.5, 0.25, 0.0), theta0_deg (float in degrees).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/theta0_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### theta0_predictions.csv
- path: `/app/outputs/theta0_predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted fracture initiation angles (in degrees) from the GMTS criterion for each specimen, size, and mode mixity.
- schema:
  - `type`: table
  - `required_columns`: `specimen`, `size`, `M_e`, `theta0_deg`
  - `units`:
    - `theta0_deg`: degrees

Notes: The checker will compare each row's theta0_deg to the paper's reported GMTS predictions with a hidden tolerance (absolute difference ≤ threshold).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "theta0_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "specimen",
          "size",
          "M_e",
          "theta0_deg"
        ],
        "units": {
          "theta0_deg": "degrees"
        }
      },
      "description": "Predicted fracture initiation angles (in degrees) from the GMTS criterion for each specimen, size, and mode mixity."
    }
  ],
  "notes": "The checker will compare each row's theta0_deg to the paper's reported GMTS predictions with a hidden tolerance (absolute difference ≤ threshold)."
}
```

## How you are scored
A hidden verifier will read your `theta0_predictions.csv` and independently evaluate each row. For each row, the verifier compares your `theta0_deg` to a reference value (the same quantity computed or reported elsewhere, not supplied to you). The per-row error is the absolute difference in degrees. A row passes if the error is within a hidden tolerance; it fails otherwise. The score for this step is the fraction of rows that pass. This score is the sole factor in your reward (weight = 1.0). Reporting a value that matches a published number is not sufficient—you must actually solve the equation to produce the output. The final reward will be a single float in \([0,1]\).
