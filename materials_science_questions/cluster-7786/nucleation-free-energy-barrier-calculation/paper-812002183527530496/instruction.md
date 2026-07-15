# Compute Gibbs Free-Energy Curve for Compound Nucleation in Ternary Solution

## Problem background
Classical homogeneous nucleation theory predicts that the total Gibbs free energy change ΔG as a function of the radius r of a spherical nucleus exhibits only a maximum — the barrier for nucleation. However, when the free energy change of the parent phase is taken into account in a closed system, the ΔG(r) curve can develop a minimum in addition to the maximum. This task investigates this phenomenon for the nucleation of an AB compound from an ideal ternary solution. You will compute ΔG as a function of r and determine whether the curve shows both a maximum and a minimum under the given conditions.

## Approach
We consider the Gibbs free energy change for compound nucleation under constant pressure in a closed A–B–C ternary solution. The total ΔG is composed of:
- a term representing the free energy change of forming the compound nuclei,
- terms accounting for the change in the chemical potential of each component in the parent phase, and
- an interfacial energy term proportional to the total surface area of the nuclei.

The parent phase is an ideal solution. The activities of the components are expressed through their mole fractions and the amount of material transferred to the nuclei. For spherical nuclei with radius r and a total number N of nuclei, the mole number of compound AB in the nuclei and the total surface area are expressed using the molar volume vⁿ and r.

You will numerically sweep r from a very small value (e.g. 1 × 10⁻¹¹ m) upward, compute the parent-phase activities, evaluate ΔG at each step, and stop when the parent-phase activity of component A reaches its saturated activity. The result is a table of (r, ΔG) points that captures the entire nucleation curve.

## Reproduction target
Produce a CSV file `nucleation_curve.csv` containing the complete nucleation curve for the following fixed parameters:
- initial mole fractions: x_A = x_B = 2.5 × 10⁻³
- saturated activities: a_A^sat = a_B^sat = 1.0 × 10⁻³
- molar volume of the compound: vⁿ = 2 × 10⁻⁵ m³ mol⁻¹
- interfacial tension: σ = 0.8 N m⁻¹
- total number of nuclei in 1 mol of the system: N = 10¹⁶
- temperature: T = 1000 K

Sweep the nucleus radius r from a small starting value (e.g. 1 × 10⁻¹¹ m) and increase it in fine steps until the parent-phase activity a_A* reaches its saturated value a_A^sat. The output file must have exactly two columns with the radius r (in meters) and the Gibbs free energy change dG (in Joules), sorted by increasing r. The file may include a header row exactly equal to 'r,dG', or no header at all.

## Assets

- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Compute nucleation free-energy curve
- Role: scored (load-bearing)
- Action: Implement the total Gibbs free energy change equation for AB compound nucleation from an ideal A–B–C ternary solution, using the ideal-solution assumptions and material balances. For spherical nuclei, express the mole number of nuclei and surface area as functions of nucleus radius r and total number of nuclei N. Numerically evaluate ΔG by sweeping r from a small value (e.g., 1e-11 m) upward until the parent-phase activity reaches its saturation value. Output the resulting (r, ΔG) pairs as a CSV file.
- Output file: `/app/outputs/nucleation_curve.csv`
- Format: csv
- Contract: Two columns: 'r' (radius in meters, float) and 'dG' (Gibbs free energy change in Joules, float). Sorted by increasing r. No header row is required; if a header is present, it must be exactly 'r,dG'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_curve.csv
- path: `/app/outputs/nucleation_curve.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The CSV file containing the computed total Gibbs free energy change ΔG versus nucleus radius r. The curve should exhibit a maximum and a minimum. The checker extracts the radius at the minimum and compares the relative error against a hidden reference; meeting or beating the threshold earns full credit.
- schema:
  - `type`: table
  - `required_columns`: `r`, `dG`
  - `units`:
    - `r`: meters
    - `dG`: Joules

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "dG"
        ],
        "units": {
          "r": "meters",
          "dG": "Joules"
        }
      },
      "description": "The CSV file containing the computed total Gibbs free energy change ΔG versus nucleus radius r. The curve should exhibit a maximum and a minimum. The checker extracts the radius at the minimum and compares the relative error against a hidden reference; meeting or beating the threshold earns full credit."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `nucleation_curve.csv` and independently checks the shape of the nucleation curve. It locates the first local maximum (where dG stops increasing) and then seeks the subsequent local minimum (where dG stops decreasing). The verifier extracts the radius r_min at that minimum and compares it against a hidden reference radius. Your reward is based on the presence of the maximum and minimum (structural check) and on the relative error of your extracted r_min compared to the reference; the closer your r_min to the reference, the higher the score, with full credit awarded if the relative error is within a tolerance. The verifier does not require you to match any exact values from the original paper; it judges your result solely against the physics encoded in the reference computation.
