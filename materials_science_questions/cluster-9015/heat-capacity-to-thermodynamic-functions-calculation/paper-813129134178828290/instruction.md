# Thermodynamic function calculation from DSC heat capacity data

## Problem background
Barium cerate doped with holmium and indium is a promising electrolyte material for solid oxide fuel cells. Understanding its thermodynamic properties, such as heat capacity, enthalpy, and entropy, over a range of temperatures is crucial for assessing its stability and performance in operating conditions. This work addresses the experimental determination and computational derivation of these thermodynamic functions from raw differential scanning calorimetry (DSC) measurements.

## Approach
The raw heat capacity data is provided as a CSV file. Over distinct temperature intervals, the heat capacity exhibits smooth behavior that can be described by fitted polynomial functions. Using least-squares fitting, you will fit a cubic polynomial for the interval 200–500 K, a polynomial containing a $1/T^2$ term for 500–573 K, and a quadratic polynomial for 573–700 K. With these piecewise polynomials, you will evaluate Cp at 5 K intervals and numerically integrate Cp from 298.15 K to each temperature to obtain the enthalpy increment, and integrate Cp/T to obtain the absolute entropy, adding the provided standard entropy at 298.15 K to the entropy increment.

## Reproduction target
Your task is to produce a CSV file, `thermodynamic_functions.csv`, containing columns: T (temperature in K), Cp (molar heat capacity in J mol⁻¹ K⁻¹), H_T_minus_H298 (enthalpy increment $H^\circ(T)-H^\circ$ (298.15) in J mol⁻¹), and S_T (absolute molar entropy in J K⁻¹ mol⁻¹). The rows must cover the temperature range from 200 K to 700 K in steps of 5 K. The values must be computed from the fitted polynomials using the provided raw heat capacity data and standard entropy at 298.15 K (136.57 J mol⁻¹ K⁻¹). The final CSV will be evaluated against a hidden reference dataset.

## Assets

- BaCe0.7Ho0.2In0.1O2.85_raw_heat_capacity.csv

## Workflow steps

### Step 1: Fit piecewise polynomial functions to heat capacity data
- Role: process
- Action: Load the raw heat capacity CSV, split the data into three temperature intervals (200–500 K, 500–573 K, 573–700 K). Fit the specified polynomial forms to each interval using least squares. Store the fitted coefficients for later use.
- Evidence: `/app/outputs/fitted_coefficients.json`

### Step 2: Compute smoothed thermodynamic functions
- Role: scored (load-bearing)
- Action: Using the fitted polynomials and the given standard entropy S°(298.15)=136.57 J mol⁻¹ K⁻¹, evaluate Cp from the appropriate polynomial for T=200 to 700 K step 5. Numerically integrate Cp from 298.15 K to each T to obtain H°(T)−H°(298.15), and integrate Cp/T to obtain S°(T). Write results to thermodynamic_functions.csv.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: columns: T (float, K), Cp (float, J mol⁻¹ K⁻¹), H_T_minus_H298 (float, J mol⁻¹), S_T (float, J K⁻¹ mol⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Smoothed thermodynamic functions at 5 K intervals from 200 to 700 K. Columns: temperature T, molar heat capacity Cp, enthalpy increment H°(T)−H°(298.15), and absolute molar entropy S°(T).
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp`, `H_T_minus_H298`, `S_T`
  - `units`:
    - `T`: K
    - `Cp`: J mol⁻¹ K⁻¹
    - `H_T_minus_H298`: J mol⁻¹
    - `S_T`: J K⁻¹ mol⁻¹

Notes: The hidden reference values are from Tables 5 and 6 of the paper, used only for scoring. The standard entropy at 298.15 K is provided in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp",
          "H_T_minus_H298",
          "S_T"
        ],
        "units": {
          "T": "K",
          "Cp": "J mol⁻¹ K⁻¹",
          "H_T_minus_H298": "J mol⁻¹",
          "S_T": "J K⁻¹ mol⁻¹"
        }
      },
      "description": "Smoothed thermodynamic functions at 5 K intervals from 200 to 700 K. Columns: temperature T, molar heat capacity Cp, enthalpy increment H°(T)−H°(298.15), and absolute molar entropy S°(T)."
    }
  ],
  "notes": "The hidden reference values are from Tables 5 and 6 of the paper, used only for scoring. The standard entropy at 298.15 K is provided in the instruction."
}
```

## How you are scored
The evaluation is performed automatically by a hidden verifier. The verifier inspects your output CSV and compares the computed Cp, H_T_minus_H298, and S_T values against previously established reference values for the same compound. Each of these three quantities is compared with acceptable tolerances that reflect legitimate numerical and implementation differences. Only submissions that correctly implement the fitting and integration pipeline will achieve high scores. Additionally, the verifier may check that the output file conforms to the required format and that the enthalpy and entropy are physically plausible (e.g., monotonic). The evidence from the polynomial fitting step is not directly scored but is necessary to produce the final scored artifact. The final reward is a weighted combination of these checks, with primary weight on the accuracy of the thermodynamic function values.
