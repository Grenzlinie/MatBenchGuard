# Isothermal heat exchange of Mooney-Rivlin-Besseling body under finite deformations

## Problem background
When an elastic body undergoes finite, homogeneous, isothermal deformations, heat flows between the body and its surroundings. The amount of heat exchanged can be determined from the material's entropy. This task focuses on a non-linear elastic material, the Mooney-Rivlin-Besseling body, for which closed-form expressions for the isothermal heat exchange have been derived. The goal is to compute these heat values for three distinct deformation modes: pure volume change, simple shear, and isochoric shape change without shear. Two sets of material constants (A and B) are considered, reflecting materials that exhibit qualitatively different volumetric behaviour under tension.

## Approach
The heat exchange W (in J/kg) for each deformation is given by an analytic expression that depends on the deformation parameter (stretch ratio λ or shear parameter p) and the material constants. The computation is purely numerical: evaluate these expressions for a prescribed list of deformation parameter values, using the two sets of material constants, and record the results in a CSV file. No external data or complex numerical methods are required; the built-in mathematics and CSV modules of Python's standard library suffice.

## Reproduction target
Compute the isothermal heat exchange W (J/kg) for the Mooney-Rivlin-Besseling body under three deformation types: pure volume change, simple shear, and isochoric shape change without shear. Use the following material constants: c1 = 0.28, γ = 1.5, cE = 1.622 × 10³ J/(kg·K), T0 = 303 K. For material set A: c3 = 0.8683 × 10⁻³, β2 = -0.0288. For material set B: c3 = 1.0829 × 10⁻³, β2 = 0.0689. For volume and shape deformations, evaluate the heat for stretch ratio λ in {0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2}. For shear deformation, evaluate for shear parameter p in {0.0, 0.2, 0.4, 0.6, 0.8, 1.0}. Produce a CSV file `heat_curves.csv` with columns: `deformation` (string: `volume`, `shear`, or `shape`), `material` (string: `A` or `B`), `parameter` (float, λ or p), `W` (float, J/kg). Include exactly one row for each combination of deformation type, material set, and parameter value.

## Assets

- Python 3 standard library: https://www.python.org/

## Workflow steps

### Step 1: Compute isothermal heat exchange curves
- Role: scored (load-bearing)
- Action: Evaluate the analytic heat exchange formulas for the Mooney-Rivlin-Besseling body under three deformation types: pure volume change, simple shear, and isochoric shape change without shear. Use the material constants provided in the task description: c1=0.28, γ=1.5, cE=1.622e3 J/(kg·K), T0=303 K; for material A: c3=0.8683e-3, β2=-0.0288; for material B: c3=1.0829e-3, β2=0.0689. Compute the heat W (J/kg) for stretch ratio λ ∈ {0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2} for volume and shape changes, and for shear parameter p ∈ {0.0, 0.2, 0.4, 0.6, 0.8, 1.0} for shear deformation. Write a CSV file with one row per combination.
- Output file: `/app/outputs/heat_curves.csv`
- Format: csv
- Contract: Columns: deformation (string, one of 'volume', 'shear', 'shape'), material (string, 'A' or 'B'), parameter (float, λ or p), W (float, J/kg).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heat_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heat_curves.csv
- path: `/app/outputs/heat_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Recomputed isothermal heat exchange values for the Mooney-Rivlin-Besseling body under three deformation types. The checker will re-evaluate the same analytic formulas using the same material constants and parameter values, then compare each W value against the agent's submission with absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `deformation`, `material`, `parameter`, `W`
  - `units`:
    - `parameter`: dimensionless
    - `W`: J/kg

Notes: The linear-elastic body (Section 2a) is omitted per taskability scope. The formulas for the Mooney-Rivlin-Besseling body are those derived in the paper: for pure volume change W = -c_E T_0 log(1 + c1(λ^{-6γ} - 1)); for simple shear W = -c_E T_0 log(1 + (c3/3) p^2); for isochoric shape change without shear W = -c_E T_0 log(1 + (c3/3)[(½+β2)(λ²+2/λ) + (½-β2)(2λ+1/λ²) - 3]). Only the constants and parameter sets stated in the step action are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heat_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "deformation",
          "material",
          "parameter",
          "W"
        ],
        "units": {
          "parameter": "dimensionless",
          "W": "J/kg"
        }
      },
      "description": "Recomputed isothermal heat exchange values for the Mooney-Rivlin-Besseling body under three deformation types. The checker will re-evaluate the same analytic formulas using the same material constants and parameter values, then compare each W value against the agent's submission with absolute tolerance."
    }
  ],
  "notes": "The linear-elastic body (Section 2a) is omitted per taskability scope. The formulas for the Mooney-Rivlin-Besseling body are those derived in the paper: for pure volume change W = -c_E T_0 log(1 + c1(λ^{-6γ} - 1)); for simple shear W = -c_E T_0 log(1 + (c3/3) p^2); for isochoric shape change without shear W = -c_E T_0 log(1 + (c3/3)[(½+β2)(λ²+2/λ) + (½-β2)(2λ+1/λ²) - 3]). Only the constants and parameter sets stated in the step action are required."
}
```

## How you are scored
A hidden checker independently recomputes the correct heat values using the same formulas and constants, then reads your `heat_curves.csv`. For each row, it compares your reported W against the recomputed gold value using an absolute tolerance. Full credit is awarded if every row satisfies the tolerance; partial credit may be given if only some rows pass. The tolerance is set to allow for minor numerical rounding differences but is tight enough that only correct evaluation passes. You do not need to know the exact tolerance; it is hidden. Simply providing numbers without performing the computation will not succeed.
