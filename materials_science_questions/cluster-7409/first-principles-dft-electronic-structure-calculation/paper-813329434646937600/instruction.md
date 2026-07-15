# First-principles DFT calculation of rutile TiO2 band gaps and surface formation energies

## Problem background
Rutile titanium dioxide (TiO₂) is a widely studied semiconductor for photocatalysis, solar cells, and water splitting. Understanding the electronic band structure and the stability of its surfaces is essential for predicting and engineering its reactivity. In a solid, the electronic gap depends on dimensionality—how it changes from an infinite bulk crystal to a thin slab is an open problem. This task addresses that question for the rutile polymorph by having you compute, from first principles, the electronic band gap of bulk rutile and of (110) surface slabs with different numbers of atomic layers, as well as the surface formation energies that determine which termination is thermodynamically preferred.

## Approach
The calculations are carried out with periodic density functional theory using a hybrid functional (B3LYP or an equivalent such as PBE0). You will first fully optimize the bulk rutile crystal (lattice parameters and atomic positions). From the optimized bulk, you will construct slab models of the (110) surface: five models in total, covering three thicknesses (3, 6, and 9 atomic layers) all terminated at the second atomic plane, plus two additional 3‑layer slabs terminated at the first and third atomic planes. A vacuum region of at least 15 Å is placed perpendicular to the surface. For each slab, only the atomic positions are relaxed while keeping the in‑plane cell fixed to the bulk values. Afterwards, non‑self‑consistent band‑structure calculations along high‑symmetry paths are performed and the direct band gap at the Γ point is extracted for the bulk and for every slab. The surface formation energy is computed with a modified formula:

E_surface = (E_slab − k·E_bulk_per_repeat_unit) / (2A),

where A = 19.547 Å², k = 1 for 3‑layer slabs and k = 2 for the 6‑layer slab, and E_bulk_per_repeat_unit is the energy of one repeating (110) bulk unit obtained from the bulk calculation. This formula corrects the original expression that did not account for the number of non‑identical atomic planes in the repeating unit. All calculated band gaps and surface energies are collected into a single JSON file (`/app/outputs/results.json`).

## Reproduction target
Produce the file `/app/outputs/results.json` with the direct band gaps (in eV) for bulk rutile and for the three (110) slabs of 3, 6, and 9 atomic layers (second‑plane termination). The file must also contain an array of surface formation energies (in J/m²) for all five slab models, together with the slab total energy (Ha), the bulk repeating unit energy used in the formula, and the value of k. The values must be computed from your own DFT runs; the surface energies should be physically reasonable (of order a few J/m²) and the relative stability of different terminations should emerge from the computed numbers.

## Assets

- Open-source DFT code supporting hybrid functionals (e.g., Quantum ESPRESSO or CP2K): https://www.quantum-espresso.org/
- Pseudopotentials for Ti and O (e.g., from SSSP or GBRV libraries): https://www.materialscloud.org/discover/sssp/
- Rutile TiO2 crystal structure (space group P4_2/mnm): 10.1007/BF0025023

## Workflow steps

### Step 1: Bulk geometry optimization
- Role: process
- Action: Perform full geometry optimization (lattice parameters and atomic positions) of bulk rutile TiO2 using DFT with a hybrid functional (e.g., B3LYP or equivalent).
- Evidence: `/app/outputs/bulk_opt.log`

### Step 2: Slab construction and optimization
- Role: process
- Action: From the optimized bulk, construct slab models for the (110) surface: (a) 3 atomic layers with surface termination on the second atomic plane; (b) 6 layers, second-plane termination; (c) 9 layers, second-plane termination; (d) 3 layers, termination on the first atomic plane; (e) 3 layers, termination on the third atomic plane. Set a vacuum layer of at least 15 Å. Optimize only the atomic positions of each slab while keeping the in-plane cell dimensions fixed. Record the optimized total energies.
- Evidence: `/app/outputs/slab_optimizations.log`

### Step 3: Electronic structure, band gaps, and surface formation energies
- Role: scored (load-bearing)
- Action: For the optimized bulk and for each of the five slabs, perform non-self-consistent band-structure calculations along high-symmetry paths (include Γ point) and determine the direct band gap at Γ. Extract the total energies of the bulk primitive cell and each slab. Compute the surface formation energy using the modified formula: E_surface = (E_slab − k × E_bulk_per_repeat_unit) / (2A), where A = 19.547 Å², k = 1 for the 3-layer slabs and k = 2 for the 6-layer slab, and E_bulk_per_repeat_unit is the energy per one (110) repeating bulk unit derived from the bulk calculation. Report all band gaps and surface energies in a single JSON file as specified.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"bulk_bandgap_eV": number, "slab3_t2_bandgap_eV": number, "slab6_t2_bandgap_eV": number, "slab9_t2_bandgap_eV": number, "surface_energies": [{"n_layers": int, "termination_layer": int, "k": int, "E_surface_Jpm2": float, "E_slab_Ha": float, "E_bulk_per_repeat_unit_Ha": float}]}
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
- description: JSON file containing all headline quantities: bulk and slab band gaps (Γ→Γ) and a table of surface formation energies computed with the modified formula.
- schema:
  - `type`: object
  - `required`:
    - `bulk_bandgap_eV`: number
    - `slab3_t2_bandgap_eV`: number
    - `slab6_t2_bandgap_eV`: number
    - `slab9_t2_bandgap_eV`: number
    - `surface_energies`: array
  - `items`:
    - `type`: object
    - `required`:
      - `n_layers`: integer
      - `termination_layer`: integer
      - `k`: integer
      - `E_surface_Jpm2`: number
      - `E_slab_Ha`: number
      - `E_bulk_per_repeat_unit_Ha`: number
  - `description`: Band gaps in eV; surface_energies array where each object has n_layers, termination_layer (1,2,3), k, E_surface_Jpm2, E_slab_Ha, and E_bulk_per_repeat_unit_Ha.

Notes: The checker uses reference_match policy: it compares the agent's values to the paper's reported band gaps and surface energies with domain-appropriate tolerances, and also checks the relative stability ordering (termination 2 < termination 1 and termination 2 < termination 3). Internal consistency (k=1 for 3‑layer, k=2 for 6‑layer) is also verified.

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
        "required": {
          "bulk_bandgap_eV": "number",
          "slab3_t2_bandgap_eV": "number",
          "slab6_t2_bandgap_eV": "number",
          "slab9_t2_bandgap_eV": "number",
          "surface_energies": "array"
        },
        "items": {
          "type": "object",
          "required": {
            "n_layers": "integer",
            "termination_layer": "integer",
            "k": "integer",
            "E_surface_Jpm2": "number",
            "E_slab_Ha": "number",
            "E_bulk_per_repeat_unit_Ha": "number"
          }
        },
        "description": "Band gaps in eV; surface_energies array where each object has n_layers, termination_layer (1,2,3), k, E_surface_Jpm2, E_slab_Ha, and E_bulk_per_repeat_unit_Ha."
      },
      "description": "JSON file containing all headline quantities: bulk and slab band gaps (Γ→Γ) and a table of surface formation energies computed with the modified formula."
    }
  ],
  "notes": "The checker uses reference_match policy: it compares the agent's values to the paper's reported band gaps and surface energies with domain-appropriate tolerances, and also checks the relative stability ordering (termination 2 < termination 1 and termination 2 < termination 3). Internal consistency (k=1 for 3‑layer, k=2 for 6‑layer) is also verified."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and independently assesses three aspects: (i) how close your band gaps are to the expected reference values (within domain‑appropriate tolerances), (ii) whether the surface energies show the correct stability ordering (the second‑plane termination lower than the first and third), and (iii) whether the surface energies obey internal consistency with the modified formula and have the right order of magnitude. Each aspect contributes a weighted fraction to a total reward between 0 and 1. Reporting values without performing the calculations will yield a low score because the checks evaluate both numerical closeness and structural consistency. The exact scoring weights and tolerances are hidden; only the final reward is returned.
