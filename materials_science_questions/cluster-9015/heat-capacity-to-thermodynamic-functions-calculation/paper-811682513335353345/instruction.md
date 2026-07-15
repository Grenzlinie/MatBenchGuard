# Heat capacity and thermodynamic functions of lithium cobaltate

## Problem background
Lithium cobaltate (LiCoO2) crystallizes in two modifications: a high-temperature (HT) phase with a layered α-NaFeO2 structure and a low-temperature (LT) phase with a spinel structure. The thermodynamic properties of these phases—heat capacity, enthalpy, and entropy—are essential for understanding their stability and for optimizing synthesis and processing. This work reports differential scanning calorimetry (DSC) measurements of heat capacity for both HT and LT LiCoO2 and fits the data to a Haas-Fisher polynomial. From these polynomial fits, relative enthalpy increments and entropy increments are obtained by numerical integration. This reproduction task computes those thermodynamic quantities from the published polynomial coefficients.

## Approach
The heat capacity Cp(T) is modeled by the Haas-Fisher polynomial:

Cp(T) = a0 + a1*T + a2*T^2 + a3*T^{-0.5} + a4*T^{-2}

For each phase (HT and LT), the polynomial coefficients (a0, a1, a2, a3, a4) are provided. After computing Cp at a set of temperatures, the relative enthalpy increment ΔH(T) = ∫_{T_min}^{T} Cp dT and the relative entropy increment ΔS(T) = ∫_{T_min}^{T} (Cp/T) dT are obtained by numerical integration (e.g., trapezoidal rule) from the lowest measured temperature T_min to each target temperature. This yields a table of computed thermodynamic functions for each phase.

## Reproduction target
Using the Haas-Fisher polynomial coefficients given for the HT and LT phases, compute the heat capacity Cp and the integrated thermodynamic functions (enthalpy increment H_diff and entropy increment S_diff) at the temperatures specified in the workflow step. Output a single CSV file named thermodynamic_functions.csv containing columns: Phase, T_K, Cp_J_mol_K, H_diff_J_mol, S_diff_J_mol_K.

## Assets

- numpy: numpy
- scipy: scipy
- pandas: pandas

## Workflow steps

### Step 1: Compute Cp and thermodynamic functions
- Role: scored (load-bearing)
- Action: Implement the Haas-Fisher polynomial for heat capacity: Cp(T) = a0 + a1*T + a2*T^2 + a3*T^{-0.5} + a4*T^{-2}. Use the published coefficients for the HT and LT phases. For each phase, compute Cp at every temperature listed in the paper's Table 2 (HT: 180–570 K; LT: 140–570 K, including 298.15 K). Numerically integrate Cp from the lowest temperature T_min to each T to obtain the enthalpy increment H_diff(T) = ∫_{T_min}^{T} Cp dT, and integrate Cp/T to obtain the entropy increment S_diff(T) = ∫_{T_min}^{T} (Cp/T) dT. Write the results to a CSV file with columns Phase, T_K, Cp_J_mol_K, H_diff_J_mol, S_diff_J_mol_K.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: Phase (string: 'HT' or 'LT'), T_K (float, temperature in Kelvin), Cp_J_mol_K (float, heat capacity in J/(mol·K)), H_diff_J_mol (float, enthalpy increment in J/mol), S_diff_J_mol_K (float, entropy increment in J/(mol·K))
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed heat capacity and thermodynamic functions for HT and LT LiCoO2, compared to the paper's reference values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `Phase`, `T_K`, `Cp_J_mol_K`, `H_diff_J_mol`, `S_diff_J_mol_K`
  - `units`:
    - `T_K`: K
    - `Cp_J_mol_K`: J/(mol*K)
    - `H_diff_J_mol`: J/mol
    - `S_diff_J_mol_K`: J/(mol*K)

Notes: The computed values are derived from the polynomial coefficients and numerical integration; the checker validates them against the paper's reported thermodynamic data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Phase",
          "T_K",
          "Cp_J_mol_K",
          "H_diff_J_mol",
          "S_diff_J_mol_K"
        ],
        "units": {
          "T_K": "K",
          "Cp_J_mol_K": "J/(mol*K)",
          "H_diff_J_mol": "J/mol",
          "S_diff_J_mol_K": "J/(mol*K)"
        }
      },
      "description": "Computed heat capacity and thermodynamic functions for HT and LT LiCoO2, compared to the paper's reference values with appropriate tolerances."
    }
  ],
  "notes": "The computed values are derived from the polynomial coefficients and numerical integration; the checker validates them against the paper's reported thermodynamic data."
}
```

## How you are scored
A hidden verifier examines your CSV file. For each row (phase, temperature), it compares your computed Cp, H_diff, and S_diff against independently derived reference values using pre-defined tolerances that account for reasonable numerical integration differences. The overall score is proportional to the fraction of rows where all three quantities fall within their respective tolerances. Simply copying published numbers without correctly implementing the polynomial and integration will not meet the tolerance requirements.
