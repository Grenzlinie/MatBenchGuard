# Adsorption Energies and Diffusion Barrier of Lithium Polysulfides on InP3 Monolayer

## Problem background
Lithium-sulfur (Li-S) batteries offer high theoretical energy density but suffer from the polysulfide shuttle effect, where soluble lithium polysulfides (LiPSs) migrate between electrodes, degrading capacity and coulombic efficiency. Anchoring materials that strongly bind LiPSs can mitigate this problem. This work investigates whether an InP3 monolayer can serve as an effective anchoring material by computationally determining the adsorption strengths of six key S-containing species (Li2S, Li2S2, Li2S4, Li2S6, Li2S8, S8) and the surface diffusion barrier of Li2S.

## Approach
The core computational protocol uses density functional theory (DFT) with the GGA-PBE exchange-correlation functional, supplemented by the DFT-D2 van der Waals correction. Adsorption energies are obtained as total energy differences: E_ads = E(InP3 + adsorbate) − E(InP3) − E(isolated adsorbate). To model the battery electrolyte environment, calculations are repeated using an implicit solvent model (COSMO) with a dielectric constant ε = 7.17, representative of DME/DOL solvent. Both with and without the DFT-D2 dispersion term are evaluated to separate physical and chemical contributions. For Li2S diffusion, a transition‑state search (e.g., LST/QST or NEB) locates the energy barrier between two equivalent adsorption sites.

## Reproduction target
Using DFT (GGA-PBE, DFT-D2, implicit COSMO solvent model with ε=7.17), build a 2×2 InP3 supercell with a vacuum layer of at least 15 Å and a 4×4×1 k-point mesh. Optimize the pristine monolayer and isolated clusters of Li2S, Li2S2, Li2S4, Li2S6, Li2S8, and S8 in vacuum and in implicit solvent. For each adsorbate, place the molecule on several plausible sites, relax the combined system, and identify the most stable configuration. For every species, compute the adsorption energy (Eq. 1) in vacuum and in solvent, both with and without DFT-D2 dispersion. For Li2S, compute the diffusion energy barrier between two equivalent adsorption sites via transition‑state search. Write all computed values into a single JSON file: `/app/outputs/results.json`.

## Assets

- Open-source DFT software supporting GGA-PBE functional and DFT-D2 dispersion correction (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- PBE pseudopotentials library (e.g., SSSP PBE efficiency): https://www.quantum-espresso.org/pseudopotentials/
- InP3 monolayer crystal structure from Miao et al., J. Am. Chem. Soc. 2017: 10.1021/jacs.7b05630

## Workflow steps

### Step 1: Optimize pristine InP3 monolayer
- Role: process
- Action: Build a 2x2 supercell of the InP3 monolayer with a vacuum layer of at least 15 Å, then relax the atomic positions and cell (if needed) using DFT-PBE with a suitable basis and k-point sampling. Record the optimized geometry and total energy.
- Evidence: `/app/outputs/inp3_relaxed.xyz`

### Step 2: Optimize isolated LiPS and S8 clusters
- Role: process
- Action: Set up isolated clusters of Li2S, Li2S2, Li2S4, Li2S6, Li2S8, and S8 in a large simulation box. Optimize the geometry of each cluster in vacuum and in an implicit solvent (COSMO model, dielectric constant epsilon = 7.17) using the same DFT settings. Record the total energy of each optimized cluster.
- Evidence: `/app/outputs/isolated_clusters.xyz`

### Step 3: Adsorption energies and Li2S diffusion barrier
- Role: scored (load-bearing)
- Action: For each of the six adsorbates (Li2S, Li2S2, Li2S4, Li2S6, Li2S8, S8), place the molecule on several plausible adsorption sites of the optimized 2x2 InP3 supercell, relax the combined system, and identify the most stable configuration. For the most stable configuration, compute the total energy of the InP3+adsorbate system in vacuum and in implicit solvent (COSMO, epsilon=7.17), both with and without DFT-D2 van der Waals correction. Compute the adsorption energy E_ads = E(InP3+adsorbate) - E(InP3) - E(isolated) for each condition. For Li2S, perform a transition-state search (e.g., LST/QST or NEB) between two equivalent adsorption sites to obtain the diffusion energy barrier. Write all results to a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type":"object","required":["adsorption_energies","diffusion_barrier"],"properties":{"adsorption_energies":{"type":"array","items":{"type":"object","required":["species","condition","with_vdw","energy_eV"],"properties":{"species":{"type":"string","description":"One of Li2S, Li2S2, Li2S4, Li2S6, Li2S8, S8"},"condition":{"type":"string","enum":["vacuum","solvent"]},"with_vdw":{"type":"boolean"},"energy_eV":{"type":"number","description":"Adsorption energy in eV"}}}},"diffusion_barrier":{"type":"object","required":["species","barrier_eV"],"properties":{"species":{"type":"string","description":"Li2S"},"barrier_eV":{"type":"number","description":"Diffusion energy barrier in eV"}}}}}
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
- target_policy: reference_match
- description: Adsorption energies (with and without van der Waals correction, in vacuum and in implicit solvent) for six species, and the Li2S diffusion barrier, compared against the paper's reference values.
- schema:
  - `type`: object
  - `required`: `adsorption_energies`, `diffusion_barrier`
  - `properties`:
    - `adsorption_energies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `species`, `condition`, `with_vdw`, `energy_eV`
        - `properties`:
          - `species`:
            - `type`: string
            - `description`: One of Li2S, Li2S2, Li2S4, Li2S6, Li2S8, S8
          - `condition`:
            - `type`: string
            - `enum`: `vacuum`, `solvent`
          - `with_vdw`:
            - `type`: boolean
          - `energy_eV`:
            - `type`: number
            - `units`: eV
    - `diffusion_barrier`:
      - `type`: object
      - `required`: `species`, `barrier_eV`
      - `properties`:
        - `species`:
          - `type`: string
          - `description`: Li2S
        - `barrier_eV`:
          - `type`: number
          - `units`: eV

Notes: The hidden checker reads this file, extracts each reported value, and compares it to the paper's reference using tolerances; only the scored outputs are declared here.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "adsorption_energies",
          "diffusion_barrier"
        ],
        "properties": {
          "adsorption_energies": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "species",
                "condition",
                "with_vdw",
                "energy_eV"
              ],
              "properties": {
                "species": {
                  "type": "string",
                  "description": "One of Li2S, Li2S2, Li2S4, Li2S6, Li2S8, S8"
                },
                "condition": {
                  "type": "string",
                  "enum": [
                    "vacuum",
                    "solvent"
                  ]
                },
                "with_vdw": {
                  "type": "boolean"
                },
                "energy_eV": {
                  "type": "number",
                  "units": "eV"
                }
              }
            }
          },
          "diffusion_barrier": {
            "type": "object",
            "required": [
              "species",
              "barrier_eV"
            ],
            "properties": {
              "species": {
                "type": "string",
                "description": "Li2S"
              },
              "barrier_eV": {
                "type": "number",
                "units": "eV"
              }
            }
          }
        }
      },
      "description": "Adsorption energies (with and without van der Waals correction, in vacuum and in implicit solvent) for six species, and the Li2S diffusion barrier, compared against the paper's reference values."
    }
  ],
  "notes": "The hidden checker reads this file, extracts each reported value, and compares it to the paper's reference using tolerances; only the scored outputs are declared here."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json`, extracts each reported adsorption energy and the diffusion barrier, and compares them to hidden reference values using appropriate tolerances. It also checks that all adsorption energies are negative, the diffusion barrier is positive, and that the magnitude ordering across species conforms to physical expectations. The final reward is a weighted fraction of values that pass the checks; full credit requires all quantities to fall within tolerances and all qualitative requirements to be met.
