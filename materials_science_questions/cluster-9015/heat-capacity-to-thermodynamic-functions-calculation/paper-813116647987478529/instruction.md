# Thermodynamic functions of H2-N2-NH3 mixtures from PV isotherms

## Problem background
The thermodynamic properties of hydrogen-nitrogen-ammonia gas mixtures are of critical importance for ammonia synthesis processes. Compressibility isotherms (PVT data) for such mixtures have been measured experimentally, and from these data one can derive key thermodynamic functions—entropy, enthalpy, internal energy, and isobaric heat capacity—as functions of temperature and pressure. Accurately computing these functions from the measured PV data is a classic numerical task that links experimental measurements to usable thermodynamic quantities.

## Approach
The core workflow consists of two stages. First, experimental PV data (in Amagat units) for each mixture and temperature are fitted to a cubic polynomial in density: PV = A + B·d + C·d² + Z·d³, where d is the density in Amagat units. The coefficient A must correspond to RT, the ideal gas limit. Second, from these polynomial representations and the known zero-pressure heat capacities of the pure components (H₂, N₂, NH₃), the thermodynamic functions S, H, U, and Cp are computed by numerically integrating the standard thermodynamic relations: (∂S/∂P)_T = –(∂V/∂T)_P, (∂H/∂P)_T = V – T(∂V/∂T)_P, and (∂U/∂P)_T = –T(∂V/∂T)_P – P(∂V/∂P)_T, together with the definition Cp = (∂H/∂T)_P. The integration is carried out from the zero-pressure limit up to the target pressure at each temperature of interest, using the fitted PV function to evaluate the integrands. The zero-pressure heat capacities of the mixture are obtained as a mole-fraction-weighted sum of the pure-component Cp values.

## Reproduction target
Produce three CSV files, one for each H₂–N₂–NH₃ mixture with analyzed compositions: (1) 66.5% H₂, 26.4% N₂, 7.1% NH₃; (2) 60.1% H₂, 27.6% N₂, 12.3% NH₃; (3) 58.56% H₂, 23.88% N₂, 17.56% NH₃. Each file must contain the computed entropy S (cal/mol·K), enthalpy H (cal/mol), internal energy U (cal/mol), and isobaric heat capacity Cp (cal/mol·K) at temperatures 50, 75, 100, 125, 150 °C and pressures 1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300 international atmospheres. The required columns are: P_int_atm, T_C, S_cal_mol_K, H_cal_mol, U_cal_mol, Cp_cal_mol_K.

## Assets

- Experimental PV isotherm data (Amagat units) for three H2-N2-NH3 mixtures
- Zero-pressure heat capacities of pure H2, N2, NH3
- Mixture metadata and conversion factors (Table I)

## Workflow steps

### Step 1: Fit cubic PV polynomials
- Role: process
- Action: From the provided experimental PV isotherm data and mixture metadata, fit a power series PV = A + B*d + C*d^2 + Z*d^3 to the data for each mixture and temperature. Obtain coefficients A, B, C, Z. Save the coefficients as a structured JSON file.
- Evidence: `/app/outputs/pv_coefficients.json`

### Step 2: Compute thermodynamic functions for mixture 1 (66.5:26.4:7.1)
- Role: scored (load-bearing)
- Action: From the polynomial coefficients for this mixture and the zero-pressure heat capacity data of pure components, compute using numerical integration the entropy S, enthalpy H, internal energy U, and constant-pressure heat capacity Cp at temperatures 50, 75, 100, 125, 150 °C and pressures 1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300 international atmospheres. Output a CSV file.
- Output file: `/app/outputs/thermo_functions_mix1.csv`
- Format: csv
- Contract: P_int_atm, T_C, S_cal_mol_K, H_cal_mol, U_cal_mol, Cp_cal_mol_K
- Scoring: scored by hidden verifier

### Step 3: Compute thermodynamic functions for mixture 2 (60.1:27.6:12.3)
- Role: scored
- Action: Analogous computation for the second mixture. Output a CSV file.
- Output file: `/app/outputs/thermo_functions_mix2.csv`
- Format: csv
- Contract: P_int_atm, T_C, S_cal_mol_K, H_cal_mol, U_cal_mol, Cp_cal_mol_K
- Scoring: scored by hidden verifier

### Step 4: Compute thermodynamic functions for mixture 3 (58.56:23.88:17.56)
- Role: scored
- Action: Analogous computation for the third mixture. Output a CSV file.
- Output file: `/app/outputs/thermo_functions_mix3.csv`
- Format: csv
- Contract: P_int_atm, T_C, S_cal_mol_K, H_cal_mol, U_cal_mol, Cp_cal_mol_K
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_functions_mix1.csv`
- `/app/outputs/thermo_functions_mix2.csv`
- `/app/outputs/thermo_functions_mix3.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_functions_mix1.csv
- path: `/app/outputs/thermo_functions_mix1.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic functions for the 66.5% H2 mixture.
- schema:
  - `type`: table
  - `required_columns`: `P_int_atm`, `T_C`, `S_cal_mol_K`, `H_cal_mol`, `U_cal_mol`, `Cp_cal_mol_K`
  - `units`:
    - `P_int_atm`: international atmosphere
    - `T_C`: degree Celsius
    - `S_cal_mol_K`: cal/(mol·K)
    - `H_cal_mol`: cal/mol
    - `U_cal_mol`: cal/mol
    - `Cp_cal_mol_K`: cal/(mol·K)

### thermo_functions_mix2.csv
- path: `/app/outputs/thermo_functions_mix2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic functions for the 60.1% H2 mixture.
- schema:
  - `type`: table
  - `required_columns`: `P_int_atm`, `T_C`, `S_cal_mol_K`, `H_cal_mol`, `U_cal_mol`, `Cp_cal_mol_K`
  - `units`:
    - `P_int_atm`: international atmosphere
    - `T_C`: degree Celsius
    - `S_cal_mol_K`: cal/(mol·K)
    - `H_cal_mol`: cal/mol
    - `U_cal_mol`: cal/mol
    - `Cp_cal_mol_K`: cal/(mol·K)

### thermo_functions_mix3.csv
- path: `/app/outputs/thermo_functions_mix3.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic functions for the 58.56% H2 mixture.
- schema:
  - `type`: table
  - `required_columns`: `P_int_atm`, `T_C`, `S_cal_mol_K`, `H_cal_mol`, `U_cal_mol`, `Cp_cal_mol_K`
  - `units`:
    - `P_int_atm`: international atmosphere
    - `T_C`: degree Celsius
    - `S_cal_mol_K`: cal/(mol·K)
    - `H_cal_mol`: cal/mol
    - `U_cal_mol`: cal/mol
    - `Cp_cal_mol_K`: cal/(mol·K)

Notes: The verifier compares selected (T,P) conditions to reference values with appropriate tolerances. All outputs must include the required columns with numeric values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_functions_mix1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "P_int_atm",
          "T_C",
          "S_cal_mol_K",
          "H_cal_mol",
          "U_cal_mol",
          "Cp_cal_mol_K"
        ],
        "units": {
          "P_int_atm": "international atmosphere",
          "T_C": "degree Celsius",
          "S_cal_mol_K": "cal/(mol·K)",
          "H_cal_mol": "cal/mol",
          "U_cal_mol": "cal/mol",
          "Cp_cal_mol_K": "cal/(mol·K)"
        }
      },
      "description": "Computed thermodynamic functions for the 66.5% H2 mixture."
    },
    {
      "file": "thermo_functions_mix2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "P_int_atm",
          "T_C",
          "S_cal_mol_K",
          "H_cal_mol",
          "U_cal_mol",
          "Cp_cal_mol_K"
        ],
        "units": {
          "P_int_atm": "international atmosphere",
          "T_C": "degree Celsius",
          "S_cal_mol_K": "cal/(mol·K)",
          "H_cal_mol": "cal/mol",
          "U_cal_mol": "cal/mol",
          "Cp_cal_mol_K": "cal/(mol·K)"
        }
      },
      "description": "Computed thermodynamic functions for the 60.1% H2 mixture."
    },
    {
      "file": "thermo_functions_mix3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "P_int_atm",
          "T_C",
          "S_cal_mol_K",
          "H_cal_mol",
          "U_cal_mol",
          "Cp_cal_mol_K"
        ],
        "units": {
          "P_int_atm": "international atmosphere",
          "T_C": "degree Celsius",
          "S_cal_mol_K": "cal/(mol·K)",
          "H_cal_mol": "cal/mol",
          "U_cal_mol": "cal/mol",
          "Cp_cal_mol_K": "cal/(mol·K)"
        }
      },
      "description": "Computed thermodynamic functions for the 58.56% H2 mixture."
    }
  ],
  "notes": "The verifier compares selected (T,P) conditions to reference values with appropriate tolerances. All outputs must include the required columns with numeric values."
}
```

## How you are scored
Each of the three output CSVs is checked independently by a hidden verifier. For each mixture, the verifier extracts the agent’s computed values at a subset of the specified (T, P) conditions and compares them against reference values derived from the original experimental measurements. A point is considered correct if its deviation falls within the verifier’s prescribed absolute tolerance. The reward for each mixture is the fraction of compared points that are within tolerance, and the final reward is an equally weighted average across the three mixtures. Simply reporting a number that matches the reference is not sufficient—the entire CSV tables must be produced and must result from the required computational pipeline.
