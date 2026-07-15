# Compute vacancy formation and migration activation energies near a twist grain boundary in copper

## Problem background
Grain boundaries play a critical role in materials properties such as grain growth, deformation, and fracture, and atomic diffusion along boundaries is central to these phenomena. Understanding how vacancies form and migrate near a grain boundary is essential for predicting diffusion behavior and vacancy accumulation. This task investigates the energetic landscape of a single vacancy in the vicinity of a copper Σ=5 [001] twist grain boundary by computing the formation energies at different positions and the migration activation barriers for intra- and inter-layer hops using molecular dynamics with a modified analytical embedded-atom method (MAEAM) potential.

## Approach
The atomic interactions are described by a modified analytical embedded-atom method (MAEAM) potential for Cu, whose functional forms and all parameter values are fully specified in this instruction. The grain boundary is modeled as a Σ=5 [001] twist boundary with a supercell containing two grains of 30 layers each, periodic in the boundary plane, and a surrounding mantle of fixed atoms. The MAEAM energy and forces are computed from the pairwise and embedding terms, and the system is relaxed using a predictor–corrector molecular dynamics algorithm. Vacancy formation energies are obtained by comparing the total energy of the perfect cell with that of a cell containing a single vacancy, plus the cohesion energy. Migration activation energies are determined by mapping the minimum-energy path for vacancy hops within a layer or between adjacent layers, identifying the saddle-point energy relative to the initial equilibrium site. The computation is performed for the three inequivalent coincident-site-lattice (CSL) sites in each of the first four atomic layers on one side of the boundary, plus a bulk reference, and for the nearest-neighbor migration paths defined in the instruction.

## Reproduction target
Compute the vacancy formation energy for each inequivalent CSL site (coincident and un-coincident) in layers 1–4 and in bulk Cu, and compute the activation energy for every intra-layer migration path in layers 1–4 and every inter-layer migration path including the cross-boundary jump to the rotating grain (1L–1LR). The output must be two JSON files: one containing the formation energies in eV following the schema in Step 2, and one containing the activation energies in eV following the schema in Step 3. All energies must be obtained by molecular dynamics relaxations using the provided MAEAM potential and the grain boundary supercell built in Step 1.

## Assets
This task does not require any external datasets or pre-trained models. All needed components are either provided in this instruction or are standard Python libraries. The MAEAM potential functional forms and all parameter values for copper are reproduced in the instruction. You may use Python 3 with NumPy for numerical operations. Molecular dynamics integration and energy minimization can be implemented from scratch or using a general-purpose optimization library, but no specific MD package is mandated.

## Workflow steps

### Step 1: Build Σ=5 [001] twist grain boundary supercell and identify vacancy sites
- Role: process
- Action: Construct the atomic supercell for a Cu Σ=5 [001] twist grain boundary with two grains of 30 layers each, a free-atom region of approximately 5a x 5a x 10a (a = lattice constant), and a surrounding mantle of fixed atoms. Identify the three inequivalent coincident-site-lattice sites per layer (coincident site '1'/'a', and un-coincident sites '2'/'b' and '3'/'c') in the first four atomic layers adjacent to the boundary and in a bulk reference region. Save the supercell and site labels for later steps.
- Evidence: `/app/outputs/gb_supercell.data`

### Step 2: Vacancy formation energies
- Role: scored (load-bearing)
- Action: Implement the MAEAM interatomic potential for Cu using the provided functional forms and parameter values. For each inequivalent site (coincident and un-coincident) in layers 1–4 and a bulk reference, create a single vacancy by removing the corresponding atom and relax the system using molecular dynamics with MAEAM forces. Compute the formation energy Ef = E(N-1,1) – E(N,0) + Ec, where E(N-1,1) is the energy of the cell with a vacancy, E(N,0) is the energy of the perfect cell, and Ec is the cohesion energy. Collect all formation energies (in eV) in a structured JSON file.
- Output file: `/app/outputs/step_01_formation_energies.json`
- Format: json
- Contract: A JSON object with key 'bulk_formation_energy' (float) and for each of the first four layers a key 'layer1', 'layer2', 'layer3', 'layer4'. Each layer value is an object with keys 'site1', 'site2', 'site3' mapping to the formation energy in eV (float). Example: {"bulk_formation_energy": 1.1838, "layer1": {"site1": 1.1814, "site2": -0.2288, "site3": -0.2288}, ...}
- Scoring: scored by hidden verifier

### Step 3: Vacancy migration activation energies
- Role: scored (load-bearing)
- Action: For each defined intra-layer migration path in layers 1L, 2L, 3L, 4L (nearest-neighbor jumps) and each defined inter-layer migration path (1L-1LR, 2L-1L, 3L-2L, 4L-3L, 5L-4L), sample the system energy along the migration path (e.g., by stepwise displacement of the vacancy followed by constrained relaxations) to identify the saddle point energy Esad. Compute the activation energy Qv = Esad – Eeq + Ev, where Eeq is the equilibrium energy of the initial vacancy site and Ev is the vacancy formation energy at that site from step 01. Use the site labels from the paper (1,2,3 for odd layers; a,b,c for even layers; cR, bR for the rotating grain). Collect all activation energies (in eV) in a structured JSON file.
- Output file: `/app/outputs/step_02_activation_energies.json`
- Format: json
- Contract: A JSON object with top-level keys for each migration path: 'intra_1L', 'intra_2L', 'intra_3L', 'intra_4L', 'inter_1L-1LR', 'inter_2L-1L', 'inter_3L-2L', 'inter_4L-3L', 'inter_5L-4L'. Each path's value is an object whose keys are strings of the form '<source_site>_to_<target_site>' (e.g., '1_to_2', 'c_to_a', '2_to_cR') and whose values are the activation energy in eV (float). All site labels must use the exact notation from the paper.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.json`
- `/app/outputs/step_02_activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.json
- path: `/app/outputs/step_01_formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Layer- and site-resolved vacancy formation energies computed via MD/MAEAM. All energies are in eV. The JSON must contain exactly the specified keys.
- schema:
  - `type`: object
  - `required`:
    - `bulk_formation_energy`: float (eV)
    - `layer1`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)
    - `layer2`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)
    - `layer3`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)
    - `layer4`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)

### step_02_activation_energies.json
- path: `/app/outputs/step_02_activation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Vacancy migration activation energies for intra- and inter-layer paths. All energies in eV. The JSON must contain entries for every path listed, using the correct site labels from the paper.
- schema:
  - `type`: object
  - `required`:
    - `intra_1L`: object with keys like '1_to_2', '2_to_3', etc. mapping to float activation energy (eV)
    - `intra_2L`: object with keys like 'a_to_b', 'b_to_c', etc.
    - `intra_3L`: object with keys like '1_to_2', '2_to_3', etc.
    - `intra_4L`: object with keys like 'a_to_b', 'b_to_c', etc.
    - `inter_1L-1LR`: object with keys like '2_to_cR', '3_to_bR', etc.
    - `inter_2L-1L`: object with keys like 'a_to_2', 'b_to_2', etc.
    - `inter_3L-2L`: object with keys like '1_to_a', '2_to_a', etc.
    - `inter_4L-3L`: object with keys like 'a_to_1', 'b_to_1', etc.
    - `inter_5L-4L`: object with keys like '1_to_a', '2_to_a', etc.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_formation_energy": "float (eV)",
          "layer1": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          },
          "layer2": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          },
          "layer3": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          },
          "layer4": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          }
        }
      },
      "description": "Layer- and site-resolved vacancy formation energies computed via MD/MAEAM. All energies are in eV. The JSON must contain exactly the specified keys."
    },
    {
      "file": "step_02_activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "intra_1L": "object with keys like '1_to_2', '2_to_3', etc. mapping to float activation energy (eV)",
          "intra_2L": "object with keys like 'a_to_b', 'b_to_c', etc.",
          "intra_3L": "object with keys like '1_to_2', '2_to_3', etc.",
          "intra_4L": "object with keys like 'a_to_b', 'b_to_c', etc.",
          "inter_1L-1LR": "object with keys like '2_to_cR', '3_to_bR', etc.",
          "inter_2L-1L": "object with keys like 'a_to_2', 'b_to_2', etc.",
          "inter_3L-2L": "object with keys like '1_to_a', '2_to_a', etc.",
          "inter_4L-3L": "object with keys like 'a_to_1', 'b_to_1', etc.",
          "inter_5L-4L": "object with keys like '1_to_a', '2_to_a', etc."
        }
      },
      "description": "Vacancy migration activation energies for intra- and inter-layer paths. All energies in eV. The JSON must contain entries for every path listed, using the correct site labels from the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently score each of the scored workflow stages (vacancy formation energies and vacancy migration activation energies) by comparing your submitted JSON artifacts against reference values. The verifier combines the scores from the individual stages into a final reward between 0 and 1. You must produce outputs that follow exactly the required format and contain physically correct energies computed from the specified potential and geometry. Reporting numbers without performing the required molecular dynamics relaxations will not succeed, as the verifier checks both the values and their consistency.
