# Kinetic Modeling and Thermochemical Analysis of Ethylsilane Thermal Decomposition

## Problem background
The thermal decomposition of ethylsilane (EtSiH₃) under static reactor conditions proceeds via a silylene‑carried chain mechanism. In this task you must:
1. Build a kinetic (ODE) model of the neat ethylsilane decomposition using the reaction mechanism given below.
2. Fit the unknown rate constants to the provided experimental data (723 K).
3. Perform RRKM falloff calculations to obtain high‑pressure activation energies.
4. Derive thermochemical quantities: the heat of formation of ethylsilylene and a methylene group additivity value.
All required data — rate parameters, experimental measurements, RRKM molecular constants, and thermochemical reference values — are supplied in this instruction.  No external files or internet access are needed.

## Reaction mechanism (chain model for neat ethylsilane decomposition)
Each reaction is labelled with a rate‑constant ID as used in the rate‑parameter table.  Forward directions carry positive numbers; reversible reactions also list the reverse ID with a minus sign.  M denotes the bath gas (primarily tetramethylsilane, TMS), whose concentration is taken as constant.

| ID  | Reaction                                |
|-----|-----------------------------------------|
| 1   | EtSiH₃ → EtSiH + H₂                    |
| 2   | EtSiH + M → C₂H₄ + SiH₂ + M            |
| -2  | C₂H₄ + SiH₂ + M → EtSiH + M            |
| 3   | SiH₂ + EtSiH₃ → EtSi₂H₅                |
| -3  | EtSi₂H₅ → SiH₂ + EtSiH₃                |
| 4   | EtSi₂H₅ → SiH₄ + EtSiH                 |
| -4  | SiH₄ + EtSiH → EtSi₂H₅                 |
| 5   | SiH₄ + M → SiH₂ + H₂ + M               |
| 6   | SiH₂ + SiH₄ → Si₂H₆                    |
| -6  | Si₂H₆ → SiH₂ + SiH₄                    |
| 7   | EtSiH + EtSiH₃ → EtSiH₂SiH₂Et          |
| -7  | EtSiH₂SiH₂Et → EtSiH + EtSiH₃          |
| 8   | EtSiH + M → C₂H₃SiH₃ + M               |
| 9   | C₂H₃SiH₃ → C₂H₄ + SiH₂                 |
| u1  | EtSi₂H₅ → products (lumped sink)       |
| u2  | EtSiH₂SiH₂Et → products (lumped sink)  |

Species abbreviations and full names:
- ES: EtSiH₃, ethylsilane
- EtSiH: ethylsilylene
- C₂H₄: ethylene
- SiH₂: silylene
- SiH₄: silane
- EtSi₂H₅: ethyldisilane
- EtSiH₂SiH₂Et: diethyldisilane
- C₂H₃SiH₃: vinylsilane

## Kinetic model construction
All reactions occur at a constant temperature of T = 723 K.  Rate constants follow the Arrhenius form
  k = A · exp(–E / (R·T))
with the gas constant R = 1.987 × 10⁻³ kcal·mol⁻¹·K⁻¹.

Initial concentrations at t = 0:
- ES: 4.93 × 10⁻⁴ mol·L⁻¹  (22 Torr EtSiH₃ at 723 K)
- All other species: 0
- M (bath gas, mainly TMS): 3.51 × 10⁻³ mol·L⁻¹  (total pressure 179 Torr, 723 K)

For reactions that explicitly include M, the rate law for the forward/reverse step is multiplied by the constant [M].  (Example: rate₂ = k₂ [EtSiH][M]; rate₋₂ = k₋₂ [C₂H₄][SiH₂][M].)

Build the system of ordinary differential equations using the above rate expressions and integrate from t = 0 to 1200 s with a stiff solver (e.g., `scipy.integrate.solve_ivp` with Radau or BDF).  The yields of observable products and the percent conversion of ES are obtained from the simulated concentrations.

## Experimental data at 723 K (target for fitting)
```csv
time_s,conversion_pct,C2H4_yield,SiH4_yield,EtSi2H5_yield,VSiH3_yield
300,23.7,0.64,0.42,NA,0.0
600,40.7,0.64,0.35,0.08,0.0
900,52.3,0.59,0.28,NA,0.003
1200,58.6,0.46,0.19,0.08,0.004
```
`NA` entries denote missing measurements; those data points must be omitted from the objective function during optimization.

## Rate‑constant parameters
Except for the adjustable rates (k₂, k₈, and the sink rate kᵤᵢ), all rate constants are fixed at the values below.  For unimolecular reactions the unit is s⁻¹; for bimolecular reactions it is M⁻¹ s⁻¹.

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
  {"id": "u1", "logA": null,  "E_kcal_mol": null,   "unit": "s^-1", "adjustable": true, "note": "sink for EtSi₂H₅, fit as kᵤᵢ (same numeric value as u2)"},
  {"id": "u2", "logA": null,  "E_kcal_mol": null,   "unit": "s^-1", "adjustable": true, "note": "sink for heavy disilane, same kᵤᵢ as u1"}
]
```

The adjustable parameters are **k₂** (id 2), **k₈** (id 8), and a common **kᵤᵢ** assigned to both u1 and u2.  Use the listed logA/E values for ids 2 and 8 as initial guesses; choose a small initial value for kᵤᵢ (e.g., 10⁻² s⁻¹).

## Parameter fitting (optimization)
Define the objective function as the sum of squared residuals between the model predictions and the experimental data for:
- ES conversion percentage (where available)
- C₂H₄ yield
- SiH₄ yield
- EtSi₂H₅ yield (omit `NA` points)
- VSiH₃ yield (C₂H₃SiH₃, omit `NA` points)

Minimize this sum over the three unknowns (k₂, k₈, kᵤᵢ) using a numerical optimizer (e.g., `scipy.optimize.least_squares`).  After convergence, record the optimised values of k₂ and k₈ at 723 K.

## RRKM falloff analysis
The fitted k₂(723 K) and k₈(723 K) represent low‑pressure (falloff) rate constants.  Perform RRKM calculations to extract the high‑pressure limit activation energies E₂∞ and E₈∞.  Use the strong‑collision approximation; implement a standard Rice‑Ramsperger‑Kassel‑Marcus routine or a Troe falloff representation.  All needed molecular data are given below.

### RRKM input parameters

```json
{
  "reaction_2": {
    "A_inf_s_1": 4.5e14,
    "rpd": 3,
    "beta_c": 0.85,
    "sigma_Ang": 4.0,
    "epsilon_kB_K": 200,
    "molecular_weight_g_mol": 58.0,
    "rotational_constants_cm_1": [0.55, 0.30, 0.22],
    "symmetry_number": 1,
    "reactant_freqs_cm_1": [3000,3000,3000,3000,3000,2130,1450,1450,1450,1450,1200,1200,1200,1200,950,800,700,690,690,250,225],
    "ts_freqs_cm_1": [3000,3000,3000,3000,2130,1450,1450,1450,1450,1200,1200,1200,1200,950,800,690,690,250,225,175],
    "ts_rotational_constants_cm_1": [0.53, 0.28, 0.20],
    "ts_symmetry_number": 1
  },
  "reaction_8": {
    "A_inf_s_1": 7.94e13,
    "rpd": 12,
    "beta_c": 0.85,
    "sigma_Ang": 4.0,
    "epsilon_kB_K": 200,
    "molecular_weight_g_mol": 58.0,
    "rotational_constants_cm_1": [0.55, 0.30, 0.22],
    "symmetry_number": 1,
    "reactant_freqs_cm_1": [3000,3000,3000,3000,3000,2130,1450,1450,1450,1450,1200,1200,1200,1200,950,800,700,690,690,250,225],
    "ts_freqs_cm_1": [3000,3000,3000,3000,2130,1450,1450,1450,1450,1300,1250,1200,1200,1200,1200,950,800,690,690,225],
    "ts_rotational_constants_cm_1": [0.50, 0.25, 0.18],
    "ts_symmetry_number": 1
  }
}
```

Bath gas (TMS) properties:
- Molecular weight: 88.2 g·mol⁻¹
- Lennard‑Jones parameters: σ = 5.8 Å, ε/k_B = 330 K

## Thermochemical derivation
1. **Heat of formation of ethylsilylene**  
   The high‑pressure activation energy of reaction 2 (forward) is E₂∞, and the reverse reaction (–2) has a negligible barrier (E = 0).  Therefore the reaction enthalpy ΔH₂ = E₂∞ – 0.  Using the standard heats of formation:
   - ΔHf(C₂H₄) = 12.5 kcal·mol⁻¹
   - ΔHf(SiH₂) = 60.0 kcal·mol⁻¹
   - ΔHf(H₂)   = 0.0 kcal·mol⁻¹

   Obtain ΔHf(EtSiH) from the relation:
   ```
   ΔHf(EtSiH) = ΔHf(C₂H₄) + ΔHf(SiH₂) – ΔH₂
   ```

2. **Methylene group additivity**  
   Using the derived ΔHf(EtSiH) and the standard group‑additivity framework for organosilanes, determine the enthalpy group additivity for the methylene group, ΔHf[C‑(H₂)(C)(Si)].  The necessary reference group values (C‑(H)₃(C), C‑(H₂)(C)₂, Si‑(H)₃(C), etc.) are available from Benson group‑additivity tables; you may use the following values extracted from the literature for consistency:
   - C‑(H)₃(C)          = –10.08 kcal·mol⁻¹
   - C‑(H₂)(C)₂         = –4.93 kcal·mol⁻¹
   - Si‑(H)₃(C)         = 3.0 kcal·mol⁻¹   (from analogous silane data)
   The detailed group‑additivity expression is:
   ```
   ΔHf(EtSiH) = ΔHf[C‑(H₂)(C)(Si)] + ΔHf[Si‑(H)(C)₂] + …
   ```
   (Supply the needed decomposition yourself; the above constants are sufficient to isolate the unknown group.)

## Reproduction target
Write a single JSON file to `/app/outputs/derived_quantities.json` containing the following numeric fields:
- `k2_at_723K` (s⁻¹) – fitted ethylsilylene decomposition rate constant
- `k8_at_723K` (s⁻¹) – fitted ethylsilylene isomerization rate constant
- `E2_inf` (kcal·mol⁻¹) – high‑pressure activation energy of reaction 2
- `E8_inf` (kcal·mol⁻¹) – high‑pressure activation energy of reaction 8
- `delta_Hf_EtSiH` (kcal·mol⁻¹) – heat of formation of ethylsilylene
- `group_additivity_C_H2_C_Si` (kcal·mol⁻¹) – methylene group additivity value
- `predicted_ES_conversion_pct_600s` – ES conversion percentage at t = 600 s predicted by your fitted model (demonstrates the ODE integration was actually performed).

All values must be obtained by genuine kinetic modeling and RRKM calculation using the inputs above.  Do not copy numbers from external sources; the derivations must be reproducible from your code.