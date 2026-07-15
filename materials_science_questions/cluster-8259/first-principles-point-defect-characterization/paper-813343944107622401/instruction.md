# SCC-DFTB QM/MM annealing of SiC quantum dots in quartz and coordination defect analysis

## Problem background
3C-SiC quantum dots (QDs) embedded in SiO2 are attractive for Si-based optoelectronics because of their favorable band offsets, yet the measured luminescence is quenched—most likely by defects at the SiC/SiO2 interface. This study uses self-consistent charge density functional tight-binding (SCC-DFTB) simulated annealing to generate atomistic models of SiC QDs in a quartz matrix and to systematically characterize the recurring point defects that form at the interface. The present task concentrates on quantifying coordination defects for two models: an embedded cluster model (66-sph-1) and a periodic supercell model (66-sup). The aim is to compute how the number of undercoordinated and overcoordinated atoms evolves during annealing, and to compare the residual defect population between the two modeling approaches.

## Approach
The atomic models are built from an α-quartz unit cell that is first relaxed with DFTB+. A 66-atom spherical 3C‑SiC nanocrystal is placed inside a cavity carved in the quartz, giving two representations: (i) an embedded‑cluster model (66‑sph‑1) in which the outer SiO2 shells are kept fixed and link atoms handle boundary conditions, and (ii) a fully periodic supercell model (66‑sup) without atom constraints. Both models are annealed via Born–Oppenheimer molecular dynamics using SCC-DFTB with the pbc‑1‑0 parameter set. The thermal protocol starts at 300 K, ramps up to 1500 K, equilibrates there, then rapidly quenches to 0 K, followed by a conjugate‑gradient geometry optimization until forces fall below 10−4 H/Bohr. After obtaining the final relaxed geometries, a bond‑detection scheme (distance ≤ 1.2 × sum of covalent radii from Pyykkö & Atsumi) is applied to identify the coordination state of every O, C, and Si atom. For each element, the number of atoms with each coordination deviation (−2, −1, 0, +1, +2) is tallied in both the initial (unrelaxed) structures and the final (relaxed) structures. These counts capture the extent and healing of under‑ and over‑coordination at the SiC/SiO2 interface.

## Reproduction target
Carry out the full SCC-DFTB MD annealing and geometry relaxation workflow for the two models (66‑sph‑1 and 66‑sup). From the final relaxed geometries, compute the coordination defect counts (deviations from ideal single‑bonded coordination) for O, C, and Si, and report the same counts for the initial unrelaxed models. Use these data to verify two quantitative trends:
(1) In each model, the total number of undercoordinated atoms (atoms with a deviation of −1 or less) decreases from the initial state to the final state.
(2) The number of undercoordinated carbon atoms in the final periodic supercell model (66‑sup) is larger than that in the final embedded cluster model (66‑sph‑1).
Submit the final geometries as XYZ files and the full coordination error counts as a JSON file; the subsequent evaluation is based solely on these artifacts.

## Assets

- DFTB+: https://www.dftb-plus.info
- pbc-1-0 parameter set for Si–O–C–H: https://github.com/dftbparams
- α-quartz unit cell: COD 9005004
- 66-atom spherical 3C-SiC nanocrystal geometry
- Covalent radii (Pyykkö & Atsumi): 10.1002/chem.200800912

## Workflow steps

### Step 1: Optimize α-quartz unit cell
- Role: process
- Action: Build the α-quartz unit cell with experimental lattice vectors and relax atomic positions using DFTB+ (Γ‑point calculation) until forces are converged.
- Evidence: `/app/outputs/quartz_optimized.xyz`

### Step 2: Construct initial 66‑sph‑1 and 66‑sup models
- Role: process
- Action: From the optimized quartz cell, carve a quartz rhomboid, embed the 66‑atom spherical SiC nanocrystal, remove overlapping quartz atoms (maintaining SiO₂ stoichiometry and distance constraints), define the QM zone with link atoms and BCTC neutralization, and fix outer shells to create the 66‑sph‑1 embedded cluster model. In parallel, build a 5×5×4 periodic supercell with the same nanocrystal, without constraints. Save the initial coordinates of both models.
- Evidence: `/app/outputs/initial_66sph1.xyz and initial_66sup.xyz`

### Step 3: SCC‑DFTB MD annealing and geometry optimization
- Role: process
- Action: For each model (66‑sph‑1 and 66‑sup), run Born–Oppenheimer molecular dynamics with DFTB+ and pbc‑1‑0 parameters. Use a 1 fs time step, an Andersen thermostat (heat from 300 K to 1500 K at 1.5 K/fs, equilibrate at 1500 K for 3–5 ps, exponentially quench to 0 K in 0.8 ps). Follow by conjugate‑gradient geometry optimization until the maximum atomic force falls below 10⁻⁴ H/Bohr. For the embedded model, keep the outer SiO₂ shells fixed; for the periodic model, fix the supercell vectors.
- Evidence: `/app/outputs/md_output.log`

### Step 4: Write 66‑sph‑1 final geometry
- Role: scored
- Action: Write the final relaxed atomic coordinates of the 66‑sph‑1 model to an XYZ file.
- Output file: `/app/outputs/66-sph-1_final.xyz`
- Format: txt
- Contract: Standard XYZ format: integer atom count, comment string (must contain '66-sph-1'), per-atom lines 'element x y z' with Cartesian coordinates in Å.
- Scoring: scored by hidden verifier

### Step 5: Write 66‑sup final geometry
- Role: scored
- Action: Write the final relaxed atomic coordinates of the 66‑sup model to an XYZ file.
- Output file: `/app/outputs/66-sup_final.xyz`
- Format: txt
- Contract: Standard XYZ format: integer atom count, comment string (must contain '66-sup'), per-atom lines 'element x y z' with Cartesian coordinates in Å.
- Scoring: scored by hidden verifier

### Step 6: Compute coordination defect counts
- Role: scored (load-bearing)
- Action: Using the bond criterion (distance ≤ 1.2 × sum of covalent radii from Pyykkö & Atsumi), compute the coordination deviation for every O, C, and Si atom in the initial (unrelaxed) and final (relaxed) structures of both models. Aggregate counts per element and per deviation value (−2, −1, 0, +1, +2). Write a JSON file with keys '66-sph-1' and '66-sup', each containing 'initial' and 'final' dictionaries.
- Output file: `/app/outputs/coordination_errors.json`
- Format: json
- Contract: JSON object with keys '66-sph-1' and '66-sup'. Each value is an object with keys 'initial' and 'final'. Each 'initial'/'final' is an object mapping element ('O','C','Si') to an object mapping integer deviation (−2,−1,0,1,2) to an integer count.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/66-sph-1_final.xyz`
- `/app/outputs/66-sup_final.xyz`
- `/app/outputs/coordination_errors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### 66-sph-1_final.xyz
- path: `/app/outputs/66-sph-1_final.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed geometry of the embedded cluster model. The checker recomputes coordination defect counts from this file.
- schema:
  - `type`: text
  - `description`: Standard XYZ file: first line atom count, second line comment (including '66-sph-1'), then lines with element symbol and Cartesian coordinates in Å.

### 66-sup_final.xyz
- path: `/app/outputs/66-sup_final.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed geometry of the periodic supercell model. The checker recomputes coordination defect counts from this file.
- schema:
  - `type`: text
  - `description`: Standard XYZ file: first line atom count, second line comment (including '66-sup'), then lines with element symbol and Cartesian coordinates in Å.

### coordination_errors.json
- path: `/app/outputs/coordination_errors.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Coordination deviation counts per element and per model for initial and final structures. The checker will recompute the final counts from the XYZ geometries, compare them with tolerance, and verify that total undercoordination decreases and that the periodic model retains more carbon undercoordination.
- schema:
  - `type`: object
  - `required`:
    - `66-sph-1`:
      - `type`: object
      - `required`: `initial`, `final`
      - `properties`:
        - `initial`:
          - `type`: object
          - `description`: mapping element ('O','C','Si') to deviation counts
        - `final`:
          - `type`: object
          - `description`: mapping element ('O','C','Si') to deviation counts
    - `66-sup`:
      - `type`: object
      - `required`: `initial`, `final`
      - `properties`:
        - `initial`: object
        - `final`: object

Notes: The scored output contract covers the two final geometries and the coordination error report. The checker recomputes the coordination from the geometries and validates the paper's trends; absolute counts are compared with a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "66-sph-1_final.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Standard XYZ file: first line atom count, second line comment (including '66-sph-1'), then lines with element symbol and Cartesian coordinates in Å."
      },
      "description": "Relaxed geometry of the embedded cluster model. The checker recomputes coordination defect counts from this file."
    },
    {
      "file": "66-sup_final.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Standard XYZ file: first line atom count, second line comment (including '66-sup'), then lines with element symbol and Cartesian coordinates in Å."
      },
      "description": "Relaxed geometry of the periodic supercell model. The checker recomputes coordination defect counts from this file."
    },
    {
      "file": "coordination_errors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "66-sph-1": {
            "type": "object",
            "required": [
              "initial",
              "final"
            ],
            "properties": {
              "initial": {
                "type": "object",
                "description": "mapping element ('O','C','Si') to deviation counts"
              },
              "final": {
                "type": "object",
                "description": "mapping element ('O','C','Si') to deviation counts"
              }
            }
          },
          "66-sup": {
            "type": "object",
            "required": [
              "initial",
              "final"
            ],
            "properties": {
              "initial": "object",
              "final": "object"
            }
          }
        }
      },
      "description": "Coordination deviation counts per element and per model for initial and final structures. The checker will recompute the final counts from the XYZ geometries, compare them with tolerance, and verify that total undercoordination decreases and that the periodic model retains more carbon undercoordination."
    }
  ],
  "notes": "The scored output contract covers the two final geometries and the coordination error report. The checker recomputes the coordination from the geometries and validates the paper's trends; absolute counts are compared with a tolerance."
}
```

## How you are scored
A hidden verifier reads your submitted XYZ files and coordination report. It independently recomputes the final coordination defect counts from the XYZ geometries using the same bond‑detection criterion and compares them to your reported counts (a small tolerance absorbs minor numerical differences). It uses the initial coordination counts you reported to check two trends: (1) the total undercoordination must be lower in the final state for both models, and (2) the final carbon undercoordination in the periodic model must exceed that in the embedded model. Fulfillment of each trend earns full weight; otherwise partial credit may be awarded based on how close the computed quantities are to the expected values. The overall score is a weighted combination of the agreement of the coordination counts and the satisfaction of the required trends.
