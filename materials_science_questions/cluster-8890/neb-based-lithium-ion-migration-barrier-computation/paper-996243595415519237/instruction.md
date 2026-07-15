# DFT Calculation of Li-Ion Migration Barriers and Band Gap Trends in a Phosphorus–Carbon Heterostructure

## Problem background
Black phosphorus (BP) is a high-capacity anode material for lithium-ion batteries, but it undergoes large volume expansion and suffers from structural degradation during cycling. A recent strategy to stabilize the electrode is to construct a covalent lateral/vertical heterostructure between BP and graphdiyne oxide (GDYO). The heterostructure is expected to modify the electronic structure and create favorable Li-ion transport pathways at the interface. Density functional theory (DFT) calculations are used to quantify these effects by computing the electronic band gap, the energy barriers for Li-ion migration along different pathways, and the Li adsorption energies at various binding sites. This task reproduces those DFT predictions to assess the electronic and ionic transport characteristics of the BP–GDYO heterostructure.

## Approach
Construct atomistic models for bulk BP, a defect-free BP edge, an edge-reconstructed BP edge, a GDYO monolayer, and a lateral BP–GDYO heterostructure interface. Starting from publicly available crystal structures, perform DFT geometry optimizations with an open-source plane-wave DFT code (Quantum ESPRESSO, or equivalent) using a suitable exchange–correlation functional and pseudopotentials. After relaxation, compute the electronic density of states for bulk BP and the BP–GDYO heterostructure to extract the Kohn–Sham band gap. Then, use the nudged elastic band (NEB) method to determine the Li-ion migration energy barrier for three pathways: across the BP–GDYO interface, along a defect-free BP edge, and along an edge-reconstructed BP edge. Finally, calculate Li adsorption energies on four sites: the BP phase within the heterostructure, the GDYO surface, a defect-free BP surface, and an edge-reconstructed BP surface, using the total energy difference between the combined system, the isolated substrate, and an isolated Li atom.

## Reproduction target
Produce three JSON output files as specified in the workflow steps: the band gap values, the three Li-ion migration energy barriers, and the four Li adsorption energies (all in eV). The hidden verifier will evaluate whether the computed numbers satisfy the expected physical relationships that motivate the heterostructure design, checking for consistency of the relative ordering of the barriers and binding energies. Correct relative trends, rather than exact numerical matches, determine success.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bulk black phosphorus crystal structure: https://next-gen.materialsproject.org/materials/mp-1143
- Graphdiyne (GDY) crystal structure: doi:10.1002/anie.201612196 / CCDC 1401460
- SSSP precision pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Construct supercell models for bulk BP, defect‑free BP edge, edge‑reconstructed BP edge, GDYO monolayer, and the BP–GDYO lateral heterostructure interface. Use the public crystal structures as starting points. Save initial atomic coordinates.
- Evidence: none

### Step 2: Geometry optimization
- Role: process
- Action: For each model, perform DFT structural relaxation using Quantum ESPRESSO (pw.x) with an appropriate exchange‑correlation functional and pseudopotentials. Converge forces and energy to sufficient tolerance. Save the optimized structures.
- Evidence: none

### Step 3: Band gap from density of states
- Role: scored
- Action: Perform self‑consistent DFT calculations for the optimized bulk BP and BP–GDYO heterostructure. Compute the electronic density of states and extract the Kohn–Sham band gap. Output both values in eV.
- Output file: `/app/outputs/step_01_band_gap.json`
- Format: json
- Contract: JSON object with keys: 'bulk_BP_band_gap_ev' (float) and 'BP_GDYO_band_gap_ev' (float).
- Scoring: scored by hidden verifier

### Step 4: Li‑ion migration barriers
- Role: scored (load-bearing)
- Action: For the BP–GDYO interfacial pathway, the defect‑free BP edge, and the edge‑reconstructed BP edge, run NEB calculations (neb.x in Quantum ESPRESSO) with a Li ion moving between two stable sites. Extract the maximum energy along the path as the migration barrier. Output the three barriers in eV.
- Output file: `/app/outputs/step_02_migration_barriers.json`
- Format: json
- Contract: JSON object with keys: 'BP_GDYO_barrier_ev' (float), 'defect_free_BP_edge_barrier_ev' (float), 'edge_reconstructed_BP_barrier_ev' (float).
- Scoring: scored by hidden verifier

### Step 5: Li adsorption energies
- Role: scored
- Action: For Li adsorbed on the BP phase (within BP–GDYO), on GDYO, on defect‑free BP, and on edge‑reconstructed BP, compute total energies of the combined system, isolated substrate, and isolated Li atom. Calculate adsorption energy as E_ads = E_total − E_substrate − E_Li. Output the four energies in eV.
- Output file: `/app/outputs/step_03_adsorption_energies.json`
- Format: json
- Contract: JSON object with keys: 'BP_phase_adsorption_ev' (float), 'GDYO_adsorption_ev' (float), 'defect_free_BP_adsorption_ev' (float), 'edge_reconstructed_BP_adsorption_ev' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gap.json`
- `/app/outputs/step_02_migration_barriers.json`
- `/app/outputs/step_03_adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gap.json
- path: `/app/outputs/step_01_band_gap.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Band gap values from DFT density-of-states calculations. The expected trend is BP_GDYO_band_gap_ev < bulk_BP_band_gap_ev.
- schema:
  - `type`: object
  - `required`:
    - `bulk_BP_band_gap_ev`: float
    - `BP_GDYO_band_gap_ev`: float

### step_02_migration_barriers.json
- path: `/app/outputs/step_02_migration_barriers.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Li-ion migration energy barriers from NEB calculations. The expected ordering is BP_GDYO_barrier_ev < defect_free_BP_edge_barrier_ev < edge_reconstructed_BP_barrier_ev.
- schema:
  - `type`: object
  - `required`:
    - `BP_GDYO_barrier_ev`: float
    - `defect_free_BP_edge_barrier_ev`: float
    - `edge_reconstructed_BP_barrier_ev`: float

### step_03_adsorption_energies.json
- path: `/app/outputs/step_03_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Li adsorption energies on four sites. The expected ordering (more negative indicates stronger binding) is BP_phase_adsorption_ev < GDYO_adsorption_ev < defect_free_BP_adsorption_ev < edge_reconstructed_BP_adsorption_ev.
- schema:
  - `type`: object
  - `required`:
    - `BP_phase_adsorption_ev`: float
    - `GDYO_adsorption_ev`: float
    - `defect_free_BP_adsorption_ev`: float
    - `edge_reconstructed_BP_adsorption_ev`: float

Notes: All values are in eV. Scoring uses structural ordering with a small tolerance (e.g., 0.1 eV) to accept nearly equal values as correct ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "bulk_BP_band_gap_ev": "float",
          "BP_GDYO_band_gap_ev": "float"
        }
      },
      "description": "Band gap values from DFT density-of-states calculations. The expected trend is BP_GDYO_band_gap_ev < bulk_BP_band_gap_ev."
    },
    {
      "file": "step_02_migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "BP_GDYO_barrier_ev": "float",
          "defect_free_BP_edge_barrier_ev": "float",
          "edge_reconstructed_BP_barrier_ev": "float"
        }
      },
      "description": "Li-ion migration energy barriers from NEB calculations. The expected ordering is BP_GDYO_barrier_ev < defect_free_BP_edge_barrier_ev < edge_reconstructed_BP_barrier_ev."
    },
    {
      "file": "step_03_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "BP_phase_adsorption_ev": "float",
          "GDYO_adsorption_ev": "float",
          "defect_free_BP_adsorption_ev": "float",
          "edge_reconstructed_BP_adsorption_ev": "float"
        }
      },
      "description": "Li adsorption energies on four sites. The expected ordering (more negative indicates stronger binding) is BP_phase_adsorption_ev < GDYO_adsorption_ev < defect_free_BP_adsorption_ev < edge_reconstructed_BP_adsorption_ev."
    }
  ],
  "notes": "All values are in eV. Scoring uses structural ordering with a small tolerance (e.g., 0.1 eV) to accept nearly equal values as correct ordering."
}
```

## How you are scored
A hidden checker independently scores each of the three workflow outputs. Each scored artifact is compared against physical expectations, and the individual scores are combined into a final reward between 0 and 1. You must genuinely execute the DFT calculations and produce consistent results—simply reporting numbers from a reference or fabricating values will lead to low or zero reward. The tolerance for near-equal values is generous enough to accommodate method-dependent shifts, so an honest re‑run that captures the correct trends will score well.
