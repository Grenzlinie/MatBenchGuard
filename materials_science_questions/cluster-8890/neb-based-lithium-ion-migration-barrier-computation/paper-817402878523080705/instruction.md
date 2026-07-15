# DFT+NEB Computation of Band Gaps and Li-ion Diffusion Barriers in λ-MnO₂/Graphene Composites

## Problem background
Electrochemical adsorption using spinel \(\lambda\)-MnO\(_2\)/graphene composites is a promising route for extracting lithium ions from low-concentration brines and seawater. \(\lambda\)-MnO\(_2\) offers high Li\(^+\) selectivity but suffers from poor electronic and ionic conductivity, while graphene is an excellent conductor. Combining them may enhance conductivity and improve ion diffusion, but the mechanism remains to be clarified. First-principles density functional theory (DFT) calculations can predict key properties — band gaps and ion diffusion energy barriers — that govern electronic and ionic transport, providing insight into the synergy and selectivity.

## Approach
Construct the crystal structure of spinel \(\lambda\)-MnO\(_2\) (space group \(Fd\bar{3}m\)) and a monolayer graphene sheet. Build a composite by placing the (1 0 1) surface of \(\lambda\)-MnO\(_2\) against graphene with a vacuum layer. Perform DFT+U calculations using the PBE-GGA functional to compute total and projected density of states, and extract the band gap from the electronic structure. Use the nudged elastic band (NEB) method to calculate the diffusion energy barriers for Li\(^+\), Na\(^+\), and Mg\(^{2+}\) ions migrating through pure \(\lambda\)-MnO\(_2\), pristine graphene, and at the \(\lambda\)-MnO\(_2\)/graphene interface. Determine the relative ease of diffusion by ordering the computed barriers.

## Reproduction target
Compute the band gap of \(\lambda\)-MnO\(_2\) and the \(\lambda\)-MnO\(_2\)/graphene composite, the diffusion energy barriers for Li\(^+\), Na\(^+\), and Mg\(^{2+}\) in pure \(\lambda\)-MnO\(_2\), in pristine graphene, and in the composite interface, and report these values together with the ordering of diffusion barriers from lowest to highest in a JSON file named `reproduced_results.json`. The target quantities are the band gaps (eV) and diffusion barriers (eV); the ordering should list the ions from lowest to highest barrier for each material (pure \(\lambda\)-MnO\(_2\) and composite). The final JSON must be placed at `/app/outputs/reproduced_results.json`.

## Assets

- λ-MnO₂ (LiMn₂O₄) crystal structure: https://materialsproject.org/materials/mp-22659/
- Monolayer graphene structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): ase
- Ultrasoft pseudopotentials: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: Build and optimize crystal models
- Role: process
- Action: Construct the bulk λ-MnO₂ (space group Fd-3m, a=8.236 Å) and monolayer graphene structures. Cleave the (1 0 1) surface of λ-MnO₂ and build the λ-MnO₂/graphene composite with a vacuum layer of ~15 Å. Perform DFT geometry optimization for all systems (bulk, slab, composite) using Quantum ESPRESSO with PBE-GGA ultrasoft pseudopotentials. Optimize the interfacial distance to a stable value.
- Evidence: `/app/outputs/optimized_structures.log`

### Step 2: Electronic structure calculation
- Role: process
- Action: Perform spin-polarized DFT+U calculations (U=4.0 eV on Mn d electrons) on the optimized pure λ-MnO₂ and λ-MnO₂/graphene composite. Compute total and projected density of states (DOS, PDOS) and extract the band gap values. Use the same PBE functional and pseudopotentials as in step 1.
- Evidence: `/app/outputs/dos_data.json`

### Step 3: NEB ion diffusion barrier calculations
- Role: process
- Action: Set up NEB calculations for Li⁺ diffusion along the 8a–16c–8a path in λ-MnO₂, for Li⁺ between graphene layers (HT–HT path), and for Li⁺ at the λ-MnO₂/graphene interface. Also compute diffusion barriers for Na⁺ and Mg²⁺ in pure λ-MnO₂ and the composite. Use LST/QST for initial path guess and NEB refinement. Freeze all atoms except the diffusing ion.
- Evidence: `/app/outputs/neb_barriers.txt`

### Step 4: Compile final results
- Role: scored (load-bearing)
- Action: Collect the computed band gaps and diffusion energy barriers from the previous steps. Write a single JSON file named 'reproduced_results.json' containing exactly the following fields: band_gap_MnO2 (eV), band_gap_composite (eV), diffusion_barrier_Li_MnO2 (eV), diffusion_barrier_Li_composite (eV), diffusion_barrier_Na_MnO2 (eV), diffusion_barrier_Na_composite (eV), diffusion_barrier_Mg_MnO2 (eV), diffusion_barrier_Mg_composite (eV), diffusion_barrier_Li_graphene (eV, optional), diffusion_ordering_pure (array of strings, sorted low to high barrier), diffusion_ordering_composite (array of strings, sorted low to high barrier).
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: JSON object with keys: band_gap_MnO2 (number), band_gap_composite (number), diffusion_barrier_Li_MnO2 (number), diffusion_barrier_Li_composite (number), diffusion_barrier_Na_MnO2 (number), diffusion_barrier_Na_composite (number), diffusion_barrier_Mg_MnO2 (number), diffusion_barrier_Mg_composite (number), diffusion_barrier_Li_graphene (number, optional), diffusion_ordering_pure (array of strings), diffusion_ordering_composite (array of strings).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the computed band gaps (eV) and diffusion energy barriers (eV) for Li⁺, Na⁺ and Mg²⁺ in λ-MnO₂ and λ-MnO₂/graphene, along with the relative ordering.
- schema:
  - `type`: object
  - `properties`:
    - `band_gap_MnO2`:
      - `type`: number
    - `band_gap_composite`:
      - `type`: number
    - `diffusion_barrier_Li_MnO2`:
      - `type`: number
    - `diffusion_barrier_Li_composite`:
      - `type`: number
    - `diffusion_barrier_Na_MnO2`:
      - `type`: number
    - `diffusion_barrier_Na_composite`:
      - `type`: number
    - `diffusion_barrier_Mg_MnO2`:
      - `type`: number
    - `diffusion_barrier_Mg_composite`:
      - `type`: number
    - `diffusion_barrier_Li_graphene`:
      - `type`: number
    - `diffusion_ordering_pure`:
      - `type`: array
      - `items`:
        - `type`: string
      - `description`: List of ions ['Li','Na','Mg'] sorted by increasing barrier in pure λ-MnO₂.
    - `diffusion_ordering_composite`:
      - `type`: array
      - `items`:
        - `type`: string
      - `description`: List of ions ['Li','Na','Mg'] sorted by increasing barrier in the composite.
  - `required`: `band_gap_MnO2`, `band_gap_composite`, `diffusion_barrier_Li_MnO2`, `diffusion_barrier_Li_composite`, `diffusion_barrier_Na_MnO2`, `diffusion_barrier_Na_composite`, `diffusion_barrier_Mg_MnO2`, `diffusion_barrier_Mg_composite`, `diffusion_ordering_pure`, `diffusion_ordering_composite`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "band_gap_MnO2": {
            "type": "number"
          },
          "band_gap_composite": {
            "type": "number"
          },
          "diffusion_barrier_Li_MnO2": {
            "type": "number"
          },
          "diffusion_barrier_Li_composite": {
            "type": "number"
          },
          "diffusion_barrier_Na_MnO2": {
            "type": "number"
          },
          "diffusion_barrier_Na_composite": {
            "type": "number"
          },
          "diffusion_barrier_Mg_MnO2": {
            "type": "number"
          },
          "diffusion_barrier_Mg_composite": {
            "type": "number"
          },
          "diffusion_barrier_Li_graphene": {
            "type": "number"
          },
          "diffusion_ordering_pure": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of ions ['Li','Na','Mg'] sorted by increasing barrier in pure λ-MnO₂."
          },
          "diffusion_ordering_composite": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of ions ['Li','Na','Mg'] sorted by increasing barrier in the composite."
          }
        },
        "required": [
          "band_gap_MnO2",
          "band_gap_composite",
          "diffusion_barrier_Li_MnO2",
          "diffusion_barrier_Li_composite",
          "diffusion_barrier_Na_MnO2",
          "diffusion_barrier_Na_composite",
          "diffusion_barrier_Mg_MnO2",
          "diffusion_barrier_Mg_composite",
          "diffusion_ordering_pure",
          "diffusion_ordering_composite"
        ]
      },
      "description": "Scored artifact containing the computed band gaps (eV) and diffusion energy barriers (eV) for Li⁺, Na⁺ and Mg²⁺ in λ-MnO₂ and λ-MnO₂/graphene, along with the relative ordering."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier program reads the produced JSON file and compares each reported band gap and diffusion barrier to reference values derived from the original study, using appropriate tolerances. It also checks that the ordering arrays correctly reflect the relative ease of diffusion (Li < Na < Mg). Each scored quantity contributes a weighted fraction to the final reward between 0 and 1. The verification uses a result-level comparison: the reported numbers are compared directly against hidden reference values, rewarding correct reproduction within numerical tolerances. Simply declaring the paper's results without executing the required computations will not yield the correct artifacts for scoring.
