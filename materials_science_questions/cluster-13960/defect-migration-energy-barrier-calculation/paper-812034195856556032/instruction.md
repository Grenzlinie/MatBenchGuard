# Reproduce Spin Localization and Ligand Binding Energies of Al13X- Clusters

## Problem background
Aluminum clusters such as Al13 are candidates for cluster-assembled nanomaterials. When functionalized with a single outer ligand X (X = H, F, Cl, Br, OH, NH2, CH3, C6H5), the radical anion Al13X- carries one unpaired electron. Key questions are where this electron localizes on the icosahedral Al13 cage and how that localization influences the energies of adding a second ligand. This computational study investigates these issues by calculating the spin density distribution and the stepwise ligand binding energies D1 and D2 for a series of Al13X- and trans-Al13X2- anions. Reproducing these quantities provides insight into the electronic structure of partially coated aluminum clusters and tests the superatom valence model for the Al13 cage.

## Approach
The investigation uses density functional theory (DFT) with the B3LYP exchange-correlation functional. Initial centered icosahedral geometries for the bare Al13- anion and all substituted species are constructed from standard icosahedron coordinates. Geometry optimizations and harmonic vibrational frequency calculations are performed at the B3LYP/6-31G* level to verify that all structures are true minima. Single-point electronic energies are then refined with the larger 6-311+G* basis set. Mulliken population analysis is applied to the relaxed radical anion wavefunctions to extract spin densities. Successive ligand addition energies D1 and D2 are derived from total electronic energies and zero-point vibrational corrections, including consistent treatment of the isolated X radicals. The overall workflow follows a sequential protocol: optimize geometries, refine energies, extract spin densities, and compute binding energies.

## Reproduction target
The task is to produce two CSV files under /app/outputs:
- spin_densities.csv: for each of the eight ligands X, report the Mulliken spin density (in electrons) on the cage atom that is opposite the Al–X bond (the Al_t* atom).
- bond_energies.csv: for each ligand X, report the first (D1) and second (D2) ligand attachment energies (in eV), including zero-point energy corrections. D1 corresponds to the reaction Al13- + X → Al13X- and D2 to trans-Al13X2- → Al13X- + X, with appropriate sign conventions and unit conversion (1 au = 27.2114 eV).
The required columns and exact formats are given in the workflow steps. The target is to compute these quantities for all eight ligands and deliver them in the specified CSV structure.

## Assets

- Quantum chemistry package supporting B3LYP functional, 6-31G* and 6-311+G* basis sets, and Mulliken population analysis (e.g., Psi4 or PySCF): psi4
- Initial centered icosahedral geometry of Al13-

## Workflow steps

### Step 1: Geometry optimization and vibrational frequency analysis of all cluster species
- Role: process
- Action: Construct initial Cartesian coordinates for the centered icosahedral Al13- cage and all required derivatives: Al13- anion, 8 Al13X- radical anions (X = H, F, Cl, Br, OH, NH2, CH3, C6H5) and 8 trans-Al13X2- diamagnetic anions. Perform B3LYP/6-31G* geometry optimization for each species, followed by harmonic vibrational frequency calculation to confirm that all structures are local minima (no imaginary frequencies). Retain optimized coordinates and zero-point vibrational energies.
- Evidence: `/app/outputs/geom_opt_log.txt`

### Step 2: Single-point energy refinement at larger basis set
- Role: process
- Action: For every optimized geometry from step-geom-opt, compute single-point electronic energy at the B3LYP/6-311+G* level. For each isolated radical X (H, F, Cl, Br, OH, NH2, CH3, C6H5), compute the total energy at the same B3LYP/6-311+G* level (including appropriate spin treatment). Record all total electronic energies and the previously obtained zero-point energies in a structured file for the next step.
- Evidence: `/app/outputs/sp_energies.txt`

### Step 3: Extract Mulliken spin densities on the opposite cage atom Al_t*
- Role: scored
- Action: Using the B3LYP/6-31G* wavefunction from each optimized Al13X- radical, perform Mulliken population analysis. Identify the cage atom opposite the Al_X-X bond (Al_t*) and extract its spin density. Write a CSV file spin_densities.csv with columns: ligand (string), rho_Al_t (float, in electrons). One row per ligand, exactly eight rows.
- Output file: `/app/outputs/spin_densities.csv`
- Format: csv
- Contract: ligand (string), rho_Al_t (float, electrons)
- Scoring: scored by hidden verifier

### Step 4: Compute successive ligand addition energies D1 and D2
- Role: scored (load-bearing)
- Action: Using total electronic energies from step-sp-energy and zero-point vibrational energies from step-geom-opt, calculate for each ligand X: D1 = E_total(Al13X-) - E_total(Al13-) - E_total(X) + ZPE_correction; D2 = E_total(Al13X2-) - E_total(Al13X-) - E_total(X) + ZPE_correction. Convert all energies to electronvolts (1 au = 27.2114 eV). Write a CSV file bond_energies.csv with columns: ligand (string), D1_eV (float), D2_eV (float). One row per ligand, exactly eight rows.
- Output file: `/app/outputs/bond_energies.csv`
- Format: csv
- Contract: ligand (string), D1_eV (float), D2_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_densities.csv`
- `/app/outputs/bond_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_densities.csv
- path: `/app/outputs/spin_densities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mulliken spin density on the Al_t* atom for each Al13X- radical anion. The checker compares the reported values to a hidden gold reference with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `ligand`, `rho_Al_t`
  - `units`:
    - `rho_Al_t`: electrons

### bond_energies.csv
- path: `/app/outputs/bond_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Successive ligand addition energies D1 and D2 for each ligand X, with ZPE corrections. The checker compares reported values to a hidden gold reference and also verifies the condition D2 > D1 for every ligand.
- schema:
  - `type`: table
  - `required_columns`: `ligand`, `D1_eV`, `D2_eV`
  - `units`:
    - `D1_eV`: eV
    - `D2_eV`: eV

Notes: All DFT calculations must be performed with an open-source quantum chemistry package supporting the B3LYP functional and the 6-31G* / 6-311+G* basis sets. The initial icosahedral geometry is constructed from standard coordinates. The load-bearing bond_energies step is unreachable without completing the process steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ligand",
          "rho_Al_t"
        ],
        "units": {
          "rho_Al_t": "electrons"
        }
      },
      "description": "Mulliken spin density on the Al_t* atom for each Al13X- radical anion. The checker compares the reported values to a hidden gold reference with an appropriate tolerance."
    },
    {
      "file": "bond_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ligand",
          "D1_eV",
          "D2_eV"
        ],
        "units": {
          "D1_eV": "eV",
          "D2_eV": "eV"
        }
      },
      "description": "Successive ligand addition energies D1 and D2 for each ligand X, with ZPE corrections. The checker compares reported values to a hidden gold reference and also verifies the condition D2 > D1 for every ligand."
    }
  ],
  "notes": "All DFT calculations must be performed with an open-source quantum chemistry package supporting the B3LYP functional and the 6-31G* / 6-311+G* basis sets. The initial icosahedral geometry is constructed from standard coordinates. The load-bearing bond_energies step is unreachable without completing the process steps."
}
```

## How you are scored
A hidden verifier scores each submitted CSV artifact independently. For spin_densities.csv, your reported spin densities are compared against reference values within a tolerance; for bond_energies.csv, your reported D1 and D2 values are similarly compared, and the verifier also checks that D2 > D1 for every ligand. The verifier does not re-run any quantum chemistry calculations; it evaluates only the files you write. Each stage carries a weight, and the final reward is the weighted sum of the per-artifact scores. To succeed, you must execute the computational protocol accurately so that your computed numbers fall within the expected range; you are not expected to match any particular number exactly.
