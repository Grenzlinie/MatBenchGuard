# Thermodynamic property computation from heat capacity data

## Problem background
This task concerns the determination of thermodynamic properties for four low-molecular-weight organic nitrogen compounds: acrylonitrile, 1-aminopropane, 2-aminopropane, and 2-methyl-2-aminopropane. Low-temperature heat capacity data for the solid and liquid phases were measured from about 12 K to near the respective boiling points. From these data, together with phase-transition enthalpies and appropriate low-temperature extrapolation, the condensed-phase thermodynamic functions (Gibbs energy, enthalpy, entropy, and heat capacity) were computed over a wide temperature range. Additionally, ideal gas entropies at 298.15 K were derived from the condensed-phase entropies combined with vaporization data, and for acrylonitrile a full table of ideal gas thermodynamic functions and formation properties was obtained via statistical thermodynamics.

## Approach
The condensed-phase thermodynamic functions are obtained by numerically integrating smoothed heat capacity curves. Low-temperature behavior (below 10 K) is handled by a Debye model with compound-specific parameters. The raw heat capacity data are smoothed, including premelting corrections for solid phases and fitting liquid-phase data to provided cubic polynomials. Phase-transition enthalpies and triple-point corrections are then incorporated. The resulting functions — the Gibbs energy function, enthalpy function, enthalpy, entropy, and heat capacity — are computed for all solid and liquid phases at selected temperatures. To obtain standard ideal gas entropies at 298.15 K, the condensed-phase liquid entropy at that temperature is combined with provided vaporization data (enthalpy of vaporization, entropy of vaporization, non-ideality correction, and compression term). For acrylonitrile, the ideal gas thermodynamic functions are calculated using the rigid-rotator harmonic-oscillator approximation from the fundamental vibrational wavenumbers and moments of inertia supplied. These ideal gas functions are then combined with the standard enthalpy of combustion of acrylonitrile and standard thermodynamic data for the elements (C, H₂, N₂) to compute the enthalpy of formation, Gibbs energy of formation, and decimal logarithm of the equilibrium constant of formation as functions of temperature.

## Reproduction target
Produce three CSV tables: (1) molar thermodynamic functions for the condensed phases (all compounds, all observed solid and liquid phases, at selected temperatures) containing the Gibbs energy function, enthalpy function, enthalpy, entropy, and heat capacity at saturation; (2) standard ideal gas entropies at 298.15 K for all four compounds; (3) ideal gas thermodynamic functions and formation properties (ΔH_f°, ΔG_f°, log10 K_f) for acrylonitrile at temperatures from 0 to 1000 K. The columns and units for each file are specified in the workflow steps and output contract. All computations must be based solely on the provided resources and the described physical models.

## Assets

- **raw_heat_capacity_data.csv**: molar heat capacity C_s at saturation for all solid and liquid phases of the four compounds at the original measurement temperatures, from the published raw data. Includes footnoted temperature increments ΔT for premelting regions.
- **phase_transition_enthalpies.csv**: solid–solid transition and fusion temperatures and enthalpies from the published transition data. Columns: compound, type, T (K), ΔH (cal_th mol⁻¹).
- **raw_melting_data.csv**: equilibrium melting temperatures T_F as a function of fraction melted F for each compound, from Table 4. Columns: compound, F, 1/F, T_F (K), T_calc (K). The printed cryoscopic constants A, B, and impurity mole fraction x₂ are omitted; the agent must derive them from these data.
- **debye_parameters.json**: Debye temperatures (K) and number of degrees of freedom for each compound, for low‑temperature extrapolation below 10 K.
- **raw_vibrational_bands.json**: observed Raman and infrared wavenumbers (cm⁻¹) for acrylonitrile from the published spectra of Halverson et al. (1948) and Thompson & Torkington (1944). Includes liquid‑state values and information on vapor–liquid shifts for the CCN bending modes. The assignment of fundamental wavenumbers IS NOT provided; it must be carried out by the agent.
- **combustion_and_inertia.json**: standard enthalpy of combustion of liquid acrylonitrile (‑420.5 kcal_th mol⁻¹) from Davis & Wiedeman (1945) and the principal moments of inertia I_a, I_b, I_c (amu·Å²) from Costain & Stoicheff (1959).
- **vaporization_data.csv**: enthalpy of vaporization ΔH_vap (kcal_th mol⁻¹), non‑ideality correction (S_ideal − S_s) (cal_th K⁻¹ mol⁻¹), and R ln(p/atm) (cal_th K⁻¹ mol⁻¹) at 298.15 K for all four compounds.
- **JANAF_thermodynamic_data.csv**: thermodynamic functions for C(graphite), H₂(g), N₂(g) at selected temperatures from the JANAF tables, required for formation‑property calculations.
- **standard_enthalpies_formation.json**: standard enthalpies of formation at 298.15 K for CO₂(g) (‑94.051 kcalₜₕ mol⁻¹) and H₂O(l) (‑68.317 kcalₜₕ mol⁻¹) taken from the 1968 NBS Technical Note 270-3 (reference 20 of the paper). Required for converting the combustion enthalpy to the enthalpy of formation of acrylonitrile.

## Workflow steps

### Step 1: Melting-point and purity analysis (derive triple-point parameters)
- Role: process
- Action: Using the equilibrium melting data (F, T_F) from `raw_melting_data.csv`, apply the cryoscopic relations (e.g., T_F = T_tp⁰ – (1/F)*x₂/(A) + …) to determine, for each compound, the triple-point temperature T_tp, the impurity mole fraction x₂, and the cryoscopic constants A and B. The form of the equations and guidance can be found in standard low‑temperature calorimetry references (e.g., Westrum et al., Experimental Thermodynamics Vol. 1, Ch. 6). The results will be used in the corrections for premelting and in the enthalpy‑of‑fusion treatment.
- Evidence: `/app/outputs/melting_analysis.csv`

### Step 2: Fitting of liquid heat capacity to cubic polynomials
- Role: process
- Action: Using the raw liquid‑phase C_s data from `raw_heat_capacity_data.csv` for each compound, perform a least‑squares fit to the cubic equation C_s = A + B·T + C·T² + D·T³ over the temperature range for which liquid C_s data are available. Report the fitted coefficients A, B, C, D, the temperature range, and the average and maximum deviation. These polynomials will be used to generate smooth liquid C_s values for the subsequent thermodynamic integration.
- Evidence: `/app/outputs/liquid_cp_fit_coefficients.csv`

### Step 3: Vibrational reassignment for acrylonitrile
- Role: process
- Action: From the infrared and Raman bands provided in `raw_vibrational_bands.json`, select the 15 fundamental wavenumbers for acrylonitrile using the following reassignment logic: identify the Fermi‑resonant doublet near 963 cm⁻¹ as one fundamental with a sum‑combination; treat the weak infrared band at 1033 cm⁻¹ as the other fundamental instead of the second component of the doublet; use the liquid‑state value 566 cm⁻¹ where the vapour‑state value is not directly observed; for the two CCN bending modes (liquid values 240 and 305 cm⁻¹) apply a vapour–liquid downshift of ~16 cm⁻¹ (as observed for acetonitrile) to obtain the vapour‑state fundamentals. Output the set of 15 fundamental wavenumbers (cm⁻¹) to be used in the ideal‑gas statistical‑mechanical calculation.
- Evidence: `/app/outputs/assigned_fundamentals.json`

### Step 4: Smoothing and premelting correction of heat capacity data
- Role: process
- Action: Using the raw heat capacity data, the temperature increments, the triple‑point temperatures and cryoscopic constants from Step 1, and the transition/fusion enthalpies from `phase_transition_enthalpies.csv`, perform premelting corrections and generate smoothed C_s(T) curves for all crystalline phases of the four compounds. For liquid phases, use the cubic polynomial coefficients from Step 2 to produce smooth C_s values. The smoothed curves are required for the subsequent numerical integration.
- Evidence: `/app/outputs/smoothed_cp_values.csv`

### Step 5: Compute condensed phase thermodynamic functions
- Role: scored (load-bearing)
- Action: Numerically integrate the smoothed C_s(T) curves (with Debye function extrapolation below 10 K using the parameters from `debye_parameters.json`) and incorporate the phase‑transition enthalpies and triple‑point corrections derived in Step 1. Compute at the same selected temperatures as in the published condensed-phase table the five thermodynamic quantities: -{G_s(T)-H°(0)}/T, {H_s(T)-H°(0)}/T, {H_s(T)-H°(0)}, S_s, and C_s for all phases of all four compounds. Output a CSV file with columns: compound, phase, T (K), neg_Gs_over_T (cal_th K⁻¹ mol⁻¹), Hs_over_T (cal_th K⁻¹ mol⁻¹), Hs (cal_th mol⁻¹), Ss (cal_th K⁻¹ mol⁻¹), Cs (cal_th K⁻¹ mol⁻¹).
- Output file: `/app/outputs/condensed_phase_thermodynamic_functions.csv`
- Format: csv
- Contract: columns: compound, phase, T (K), neg_Gs_over_T (cal_th K⁻¹ mol⁻¹), Hs_over_T (cal_th K⁻¹ mol⁻¹), Hs (cal_th mol⁻¹), Ss (cal_th K⁻¹ mol⁻¹), Cs (cal_th K⁻¹ mol⁻¹)
- Scoring: scored by hidden verifier

### Step 6: Compute ideal gas entropies at 298.15 K
- Role: scored
- Action: Take the liquid entropy S_s(l) at 298.15 K from the condensed‑phase table (Step 5) and use the provided vaporization data (ΔH_vap, ΔS_vap, (S_ideal – S_s) correction, R ln(p/atm)) to compute the standard ideal gas entropy S°(298.15 K) for all four compounds. Output a CSV file with columns: compound, S_ideal_298.15 (cal_th K⁻¹ mol⁻¹).
- Output file: `/app/outputs/ideal_gas_entropy.csv`
- Format: csv
- Contract: columns: compound, S_ideal_298.15 (cal_th K⁻¹ mol⁻¹)
- Scoring: scored by hidden verifier

### Step 7: Compute ideal gas thermodynamic functions and formation properties for acrylonitrile
- Role: scored
- Action: Using the 15 fundamental wavenumbers from Step 3, the moments of inertia from `combustion_and_inertia.json`, and the rigid‑rotator harmonic‑oscillator approximation, compute the ideal gas thermodynamic functions (Gibbs energy function, enthalpy function, entropy, heat capacity) for acrylonitrile at temperatures up to 1000 K. Then, using the enthalpy of combustion from `combustion_and_inertia.json`, the standard enthalpies of formation of CO₂(g) and H₂O(l) from `standard_enthalpies_formation.json`, and the JANAF elemental data, compute the enthalpy of formation, Gibbs energy of formation, and log₁₀ equilibrium constant of formation. Output a CSV file with columns: T, neg_G_over_T, H_over_T, S, Cp, ΔH_f°, ΔG_f°, log_K_f.
- Output file: `/app/outputs/ideal_gas_functions_acrylonitrile.csv`
- Format: csv
- Contract: columns: T, neg_G_over_T, H_over_T, S, Cp, ΔH_f°, ΔG_f°, log_K_f
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/condensed_phase_thermodynamic_functions.csv`
- `/app/outputs/ideal_gas_entropy.csv`
- `/app/outputs/ideal_gas_functions_acrylonitrile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### condensed_phase_thermodynamic_functions.csv
- path: `/app/outputs/condensed_phase_thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Condensed phase thermodynamic functions for all four compounds at selected temperatures; one row per (compound, phase, temperature).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `phase`, `T`, `neg_Gs_over_T`, `Hs_over_T`, `Hs`, `Ss`, `Cs`
  - `units`:
    - `T`: K
    - `neg_Gs_over_T`: cal_th K^-1 mol^-1
    - `Hs_over_T`: cal_th K^-1 mol^-1
    - `Hs`: cal_th mol^-1
    - `Ss`: cal_th K^-1 mol^-1
    - `Cs`: cal_th K^-1 mol^-1

### ideal_gas_entropy.csv
- path: `/app/outputs/ideal_gas_entropy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Standard ideal gas entropy at 298.15 K for all four compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `S_ideal_298.15`
  - `units`:
    - `S_ideal_298.15`: cal_th K^-1 mol^-1

### ideal_gas_functions_acrylonitrile.csv
- path: `/app/outputs/ideal_gas_functions_acrylonitrile.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ideal gas thermodynamic functions and formation properties for acrylonitrile at temperatures 0–1000 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `neg_G_over_T`, `H_over_T`, `S`, `Cp`, `ΔH_f°`, `ΔG_f°`, `log_K_f`
  - `units`:
    - `T`: K
    - `neg_G_over_T`: cal_th K^-1 mol^-1
    - `H_over_T`: cal_th K^-1 mol^-1
    - `S`: cal_th K^-1 mol^-1
    - `Cp`: cal_th K^-1 mol^-1
    - `ΔH_f°`: kcal_th mol^-1
    - `ΔG_f°`: kcal_th mol^-1
    - `log_K_f`: 

Notes: Scoring compares computed values to paper-reported gold values with appropriate tolerances. The reconstruction must follow the described workflow using the provided resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "condensed_phase_thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "phase",
          "T",
          "neg_Gs_over_T",
          "Hs_over_T",
          "Hs",
          "Ss",
          "Cs"
        ],
        "units": {
          "T": "K",
          "neg_Gs_over_T": "cal_th K^-1 mol^-1",
          "Hs_over_T": "cal_th K^-1 mol^-1",
          "Hs": "cal_th mol^-1",
          "Ss": "cal_th K^-1 mol^-1",
          "Cs": "cal_th K^-1 mol^-1"
        }
      },
      "description": "Condensed phase thermodynamic functions for all four compounds at selected temperatures; one row per (compound, phase, temperature)."
    },
    {
      "file": "ideal_gas_entropy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "S_ideal_298.15"
        ],
        "units": {
          "S_ideal_298.15": "cal_th K^-1 mol^-1"
        }
      },
      "description": "Standard ideal gas entropy at 298.15 K for all four compounds."
    },
    {
      "file": "ideal_gas_functions_acrylonitrile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "neg_G_over_T",
          "H_over_T",
          "S",
          "Cp",
          "ΔH_f°",
          "ΔG_f°",
          "log_K_f"
        ],
        "units": {
          "T": "K",
          "neg_G_over_T": "cal_th K^-1 mol^-1",
          "H_over_T": "cal_th K^-1 mol^-1",
          "S": "cal_th K^-1 mol^-1",
          "Cp": "cal_th K^-1 mol^-1",
          "ΔH_f°": "kcal_th mol^-1",
          "ΔG_f°": "kcal_th mol^-1",
          "log_K_f": ""
        }
      },
      "description": "Ideal gas thermodynamic functions and formation properties for acrylonitrile at temperatures 0–1000 K."
    }
  ],
  "notes": "Scoring compares computed values to paper-reported gold values with appropriate tolerances. The reconstruction must follow the described workflow using the provided resources."
}
```

## How you are scored
A hidden verifier independently inspects the three scored CSV outputs. For each file, the verifier compares your computed entries cell‑by‑cell against reference values derived from the source literature, allowing small tolerances that account for differences in numerical integration, interpolation, and physical constants across implementations. Each file’s score is a weighted combination of the cell‑wise agreements; the final reward (a float between 0 and 1) is the weighted sum of the three file scores, with the condensed‑phase thermodynamic functions carrying the largest weight. The verifier does not reward simply copying known literature values — it expects the results to be generated by the specified smoothing, integration, and statistical thermodynamics procedures. Intermediate files (e.g., smoothed Cp) are not routinely scored unless gross structural inconsistencies are detected.
