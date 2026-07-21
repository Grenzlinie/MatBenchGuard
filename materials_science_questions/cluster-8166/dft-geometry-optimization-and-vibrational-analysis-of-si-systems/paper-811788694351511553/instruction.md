# DFT Optimization and Properties of Passivated Si60 Fullerene Cages

## Problem background
Silicon fullerene-like cages (Si60) are of interest as novel materials, but bare Si60 is geometrically unstable and does not retain the icosahedral (I_h) symmetry of carbon fullerenes. A promising strategy is exohedral passivation: attaching electronegative atoms to each Si site to satisfy the dangling bonds and stabilise an sp³-like local environment. This task investigates whether passivating Si60 with fluorine (F) or chlorine (Cl) can yield stable, perfect I_h fullerene cages, and what the resulting structural, electronic, and energetic properties would be. The goal is to compute and compare these properties for Si60F60 and Si60Cl60 clusters using first-principles density functional theory.

## Approach
The study employs density functional theory (DFT) within the generalized gradient approximation using the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and a double-zeta quality basis set. All calculations are spin-restricted. The workflow begins by constructing an initial I_h Si60 cage from the known C60 fullerene topology, scaled to an appropriate Si–Si bond distance. For each passivation case, the corresponding halogen atoms (F or Cl) are attached to every Si site at a typical bond length to form the starting geometries of Si60F60 and Si60Cl60. Full geometry optimizations are then performed without any symmetry constraints, allowing all atomic positions to relax until forces and total energy are converged. From the relaxed structures, the symmetry is verified, and the following properties are extracted: the range of Si–Si bond lengths, the Si–X (X = F, Cl) bond length, the HOMO–LUMO gap, the Mulliken charge transferred from each Si to the halogen, and the total energy of the cluster. Isolated-atom reference energies for Si, F, and Cl are computed at the same level of theory. The binding energy per atom is then calculated using these atomic references. The results for the two cages are compared to assess the effect of the passivating element on stability, geometry, and electronic structure.

## Reproduction target
For both Si60F60 and Si60Cl60, produce the following: (1) the fully relaxed geometry saved as an XYZ file with 120 atoms. (2) A JSON file (results.json) containing the point-group symmetry, the minimum and maximum Si–Si bond length, the Si–X bond length, the HOMO–LUMO gap, the average Mulliken charge transferred from each Si atom to the halogen, the total energy of the cluster, and the binding energy per atom. Also include in the JSON the isolated-atom energies used to compute the binding energies. All bond lengths are in angstroms, gaps in electron‑volts, charge in elementary charge, total energies in hartree, and binding energies in eV/atom.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- PBE pseudopotentials for Si, F, Cl: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build initial structural models
- Role: process
- Action: Construct the initial I_h-symmetric Si60 fullerene cage by adopting the icosahedral topology of C60 scaled to an appropriate Si-Si distance. For each of the two passivated clusters (Si60F60 and Si60Cl60), attach the corresponding halogen atom (F or Cl) to each Si site at a typical bond length, and generate input files suitable for DFT geometry optimization.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform separate full geometry optimizations for Si60F60 and Si60Cl60 using the chosen DFT code with PBE functional, a double-zeta basis set, and spin-restricted calculation. Relax all atomic positions without symmetry constraints until forces converge below an appropriate threshold and total energy convergence is reached. Save the final relaxed atomic coordinates and total energies for each cluster.
- Evidence: `/app/outputs/optimization.log`

### Step 3: Compute properties and write results.json
- Role: scored (load-bearing)
- Action: From the optimized geometries, determine the point group symmetry (must be I_h) and extract the minimum and maximum Si-Si bond lengths and the Si-X bond length. Compute the HOMO-LUMO gap. Perform Mulliken population analysis to obtain the charge transferred from each Si to the halogen. Calculate binding energy per atom using isolated-atom reference energies computed at the same level of theory. Write all these computed quantities for both Si60F60 and Si60Cl60, together with the atomic reference energies, into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with top-level keys "Si60F60", "Si60Cl60", and "atomic_energies". Each cluster key contains: "symmetry" (string), "Si_Si_bond_length_min_Ang" (float), "Si_Si_bond_length_max_Ang" (float), "Si_X_bond_length_Ang" (float), "HOMO_LUMO_gap_eV" (float), "Mulliken_charge_transfer_e" (float), "total_energy_Ha" (float), "binding_energy_eV_per_atom" (float). The "atomic_energies" key contains: "Si_Ha", "F_Ha", "Cl_Ha" (all floats).
- Scoring: scored by hidden verifier

### Step 4: Save optimized Si60F60 coordinates
- Role: scored
- Action: Extract the final relaxed atomic positions of Si60F60 and write them in XYZ format to si60f60_relaxed.xyz.
- Output file: `/app/outputs/si60f60_relaxed.xyz`
- Format: txt
- Contract: Standard XYZ format: first line is the number of atoms (120), second line is a comment line, followed by 120 lines, each line containing the element symbol (Si or F) and three Cartesian coordinates (in Angstrom) separated by whitespace.
- Scoring: scored by hidden verifier

### Step 5: Save optimized Si60Cl60 coordinates
- Role: scored
- Action: Extract the final relaxed atomic positions of Si60Cl60 and write them in XYZ format to si60cl60_relaxed.xyz.
- Output file: `/app/outputs/si60cl60_relaxed.xyz`
- Format: txt
- Contract: Standard XYZ format: first line is the number of atoms (120), second line is a comment line, followed by 120 lines, each line containing the element symbol (Si or Cl) and three Cartesian coordinates (in Angstrom) separated by whitespace.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/si60f60_relaxed.xyz`
- `/app/outputs/si60cl60_relaxed.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All computed structural, electronic, and energetic quantities for Si60F60 and Si60Cl60, along with the isolated-atom reference energies used to compute binding energies.
- schema:
  - `type`: object
  - `required`:
    - `Si60F60`: object
    - `Si60Cl60`: object
    - `atomic_energies`: object
  - `Si60F60`:
    - `symmetry`: string
    - `Si_Si_bond_length_min_Ang`: float
    - `Si_Si_bond_length_max_Ang`: float
    - `Si_X_bond_length_Ang`: float
    - `HOMO_LUMO_gap_eV`: float
    - `Mulliken_charge_transfer_e`: float
    - `total_energy_Ha`: float
    - `binding_energy_eV_per_atom`: float
  - `Si60Cl60`:
    - `symmetry`: string
    - `Si_Si_bond_length_min_Ang`: float
    - `Si_Si_bond_length_max_Ang`: float
    - `Si_X_bond_length_Ang`: float
    - `HOMO_LUMO_gap_eV`: float
    - `Mulliken_charge_transfer_e`: float
    - `total_energy_Ha`: float
    - `binding_energy_eV_per_atom`: float
  - `atomic_energies`:
    - `Si_Ha`: float
    - `F_Ha`: float
    - `Cl_Ha`: float

### si60f60_relaxed.xyz
- path: `/app/outputs/si60f60_relaxed.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Final relaxed geometry of the Si60F60 cluster.
- schema:
  - `type`: text
  - `description`: XYZ file with 120 atoms (60 Si, 60 F). First line: integer (120); second line: comment; 120 coordinate lines, each with element symbol and x, y, z in Angstrom.

### si60cl60_relaxed.xyz
- path: `/app/outputs/si60cl60_relaxed.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Final relaxed geometry of the Si60Cl60 cluster.
- schema:
  - `type`: text
  - `description`: XYZ file with 120 atoms (60 Si, 60 Cl). First line: integer (120); second line: comment; 120 coordinate lines, each with element symbol and x, y, z in Angstrom.

Notes: The symmetry field must be the string 'I_h'. All bond lengths, gaps, charges, and energies are compared to hidden reference values within tolerances appropriate for DFT reproduction. Structural consistency (bond lengths within tolerance, correct atom count) is also enforced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Si60F60": "object",
          "Si60Cl60": "object",
          "atomic_energies": "object"
        },
        "Si60F60": {
          "symmetry": "string",
          "Si_Si_bond_length_min_Ang": "float",
          "Si_Si_bond_length_max_Ang": "float",
          "Si_X_bond_length_Ang": "float",
          "HOMO_LUMO_gap_eV": "float",
          "Mulliken_charge_transfer_e": "float",
          "total_energy_Ha": "float",
          "binding_energy_eV_per_atom": "float"
        },
        "Si60Cl60": {
          "symmetry": "string",
          "Si_Si_bond_length_min_Ang": "float",
          "Si_Si_bond_length_max_Ang": "float",
          "Si_X_bond_length_Ang": "float",
          "HOMO_LUMO_gap_eV": "float",
          "Mulliken_charge_transfer_e": "float",
          "total_energy_Ha": "float",
          "binding_energy_eV_per_atom": "float"
        },
        "atomic_energies": {
          "Si_Ha": "float",
          "F_Ha": "float",
          "Cl_Ha": "float"
        }
      },
      "description": "All computed structural, electronic, and energetic quantities for Si60F60 and Si60Cl60, along with the isolated-atom reference energies used to compute binding energies."
    },
    {
      "file": "si60f60_relaxed.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ file with 120 atoms (60 Si, 60 F). First line: integer (120); second line: comment; 120 coordinate lines, each with element symbol and x, y, z in Angstrom."
      },
      "description": "Final relaxed geometry of the Si60F60 cluster."
    },
    {
      "file": "si60cl60_relaxed.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ file with 120 atoms (60 Si, 60 Cl). First line: integer (120); second line: comment; 120 coordinate lines, each with element symbol and x, y, z in Angstrom."
      },
      "description": "Final relaxed geometry of the Si60Cl60 cluster."
    }
  ],
  "notes": "The symmetry field must be the string 'I_h'. All bond lengths, gaps, charges, and energies are compared to hidden reference values within tolerances appropriate for DFT reproduction. Structural consistency (bond lengths within tolerance, correct atom count) is also enforced."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each of the required output artifacts. The verifier reads the XYZ files to confirm the correct number of atoms and Ih symmetry (verified by bond-length uniformity). It then reads results.json and compares the reported structural, electronic, and energetic quantities against hidden reference values obtained from the original study, using tolerances appropriate for independent DFT reproductions. The verifier also checks that the internal consistency among reported quantities is physically sound. The total reward is a weighted combination of the scores for the individual artifacts; producing the correct numbers through an honest re-run of the computational workflow is the expected way to receive full credit.
