# Heat Capacity to Thermodynamic Functions Calculation

## Problem background
Titanium disulfide (TiS₂) is a compound in the titanium–sulfur system for which no thermodynamic data were previously available. This work addresses that gap by determining the standard entropy at 298.16 K and characterizing the high-temperature heat content of TiS₂ from experimental measurements. The task is to compute these thermodynamic quantities from the reported low-temperature heat capacity data and the high-temperature heat content data. The low-temperature data span roughly 50 K to 300 K, while the high-temperature data extend from 298 K to over 1000 K and are reported to contain a small thermal anomaly. The target result identifies the anomaly and provides a self-consistent set of entropy and heat-content increments that can be used in further thermodynamic calculations.

## Approach
The reproduction uses a two-stage computational approach. First, the low-temperature heat capacity data are used to obtain the standard entropy at 298.16 K. Because the measured data do not extend to 0 K, the entropy contribution from absolute zero to the lowest measured temperature must be estimated by a physically motivated extrapolation (e.g., a Debye-type model or a polynomial fit). Numerical integration of the corrected Cp/T curve then yields the total entropy. Second, the high-temperature heat content measurements are analyzed to detect any thermal anomaly; if present, the data are split into a low-temperature phase (below the anomaly) and a high-temperature phase (above it). For each phase a suitable polynomial is fitted to the heat-content data. These fits are then used to generate a smooth table of heat-content increments (H_T − H_298.16) and entropy increments (S_T − S_298.16) at a grid of temperatures covering the experimental range, including a row at the estimated transition temperature. The final artifacts are the computed standard entropy and the smooth thermodynamic table.

## Reproduction target
Given the file `cp_data.csv` (low-temperature heat capacity measurements, temperature in K and Cp in cal/(deg·mole)) and the file `heat_content.csv` (high-temperature heat-content increments H_T − H_298.16 in cal/mole versus temperature in K), produce the following two scored artifacts:

1. **Standard entropy at 298.16 K** — written to `/app/outputs/entropy.txt` as a single floating-point number in cal/(deg·mole). This value must be derived from the Cp data by numerical integration and a reasonable extrapolation to 0 K.

2. **High-temperature thermodynamic table** — written to `/app/outputs/heat_content_table.csv` as a CSV with header `T,H_diff,S_diff`. The table must contain rows for the temperatures 350, 400, 420, 500, 600, 700, 800, 900, and 1000 K. `H_diff` is H_T − H_298.16 in cal/mole, and `S_diff` is S_T − S_298.16 in cal/(deg·mole). The 420 K row represents the transition temperature and should report the same values for both the low- and high-temperature phases. The values must be smooth and consistent with the original heat-content data after fitting separate polynomials for the two phases.

## Assets

- Low-temperature heat capacity data (Table I)
- High-temperature heat content data (Table II)
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute standard entropy at 298.16 K
- Role: scored
- Action: Read cp_data.csv, perform numerical integration (e.g., Simpson's rule) of Cp/T from the lowest measured temperature up to 298.16 K. Estimate the entropy contribution from 0 K to the lowest temperature using a reasonable extrapolation (such as a Debye model approximation or polynomial fit). Output the total standard entropy S°298.16 in cal/(deg·mole) as a single float.
- Output file: `/app/outputs/entropy.txt`
- Format: txt
- Contract: A single line containing a decimal number.
- Scoring: scored by hidden verifier

### Step 2: Compute high-temperature thermodynamic functions
- Role: scored (load-bearing)
- Action: Read heat_content.csv, identify the thermal anomaly (heat capacity peak near 420 K) by analyzing the data. Fit separate polynomial heat‑content equations for the low-temperature α phase (below ~420 K) and the high‑temperature β phase (above ~420 K). Use these fits to compute smooth values of H_T − H_298.16 (cal/mole) and S_T − S_298.16 (cal/(deg·mole)) at 350, 400, 420, 500, 600, 700, 800, 900, 1000 K. Output a CSV table with columns T, H_diff, S_diff for these temperatures.
- Output file: `/app/outputs/heat_content_table.csv`
- Format: csv
- Contract: CSV with columns: T (float), H_diff (float, cal/mole), S_diff (float, cal/(deg·mole)). Rows for T = 350, 400, 420, 500, 600, 700, 800, 900, 1000. For 420 K, include the same values for both phases.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/entropy.txt`
- `/app/outputs/heat_content_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### entropy.txt
- path: `/app/outputs/entropy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Standard entropy at 298.16 K derived from low-temperature heat capacity data.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing S°298.16 in cal/(deg·mole).

### heat_content_table.csv
- path: `/app/outputs/heat_content_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Smoothed heat content and entropy increments above 298.16 K, obtained from fitted high-temperature equations.
- schema:
  - `type`: table
  - `required_columns`: `T`, `H_diff`, `S_diff`
  - `units`:
    - `T`: K
    - `H_diff`: cal/mole
    - `S_diff`: cal/(deg·mole)
  - `description`: Rows for T = 350, 400, 420, 500, 600, 700, 800, 900, 1000. 420 K row carries the phase-transition values.

Notes: The low-temperature extrapolation may use any reasonable method; exact Debye–Einstein function is not required. Only the smooth table values are scored, not the fitted polynomial coefficients.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "entropy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing S°298.16 in cal/(deg·mole)."
      },
      "description": "Standard entropy at 298.16 K derived from low-temperature heat capacity data."
    },
    {
      "file": "heat_content_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "H_diff",
          "S_diff"
        ],
        "units": {
          "T": "K",
          "H_diff": "cal/mole",
          "S_diff": "cal/(deg·mole)"
        },
        "description": "Rows for T = 350, 400, 420, 500, 600, 700, 800, 900, 1000. 420 K row carries the phase-transition values."
      },
      "description": "Smoothed heat content and entropy increments above 298.16 K, obtained from fitted high-temperature equations."
    }
  ],
  "notes": "The low-temperature extrapolation may use any reasonable method; exact Debye–Einstein function is not required. Only the smooth table values are scored, not the fitted polynomial coefficients."
}
```

## How you are scored
A hidden verifier independently inspects each output file after your run finishes. For `entropy.txt`, it reads the single value and compares it to a reference entropy derived from the same input data; for `heat_content_table.csv`, it reads the CSV table and compares each row’s H_diff and S_diff to reference values. The verifier combines the scores from the two stages by weight to produce a single reward between 0 and 1. To obtain full credit, your computations must produce numerically accurate thermodynamic quantities that are consistent with the provided experimental data. The verifier assesses correctness, not merely the presence of files; reporting a number without genuine computation will not yield a high reward.
