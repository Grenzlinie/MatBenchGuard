# Anharmonic Analysis of Rutile Heat Capacity

## Problem background
Rutile (TiO₂) is a technologically important oxide, notable for its high dielectric constant and complex polymorphism. Accurate high‑temperature heat‑capacity data are essential for thermodynamic modeling and for understanding anharmonic lattice vibrations. This task reproduces the core analysis of a published study on rutile heat capacity: converting measured constant‑pressure heat capacity (Cp) to constant‑volume heat capacity (Cv), fitting a combined harmonic‑plus‑anharmonic model, and extracting the anharmonic coefficient and the characteristic Einstein temperature of the optical branches.

## Approach
The analysis proceeds in three stages.

1. **Cp → Cv correction.** Convert every Cp value to Cv using the Nernst‑Lindemann approximation:  
   `Cv = Cp – a·Cp²·T`,  
   with the coefficient `a = 5.41 × 10⁻⁷ J⁻¹·mol` deduced from the thermal‑expansion data at 550 K in the original study. The same formula is applied over the whole temperature range; it reproduces the reference Cv values within the stated uncertainty.

2. **High‑temperature harmonic‑plus‑anharmonic model.** At high temperatures (T ≥ 650 K) the harmonic heat capacity Ch can be written as a sum of one Debye term (acoustic branches) and one Einstein term (optical branches). The equipartition limit for rutile (3 atoms per formula unit) is 9 R. The anharmonic contribution grows linearly with T, leading to the relation  
   `(Cv − 9R)/T = −(9R/20)·θ∞²·T⁻³ + A`,  
   where A is the anharmonic coefficient and θ∞ is a high‑temperature Debye temperature. Perform a linear least‑squares fit of `(Cv−9R)/T` versus `T⁻³` using all data points with T ≥ 650 K. The intercept directly yields A; the slope gives θ∞ via  
   `slope = −(9R/20)·θ∞²`.  
   From θ∞ and the known low‑temperature Debye temperature θD = 778 K (elastic‑constant and low‑temperature heat‑capacity measurements) the Einstein temperature θE follows:  
   `θ∞² = (1/6)·θD² + (25/18)·θE²`.

3. **Full‑range harmonic model and anharmonic difference.** Using the fitted θE and the fixed θD, compute the harmonic heat capacity for every temperature in the input dataset:  
   `Ch = 0.5·[ 3R·D(θD/T) + 15R·E(θE/T) ]`,  
   where D(x) and E(x) are the Debye and Einstein functions, respectively. The anharmonic contribution is then `Ca = Cv − Ch`. The complete table of Cp, Cv, Ch and Ca, together with the fitted parameters A, θE and θ∞, forms the required output.

## Required constants
- Gas constant: **R = 8.314 J·mol⁻¹·K⁻¹**. Use this value for all calculations.
- Thermal‑expansion coefficient for Cp → Cv: **a = 5.41 × 10⁻⁷ J⁻¹·mol** (Nernst‑Lindemann).
- Known lattice Debye temperature: **θD = 778 K**.

## Input data – Smoothed heat capacity of rutile
Use the following published smoothed Cp values. They are also available as a CSV file at `/app/inputs/rutile_cp.csv` with columns `T` (K) and `Cp` (J mol⁻¹ K⁻¹). If you cannot read the file, you must reconstruct the table from the numbers below.

| T / K | Cp / J mol⁻¹ K⁻¹ |
|-------|-------------------|
| 80       | 15.42 |
| 100      | 18.86 |
| 120      | 24.29 |
| 140      | 29.44 |
| 160      | 34.24 |
| 180      | 38.50 |
| 200      | 42.29 |
| 220      | 45.64 |
| 240      | 48.64 |
| 260      | 51.07 |
| 280      | 53.23 |
| 298.15   | 55.08 |
| 300      | 55.24 |
| 320      | 57.29 |
| 340      | 59.13 |
| 360      | 60.31 |
| 380      | 61.33 |
| 400      | 62.37 |
| 450      | 64.82 |
| 500      | 66.84 |
| 550      | 68.51 |
| 600      | 69.70 |
| 650      | 70.55 |
| 700      | 71.33 |
| 750      | 72.02 |
| 800      | 72.67 |
| 850      | 73.29 |
| 900      | 73.83 |
| 950      | 74.22 |
| 1000     | 74.55 |
| 1050     | 74.83 |
| 1100     | 75.01 |

## Reproduction target
Produce two artifacts:

- **`step_01_cv_ch.csv`** — a CSV file with the columns `T` (K), `Cp` (J/mol/K), `Cv` (J/mol/K), `Ch` (J/mol/K), and `anharmonic` (J/mol/K), for every temperature point in the input dataset.
- **`step_02_fitted_params.json`** — a JSON object containing the fitted parameters: `anharmonic_coefficient_A` (J mol⁻¹ K⁻²), `einstein_temperature_thetaE` (K), and `high_temp_debye_theta_inf` (K).

## Workflow steps

### Step 1: Convert Cp to Cv
- Role: process
- Action: Compute Cv = Cp − a Cp² T using `a = 5.41 × 10⁻⁷` for every temperature in the input table.
- Evidence: none

### Step 2: Fit anharmonic terms and produce heat capacity table
- Role: scored (load‑bearing)
- Action: Using the computed Cv values, perform a linear least‑squares fit of `(Cv − 9R)/T` against `T⁻³` for temperatures **T ≥ 650 K**. Obtain the anharmonic coefficient **A** (intercept) and the high‑temperature Debye temperature **θ∞** from the slope. Compute **θE** from the relation `θ∞² = (1/6)·θD² + (25/18)·θE²` with `θD = 778 K`. Then compute the harmonic heat capacity `Ch = 0.5[ 3R·D(θD/T) + 15R·E(θE/T) ]` at every temperature, using the Debye function D and the Einstein function E. Finally compute the anharmonic contribution `anharmonic = Cv − Ch`. Write the full table to the specified CSV file.
- Output file: `/app/outputs/step_01_cv_ch.csv`
- Format: csv
- Contract: CSV with header: `T`, `Cp`, `Cv`, `Ch`, `anharmonic`. Rows correspond to all temperatures from the input Cp dataset.
- Scoring: scored by hidden verifier

### Step 3: Record fitted parameters
- Role: scored
- Action: Write the fitted anharmonic coefficient A, Einstein temperature θE, and high‑temperature Debye temperature θ∞ as a JSON object to the specified file.
- Output file: `/app/outputs/step_02_fitted_params.json`
- Format: json
- Contract: JSON object with keys: `"anharmonic_coefficient_A"` (number, J mol⁻¹ K⁻²), `"einstein_temperature_thetaE"` (number, K), `"high_temp_debye_theta_inf"` (number, K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_cv_ch.csv`
- `/app/outputs/step_02_fitted_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_cv_ch.csv
- path: `/app/outputs/step_01_cv_ch.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Heat capacity table. The hidden checker extracts the Cv column for T≥650 K, recomputes the linear fit of `(Cv−9R)/T` vs `T⁻³` to obtain A and θ∞, derives θE, and compares them against the expected values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp`, `Cv`, `Ch`, `anharmonic`
  - `units`:
    - `T`: K
    - `Cp`: J mol⁻¹ K⁻¹
    - `Cv`: J mol⁻¹ K⁻¹
    - `Ch`: J mol⁻¹ K⁻¹
    - `anharmonic`: J mol⁻¹ K⁻¹

### step_02_fitted_params.json
- path: `/app/outputs/step_02_fitted_params.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fitted parameters log. The checker verifies that the reported A and θE are consistent with the values recomputed from the CSV (`step_01_cv_ch.csv`).
- schema:
  - `type`: object
  - `required`:
    - `anharmonic_coefficient_A`: number
    - `einstein_temperature_thetaE`: number
    - `high_temp_debye_theta_inf`: number
  - `units`:
    - `anharmonic_coefficient_A`: J mol⁻¹ K⁻²
    - `einstein_temperature_thetaE`: K
    - `high_temp_debye_theta_inf`: K

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_cv_ch.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": ["T", "Cp", "Cv", "Ch", "anharmonic"],
        "units": {
          "T": "K",
          "Cp": "J/mol/K",
          "Cv": "J/mol/K",
          "Ch": "J/mol/K",
          "anharmonic": "J/mol/K"
        }
      }
    },
    {
      "file": "step_02_fitted_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "anharmonic_coefficient_A": "number",
          "einstein_temperature_thetaE": "number",
          "high_temp_debye_theta_inf": "number"
        },
        "units": {
          "anharmonic_coefficient_A": "J/mol/K^2",
          "einstein_temperature_thetaE": "K",
          "high_temp_debye_theta_inf": "K"
        }
      }
    }
  ]
}
```

## How you are scored
Your submission is graded by a hidden verifier that independently examines each artifact.
- For **step_01_cv_ch.csv**, the verifier reads the Cv column for T ≥ 650 K, recomputes the linear least‑squares fit of `(Cv−9R)/T` versus `T⁻³`, extracts A and θ∞, computes θE via the relation given above, and compares these quantities to the expected values. This recomputation carries the primary reward; it ensures that the analysis has actually been performed correctly, not merely that the numbers have been self‑reported.
- For **step_02_fitted_params.json**, the verifier cross‑checks the reported parameters against those obtained from the CSV recomputation (a light structural consistency check).

The final reward is a weighted combination of these checks. Reporting plausible numbers without a correct Cv column will not succeed, because the verifier derives its scores from the raw data in your CSV.