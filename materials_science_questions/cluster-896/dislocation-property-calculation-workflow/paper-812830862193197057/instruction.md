# Schottky Vacancy Defect Energy Calculation in Sillimanite at Melting Temperature

## Problem background
Lattice defects such as vacancies can add an excess free energy to a crystal, potentially influencing mineral stability. This task examines whether intrinsic Schottky (vacancy) point defects in sillimanite could produce a meaningful excess molar energy that would alter the pressure-temperature stability relations of the Al₂SiO₅ polymorphs. The computation relies on an empirical linear relationship between Schottky defect formation enthalpy and melting temperature, originally derived from alkali halides, together with a quasi-chemical equilibrium description of vacancy site fractions.

## Approach
The approach is a three-stage thermodynamic calculation:
1.  Estimate the Schottky defect formation enthalpy ΔH_s (eV) from the melting temperature of sillimanite (1473 K) using the empirical factor 2.14×10⁻³ eV/K.
2.  Convert the formation enthalpy to a silicon vacancy site fraction X_Si,v through the equilibrium relation for a vacancy-forming quasi-chemical reaction, assuming the Gibbs free energy of formation ΔG_f equals ΔH_s.
3.  Convert the formation enthalpy to joules per defect, then combine the site fraction with Avogadro's number and the per-defect energy to obtain the excess molar energy (J/mol).
All required physical constants (gas constant R, Avogadro's number, eV-to-J conversion) are publicly available and may be hardcoded.

## Reproduction target
The reproduction target is to compute the four quantities that characterize the thermodynamic contribution of Schottky vacancies in sillimanite at its melting temperature, as derived from the empirical formation enthalpy relation and the vacancy equilibrium expression. Submit the output as a single JSON object in /app/outputs/vacancy_defect_results.json with the keys delta_H_s_eV, X_Si_v_per_mol, energy_per_defect_J, and excess_molar_energy_J_per_mol.

## Assets
No external datasets, models, or service accounts are needed. The only inputs are fundamental physical constants (gas constant R, Avogadro's number, the electronvolt–joule conversion factor) and the melting temperature of sillimanite (1473 K), all of which are publicly available and can be obtained from standard references or hardcoded.

## Workflow steps

### Step 1: Calculate vacancy defect properties
- Role: scored (load-bearing)
- Action: Compute the Schottky vacancy formation enthalpy ΔH_s (eV) from the melting temperature of sillimanite (1473 K) using the empirical relation ΔH_s = 2.14×10⁻³ T_m. Using the quasi-chemical equilibrium with the assumption ΔG_f = ΔH_s, compute the silicon vacancy site fraction X_Si,v (per mol) via X_Si,v = exp(−ΔH_s/(2RT)) after converting ΔH_s to joules. Convert ΔH_s to energy per defect in joules. Calculate the excess molar energy (J/mol) as X_Si,v × N_A × energy_per_defect. Write all four computed values to vacancy_defect_results.json.
- Output file: `/app/outputs/vacancy_defect_results.json`
- Format: json
- Contract: {"delta_H_s_eV": "number (eV)", "X_Si_v_per_mol": "number (per mol)", "energy_per_defect_J": "number (J)", "excess_molar_energy_J_per_mol": "number (J/mol)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_defect_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_defect_results.json
- path: `/app/outputs/vacancy_defect_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: All four computed vacancy defect quantities: formation enthalpy, site fraction, energy per defect, and excess molar energy.
- schema:
  - `type`: object
  - `required`:
    - `delta_H_s_eV`: number
    - `X_Si_v_per_mol`: number
    - `energy_per_defect_J`: number
    - `excess_molar_energy_J_per_mol`: number
  - `units`:
    - `delta_H_s_eV`: eV
    - `X_Si_v_per_mol`: per mol
    - `energy_per_defect_J`: J
    - `excess_molar_energy_J_per_mol`: J/mol

Notes: The task is limited to the Schottky vacancy calculation as specified in the pre-scan; the paper’s dislocation strain energy and planar defect discussions are not included because they lack fully provided parameters (do_not_attempt). No external data fetch is required; all constants (melting temperature, R, N_A, eV-to-J) are publicly available and can be hardcoded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_defect_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_H_s_eV": "number",
          "X_Si_v_per_mol": "number",
          "energy_per_defect_J": "number",
          "excess_molar_energy_J_per_mol": "number"
        },
        "units": {
          "delta_H_s_eV": "eV",
          "X_Si_v_per_mol": "per mol",
          "energy_per_defect_J": "J",
          "excess_molar_energy_J_per_mol": "J/mol"
        }
      },
      "description": "All four computed vacancy defect quantities: formation enthalpy, site fraction, energy per defect, and excess molar energy."
    }
  ],
  "notes": "The task is limited to the Schottky vacancy calculation as specified in the pre-scan; the paper’s dislocation strain energy and planar defect discussions are not included because they lack fully provided parameters (do_not_attempt). No external data fetch is required; all constants (melting temperature, R, N_A, eV-to-J) are publicly available and can be hardcoded."
}
```

## How you are scored
A hidden verifier independently recomputes each of the four quantities using the same formulas and fundamental constants. It then compares your submitted values with the recomputed ones. Full credit requires all four quantities to be correct; minor deviations due to floating-point error are permitted within a hidden tolerance. You must ensure that your calculations are free of arithmetic or unit-conversion errors.
