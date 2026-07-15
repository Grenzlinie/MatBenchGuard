# PM3 analysis of heme–amino acid–ligand complexes

## Problem background
The proximal ligand in the fifth coordination position of the heme iron plays a critical role in modulating the binding and activation of small molecules such as O2 and NO. Mutations of this residue (e.g., His to Cys or Gly) significantly affect the properties of hemoproteins. To design proteins with desired ligand-binding characteristics, it is essential to quantitatively understand how the identity of the proximal residue influences the geometry, the binding strength, and the electronic charge distribution of the heme–ligand complex. This task addresses this by computing these properties for model heme complexes with His, Cys, and Gly as proximal residues and O2 and NO as ligands.

## Approach
The computational approach uses the PM3 semiempirical quantum-chemical method, which provides a good balance between accuracy and computational cost for heme systems. Starting from a heme-containing structure retrieved from the Protein Data Bank, we build simplified models comprising the heme, a single amino acid residue (His, Cys, or Gly) coordinated to iron in the fifth position, and a diatomic ligand (O2 or NO) in the sixth position. Additionally, we prepare isolated fragments (heme+amino acid and free ligand) for subsequent binding energy calculations. All structures are then optimized with PM3 using a conjugate-gradient algorithm. From the optimized wavefunctions, Mulliken charges are extracted. The optimized coordinates yield internuclear distances. Binding energies for O2 are obtained from the energy difference between the ternary complex and its separated components. The results are compiled into a single results.json file.

## Reproduction target
Compute and output a results.json file containing three sections: (1) internuclear distances (Å) for all six ternary complexes, including Fe–O1, Fe–O2, O1–O2, and the Fe–donor atom distance for the proximal residue (Fe–N for His/Gly, Fe–S for Cys), as well as the distance from Fe to the center of the O–O bond for the Cys and Gly O₂ complexes; (2) O₂ binding energies (kcal/mol) for the three O₂ complexes (His, Cys, Gly), computed as E(heme–amino acid–O₂) – E(heme–amino acid) – E(free O₂); and (3) Mulliken atomic charges (e) for the iron atom, the two ligand atoms (O1, O2 for O₂; N, O for NO), and the donor atom of the proximal residue (N for His/Gly, S for Cys) in each complex.

## Assets

- Protein Data Bank: https://www.rcsb.org
- MOPAC (or equivalent PM3 semiempirical quantum chemistry package): http://openmopac.net/

## Workflow steps

### Step 1: Model construction from PDB
- Role: process
- Action: Retrieve a heme-containing protein structure from the Protein Data Bank, extract the heme with the proximal amino acid residue (His, Cys, or Gly), and construct simplified complexes (all six ternary complexes plus isolated fragments needed for binding energy calculation) using standard bond lengths for O2 and NO. Generate PM3 input files for geometry optimization.
- Evidence: none

### Step 2: PM3 geometry optimization and energy calculation
- Role: process
- Action: For each system (ternary complexes and fragments), perform a PM3 semiempirical geometry optimization using a conjugate gradient optimizer to high precision. Save the optimized Cartesian coordinates, total electronic energies, and output logs containing the Mulliken population analysis.
- Evidence: none

### Step 3: Extract quantities and compile results.json
- Role: scored (load-bearing)
- Action: From the PM3 optimization outputs, extract internuclear distances (Fe–O, O–O, Fe–N,S, and Fe–O2_center for certain complexes), O2 binding energies by computing E(ternary) – E(heme+amino acid) – E(free O2) for each O2 complex, and Mulliken atomic charges for Fe, ligand atoms, and proximal residue atom. Organize all values into a single JSON file results.json according to the specified schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with three top-level keys: 'distances' (object whose keys are complex names and values are sub-objects containing distances as floats in Angstroms), 'bond_energies' (object whose keys are O2 complex names and values are floats in kcal/mol), and 'charges' (object whose keys are complex names and values are sub-objects with Mulliken charges as floats in elementary charge units).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing all reproduced quantities: internuclear distances, O2 binding energies, and Mulliken atomic charges, as computed from PM3 calculations.
- schema:
  - `type`: object
  - `required`: `distances`, `bond_energies`, `charges`
  - `properties`:
    - `distances`:
      - `type`: object
      - `description`: Each complex name (e.g., 'Heme+His+O2') maps to an object of interatomic distances (Fe-O1, Fe-O2, O1-O2, Fe-N(S)aa, Fe-O2_center where applicable, etc.) in Angstroms.
    - `bond_energies`:
      - `type`: object
      - `description`: Keys are O2 complex names; values are the computed binding energy in kcal/mol.
    - `charges`:
      - `type`: object
      - `description`: Each complex name maps to an object of Mulliken atomic charges (Fe, O1, O2, N(S)aa for O2 complexes; Fe, N, O, N(S)aa for NO complexes) in elementary charge units.

Notes: Distances are in Angstroms, bond energies in kcal/mol, charges in elementary charge units. For Heme+Cys+O2 and Heme+Gly+O2, include the actual distance from Fe to the center of the O-O bond as 'Fe-O2_center'. The complex naming follows the paper's convention.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "distances",
          "bond_energies",
          "charges"
        ],
        "properties": {
          "distances": {
            "type": "object",
            "description": "Each complex name (e.g., 'Heme+His+O2') maps to an object of interatomic distances (Fe-O1, Fe-O2, O1-O2, Fe-N(S)aa, Fe-O2_center where applicable, etc.) in Angstroms."
          },
          "bond_energies": {
            "type": "object",
            "description": "Keys are O2 complex names; values are the computed binding energy in kcal/mol."
          },
          "charges": {
            "type": "object",
            "description": "Each complex name maps to an object of Mulliken atomic charges (Fe, O1, O2, N(S)aa for O2 complexes; Fe, N, O, N(S)aa for NO complexes) in elementary charge units."
          }
        }
      },
      "description": "Scored artifact containing all reproduced quantities: internuclear distances, O2 binding energies, and Mulliken atomic charges, as computed from PM3 calculations."
    }
  ],
  "notes": "Distances are in Angstroms, bond energies in kcal/mol, charges in elementary charge units. For Heme+Cys+O2 and Heme+Gly+O2, include the actual distance from Fe to the center of the O-O bond as 'Fe-O2_center'. The complex naming follows the paper's convention."
}
```

## How you are scored
Your results.json will be evaluated by a hidden verifier. It will compare your reported distances, bond energies, and charges to reference values derived from rigorous calculations, using tolerance margins that reflect the expected variability of the PM3 method. In addition, the verifier will check that structural trends are consistent with the underlying physics: for example, the O–O bond length should follow a specific ordering across the three amino acids, and the Fe charge should display a specific relative shift upon ligand binding. The total score is a weighted combination of the agreement of each quantity and trend. Simply printing a particular number is insufficient; you must run the full PM3 workflow to produce the published quantities. No part of the answer will be given in the instructions.
