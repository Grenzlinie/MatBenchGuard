# Temperature-Dependent Sellmeier Coefficient Computation using Quadratic Expansion

## Problem background
Silica is used as the background material for a double-clad photonic bandgap fiber (DCPBGF) intended for in‑vivo endoscopy. Inside the human body, temperature is higher than ambient, so the fiber's dispersion and loss properties may change. These properties depend on the refractive index, which itself varies with temperature. To model propagation at body‑relevant temperatures, one needs the temperature‑dependent Sellmeier coefficients of silica at T = 20 °C and T = 40 °C.

## Approach
The refractive index of silica glass can be described by a three‑term Sellmeier equation with oscillator parameters a_i and b_i (i = 1, 2, 3). To include temperature dependence, a referenced model expresses each coefficient as a quadratic function of temperature:

a_i(T) = a_i0 + a_i1 · T + a_i2 · T²  
b_i(T) = b_i0 + b_i1 · T + b_i2 · T²

where T is the temperature in degrees Celsius. The expansion constants (nine values per oscillator index) have been determined from experimental data and are provided below.

### Expansion coefficients (from Table 1 of the cited paper)

| Parameter | i = 1 | i = 2 | i = 3 |
|-----------|--------|--------|--------|
| a_i0 (eV²) | 228.7018 | 46.40806 | 0.014173 |
| a_i1 (eV² °C⁻¹) | 4.93×10⁻⁵ | -3.27×10⁻⁵ | -1.704×10⁻⁶ |
| a_i2 (eV² °C⁻²) | 1.10×10⁻⁷ | -3.78×10⁻⁸ | -2.14×10⁻⁹ |
| b_i0 (eV²) | 18.111630 | 10.671082 | 0.125 |
| b_i1 (eV² °C⁻¹) | 9.15×10⁻⁵ | -2.9913×10⁻⁴ | 1×10⁻⁵ (approximate) |
| b_i2 (eV² °C⁻²) | 7.478×10⁻⁵ | -4.8074×10⁻⁸ | 1×10⁻⁸ (approximate) |

*Note: For i=3, the original reference lists the linear and quadratic coefficients as <10⁻⁵ and <10⁻⁸; the approximate values 1×10⁻⁵ and 1×10⁻⁸ are adopted for computation.*

The task is to evaluate these quadratic forms at T = 20 °C and T = 40 °C to obtain the temperature‑dependent Sellmeier coefficients.

## Reproduction target
Compute a_i and b_i for i = 1, 2, 3 at the two temperatures T = 20 °C and T = 40 °C from the provided expansion coefficients, and write the results to `sellmeier_coefficients.csv`. The file must contain exactly six data rows — one per oscillator index at each temperature — with columns `temperature`, `i`, `a_i`, `b_i`. The correctness of these coefficients will be evaluated against independently recomputed expected values.

## Assets

- Temperature-dependent expansion coefficients (table above)

## Workflow steps

### Step 1: Compute temperature-dependent Sellmeier coefficients
- Role: scored (load-bearing)
- Action: Using the quadratic temperature relationships a_i(T)=a_i0 + a_i1*T + a_i2*T^2 and b_i(T)=b_i0 + b_i1*T + b_i2*T^2 with the coefficients provided in the table above, calculate a_i and b_i for i=1,2,3 at T=20°C and T=40°C. Write the results to sellmeier_coefficients.csv.
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
- description: Temperature-evaluated Sellmeier parameters a_i and b_i for each oscillator index at 20°C and 40°C, derived from the temperature-dependent quadratic expansion.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `i`, `a_i`, `b_i`
  - `units`:
    - `temperature`: °C
    - `i`: oscillator index (dimensionless)
    - `a_i`: eV²
    - `b_i`: eV

Notes: The agent must compute the coefficients exactly from the provided expansion coefficients. The checker will compare the submitted values to the correct values derived from the same expansion using a tight relative tolerance (≤0.001). Artifact shape: 6 rows, CSV with the declared columns.

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
      "description": "Temperature-evaluated Sellmeier parameters a_i and b_i for each oscillator index at 20°C and 40°C, derived from the temperature-dependent quadratic expansion."
    }
  ],
  "notes": "The agent must compute the coefficients exactly from the provided expansion coefficients. The checker will compare the submitted values to the correct values derived from the same expansion using a tight relative tolerance (≤0.001). Artifact shape: 6 rows, CSV with the declared columns."
}
```

## How you are scored
A hidden verifier independently scores each workflow artifact and combines the results into a final reward. For `sellmeier_coefficients.csv`, the verifier first checks that the file exists, has the correct format, column names, and row count. It then recomputes the expected Sellmeier coefficients from the same quadratic expansion and compares your submitted values to those expected values using a tight relative tolerance. The comparison accounts for the deterministic nature of the arithmetic: values that deviate beyond the tolerance receive partial or zero credit. Because there is one scored artifact in this task, it carries full weight. Submitting a plausible number without performing the required computation will not pass.