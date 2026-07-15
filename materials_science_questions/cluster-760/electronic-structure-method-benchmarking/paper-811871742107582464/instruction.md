# Fe + CCl4 Reaction Intermediate Energies (B3LYP/Ahlrichs TZV+P)

## Problem background
Iron atoms can react with carbon tetrachloride (CCl₄) to produce a variety of products including FeCl₂, FeCl₃, and C₂ chlorocarbons, but the underlying mechanisms and intermediates are not fully known. Theoretical calculations can map the reaction pathways and identify stable Fe-C-Cl intermediates, helping to explain the experimental product distributions and informing remediation strategies.

## Approach
Use density functional theory (DFT) with the B3LYP functional and the Ahlrichs TZV+P basis set to perform gas-phase geometry optimizations and harmonic vibrational frequency calculations for a set of Fe-C-Cl species representing intermediates in the Fe + CCl₄ reaction. From these calculations, obtain zero-point-energy (ZPE) corrected electronic energies and compute the relative stability of each species with respect to the separated Fe atom and CCl₄ molecule. This provides a quantitative energy landscape for the (1:1) stoichiometry and the most stable (2:1) dimer species.

## Reproduction target
For the nine key species – Fe, CCl₄, Fe···CCl₄ complex (Fe_CCl4_complex), [FeCl·CCl₃] (FeCl_CCl3_complex), ClFeCCl₃, Cl₂FeCCl₂, Cl₃FeCCl, the separated pair FeCl₂ + :CCl₂ (FeCl2_plus_CCl2), and Cl₂FeCFeCl₂ – in their specified spin multiplicities, compute the ZPE-corrected electronic energy (Hartree). Then compute the relative energy (kcal/mol) of each species as (E_species – E_Fe – E_CCl₄) × 627.509. Report the results in a CSV file (/app/outputs/geometries_and_energies.csv) with columns: species (string), multiplicity (int), ZPE_corrected_energy_Hartree (float), relative_energy_kcal_mol (float). The species column must use exactly the names listed above. Fe and CCl₄ should have relative_energy_kcal_mol = 0.

## Assets

- Quantum chemistry package (NWChem or ORCA): https://github.com/nwchemgit/nwchem (NWChem) or https://www.orcasoftware.de/ (ORCA)

## Workflow steps

### Step 1: DFT Geometry Optimization and Vibrational Analysis
- Role: process
- Action: For each of the nine required species (Fe, CCl4, Fe···CCl4 complex, [FeCl·CCl3], ClFeCCl3, Cl2FeCCl2, Cl3FeCCl, FeCl2 + :CCl2 separated pair, Cl2FeCFeCl2) in their specified spin multiplicities, perform gas-phase geometry optimization and harmonic vibrational frequency calculation using the B3LYP functional and the Ahlrichs TZV+P basis set to obtain ZPE-corrected electronic energies. Use an appropriate quantum chemistry package (e.g., NWChem or ORCA).
- Evidence: `/app/outputs/dft_calculation_logs.tar.gz`

### Step 2: Relative Energy Extraction and Reporting
- Role: scored (load-bearing)
- Action: For each species, extract the ZPE-corrected electronic energy (Hartree) from the output logs. Compute the relative energy (kcal/mol) with respect to the sum of Fe and CCl4 energies (i.e., (E_species - E_Fe - E_CCl4) * 627.509). Write the results, including all nine required species, to geometries_and_energies.csv.
- Output file: `/app/outputs/geometries_and_energies.csv`
- Format: csv
- Contract: CSV with columns: species (string), multiplicity (int), ZPE_corrected_energy_Hartree (float), relative_energy_kcal_mol (float). The species column must use the exact names: Fe, CCl4, Fe_CCl4_complex, FeCl_CCl3_complex, ClFeCCl3, FeCl2_plus_CCl2, Cl2FeCCl2, Cl3FeCCl, Cl2FeCFeCl2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometries_and_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometries_and_energies.csv
- path: `/app/outputs/geometries_and_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of ZPE-corrected electronic energies and relative energies (vs Fe + CCl4) for all nine required species. The relative energies are recomputed by the checker and compared to hidden reference values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `species`, `multiplicity`, `ZPE_corrected_energy_Hartree`, `relative_energy_kcal_mol`
  - `units`:
    - `ZPE_corrected_energy_Hartree`: Hartree
    - `relative_energy_kcal_mol`: kcal/mol

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometries_and_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "multiplicity",
          "ZPE_corrected_energy_Hartree",
          "relative_energy_kcal_mol"
        ],
        "units": {
          "ZPE_corrected_energy_Hartree": "Hartree",
          "relative_energy_kcal_mol": "kcal/mol"
        }
      },
      "description": "Table of ZPE-corrected electronic energies and relative energies (vs Fe + CCl4) for all nine required species. The relative energies are recomputed by the checker and compared to hidden reference values from the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier checks your CSV for completeness and correctness. It verifies that all nine required species are present, that the relative energy for each species is correctly derived from the ZPE-corrected energies, and that the energies are physically plausible. It then compares each relative energy to hidden reference values (gold values from the paper) within an allowed tolerance. Additionally, it checks that the relative stabilities of the intermediates satisfy the correct energetic ordering between species (as determined by the original study). Missing species or energies outside tolerance reduce the score proportionally. The final reward is a number from 0 to 1 based on how many checks pass.
