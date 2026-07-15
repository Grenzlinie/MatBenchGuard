# Silicalite low-temperature thermodynamic functions from heat capacity

## Problem background
Silicalite, a pure SiO₂ molecular sieve, is of interest for its thermodynamic properties and potential as a thermochemical reference substance. Low-temperature adiabatic calorimetry (5–350 K) provides the molar heat capacity as a function of temperature. From these experimental data, standard molar thermodynamic functions — heat capacity, entropy change, and enthalpy increment — can be derived by polynomial fitting and numerical integration. This task targets the computational determination of these derived quantities at the reference temperature 298.15 K using the published heat‑capacity measurements.

## Approach
The experimental molar heat capacity data (dimensionless Cp/R versus mean temperature) are provided. The analysis proceeds in two main stages. First, weighted least‑squares polynomial fitting is performed separately on low‑temperature (below 40 K) and high‑temperature (above 20 K) subsets, ensuring a smooth merge of the two polynomials near 25.6 K. Below 5 K, the heat capacity is extrapolated to 0 K using the Debye T³ law (C ∝ T³). Second, the fitted polynomials and the low‑temperature extrapolation are integrated numerically: Cp/T is integrated to obtain the standard molar entropy change Δ₀ᵗSₘ°, and Cp is integrated to obtain the enthalpy increment Δ₀ᵗHₘ°, both as functions of temperature. The results at 298.15 K are reported in dimensionless form.

## Reproduction target
Using the raw heat‑capacity data (file `silicalite_heat_capacity_data.csv`), produce:

1. **Fitted polynomial coefficients** — the coefficients (ascending order) of the two weighted least‑squares polynomials that represent the experimental Cp data, stored as `fitted_polynomial_coefficients.json`.
2. **Thermodynamic functions at 298.15 K** — the standard molar heat capacity (Cp/R), entropy change (Δ₀ᵗSₘ°/R), and enthalpy increment (Δ₀ᵗHₘ°/(R·K)) in dimensionless form, written as one CSV row in `thermodynamic_functions_298.15.csv`.

The target is to obtain these quantities entirely from the provided data and the described fitting, extrapolation, and integration procedure, without relying on external thermodynamic tables.

## Assets

- silicalite_heat_capacity_data.csv
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Load and prepare heat capacity data
- Role: process
- Action: Load the raw heat capacity data from the provided silicalite_heat_capacity_data.csv. Separate the data into low-temperature (mean temperature < 40 K) and high-temperature (mean temperature > 20 K) subsets for independent polynomial fitting. Prepare the data arrays for weighted least-squares fitting.
- Evidence: none

### Step 2: Fit heat-capacity polynomials
- Role: scored (load-bearing)
- Action: Perform weighted least-squares polynomial fitting of the experimental C_p / R data as a function of mean temperature. Fit two separate polynomials: one valid for T < 40 K, another valid for T > 20 K, with a smooth merge near 25.6 K. Output the polynomial coefficients in ascending order (constant term first).
- Output file: `/app/outputs/fitted_polynomial_coefficients.json`
- Format: json
- Contract: JSON object with keys 'low_T_poly' (array of floats, coefficients in ascending order for T < 40 K) and 'high_T_poly' (array of floats, coefficients for T > 20 K).
- Scoring: scored by hidden verifier

### Step 3: Compute thermodynamic functions at 298.15 K
- Role: scored
- Action: Starting from the fitted polynomials and a Debye T³ extrapolation of the heat capacity below 5 K, numerically integrate C_p / T and C_p to obtain the standard molar entropy change Δ₀ᵗ Sₘ° and enthalpy increment Δ₀ᵗ Hₘ° as functions of temperature. Report the values at T = 298.15 K in dimensionless form (C_p / R, Δ₀ᵗ Sₘ° / R, Δ₀ᵗ Hₘ° / (R·K)).
- Output file: `/app/outputs/thermodynamic_functions_298.15.csv`
- Format: csv
- Contract: CSV file with header: T, Cp_m_R, DeltaS_R, DeltaH_R_K. Contains one data row with T=298.15 and the computed dimensionless values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_polynomial_coefficients.json`
- `/app/outputs/thermodynamic_functions_298.15.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_polynomial_coefficients.json
- path: `/app/outputs/fitted_polynomial_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polynomial coefficients obtained from weighted least-squares fitting of experimental heat capacity data. The checker evaluates these polynomials at hidden temperatures and compares the resulting Cp/R to the paper's reference values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `low_T_poly`: array of floats (coefficients ascending order for T < 40 K)
    - `high_T_poly`: array of floats (coefficients ascending order for T > 20 K)

### thermodynamic_functions_298.15.csv
- path: `/app/outputs/thermodynamic_functions_298.15.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Standard molar heat capacity, entropy change, and enthalpy increment at 298.15 K derived by integration of the fitted polynomials and Debye extrapolation. Compared to paper-reported values with relative tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp_m_R`, `DeltaS_R`, `DeltaH_R_K`
  - `units`:
    - `T`: K
    - `Cp_m_R`: dimensionless
    - `DeltaS_R`: dimensionless
    - `DeltaH_R_K`: dimensionless (ΔH/(R·K))

Notes: The checker recomputes the fitting from the same raw data and integrates to obtain reference values. The agent's artifacts are compared to these reference values within tolerances. The high-temperature enthalpy, combustion, and reaction calorimetry sections are excluded from this reproduction scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_polynomial_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "low_T_poly": "array of floats (coefficients ascending order for T < 40 K)",
          "high_T_poly": "array of floats (coefficients ascending order for T > 20 K)"
        }
      },
      "description": "Polynomial coefficients obtained from weighted least-squares fitting of experimental heat capacity data. The checker evaluates these polynomials at hidden temperatures and compares the resulting Cp/R to the paper's reference values with tolerance."
    },
    {
      "file": "thermodynamic_functions_298.15.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp_m_R",
          "DeltaS_R",
          "DeltaH_R_K"
        ],
        "units": {
          "T": "K",
          "Cp_m_R": "dimensionless",
          "DeltaS_R": "dimensionless",
          "DeltaH_R_K": "dimensionless (ΔH/(R·K))"
        }
      },
      "description": "Standard molar heat capacity, entropy change, and enthalpy increment at 298.15 K derived by integration of the fitted polynomials and Debye extrapolation. Compared to paper-reported values with relative tolerances."
    }
  ],
  "notes": "The checker recomputes the fitting from the same raw data and integrates to obtain reference values. The agent's artifacts are compared to these reference values within tolerances. The high-temperature enthalpy, combustion, and reaction calorimetry sections are excluded from this reproduction scope."
}
```

## How you are scored
A hidden verifier independently performs the same weighted least‑squares fitting and numerical integration on the same raw Cp data, producing its own reference polynomial coefficients and 298.15 K values. Your submitted `fitted_polynomial_coefficients.json` is scored by evaluating its polynomials at a set of hidden temperatures and comparing the resulting Cp/R to the verifier’s reference values. Your `thermodynamic_functions_298.15.csv` is scored by comparing the three dimensionless quantities against the reference values. The reward from the two stages is combined by weight (the coefficient artifact and the 298.15 K functions both carry significant weight). No single reported number is sufficient; the verifier checks that your artifacts are consistent with a correct execution of the described workflow within acceptable tolerances.
