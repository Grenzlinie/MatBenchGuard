# Thermodynamic Model of Carbothermal Oxide Reduction

## Problem background
Carbothermal reduction of FeO, CoO, NiO, and Cu₂O by carbon is a longstanding metallurgical process. A proposed mechanism suggests that the oxide decomposes via dissociative evaporation: the oxide separates into gaseous products while the low-volatile metal simultaneously condenses at the oxide/metal interface. Part of the condensation energy is transferred back to the reactant, accelerating the decomposition. This thermodynamic model can, in principle, predict the initial temperature at which decomposition begins, the activation energy for different evaporation regimes, and the equilibrium partial pressures of metal vapour and oxygen. Your task is to implement this dissociative-evaporation model with condensation-energy transfer and compute these quantities, then compare the results with the experimental reference data provided.

## Approach
The model extends Hertz–Langmuir evaporation theory to dissociative evaporation of a compound S(s) → a A(g) + b B(g). The evaporation rate depends on the equilibrium constant and on whether the decomposition occurs in an equimolar mode (no excess of any product) or an isobaric mode (one gaseous product, e.g. O₂, maintains a fixed partial pressure). The activation energy for each mode is proportional to the reaction enthalpy, corrected for a fraction τ of the condensation energy of the low-volatile product that is assumed to transfer back to the reactant; here τ = 0.5. Equilibrium partial pressures of metal vapour from oxide dissociation and from pure metal evaporation, as well as the oxygen partial pressure from the condensate dissociation MO(s) → M(s) + ½ O₂, follow from standard thermodynamic relations and the provided enthalpy and entropy changes. All required thermodynamic functions (ΔH° and ΔS° at 1000 K, 1300 K, and 1600 K for each relevant reaction) are supplied as constants. You will implement the governing equations, solve for the unknown temperatures and pressures numerically (e.g., root-finding), and produce the three output tables described in the workflow steps.

## Reproduction target
Using the supplied thermodynamic constants and the dissociative evaporation model with τ = 0.5:

1. Compute the theoretical initial decomposition temperature for each oxide under an oxygen partial pressure of 1×10⁻⁷ atm. Merge the computed temperatures with the experimental values from the bundled experimental-reference CSV file and write the full table to /app/outputs/initial_temperatures.csv.

2. Calculate the activation energies for the equimolar and isobaric modes for FeO, the equimolar mode for NiO, and the equimolar mode for Cu₂O. Output the results as /app/outputs/activation_energies.csv.

3. Evaluate the equilibrium metal-vapour pressures for gaseous dissociation of each oxide and for evaporation of the corresponding metal at 1700 K (FeO, CoO, NiO) and at 1500 K and 1300 K (Cu₂O). Then compute the equilibrium oxygen partial pressure for the condensate dissociation MO(s) → M(s) + ½ O₂ at the same temperatures, and merge with the experimental Knudsen-cell oxygen pressures from the bundled experimental-reference CSV. Save this table as /app/outputs/equilibrium_pressures.csv.

## Assets

- Experimental reference data for initial temperatures and Knudsen-cell oxygen pressures
- Python 3: python3

## Thermodynamic constants

The following thermodynamic functions are used in all calculations.  
Values of ΔrH_T^0 (kJ mol⁻¹) and ΔrS_T^0 (J mol⁻¹ K⁻¹) are given at 1000 K, 1300 K, and 1600 K (except Cu species at 1500 K).

| Reaction | ΔrH (1000 K) | ΔrH (1300 K) | ΔrH (1600 K) | ΔrS (1000 K) | ΔrS (1300 K) | ΔrS (1600 K) |
|----------|--------------|--------------|--------------|--------------|--------------|--------------|
| Fe (s) = Fe (g) | 409.5 | 402.1 | 398.0 | 143.4 | 136.7 | 131.0 |
| FeO (s) = Fe (g) + ½ O₂ | 675.7 | 669.4 | 662.6 | 205.2 | 199.7 | 195.0 |
| FeO (s) = Fe (s) + ½ O₂ | 266.1 | 267.4 | 264.6 | 61.8 | 63.0 | 64.1 |
| Co (s) = Co (g) | 424.5 | 419.9 | 414.7 | 143.8 | 139.7 | 136.1 |
| CoO (s) = Co (g) + ½ O₂ | 662.9 | 659.1 | 654.0 | 213.5 | 210.0 | 206.8 |
| CoO (s) = Co (s) + ½ O₂ | 238.4 | 239.2 | 239.3 | 69.7 | 70.3 | 70.6 |
| Ni (s) = Ni (g) | 424.2 | 421.3 | 417.7 | 144.7 | 142.0 | 139.6 |
| NiO (s) = Ni (g) + ½ O₂ | 663.5 | 659.5 | 653.6 | 230.4 | 226.8 | 223.4 |
| NiO (s) = Ni (s) + ½ O₂ | 239.3 | 238.2 | 236.8 | 85.7 | 84.8 | 83.8 |
| Cu (s) = Cu (g) | 332.8 | 330.8 | 315.8* | 126.2 | 124.0 | 113.1* |
| Cu₂O (s) = 2 Cu (g) + ½ O₂ | 838.8 | 830.5 | 822.8* | 319.2 | 313.5 | 308.3* |
| Cu₂O (s) = 2 Cu (s/l) + ½ O₂ | 172.8 | 168.8 | 187.8* | 66.0 | 65.5 | 82.2* |

*For Cu species, the 1600 K column corresponds to 1500 K.

## Workflow steps

### Step 1: Compute initial decomposition temperatures
- Role: scored
- Action: Calculate theoretical initial decomposition temperatures for FeO, CoO, NiO, Cu2O using the dissociative evaporation model with condensation energy transfer coefficient τ=0.5 and the provided thermodynamic functions. Merge the computed temperatures with experimental values from the bundled experimental-reference CSV file.
- Output file: `/app/outputs/initial_temperatures.csv`
- Format: csv
- Contract: Oxide (string), T_calc_K (float, theoretical initial temperature in K), T_expt_vacuum_K (float, experimental temperature under vacuum in K), T_expt_1atm_Ar_K (float, experimental temperature under 1 atm Ar in K).
- Scoring: scored by hidden verifier

### Step 2: Compute activation energies
- Role: scored (load-bearing)
- Action: Compute activation energies for the equimolar and isobaric evaporation modes using the dissociative evaporation model with τ=0.5. Include FeO (equimolar and isobaric), NiO (equimolar), and Cu2O (equimolar).
- Output file: `/app/outputs/activation_energies.csv`
- Format: csv
- Contract: Oxide (string, e.g., FeO), Mode (string, Equimolar or Isobaric), Ea_calculated_kJ_per_mol (float, activation energy in kJ/mol).
- Scoring: scored by hidden verifier

### Step 3: Compute equilibrium pressures
- Role: scored
- Action: Calculate equilibrium metal-vapor pressures for gaseous dissociation of each oxide and for evaporation of the corresponding metal at specified temperatures (1700 K for FeO/CoO/NiO; 1500 K and 1300 K for Cu2O). Also compute the equilibrium oxygen partial pressure for the condensate dissociation (MO(s) = M(s) + 1/2 O2) and merge with experimental Knudsen-cell oxygen pressures from the bundled experimental-reference CSV file.
- Output file: `/app/outputs/equilibrium_pressures.csv`
- Format: csv
- Contract: Oxide (string), T_K (int, temperature in K), P_M_dissociation_atm (float, metal pressure from dissociation in atm), P_M_evaporation_atm (float, metal pressure from evaporation in atm), P_O2_calculated_condensate_atm (float, O2 pressure from condensate dissociation in atm), P_O2_experimental_atm (float, experimental O2 pressure from literature in atm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/initial_temperatures.csv`
- `/app/outputs/activation_energies.csv`
- `/app/outputs/equilibrium_pressures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### initial_temperatures.csv
- path: `/app/outputs/initial_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Theoretical initial decomposition temperatures computed from the dissociative evaporation model, alongside experimental reference values.
- schema:
  - `type`: table
  - `required_columns`: `Oxide`, `T_calc_K`, `T_expt_vacuum_K`, `T_expt_1atm_Ar_K`
  - `units`:
    - `T_calc_K`: K
    - `T_expt_vacuum_K`: K
    - `T_expt_1atm_Ar_K`: K

### activation_energies.csv
- path: `/app/outputs/activation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Activation energies for oxide decomposition under equimolar and isobaric evaporation modes.
- schema:
  - `type`: table
  - `required_columns`: `Oxide`, `Mode`, `Ea_calculated_kJ_per_mol`
  - `units`:
    - `Ea_calculated_kJ_per_mol`: kJ/mol

### equilibrium_pressures.csv
- path: `/app/outputs/equilibrium_pressures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium metal-vapor and oxygen partial pressures computed for gaseous dissociation, evaporation, and condensate dissociation, with literature experimental oxygen pressures.
- schema:
  - `type`: table
  - `required_columns`: `Oxide`, `T_K`, `P_M_dissociation_atm`, `P_M_evaporation_atm`, `P_O2_calculated_condensate_atm`, `P_O2_experimental_atm`
  - `units`:
    - `T_K`: K
    - `P_M_dissociation_atm`: atm
    - `P_M_evaporation_atm`: atm
    - `P_O2_calculated_condensate_atm`: atm
    - `P_O2_experimental_atm`: atm

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "initial_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Oxide",
          "T_calc_K",
          "T_expt_vacuum_K",
          "T_expt_1atm_Ar_K"
        ],
        "units": {
          "T_calc_K": "K",
          "T_expt_vacuum_K": "K",
          "T_expt_1atm_Ar_K": "K"
        }
      },
      "description": "Theoretical initial decomposition temperatures computed from the dissociative evaporation model, alongside experimental reference values."
    },
    {
      "file": "activation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Oxide",
          "Mode",
          "Ea_calculated_kJ_per_mol"
        ],
        "units": {
          "Ea_calculated_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Activation energies for oxide decomposition under equimolar and isobaric evaporation modes."
    },
    {
      "file": "equilibrium_pressures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Oxide",
          "T_K",
          "P_M_dissociation_atm",
          "P_M_evaporation_atm",
          "P_O2_calculated_condensate_atm",
          "P_O2_experimental_atm"
        ],
        "units": {
          "T_K": "K",
          "P_M_dissociation_atm": "atm",
          "P_M_evaporation_atm": "atm",
          "P_O2_calculated_condensate_atm": "atm",
          "P_O2_experimental_atm": "atm"
        }
      },
      "description": "Equilibrium metal-vapor and oxygen partial pressures computed for gaseous dissociation, evaporation, and condensate dissociation, with literature experimental oxygen pressures."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each of the three CSV files. The verifier reads every computed numeric value (initial temperatures, activation energies, partial pressures) and compares them against the expected results derived from the model using tolerances that account for legitimate differences in numerical implementation. The experimental reference columns are validated but contribute only a small weighting. Each output artifact receives a score, and the final reward is the weighted combination of these scores. A higher reward means closer agreement with the reference. Simply producing files with the correct columns is not sufficient; the accuracy of the calculated values determines your score.
