# Binary Homogeneous Nucleation of Sulfuric Acid and Water

## Problem background
Atmospheric aerosols can form when molecules of water and a pollutant such as sulfuric acid combine to create tiny liquid droplets — a process called binary homogeneous nucleation. According to the Flood–Neumann–Döring–Reiss–Doyle nucleation theory, the rate at which droplets form and the properties of the critical nucleus (the smallest stable droplet) can be predicted from the thermodynamic data of the mixture. The theory yields a free-energy barrier, a critical composition and radius, and a pre-exponential frequency factor that together determine the nucleation rate. After passing the barrier, droplets grow along an equilibrium path that relates their composition to their radius, governed by a generalized Kelvin equation that accounts for the composition dependence of surface tension. Understanding this process helps to assess when and how sulfuric acid generated in the atmosphere can nucleate new particles, even when relative humidity is below 100%.

## Approach
Implement the binary homogeneous nucleation theory for the H2SO4+H2O system. First, obtain the published thermodynamic data (partial molar free energies, density vs. composition, surface tension) and fit their dependence on mole fraction of H2SO4 with suitable polynomials, as needed to evaluate chemical potentials, molar volumes, partial molar volumes, and surface tension at any composition. Then, for a fixed water relative humidity (i.e., a fixed water vapor activity), choose a trial sulfuric acid vapor activity and iteratively solve the two saddle‑point equilibrium equations. These equations combine the chemical potential difference between liquid and gas with a curvature term (involving surface tension and the partial molar volumes) and a correction term due to the composition dependence of surface tension. The solution yields the critical composition X* and radius r* of the nucleus. From these, compute the free-energy barrier ΔG*/kT, the curvature‑dependent pre‑exponential factor C, and the resulting nucleation rate J. Systematically adjust the acid activity until J = 1 cm⁻³ s⁻¹. Repeat this procedure for water relative humidities of 10%, 25%, 50%, 75%, and 100%, all at 25°C. Finally, using the critical radius obtained at 100% relative humidity, solve the same equilibrium equation (now holding the water activity constant while allowing composition to vary with radius) to trace the droplet composition as a function of radius from the critical size up to 1000 Å.

## Reproduction target
Produce two CSV files:

1. **Saddle‑point properties and nucleation parameters** for H2SO4+H2O at 25°C. For each relative humidity (10%, 25%, 50%, 75%, 100%) determine the acid vapor activity that gives J = 1 cm⁻³ s⁻¹ and compute the corresponding values. Write the results to `saddle_point_table.csv` with columns:
   - `relative_humidity_pct`
   - `acid_vapor_activity`
   - `acid_vapor_pressure_torr`
   - `composition_X_star` (mole fraction of H2SO4)
   - `radius_A` (angstrom)
   - `molecules_per_nucleus`
   - `deltaG_over_kT`
   - `frequency_factor_C` (cm⁻³ s⁻¹)
2. **Growth curve** at 100% relative humidity. From the critical radius r* (obtained in step 1 for 100% RH) up to 1000 Å, step by approximately 1 Å and compute the equilibrium droplet composition X (mole fraction of H2SO4). Write the results to `growth_curve_100RH.csv` with columns `radius_A` and `composition_X`.

## Assets

- Partial molar free energies for H2SO4+H2O from Giauque et al. (1960): 10.1021/ja01487a011
- Density vs. composition data for H2SO4+H2O from Perry's Chemical Engineer's Handbook (4th ed.)
- Surface tension of H2SO4+H2O mixtures from Sabinina & Terpugow (1935)
- Vapor pressure of pure H2SO4 from Vermeulen & Gmitro (1964): 10.1002/aic.690100611
- Vapor pressure of pure water at 25°C
- Molecular masses of H2O (18.0 g/mol) and H2SO4 (98.0 g/mol)
- Python with scipy/numpy: python3, scipy, numpy

## Workflow steps

### Step 1: Fit polynomials to thermodynamic data for H2SO4+H2O
- Role: process
- Action: Obtain the published datasets (partial molar free energies, density, surface tension) for H2SO4+H2O. Fit polynomials: chemical potentials μ₁, μ₂ vs. mole fraction X of H2SO4, molar volume V and partial molar volumes vs. X, surface tension γ vs. X. Store the fitted coefficients for use in later steps.
- Evidence: `/app/outputs/fitted_coefficients.json`

### Step 2: Saddle point and nucleation rate for H2SO4+H2O
- Role: scored (load-bearing)
- Action: For H2SO4+H2O at 25°C and relative humidities 10%, 25%, 50%, 75%, 100%, find the acid activity that yields a nucleation rate J=1 cm⁻³ s⁻¹ by iteratively solving the saddle-point conditions for critical composition X* and radius r*. Then compute the free energy barrier ΔG*, the pre-exponential factor C, and the nucleation rate J from the binary nucleation theory. Output a CSV table with the eight quantities listed in the paper's Table I (H2SO4 part).
- Output file: `/app/outputs/saddle_point_table.csv`
- Format: csv
- Contract: Columns: relative_humidity_pct (int), acid_vapor_activity (float), acid_vapor_pressure_torr (float), composition_X_star (float), radius_A (float), molecules_per_nucleus (float), deltaG_over_kT (float), frequency_factor_C (float).
- Scoring: scored by hidden verifier

### Step 3: Growth curve for H2SO4+H2O at 100% RH
- Role: scored (load-bearing)
- Action: For H2SO4+H2O at 100% relative humidity, after obtaining the critical radius r* from step 2, solve the generalized Kelvin equation to compute the equilibrium droplet composition X as a function of radius r from r* up to 1000 Å, at a step of approximately 1 Å. Output a CSV with columns radius_A and composition_X.
- Output file: `/app/outputs/growth_curve_100RH.csv`
- Format: csv
- Contract: Columns: radius_A (float), composition_X (float, mole fraction of H2SO4).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/saddle_point_table.csv`
- `/app/outputs/growth_curve_100RH.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### saddle_point_table.csv
- path: `/app/outputs/saddle_point_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nucleation saddle-point properties and frequency factor for H2SO4+H2O at 25°C and five relative humidities, corresponding to the H2SO4 part of Table I in the source literature.
- schema:
  - `type`: table
  - `required_columns`: `relative_humidity_pct`, `acid_vapor_activity`, `acid_vapor_pressure_torr`, `composition_X_star`, `radius_A`, `molecules_per_nucleus`, `deltaG_over_kT`, `frequency_factor_C`
  - `units`:
    - `radius_A`: angstrom
    - `acid_vapor_pressure_torr`: torr

### growth_curve_100RH.csv
- path: `/app/outputs/growth_curve_100RH.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium droplet composition (mole fraction of H2SO4) as a function of radius from the critical size to 1000 Å at 100% relative humidity for H2SO4+H2O.
- schema:
  - `type`: table
  - `required_columns`: `radius_A`, `composition_X`
  - `units`:
    - `radius_A`: angstrom

Notes: The checker compares the submitted tables to reference values from the original literature, using appropriate tolerances that account for differences in polynomial fits and numerical solvers. No hidden gold values are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "saddle_point_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "relative_humidity_pct",
          "acid_vapor_activity",
          "acid_vapor_pressure_torr",
          "composition_X_star",
          "radius_A",
          "molecules_per_nucleus",
          "deltaG_over_kT",
          "frequency_factor_C"
        ],
        "units": {
          "radius_A": "angstrom",
          "acid_vapor_pressure_torr": "torr"
        }
      },
      "description": "Nucleation saddle-point properties and frequency factor for H2SO4+H2O at 25°C and five relative humidities, corresponding to the H2SO4 part of Table I in the source literature."
    },
    {
      "file": "growth_curve_100RH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius_A",
          "composition_X"
        ],
        "units": {
          "radius_A": "angstrom"
        }
      },
      "description": "Equilibrium droplet composition (mole fraction of H2SO4) as a function of radius from the critical size to 1000 Å at 100% relative humidity for H2SO4+H2O."
    }
  ],
  "notes": "The checker compares the submitted tables to reference values from the original literature, using appropriate tolerances that account for differences in polynomial fits and numerical solvers. No hidden gold values are disclosed."
}
```

## How you are scored
A hidden verifier independently checks each of your artifacts. For `saddle_point_table.csv`, the verifier compares every numerical column (row by row) against reference values from the original study, using tolerances that allow for differences in polynomial fitting and solver implementation. For `growth_curve_100RH.csv`, the verifier extracts the composition at a few specific radii and compares them to reference values with an absolute tolerance in mole fraction. The two artifacts contribute different weights to the final reward, which will be a number between 0 and 1. Simply reporting values from the literature is insufficient — you must generate the files by running the computational procedure described in the workflow steps.
