# Displaced Maxwellian Gunn Effect Simulation with Nonparabolicity

## Problem background
The Gunn effect in n-GaAs is a negative differential resistance phenomenon that occurs when an electric field heats electrons in the high-mobility central (000) valley sufficiently to transfer them to low-mobility (100) satellite valleys. This transfer reduces drift velocity with increasing field, enabling microwave generation. The central valley band deviates from parabolic shape at high energies, which is expected to affect the electron transfer and hence the Gunn-effect characteristic. This task quantifies the effect of nonparabolicity on the static drift-velocity versus electric-field relation and on key derived quantities.

## Approach
Model the electron distribution by a displaced Maxwellian in a two-valley (central and satellite) system. The central valley dispersion is taken as spherical and nonparabolic: ℏ²k²/(2m₁) = ε(1+ε/ε₀). Use the collision operators for acoustic, polar optical, and intervalley scattering with material constants from Butcher (1967) and the nonparabolicity parameter ε₀≈1.8 eV from Ehrenreich (1960). For each electric field E, solve the balance equations for particle number, momentum, and energy to obtain the drift velocity v(E). Compute v(E) for two cases—parabolic (ε₀=∞) and nonparabolic—over a field range of 0 to at least 50 kV/cm with sufficient resolution. During the calculation, also track the fraction of electrons in the satellite valleys. From the results, extract: (1) peak velocity field (threshold field), (2) field at the post-peak velocity minimum (valley field), (3) low-field mobility from the slope v/E, (4) the most negative slope dv/dE expressed as mobility (maximum negative differential mobility), and (5) the satellite‑valley population ratio at E=2 kV/cm.

## Reproduction target
Produce a CSV file (step_01_vE_curve.csv) with columns: field_kV_per_cm, v_parabolic (cm/s), v_nonparabolic (cm/s). Produce a JSON file (step_02_summary.json) containing ten numeric fields: parabolic_threshold_field_kV_per_cm, nonparabolic_threshold_field_kV_per_cm, parabolic_valley_field_kV_per_cm, nonparabolic_valley_field_kV_per_cm, parabolic_zero_field_mobility_cm2_per_Vs, nonparabolic_zero_field_mobility_cm2_per_Vs, parabolic_max_NDM_cm2_per_Vs, nonparabolic_max_NDM_cm2_per_Vs, parabolic_population_ratio_2kV_per_cm_pct, nonparabolic_population_ratio_2kV_per_cm_pct.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/
- GaAs material parameters from Butcher (1967): 10.1088/0034-4885/30/1/306
- Nonparabolicity parameter ε₀ from Ehrenreich (1960): 10.1103/PhysRev.120.1951

## Workflow steps

### Step 1: Compute drift velocity vs electric field
- Role: scored (load-bearing)
- Action: Implement the displaced‑Maxwellian transport equations for the two-valley model with spherical nonparabolic band structure. Solve the momentum and energy balance equations for electric fields from 0 to at least 50 kV/cm to obtain the drift velocity for both parabolic (ε₀=∞) and nonparabolic (ε₀=1.8 eV) cases. Output the curves as CSV.
- Output file: `/app/outputs/step_01_vE_curve.csv`
- Format: csv
- Contract: Columns: field_kV_per_cm (float), v_parabolic (float), v_nonparabolic (float)
- Scoring: scored by hidden verifier

### Step 2: Extract characteristic quantities
- Role: scored
- Action: From the computed v(E) curves and the valley populations tracked during the simulation, extract: (a) threshold field (kV/cm) – location of peak velocity, (b) valley field (kV/cm) – location of minimum velocity after peak, (c) zero-field mobility (cm²/V·s) – low-field slope v/E, (d) maximum negative differential mobility (cm²/V·s) – most negative dv/dE expressed as mobility, (e) population ratio of (100) valleys at 2 kV/cm (%). Output a JSON file with ten numeric fields.
- Output file: `/app/outputs/step_02_summary.json`
- Format: json
- Contract: Keys: parabolic_threshold_field_kV_per_cm, nonparabolic_threshold_field_kV_per_cm, parabolic_valley_field_kV_per_cm, nonparabolic_valley_field_kV_per_cm, parabolic_zero_field_mobility_cm2_per_Vs, nonparabolic_zero_field_mobility_cm2_per_Vs, parabolic_max_NDM_cm2_per_Vs, nonparabolic_max_NDM_cm2_per_Vs, parabolic_population_ratio_2kV_per_cm_pct, nonparabolic_population_ratio_2kV_per_cm_pct
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_vE_curve.csv`
- `/app/outputs/step_02_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_vE_curve.csv
- path: `/app/outputs/step_01_vE_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Drift velocity vs electric field for parabolic and nonparabolic cases. The checker will recompute threshold field, valley field, zero-field mobility, and maximum negative differential mobility from this curve.
- schema:
  - `type`: table
  - `required_columns`: `field_kV_per_cm`, `v_parabolic`, `v_nonparabolic`
  - `units`:
    - `field_kV_per_cm`: kV/cm
    - `v_parabolic`: cm/s
    - `v_nonparabolic`: cm/s

### step_02_summary.json
- path: `/app/outputs/step_02_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Characteristic quantities extracted from the simulation, compared against hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `parabolic_threshold_field_kV_per_cm`: number (kV/cm)
    - `nonparabolic_threshold_field_kV_per_cm`: number (kV/cm)
    - `parabolic_valley_field_kV_per_cm`: number (kV/cm)
    - `nonparabolic_valley_field_kV_per_cm`: number (kV/cm)
    - `parabolic_zero_field_mobility_cm2_per_Vs`: number (cm^2/V·s)
    - `nonparabolic_zero_field_mobility_cm2_per_Vs`: number (cm^2/V·s)
    - `parabolic_max_NDM_cm2_per_Vs`: number (cm^2/V·s)
    - `nonparabolic_max_NDM_cm2_per_Vs`: number (cm^2/V·s)
    - `parabolic_population_ratio_2kV_per_cm_pct`: number (%)
    - `nonparabolic_population_ratio_2kV_per_cm_pct`: number (%)

Notes: The hidden checker will also cross-verify consistency between the curve and the summary for quantities that can be recomputed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_vE_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_kV_per_cm",
          "v_parabolic",
          "v_nonparabolic"
        ],
        "units": {
          "field_kV_per_cm": "kV/cm",
          "v_parabolic": "cm/s",
          "v_nonparabolic": "cm/s"
        }
      },
      "description": "Drift velocity vs electric field for parabolic and nonparabolic cases. The checker will recompute threshold field, valley field, zero-field mobility, and maximum negative differential mobility from this curve."
    },
    {
      "file": "step_02_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "parabolic_threshold_field_kV_per_cm": "number (kV/cm)",
          "nonparabolic_threshold_field_kV_per_cm": "number (kV/cm)",
          "parabolic_valley_field_kV_per_cm": "number (kV/cm)",
          "nonparabolic_valley_field_kV_per_cm": "number (kV/cm)",
          "parabolic_zero_field_mobility_cm2_per_Vs": "number (cm^2/V·s)",
          "nonparabolic_zero_field_mobility_cm2_per_Vs": "number (cm^2/V·s)",
          "parabolic_max_NDM_cm2_per_Vs": "number (cm^2/V·s)",
          "nonparabolic_max_NDM_cm2_per_Vs": "number (cm^2/V·s)",
          "parabolic_population_ratio_2kV_per_cm_pct": "number (%)",
          "nonparabolic_population_ratio_2kV_per_cm_pct": "number (%)"
        }
      },
      "description": "Characteristic quantities extracted from the simulation, compared against hidden reference values."
    }
  ],
  "notes": "The hidden checker will also cross-verify consistency between the curve and the summary for quantities that can be recomputed."
}
```

## How you are scored
Each workflow artifact is independently evaluated by a hidden verifier. For step_01_vE_curve.csv, the verifier will recompute the threshold field, valley field, zero‑field mobility, and maximum negative differential mobility from your submitted curve and compare them against reference values with appropriate tolerances. For step_02_summary.json, the verifier will compare your reported ten quantities against hidden reference values. The final reward is a weighted combination of these stage scores. Simply reporting numbers is not sufficient; the verifier cross‑checks derived quantities against your raw v(E) curve to ensure internal consistency.
