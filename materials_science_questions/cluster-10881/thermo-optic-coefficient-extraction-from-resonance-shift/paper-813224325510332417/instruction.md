# Temperature-Dependent Sellmeier Coefficient Computation using Matsuoka Expansion

## Problem background
Silica is used as the background material for a double-clad photonic bandgap fiber (DCPBGF) intended for in‑vivo endoscopy. Inside the human body, temperature is higher than ambient, so the fiber's dispersion and loss properties may change. These properties depend on the refractive index, which itself varies with temperature. To model propagation at body‑relevant temperatures, one needs the temperature‑dependent Sellmeier coefficients of silica at T = 20 °C and T = 40 °C.

## Approach
The refractive index of silica glass can be described by a three‑term Sellmeier equation with oscillator parameters a_i and b_i (i = 1, 2, 3). To include temperature dependence, Matsuoka expressed each coefficient as a quadratic function of temperature: a_i(T) = a_i0 + a_i1 · T + a_i2 · T² and b_i(T) = b_i0 + b_i1 · T + b_i2 · T². The expansion constants a_i0, a_i1, a_i2, b_i0, b_i1, b_i2 (nine values per oscillator index) were determined from experimental data and are provided in the instruction. The task is to evaluate these quadratic forms at T = 20 °C and T = 40 °C to obtain the temperature‑dependent Sellmeier coefficients.

## Reproduction target
Compute a_i and b_i for i = 1, 2, 3 at the two temperatures T = 20 °C and T = 40 °C from the provided Matsuoka expansion coefficients, and write the results to `sellmeier_coefficients.csv`. The file must contain exactly six data rows — one per oscillator index at each temperature — with columns `temperature`, `i`, `a_i`, `b_i`. The correctness of these coefficients will be evaluated against independently recomputed expected values.

## Assets

- Matsuoka temperature-dependent Sellmeier coefficients

## Workflow steps

### Step 1: Compute temperature-dependent Sellmeier coefficients
- Role: scored (load-bearing)
- Action: Using the quadratic temperature relationships a_i(T)=a_i0 + a_i1*T + a_i2*T^2 and b_i(T)=b_i0 + b_i1*T + b_i2*T^2 with the Matsuoka coefficients provided in the instruction, calculate a_i and b_i for i=1,2,3 at T=20°C and T=40°C. Write the results to sellmeier_coefficients.csv.
- Output file: `/app/outputs/sellmeier_coefficients.csv`
- Format: csv
- Contract: CSV with a header row and exactly 6 data rows. Columns: temperature (integer, 20 or 40), i (integer, 1, 2, or 3), a_i (float), b_i (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sellmeier_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sellmeier_coefficients.csv
- path: `/app/outputs/sellmeier_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Temperature-evaluated Sellmeier parameters a_i and b_i for each oscillator index at 20°C and 40°C, derived from the Matsuoka quadratic expansion.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `i`, `a_i`, `b_i`
  - `units`:
    - `temperature`: °C
    - `i`: oscillator index (dimensionless)
    - `a_i`: eV²
    - `b_i`: eV

Notes: The agent must compute the coefficients exactly from the provided Matsuoka expansion coefficients. The checker will compare the submitted values to the correct values derived from the same expansion using a tight relative tolerance (≤0.001). Artifact shape: 6 rows, CSV with the declared columns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sellmeier_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "i",
          "a_i",
          "b_i"
        ],
        "units": {
          "temperature": "°C",
          "i": "oscillator index (dimensionless)",
          "a_i": "eV²",
          "b_i": "eV"
        }
      },
      "description": "Temperature-evaluated Sellmeier parameters a_i and b_i for each oscillator index at 20°C and 40°C, derived from the Matsuoka quadratic expansion."
    }
  ],
  "notes": "The agent must compute the coefficients exactly from the provided Matsuoka expansion coefficients. The checker will compare the submitted values to the correct values derived from the same expansion using a tight relative tolerance (≤0.001). Artifact shape: 6 rows, CSV with the declared columns."
}
```

## How you are scored
A hidden verifier independently scores each workflow artifact and combines the results into a final reward. For `sellmeier_coefficients.csv`, the verifier first checks that the file exists, has the correct format, column names, and row count. It then recomputes the expected Sellmeier coefficients from the same Matsuoka quadratic expansion and compares your submitted values to those expected values using a tight relative tolerance. The comparison accounts for the deterministic nature of the arithmetic: values that deviate beyond the tolerance receive partial or zero credit. Because there is one scored artifact in this task, it carries full weight. Submitting a plausible number without performing the required computation will not pass.
