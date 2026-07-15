# Magnetic Anisotropy Barrier and Bonding Energies of Mn12 Molecules on Graphene

## Problem background
Magnetic single-molecule magnets (SMMs) such as Mn12 cluster molecules are candidates for molecular spintronics, especially when combined with two-dimensional materials like graphene. The interaction between the molecule and substrate, and consequently the magnetic properties, can be tuned by changing the terminating ligands bonded to the Mn12 core. In this work we study how four different ligands (-H, -CH3, -C6H5, -CHCl2) affect the adsorption of Mn12 on graphene and whether the magnetic anisotropy barrier (MAB) changes upon adsorption.

## Approach
We use spin-polarized density functional theory (DFT) with the PBE exchange-correlation functional and a van der Waals correction (e.g., optB86b) to model isolated Mn12 molecules and Mn12 adsorbed on a graphene supercell. The initial molecular geometry is obtained from the crystal structure of Mn12-acetate (CCDC entry). Ligand variants are built by substituting the R groups. For each ligand a supercell with a vacuum layer is constructed; several lateral positions are scanned with single-point calculations to find the lowest-energy adsorption configuration. All structures are then relaxed until forces are below 0.05 eV/Å. After relaxation, non-self-consistent spin-orbit coupling calculations are performed with the spin quantization axis along the easy axis (normal to graphene) and in the hard plane; the MAB is the energy difference E(hard plane) − E(easy axis). Bonding energies are computed from the energies of the deformed molecule and graphene separately and of the combined system using the same relaxed geometries.

## Reproduction target
Produce two CSV tables: 1) mab_values.csv containing MAB values (in K) for each ligand under two conditions (isolated molecule and graphene-supported molecule), and 2) bonding_energies.csv containing the bonding energy (in eV) between the molecule and graphene for each ligand. The verifier will check that the reduction in MAB upon adsorption is significantly larger for one ligand than for the others, and that the bonding energies are consistent with the expected adsorption character (physical vs ionic). Absolute values may vary depending on computational details; only the qualitative trends are scored.

## Assets

- Mn12 acetate crystal structure (CCDC entry): https://www.ccdc.cam.ac.uk/
- Quantum ESPRESSO or equivalent open-source DFT code: https://www.quantum-espresso.org/
- PBE PAW pseudopotentials (SSSP or pslibrary): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Preliminary adsorption site scan
- Role: process
- Action: Build several initial configurations of each Mn12 ligand on a graphene supercell by shifting/rotating the molecule laterally; run single-point DFT energy evaluations to identify the lowest-energy configuration for subsequent relaxation.
- Evidence: `/app/outputs/site_scan_energies.csv`

### Step 2: Geometry optimization of all systems
- Role: process
- Action: Fully relax the atomic positions of: the combined Mn12/graphene system (each ligand, starting from best scan configuration), the isolated Mn12 molecule (each ligand), and the isolated graphene supercell. Use DFT-PBE+optB86b (or a comparable vdW-inclusive functional) with a 500 eV cutoff and force convergence <0.05 eV/Å.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Magnetic anisotropy barrier calculation
- Role: scored (load-bearing)
- Action: For each ligand, using the relaxed geometries, perform non-self-consistent spin-orbit coupling (SOC) calculations on the isolated and graphene-supported molecules with spin quantisation axis along the easy axis (normal to graphene) and in the horizontal plane. Compute MAB = E_hard_plane − E_easy_axis and convert to kelvin. Generate the output file.
- Output file: `/app/outputs/mab_values.csv`
- Format: csv
- Contract: csv with columns: ligand (string), condition (string), MAB_K (float)
- Scoring: scored by hidden verifier

### Step 4: Bonding energy calculation
- Role: scored
- Action: For each ligand, extract the deformed molecule and graphene coordinates from the relaxed combined supercell; run single-point DFT energy calculations on these deformed components (molecule alone, graphene alone) and on the combined system. Compute bonding energy E_b = E_graphene + E_molecule − E_combined. Output the result.
- Output file: `/app/outputs/bonding_energies.csv`
- Format: csv
- Contract: csv with columns: ligand (string), bonding_energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mab_values.csv`
- `/app/outputs/bonding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mab_values.csv
- path: `/app/outputs/mab_values.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetic anisotropy barrier values for each ligand and condition (isolated vs supported)
- schema:
  - `type`: table
  - `required_columns`: `ligand`, `condition`, `MAB_K`
  - `units`:
    - `MAB_K`: K

### bonding_energies.csv
- path: `/app/outputs/bonding_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Bonding energy between molecule and graphene for each ligand
- schema:
  - `type`: table
  - `required_columns`: `ligand`, `bonding_energy_eV`
  - `units`:
    - `bonding_energy_eV`: eV

Notes: Zero-strain case only. Scoring checks structural trends: The MAB reduction for one ligand is significantly larger than for the other three, and bonding energies reflect the expected strong interaction for that ligand. No absolute values are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mab_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ligand",
          "condition",
          "MAB_K"
        ],
        "units": {
          "MAB_K": "K"
        }
      },
      "description": "Magnetic anisotropy barrier values for each ligand and condition (isolated vs supported)"
    },
    {
      "file": "bonding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ligand",
          "bonding_energy_eV"
        ],
        "units": {
          "bonding_energy_eV": "eV"
        }
      },
      "description": "Bonding energy between molecule and graphene for each ligand"
    }
  ],
  "notes": "Zero-strain case only. Scoring checks structural trends: The MAB reduction for one ligand is significantly larger than for the other three, and bonding energies reflect the expected strong interaction for that ligand. No absolute values are required."
}
```

## How you are scored
A hidden verifier inspects your output files. It checks that the required columns are present and populated, and then verifies that the MAB reduction pattern across ligands and the bonding energy pattern follow the expected physical trends (e.g., one ligand showing a much larger reduction and stronger bonding). Each check contributes to a final score between 0 and 1. Reporting the correct qualitative trends is sufficient to obtain full credit; exactly matching any absolute reference values is not required.
