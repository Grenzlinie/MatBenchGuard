# Classical Nucleation Theory with Tolman and Power-Law Surface Tension

## Problem background
In classical nucleation theory the free‑energy barrier for droplet formation is evaluated via the capillary approximation, where the surface tension of a bulk liquid is assumed constant. Observations of homogeneous nucleation of water vapour, however, suggest that a larger free‑energy barrier than predicted by a constant surface tension is needed, so attention has turned to surface‑tension values that depend on the radius of curvature. This task computes, for two commonly studied functional forms of σ(r), the critical radius ratio a/r* and the surface‑tension ratio σ(r*)/σ₀ that satisfy a given free‑energy ratio ΔF/ΔF⁰ = 1.6, a value identified with cloud‑chamber measurements for water vapour. The challenge is to solve the exact implicit equations that result from integrating the Gibbs‑Duhem relation with a variable surface tension.

## Approach
The thermodynamic treatment follows the standard procedure of inserting an assumed σ(r) into the differential Gibbs‑Duhem relation for a spherical drop, integrating from the bulk limit to the critical radius, and using the equilibrium condition and Laplace's equation to eliminate the supersaturation. This yields an implicit relation that must be solved numerically for the dimensionless root a/r* at the given free‑energy ratio. Once a/r* is known, σ(r*)/σ₀ is obtained directly from the assumed σ(r) expression. Two functional forms are examined: (i) the Tolman form σ(r) = σ₀/(1 + a/r), which leads to a single equation; (ii) a general power‑law σ(r) = σ₀[1 + (a/r)ᵐ] with positive sign and integer m = 1,…,10. For each form the condition ΔF/ΔF⁰ = 1.6 is enforced, and the resulting a/r* and σ(r*)/σ₀ are computed using standard numerical root‑finding (e.g., scipy.optimize). No external dataset is needed; the entire procedure is driven by the specified formulas and the fixed free‑energy ratio.

## Reproduction target
Produce the following two outputs under the condition ΔF/ΔF⁰ = 1.6:

- For the Tolman surface‑tension form, numerically solve for the dimensionless root a/r* and the corresponding surface‑tension ratio σ(r*)/σ₀. Write the result to `tolman_results.json`.

- For the general power‑law form with positive sign, compute a/r* and σ(r*)/σ₀ for each integer exponent m from 1 to 10. Write the results to `general_power_table.csv`.

The outputs will be compared against independently calculated reference values.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Solve Tolman form
- Role: scored (load-bearing)
- Action: Implement the exact implicit relation between supersaturation and critical radius for the Tolman surface-tension form σ(r)=σ₀/(1+a/r) (derived from the integrated Gibbs-Duhem relation and equilibrium condition) and the corresponding free-energy ratio expression. Solve numerically for the dimensionless root a/r* under the condition ΔF/ΔF⁰ = 1.6. Compute σ(r*)/σ₀ from the Tolman form. Write the results to tolman_results.json.
- Output file: `/app/outputs/tolman_results.json`
- Format: json
- Contract: {"a_over_rstar": <float>, "sigma_over_sigma0": <float>}
- Scoring: scored by hidden verifier

### Step 2: Solve general power-law forms
- Role: scored
- Action: Implement the exact relation for a general power-law surface-tension form σ(r)=σ₀[1 + (a/r)^m] with positive sign, derived from the same thermodynamic integration. For each integer m from 1 to 10, solve the equation for a/r* given ΔF/ΔF⁰ = 1.6, then compute σ(r*)/σ₀ = 1 + (a/r*)^m. Write the results as a CSV table general_power_table.csv.
- Output file: `/app/outputs/general_power_table.csv`
- Format: csv
- Contract: columns: m (int), a_over_rstar (float), sigma_over_sigma0 (float); one row per m=1..10.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tolman_results.json`
- `/app/outputs/general_power_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tolman_results.json
- path: `/app/outputs/tolman_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dimensionless root a/r* and surface tension ratio σ(r*)/σ₀ for the Tolman form at ΔF/ΔF⁰ = 1.6. Both values are fixed by the equation and condition.
- schema:
  - `type`: object
  - `required`:
    - `a_over_rstar`: float
    - `sigma_over_sigma0`: float

### general_power_table.csv
- path: `/app/outputs/general_power_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Solved a/r* and σ/σ₀ for integer exponents m=1..10 of the power-law surface-tension dependence at ΔF/ΔF⁰ = 1.6. Each row corresponds to one m.
- schema:
  - `type`: table
  - `required_columns`: `m`, `a_over_rstar`, `sigma_over_sigma0`
  - `items`:
    - `m`: int
    - `a_over_rstar`: float
    - `sigma_over_sigma0`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tolman_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a_over_rstar": "float",
          "sigma_over_sigma0": "float"
        }
      },
      "description": "Dimensionless root a/r* and surface tension ratio σ(r*)/σ₀ for the Tolman form at ΔF/ΔF⁰ = 1.6. Both values are fixed by the equation and condition."
    },
    {
      "file": "general_power_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "a_over_rstar",
          "sigma_over_sigma0"
        ],
        "items": {
          "m": "int",
          "a_over_rstar": "float",
          "sigma_over_sigma0": "float"
        }
      },
      "description": "Solved a/r* and σ/σ₀ for integer exponents m=1..10 of the power-law surface-tension dependence at ΔF/ΔF⁰ = 1.6. Each row corresponds to one m."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier evaluates each scored artifact independently. The verifier reads your `tolman_results.json` and `general_power_table.csv` and compares the numbers you report to the expected values that satisfy the given ΔF/ΔF⁰ = 1.6 condition. Both artifacts contribute to a single numeric reward between 0 and 1; simply stating the required values without performing the numerical solution will not earn full credit. The verifier does not re‑run the root‑finding; it checks only the final numeric outputs using appropriate tolerances.
