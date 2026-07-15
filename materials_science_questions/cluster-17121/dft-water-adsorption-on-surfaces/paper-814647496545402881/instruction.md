# DFT Binding Energies and Tetramer Structure for Water Chains on CaO(001)

## Problem background
Water adsorption on oxide surfaces is central to many areas of surface science, including catalysis and geochemistry. On the calcium oxide (001) surface, water molecules can arrange into one‑dimensional (1D) chain‑like assemblies along a [110] direction, even though the substrate has four‑fold rotational symmetry. Understanding what drives this 1D growth—and the role of a symmetry‑breaking water tetramer unit—requires accurate first‑principles energetics and structural determination. Density functional theory (DFT) calculations provide the binding strength of water molecules in such configurations and can reveal the special tetramer geometry that nucleates the chain.

## Approach
The calculations use periodic DFT with the screened hybrid HSE06 exchange‑correlation functional and the Tkatchenko–Scheffler many‑body van der Waals correction. A slab model of the CaO(001) surface is constructed, and water molecules are placed in a series of chain‑like arrangements containing 1 to 6 molecules (monomer through hexamer). For the pentamer, an additional configuration with a different attachment direction is prepared. All geometries are relaxed at the HSE06+vdW level, and the total energy and zero‑point energy are extracted. From these the binding energy per water molecule is obtained, and for the pentamer the energy difference between the two attachment paths is computed. Finally, the atomistic structure of the tetramer is exported for structural verification.

## Reproduction target
Compute, for a (3×4) CaO(001) supercell, the binding energy per water molecule (including zero‑point energy) for the chain‑like configurations with 1 to 6 water molecules. For the pentamer, compute the total‑energy difference between the chain‑extending configuration (molecule attached along [110]) and the configuration where the fifth molecule attaches orthogonally to the tetramer square. Provide the relaxed atomic coordinates of the tetramer (4 H₂O) together with the surface atoms. The results must be written to the files `/app/outputs/binding_energies.json` and `/app/outputs/tetramer_structure.xyz` as specified in the workflow steps and output contract.

## Assets

- FHI-aims all-electron DFT code with HSE06 and Tkatchenko-Scheffler many-body van der Waals correction: https://aimsclub.fhi-berlin.mpg.de/

## Workflow steps

### Step 1: Construct CaO(001) slab and water configurations
- Role: process
- Action: Build a CaO(001) (3×4) surface supercell slab model with appropriate vacuum using the rocksalt structure (lattice constant 4.81 Å). Place 1 to 6 water molecules in the chain-like configurations described in the paper: monomer dissociated, dimer fully dissociated along a [110] oxygen row, trimer with one intact molecule in the centre, tetramer forming a distorted square with one surface hydroxyl inside and one outside, and pentamer/hexamer extending the chain along [110] by attaching to the extra hydroxyl. Also prepare a pentamer configuration where the fifth molecule attaches orthogonally to the tetramer square.
- Evidence: none

### Step 2: DFT relaxation and binding energy calculation
- Role: scored (load-bearing)
- Action: For each water configuration (n=1..6) relax the geometry using HSE06 exchange-correlation functional with Tkatchenko-Scheffler many-body van der Waals correction as implemented in FHI-aims. Compute the total energy and the binding energy per water molecule (including zero-point energy). For n=5, also relax the configuration where the fifth molecule attaches orthogonally and compute the absolute total energy difference relative to the chain configuration.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"binding_energies": [{"n": int, "binding_energy_per_molecule": float}], "pentamer_orthogonal_energy_difference": float}
- Scoring: scored by hidden verifier

### Step 3: Extract tetramer structure
- Role: scored
- Action: From the relaxed tetramer (4 H₂O) configuration, extract the atomic coordinates of all atoms (surface Ca, surface O, water species) and save as an XYZ file with unit cell information in the comment line.
- Output file: `/app/outputs/tetramer_structure.xyz`
- Format: other
- Contract: Standard XYZ format: first line number of atoms, second line comment with lattice parameters, subsequent lines element symbol x y z.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`
- `/app/outputs/tetramer_structure.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Binding energy per water molecule (eV) for n=1 to 6 water molecules on a CaO(001) (3×4) supercell, including zero-point energy, and the energy difference (eV) between chain and orthogonal attachment for the pentamer. The values will be compared to the paper's reported results with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `binding_energies`, `pentamer_orthogonal_energy_difference`
  - `properties`:
    - `binding_energies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `n`:
            - `type`: integer
          - `binding_energy_per_molecule`:
            - `type`: number
            - `unit`: eV
    - `pentamer_orthogonal_energy_difference`:
      - `type`: number
      - `unit`: eV

### tetramer_structure.xyz
- path: `/app/outputs/tetramer_structure.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Relaxed atomic coordinates of the water tetramer and surface atoms, verifying the extra hydroxyl positions.
- schema:
  - `type`: text
  - `description`: Standard XYZ file. First line: number of atoms. Second line: comment containing the unit cell parameters (e.g., Lattice="a b c alpha beta gamma"). Subsequent lines: element symbol followed by x, y, z coordinates (Angstrom). The structure must contain exactly one oxygen atom from a water species inside the distorted square of the tetramer and one such oxygen atom outside the square on an adjacent surface site.

Notes: All output files must be written under /app/outputs. The binding energies are scored by comparing each value to the paper's reported HSE06+vdW results (reference match); the tetramer structure is checked for the correct positions of the extra hydroxyl (structural audit).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "binding_energies",
          "pentamer_orthogonal_energy_difference"
        ],
        "properties": {
          "binding_energies": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "n": {
                  "type": "integer"
                },
                "binding_energy_per_molecule": {
                  "type": "number",
                  "unit": "eV"
                }
              }
            }
          },
          "pentamer_orthogonal_energy_difference": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Binding energy per water molecule (eV) for n=1 to 6 water molecules on a CaO(001) (3×4) supercell, including zero-point energy, and the energy difference (eV) between chain and orthogonal attachment for the pentamer. The values will be compared to the paper's reported results with appropriate tolerances."
    },
    {
      "file": "tetramer_structure.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Standard XYZ file. First line: number of atoms. Second line: comment containing the unit cell parameters (e.g., Lattice=\"a b c alpha beta gamma\"). Subsequent lines: element symbol followed by x, y, z coordinates (Angstrom). The structure must contain exactly one oxygen atom from a water species inside the distorted square of the tetramer and one such oxygen atom outside the square on an adjacent surface site."
      },
      "description": "Relaxed atomic coordinates of the water tetramer and surface atoms, verifying the extra hydroxyl positions."
    }
  ],
  "notes": "All output files must be written under /app/outputs. The binding energies are scored by comparing each value to the paper's reported HSE06+vdW results (reference match); the tetramer structure is checked for the correct positions of the extra hydroxyl (structural audit)."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted artifacts. It parses `binding_energies.json` and compares each binding energy value and the pentamer energy difference against reference values (derived from the original computational study) using a tolerance that allows for legitimate spread between different DFT implementations. It also inspects `tetramer_structure.xyz` to verify the correct placement of the extra hydroxyl groups—specifically that one oxygen atom from the water species sits inside the distorted tetramer square and another sits outside on a surface site. The two scored stages are weighted and combined into a single reward between 0 and 1. Simply writing numbers that happen to match the reference is not sufficient if the structure is wrong; the verifier checks structural consistency and expects energetics that are compatible with a genuine DFT relaxation.
