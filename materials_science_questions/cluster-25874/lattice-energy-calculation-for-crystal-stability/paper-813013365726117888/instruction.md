# High-Throughput Imine Cage Formation Energy Screening

## Problem background
Designing new organic cage molecules via supramolecular self-assembly is challenging because many topologies can form from the same precursors. This work explores a high-throughput computational screening approach to predict which combinations of triamines and aldehydes are likely to form clean imine cages. The central hypothesis is that computed formation energies per imine bond correlate with experimental cage-forming success, allowing computation to focus synthetic efforts. Your task is to reproduce the computational screening pipeline that evaluates all 78 triamine-aldehyde combinations.

## Approach
The workflow begins with the SMILES strings for 26 aldehydes and 3 triamines provided in `/app/assets/precursors.csv`. For each combination, the expected cage topology is determined: Tri²Di³ capsules for meta‑dialdehydes, Tri⁴Di⁶ tetrahedra for para‑dialdehydes, and Tri⁴Tri⁴ tetrapods for trialdehydes. After generating initial 3D models, a conformer search is performed using a molecular mechanics force field to locate low‑energy geometries. The lowest‑energy conformer is then optimized at the density functional theory (DFT) level PBE+D3/TZVP. The electronic energies of the isolated precursors are computed at the same level. The formation energy per imine bond is defined as ΔE = (E_cage − Σ E_precursors) / N_imine, converted to kJ mol⁻¹ per imine bond. Certain simplifications are applied: models for aldehyde 7 are omitted (nitro group poorly described by the force field), and aldehyde 10 is modeled without its external alkyl chains.

## Reproduction target
Produce a CSV file at /app/outputs/formation_energies.csv containing the computed formation energy per imine bond for each precursor combination (excluding those with aldehyde 7). The file must have exactly three columns: Triamine (string, one of 'A','B','C'), Aldehyde (integer, 1–26), and FormationEnergy_kJ_per_mol_per_imine_bond (float). The rows should cover all combinations where Aldehyde ≠ 7, resulting in 75 entries. The program that generates the CSV must implement the full pipeline of model construction, conformer search, DFT optimization, and energy evaluation, using the provided SMILES strings and open‑source tools.

## Assets

- RDKit: rdkit
- Open Force Field: openforcefield
- CP2K: https://www.cp2k.org/
- TZVP basis set: https://www.basissetexchange.org/
- Precursor SMILES table: `/app/assets/precursors.csv`

## Workflow steps

### Step 1: Build 3D models of target cages
- Role: process
- Action: For each of the 78 precursor combinations (excluding those with aldehyde 7), generate the 3D molecular structure of the targeted cage topology (Tri²Di³ for meta‑dialdehydes 1–10, Tri⁴Di⁶ for para‑dialdehydes 11–21, Tri⁴Tri⁴ for trialdehydes 22–26) using the provided SMILES strings of the precursors. For aldehyde 10, simplify the model by removing external alkyl substituents.
- Evidence: none

### Step 2: Conformer search using force field
- Role: process
- Action: For each cage model, perform a conformer search (e.g., using RDKit ETKDG or OpenMM/OpenFF with a SMIRNOFF force field) to generate low-energy conformers. Select the lowest-energy conformer as the starting point for DFT optimization.
- Evidence: none

### Step 3: DFT geometry optimization and precursor energies
- Role: process
- Action: For each cage, perform geometry optimization of the selected low‑energy conformer at the PBE+D3/TZVP level using an open‑source DFT code (e.g., CP2K or ORCA) and compute its electronic energy. Also compute the electronic energy of the isolated precursor molecules (aldehydes and triamines) at the same level of theory.
- Evidence: none

### Step 4: Calculate formation energies per imine bond
- Role: scored (load-bearing)
- Action: For each cage, compute formation energy per imine bond as ΔE = E_cage − Σ E_precursors (in kJ/mol) divided by the number of imine bonds in that cage topology. Output a CSV file with columns Triamine, Aldehyde, FormationEnergy_kJ_per_mol_per_imine_bond. Exclude combinations with aldehyde 7 (A7, B7, C7).
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: Triamine (string, 'A'/'B'/'C'), Aldehyde (int, 1–26), FormationEnergy_kJ_per_mol_per_imine_bond (float). One row per combination, excluding A7/B7/C7.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed formation energies per imine bond for each precursor combination (excluding aldehyde 7).
- schema:
  - `type`: table
  - `required_columns`: `Triamine`, `Aldehyde`, `FormationEnergy_kJ_per_mol_per_imine_bond`
  - `units`:
    - `FormationEnergy_kJ_per_mol_per_imine_bond`: kJ mol^{-1} per imine bond

Notes: The checker compares the submitted formation energies against the paper's reported range, averages per triamine, and coarse correlation with experimental outcomes (derived from a hidden mapping). Scoring tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Triamine",
          "Aldehyde",
          "FormationEnergy_kJ_per_mol_per_imine_bond"
        ],
        "units": {
          "FormationEnergy_kJ_per_mol_per_imine_bond": "kJ mol^{-1} per imine bond"
        }
      },
      "description": "Computed formation energies per imine bond for each precursor combination (excluding aldehyde 7)."
    }
  ],
  "notes": "The checker compares the submitted formation energies against the paper's reported range, averages per triamine, and coarse correlation with experimental outcomes (derived from a hidden mapping). Scoring tolerances are hidden."
}
```

## How you are scored
A hidden verifier will read your formation_energies.csv and compare it against reference computational data derived from the original study. The verifier checks: (i) whether the overall spread of formation energies is consistent with the expected range, (ii) whether the average formation energies per triamine fall within plausible bounds for a correct implementation, and (iii) whether the relative ordering of the mean formation energies for the different experimental outcome categories (clean, impure, no cage) matches the trend established in the high-throughput experiment. Scoring is based on how well your computed energies reproduce these statistical and trend‑based properties, not on exact numerical equality. The verifier does not require you to match the reference numbers pixel‑for‑pixel, but it expects that a faithful execution of the pipeline will yield energies that satisfy the above structural and trend checks.
