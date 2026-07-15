# DFT structural and stability analysis of Fe(II)-triazole oligomers

## Problem background
Fe(II)‑1,2,4‑H‑triazole polymeric complexes are spin‑crossover materials whose structure and stoichiometry have not been fully determined by single‑crystal X‑ray diffraction. Two candidate linear‑chain formulas are considered: a fully protonated form, ([Fe(Htrz)₃]²⁺)ₙ, and a partially deprotonated form, ([Fe(Htrz)₂(trz)]⁺)ₙ, where one triazole per Fe is deprotonated. The relative stability of these two forms and their structural differences (Fe–Fe separations, Fe–N bond lengths) are debated, and unambiguous experimental resolution is lacking. This task uses density functional theory (DFT) to predict the geometry and formation energetics of oligomeric fragments representing both candidates, aiming to identify which ligand arrangement is favored and to quantify how the key structural parameters differ between them.

## Approach
Linear oligomer models containing 2, 4, and 6 Fe ions (models A1, A2, A3) are built for both the fully protonated and the partially deprotonated chains. Each Fe(II) ion is octahedrally coordinated by six N atoms from three bridging triazole rings. The geometries are optimized with DFT using the B3LYP exchange‑correlation functional and the 6‑31G(d) basis set. From the optimized structures, nearest‑neighbor Fe–Fe distances and all Fe–N bond lengths are extracted. To compare stability, formation energies are computed as the oligomer total energy minus the sum of the energies of isolated Fe²⁺ ions and neutral Htrz molecules, all evaluated at the same level of theory. The entire workflow is carried out with an open‑source quantum chemistry code (ORCA or NWChem). By computing these quantities for both ligand types and all model sizes, the structural trends and energetic ordering between the two candidate formulas can be established.

## Reproduction target
For the B3LYP/6‑31G(d) method, compute (i) Fe–Fe nearest‑neighbor distances, (ii) Fe–N bond lengths, and (iii) formation energies for each oligomer model A1, A2, A3 in both the deprotonated and undeprotonated forms. Report the results in structured JSON and XYZ files. The objective is to determine, from your computed values, which class of complexes consistently yields shorter Fe–Fe distances, shorter Fe–N bonds, and lower (more stable) formation energies across the model sizes.

## Assets

- open-source DFT code (ORCA or NWChem): https://orcaforum.kofo.mpg.de/ (ORCA) or https://nwchemgit.github.io/ (NWChem)
- molecular visualization (Avogadro, Jmol, etc.): https://avogadro.cc/ or https://jmol.org/

## Workflow steps

### Step 1: Build molecular models and input files
- Role: process
- Action: Construct the six oligomer models: deprotonated ([Fe2(Htrz)4(trz)2]2+, [Fe4(Htrz)8(trz)4]4+, [Fe6(Htrz)12(trz)6]6+) and undeprotonated ([Fe2(Htrz)6]4+, [Fe4(Htrz)12]8+, [Fe6(Htrz)18]12+) linear chains with triazole bridges. Prepare input files for geometry optimization using B3LYP/6-31G(d) with an open-source DFT code.
- Evidence: none

### Step 2: Run geometry optimizations
- Role: process
- Action: Execute geometry optimizations for all six complexes at the B3LYP/6-31G(d) level using the chosen DFT code. Retain the final optimized coordinates and total electronic energies for each complex.
- Evidence: `/app/outputs/optimization.log`

### Step 3: Collect optimized structures into a single XYZ file
- Role: scored (load-bearing)
- Action: Concatenate the final optimized coordinates of all six complexes into one XYZ file, with a comment line naming each complex (e.g., 'deprotonated A1').
- Output file: `/app/outputs/step_01_optimized_structures.xyz`
- Format: txt
- Contract: Concatenated XYZ text file containing coordinates for all six complexes. Each structure begins with the number of atoms on one line, a comment line identifying the complex, and then atom lines (element symbol and xyz coordinates).
- Scoring: scored by hidden verifier

### Step 4: Compute Fe-Fe distances
- Role: scored (load-bearing)
- Action: From the optimized structures, calculate center-to-center Fe-Fe distances for all adjacent Fe pairs in each complex. Output the distances in angstroms as a JSON file.
- Output file: `/app/outputs/step_02_Fe_Fe_distances.json`
- Format: json
- Contract: {"method": "B3LYP/6-31G(d)", "deprotonated": {"A1": [dist], "A2": [dist,dist,...], "A3": [dist,...]}, "undeprotonated": {"A1": [dist], "A2": [...], "A3": [...]}}
- Scoring: scored by hidden verifier

### Step 5: Compute Fe-N bond lengths
- Role: scored (load-bearing)
- Action: Extract all Fe-N bond lengths from the optimized structures, separating deprotonated and undeprotonated triazole rings where applicable. Output as JSON.
- Output file: `/app/outputs/step_03_Fe_N_bond_lengths.json`
- Format: json
- Contract: {"method": "B3LYP/6-31G(d)", "deprotonated": {"A2": {"deprot_ring": [l1,...], "undeprot_ring": [l1,...]}, "A3": {...}}, "undeprotonated": {"A2": [l1,...], "A3": [l1,...]}}
- Scoring: scored by hidden verifier

### Step 6: Calculate isolated fragment energies
- Role: process
- Action: Perform energy calculations for an isolated Fe(II) ion and an isolated 1,2,4-H-triazole molecule at the same B3LYP/6-31G(d) level to serve as reference energies for formation energy analysis.
- Evidence: `/app/outputs/isolated_energies.json`

### Step 7: Compute formation energies
- Role: scored (load-bearing)
- Action: Using the total energies of the optimized oligomers and the isolated fragments, compute the formation energy for each complex: E_stability = E_oligomer - (n*E_Fe + m*E_Htrz). Report values in kJ/mol in a JSON file.
- Output file: `/app/outputs/step_04_formation_energies.json`
- Format: json
- Contract: {"method": "B3LYP/6-31G(d)", "deprotonated": {"A1": E, "A2": E, "A3": E}, "undeprotonated": {"A1": E, "A2": E, "A3": E}, "units": "kJ/mol"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_optimized_structures.xyz`
- `/app/outputs/step_02_Fe_Fe_distances.json`
- `/app/outputs/step_03_Fe_N_bond_lengths.json`
- `/app/outputs/step_04_formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_optimized_structures.xyz
- path: `/app/outputs/step_01_optimized_structures.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized geometries of all six complexes for structural verification and cross-check of atom counts.
- schema:
  - `type`: text
  - `required`: Concatenated XYZ with a comment line per complex identifying deprotonated/undeprotonated and model (A1/A2/A3).
  - `description`: Expected atom counts must match the molecular formulas of the six complexes.

### step_02_Fe_Fe_distances.json
- path: `/app/outputs/step_02_Fe_Fe_distances.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fe-Fe distances per model and ligand type; used to check that deprotonated complexes exhibit systematically smaller distances.
- schema:
  - `type`: object
  - `required`: `method`, `deprotonated`, `undeprotonated`
  - `deprotonated`:
    - `type`: object
    - `keys`: `A1`, `A2`, `A3`
    - `values`: array of numbers (Å)
  - `undeprotonated`:
    - `type`: object
    - `keys`: `A1`, `A2`, `A3`
    - `values`: array of numbers (Å)
  - `method`:
    - `type`: string

### step_03_Fe_N_bond_lengths.json
- path: `/app/outputs/step_03_Fe_N_bond_lengths.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fe-N bond lengths organized by complex and ring type; used to verify that deprotonated bonds are shorter.
- schema:
  - `type`: object
  - `required`: `method`, `deprotonated`, `undeprotonated`
  - `deprotonated`:
    - `type`: object
    - `keys`: `A2`, `A3`
    - `values`:
      - `type`: object
      - `keys`: `deprot_ring`, `undeprot_ring`
      - `values`: array of numbers (Å)
  - `undeprotonated`:
    - `type`: object
    - `keys`: `A2`, `A3`
    - `values`: array of numbers (Å)
  - `method`:
    - `type`: string

### step_04_formation_energies.json
- path: `/app/outputs/step_04_formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies for each complex; used to confirm that deprotonated complexes are more stable (lower energy).
- schema:
  - `type`: object
  - `required`: `method`, `deprotonated`, `undeprotonated`, `units`
  - `deprotonated`:
    - `type`: object
    - `keys`: `A1`, `A2`, `A3`
    - `values`: number (kJ/mol)
  - `undeprotonated`:
    - `type`: object
    - `keys`: `A1`, `A2`, `A3`
    - `values`: number (kJ/mol)
  - `units`:
    - `type`: string
    - `const`: kJ/mol

Notes: Only the B3LYP/6-31G(d) method is required; the agent must use an open-source DFT code. The scoring of geometric trends is based on the relative ordering of deprotonated versus undeprotonated values for each model, not on exact absolute values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_optimized_structures.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": "Concatenated XYZ with a comment line per complex identifying deprotonated/undeprotonated and model (A1/A2/A3).",
        "description": "Expected atom counts must match the molecular formulas of the six complexes."
      },
      "description": "Optimized geometries of all six complexes for structural verification and cross-check of atom counts."
    },
    {
      "file": "step_02_Fe_Fe_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "method",
          "deprotonated",
          "undeprotonated"
        ],
        "deprotonated": {
          "type": "object",
          "keys": [
            "A1",
            "A2",
            "A3"
          ],
          "values": "array of numbers (Å)"
        },
        "undeprotonated": {
          "type": "object",
          "keys": [
            "A1",
            "A2",
            "A3"
          ],
          "values": "array of numbers (Å)"
        },
        "method": {
          "type": "string"
        }
      },
      "description": "Fe-Fe distances per model and ligand type; used to check that deprotonated complexes exhibit systematically smaller distances."
    },
    {
      "file": "step_03_Fe_N_bond_lengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "method",
          "deprotonated",
          "undeprotonated"
        ],
        "deprotonated": {
          "type": "object",
          "keys": [
            "A2",
            "A3"
          ],
          "values": {
            "type": "object",
            "keys": [
              "deprot_ring",
              "undeprot_ring"
            ],
            "values": "array of numbers (Å)"
          }
        },
        "undeprotonated": {
          "type": "object",
          "keys": [
            "A2",
            "A3"
          ],
          "values": "array of numbers (Å)"
        },
        "method": {
          "type": "string"
        }
      },
      "description": "Fe-N bond lengths organized by complex and ring type; used to verify that deprotonated bonds are shorter."
    },
    {
      "file": "step_04_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "method",
          "deprotonated",
          "undeprotonated",
          "units"
        ],
        "deprotonated": {
          "type": "object",
          "keys": [
            "A1",
            "A2",
            "A3"
          ],
          "values": "number (kJ/mol)"
        },
        "undeprotonated": {
          "type": "object",
          "keys": [
            "A1",
            "A2",
            "A3"
          ],
          "values": "number (kJ/mol)"
        },
        "units": {
          "type": "string",
          "const": "kJ/mol"
        }
      },
      "description": "Formation energies for each complex; used to confirm that deprotonated complexes are more stable (lower energy)."
    }
  ],
  "notes": "Only the B3LYP/6-31G(d) method is required; the agent must use an open-source DFT code. The scoring of geometric trends is based on the relative ordering of deprotonated versus undeprotonated values for each model, not on exact absolute values."
}
```

## How you are scored
A hidden verifier inspects your output files (step_01 through step_04) and checks whether the deprotonated and undeprotonated complexes exhibit a consistent geometric and energetic ordering across all models. The specific direction of the ordering—which candidate class is shorter and more stable—is part of the target you must reproduce by accurate computation. The verifier scores the trend by comparing the deprotonated values to the undeprotonated values for each model and combining the per‑stage results into a final reward. Reporting the paper’s numbers without completing the required workflow will not earn score; the computed artifacts from your simulation run are what determine success.
