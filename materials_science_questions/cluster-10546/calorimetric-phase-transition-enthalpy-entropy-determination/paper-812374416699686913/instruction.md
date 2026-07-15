# Calorimetric Phase Transition Enthalpy/Entropy Determination

## Problem background
Lithium tungsten bronzes (Li_xWO_3) with x in the range 0.36-0.48 exhibit λ-type heat capacity anomalies at certain temperatures, indicating second-order phase transitions. Quantifying the enthalpy (ΔH) and entropy (ΔS) increments of these transitions is essential for understanding the underlying order-disorder physics and for comparison with theoretical models. This task computes these thermodynamic quantities from measured molar heat capacity data for three compositions: Li₀.₃₆₃WO₃, Li₀.₄₃₇WO₃, and Li₀.₄₇₈WO₃.

## Approach
The transition increments are isolated by subtracting a smooth baseline from the measured heat capacity Cp(T). For each composition and each λ-type anomaly, a non-anomalous baseline Cp_baseline(T) is constructed by interpolating between temperature regions outside the anomaly (e.g., linear interpolation between the two ends of the peak), ensuring it joins the Cp curve smoothly. The excess heat capacity ΔCp = Cp − Cp_baseline is then integrated numerically over the anomaly temperature range to obtain ΔH = ∫ ΔCp dT, and ΔCp/T is integrated to obtain ΔS = ∫ (ΔCp/T) dT. The integrations are performed on the discrete temperature grid provided in the Cp data file.

## Reproduction target
Using the supplied heat capacity data (data/Cp_data.csv) for Li₀.₃₆₃WO₃, Li₀.₄₃₇WO₃, and Li₀.₄₇₈WO₃, determine the baseline for each λ-type anomaly and compute the enthalpy (ΔH, J/mol) and entropy (ΔS, J/mol/K) increments. Output all results in a CSV file at /app/outputs/transition_results.csv containing exactly seven rows: three peaks for Li₀.₃₆₃WO₃ (peak_number 1,2,3) and two peaks each for Li₀.₄₃₇WO₃ and Li₀.₄₇₈WO₃ (peak_number 1,2). Columns: composition, peak_number, delta_H, delta_S.

## Assets

- Cubic Li_xWO_3 heat capacity data (Table I)
- Python numerical libraries (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Determine baselines for λ-type anomalies
- Role: process
- Action: For each composition (Li0.363WO3, Li0.437WO3, Li0.478WO3), identify the temperature regions of the λ-type anomalies (approximate peak temperatures: ~330 K, ~460 K, and ~590 K for Li0.363WO3; ~330 K and ~460 K for Li0.437WO3 and Li0.478WO3) and define a smooth baseline Cp_baseline(T) for each anomaly region by interpolating between non‑anomalous temperature ranges (e.g. linear interpolation between the two ends of the anomaly or a polynomial fit to the pre‑ and post‑transition data). The baseline must join smoothly with the Cp curve outside the anomaly.
- Evidence: `/app/outputs/baseline_data.csv`

### Step 2: Compute transition enthalpy and entropy increments
- Role: scored (load-bearing)
- Action: Using the measured Cp(T) data and the determined baselines, for each anomaly in each composition compute the excess heat capacity ΔCp = Cp - Cp_baseline. Numerically integrate ΔCp over the anomaly region to obtain the enthalpy increment ΔH = ∫ ΔCp dT, and integrate ΔCp/T over the same region to obtain the entropy increment ΔS = ∫ (ΔCp/T) dT. Report all results in transition_results.csv.
- Output file: `/app/outputs/transition_results.csv`
- Format: csv
- Contract: CSV with columns: composition (string, e.g. 'Li0.363WO3'), peak_number (integer, 1, 2, or 3), delta_H (float, units J/mol), delta_S (float, units J/mol/K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_results.csv
- path: `/app/outputs/transition_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transition enthalpy and entropy increments for each λ-type anomaly, computed by baseline-subtracted integration. The checker compares delta_H and delta_S to hidden reference values (paper Table III) with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `peak_number`, `delta_H`, `delta_S`
  - `units`:
    - `delta_H`: J/mol
    - `delta_S`: J/mol/K
  - `description`: Seven rows total: exactly three for Li0.363WO3 (peak_number 1,2,3), two each for Li0.437WO3 and Li0.478WO3 (peak_number 1,2).

Notes: The baseline determination step is internal; only the final transition results are scored. The hidden gold values are the paper-reported ΔH and ΔS from Table III. Tolerance margins are set to absorb typical integration and baseline-choice variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "peak_number",
          "delta_H",
          "delta_S"
        ],
        "units": {
          "delta_H": "J/mol",
          "delta_S": "J/mol/K"
        },
        "description": "Seven rows total: exactly three for Li0.363WO3 (peak_number 1,2,3), two each for Li0.437WO3 and Li0.478WO3 (peak_number 1,2)."
      },
      "description": "Transition enthalpy and entropy increments for each λ-type anomaly, computed by baseline-subtracted integration. The checker compares delta_H and delta_S to hidden reference values (paper Table III) with appropriate tolerances."
    }
  ],
  "notes": "The baseline determination step is internal; only the final transition results are scored. The hidden gold values are the paper-reported ΔH and ΔS from Table III. Tolerance margins are set to absorb typical integration and baseline-choice variation."
}
```

## How you are scored
A hidden verifier reads your transition_results.csv and compares each row's delta_H and delta_S to undisclosed reference transition increments. Your score is the fraction of the seven rows for which both delta_H and delta_S fall within acceptable tolerances (the tolerances absorb typical numerical integration and baseline-choice variability). The file must also conform to the specified schema (correct column names, data types, and exactly seven rows) to be considered. No other outputs are scored.
