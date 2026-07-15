# Volume-based Debye temperature ratio calculation using thermal expansion and Grüneisen constant

## Problem background
In Debye theory, the characteristic temperature Θ is typically treated as constant, but under constant-pressure conditions thermal expansion changes the volume, causing Θ to vary with temperature. By relating Θ to volume and introducing the Grüneisen constant γ, the temperature dependence can be expressed as Θ(T)/Θ(T0) = (V_{T0}/V_T)^γ, and for isotropic crystals as [l(T0)/l(T)]^{3γ}. This task computes the resulting quantity -ln[Θ(T)/Θ(T0)] for NaCl and KCl using published linear thermal expansion data and γ constants, thereby quantifying how much Θ deviates from its reference value at 0°C.

## Approach
You will implement the volume-based formulation. For a given substance, the ratio Θ(T)/Θ(T0) is computed as [l(T0)/l(T)]^{3γ}, where l(T) is the linear thermal expansion at temperature T, and T0 = 0°C is the reference temperature. The required inputs are: linear thermal expansion data l(T)/l(T0) for NaCl and KCl from the *Handbook of Physical Constants* (Birch, Schairer & Spicer, 1942), and the Grüneisen constant γ for each substance from Slater (1939). Using these data, compute -ln[Θ(T)/Θ(T0)] for T = 0, 100, 200, …, 600 °C. The resulting values characterise the temperature-dependent change in the Debye temperature relative to the 0°C reference.

## Reproduction target
Compute -ln[Θ(T)/Θ(T0)] for NaCl and KCl at temperatures 0°C, 100°C, 200°C, 300°C, 400°C, 500°C, and 600°C using the volume formulation with T0 = 0°C. Output the results as a CSV file with columns: substance ("NaCl" or "KCl"), temperature_C (integer 0–600), and ln_ratio_volume (the computed value, formatted to three decimal places). The file must contain exactly 14 data rows (7 temperatures × 2 substances).

## Assets

- Handbook of Physical Constants (Birch, Schairer & Spicer, 1942)
- Slater, J.C. (1939). Introduction to Chemical Physics, p.393

## Workflow steps

### Step 1: Collect thermal expansion data and Grüneisen constants
- Role: process
- Action: Obtain linear thermal expansion data l(T) for NaCl and KCl from the Handbook of Physical Constants (Birch, Schairer & Spicer, 1942) and the Grüneisen constant γ for each from Slater (1939). Extract the relevant data (temperatures, length ratios, γ values) and store them in a structured file for downstream computation.
- Evidence: `/app/outputs/expansion_data.json`

### Step 2: Compute volume-based Debye temperature ratios
- Role: scored (load-bearing)
- Action: Using the thermal expansion data and γ values collected in step_01, compute Θ(T)/Θ(T0) = [l(T0)/l(T)]^{3γ} with T0 = 0°C for T = 0, 100, 200, 300, 400, 500, 600 °C. Then compute -ln[Θ(T)/Θ(T0)] and write the results to a CSV file.
- Output file: `/app/outputs/step_02_volume_formulation_table.csv`
- Format: csv
- Contract: CSV with columns: substance (string, 'NaCl' or 'KCl'), temperature_C (integer, 0 to 600 in steps of 100), ln_ratio_volume (float, three decimal places). Exactly 14 data rows (7 temperatures × 2 substances).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_volume_formulation_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_volume_formulation_table.csv
- path: `/app/outputs/step_02_volume_formulation_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: This artifact reproduces the volume-based -ln[Θ(T)/Θ(T0)] values for NaCl and KCl tabulated in the paper. It will be compared to the hidden reference values from the paper's Table 1 (volume rows).
- schema:
  - `type`: table
  - `required_columns`: `substance`, `temperature_C`, `ln_ratio_volume`
  - `description`: Each row contains the computed -ln[Θ(T)/Θ(T0)] for a given substance and temperature, as obtained from the volume formulation.

Notes: The enthalpy-based Zener-Bilinsky formulation rows from Table 1 are not part of the scored target; only the volume formulation values computed here are scored. The Debye-Waller factor analysis is excluded due to unavailability of the required X-ray intensity data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_volume_formulation_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "substance",
          "temperature_C",
          "ln_ratio_volume"
        ],
        "description": "Each row contains the computed -ln[Θ(T)/Θ(T0)] for a given substance and temperature, as obtained from the volume formulation."
      },
      "description": "This artifact reproduces the volume-based -ln[Θ(T)/Θ(T0)] values for NaCl and KCl tabulated in the paper. It will be compared to the hidden reference values from the paper's Table 1 (volume rows)."
    }
  ],
  "notes": "The enthalpy-based Zener-Bilinsky formulation rows from Table 1 are not part of the scored target; only the volume formulation values computed here are scored. The Debye-Waller factor analysis is excluded due to unavailability of the required X-ray intensity data."
}
```

## How you are scored
A hidden verifier reads your CSV file and compares each ln_ratio_volume value against reference values from the volume formulation. The reward is the fraction of the 14 values that fall within a predetermined tolerance. The verifier does not disclose the tolerance or the reference numbers; you must compute the correct values from the provided data. The reward ranges from 0 to 1, reflecting how accurately your computed results match the expected ones.
