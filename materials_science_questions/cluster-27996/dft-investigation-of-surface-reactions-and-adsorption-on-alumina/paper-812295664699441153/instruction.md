# Ab Initio Investigation of Al+ Ion-Molecule Complexation Structures and Energies

## Problem background
Al+ ion-molecule interactions are fundamental in gas-phase ion chemistry, but absolute binding energies and the detailed bonding character (charge transfer versus ion‑dipole contributions) have not been fully characterized. This work uses ab initio molecular orbital theory to investigate the structures and binding energies (Al+ affinities) of Al+ with 12 saturated and unsaturated O, N, and F bases. The computed complexation energies and population analysis results will help establish an absolute energy scale for Al+ binding and reveal the relative importance of σ donation, π donation, and ion‑dipolar forces in these complexes.

## Approach
The investigation follows a multi‑step computational protocol using open‑source quantum chemistry software (e.g., Psi4) and standard Gaussian basis sets (3‑21G and 6‑31G*). First, the geometries of all 12 free bases and their corresponding Al+-base complexes are optimized at the 3‑21G level. Harmonic vibrational frequencies are then computed at the same level to obtain zero‑point energy corrections and to confirm that all structures are true minima. Using these optimized geometries, single‑point energy calculations are performed with the larger 6‑31G* basis set. From the total energies and zero‑point corrections, the Al+ complexation energies (with and without zero‑point energy) are derived for each base. Additionally, for a subset of seven bases, Mulliken population analyses are carried out on the 3‑21G wavefunctions to quantify the σ and π electron transfer from the base to the Al+ ion. The overall protocol is designed to reproduce the electronic structure results reported in the literature without requiring access to the original proprietary software.

## Reproduction target
Produce three output files under `/app/outputs`:
1. `energies.csv` – a table of Al+ complexation energies (with and without zero‑point correction) for all 12 bases: NH3, CH3NH2, H2O, CH3OH, CH3CH2OH, (CH3)2O, HF, CH3F, H2CO, CH3CHO, HCN, CH3CN. The columns must include the 3‑21G total energy, the 6‑31G* total energy, the zero‑point energy, and the complexation energies with and without ZPE.
2. `populations.csv` – a table of Mulliken population analysis results (σ electron transfer and π electron transfer) for the 7‑base subset: NH3, H2O, HF, CH3F, H2CO, HCN, CH3CN. For H2O and H2CO, also report the in‑plane π' electron transfer.
3. `geometries.xyz` – a concatenated XYZ file containing the 3‑21G optimized geometries of all 12 Al+-base complexes.
The values in these files must be obtained by faithfully executing the computational steps described below; they will be compared to independently established reference data.

## Assets

- Psi4 quantum chemistry package: https://psicode.org/
- 3-21G and 6-31G* basis sets

## Workflow steps

### Step 1: Geometry optimization of free bases at 3-21G
- Role: process
- Action: For each of the 12 bases (NH3, CH3NH2, H2O, CH3OH, CH3CH2OH, (CH3)2O, HF, CH3F, H2CO, CH3CHO, HCN, CH3CN), build an initial molecular structure and perform geometry optimization using the 3-21G basis set. Ensure all structures are true minima (all real frequencies).
- Evidence: `/app/outputs/free_base_opt.log`

### Step 2: Geometry optimization of Al+ complexes at 3-21G
- Role: process
- Action: For each base, construct an initial geometry for the Al+-base complex (placing Al+ along the expected lone pair/dipole axis) and perform geometry optimization using the 3-21G basis set. Verify that all optimized structures are true minima (all real frequencies).
- Evidence: `/app/outputs/complex_opt.log`

### Step 3: Vibrational frequency calculations
- Role: process
- Action: Compute harmonic vibrational frequencies at the 3-21G level for all free bases and Al+ complexes (using geometries from steps 1 and 2) to extract zero-point vibrational energies (in kcal/mol). Ensure all structures have no imaginary frequencies, confirming they are minima.
- Evidence: none

### Step 4: Single-point energy calculations at 6-31G*
- Role: process
- Action: Perform single-point energy calculations at the 6-31G* level using the optimized geometries from steps 1 and 2 for all free bases, Al+ complexes, and the isolated Al+ ion. Record the total energies in hartree.
- Evidence: none

### Step 5: Compute Al+ complexation energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in step 4 and zero-point energies from step 3, calculate the Al+ complexation energies (kcal/mol) for each of the 12 bases, both with and without zero-point energy correction. The complexation energy is the energy difference: E(complex) - E(Al+) - E(free base). Write the results to /app/outputs/energies.csv.
- Output file: `/app/outputs/energies.csv`
- Format: csv
- Contract: CSV with columns: base (str), total_energy_3-21G_hartree (float), total_energy_6-31Gstar_hartree (float), zero_point_energy_kcal_per_mol (float), complexation_energy_with_zpe_kcal_per_mol (float), complexation_energy_without_zpe_kcal_per_mol (float). 12 rows, one per base.
- Scoring: scored by hidden verifier

### Step 6: Mulliken population analysis
- Role: scored (load-bearing)
- Action: For the 7 bases NH3, H2O, HF, CH3F, H2CO, HCN, CH3CN, perform Mulliken population analysis on the 3-21G wavefunctions of the optimized Al+ complexes (from step 2) to extract the σ electron transfer to Al+ and the π electron transfer to Al+. For H2O and H2CO, also compute the in-plane π' electron transfer to the metal. Write results to /app/outputs/populations.csv.
- Output file: `/app/outputs/populations.csv`
- Format: csv
- Contract: CSV with columns: base (str), sigma_electron_transfer_to_Al (float), pi_electron_transfer_to_Al (float). For H2O and H2CO, also include in_plane_pi_electron_transfer (float). 7 rows, one per base in the subset.
- Scoring: scored by hidden verifier

### Step 7: Collect optimized complex geometries
- Role: scored
- Action: From the optimized geometries of the 12 Al+ complexes (step 2), assemble a single XYZ file containing all structures. Write to /app/outputs/geometries.xyz.
- Output file: `/app/outputs/geometries.xyz`
- Format: other
- Contract: Standard XYZ format with atomic symbols and coordinates in Angstroms. 12 concatenated entries.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.csv`
- `/app/outputs/populations.csv`
- `/app/outputs/geometries.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.csv
- path: `/app/outputs/energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed Al+ complexation energies (with and without ZPE correction) for 12 saturated and unsaturated bases at the 6-31G*//3-21G level.
- schema:
  - `type`: table
  - `required_columns`: `base`, `total_energy_3-21G_hartree`, `total_energy_6-31Gstar_hartree`, `zero_point_energy_kcal_per_mol`, `complexation_energy_with_zpe_kcal_per_mol`, `complexation_energy_without_zpe_kcal_per_mol`
  - `units`:
    - `total_energy_3-21G_hartree`: hartree
    - `total_energy_6-31Gstar_hartree`: hartree
    - `zero_point_energy_kcal_per_mol`: kcal/mol
    - `complexation_energy_with_zpe_kcal_per_mol`: kcal/mol
    - `complexation_energy_without_zpe_kcal_per_mol`: kcal/mol

### populations.csv
- path: `/app/outputs/populations.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mulliken population analysis data (σ and π electron transfer) for a subset of 7 Al+ complexes.
- schema:
  - `type`: table
  - `required_columns`: `base`, `sigma_electron_transfer_to_Al`, `pi_electron_transfer_to_Al`
  - `optional_columns`: `in_plane_pi_electron_transfer`
  - `units`:
    - `sigma_electron_transfer_to_Al`: electrons
    - `pi_electron_transfer_to_Al`: electrons
    - `in_plane_pi_electron_transfer`: electrons

### geometries.xyz
- path: `/app/outputs/geometries.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Optimized 3-21G geometries of all 12 Al+-base complexes, concatenated in a single XYZ file.
- schema:
  - `type`: text
  - `description`: Standard XYZ format; 12 entries, each with atom count, comment line, and atomic coordinates.

Notes: Tolerances for exact_match on energies.csv: 0.5 kcal/mol for complexation energies, 0.001 hartree for total energies. For populations.csv: 0.01 electrons. geometries.xyz is checked for syntax and that it contains 12 entries, not for numerical values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "base",
          "total_energy_3-21G_hartree",
          "total_energy_6-31Gstar_hartree",
          "zero_point_energy_kcal_per_mol",
          "complexation_energy_with_zpe_kcal_per_mol",
          "complexation_energy_without_zpe_kcal_per_mol"
        ],
        "units": {
          "total_energy_3-21G_hartree": "hartree",
          "total_energy_6-31Gstar_hartree": "hartree",
          "zero_point_energy_kcal_per_mol": "kcal/mol",
          "complexation_energy_with_zpe_kcal_per_mol": "kcal/mol",
          "complexation_energy_without_zpe_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Computed Al+ complexation energies (with and without ZPE correction) for 12 saturated and unsaturated bases at the 6-31G*//3-21G level."
    },
    {
      "file": "populations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "base",
          "sigma_electron_transfer_to_Al",
          "pi_electron_transfer_to_Al"
        ],
        "optional_columns": [
          "in_plane_pi_electron_transfer"
        ],
        "units": {
          "sigma_electron_transfer_to_Al": "electrons",
          "pi_electron_transfer_to_Al": "electrons",
          "in_plane_pi_electron_transfer": "electrons"
        }
      },
      "description": "Mulliken population analysis data (σ and π electron transfer) for a subset of 7 Al+ complexes."
    },
    {
      "file": "geometries.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Standard XYZ format; 12 entries, each with atom count, comment line, and atomic coordinates."
      },
      "description": "Optimized 3-21G geometries of all 12 Al+-base complexes, concatenated in a single XYZ file."
    }
  ],
  "notes": "Tolerances for exact_match on energies.csv: 0.5 kcal/mol for complexation energies, 0.001 hartree for total energies. For populations.csv: 0.01 electrons. geometries.xyz is checked for syntax and that it contains 12 entries, not for numerical values."
}
```

## How you are scored
A hidden verifier reads your three output files. For `energies.csv` it compares each complexation energy and total energy to reference values with appropriate tolerances; for `populations.csv` it checks the electron transfer values against reference data; and for `geometries.xyz` it validates the XYZ syntax and that it contains 12 entries. The verifier may also assess whether certain relative trends among the bases are reproduced. Each file contributes to an overall weighted score; the exact tolerances and weights are not disclosed. To succeed, you must run the full computational workflow and ensure all outputs match the required format and physical content.
