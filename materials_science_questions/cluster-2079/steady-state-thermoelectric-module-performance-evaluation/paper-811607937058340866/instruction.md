# Evaluating Thermoelectric Generator Performance under Fixed Heat Flux and Temperature Constraints

## Problem background
Thermoelectric generators (TEGs) convert heat directly into electricity. Their performance is commonly evaluated using the dimensionless figure of merit ZT, which depends on the Seebeck coefficient, electrical conductivity, and thermal conductivity. This task examines whether ZT alone is the appropriate optimisation target when a TEG is operated under realistic thermal boundary conditions. Two distinct regimes are considered: (i) a fixed heat‑flow regime where a prescribed thermal power must be dissipated through the device, and (ii) a fixed‑temperature‑reservoir regime where the hot‑ and cold‑side temperatures are held constant and the thermal conductivity can be chosen freely. Analytical models are developed to predict the effective efficiency and the electrical power output in these two settings, and the goal is to compute the resulting numerical relationships.

## Approach
The reproduction is based on the analytical model of a two‑leg thermoelectric module operating under steady‑state conditions with constant material properties. In the shunted‑wall regime, a fraction χ of the heat is bypassed through a non‑thermoelectric material, and the effective efficiency η_eff is expressed in terms of χ and a dimensionless parameter Z_opt·T̄. In the fixed‑reservoir regime, the electrical power output W depends on the thermal conductivity κ and the power factor (α²σ). The solving agent must implement these closed‑form expressions and evaluate them over the specified parameter ranges to generate two CSV data files, one for each regime.

## Reproduction target
Produce two CSV files that capture the key numerical dependences: (1) effective efficiency η_eff as a function of the shunt fraction χ for several values of Z_opt·T̄; (2) electrical power output W as a function of thermal conductivity κ for several values of the power factor. The parameter values, ranges, and fixed constants are detailed in the workflow steps.

## Assets
Python 3 with NumPy. No external datasets, models, or pre‑trained weights are required; all inputs are defined by the analytical expressions and parameter ranges given in the workflow steps.

## Workflow steps

### Step 1: Generate effective efficiency vs. shunt fraction data
- Role: scored
- Action: Using the analytical expression for the effective efficiency of a shunted thermoelectric wall: η_eff = η_C (1 - χ) * (sqrt(1 + (Z_opt*T̄)/(1 - χ)) - 1) / (sqrt(1 + (Z_opt*T̄)/(1 - χ)) + T_C/T_H), where η_C = (T_H - T_C)/T_H and T̄ = (T_H + T_C)/2. Compute η_eff for a range of χ ∈ [0, 0.99] (at least 100 points, exclude χ=1) and for each Z_opt*T̄ in [0.1, 0.2, 0.3, 0.4, 0.5]. Set T_H = 400 K, T_C = 300 K. Output a CSV file with columns: χ (float), η_eff (float), Z_opt_T_bar (float identifier).
- Output file: `/app/outputs/step_01_figure1_data.csv`
- Format: csv
- Contract: Columns: χ (float), η_eff (float), Z_opt_T_bar (float). Each row corresponds to one (χ, Z_opt_T_bar) combination.
- Scoring: scored by hidden verifier

### Step 2: Generate power output vs. thermal conductivity data
- Role: scored
- Action: Using the analytical expression for electrical power output W of a thermoelectric generator operating between fixed‑temperature reservoirs: W = (P * (ΔT)² * S / (2d)) / (1 + P * T_H / (2κ) + sqrt(1 + P * T̄ / κ)), where ΔT = T_H - T_C, T̄ = (T_H + T_C)/2, and P is the power factor (α²σ). Compute W for a range of κ ∈ [0.1, 100] W m⁻¹ K⁻¹ (at least 100 points) and for each power factor in [1e-4, 2e-4, 3e-4, 4e-4, 5e-4] W m⁻¹ K⁻². Use T_H = 400 K, T_C = 300 K, d = 0.01 m, S = 1 m². Output a CSV file with columns: κ (float), W (float), power_factor (float).
- Output file: `/app/outputs/step_02_figure2_data.csv`
- Format: csv
- Contract: Columns: κ (float), W (float), power_factor (float). Each row corresponds to one (κ, power_factor) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_figure1_data.csv`
- `/app/outputs/step_02_figure2_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_figure1_data.csv
- path: `/app/outputs/step_01_figure1_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Effective efficiency η_eff as a function of shunt fraction χ for different Z_opt*T̄ values. The checker recomputes the expected η_eff from the formulas and checks monotonic decrease with χ.
- schema:
  - `type`: table
  - `required_columns`: `χ`, `η_eff`, `Z_opt_T_bar`
  - `units`:
    - `χ`: dimensionless (0-1)
    - `η_eff`: dimensionless efficiency
    - `Z_opt_T_bar`: dimensionless

### step_02_figure2_data.csv
- path: `/app/outputs/step_02_figure2_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Electrical power output W as a function of thermal conductivity κ for different power factor values. The checker recomputes the expected W from the formulas and checks monotonic increase with κ.
- schema:
  - `type`: table
  - `required_columns`: `κ`, `W`, `power_factor`
  - `units`:
    - `κ`: W m⁻¹ K⁻¹
    - `W`: W (electrical power)
    - `power_factor`: W m⁻¹ K⁻²

Notes: Both artifacts are scored by recomputing the analytical values from the raw CSV data and comparing within a tight relative tolerance. Structural monotonicity checks are applied (η_eff monotonically decreasing with χ, W monotonically increasing with κ). No gold values or tolerances are exposed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_figure1_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "χ",
          "η_eff",
          "Z_opt_T_bar"
        ],
        "units": {
          "χ": "dimensionless (0-1)",
          "η_eff": "dimensionless efficiency",
          "Z_opt_T_bar": "dimensionless"
        }
      },
      "description": "Effective efficiency η_eff as a function of shunt fraction χ for different Z_opt*T̄ values. The checker recomputes the expected η_eff from the formulas and checks monotonic decrease with χ."
    },
    {
      "file": "step_02_figure2_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "κ",
          "W",
          "power_factor"
        ],
        "units": {
          "κ": "W m⁻¹ K⁻¹",
          "W": "W (electrical power)",
          "power_factor": "W m⁻¹ K⁻²"
        }
      },
      "description": "Electrical power output W as a function of thermal conductivity κ for different power factor values. The checker recomputes the expected W from the formulas and checks monotonic increase with κ."
    }
  ],
  "notes": "Both artifacts are scored by recomputing the analytical values from the raw CSV data and comparing within a tight relative tolerance. Structural monotonicity checks are applied (η_eff monotonically decreasing with χ, W monotonically increasing with κ). No gold values or tolerances are exposed here."
}
```

## How you are scored
A hidden verifier independently recomputes the expected η_eff and W values from the analytical formulas using a subset of the parameter combinations you were asked to evaluate. It compares your submitted numbers to the reference values and also checks that the overall trends present in your data are correct. Both workflow stages contribute to the final score. Simply hard‑coding a few known numbers will not satisfy all of the verifier’s checks.
