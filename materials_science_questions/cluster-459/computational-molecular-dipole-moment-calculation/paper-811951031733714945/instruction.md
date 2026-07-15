# HF/6-31G(d) Calculation of Molecular Dipole Moments in Gas and THF Solvent

## Problem background
Succinic acid (SA) and maleic acid (MA) are dicarboxylic acids whose dipole moments and conformational preferences in solution are of interest for understanding solvation and hydrogen-bonding effects. The computational component of the study calculates total electronic energies and dipole moments for SA in gauche and trans conformations, and for MA, at the Hartree-Fock level with the 6-31G(d) basis set. Calculations are performed both in the gas phase and with an implicit solvent model (Onsager reaction field) for tetrahydrofuran (THF) to estimate the solvent's influence on the molecular properties. The resulting dipole moments can be compared with experimental data to assess the degree of solvation.

## Approach
Build initial 3D structures for succinic acid (gauche and trans) and maleic acid. Optimize each geometry at the HF/6-31G(d) level of theory in the gas phase. Then apply the Onsager self-consistent reaction field model with the dielectric constant of THF (ε = 7.14) to compute the total electronic energy and dipole moment in implicit solvent. Assemble the gas-phase and solvated results into a single CSV table.

## Reproduction target
Produce a CSV file `dipole_results.csv` with columns `system`, `conformation`, `solvent`, `total_energy`, `dipole_moment`. It must contain one row for each of the six system–solvent combinations: SA in gauche conformation (gas), SA in gauche conformation (THF), SA in trans conformation (gas), SA in trans conformation (THF), MA (gas), and MA (THF). Report `total_energy` in Hartree and `dipole_moment` in Debye, computed at the HF/6-31G(d) level with Onsager solvation where applicable.

## Assets

- Open-source quantum chemistry package (e.g., Psi4, ORCA): https://psicode.org/
- Molecular structures of succinic acid, maleic acid, and tetrahydrofuran

## Workflow steps

### Step 1: Generate initial geometries
- Role: process
- Action: Build reasonable starting 3D geometries for succinic acid (SA) in gauche and trans conformations, and for maleic acid (MA). Structures may be retrieved from public databases or manually constructed using chemical intuition.
- Evidence: none

### Step 2: Gas-phase HF/6-31G(d) geometry optimization
- Role: process
- Action: For each system (SA gauche, SA trans, MA), perform a Hartree-Fock geometry optimization at the 6-31G(d) basis set in the gas phase. Record the total energy and dipole moment.
- Evidence: `/app/outputs/gas_opt_outputs.log`

### Step 3: Onsager solvation model calculation in THF
- Role: process
- Action: For each optimized geometry from the gas-phase step, perform a self-consistent field calculation using the Onsager solvation model with the dielectric constant of tetrahydrofuran (THF, ε=7.14) at the HF/6-31G(d) level. Record the total energy and dipole moment in the solvent.
- Evidence: `/app/outputs/solvation_outputs.log`

### Step 4: Assemble results into CSV
- Role: scored (load-bearing)
- Action: Compile the gas-phase and THF total energies and dipole moments for all systems into a CSV file. Each row corresponds to one system-solvent combination, with columns: system, conformation, solvent, total_energy, dipole_moment.
- Output file: `/app/outputs/dipole_results.csv`
- Format: csv
- Contract: Columns: system (string, 'SA' or 'MA'), conformation (string, 'gauche' or 'trans' for SA, 'MA' for MA), solvent (string, 'gas' or 'THF'), total_energy (float, Hartree), dipole_moment (float, Debye).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_results.csv
- path: `/app/outputs/dipole_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed total electronic energy and dipole moment for succinic acid and maleic acid in gas phase and in THF implicit solvent using HF/6-31G(d) with Onsager solvation.
- schema:
  - `type`: table
  - `required_columns`: `system`, `conformation`, `solvent`, `total_energy`, `dipole_moment`
  - `units`:
    - `total_energy`: Hartree
    - `dipole_moment`: Debye

Notes: The dipole moment values are to be computed at the HF/6-31G(d) level of theory, not STO-3G. The Onsager solvation model is applied with the experimentally determined dielectric constant of THF (ε=7.14). The target values for comparison are the paper's reported HF/6-31G(d) results from Table 4. Tolerances are set to account for small implementation differences between quantum chemistry packages.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "conformation",
          "solvent",
          "total_energy",
          "dipole_moment"
        ],
        "units": {
          "total_energy": "Hartree",
          "dipole_moment": "Debye"
        }
      },
      "description": "Computed total electronic energy and dipole moment for succinic acid and maleic acid in gas phase and in THF implicit solvent using HF/6-31G(d) with Onsager solvation."
    }
  ],
  "notes": "The dipole moment values are to be computed at the HF/6-31G(d) level of theory, not STO-3G. The Onsager solvation model is applied with the experimentally determined dielectric constant of THF (ε=7.14). The target values for comparison are the paper's reported HF/6-31G(d) results from Table 4. Tolerances are set to account for small implementation differences between quantum chemistry packages."
}
```

## How you are scored
A hidden verifier will read your `dipole_results.csv` and compare each row's `total_energy` and `dipole_moment` to reference values obtained from the underlying study. Every row whose values fall within the verifier's hidden tolerances contributes an equal share of the total reward. The output must match the required CSV format and contain reasonable numeric values derived from the specified quantum chemical procedure.
