# Activation barriers for Cr migration into γ- and η-alumina bulk

## Problem background
Chromia (chromium oxide) supported on alumina is a widely used industrial catalyst for alkane dehydrogenation. Over time, however, the catalyst loses activity, and the lifetime depends strongly on which alumina polytype serves as the support: catalysts on γ-Al2O3 degrade within weeks, while those on η-Al2O3 can last for years. Experimental evidence suggests that deactivation is linked to chromium atoms leaving the reactive surface and migrating into the bulk support. Reaching a predictive understanding requires quantifying the energy barriers that control this migration for the two alumina polytypes, thereby explaining the large difference in catalyst durability.

## Approach
The problem is studied with first‑principles density‑functional theory (DFT) using the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation. Periodic slab models of the (110C) surfaces of γ‑Al2O3 and η‑Al2O3 are constructed from known bulk crystal structures, each with five atomic layers and a vacuum region to isolate the surface. A single chromium atom is placed at a surface trench site. Geometry relaxations are performed for the clean surfaces and for the Cr‑decorated slabs in both surface‑bound and subsurface octahedral interstitial configurations. The minimum energy pathway for Cr migration into the subsurface is then mapped with the climbing‑image nudged elastic band (CI‑NEB) method. From these calculations the activation barriers and the relative stability of the subsurface site are obtained.

## Reproduction target
Using DFT calculations with the PBE functional, produce three values:
(i) the activation barrier (eV) for a chromium atom to move from a surface trench site into a subsurface octahedral interstitial in γ‑Al2O3,
(ii) the analogous activation barrier for η‑Al2O3, and
(iii) the energy gain (eV) of the subsurface octahedral interstitial relative to the surface‑bound chromium for γ‑Al2O3 (positive if the subsurface site is more stable).
Report all three in a file `/app/outputs/results.json`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.quantum-espresso.org/pseudopotentials/
- Crystal structures of γ- and η-Al2O3: 10.1107/S0108768191002719

## Workflow steps

### Step 1: Build slab models of γ- and η-Al2O3 (110C) surfaces
- Role: process
- Action: Construct periodic slab supercells for γ-Al2O3(110C) and η-Al2O3(110C) surfaces, each with five atomic layers (70 atoms for γ, 72 atoms for η) and a 10 Å vacuum gap, using the bulk crystal structures. Generate the necessary DFT input files for geometry relaxations.
- Evidence: none

### Step 2: DFT geometry relaxations of clean and Cr-decorated slabs
- Role: process
- Action: Using Quantum ESPRESSO with GGA-PBE functional, plane-wave cutoff 24 Ry, and k-point sampling equivalent to 2×2×1, perform geometry relaxations for the clean slabs and for configurations with a Cr atom placed at a surface trench site and at a subsurface octahedral interstitial site, for both γ and η slabs. Save total energies and relaxed geometries.
- Evidence: `/app/outputs/cr_energies.json`

### Step 3: Compute activation barriers and energetic stability
- Role: scored (load-bearing)
- Action: Compute the minimum energy pathway for Cr migration from a surface trench site into a subsurface octahedral interstitial for γ-Al2O3 and η-Al2O3 using the NEB method. Determine the activation barriers. Also calculate the total energy difference between surface-bound Cr and subsurface Cr for γ-Al2O3. Write these three quantities to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: activation_barrier_gamma (float, eV), activation_barrier_eta (float, eV), subsurface_energy_gain_gamma (float, eV).
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
- description: Checker compares each reported energy to hidden paper-derived reference values within tolerances, and verifies activation_barrier_eta > activation_barrier_gamma (trend check).
- schema:
  - `type`: object
  - `required`: `activation_barrier_gamma`, `activation_barrier_eta`, `subsurface_energy_gain_gamma`
  - `properties`:
    - `activation_barrier_gamma`:
      - `type`: number
      - `units`: eV
    - `activation_barrier_eta`:
      - `type`: number
      - `units`: eV
    - `subsurface_energy_gain_gamma`:
      - `type`: number
      - `units`: eV

Notes: All values must be in eV. The trend check ensures the η-alumina barrier is higher than the γ-alumina barrier.

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
          "activation_barrier_gamma",
          "activation_barrier_eta",
          "subsurface_energy_gain_gamma"
        ],
        "properties": {
          "activation_barrier_gamma": {
            "type": "number",
            "units": "eV"
          },
          "activation_barrier_eta": {
            "type": "number",
            "units": "eV"
          },
          "subsurface_energy_gain_gamma": {
            "type": "number",
            "units": "eV"
          }
        }
      },
      "description": "Checker compares each reported energy to hidden paper-derived reference values within tolerances, and verifies activation_barrier_eta > activation_barrier_gamma (trend check)."
    }
  ],
  "notes": "All values must be in eV. The trend check ensures the η-alumina barrier is higher than the γ-alumina barrier."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json`. It compares each of the three quantities to reference values obtained from the literature, allowing tolerances that reflect the expected variation between different DFT implementations and computational settings. In addition, it verifies that the computed barrier for η‑Al2O3 is larger than the one for γ‑Al2O3. The final reward is a combination of the individual checks, with the barrier‑trend check carrying a fraction of the weight.
