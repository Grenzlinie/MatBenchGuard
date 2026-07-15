# Thermoelectric cooler performance prediction from datasheet specifications

## Problem background
Thermoelectric coolers (TECs) are solid‑state heat pumps used in precision cooling applications. Selecting a suitable TEC requires predicting its operating performance under a specific thermal load, heat sink, and ambient environment. Manufacturers provide only maximum‑rating parameters (Qmax, Imax, Vmax, ΔTmax, Thot) in their catalogs, making direct comparison difficult. This task reproduces a computational methodology that first estimates the TEC's internal electrical resistance (R), Seebeck coefficient (S), and thermal resistance (θ_TEC) from those maximum ratings, and then solves the coupled heat‑balance and electrical equations iteratively to forecast the operating current, voltage, hot‑side temperature, and coefficient of performance (COP). You will apply this methodology to a case study with ten commercial TEC models and specified design parameters.

## Approach
The methodology proceeds in two deterministic stages.

**Stage 1 – Parameter estimation:** For each TEC model, use its provided maximum ratings (Imax, Vmax, ΔTmax, Thot) to compute the device resistance R, Seebeck coefficient S, and thermal resistance θ_TEC via algebraic formulas derived from a standard thermoelectric model.

**Stage 2 – Iterative performance prediction:** Using those estimated parameters together with the fixed case‑study design values—cooling load Qc = 22 W, cold‑side temperature Tcold = 5 °C, ambient temperature Tamb = 25 °C, and heat sink thermal resistance θ_HS = 0.15 °C/W—solve the coupled thermal and electrical equations. Starting from an initial guess for the hot‑side temperature Thot, compute the temperature difference across the TEC, solve the quadratic heat‑balance equation for the operating current I, compute the voltage V and electrical power P, determine the heat rejected to the hot side, and update Thot from the heat sink equation. Iterate until Thot converges. Finally, compute the coefficient of performance COP = Qc/P.

## Reproduction target
Your goal is to produce two CSV files:
- `step_01_tec_parameters.csv`: For each of the 10 TEC models, the estimated R (Ω), S (V/K), and θ_TEC (K/W).
- `step_02_predictions.csv`: For each model, the converged operating current I (A), voltage V (V), hot‑side temperature Thot (°C), and COP (dimensionless).
All model specifications and design parameters are embedded in this instruction; no external dataset retrieval is required.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute TEC device parameters R, S, θ_TEC
- Role: scored
- Action: For each of the ten TEC models, use the provided maximum ratings to calculate the electrical resistance R, Seebeck coefficient S, and thermal resistance θ_TEC using the standard estimation formulas: R = (Vmax/Imax)*(Thot − ΔTmax)/Thot, S = Vmax/Thot, θ_TEC = (ΔTmax/(Imax*Vmax)) * (2*Thot)/(Thot − ΔTmax). Write the results to step_01_tec_parameters.csv.
- Output file: `/app/outputs/step_01_tec_parameters.csv`
- Format: csv
- Contract: columns: Model (string), R (float, Ω), S (float, V/K), theta_TEC (float, K/W). One row per model.
- Scoring: scored by hidden verifier

### Step 2: Predict operating conditions by iterative solution
- Role: scored (load-bearing)
- Action: Using the computed R, S, θ_TEC from step_01 and the design parameters (cooling load Qc=22 W, cold‑side temperature Tcold=5 °C, ambient temperature Tamb=25 °C, heat sink thermal resistance θ_HS=0.15 °C/W), solve the coupled system iteratively for each model: (a) choose an initial guess for Thot; (b) compute ΔT = Thot − Tcold; (c) solve the quadratic equation Qc = S·Tcold·I − 0.5·I²·R − ΔT/θ_TEC for the appropriate root of current I; (d) compute voltage V = S·ΔT + I·R; (e) compute power P = I·V; (f) compute heat to hot side Qh = Qc + P; (g) update Thot = Tamb + Qh·θ_HS; (h) repeat until Thot converges. Calculate COP = Qc/P. Output the final converged I, V, Thot, and COP for each model to step_02_predictions.csv.
- Output file: `/app/outputs/step_02_predictions.csv`
- Format: csv
- Contract: columns: Model (string), I (float, A), V (float, V), T_hot (float, °C), COP (float). One row per model.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_tec_parameters.csv`
- `/app/outputs/step_02_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_tec_parameters.csv
- path: `/app/outputs/step_01_tec_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed electrical resistance, Seebeck coefficient, and thermal resistance for each of the ten TEC models.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `R`, `S`, `theta_TEC`
  - `units`:
    - `R`: Ω
    - `S`: V/K
    - `theta_TEC`: K/W

### step_02_predictions.csv
- path: `/app/outputs/step_02_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted operating current, voltage, hot‑side temperature, and coefficient of performance for each TEC model.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `I`, `V`, `T_hot`, `COP`
  - `units`:
    - `I`: A
    - `V`: V
    - `T_hot`: °C
    - `COP`: unitless

Notes: The ten TEC model specifications and the case study design parameters are provided directly in the instruction; no external dataset lookup is required. The iterative solver must implement a suitable convergence criterion; the final values will be compared to the paper's predicted reference values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_tec_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "R",
          "S",
          "theta_TEC"
        ],
        "units": {
          "R": "Ω",
          "S": "V/K",
          "theta_TEC": "K/W"
        }
      },
      "description": "Computed electrical resistance, Seebeck coefficient, and thermal resistance for each of the ten TEC models."
    },
    {
      "file": "step_02_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "I",
          "V",
          "T_hot",
          "COP"
        ],
        "units": {
          "I": "A",
          "V": "V",
          "T_hot": "°C",
          "COP": "unitless"
        }
      },
      "description": "Predicted operating current, voltage, hot‑side temperature, and coefficient of performance for each TEC model."
    }
  ],
  "notes": "The ten TEC model specifications and the case study design parameters are provided directly in the instruction; no external dataset lookup is required. The iterative solver must implement a suitable convergence criterion; the final values will be compared to the paper's predicted reference values with tolerances."
}
```

## How you are scored
A hidden verifier will inspect your two output files. For each TEC model, it compares your computed R, S, θ_TEC, I, V, Thot, and COP against independently established reference values. The final reward is the fraction of these comparisons that fall within acceptable agreement. The verifier directly reads the CSV files; it does not rely on any self‑reported score. Simply hardcoding the expected numbers or otherwise circumventing the computation will yield a poor score. You must faithfully implement the estimation formulas and the iterative solver as described to receive full credit.
