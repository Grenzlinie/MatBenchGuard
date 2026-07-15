# DFT Structural Analysis of Cr-Cu Substituted CeO2(111) Surface

## Problem background
The work investigates the atomic-level structure of Cr–Cu species deposited on CeO<sub>2</sub>(111) surfaces. After thermal aging, Cr–Cu/CeO<sub>2</sub> catalysts exhibit high CO oxidation activity; understanding how Cu substitutes at surface Ce sites and how the presence of Cr modifies the Cu oxidation state and local oxygen coordination is essential to explaining this activity. This task reproduces the density functional theory (DFT) calculations used to characterize the local geometry and charge state of Cu in two surface slab models: a monometallic Cu‑substituted CeO<sub>2</sub>(111) model and a bimetallic Cr‑Cu‑substituted model. By computing the relaxed structures and Bader charges, one can determine the Cu oxidation state (monovalent or divalent) and its oxygen coordination number in each environment.

## Approach
Spin‑polarised GGA+U DFT calculations are performed on periodic slab models of the CeO<sub>2</sub> (111) surface. The workflow begins by constructing and relaxing a pristine (2×2) slab with 12 atomic layers and a vacuum gap. One Ce atom on the outermost layer is substituted by Cu and an oxygen vacancy is introduced at a specific surface site to create the monometallic CuCe<sub>15</sub>O<sub>31</sub> model. For the bimetallic model, Cr is additionally substituted at a second Ce site and a second oxygen vacancy is introduced, yielding the CrCuCe<sub>14</sub>O<sub>30</sub> model (type Iα). Hubbard‑U corrections are applied to Ce f, Cu d, and Cr d states. After geometry optimisation, Bader charge analysis is performed to extract the charge on Cu and, in the bimetallic model, on Cr. Structural parameters—Cu–O distances, Cu–O–Ce distances, and Cu coordination number—are then computed from the optimised geometries. The comparison between the two models reveals how Cr influences the Cu site.

## Reproduction target
Produce the following three artefacts from first‑principles DFT:
1. The fully optimised geometry of the monometallic CuCe<sub>15</sub>O<sub>31</sub> slab (XYZ).
2. The fully optimised geometry of the bimetallic CrCuCe<sub>14</sub>O<sub>30</sub> slab (type Iα, XYZ).
3. A JSON file (`structural_parameters.json`) containing, for each model: Cu–O distances (all oxygen neighbours within 2.3 Å), Cu–O–Ce distances (Cu to Ce through bridging oxygen within 3.5 Å), Cu coordination number (count of oxygen neighbours within 2.3 Å), and Bader charges on Cu (both models) and on Cr (bimetallic model). The hidden verifier will check these quantities for consistency with the paper’s DFT results.

## Assets

- CeO2 bulk crystal structure (cubic fluorite, space group Fm-3m, lattice parameter a = 5.48 Å)
- Open-source periodic DFT code (e.g., Quantum ESPRESSO, CP2K, or equivalent) with PAW/pseudopotential and GGA+U support: https://www.quantum-espresso.org/
- PAW pseudopotential library for Ce, Cu, Cr, O (PBE exchange-correlation, with Ce 4f electrons in valence): https://www.materialscloud.org/discover/sssp/
- Bader charge analysis code (e.g., Henkelman group's Bader program): https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build and optimize CeO2 (111) surface slab model
- Role: process
- Action: Construct the bulk cubic CeO2 unit cell (lattice parameter a = 5.48 Å). Perform a DFT optimization of the bulk structure. Then create a (2×2) surface slab of the (111) facet with 12 atomic layers and a 15 Å vacuum layer. Relax the top six atomic layers while keeping the bottom six fixed.
- Evidence: `/app/outputs/slab_optimization.log`

### Step 2: DFT geometry optimization of monometallic Cu-substituted CeO2(111) model (CuCe15O31 with O1 vacancy)
- Role: process
- Action: From the relaxed (2×2) (111) slab, replace one outermost Ce atom at the site labelled Ce1 with Cu. Remove one surface oxygen atom at the site labelled O1 (creating an oxygen vacancy). Perform spin-polarised GGA+U DFT geometry optimization on this CuCe15O31 model, relaxing the top six atomic layers until forces are below 0.02 eV/Å.
- Evidence: `/app/outputs/monometallic_opt.log`

### Step 3: DFT geometry optimization of bimetallic Cr-Cu-substituted CeO2(111) model (type Iα: CrCuCe14O30 with vacancies at O1 and O3)
- Role: process
- Action: Starting from the same relaxed (2×2) (111) slab, substitute Cu at the Ce1 site and Cr at the Ce2 site. Remove oxygen atoms at both O1 and O3 sites (two oxygen vacancies). Perform the same spin-polarised GGA+U DFT optimization, with an additional Hubbard U correction for Cr d, and relax the top six layers until forces are below 0.02 eV/Å.
- Evidence: `/app/outputs/bimetallic_opt.log`

### Step 4: Compute Bader charges on the optimized models
- Role: process
- Action: Perform Bader charge analysis on the self-consistent charge densities of the optimized monometallic and bimetallic models to obtain Bader charges on Cu and, for the bimetallic model, on Cr.
- Evidence: `/app/outputs/bader_charges.out`

### Step 5: Extract optimized monometallic geometry as XYZ
- Role: scored
- Action: From the optimized monometallic CuCe15O31 model, extract the relaxed atomic coordinates and write them as an XYZ file. Include lattice vectors and all atoms in the slab.
- Output file: `/app/outputs/monometallic_optimized_geometry.xyz`
- Format: other
- Contract: Text file in XYZ format; the first line gives the number of atoms, the second line contains the lattice vectors (if applicable), followed by one line per atom with element and x,y,z coordinates in Å.
- Scoring: scored by hidden verifier

### Step 6: Extract optimized bimetallic geometry as XYZ
- Role: scored
- Action: From the optimized bimetallic CrCuCe14O30 model (type Iα), extract the relaxed atomic coordinates and write them as an XYZ file. Include lattice vectors and all atoms in the slab.
- Output file: `/app/outputs/bimetallic_optimized_geometry.xyz`
- Format: other
- Contract: Text file in XYZ format; same format as the monometallic geometry file.
- Scoring: scored by hidden verifier

### Step 7: Extract scored structural parameters and Bader charges
- Role: scored (load-bearing)
- Action: From the optimized geometries of the monometallic and bimetallic models, and from the Bader analysis, compute the Cu–O distances (all oxygen neighbours within 2.3 Å of Cu), Cu–O–Ce distances (Cu to Ce through bridging oxygen within 3.5 Å), Cu coordination number (count of oxygen atoms within 2.3 Å), and Bader charges on Cu (both models) and Cr (bimetallic model). Write these quantities as a JSON file.
- Output file: `/app/outputs/structural_parameters.json`
- Format: json
- Contract: A JSON object with keys "monometallic" and "bimetallic". Each key holds an object with: "Cu-O_distances" (array of floats, Å), "Cu-O-Ce_distances" (array of floats, Å), "Cu coordination_number" (integer), "Cu Bader_charge" (float). The "bimetallic" object additionally contains "Cr Bader_charge" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monometallic_optimized_geometry.xyz`
- `/app/outputs/bimetallic_optimized_geometry.xyz`
- `/app/outputs/structural_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monometallic_optimized_geometry.xyz
- path: `/app/outputs/monometallic_optimized_geometry.xyz`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: Optimized geometry of the monometallic CuCe15O31 slab (XYZ).
- schema:
  - `type`: other
  - `description`: XYZ file with lattice vectors and atomic coordinates. The checker recomputes Cu–O distances and coordination numbers from this file.

### bimetallic_optimized_geometry.xyz
- path: `/app/outputs/bimetallic_optimized_geometry.xyz`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: Optimized geometry of the bimetallic CrCuCe14O30 slab (type Iα) (XYZ).
- schema:
  - `type`: other
  - `description`: XYZ file with lattice vectors and atomic coordinates. The checker recomputes Cu–O distances and coordination numbers from this file.

### structural_parameters.json
- path: `/app/outputs/structural_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Self-reported structural parameters and Bader charges. Bader charges are compared directly to the paper‑reported values; distances are cross‑checked against the submitted XYZ files.
- schema:
  - `type`: object
  - `required`:
    - `monometallic`: object
    - `bimetallic`: object
  - `items`:
    - `monometallic`:
      - `Cu-O_distances`: array of floats (Å)
      - `Cu-O-Ce_distances`: array of floats (Å)
      - `Cu coordination_number`: int
      - `Cu Bader_charge`: float
    - `bimetallic`:
      - `Cu-O_distances`: array of floats (Å)
      - `Cu-O-Ce_distances`: array of floats (Å)
      - `Cu coordination_number`: int
      - `Cu Bader_charge`: float
      - `Cr Bader_charge`: float
  - `required_columns`:
  - `units`: object

Notes: The checker relies on the two XYZ files for distance‑recomputation scoring and on the JSON for Bader charge scoring. The coordination numbers reported in the JSON are also verified against the XYZ‑derived values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monometallic_optimized_geometry.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "other",
        "description": "XYZ file with lattice vectors and atomic coordinates. The checker recomputes Cu–O distances and coordination numbers from this file."
      },
      "description": "Optimized geometry of the monometallic CuCe15O31 slab (XYZ)."
    },
    {
      "file": "bimetallic_optimized_geometry.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "other",
        "description": "XYZ file with lattice vectors and atomic coordinates. The checker recomputes Cu–O distances and coordination numbers from this file."
      },
      "description": "Optimized geometry of the bimetallic CrCuCe14O30 slab (type Iα) (XYZ)."
    },
    {
      "file": "structural_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "monometallic": "object",
          "bimetallic": "object"
        },
        "items": {
          "monometallic": {
            "Cu-O_distances": "array of floats (Å)",
            "Cu-O-Ce_distances": "array of floats (Å)",
            "Cu coordination_number": "int",
            "Cu Bader_charge": "float"
          },
          "bimetallic": {
            "Cu-O_distances": "array of floats (Å)",
            "Cu-O-Ce_distances": "array of floats (Å)",
            "Cu coordination_number": "int",
            "Cu Bader_charge": "float",
            "Cr Bader_charge": "float"
          }
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Self-reported structural parameters and Bader charges. Bader charges are compared directly to the paper‑reported values; distances are cross‑checked against the submitted XYZ files."
    }
  ],
  "notes": "The checker relies on the two XYZ files for distance‑recomputation scoring and on the JSON for Bader charge scoring. The coordination numbers reported in the JSON are also verified against the XYZ‑derived values."
}
```

## How you are scored
A hidden verifier evaluates each submitted artifact independently. It recomputes Cu–O distances and coordination numbers from the XYZ files and compares them against expected values; it also compares the Bader charges you report in `structural_parameters.json` against the paper’s reported charges. Scoring uses appropriate numerical tolerances and rewards results that agree well with the reference. The final reward is a weighted average of the scores from the two geometry files and the JSON file, with the Bader charges and structural parameters carrying the largest weight. Reporting the expected numbers without genuinely performing the DFT workflow will be detected and will not yield a high score, because the verifier cross‑checks self‑reported parameters against the geometries you submit.
