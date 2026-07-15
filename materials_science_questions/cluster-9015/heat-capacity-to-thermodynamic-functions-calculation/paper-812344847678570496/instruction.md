# Thermodynamic functions from heat capacity data

## Problem background
The molar heat capacity of aluminium silicon carbide (Al4SiC4) has been measured experimentally over a wide temperature range, from cryogenic conditions (≈5 K) to above 1000 K. From such raw experimental heat capacity data, smoothed molar thermodynamic functions — heat capacity, entropy, enthalpy increment, and Gibbs free energy function — are derived through curve fitting and numerical integration. These thermodynamic functions are essential for assessing the compound's stability and for high-temperature thermodynamic calculations.

## Approach
The raw experimental heat capacity data points (temperature T and molar heat capacity Cp) are provided. The task is to perform the following computational steps:
1. **Smooth** the measured Cp values to obtain a continuous Cp(T) function valid over the measurement range (0 K to about 1047 K). A suitable curve-fitting or spline smoothing routine may be used. For temperatures below the lowest experimental point, a physically motivated low-temperature form (such as Cp ∝ T³ or a Cp/T vs T² extrapolation) should be applied to extend the function down to 0 K.
2. **Integrate** Cp(T)/T from 0 K to each target temperature T to obtain the entropy increment S°(T)-S°(0).
3. **Integrate** Cp(T) from 0 K to each target temperature T to obtain the enthalpy increment H°(T)-H°(0).
4. **Compute** the Gibbs free energy function as -(G°(T)-H°(0))/T = (H - T*S)/T.
The results are written to a CSV file for a prescribed grid of temperatures.

## Reproduction target
Produce a file named `thermodynamic_functions.csv` in `/app/outputs` that contains the smoothed molar thermodynamic functions for Al4SiC4 at every temperature listed in the step contract (5 K through 1000 K). The file must contain columns: `T` (temperature in K), `Cp` (molar heat capacity in J·K⁻¹·mol⁻¹), `S` (entropy increment in J·K⁻¹·mol⁻¹), `neg_G_over_T` (negative Gibbs free energy function in J·K⁻¹·mol⁻¹), and `H` (enthalpy increment in kJ·mol⁻¹). These values must be derived from the provided experimental Cp data using a suitable smoothing and integration procedure as described in the approach.

## Assets

- Al4SiC4 experimental heat capacity data

## Workflow steps

### Step 1: Compute smoothed thermodynamic functions from experimental Cp
- Role: scored (load-bearing)
- Action: Smooth and fit the provided experimental heat capacity data to obtain a continuous Cp(T) function valid from 0 K to 1047 K. Numerically integrate Cp(T) and Cp(T)/T to compute S°(T)-S°(0) and H°(T)-H°(0) at each target temperature, and derive -{G°(T)-H°(0)}/T. Extrapolate to 0 K using a low-temperature law. Write the resulting table to thermodynamic_functions.csv.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with header: T, Cp, S, neg_G_over_T, H. T in K; Cp, S, neg_G_over_T in J·K⁻¹·mol⁻¹; H in kJ·mol⁻¹. Rows for temperatures: 5,10,15,20,25,30,35,40,45,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,273.15,280,290,298.15,300,325,350,375,400,425,450,475,500,550,600,650,700,750,800,850,900,950,1000.
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
- target_policy: threshold_or_better
- description: Computed smoothed molar thermodynamic functions for Al4SiC4. The hidden checker compares values at key temperatures to the paper's reference values using relative tolerances (threshold_or_better: meeting/exceeding tolerance earns full credit).
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp`, `S`, `neg_G_over_T`, `H`
  - `units`:
    - `T`: K
    - `Cp`: J·K⁻¹·mol⁻¹
    - `S`: J·K⁻¹·mol⁻¹
    - `neg_G_over_T`: J·K⁻¹·mol⁻¹
    - `H`: kJ·mol⁻¹

Notes: The raw experimental heat capacity data is provided as a bundled CSV. The solving agent must perform all fitting, integration, and extrapolation; it must not reference the source paper identity. Extrapolation above 1047 K is excluded from this task.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp",
          "S",
          "neg_G_over_T",
          "H"
        ],
        "units": {
          "T": "K",
          "Cp": "J·K⁻¹·mol⁻¹",
          "S": "J·K⁻¹·mol⁻¹",
          "neg_G_over_T": "J·K⁻¹·mol⁻¹",
          "H": "kJ·mol⁻¹"
        }
      },
      "description": "Computed smoothed molar thermodynamic functions for Al4SiC4. The hidden checker compares values at key temperatures to the paper's reference values using relative tolerances (threshold_or_better: meeting/exceeding tolerance earns full credit)."
    }
  ],
  "notes": "The raw experimental heat capacity data is provided as a bundled CSV. The solving agent must perform all fitting, integration, and extrapolation; it must not reference the source paper identity. Extrapolation above 1047 K is excluded from this task."
}
```

## How you are scored
A hidden verifier will read your `thermodynamic_functions.csv` and compare the values you computed to a set of hidden reference values at selected key temperatures (including the standard 298.15 K). Scoring is **threshold-or-better**: if your computed value for a given quantity at a given temperature falls within a relative tolerance of the reference, that cell earns full credit; values outside the tolerance receive reduced credit. The overall reward is a weighted average of these cell scores, with higher weight assigned to physically important reference temperatures. Reporting numbers that happen to match the hidden reference without genuinely performing the smoothing and integration steps is not sufficient — the verifier checks the entire table for internal consistency and smoothness.
