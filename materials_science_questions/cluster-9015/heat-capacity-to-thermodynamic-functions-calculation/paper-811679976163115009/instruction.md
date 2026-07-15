# Thermodynamic data extrapolation using Lorentz approximation

## Problem background
Accurate low-temperature thermodynamic data are essential for modelling cryogenic and geochemical processes, but experimental heat capacities below 300 K are scarce. The Lorentz (L) approximation, Cp(T) = a(1 − 1/(1 + b T²)) + c T, has the correct limit Cp(0) = 0 and can be used to extrapolate heat capacities known above 298.15 K to temperatures near absolute zero. This work investigates which temperature range above 298.15 K, when used to fit the L approximation, yields the most accurate low-temperature extrapolations for two example compounds, enabling consistent calculation of entropy, enthalpy, and Gibbs energy.

## Approach
Isobaric heat capacity data Cp(T) for LiBO₂ and BaS are obtained from the JANAF thermochemical tables. For each compound, the Lorentz equation is fitted by non-linear least-squares over several temperature intervals that start at 298.15 K and extend to different upper limits: 700 K, 1000 K, 1500 K, and 2000 K; additionally, LiBO₂ is fitted to its phase-transition temperature (1117 K) and BaS is fitted up to 3000 K. For each fit, the resulting equation is evaluated at low temperatures (100 K, 200 K, and 298.15 K) and the predicted heat capacities are compared with the JANAF benchmark values at those temperatures. The mean square deviation Δ and the correlation coefficient R quantify the extrapolation accuracy for each interval, allowing the relative performance of the different temperature ranges to be compared.

## Reproduction target
For the two compounds LiBO₂ and BaS, use JANAF Cp data to non-linearly fit the L approximation Cp(T)=a(1 − 1/(1 + b T²)) + c T over the temperature intervals 298.15–700 K, 298.15–1000 K, 298.15–1500 K, and 298.15–2000 K. Additionally fit LiBO₂ over 298.15–1117 K, and BaS over 298.15–3000 K. For each fit, record the coefficients a, b, c, compute the predicted Cp at T = 100 K, 200 K, and 298.15 K, and calculate the mean square deviation Δ and correlation coefficient R between these predicted values and the JANAF benchmark Cp values at the same three temperatures. Output all results in the single CSV file specified in the workflow steps.

## Assets

- JANAF Thermochemical Tables (3rd ed.): https://janaf.nist.gov/
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Extract JANAF heat capacity data
- Role: process
- Action: Extract isobaric heat capacity Cp(T) data for compounds LiBO₂ and BaS from JANAF thermochemical tables (or equivalent public source). Include all temperatures from 100 K up to 3000 K. Save the extracted data as a CSV file (janaf_data.csv) with columns: compound (str), T (K, numeric), Cp (J/(mol·K), numeric).
- Evidence: `/app/outputs/janaf_data.csv`

### Step 2: Fit L approximation and evaluate extrapolation accuracy
- Role: scored (load-bearing)
- Action: Using the extracted Cp data, for each compound LiBO₂ and BaS: (a) Perform non-linear least-squares fitting of the Lorentz approximation Cp(T) = a*(1 - 1/(1 + b*T^2)) + c*T over the temperature intervals 298.15–700 K, 298.15–1000 K, 298.15–1500 K, 298.15–2000 K. Additionally for LiBO₂ fit over 298.15–1117 K, and for BaS over 298.15–3000 K. (b) For each fit, record the coefficients a, b, c and use the fitted equation to compute predicted Cp at T = 100 K, 200 K, 298.15 K. (c) Compute the mean square deviation Δ and correlation coefficient R between the predicted Cp values at those three temperatures and the corresponding JANAF benchmark Cp values (also extracted at those temperatures). Output a single CSV file with all results.
- Output file: `/app/outputs/step_02_results.csv`
- Format: csv
- Contract: CSV with columns: compound (str), interval_start (K, numeric), interval_end (K, numeric), a (J/(mol·K), numeric), b (1/K^2, numeric), c (J/(mol·K^2), numeric), Cp_100 (J/(mol·K), numeric), Cp_200 (J/(mol·K), numeric), Cp_298 (J/(mol·K), numeric), Delta (J^2/(mol^2·K^2), numeric), R (dimensionless, numeric). One row per compound per temperature interval.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_results.csv
- path: `/app/outputs/step_02_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Main scored artifact: results of fitting the Lorentz approximation to JANAF data for LiBO₂ and BaS over multiple temperature intervals, including coefficients, predicted low-temperature Cp, and error metrics Δ and R.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `interval_start`, `interval_end`, `a`, `b`, `c`, `Cp_100`, `Cp_200`, `Cp_298`, `Delta`, `R`
  - `units`:
    - `interval_start`: K
    - `interval_end`: K
    - `a`: J/(mol·K)
    - `b`: 1/K^2
    - `c`: J/(mol·K^2)
    - `Cp_100`: J/(mol·K)
    - `Cp_200`: J/(mol·K)
    - `Cp_298`: J/(mol·K)
    - `Delta`: J^2/(mol^2·K^2)
    - `R`: dimensionless

Notes: The checker will recompute Δ and R from the reported Cp values and hidden benchmark values, compare coefficients to reference values, and verify that Δ is minimal for the 298.15–700 K interval.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "interval_start",
          "interval_end",
          "a",
          "b",
          "c",
          "Cp_100",
          "Cp_200",
          "Cp_298",
          "Delta",
          "R"
        ],
        "units": {
          "interval_start": "K",
          "interval_end": "K",
          "a": "J/(mol·K)",
          "b": "1/K^2",
          "c": "J/(mol·K^2)",
          "Cp_100": "J/(mol·K)",
          "Cp_200": "J/(mol·K)",
          "Cp_298": "J/(mol·K)",
          "Delta": "J^2/(mol^2·K^2)",
          "R": "dimensionless"
        }
      },
      "description": "Main scored artifact: results of fitting the Lorentz approximation to JANAF data for LiBO₂ and BaS over multiple temperature intervals, including coefficients, predicted low-temperature Cp, and error metrics Δ and R."
    }
  ],
  "notes": "The checker will recompute Δ and R from the reported Cp values and hidden benchmark values, compare coefficients to reference values, and verify that Δ is minimal for the 298.15–700 K interval."
}
```

## How you are scored
A hidden verifier independently recomputes the mean square deviation Δ and the correlation coefficient R from your reported predicted heat capacities (Cp_100, Cp_200, Cp_298) and hidden JANAF benchmark values. It also compares the fitted coefficients a, b, c to reference values. Your final reward is based on the accuracy of these quantities. Simply reporting paper-reported numbers without performing the required fits will not pass.
