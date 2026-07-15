# Reproducing Dissociation Energies and Hydrogen-Bond Critical Point Densities of BASE-HF Complexes

## Problem background
The theory of atoms in molecules provides a unified explanation of hydrogen bonding through charge-density topology and the atomic virial theorem. This task computes dissociation energies and the charge density at the hydrogen bond critical point for a series of BASE-HF complexes (where BASE = OC, SC, N₂, HCN, H₃N, O₃, SCO, CO₂, N₂O, SO₂, H₂CO, H₂O, HF, H₃P, H₂S, HCl). The target quantities quantify the strength and electronic structure of hydrogen bonds, and this exercise evaluates whether the ab initio results can be reproduced using open-source computational tools.

## Approach
The method implements restricted Hartree-Fock (RHF) energy calculations followed by atoms-in-molecules topological analysis. First, the geometries of isolated monomers (HF and each base) and each BASE–HF complex are optimized at the RHF/6-31G** level. Using those optimized structures, single-point RHF/6-311++G** calculations provide total SCF energies and wavefunctions. The wavefunctions are then analyzed with an atoms-in-molecules tool to locate the bond critical point of the hydrogen bond (B–H) and extract the charge density ρ at that point. Finally, the dissociation energy Dₑ for each complex is computed as the difference between the complex’s total energy and the sum of the isolated base and HF energies. The entire procedure is carried out with open-source quantum chemistry and wavefunction analysis software.

## Reproduction target
For every BASE–HF complex in the set (OC–HF, SC–HF, NN–HF, HCN–HF, H₃N–HF, OOO–HF, SCO–HF, OCO–HF, NNO–HF, OSO–HF, H₂CO–HF, H₂O–HF, HF–HF, H₃P–HF, H₂S–HF, HCl–HF, HF–HCl), compute the dissociation energy Dₑ (in kJ/mol) and the charge density ρ at the hydrogen-bond critical point (in atomic units). Report both values for all complexes in a CSV file with columns: complex, D_e_kJmol, rho_bcp_au. The computations must follow the RHF/6-311++G**//6-31G** protocol using the optimized geometries. No external datasets are required; the structures and basis sets are publicly available.

## Assets

- Psi4: https://psicode.org/
- Multiwfn: http://sobereva.com/multiwfn/

## Workflow steps

### Step 1: Geometry optimization of monomers and complexes
- Role: process
- Action: Perform geometry optimization of all isolated monomers (HF and each base: OC, SC, N2, HCN, H3N, O3, SCO, CO2, N2O, SO2, H2CO, H2O, H3P, H2S, HCl) and all BASE-HF complexes at the RHF/6-31G** level using an open-source quantum chemistry package. The optimized structures are needed for subsequent single-point calculations.
- Evidence: `/app/outputs/optimized_geometries.log`

### Step 2: Single-point energy calculation
- Role: process
- Action: For each species (monomers and complexes) using the optimized geometries, run single-point RHF/6-311++G** calculations to obtain total SCF energies. Save the wavefunction files for subsequent AIM analysis.
- Evidence: `/app/outputs/scf_energies.log`

### Step 3: Atoms-in-molecules analysis
- Role: process
- Action: Using the wavefunction files from the single-point calculations, perform topological analysis to locate the bond critical point of the hydrogen bond (B–H) for each complex and extract the charge density ρ (a.u.) at that point.
- Evidence: `/app/outputs/aim_output.txt`

### Step 4: Assemble results and compute D_e
- Role: scored (load-bearing)
- Action: Compute the dissociation energy D_e (kJ/mol) for each complex as the difference between the total energy of the complex and the sum of the energies of the isolated base and HF. Combine with the extracted ρ values. Write a CSV file with columns: complex, D_e_kJmol, rho_bcp_au.
- Output file: `/app/outputs/reproduced_results.csv`
- Format: csv
- Contract: complex (string), D_e_kJmol (float), rho_bcp_au (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.csv
- path: `/app/outputs/reproduced_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with one row per BASE-HF complex, containing the computed dissociation energy and the charge density at the hydrogen-bond critical point. The checker compares these values to hidden reference values from the paper within prescribed tolerances.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `D_e_kJmol`, `rho_bcp_au`
  - `units`:
    - `D_e_kJmol`: kJ/mol
    - `rho_bcp_au`: a.u.

Notes: The CSV must include all 17 complexes: OC–HF, SC–HF, NN–HF, HCN–HF, H3N–HF, OOO–HF, SCO–HF, OCO–HF, NNO–HF, OSO–HF, H2CO–HF, H2O–HF, HF–HF, H3P–HF, H2S–HF, HCl–HF, HF–HCl. The complex column should use the same naming convention as shown here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "D_e_kJmol",
          "rho_bcp_au"
        ],
        "units": {
          "D_e_kJmol": "kJ/mol",
          "rho_bcp_au": "a.u."
        }
      },
      "description": "CSV file with one row per BASE-HF complex, containing the computed dissociation energy and the charge density at the hydrogen-bond critical point. The checker compares these values to hidden reference values from the paper within prescribed tolerances."
    }
  ],
  "notes": "The CSV must include all 17 complexes: OC–HF, SC–HF, NN–HF, HCN–HF, H3N–HF, OOO–HF, SCO–HF, OCO–HF, NNO–HF, OSO–HF, H2CO–HF, H2O–HF, HF–HF, H3P–HF, H2S–HF, HCl–HF, HF–HCl. The complex column should use the same naming convention as shown here."
}
```

## How you are scored
Each stage of the workflow produces output files. A hidden verifier will independently read your submitted artifacts, re-derive or compare the relevant scored quantities for each scored stage, and assign a stage score according to the output contract. The final reward is a weighted combination of the stage scores. Reporting a set of numbers is not sufficient; the verifier will verify that the intermediate computation steps (geometry optimizations, energy calculations, topological analysis) have been genuinely executed and that the final dissociation energies and critical-point densities are correctly derived from your own work. All precision requirements and comparison rules are encoded in the hidden verifier and are not disclosed here.
