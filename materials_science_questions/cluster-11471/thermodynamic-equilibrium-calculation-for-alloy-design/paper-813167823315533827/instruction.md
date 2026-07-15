# Thermal expansion model for cast iron

## Problem background
Cast iron's thermal expansion is complex because graphite dissolves upon heating, changing the volume fraction of the composite and causing lattice expansion of the surrounding austenite matrix. Traditional models that treat cast iron as a simple composite often fail to capture the measured expansion behavior, particularly at high temperatures and under different thermal histories. The reproduced work proposes a thermomechanical model that accounts for graphite dissolution, the resulting volume changes, and plastic deformation of the matrix, predicting the overall thermal expansion coefficient α as a function of temperature. Reproducing this model and computing α for two scenarios—with and without plastic deformation—provides insight into the dominant mechanisms and serves as a critical input for thermal fatigue analyses of cast iron components such as brake drums.

## Approach
The model treats cast iron as a composite of austenite (iron matrix) and graphite. The overall thermal expansion is derived from three effects: (1) thermal expansion of the austenite itself, which includes both intrinsic thermal expansion (obtained from standard pearlitic steel data at low temperatures) and a chemical expansion due to carbon uptake as graphite dissolves; (2) the volume change when graphite dissolves, driven by the density difference between graphite and iron; and (3) the thermal expansion of the graphite and iron phases weighted by their volume fractions. The volume fraction of graphite and its rate of change with temperature are determined from the equilibrium Fe–C phase diagram. 

The experiment spans 200–900°C at 50°C intervals, producing two model variants: variant B omits plastic deformation of the matrix (the matrix behaves as if graphite were pores), while variant C includes plastic deformation, allowing the matrix to accommodate the volume change of graphite dissolution. The final output is a table of the thermal expansion coefficient α for each temperature and each variant, which can be compared to experimental measurements.

## Reproduction target
Compute the thermal expansion coefficient α (in units of 10⁻⁶ K⁻¹) of a typical grey cast iron at temperatures from 200°C to 900°C, in 50°C intervals, using the composite model described above. Produce a CSV file with three columns: `temperature_C` (temperature in degrees Celsius, integer), `alpha_B` (the coefficient predicted by the model without plastic deformation, float), and `alpha_C` (the coefficient predicted by the model with plastic deformation, float). The target is to generate curves that capture the characteristic dependence on temperature, reflecting the interplay of graphite dissolution, lattice expansion, and matrix plasticity.

## Assets

- Fe-C phase diagram (Chipman 1972)
- Lattice expansion of austenite due to carbon (Ridley & Stuart 1970)
- Thermal expansion of pearlitic steel (low temperature)
- Density and thermal expansion coefficients of graphite and iron

## Workflow steps

### Step 1: Compute thermal expansion model
- Role: scored (load-bearing)
- Action: Implement the thermal expansion model for cast iron. (1) Obtain graphite volume fraction f_gr, carbon content in austenite, and derivative df_gr/dT from the Fe–C phase diagram. (2) Compute austenite thermal expansion using Eq. (1) with lattice expansion data and pearlitic steel expansion at low temperatures. (3) Compute overall thermal expansion coefficient α for cast iron using Eqs. (2)–(3) with graphite and iron densities/expansion coefficients, producing curve C (with plastic deformation) and curve B (without plastic deformation). (4) Output a CSV file with columns for temperature, alpha_B, and alpha_C at 50 °C intervals from 200 °C to 900 °C.
- Output file: `/app/outputs/step_01_thermal_expansion.csv`
- Format: csv
- Contract: temperature_C (integer), alpha_B (float, unit: 10^-6 /K), alpha_C (float, unit: 10^-6 /K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermal_expansion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermal_expansion.csv
- path: `/app/outputs/step_01_thermal_expansion.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed thermal expansion coefficient of cast iron for two model variants as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `alpha_B`, `alpha_C`
  - `description`: temperature_C: temperature in degrees Celsius (integer); alpha_B: thermal expansion coefficient without plastic deformation (10^-6 /K, float); alpha_C: thermal expansion coefficient with plastic deformation (10^-6 /K, float).

Notes: The model uses publicly available Fe–C phase diagram data, lattice expansion coefficients, and standard physical constants. The checker will recompute a metric from this artifact and compare against hidden reference values digitized from the paper's figures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermal_expansion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "alpha_B",
          "alpha_C"
        ],
        "description": "temperature_C: temperature in degrees Celsius (integer); alpha_B: thermal expansion coefficient without plastic deformation (10^-6 /K, float); alpha_C: thermal expansion coefficient with plastic deformation (10^-6 /K, float)."
      },
      "description": "Computed thermal expansion coefficient of cast iron for two model variants as a function of temperature."
    }
  ],
  "notes": "The model uses publicly available Fe–C phase diagram data, lattice expansion coefficients, and standard physical constants. The checker will recompute a metric from this artifact and compare against hidden reference values digitized from the paper's figures."
}
```

## How you are scored
Each required output file is independently checked by a hidden verifier. For the thermal expansion table, the verifier will compare your computed `alpha_B` and `alpha_C` values against reference values derived from the experimental measurements reported in the original study. The comparison uses a deviation metric across all temperature points; a higher reward is earned when the predicted curves closely match the reference values. Your reward is the weighted combination of all stage scores, so producing accurate curves that follow the expected temperature trend is essential. The exact scoring formula and tolerances are not disclosed.
