# Kinetic Modeling and Thermochemical Analysis of an Organosilane Thermal Decomposition

## Problem background
The thermal decomposition of ethylsilane (EtSiH₃) under static reactor conditions proceeds via a silylene‑carried chain mechanism (Scheme 1A). Kinetic modeling of the product yields and reactant loss data can yield the unknown rate constants for key elementary steps (ethylsilylene decomposition and isomerization), as well as high‑pressure activation energies and thermochemical parameters such as the heat of formation of ethylsilylene and the methylene group additivity. This task requires implementing a kinetic simulation, fitting the unknown rate constants to provided experimental data, performing RRKM falloff calculations, and deriving the corresponding thermochemical quantities.

## Approach
Implement a system of ordinary differential equations representing the kinetic mechanism of neat ethylsilane decomposition (Scheme 1A). Use the provided experimental conditions (temperature, total pressure, initial reactant concentrations) and the supplied rate‑constant parameters for all reactions except the adjustable ones: k2 (ethylsilylene splitting to C₂H₄ + SiH₂), k8 (ethylsilylene isomerization to vinylsilane), and the lumped sink‑reaction rate kᵤᵢ. Simulate the concentration‑versus‑time profiles with a numerical ODE solver (e.g., SciPy's solve_ivp) and fit k2, k8, and kᵤᵢ by minimizing the sum of squared residuals between the simulated and provided experimental yields and conversion percentages at 723 K. From the optimized k2 and k8 at that temperature, use the supplied RRKM input parameters (vibrational frequencies, collision characteristics, high‑pressure A‑factors) to perform falloff calculations and extract the high‑pressure activation energies E2 and E8 for the two reactions. Using the high‑pressure activation energy E2, the known heats of formation of ethylene and silylene, and the back‑reaction energy, compute the heat of formation of ethylsilylene, ΔHf(EtSiH). Finally, derive the methylene enthalpy group additivity ΔHf[C‑(H₂)(C)(Si)] from this heat of formation. All required experimental data, rate parameters, and RRKM inputs are provided in the '## Provided data' section.

## Reproduction target
Produce a single JSON file, derived_quantities.json, containing the following six values, obtained from the kinetic fitting and RRKM analysis: k2_at_723K (ethylsilylene decomposition rate constant at 723 K, in s⁻¹), k8_at_723K (ethylsilylene isomerization rate constant at 723 K, in s⁻¹), E2_inf (high‑pressure activation energy for ethylsilylene decomposition, in kcal/mol), E8_inf (high‑pressure activation energy for ethylsilylene isomerization, in kcal/mol), delta_Hf_EtSiH (heat of formation of ethylsilylene, in kcal/mol), and group_additivity_C_H2_C_Si (methylene enthalpy group additivity, in kcal/mol). The values must be determined by genuinely solving the kinetic model and performing the RRKM calculations using the provided inputs.

## Provided data

The required experimental data, rate constants, and RRKM parameters are given below. They are also automatically created as files in `/app/inputs/` (experimental_data.csv, rate_constants.json, rrmk_params.json) by the provided solve.sh, so your solver can read them directly.

### Experimental data at 723 K
The following time‑series data for the neat ethylsilane decomposition at 723 K, total pressure 179 Torr (22 Torr ES + 157 Torr TMS), are provided. Concentrations can be converted using ideal gas law at 723 K. Missing entries are denoted by `NA`; those points should be omitted from the residual sum during optimization.

```csv
time_s,conversion_pct,C2H4_yield,SiH4_yield,EtSi2H5_yield,VSiH3_yield
300,23.7,0.64,0.42,NA,0.0
600,40.7,0.64,0.35,0.08,0.0
900,52.3,0.59,0.28,NA,0.003
1200,58.6,0.46,0.19,0.08,0.004
```
```

The initial concentration of ES at 723 K and 22 Torr is approximately 4.93e-4 mol/L (using PV=nRT). This initial concentration should be used in the ODE model.

### Rate‑constant parameters
Except for the adjustable rates `k2, k8, kui` (which you must optimize), all other rate constants are fixed at the values below. For bimolecular reactions the unit is `M^{-1} s^{-1}`; for unimolecular reactions it is `s^{-1}`. When a reaction is written as reversible, the forward/reverse rate constants are given individually.

```json
[
  {"id": "1",  "logA": 15.14, "E_kcal_mol": 64.77, "unit": "s^-1"},
  {"id": "2",  "logA": 12.27, "E_kcal_mol": 20.17, "unit": "s^-1", "adjustable": true, "note": "low‑P falloff value as initial guess"},
  {"id": "-2", "logA": 10.48, "E_kcal_mol": 0.0,    "unit": "M^-1 s^-1"},
  {"id": "3",  "logA": 10.70, "E_kcal_mol": 0.0,    "unit": "M^-1 s^-1"},
  {"id": "-3", "logA": 15.26, "E_kcal_mol": 50.83,  "unit": "s^-1"},
  {"id": "4",  "logA": 13.66, "E_kcal_mol": 48.44,  "unit": "s^-1"},
  {"id": "-4", "logA": 9.90,  "E_kcal_mol": 0.0,    "unit": "M^-1 s^-1"},
  {"id": "5",  "logA": 12.76, "E_kcal_mol": 51.53,  "unit": "s^-1"},
  {"id": "6",  "logA": 10.78, "E_kcal_mol": 0.0,    "unit": "M^-1 s^-1"},
  {"id": "-6", "logA": 15.75, "E_kcal_mol": 52.20,  "unit": "s^-1"},
  {"id": "7",  "logA": 9.78,  "E_kcal_mol": 0.0,    "unit": "M^-1 s^-1"},
  {"id": "-7", "logA": 14.30, "E_kcal_mol": 47.90,  "unit": "s^-1"},
  {"id": "8",  "logA": 9.41,  "E_kcal_mol": 20.00,  "unit": "s^-1", "adjustable": true, "note": "low‑P falloff value, to be fitted"},
  {"id": "9",  "logA": 14.48, "E_kcal_mol": 62.52,  "unit": "s^-1"},
  {"id": "u1", "logA": null,  "E_kcal_mol": null,   "unit": "s^-1", "adjustable": true, "note": "sink for EtSi2H5, fit as kui"},
  {"id": "u2", "logA": null,  "E_kcal_mol": null,   "unit": "s^-1", "adjustable": true, "note": "sink for heavy disilane, same kui"}
]
```

### RRKM input parameters
The following vibrational frequencies, high‑pressure A‑factors, path degeneracies, and collision parameters are used for the RRKM calculations. Units: frequencies in cm⁻¹; A_inf in s⁻¹; σ in Å. The fitted rate constants at 723 K (k2_723K, k8_723K) obtained from the kinetic fitting step serve as the target rate constants for the falloff calculation.

```json
{
  "reaction_2": {
    "A_inf_s_1": 4.5e14,
    "rpd": 3,
    "beta_c": 0.85,
    "sigma_Ang": 4.0,
    "reactant_freqs_cm_1": [3000,3000,3000,3000,3000,2130,1450,1450,1450,1450,1200,1200,1200,1200,950,800,700,690,690,250,225],
    "ts_freqs_cm_1": [3000,3000,3000,3000,2130,1450,1450,1450,1450,1200,1200,1200,1200,950,800,690,690,250,225,175]
  },
  "reaction_8": {
    "A_inf_s_1": 7.94e13,
    "rpd": 12,
    "beta_c": 0.85,
    "sigma_Ang": 4.0,
    "reactant_freqs_cm_1": [3000,3000,3000,3000,3000,2130,1450,1450,1450,1450,1200,1200,1200,1200,950,800,700,690,690,250,225],
    "ts_freqs_cm_1": [3000,3000,3000,3000,2130,1450,1450,1450,1450,1300,1250,1200,1200,1200,1200,950,800,690,690,225]
  }
}
```

## Assets

- Python 3: python
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement kinetic model and parameter fitting
- Role: process
- Action: Implement the kinetic mechanism of ethylsilane decomposition as a system of ordinary differential equations (ODEs). The mechanism includes: initiation via 1,1‑H₂ elimination; ethylsilylene decomposition to ethylene and silylene; ethylsilylene isomerization to vinylsilane; SiH₂ + ethylsilane association and disilane formation; SiH₄ decomposition; silylene‑silane insertion; and heavy‑product sink reactions. Use the provided experimental conditions (temperature, pressure, initial concentrations) and rate constants for all reactions except the adjustable ones (k2, k8, kᵤᵢ). The experimental data and the rate‑constant parameters for all reactions are given in the 'Provided data' section below. Simulate concentration‑time profiles with SciPy’s solve_ivp. Fit the rate constants k2, k8, and kᵤᵢ by minimizing the sum of squared residuals between simulated and provided experimental yields and conversion percentages at 723 K using an optimization routine (e.g., scipy.optimize.minimize).
- Evidence: `/app/outputs/fitting_report.json`

### Step 2: RRKM falloff calculations
- Role: process
- Action: Using the fitted rate constants k2 and k8 at 723 K (from step_01), the estimated high‑pressure A‑factors, the vibrational frequencies and collision parameters provided in the 'Provided data' section, perform RRKM falloff calculations for the ethylsilylene decomposition (reaction 2) and isomerization (reaction 8). Determine the high‑pressure activation energies E2 and E8 and the temperature‑dependent rate constants k2(T) and k8(T) at 695, 723, and 748 K.
- Evidence: `/app/outputs/rrmk_output.json`

### Step 3: Compute thermochemical quantities
- Role: process
- Action: From the high‑pressure activation energy E2, the known heats of formation of ethylene and silylene, and the back‑reaction energy, compute the heat of formation of ethylsilylene (ΔHf(EtSiH)). Then derive the methylene enthalpy group additivity ΔHf[C‑(H₂)(C)(Si)].
- Evidence: `/app/outputs/thermochem_results.json`

### Step 4: Output final derived quantities
- Role: scored (load-bearing)
- Action: Compile the fitted rate constants, high‑pressure activation energies, and thermochemical values into a single JSON file. The file must contain the following quantities with the specified units: k2_at_723K (rate constant for ethylsilylene decomposition at 723 K, s⁻¹), k8_at_723K (rate constant for ethylsilylene isomerization at 723 K, s⁻¹), E2_inf (high‑pressure activation energy for ethylsilylene decomposition, kcal/mol), E8_inf (high‑pressure activation energy for ethylsilylene isomerization, kcal/mol), delta_Hf_EtSiH (heat of formation of ethylsilylene, kcal/mol), group_additivity_C_H2_C_Si (methylene enthalpy group additivity, kcal/mol).
- Output file: `/app/outputs/derived_quantities.json`
- Format: json
- Contract: JSON object with keys: k2_at_723K (number), k8_at_723K (number), E2_inf (number), E8_inf (number), delta_Hf_EtSiH (number), group_additivity_C_H2_C_Si (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/derived_quantities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### derived_quantities.json
- path: `/app/outputs/derived_quantities.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final derived quantities: fitted rate constants at 723 K (k2_at_723K, k8_at_723K), high-pressure activation energies (E2_inf, E8_inf) in kcal/mol, heat of formation of ethylsilylene (delta_Hf_EtSiH) in kcal/mol, and group additivity value (group_additivity_C_H2_C_Si) in kcal/mol.
- schema:
  - `type`: object
  - `properties`:
    - `k2_at_723K`:
      - `type`: number
    - `k8_at_723K`:
      - `type`: number
    - `E2_inf`:
      - `type`: number
    - `E8_inf`:
      - `type`: number
    - `delta_Hf_EtSiH`:
      - `type`: number
    - `group_additivity_C_H2_C_Si`:
      - `type`: number
  - `required`: `k2_at_723K`, `k8_at_723K`, `E2_inf`, `E8_inf`, `delta_Hf_EtSiH`, `group_additivity_C_H2_C_Si`

Notes: Only the load-bearing output file is listed in the output contract. Process steps produce intermediate files not evaluated by the verifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/derived_quantities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "k2_at_723K": {
            "type": "number"
          },
          "k8_at_723K": {
            "type": "number"
          },
          "E2_inf": {
            "type": "number"
          },
          "E8_inf": {
            "type": "number"
          },
          "delta_Hf_EtSiH": {
            "type": "number"
          },
          "group_additivity_C_H2_C_Si": {
            "type": "number"
          }
        },
        "required": [
          "k2_at_723K",
          "k8_at_723K",
          "E2_inf",
          "E8_inf",
          "delta_Hf_EtSiH",
          "group_additivity_C_H2_C_Si"
        ]
      },
      "description": "Final derived quantities: fitted rate constants at 723 K (k2_at_723K, k8_at_723K), high-pressure activation energies (E2_inf, E8_inf) in kcal/mol, heat of formation of ethylsilylene (delta_Hf_EtSiH) in kcal/mol, and group additivity value (group_additivity_C_H2_C_Si) in kcal/mol."
    }
  ],
  "notes": "Only the load-bearing output file is listed in the output contract. Process steps produce intermediate files not evaluated by the verifier."
}
```

## How you are scored
A hidden verifier will read your derived_quantities.json and compare each of the six values to reference values (derived from the original study) using appropriate tolerance windows. It will also check the intermediate process‑evidence files (fitting_report.json, rrmk_output.json, thermochem_results.json) to confirm that the pipeline was actually executed. The verifier combines the agreement scores into a single reward between 0 and 1. Simply reporting the expected numbers without running the required computations will not pass. The exact tolerances and reference values are hidden; the only way to succeed is to implement the full kinetic modeling, fitting, and RRKM analysis pipeline correctly.
