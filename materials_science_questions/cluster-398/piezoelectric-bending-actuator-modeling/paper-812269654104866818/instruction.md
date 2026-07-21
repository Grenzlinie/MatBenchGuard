# Piezoelectric Noise Auger Coefficient Enhancement in GaAs

## Problem background
In piezoelectric semiconductors such as GaAs, propagating acoustic noise creates a random electric field via the piezoelectric effect. This random field is predicted to alter Auger recombination rates, but the size of the effect and its dependence on experimental conditions are not obvious without a quantitative model. This task quantifies the change in the Auger coefficient for GaAs subjected to a [110] shear-mode acoustic flux by evaluating an analytic expression that relates the enhancement factor to the flux intensity, temperature, and carrier concentration.

## Approach
The work models the piezoelectric noise field as a Gaussian random potential characterized by a spatial correlation function. Under nondegenerate carrier statistics, the field influences the Auger transition through a local statistical factor. Configuration averaging leads to a closed-form expression for the ratio of the Auger coefficient in the presence of the noise field (C) to that of the noise-free sample (C0). The expression depends on standard material parameters—dielectric constant, piezoelectric stress constant, mass density, and the appropriate elastic stiffness constant—as well as physical constants (Boltzmann constant, vacuum permittivity). Carrier screening is included through the Debye–Hückel screening length. The agent will implement this expression and evaluate it for GaAs using the provided material constants, over a grid of temperatures, carrier concentrations, and flux intensities, outputting a structured table of the computed ratios.

## Reproduction target
Produce a comma-separated values (CSV) file with columns: temperature_K, carrier_concentration_m3, flux_intensity_W_m2, ratio_C_over_C0. Compute the ratio for every combination of temperature T = 10, 77, 300 K, carrier concentration n = 1e20, 1e21, 1e22 m⁻³, and a log-spaced range of acoustic flux intensity P_T from 1e4 to 1e8 W/m² (generate at least 30 distinct flux points across the range). Use the explicit formula

  C/C0 = exp( e14² * P_T / (8 * ε * n * k_B * T * ρ * v_T³) )

where
  ε = κ * ε₀,  v_T = sqrt(c44 / ρ),

and the material constants and physical constants are:
  e14 = 0.16 C/m²,
  κ = 13.18,
  ε₀ = 8.8541878128e-12 F/m,
  ρ = 5.36e3 kg/m³,
  c44 = 5.94e10 N/m²,
  k_B = 1.380649e-23 J/K.

The output file must be written to /app/outputs/step_01_results.csv with a header row.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute Auger coefficient ratio
- Role: scored (load-bearing)
- Action: For each combination of temperature T in {10, 77, 300} K, carrier concentration n in {1e20, 1e21, 1e22} m⁻³, and a log-spaced range of acoustic flux intensity P_T from 1e4 to 1e8 W/m² (at least 30 distinct points total across the range), compute the Auger coefficient ratio C/C0 using the explicit formula:

    C/C0 = exp( e14² * P_T / (8 * ε * n * k_B * T * ρ * v_T³) )

  where ε = κ ε₀, v_T = sqrt(c44/ρ). Material constants: e14 = 0.16 C/m², κ = 13.18, ε₀ = 8.8541878128e-12 F/m, ρ = 5.36e3 kg/m³, c44 = 5.94e10 N/m², k_B = 1.380649e-23 J/K. Write a CSV file with columns temperature_K, carrier_concentration_m3, flux_intensity_W_m2, ratio_C_over_C0.
- Output file: `/app/outputs/step_01_results.csv`
- Format: csv
- Contract: CSV with header: temperature_K (float), carrier_concentration_m3 (float), flux_intensity_W_m2 (float), ratio_C_over_C0 (float). All numeric; ratio dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.csv
- path: `/app/outputs/step_01_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Auger coefficient ratio C/C0 for GaAs under [110] shear acoustic noise as a function of temperature, carrier concentration, and flux intensity; the ratio is dimensionless and must be computed from the explicit formula C/C0 = exp( e14² * P_T / (8 * ε * n * k_B * T * ρ * v_T³) ) with ε = κ ε₀, v_T = sqrt(c44/ρ).
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `carrier_concentration_m3`, `flux_intensity_W_m2`, `ratio_C_over_C0`
  - `units`:
    - `temperature_K`: K
    - `carrier_concentration_m3`: m^-3
    - `flux_intensity_W_m2`: W/m^2
    - `ratio_C_over_C0`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "carrier_concentration_m3",
          "flux_intensity_W_m2",
          "ratio_C_over_C0"
        ],
        "units": {
          "temperature_K": "K",
          "carrier_concentration_m3": "m^-3",
          "flux_intensity_W_m2": "W/m^2",
          "ratio_C_over_C0": "dimensionless"
        }
      },
      "description": "Auger coefficient ratio C/C0 for GaAs under [110] shear acoustic noise as a function of temperature, carrier concentration, and flux intensity; the ratio is dimensionless and must be computed from the explicit formula C/C0 = exp( e14² * P_T / (8 * ε * n * k_B * T * ρ * v_T³) ) with ε = κ ε₀, v_T = sqrt(c44/ρ)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your output will be evaluated by a hidden verifier that examines the CSV file. The verifier checks that the file has the correct columns and that all required (temperature, carrier concentration) combinations are present with a reasonable number of flux points. For each row, the verifier independently recomputes the expected ratio using the same material and physical constants and the formula provided. It then compares your ratio to the expected value via a relative tolerance. Your score for this step is the fraction of rows that pass this check. The overall reward is the weighted combination of scores across workflow steps (here the entire weight is on this step).
