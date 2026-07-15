# DFT Formation Energy Calculation for 2D Perovskite Stability

## Problem background
Lead halide perovskites such as CsPbBr₃ and MAPbI₃ are promising photovoltaic materials, but their long‑term stability is a major hurdle. Surprisingly, reducing the material from 3D bulk to 2D slabs can sometimes enhance stability, contradicting the usual expectation that surfaces increase energy. The thermodynamic origin of this behavior is not well understood. This task investigates the stability of 2D versus 3D perovskites by computing the total energies needed to derive formation energies, surface energies, and cleavage energies for different surface terminations and slab thicknesses. By systematically performing first‑principles DFT calculations, you will provide the raw energies that reveal why certain 2D structures can be more stable than the bulk.

## Approach
We use density functional theory (DFT) with the PBEsol exchange‑correlation functional to calculate total energies of all relevant systems. Because the original study used a proprietary code, you must implement the workflow with an open‑source DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials (such as the SSSP PBEsol library).

The key systems are:
- Bulk binary compounds: CsBr, PbBr₂, PbI₂, and MAI (CH₃NH₃I).
- Bulk ternary perovskites: orthorhombic γ‑CsPbBr₃ and γ‑MAPbI₃.
- Symmetric (001) slab models of CsPbBr₃ and MAPbI₃, each with two surface terminations (AX‑terminated and BX₂‑terminated) and three thicknesses L1 (monolayer), L2 (double‑layer), L3 (triple‑layer), all with a vacuum layer >14 Å.

For each system you must perform geometry optimization (except for “ideal” slabs, where only a single‑point energy is computed) and extract the total energy. The final artifact is a JSON file that compiles all these total energies; the derivation of formation energies, surface energies, and cleavage energies is then carried out automatically by the scorer, not by you.

## Reproduction target
Produce the file `/app/outputs/total_energies.json` containing the DFT total energies (in eV) of:
- The four bulk binaries (CsBr, PbBr₂, PbI₂, MAI) and the two bulk ternaries (γ‑CsPbBr₃, γ‑MAPbI₃).
- All 12 slab models: two compounds × two terminations (AX, BX₂) × three thicknesses (L1, L2, L3), each in both ideal (unrelaxed) and relaxed states.
The exact schema is defined in the output contract; you must follow it precisely. You do not need to compute any derived thermodynamic quantities yourself — the hidden verifier will recompute all formation, surface, and cleavage energies from your supplied total energies.

## Assets

- γ-CsPbBr₃ crystal structure (orthorhombic): 10.1021/cg400645t
- γ-MAPbI₃ crystal structure (orthorhombic): 10.1039/C4CC07063E
- CsBr crystal structure (rock salt)
- PbBr₂ crystal structure (orthorhombic)
- PbI₂ crystal structure (2H polytype)
- MAI (CH₃NH₃I) crystal structure (tetragonal): 10.1107/S0108768192002823
- Density functional theory code (open-source): https://www.quantum-espresso.org
- SSSP pseudopotential library (PBEsol): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare crystal structures and slab models
- Role: process
- Action: Obtain CIF files for all required bulk compounds (γ-CsPbBr3, γ-MAPbI3, CsBr, PbBr2, PbI2, MAI) from public databases or supplementary material. Use the bulk structures to construct input files for the DFT code, including symmetric (001) slab models with AX- and PbX2-terminations at thicknesses L1 (monolayer), L2 (double-layer), and L3 (triple-layer), each with a vacuum layer >14 Å. This step produces the initial structures for all subsequent DFT calculations.
- Evidence: `/app/outputs/structure_files`

### Step 2: DFT relaxations of bulk binaries and ternaries
- Role: process
- Action: Perform DFT geometry optimizations for all bulk binaries (CsBr, PbBr2, PbI2, MAI) and the bulk ternary perovskites (γ-CsPbBr3, γ-MAPbI3) using the PBEsol exchange-correlation functional and appropriate pseudopotentials. Calculate the total energy for each system after converging to high precision (< 1 meV/atom).
- Evidence: `/app/outputs/bulk_relax_logs`

### Step 3: DFT static energies of ideal (unrelaxed) slabs
- Role: process
- Action: For each of the 12 slab models (2 compounds × 2 terminations × 3 thicknesses), perform single-point DFT energy calculations without relaxation, using the same functional and pseudopotentials. Record the total energy for each ideal slab.
- Evidence: `/app/outputs/ideal_slab_logs`

### Step 4: DFT relaxations of slab models
- Role: process
- Action: Perform DFT geometry optimizations for all 12 slab models (both terminations, L1–L3 for each compound) using the same settings. Converge forces to tight thresholds and record the relaxed total energy for each slab.
- Evidence: `/app/outputs/relaxed_slab_logs`

### Step 5: Compile total energies into scored artifact
- Role: scored (load-bearing)
- Action: Collect the total energies (in eV) from steps 2, 3, and 4 and write a JSON file with the exact schema described in the output contract.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: JSON object with top-level keys: binary_total_energies, ternary_total_energies, slab_total_energies (as defined in the output contract).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Compiled total energies (eV) of bulk binaries, ternaries, and slab models for both compounds. The checker recomputes bulk formation energies, 2D slab formation energies (under AX-rich and BX2-rich conditions), surface energies of triple-layer slabs (ideal and relaxed), and cleavage energies from this artifact, then compares to hidden reference values with tolerances and verifies ordering trends.
- schema:
  - `type`: object
  - `required_keys`: `binary_total_energies`, `ternary_total_energies`, `slab_total_energies`
  - `details`:
    - `binary_total_energies`:
      - `type`: object
      - `required_keys`: `CsBr`, `PbBr2`, `MAI`, `PbI2`
      - `value_type`: number
      - `units`: eV
    - `ternary_total_energies`:
      - `type`: object
      - `required_keys`: `CsPbBr3`, `MAPbI3`
      - `value_type`: number
      - `units`: eV
    - `slab_total_energies`:
      - `type`: array
      - `item_shape`:
        - `compound`: string ('CsPbBr3' or 'MAPbI3')
        - `termination`: string ('AX' or 'BX2')
        - `thickness`: integer (1, 2, or 3)
        - `relaxation`: string ('ideal' or 'relaxed')
        - `energy_eV`: number

Notes: All derived quantities (formation energies, surface energies, cleavage energies) are computed by the checker from this single artifact; the solving agent does not compute them.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required_keys": [
          "binary_total_energies",
          "ternary_total_energies",
          "slab_total_energies"
        ],
        "details": {
          "binary_total_energies": {
            "type": "object",
            "required_keys": [
              "CsBr",
              "PbBr2",
              "MAI",
              "PbI2"
            ],
            "value_type": "number",
            "units": "eV"
          },
          "ternary_total_energies": {
            "type": "object",
            "required_keys": [
              "CsPbBr3",
              "MAPbI3"
            ],
            "value_type": "number",
            "units": "eV"
          },
          "slab_total_energies": {
            "type": "array",
            "item_shape": {
              "compound": "string ('CsPbBr3' or 'MAPbI3')",
              "termination": "string ('AX' or 'BX2')",
              "thickness": "integer (1, 2, or 3)",
              "relaxation": "string ('ideal' or 'relaxed')",
              "energy_eV": "number"
            }
          }
        }
      },
      "description": "Compiled total energies (eV) of bulk binaries, ternaries, and slab models for both compounds. The checker recomputes bulk formation energies, 2D slab formation energies (under AX-rich and BX2-rich conditions), surface energies of triple-layer slabs (ideal and relaxed), and cleavage energies from this artifact, then compares to hidden reference values with tolerances and verifies ordering trends."
    }
  ],
  "notes": "All derived quantities (formation energies, surface energies, cleavage energies) are computed by the checker from this single artifact; the solving agent does not compute them."
}
```

## How you are scored
A hidden verifier reads your `total_energies.json` file and recomputes the bulk formation energies, the 2D slab formation energies under appropriate chemical‑potential conditions, the surface energies of triple‑layer slabs, and the cleavage energies, using the standard thermodynamic relations for these systems. The verifier compares the derived numbers and certain qualitative relationships (e.g., ordering between terminations and thicknesses) against hidden reference values. Your final reward is a weighted combination of how many of these checks are satisfied. The more accurately your DFT total energies reproduce the expected physical trends and values, the higher your score will be.
