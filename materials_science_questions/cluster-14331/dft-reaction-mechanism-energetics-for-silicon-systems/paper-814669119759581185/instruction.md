# DFT Activation Energies for Quadricyclane-Silylethylene Cycloaddition

## Problem background
This task examines the cycloaddition of quadricyclane with silicon-substituted ethylenes. The reaction can produce tricyclononene derivatives, and different silylethylene substituents lead to different reactivities. Density functional theory (DFT) calculations have been used to compute activation energies for this process, providing insight into how the nature and position of the silyl groups affect the reactivity. In this task, you will recompute those activation energies using an open‑source DFT code.

## Approach
Model the reaction with density functional theory using the PBE functional and a double‑zeta basis set (e.g., def2‑SVP). For each ethylene derivative, optimise the van der Waals complex formed by quadricyclane and the ethylene, locate the transition state for the cycloaddition, and obtain the total electronic energy of both the complex and the transition state. The activation energy is then computed as E(transition state) – E(optimised complex), without zero‑point energy correction. This procedure will be repeated for all required silylethylenes.

## Reproduction target
Produce a CSV file named `activation_energies.csv` containing the computed activation energies. For each ethylene system (the eight silylethylenes designated 1‑8 and tetrakis(trichlorosilyl)ethylene), the CSV must have one row with the ethylene identifier (e.g., '1','2',…,'8','tetrakis') and the activation energy in kcal/mol. The hidden verifier will compare these values to a reference and check whether the relative ordering among the different ethylenes is correctly reproduced.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: DFT geometry optimizations and transition state searches
- Role: process
- Action: For each ethylene system (the eight silylethylenes designated 1-8 and tetrakis(trichlorosilyl)ethylene), build molecular geometries for quadricyclane and the ethylene, optimize the van der Waals complex of quadricyclane with the ethylene, perform a transition state search for the cycloaddition, and obtain the total electronic energies of the optimized complex and the transition state. Use an open-source DFT code with the PBE functional and a double-zeta basis set (e.g., def2-SVP).
- Evidence: `/app/outputs/dft_calculations.log`

### Step 2: Activation energy report
- Role: scored (load-bearing)
- Action: For each ethylene system, compute the activation energy as E(transition state) – E(optimized van der Waals complex) in kcal/mol, without zero-point energy correction. Write a CSV file containing the results.
- Output file: `/app/outputs/activation_energies.csv`
- Format: csv
- Contract: Columns: ethylene_id (string, identifier of the ethylene system, e.g., '1','2',...,'8','tetrakis'), Ea_kcal_mol (float). Units: kcal/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.csv
- path: `/app/outputs/activation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The checker reads this file, extracts the ethylene_id and Ea_kcal_mol values, compares the absolute activation energies to the paper‑reported values with a hidden tolerance, and verifies the relative ordering (e.g., Ea(1) < Ea(2) < ... and specific isomer relations). The scoring combines both absolute closeness and ordering correctness.
- schema:
  - `type`: table
  - `required_columns`: `ethylene_id`, `Ea_kcal_mol`
  - `units`:
    - `Ea_kcal_mol`: kcal/mol
  - `description`: Each row corresponds to one ethylene system. ethylene_id is a string label; Ea_kcal_mol is the computed activation energy.

Notes: The activation energies are defined as E(TS) – E(complex) without ZPVE. The hidden reference consists of the paper's Table 1 values and the expected ordering constraints. The solver must not include zero‑point energy corrections.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ethylene_id",
          "Ea_kcal_mol"
        ],
        "units": {
          "Ea_kcal_mol": "kcal/mol"
        },
        "description": "Each row corresponds to one ethylene system. ethylene_id is a string label; Ea_kcal_mol is the computed activation energy."
      },
      "description": "The checker reads this file, extracts the ethylene_id and Ea_kcal_mol values, compares the absolute activation energies to the paper‑reported values with a hidden tolerance, and verifies the relative ordering (e.g., Ea(1) < Ea(2) < ... and specific isomer relations). The scoring combines both absolute closeness and ordering correctness."
    }
  ],
  "notes": "The activation energies are defined as E(TS) – E(complex) without ZPVE. The hidden reference consists of the paper's Table 1 values and the expected ordering constraints. The solver must not include zero‑point energy corrections."
}
```

## How you are scored
A hidden verifier examines your submitted artifacts, computes a score for each scored workflow stage, and combines them (with hidden weights) into a final reward. For the activation energy CSV, it will compare your computed energies to a hidden gold reference, verify relative ordering constraints among the ethylene systems, and assign credit based on both absolute accuracy and ordering correctness. The verifier also checks that every artifact exists and conforms to the required format. Reporting the paper’s numbers verbatim is not sufficient; your reward depends on genuine DFT computation.
