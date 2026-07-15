# Lattice Energy Calculation for Crystal Stability

## Problem background
Isotactic cis-1,4-poly(1,3-pentadiene) (icPP) is a stereoregular polymer whose crystal structure was first predicted by molecular mechanics and later confirmed by X-ray diffraction. The prediction used a classical force field and packing energy minimizations in an orthorhombic space group. This task reproduces the computational part of that study: you will compute the predicted unit cell parameters, the chain conformation, and the lattice energies of three packing models (including two competing packing modes) to validate the predictive power of the method.

## Approach
The calculations rely on molecular mechanics using the MM2_85 force field and periodic boundary conditions in the P2(1)2(1)2(1) space group. First, build the icPP polymer chain with two-fold helical symmetry and prepare initial crystal packing models (model A, model B, and the experimental structure) from the fractional coordinates and unit cell parameters given in the literature. Then, perform packing energy minimizations by scanning the a and b unit cell axes and the chain translation (z) and rotation (ω) to locate the two local minima. For the global minimum, extract the optimal cell axes and the full set of backbone bond angles and dihedral angles. Next, for each of the three models, compute the initial lattice energy and the energy after relaxation of atomic coordinates under fixed unit cell axes, all expressed per monomeric unit. The workflow is implemented with an open-source molecular mechanics package that supports MM2 and periodic calculations.

## Reproduction target
Your work must produce two scored artifacts:

1. A CSV file with the predicted crystal structure's unit cell parameters a, b, c (in Å) and the following backbone conformational parameters (in degrees): bond angles C(1)-C(2)-C(3), C(2)-C(3)-C(4), C(3)-C(4)-C(1'), C(4)-C(1')-C(2'), C(3)-C(4)-C(5); dihedral angles C(1)-C(2)-C(3)-C(4), C(2)-C(3)-C(4)-C(1'), C(3)-C(4)-C(1')-C(2'), C(4)-C(1')-C(2')-C(3'), C(2)-C(3)-C(4)-C(5).

2. A JSON file with six lattice energy values (kJ per mol of monomeric unit): initial and optimized energies for the experimental crystal structure, for model A, and for model B.

These quantities correspond to those reported in the original computational study. You must build the structures, execute the packing minimizations, and collect the results according to the workflow steps below.

## Assets

- MM2_85 force field parameters: 10.1021/ja00463a001
- Open-source molecular mechanics software supporting MM2 and periodic boundary conditions: lammps

## Workflow steps

### Step 1: Build molecular structures
- Role: process
- Action: Build the isotactic cis-1,4-poly(1,3-pentadiene) polymer chain with two-fold helical symmetry (s(2/1) line repetition group) and construct the initial crystal packing models for the experimental structure and model B using the fractional coordinates and unit cell parameters below; model A will be obtained from the packing energy scan in Step 2.
  Fractional coordinates (asymmetric unit) for model B:
  C(1)  x=0.2220  y=-0.0986  z=-0.1941
  C(2)  x=0.1044  y=-0.0324  z=-0.3131
  C(3)  x=0.1083  y=-0.0330  z=-0.4771
  C(4)  x=0.2310  y=-0.1004  z=-0.5891
  C(5)  x=0.1810  y=-0.2978  z=-0.6951
  Fractional coordinates (asymmetric unit) for the experimental crystal structure:
  C(1)  x=0.2173  y=-0.0991  z=-0.1919
  C(2)  x=0.1061  y=-0.0092  z=-0.3063
  C(3)  x=0.1112  y=-0.0018  z=-0.4706
  C(4)  x=0.2293  y=-0.0850  z=-0.5784
  C(5)  x=0.1761  y=-0.2837  z=-0.6776
  Unit cell parameters for model B: a=9.47 Å, b=5.97 Å, c=8.15 Å.
  Unit cell parameters for the experimental structure: a=9.49 Å, b=6.07 Å, c=8.17 Å.
- Evidence: `/app/outputs/initial_structures.pdb`

### Step 2: Packing energy minimization to determine predicted structure
- Role: process
- Action: Using the MM2_85 force field and periodic boundary conditions in the P2(1)2(1)2(1) space group, perform packing energy minimization to scan the a and b unit cell axes and the chain translation z and rotation ω. Identify the two local minima corresponding to model A and model B. For the global minimum, extract the optimal unit cell parameters a, b, c (c held near 8.15 Å) and the full set of backbone bond angles and dihedral angles.
- Evidence: `/app/outputs/packing_minima.json`

### Step 3: Compute lattice energies for fixed packing models
- Role: process
- Action: For each of the three packing models, compute the initial lattice energy (E_in) and the optimized energy (E_opt) after relaxation of atomic coordinates under fixed unit cell axes, all in kJ per mole of monomeric unit.
  - Experimental structure: use the fractional coordinates given above and fixed cell axes a=9.49 Å, b=6.07 Å, c=8.17 Å.
  - Model A: use the fractional coordinates obtained from the packing scan in Step 2 and fixed cell axes a=9.47 Å, b=5.97 Å, c=8.15 Å.
  - Model B: use the fractional coordinates given above and fixed cell axes a=9.47 Å, b=5.97 Å, c=8.15 Å.
- Evidence: `/app/outputs/energy_calculations.json`

### Step 4: Extract predicted structural parameters
- Role: scored (load-bearing)
- Action: From the global minimum structure (lowest energy) obtained in Step 2, extract the unit cell parameters a, b, c (in Å) and the backbone bond angles and dihedral angles as enumerated below. Write these to /app/outputs/calculated_structure_properties.csv.
- Output file: `/app/outputs/calculated_structure_properties.csv`
- Format: csv
- Contract: CSV with three columns: parameter (string), value (number), unit (string, e.g. 'Å' or 'degrees'). Required rows as listed in description.
- Scoring: scored by hidden verifier

### Step 5: Collect lattice energies
- Role: scored (load-bearing)
- Action: Extract the initial and optimized lattice energies per monomeric unit (in kJ/mol) for the experimental crystal structure, model A, and model B from the energy calculations performed in step_03. Write these to /app/outputs/lattice_energies.json.
- Output file: `/app/outputs/lattice_energies.json`
- Format: json
- Contract: JSON object with six numeric keys: experimental_Ein, experimental_Eopt, model_A_Ein, model_A_Eopt, model_B_Ein, model_B_Eopt. All values in kJ per mole of monomeric unit.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_structure_properties.csv`
- `/app/outputs/lattice_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_structure_properties.csv
- path: `/app/outputs/calculated_structure_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted crystal structure unit cell parameters and chain conformational parameters (bond angles and dihedral angles) extracted from the packing energy minimization. Checked against paper-reported values with absolute tolerances.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`, `unit`
  - `items`: object
  - `units`: object

### lattice_energies.json
- path: `/app/outputs/lattice_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice energies per monomeric unit for experimental, model A and model B structures before and after coordinate relaxation, computed with the MM2_85 force field. Checked against paper-reported values within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `experimental_Ein`: number
    - `experimental_Eopt`: number
    - `model_A_Ein`: number
    - `model_A_Eopt`: number
    - `model_B_Ein`: number
    - `model_B_Eopt`: number
  - `items`: object
  - `units`:
    - `all`: kJ/mol

Notes: The X-ray diffraction and fiber spectrum simulations are omitted as they do not produce a numerically checkable metric and would require proprietary Cerius2 modules. The core validation rests on the structural parameters and lattice energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_structure_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value",
          "unit"
        ],
        "items": {},
        "units": {}
      },
      "description": "Predicted crystal structure unit cell parameters and chain conformational parameters (bond angles and dihedral angles) extracted from the packing energy minimization. Checked against paper-reported values with absolute tolerances."
    },
    {
      "file": "lattice_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "experimental_Ein": "number",
          "experimental_Eopt": "number",
          "model_A_Ein": "number",
          "model_A_Eopt": "number",
          "model_B_Ein": "number",
          "model_B_Eopt": "number"
        },
        "items": {},
        "units": {
          "all": "kJ/mol"
        }
      },
      "description": "Lattice energies per monomeric unit for experimental, model A and model B structures before and after coordinate relaxation, computed with the MM2_85 force field. Checked against paper-reported values within tolerance."
    }
  ],
  "notes": "The X-ray diffraction and fiber spectrum simulations are omitted as they do not produce a numerically checkable metric and would require proprietary Cerius2 modules. The core validation rests on the structural parameters and lattice energies."
}
```

## How you are scored
Your outputs are scored by a hidden verifier that compares them to the reference values from the original study. Each artifact is checked independently:
- For the CSV, the unit cell parameters and conformational angles are compared with absolute tolerances that account for acceptable differences between force field implementations and minimizer settings.
- For the JSON, the energy values and the relative ordering of the models' energies (which model is most stable) are verified against the expected pattern.
Meeting the required accuracy on all parameters and energy values earns full reward; partial matches contribute proportionally. Reporting the paper's numbers without performing the actual computations will not satisfy the tolerance checks.
