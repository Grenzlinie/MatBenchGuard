# Compute thermodynamic functions and residual entropies from low-temperature Cp data for oxide glasses

## Problem background
Understanding the thermophysical properties of simple oxide glasses such as GeO2 and B2O3 is important for interpreting their structure and low-energy vibrational behavior. The low-temperature molar heat capacity (Cp) provides a sensitive probe of the vibrational density of states, and from it one can derive the entropy, enthalpy increment, and Gibbs free energy function. These thermodynamic data, when combined with high-temperature Cp equations for the crystal and liquid phases, allow the calculation of the residual entropy—the thermodynamic measure of disorder frozen in at the glass transition. This task provides the experimental Cp data for two glasses and challenges you to compute the corresponding thermodynamic functions and the residual entropy at absolute zero.

## Approach
The computation proceeds in two stages. First, for each glass, the provided low-temperature Cp versus temperature data are numerically integrated using the trapezoidal rule to obtain the entropy difference S(T)-S(0) and the enthalpy increment H(T)-H(0) at every measured point. These values are then interpolated (e.g., linearly) onto a common temperature grid from 5 K to 350 K and the derived Gibbs free energy function −(G(T)-H(0))/T is computed as S(T) − H(T)/T. Second, the residual entropy at 0 K is determined from a thermodynamic entropy cycle that combines the glass, crystal, and liquid heat capacities. The glass contribution up to 350 K comes from the low-temperature data; above 350 K and for the crystal and liquid branches, given high-temperature polynomial equations are used. The cycle also involves the fusion entropy and the fictive temperatures of the glasses, all supplied as ancillary constants. All required integrations are again carried out numerically.

## Reproduction target
Given the molar heat capacity tables (T, Cp) for GeO2 and B2O3 glasses provided below, numerically integrate Cp/T and Cp to obtain S(T)-S(0) and H(T)-H(0), then interpolate to the temperature grid: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350 K. Compute the Gibbs free energy function −(G(T)-H(0))/T for each temperature. Output the results as two CSV files (one per glass) with columns for T, S(T)-S(0), H(T)-H(0), and −(G(T)-H(0))/T. Finally, using the provided high-temperature Cp equations for the glass (above 273 K), crystal, and liquid, together with the given fusion entropies and fictive temperatures, evaluate the entropy cycle to compute the residual entropy at 0 K for each glass. Output a JSON object with keys "GeO2" and "B2O3" holding those residual entropy values in J/(mol·K).

## Assets

- Low-temperature Cp data for GeO2 glass
- Low-temperature Cp data for B2O3 glass
- High-temperature Cp equations and ancillary thermodynamic data

## Workflow steps

### Step 1: Compute thermodynamic functions for GeO2 glass
- Role: scored
- Action: From the provided low-temperature Cp data for GeO2 glass (Table 1) in the instruction, numerically integrate Cp/T and Cp vs T using the trapezoidal rule to obtain S(T)-S(0) and H(T)-H(0) at the raw measurement points. Then interpolate (e.g., linear interpolation) to generate values at the required temperature grid (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350 K). Compute the Gibbs free energy function -(G(T)-H(0))/T = S(T) - H(T)/T. Output the table as CSV.
- Output file: `/app/outputs/geO2_thermodynamic_functions.csv`
- Format: csv
- Contract: Header: T(K), S_T_minus_S0(J/mol_K), H_T_minus_H0(J/mol), minus_G_T_minus_H0_over_T(J/mol_K). Comma delimiter. All numeric columns. Temperatures exactly as listed in the action.
- Scoring: scored by hidden verifier

### Step 2: Compute thermodynamic functions for B2O3 glass
- Role: scored
- Action: From the provided low-temperature Cp data for B2O3 glass (Table 2) in the instruction, numerically integrate Cp/T and Cp vs T using the trapezoidal rule to obtain S(T)-S(0) and H(T)-H(0) at the raw measurement points. Then interpolate to the same temperature grid as for GeO2 (5 K to 350 K in steps). Compute -(G(T)-H(0))/T = S(T) - H(T)/T. Output as CSV.
- Output file: `/app/outputs/b2O3_thermodynamic_functions.csv`
- Format: csv
- Contract: Same header as GeO2 file: T(K), S_T_minus_S0(J/mol_K), H_T_minus_H0(J/mol), minus_G_T_minus_H0_over_T(J/mol_K). Comma delimiter. All numeric.
- Scoring: scored by hidden verifier

### Step 3: Calculate residual entropies at 0 K
- Role: scored (load-bearing)
- Action: Using the entropy cycle formula Sg(0) = ∫_0^Tf (Cp_c/T) dT + ΔS_f + ∫_Tf^Tg (Cp_l/T) dT - ∫_0^Tg (Cp_g/T) dT, compute residual entropy at 0 K for GeO2 (Tg=980 K) and B2O3 (Tg=543 K). High-temperature Cp equations for glass, crystal, and liquid phases, fusion entropies, and fictive temperatures are provided in the instruction. Perform the necessary integrations numerically (e.g., trapezoidal rule) from 0 K to the required limits, using the low-temperature data from previous steps for the glass up to 350 K and the given equations beyond. Output a JSON with the two values.
- Output file: `/app/outputs/residual_entropies.json`
- Format: json
- Contract: Object with keys 'GeO2' and 'B2O3', each a float representing residual entropy in J/mol K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geO2_thermodynamic_functions.csv`
- `/app/outputs/b2O3_thermodynamic_functions.csv`
- `/app/outputs/residual_entropies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geO2_thermodynamic_functions.csv
- path: `/app/outputs/geO2_thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic functions for GeO2 glass: entropy, enthalpy increment, and derived Gibbs free energy function from 5 K to 350 K.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `S_T_minus_S0(J/mol_K)`, `H_T_minus_H0(J/mol)`, `minus_G_T_minus_H0_over_T(J/mol_K)`
  - `units`:
    - `T(K)`: K
    - `S_T_minus_S0(J/mol_K)`: J/mol K
    - `H_T_minus_H0(J/mol)`: J/mol
    - `minus_G_T_minus_H0_over_T(J/mol_K)`: J/mol K

### b2O3_thermodynamic_functions.csv
- path: `/app/outputs/b2O3_thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic functions for B2O3 glass: entropy, enthalpy increment, and derived Gibbs free energy function from 5 K to 350 K.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `S_T_minus_S0(J/mol_K)`, `H_T_minus_H0(J/mol)`, `minus_G_T_minus_H0_over_T(J/mol_K)`
  - `units`:
    - `T(K)`: K
    - `S_T_minus_S0(J/mol_K)`: J/mol K
    - `H_T_minus_H0(J/mol)`: J/mol
    - `minus_G_T_minus_H0_over_T(J/mol_K)`: J/mol K

### residual_entropies.json
- path: `/app/outputs/residual_entropies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Residual entropies at 0 K for GeO2 and B2O3 glasses, in J/mol K.
- schema:
  - `type`: object
  - `required`:
    - `GeO2`: number
    - `B2O3`: number
  - `units`:
    - `GeO2`: J/mol K
    - `B2O3`: J/mol K

Notes: All outputs are derived from provided low-temperature Cp data and given high-temperature equations; checker will recompute with tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geO2_thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "S_T_minus_S0(J/mol_K)",
          "H_T_minus_H0(J/mol)",
          "minus_G_T_minus_H0_over_T(J/mol_K)"
        ],
        "units": {
          "T(K)": "K",
          "S_T_minus_S0(J/mol_K)": "J/mol K",
          "H_T_minus_H0(J/mol)": "J/mol",
          "minus_G_T_minus_H0_over_T(J/mol_K)": "J/mol K"
        }
      },
      "description": "Thermodynamic functions for GeO2 glass: entropy, enthalpy increment, and derived Gibbs free energy function from 5 K to 350 K."
    },
    {
      "file": "b2O3_thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "S_T_minus_S0(J/mol_K)",
          "H_T_minus_H0(J/mol)",
          "minus_G_T_minus_H0_over_T(J/mol_K)"
        ],
        "units": {
          "T(K)": "K",
          "S_T_minus_S0(J/mol_K)": "J/mol K",
          "H_T_minus_H0(J/mol)": "J/mol",
          "minus_G_T_minus_H0_over_T(J/mol_K)": "J/mol K"
        }
      },
      "description": "Thermodynamic functions for B2O3 glass: entropy, enthalpy increment, and derived Gibbs free energy function from 5 K to 350 K."
    },
    {
      "file": "residual_entropies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GeO2": "number",
          "B2O3": "number"
        },
        "units": {
          "GeO2": "J/mol K",
          "B2O3": "J/mol K"
        }
      },
      "description": "Residual entropies at 0 K for GeO2 and B2O3 glasses, in J/mol K."
    }
  ],
  "notes": "All outputs are derived from provided low-temperature Cp data and given high-temperature equations; checker will recompute with tolerance."
}
```

## How you are scored
Your submission will be scored by a hidden verifier. The verifier independently recomputes the thermodynamic functions from the same Cp data you are given and compares your outputs within numerical tolerances. It also recomputes the residual entropy using the provided high-temperature equations and fusion data, checking your reported values. Each scored step (GeO2 functions, B2O3 functions, residual entropies) contributes a weighted fraction to the overall reward, with the residual entropy calculation carrying the largest weight. The verifier inspects only the files you write to /app/outputs; the paper's published numbers are not sufficient—you must generate the required quantities by executing the computations described.
