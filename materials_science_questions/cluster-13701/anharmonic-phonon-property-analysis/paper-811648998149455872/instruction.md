# Anharmonic Analysis of Rutile Heat Capacity

## Problem background
Rutile (TiO2) is a technologically important oxide, notable for its high dielectric constant and complex polymorphism. Accurate high-temperature heat‑capacity data are essential for thermodynamic modeling and for understanding anharmonic lattice vibrations. This work provides a computational analysis of measured constant‑pressure heat capacity (Cp) data to extract the anharmonic contribution to the lattice heat capacity. The task is to perform this analysis using published smoothed Cp data, converting to constant‑volume heat capacity (Cv) and fitting a harmonic‑model decomposition to isolate the anharmonic coefficient and the characteristic Einstein temperature of the optical phonons.

## Approach
The analysis proceeds in three stages.

1. **Cp→Cv correction.** Convert the provided smoothed Cp values to constant‑volume Cv using a thermal‑expansion correction. Apply the Grüneisen relation (or an equivalent Nernst‑Lindemann approximation) with a constant Grüneisen parameter derived from literature expansion coefficients.

2. **High‑temperature harmonic‑plus‑anharmonic model.** At high temperatures (T ≥ 650 K) the harmonic heat capacity Ch is described by one Debye term (acoustic branches) and one Einstein term (optical branches). The equipartition limit for rutile (3 atoms per formula unit) is 9R. The anharmonic contribution grows linearly with T, leading to the relation  
`(Cv - 9R)/T = −(9R/20)·θ∞²·T⁻³ + A`,  
where A is the anharmonic coefficient and θ∞ is a high‑temperature Debye temperature. A linear least‑squares fit of `(Cv-9R)/T` versus `T⁻³` gives A (intercept) and θ∞ (from the slope).  
The Einstein temperature θE is then obtained from θ∞ and the known low‑temperature Debye temperature θD = 778 K (from elastic‑constant and low‑temperature heat‑capacity measurements) via  
`θ∞² = (1/6) θD² + (25/18) θE²`.

3. **Full‑range harmonic model and anharmonic difference.** Using the fitted θE and the known θD, compute the harmonic heat capacity for all available temperatures:  
`Ch = 0.5 [ 3R·D(θD/T) + 15R·E(θE/T) ]`,  
where D and E are the Debye and Einstein functions. The anharmonic contribution is then `Ca = Cv − Ch`. The complete table of Cp, Cv, Ch and Ca, together with the fitted parameters A, θE and θ∞, forms the required output.

## Reproduction target
Produce two artifacts:

- **`step_01_cv_ch.csv`** — a CSV file with columns `T` (K), `Cp` (J/mol/K), `Cv` (J/mol/K), `Ch` (J/mol/K), and `anharmonic` (J/mol/K), for every temperature point in the input dataset.
- **`step_02_fitted_params.json`** — a JSON object containing the fitted parameters: `anharmonic_coefficient_A` (J/mol/K²), `einstein_temperature_thetaE` (K), and `high_temp_debye_theta_inf` (K).

The hidden verifier will independently recompute the linear fit from the Cv column of the CSV for T ≥ 650 K, derive θE, and compare the resulting A and θE against expected values. The JSON file will be checked for structural consistency with the recomputed values.

## Assets

- Smoothed molar heat capacity of rutile (Table 1)

## Workflow steps

### Step 1: Convert Cp to Cv
- Role: process
- Action: Compute constant‑volume heat capacity Cv from the provided smoothed Cp data using the thermal expansion correction. Apply the Grüneisen relation with γ=1.43 (or equivalently the Nernst‑Lindemann approximation with a = 5.41×10⁻⁷ J⁻¹·mol) as described in the methodology. The correction may use the exact expression (β²V/κ)T below 550 K and the Grüneisen approximation above.
- Evidence: none

### Step 2: Fit anharmonic terms and produce heat capacity table
- Role: scored (load-bearing)
- Action: Using the computed Cv values, perform a linear least‑squares fit of (Cv - 9R)/T against T⁻³ for temperatures T ≥ 650 K to obtain the anharmonic coefficient A (intercept) and high‑temperature Debye temperature θ∞ (from slope). Compute the Einstein temperature θE from θ∞ and the literature Debye temperature θD = 778 K via θ∞² = (1/6)θD² + (25/18)θE². Compute the harmonic heat capacity Ch = 0.5[3R·D(θD/T) + 15R·E(θE/T)] for all temperatures in the Cp dataset. Calculate the anharmonic contribution Ca = Cv - Ch. Write the full table to the specified CSV file.
- Output file: `/app/outputs/step_01_cv_ch.csv`
- Format: csv
- Contract: CSV with header: T (K), Cp (J/mol/K), Cv (J/mol/K), Ch (J/mol/K), anharmonic (J/mol/K). Rows correspond to all temperatures from the input Cp dataset.
- Scoring: scored by hidden verifier

### Step 3: Record fitted parameters
- Role: scored
- Action: Write the fitted anharmonic coefficient A, Einstein temperature θE, and high‑temperature Debye temperature θ∞ as a JSON object to the specified file.
- Output file: `/app/outputs/step_02_fitted_params.json`
- Format: json
- Contract: JSON object with keys: "anharmonic_coefficient_A" (number, J/mol/K²), "einstein_temperature_thetaE" (number, K), "high_temp_debye_theta_inf" (number, K).
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
- description: Heat capacity table. The hidden checker extracts the Cv column for T≥650 K, recomputes the linear fit of (Cv-9R)/T vs T⁻³ to obtain A and θ∞, derives θE, and compares them against the paper‑reported gold values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp`, `Cv`, `Ch`, `anharmonic`
  - `units`:
    - `T`: K
    - `Cp`: J/mol/K
    - `Cv`: J/mol/K
    - `Ch`: J/mol/K
    - `anharmonic`: J/mol/K

### step_02_fitted_params.json
- path: `/app/outputs/step_02_fitted_params.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fitted parameters log. The checker verifies that the reported A and θE are consistent with the values recomputed from the CSV (step_01_cv_ch.csv).
- schema:
  - `type`: object
  - `required`:
    - `anharmonic_coefficient_A`: number
    - `einstein_temperature_thetaE`: number
    - `high_temp_debye_theta_inf`: number
  - `units`:
    - `anharmonic_coefficient_A`: J/mol/K^2
    - `einstein_temperature_thetaE`: K
    - `high_temp_debye_theta_inf`: K

Notes: The hidden gold consists of the paper‑reported anharmonic coefficient A = −1.24×10⁻³ J·mol⁻¹·K⁻² and Einstein temperature θE = 607 K. The primary scoring is metric_recompute on the CSV; the JSON entry provides a low‑weight structural consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

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
        "required_columns": [
          "T",
          "Cp",
          "Cv",
          "Ch",
          "anharmonic"
        ],
        "units": {
          "T": "K",
          "Cp": "J/mol/K",
          "Cv": "J/mol/K",
          "Ch": "J/mol/K",
          "anharmonic": "J/mol/K"
        }
      },
      "description": "Heat capacity table. The hidden checker extracts the Cv column for T≥650 K, recomputes the linear fit of (Cv-9R)/T vs T⁻³ to obtain A and θ∞, derives θE, and compares them against the paper‑reported gold values within tolerance."
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
      },
      "description": "Fitted parameters log. The checker verifies that the reported A and θE are consistent with the values recomputed from the CSV (step_01_cv_ch.csv)."
    }
  ],
  "notes": "The hidden gold consists of the paper‑reported anharmonic coefficient A = −1.24×10⁻³ J·mol⁻¹·K⁻² and Einstein temperature θE = 607 K. The primary scoring is metric_recompute on the CSV; the JSON entry provides a low‑weight structural consistency check."
}
```

## How you are scored
Your submission is graded by a hidden verifier that independently examines each artifact.
- For **step_01_cv_ch.csv**, the verifier reads the Cv column for T ≥ 650 K, recomputes the linear least‑squares fit of `(Cv-9R)/T` versus `T⁻³`, extracts A and θ∞, computes θE via the relation given above, and compares these quantities to the expected values. This recomputation carries the primary reward; it ensures that the analysis has actually been performed correctly, not merely that the numbers have been self‑reported.
- For **step_02_fitted_params.json**, the verifier cross‑checks the reported parameters against those obtained from the CSV recomputation (a light structural consistency check).

The final reward is a weighted combination of these checks. Reporting plausible numbers without a correct Cv column will not succeed, because the verifier derives its scores from the raw data in your CSV.
