# Compute Hellmann Potential Parameters and Molecular Constants for Alkali Hydrides

## Problem background
Alkali hydride diatomic molecules (LiH, NaH, KH, RbH, CsH) exhibit a mixture of ionic and covalent binding. Understanding their ground-state potential energy curves is central to validating models of interatomic interactions. A class of "ionic" potentials that includes the Coulomb attraction term -e^2/r plus a repulsive term has been proposed to describe these molecules. One such model is the Hellmann potential, which introduces an exponential repulsive factor: U = -e^2/r + T exp(-λ r)/r, with parameters T and λ. This task computes the Hellmann potential parameters and the resulting molecular constants (rotational-vibrational coupling α_e, anharmonicity ω_e x_e, and ionic binding energy D_i) for the five alkali hydrides from known experimental constants, and compares them against experimental references to evaluate the model's performance.

## Approach
The Hellmann potential parameters are determined by applying the equilibrium conditions dU/dr = 0 and d²U/dr² = k_e at the equilibrium bond length r_e, where k_e is the experimental force constant. These conditions lead to expressions that relate the dimensionless parameter y = λ r_e to measurable quantities:

  y² / (y + 1) = k_e r_e³ / e².

From y, λ = y / r_e.

The molecular constants are then derived from the potential:
- Rotational constant B_e: B_e = h/(8π² c μ r_e²), where μ is the reduced mass in atomic mass units.
- α_e = (y/3) * 6 B_e² / ω_e.
- ω_e x_e = (1/3)(2 y² + 18 y + 9) * W / (μ_A r_e²), with the constant W = 2.1078 × 10⁻¹⁶ (units consistent with cm⁻¹).
- Ionic binding energy D_i = [y/(y+1)] * e²/r_e, converted to kcal/mol using the electronic charge e = 4.80325 × 10⁻¹⁰ esu and Avogadro's number.

The experimental reference data for the five molecules (ω_e, k_e, r_e, α_e_obs, ω_e x_e_obs, D_i_obs) are provided in the workflow steps. The task is to implement these formulas, compute y, λ, α_e, ω_e x_e, and D_i for each molecule, and calculate the percentage errors relative to the observed values.

## Reproduction target
For the five alkali hydrides LiH, NaH, KH, RbH, and CsH, using the experimental molecular constants given in Step 1:
1. Compute y (dimensionless) from y²/(y+1) = k_e r_e³ / e².
2. Compute λ = y / r_e (in units of 10⁸ cm⁻¹).
3. Compute α_e_calc, ω_e_x_e_calc, and D_i_calc from the Hellmann model formulas.
4. For each constant, compute the percentage error relative to the observed value:
   %error = 100 * (calc - obs) / obs.

Write all results to the output file hellmann_results.csv with the following columns:
molecule, y, lambda, alpha_calc, alpha_error_percent, omega_x_calc, omega_x_error_percent, Di_calc, Di_error_percent.

After the five molecular rows, add a final row with molecule = 'mean' and lambda = the arithmetic mean of the five λ values; all other numeric columns in that row should be set to 0 or empty.

All numeric values must be computed to the full precision supported by the input constants.

## Assets
The experimental constants for the five molecules are provided in Step 1; no external dataset downloads are needed.

The computation requires a Python environment with numpy (and optionally scipy for root finding). Physical constants needed:
- Electronic charge e = 4.80325 × 10⁻¹⁰ esu
- Avogadro's number N_A = 6.02214076 × 10²³ mol⁻¹
- Planck's constant h = 6.62607015 × 10⁻²⁷ erg·s
- Speed of light c = 2.99792458 × 10¹⁰ cm/s
- Conversion factor W = 2.1078 × 10⁻¹⁶ (for ω_e x_e formula, yielding cm⁻¹)
- Reduced masses μ in amu, computed from atomic masses: H = 1.008, Li = 6.94, Na = 22.99, K = 39.10, Rb = 85.47, Cs = 132.91.

All are publicly known constants; no separate licenses are required.

## Workflow steps

### Step 1: Compile experimental reference data
- Role: process
- Action: Create a CSV file (experimental_data.csv) containing the experimental molecular constants from Table I: molecule, omega_e (cm⁻¹), k_e (10⁵ dyn/cm), r_e (10⁻⁸ cm), alpha_e_obs (cm⁻¹), omega_e_x_e_obs (cm⁻¹), D_i_obs (kcal/mol). The values are provided in the instruction.
- Evidence: `/app/outputs/experimental_data.csv`

### Step 2: Compute Hellmann potential parameters and molecular constants
- Role: scored (load-bearing)
- Action: For each molecule (LiH, NaH, KH, RbH, CsH), use the experimental reference data to: (1) compute y = lambda * r_e from y^2/(y+1) = k_e * r_e^3 / e^2; (2) compute lambda = y / r_e; (3) compute alpha_e, omega_e x_e, and D_i from the Hellmann model formulas; (4) calculate percentage errors relative to the observed values. Write the results to hellmann_results.csv, with a final row giving the mean lambda across the series.
- Output file: `/app/outputs/hellmann_results.csv`
- Format: csv
- Contract: Columns: molecule (LiH,NaH,KH,RbH,CsH), y (dimensionless), lambda (10^8 cm⁻¹), alpha_calc (cm⁻¹), alpha_error_percent, omega_x_calc (cm⁻¹), omega_x_error_percent, Di_calc (kcal/mol), Di_error_percent. The last row has molecule='mean', lambda = mean lambda, other columns empty/0 except lambda.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hellmann_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hellmann_results.csv
- path: `/app/outputs/hellmann_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed Hellmann parameters and molecular constants for the five alkali hydrides, including percentage errors relative to experimental references; the last row gives the mean lambda. The checker compares the computed y, lambda, alpha_calc, omega_x_calc, and Di_calc to the paper's reported values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `y`, `lambda`, `alpha_calc`, `alpha_error_percent`, `omega_x_calc`, `omega_x_error_percent`, `Di_calc`, `Di_error_percent`
  - `units`:
    - `molecule`: string (LiH, NaH, KH, RbH, CsH, or 'mean')
    - `y`: dimensionless
    - `lambda`: 10^8 cm⁻¹
    - `alpha_calc`: cm⁻¹
    - `alpha_error_percent`: %
    - `omega_x_calc`: cm⁻¹
    - `omega_x_error_percent`: %
    - `Di_calc`: kcal/mol
    - `Di_error_percent`: %

Notes: The percentage errors are computed relative to the provided experimental constants; their correctness is used as a secondary check. The mean lambda is compared to the paper's reported value. No external datasets are required beyond the hardcoded constants.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hellmann_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "y",
          "lambda",
          "alpha_calc",
          "alpha_error_percent",
          "omega_x_calc",
          "omega_x_error_percent",
          "Di_calc",
          "Di_error_percent"
        ],
        "units": {
          "molecule": "string (LiH, NaH, KH, RbH, CsH, or 'mean')",
          "y": "dimensionless",
          "lambda": "10^8 cm⁻¹",
          "alpha_calc": "cm⁻¹",
          "alpha_error_percent": "%",
          "omega_x_calc": "cm⁻¹",
          "omega_x_error_percent": "%",
          "Di_calc": "kcal/mol",
          "Di_error_percent": "%"
        }
      },
      "description": "Computed Hellmann parameters and molecular constants for the five alkali hydrides, including percentage errors relative to experimental references; the last row gives the mean lambda. The checker compares the computed y, lambda, alpha_calc, omega_x_calc, and Di_calc to the paper's reported values within tolerance."
    }
  ],
  "notes": "The percentage errors are computed relative to the provided experimental constants; their correctness is used as a secondary check. The mean lambda is compared to the paper's reported value. No external datasets are required beyond the hardcoded constants."
}
```

## How you are scored
A hidden verifier reads your hellmann_results.csv and compares the computed quantities against reference values derived from the Hellmann model. It checks:
- The dimensionless parameter y, the repulsion constant λ, the computed molecular constants α_e_calc, ω_e_x_calc, and D_i_calc for each molecule against precise reference values.
- The correctness of the percentage error calculations.
- The mean λ against the expected value.

The comparisons use tight tolerances appropriate for the deterministic analytical formulas. The file must adhere exactly to the specified column names, units, and order; deviations will cause the verifier to reject the artifact. The final reward is a weighted combination of these checks.
