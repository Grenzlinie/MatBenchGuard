# Dust-Driven Wind Model with SiO Nucleation for Silicate Dust Condensation

## Problem background
Massive, evolved stars (AGB stars) lose substantial mass through dense, dusty winds. The formation of the first solid seed particles in these oxygen-rich outflows is a long-standing puzzle. A leading candidate is clustering of gas-phase SiO molecules, but earlier laboratory vapour‑pressure data for solid SiO implied condensation temperatures far below those inferred from infrared observations. New, significantly lower vapour‑pressure measurements of SiO have now become available. This re‑opens the question: can a dust‑driven wind model that uses a recalibrated empirical nucleation rate for SiO and the improved vapour‑pressure relation produce sonic‑point gas temperatures that match the observed range? Answering this question requires computing a set of stationary wind models and examining the resulting inner‑shell temperatures.

## Approach
You will construct a one‑dimensional, spherically symmetric, stationary dust‑driven wind model for oxygen‑rich AGB stars. The model couples the stellar radiation field with a silicate dust component that grows from seed particles formed by SiO nucleation. The method uses the empirical SiO nucleation rate (J = n₁² exp(B − a/(T³ (ln S)²)), whose constants a and B are derived in the first workflow step by re‑evaluating the Nuth & Donn (1982) nucleation data with the corrected vapour pressure, the SiO vapour‑pressure formula (ln(p_vap) = −T_v/T + S_v with T_v = 49520 K and S_v = 32.52), and a dust growth scheme that condenses gaseous species into amorphous MgFeSiO₄. Radiation pressure on the dust is calculated via a flux‑averaged extinction approximation that combines Planck‑ and Rosseland‑mean opacities, using the dirty‑silicate optical constants from Ossenkopf et al. (1992, set 1). A converged wind solution is obtained for each of eight combinations of mass‑loss rate and stellar luminosity, yielding the sonic‑point thermal and dynamical properties as well as the terminal wind parameters.

## Reproduction target
Produce the file `/app/outputs/wind_model_results.csv` containing the computed wind‑model results for the eight specified stellar configurations. The table must hold the sonic‑point radius, temperature, pressure, and degree of condensation, together with the terminal velocity, terminal condensation, Rosseland optical depth, and visual optical depth at 0.5 µm. The core quantitative target is the set of sonic‑point gas temperatures; they will be compared against hidden reference values and will be checked for consistency with the observed dust‑condensation temperatures of oxygen‑rich AGB stars (from Groenewegen et al. 2009) to verify that the offset between gas and dust temperatures falls within the physically expected window.

## Assets

- Dirty silicate optical constants (Ossenkopf+, 1992, set 1): 1992A&A...261..567O

## Workflow steps

### Step 1: Re-evaluate Nuth & Donn nucleation data to derive empirical nucleation rate constants
- Role: process
- Action: Obtain the laboratory nucleation data from Nuth & Donn (1982) (temperature T, supersaturation ratio S relative to the old vapour pressure, and estimated SiO number density n1). For each data point, recompute S using the corrected SiO vapour pressure formula (ln(p_vap) = -T_v/T + S_v with T_v=49520 K, S_v=32.52). Then fit the linear relation ln(n1²) = a / (T³ (ln S)²) + b to determine the empirical constants a and b. Derive the nucleation rate parameter B from b using an assumed average nucleation rate J_av of roughly 10⁹ cm⁻³ s⁻¹ for the laboratory experiment (as argued by Nuth & Donn, 1982). The resulting values a and B will be used in the nucleation rate formula J = n₁² exp(B − a/(T³ (ln S)²)) for the wind model calculations.
- Evidence: none

### Step 2: Build the dust-driven wind model
- Role: process
- Action: Implement a 1D stationary, spherically symmetric dust-driven wind model for oxygen-rich AGB stars. The model must use the SiO nucleation rate formula (J = n1^2 * exp(B - a/(T^3 (ln S)^2))) with the constants a and B derived in Step 1, the SiO vapour pressure (ln(p_vap) = -T_v/T + S_v with T_v=49520 K, S_v=32.52), the dust growth model for amorphous MgFeSiO4, and the flux-averaged extinction approximation (kappa_H = kappa_P^ext(T_*) * exp(-tau_*) + [kappa_P^ext(T_ph) + (1-f) kappa_R^ext(T_d)]*(1-exp(-tau_*))) with dirty silicate opacities from Ossenkopf et al. (1992).
- Evidence: none

### Step 3: Compute wind models for eight parameter sets and output results
- Role: scored (load-bearing)
- Action: For each of the eight combinations of mass-loss rate and stellar luminosity (mass-loss rates: 1,2,3,5,10,20,30,50 ×10⁻⁵ M☉/yr; the first five use L=5000 L☉, the last three use L=10000 L☉; all with M=1 M☉, T_eff=2700 K), run the wind model until convergence. Extract the sonic-point radius, temperature, pressure, degree of condensation, terminal velocity, terminal condensation, Rosseland and visual optical depths. Write the results to the output CSV file.
- Output file: `/app/outputs/wind_model_results.csv`
- Format: csv
- Contract: 8 rows, comma-separated. Columns: Mdot, r_c, T_r_c, p_r_c, f_r_c, v_inf, f_inf, tau_R, tau_0.5
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/wind_model_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### wind_model_results.csv
- path: `/app/outputs/wind_model_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Wind model results at the sonic point and dust shell properties for eight dust-driven wind models.
- schema:
  - `type`: table
  - `required_columns`: `Mdot`, `r_c`, `T_r_c`, `p_r_c`, `f_r_c`, `v_inf`, `f_inf`, `tau_R`, `tau_0.5`
  - `units`:
    - `Mdot`: 10^{-5} M_sun/yr
    - `r_c`: R_star
    - `T_r_c`: K
    - `p_r_c`: 10^{-10} bar
    - `f_r_c`: %
    - `v_inf`: km/s
    - `f_inf`: %
    - `tau_R`: dimensionless
    - `tau_0.5`: dimensionless

Notes: The file must contain exactly 8 rows, one per mass-loss rate, in ascending order of Mdot.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "wind_model_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Mdot",
          "r_c",
          "T_r_c",
          "p_r_c",
          "f_r_c",
          "v_inf",
          "f_inf",
          "tau_R",
          "tau_0.5"
        ],
        "units": {
          "Mdot": "10^{-5} M_sun/yr",
          "r_c": "R_star",
          "T_r_c": "K",
          "p_r_c": "10^{-10} bar",
          "f_r_c": "%",
          "v_inf": "km/s",
          "f_inf": "%",
          "tau_R": "dimensionless",
          "tau_0.5": "dimensionless"
        }
      },
      "description": "Wind model results at the sonic point and dust shell properties for eight dust-driven wind models."
    }
  ],
  "notes": "The file must contain exactly 8 rows, one per mass-loss rate, in ascending order of Mdot."
}
```

## How you are scored
A hidden verifier reads `wind_model_results.csv` and independently scores the eight sonic‑point temperatures. Each temperature is compared to a hidden gold value with a prescribed tolerance. Additionally, the mean offset between the computed temperatures and the observational dust‑condensation temperatures from Groenewegen et al. (2009) is calculated and must lie within a predetermined acceptable range. The total reward is determined by the fraction of models whose temperatures fall within tolerance combined with the offset‑range check; simply copying the paper’s numbers is insufficient because the verifier evaluates whether the model truly reproduces the underlying physics.
