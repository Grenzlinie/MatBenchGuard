# DFT Analysis of Molecular Orbital Compositions in a High-Spin Manganese Porphyrin Complex

## Problem background
High-spin manganese(III) porphyrin complexes such as [MnIII(TPP)Cl] exhibit unusual electronic spectra resulting from strong mixing of metal d, porphyrin π, and halide p orbitals. Understanding the ground-state molecular orbital (MO) mixing is essential for interpreting their complex optical properties. This task quantifies the MO compositions and energies in the ground state of [MnIII(TPP)Cl] by performing density functional theory (DFT) calculations.

## Approach
The electronic structure is investigated with spin-unrestricted Kohn–Sham DFT using the B3LYP exchange–correlation functional and the LanL2DZ* basis set (double-zeta valence plus polarization on heavy atoms, effective core potentials on Mn and Cl). Starting from the known crystal structure, a full geometry optimization of the high-spin (S=2) complex is performed. A subsequent single-point calculation provides alpha-spin molecular orbitals, which are decomposed via Mulliken population analysis into atomic contributions from Mn d orbitals, Cl p orbitals, and the porphyrin fragment. The goal is to extract the percent contributions and orbital energies for six key frontier MOs that determine the low-energy electronic excitations.

## Reproduction target
Produce a JSON file (/app/outputs/mo_compositions.json) containing an array of six objects, each with the following keys: mo_label (one of 'alpha LUMO', 'alpha HOMO', 'alpha HOMO-1', 'alpha HOMO-2', 'alpha HOMO-3', 'alpha HOMO-4'), energy_Hartree (the orbital energy in Hartree), percent_Mn_d, percent_Cl_p, percent_porphyrin (floats between 0 and 100 representing the percentage contributions from Mn d, Cl p, and porphyrin fragments, respectively). Additionally, write the optimized geometry as an XYZ file (/app/outputs/optimized_geometry.xyz) with first line number of atoms, second line comment, then element symbol and x, y, z coordinates in Angstrom.

## Assets

- Crystal structure of [MnIII(TPP)Cl] (CCDC 603510): https://www.ccdc.cam.ac.uk/structures/search?ccdc=603510
- PySCF (Python-based quantum chemistry package): https://pypi.tuna.tsinghua.edu.cn/simple/pyscf

## Workflow steps

### Step 1: Obtain crystal structure of [MnIII(TPP)Cl]
- Role: process
- Action: Retrieve the crystal structure of [MnIII(TPP)Cl] (CCDC 603510) and convert it to XYZ format as the starting geometry.
- Evidence: `/app/outputs/crystal_structure.xyz`

### Step 2: Geometry optimization of [MnIII(TPP)Cl]
- Role: scored
- Action: Perform a full geometry optimization of high-spin [MnIII(TPP)Cl] (spin multiplicity S=2) using unrestricted Kohn-Sham DFT with the B3LYP functional and the LanL2DZ* basis set (double-zeta valence plus polarization on heavy atoms, effective core potentials on Mn and Cl). Use the crystal structure from step_01 as starting geometry. Output the converged, optimized geometry in XYZ format.
- Output file: `/app/outputs/optimized_geometry.xyz`
- Format: txt
- Contract: XYZ format: first line integer N atoms, second line comment, then N lines element symbol and x,y,z coordinates in Angstrom.
- Scoring: scored by hidden verifier

### Step 3: Molecular orbital population analysis
- Role: scored (load-bearing)
- Action: Using the optimized geometry from step_02, perform a single-point unrestricted DFT calculation with B3LYP/LanL2DZ* to obtain alpha-spin molecular orbitals. Carry out a population analysis (e.g., Mulliken) to decompose each MO into atomic contributions. Identify the following six key MOs by their energy ordering and orbital character: alpha LUMO (unoccupied, d_x2-y2_B1g), alpha HOMO (A2u with Cl(pz)_dz2 mixing), alpha HOMO-1 (A1u), alpha HOMO-2 (Cl(pz)_dz2 + A2u), alpha HOMO-3 (Cl(px)_dxz), alpha HOMO-4 (Cl(py)_dyz). Extract their orbital energies (in Hartree) and percent contributions from Mn d, Cl p, and porphyrin fragments. Write results to /app/outputs/mo_compositions.json.
- Output file: `/app/outputs/mo_compositions.json`
- Format: json
- Contract: Array of 6 objects, each with keys: mo_label (string), energy_Hartree (float), percent_Mn_d (float 0-100), percent_Cl_p (float 0-100), percent_porphyrin (float 0-100).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_geometry.xyz`
- `/app/outputs/mo_compositions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_geometry.xyz
- path: `/app/outputs/optimized_geometry.xyz`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimized geometry of [MnIII(TPP)Cl], used to check Mn-Cl and average Mn-N bond lengths against known reference values with tolerance.
- schema:
  - `type`: text
  - `description`: XYZ format: first line integer N atoms, second line comment, then N lines element symbol and x y z coordinates in Angstrom.

### mo_compositions.json
- path: `/app/outputs/mo_compositions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: MO compositions and energies for six alpha-spin orbitals, checked against reference values with tolerances appropriate for DFT method.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `mo_label`, `energy_Hartree`, `percent_Mn_d`, `percent_Cl_p`, `percent_porphyrin`
    - `properties`:
      - `mo_label`: string
      - `energy_Hartree`: float
      - `percent_Mn_d`: float
      - `percent_Cl_p`: float
      - `percent_porphyrin`: float

Notes: Geometry and MO results are compared to known reference data with appropriate tolerances that account for method dependence of DFT calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_geometry.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "XYZ format: first line integer N atoms, second line comment, then N lines element symbol and x y z coordinates in Angstrom."
      },
      "description": "Optimized geometry of [MnIII(TPP)Cl], used to check Mn-Cl and average Mn-N bond lengths against known reference values with tolerance."
    },
    {
      "file": "mo_compositions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "mo_label",
            "energy_Hartree",
            "percent_Mn_d",
            "percent_Cl_p",
            "percent_porphyrin"
          ],
          "properties": {
            "mo_label": "string",
            "energy_Hartree": "float",
            "percent_Mn_d": "float",
            "percent_Cl_p": "float",
            "percent_porphyrin": "float"
          }
        }
      },
      "description": "MO compositions and energies for six alpha-spin orbitals, checked against reference values with tolerances appropriate for DFT method."
    }
  ],
  "notes": "Geometry and MO results are compared to known reference data with appropriate tolerances that account for method dependence of DFT calculations."
}
```

## How you are scored
A hidden verifier independently inspects your submitted mo_compositions.json and optimized_geometry.xyz. For mo_compositions.json, it compares the orbital energies and percent fragment contributions against reference values obtained from a consistent computational protocol. For optimized_geometry.xyz, it checks that the Mn–Cl and average Mn–N bond lengths are physically reasonable relative to known experimental ranges. Each scored output contributes a weight to the final reward; the MO compositions carry the primary weight, while the geometry check is a secondary consistency constraint. Do not attempt to match any specific paper-reported numbers; instead, perform the DFT workflow correctly and the resulting values will fall within acceptable tolerances.
