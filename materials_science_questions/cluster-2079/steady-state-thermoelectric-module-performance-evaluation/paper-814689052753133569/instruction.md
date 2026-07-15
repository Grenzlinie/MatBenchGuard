# Steady-state thermoelectric module performance evaluation

## Problem background
Automotive internal combustion engines waste a large fraction of fuel energy as exhaust heat, typically at temperatures in the range of 500–800 K. Thermoelectric generators (TEGs) can convert this waste heat into electricity, but a single thermoelectric material operates efficiently only within a limited temperature window. One strategy to handle the wide exhaust temperature range is a two-stage TEG design that pairs a low-temperature material (bismuth telluride, Bi₂Te₃) for the cold side with a medium-temperature material (skutterudite) for the hot side. This task focuses on computing the steady-state performance of single-stage TEGs based on each material alone, and two-stage serial and parallel TEG configurations, by solving coupled thermal and electrical equations with temperature-dependent material properties. The resulting output power, conversion efficiency, and exergy efficiency reveal how these designs perform under realistic engine exhaust boundary conditions.

## Approach
The TEG performance model treats each thermoelectric module (or stage) as a lumped system governed by steady-state heat balances. Heat transfer from the hot source to the hot junction, and from the cold junction to the cold source, follows Newton’s law of cooling with specified heat transfer coefficients and areas. Inside each stage, the heat rate balances the Peltier heat, Fourier conduction, and distributed Joule heating; Thomson heat is neglected. The Seebeck coefficient, electrical resistivity, and thermal conductivity of both materials are temperature-dependent and are obtained from public references (Hi‑Z HZ‑20 datasheets for Bi₂Te₃, and theses for the specific P‑type (Zn₀.₉₉₇₅Ge₀.₀₀₂₅)Sb₃ and N‑type Ba₀.₄In₀.₄Co₄Sb₁₂ skutterudite compositions).

The four configurations to evaluate are: single‑stage Bi₂Te₃, single‑stage skutterudite, serial two‑stage (top stage skutterudite, bottom stage Bi₂Te₃, same current through both stages), and parallel two‑stage (top stage skutterudite, bottom stage Bi₂Te₃, independent currents). For each configuration, the coupled nonlinear equations are solved to find the unknown junction temperatures T₁ (hot junction), T₂ (cold junction), and (for two‑stage) T₃ (interface temperature). The electric current(s) are determined from the open‑circuit voltage and the total circuit resistance, with the external load resistance set such that the ratio of external to internal resistance equals 1. From the converged solution, the output power P = I² R_L, conversion efficiency η = P / q₁, and exergy efficiency η_e = P / [(1−T_c/T_h) q₁] are computed. Simulations are performed at two hot‑source temperatures, T_h = 500 K and T_h = 800 K, using a fixed cold‑source temperature of 353.15 K and the fixed heat‑transfer parameters from the study’s reference conditions.

## Reproduction target
Compute the output power (W), conversion efficiency (%), and exergy efficiency (%) for the following four TEG configurations:
- single_bi2te3
- single_skutterudite
- serial_two_stage
- parallel_two_stage
at two hot‑source temperatures: T_h = 500 K and T_h = 800 K. Use the leg dimensions (height 0.003 m, cross‑sectional area 0.00248 m²) from the study’s PN‑material table, and the fixed boundary conditions: cold‑source temperature 353.15 K, hot‑side heat transfer coefficient 800 W/m² K, cold‑side heat transfer coefficient 1000 W/m² K, heat transfer area 0.005625 m², and the external‑to‑internal resistance ratio set to 1. You must obtain and implement temperature‑dependent Seebeck coefficient, electrical resistivity, and thermal conductivity functions from the public material references. Solve the resulting coupled nonlinear heat‑balance equations for each configuration and temperature, and write the results to a CSV file teg_performance.csv with columns: configuration (string), T_h (float, K), output_power (float, W), conversion_efficiency (float, %), exergy_efficiency (float, %). The file must contain at least 8 rows (4 configurations × 2 temperatures) with at least three significant figures.

## Assets

- NumPy: https://numpy.org/
- SciPy: https://scipy.org/
- Bi2Te3 material properties (Hi-Z HZ-20): https://www.hi-z.com/
- P-type skutterudite (Zn0.9975Ge0.0025)Sb3 properties
- N-type skutterudite Ba0.4In0.4Co4Sb12 properties

## Workflow steps

### Step 1: Obtain and implement temperature-dependent material property functions
- Role: process
- Action: Locate temperature-dependent Seebeck coefficient, electrical resistivity, and thermal conductivity for Bi2Te3 (P and N type) and for the two skutterudite compositions (P-type (Zn0.9975Ge0.0025)Sb3, N-type Ba0.4In0.4Co4Sb12) from the specified public references. Implement Python functions alpha_T(T), rho_T(T), lambda_T(T) that return effective PN-unit properties using the relations: alpha = alpha_p - alpha_n, K = lambda_p*A_p/l_p + lambda_n*A_n/l_n, R = rho_p*l_p/A_p + rho_n*l_n/A_n with leg dimensions height 0.003 m and area 0.00248 m².
- Evidence: none

### Step 2: Run TEG performance simulations and save results
- Role: scored (load-bearing)
- Action: Implement the steady-state heat transfer and electrical models for four TEG configurations: single-stage Bi2Te3, single-stage skutterudite, serial two-stage, parallel two-stage. Use the material property functions from Step 1 and the fixed parameters: hot-side heat transfer coefficient 800 W/m²K, cold-side 1000 W/m²K, heat transfer area 0.005625 m², cold source temperature 353.15 K, external/internal resistance ratio 1. For each configuration, solve the coupled nonlinear heat balance equations to find junction temperatures T1, T2, T3 and compute electric currents; then compute output power P = I²R_L, conversion efficiency η = P/q1, and exergy efficiency η_e = P / ((1 - T_c/T_h) q1). Run at hot source temperatures T_h = 500 K and 800 K. Write a CSV file teg_performance.csv with these results.
- Output file: `/app/outputs/teg_performance.csv`
- Format: csv
- Contract: Columns: configuration (string, one of 'single_bi2te3', 'single_skutterudite', 'serial_two_stage', 'parallel_two_stage'), T_h (float, K), output_power (float, W), conversion_efficiency (float, %), exergy_efficiency (float, %). At least 8 rows (4 configs × 2 temperatures). Numerical precision: at least 3 significant figures.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/teg_performance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### teg_performance.csv
- path: `/app/outputs/teg_performance.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Performance metrics for each TEG configuration and hot source temperature. The hidden checker compares the agent's output power and conversion efficiency against paper-reported gold values (threshold_or_better) and validates structural trends between configurations.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `T_h`, `output_power`, `conversion_efficiency`, `exergy_efficiency`
  - `columns`:
    - `configuration`: string, one of 'single_bi2te3', 'single_skutterudite', 'serial_two_stage', 'parallel_two_stage'
    - `T_h`: float, K
    - `output_power`: float, W
    - `conversion_efficiency`: float, %
    - `exergy_efficiency`: float, %

Notes: Scoring will check that the agent's computed performance metrics meet or exceed thresholds derived from the paper's reported values (accounting for expected toolchain spread) and that required relative trends between configurations and temperatures are satisfied. No gold values are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "teg_performance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "T_h",
          "output_power",
          "conversion_efficiency",
          "exergy_efficiency"
        ],
        "columns": {
          "configuration": "string, one of 'single_bi2te3', 'single_skutterudite', 'serial_two_stage', 'parallel_two_stage'",
          "T_h": "float, K",
          "output_power": "float, W",
          "conversion_efficiency": "float, %",
          "exergy_efficiency": "float, %"
        }
      },
      "description": "Performance metrics for each TEG configuration and hot source temperature. The hidden checker compares the agent's output power and conversion efficiency against paper-reported gold values (threshold_or_better) and validates structural trends between configurations."
    }
  ],
  "notes": "Scoring will check that the agent's computed performance metrics meet or exceed thresholds derived from the paper's reported values (accounting for expected toolchain spread) and that required relative trends between configurations and temperatures are satisfied. No gold values are exposed."
}
```

## How you are scored
A hidden verifier reads your output files and independently scores each workflow stage’s artifact. The verifier compares your computed performance metrics against expected reference values and structural trends (e.g., relative ordering of configurations at different temperatures) derived from the underlying physics and the original study. It does not rely on a simple exact match; instead it checks whether your results are physically consistent and fall within acceptable ranges. The final reward is a weighted combination of the scores across artifacts. Simply reporting approximate numbers without a correct computational workflow will not receive full credit.
