# Asymptotic Phase Retardance of Thin Grid Polarizer

## Problem background
Wire-grid polarizers transmit one linear polarization and reflect the orthogonal one. Their performance is normally given by the extinction ratio, but a complete description also requires the relative phase retardance Δ between the two transmitted components. This work computes the relative phase retardance for an infinitely-thin wire-grid polarizer situated at the boundary between a support medium of refractive index 2.2 and vacuum (n=1). The goal is to determine how the retardance depends on the grating period-to-wavelength ratio a/λ and on the conductor-width to period ratio d/a across a range of conditions. The computed retardance values are to be collected into a single scored artifact for structural verification.

## Approach
The grating is treated as an infinitely thin plane at the interface between two semi-infinite media: the support (refractive index 2.2) and free space (refractive index 1). The method uses the well-known Marcuvitz complex impedance formulas for a plane grating of negligible thickness. These formulas give the complex impedance for the two orthogonal linear polarizations—electric field parallel to the grating wires and electric field perpendicular to the wires. The complex transmission coefficients for each polarization are then obtained from the impedances, properly accounting for the different refractive indices on either side of the grating. Finally, the relative phase retardance Δ is computed as the difference of the phases of the two complex transmission coefficients: Δ = arg(T_perp) − arg(T_par). The computation is carried out over a logarithmically spaced grid of a/λ values for several fixed ratios d/a.

## Reproduction target
Compute the relative phase retardance Δ (in radians) for a thin grid polarizer on a support of refractive index 2.2. Produce a CSV file `delta_vs_a_lambda.csv` containing Δ as a function of the dimensionless grating-period-to-wavelength ratio a/λ for four conductor-width-to-period ratios: d/a = 0.2, 0.4, 0.6, and 0.8. The a/λ axis must be sampled logarithmically from 0.001 to 1.0 with at least 50 distinct points per d/a value. The hidden verifier will check the structure of the submitted data: it will verify that Δ follows the expected asymptotic trend as a/λ becomes small and that the values remain within a prescribed bound for all a/λ ≤ 0.5. The checks are structural—no external reference numbers are needed beyond the data itself.

## Assets

- Marcuvitz complex impedance formulas for plane grating (Waveguide Handbook, MIT Rad. Lab. Series, 1951, p. 280)

## Workflow steps

### Step 1: Compute complex transmission coefficients for the two polarizations
- Role: process
- Action: Implement the Marcuvitz complex impedance formulas for an infinitely thin plane grating situated at the boundary between two semi-infinite media of refractive indices 2.2 (support) and 1.0 (air). Compute the complex amplitude transmission coefficients for the two orthogonal linear polarizations (electric field parallel and perpendicular to the grid wires) as functions of the ratios a/λ and d/a.
- Evidence: none

### Step 2: Calculate relative phase retardance Δ and write CSV
- Role: scored (load-bearing)
- Action: Using the transmission coefficients from step 00, compute the relative phase retardance Δ = arg(T_perp) - arg(T_par) (radians). Evaluate Δ for a logarithmically spaced grid of a/λ from 0.001 to 1.0 (at least 50 distinct points) and for d/a values of 0.2, 0.4, 0.6, and 0.8. Write the results to delta_vs_a_lambda.csv.
- Output file: `/app/outputs/delta_vs_a_lambda.csv`
- Format: csv
- Contract: Columns: a_lambda (float, dimensionless ratio of grating period to wavelength), d_a (float, dimensionless ratio of conductor width to grating period), Delta (float, relative phase retardance in radians). No header row is required but recommended. At least 50 rows per d_a value, covering a_lambda in logarithmic steps from 0.001 to 1.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_vs_a_lambda.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_vs_a_lambda.csv
- path: `/app/outputs/delta_vs_a_lambda.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Relative phase retardance Δ as a function of grating period/wavelength ratio (a/λ) and conductor width/period ratio (d/a). The checker will verify monotonic convergence to -π/2 as a/λ decreases and that |Δ + π/2| ≤ 0.15·(π/2) for all a/λ ≤ 0.5.
- schema:
  - `type`: table
  - `required_columns`: `a_lambda`, `d_a`, `Delta`
  - `units`:
    - `a_lambda`: dimensionless ratio
    - `d_a`: dimensionless ratio
    - `Delta`: radians

Notes: Structural audit verifies the asymptotic behaviour and the 10% bound without recomputing the underlying transmission coefficients.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_vs_a_lambda.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "a_lambda",
          "d_a",
          "Delta"
        ],
        "units": {
          "a_lambda": "dimensionless ratio",
          "d_a": "dimensionless ratio",
          "Delta": "radians"
        }
      },
      "description": "Relative phase retardance Δ as a function of grating period/wavelength ratio (a/λ) and conductor width/period ratio (d/a). The checker will verify monotonic convergence to -π/2 as a/λ decreases and that |Δ + π/2| ≤ 0.15·(π/2) for all a/λ ≤ 0.5."
    }
  ],
  "notes": "Structural audit verifies the asymptotic behaviour and the 10% bound without recomputing the underlying transmission coefficients."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored workflow step and combine the results into a final reward between 0 and 1. For this task, the primary scored artifact is the CSV file produced in step 2. The verifier will read the file, validate its format and required columns, group the data by d/a, and perform structural checks on the Delta column for each group. It does not compare your numbers directly to any pre‑recorded “gold” values; instead, it examines the trends and bounds present in your data. The checks are designed to pass when the underlying physics is captured correctly by the implementation, so simply reporting numbers that “look right” without a faithful computation will not succeed. The final reward reflects both the structural validity of the CSV and the correctness of the trends it exhibits.
