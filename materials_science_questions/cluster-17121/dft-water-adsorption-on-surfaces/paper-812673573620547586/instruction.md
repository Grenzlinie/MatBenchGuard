# Water Binding Energies on Cation-Exchanged Vermiculite Surfaces

## Problem background
The wetting properties of vermiculite laminates can be tuned by exchanging the interlayer cations. Understanding the atomic-scale water binding on different cation-exchanged surfaces is essential for explaining this tunability. This task reproduces the computational investigation of water binding on two representative cation-exchanged vermiculite surfaces, Li-vermiculite (LiV) and K-vermiculite (KV).

## Approach
The study uses density functional theory (DFT) and ab initio molecular dynamics (AIMD) simulations. Atomic models of the LiV and KV surfaces are built with the appropriate cation placements and a realistic level of Si→Al substitution. After DFT geometry optimizations of the bare surfaces, thin films of water are simulated on each surface via AIMD at room temperature. From the equilibrated trajectories, the water molecules in the first and second contact layers are identified using probability density profiles along the surface normal. For each system and each contact layer, binding energies are then computed by performing DFT geometry optimizations on selected snapshots. The final output is the average binding energy per water molecule for each of the four conditions.

## Reproduction target
Compute the average water binding energy per water molecule (in eV) for the first and second contact layers on Li-vermiculite and K-vermiculite surfaces using the DFT and AIMD protocol outlined in the workflow steps. Write the results to `/app/outputs/binding_energies.json` with the keys `LiV_first`, `LiV_second`, `KV_first`, `KV_second`.

## Assets

- Vermiculite crystal structure
- CP2K: https://www.cp2k.org/

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Construct atomic models of LiV and KV vermiculite surfaces: a 2×1 supercell with 25% Si→Al substitution and charge-compensating cations (Li⁺ or K⁺) placed on the surface.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization of the bare vermiculite surfaces (unit cell volume and ionic positions) using CP2K with the PBE-D3 functional, Goedecker-Teter-Hutter pseudopotentials, and DZVP basis set.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 3: AIMD simulation of water films
- Role: process
- Action: Run AIMD simulations of 40 D₂O molecules on each optimized LiV and KV surface at 300 K in the NVT ensemble for at least 35 ps (K) and 40 ps (Li) with a 0.5 fs timestep. Equilibrate for 5 ps before collecting statistics. Save trajectories.
- Evidence: `/app/outputs/trajectories.xyz`

### Step 4: Contact layer identification
- Role: process
- Action: From the AIMD trajectories, compute probability density profiles of water oxygen and hydrogen atoms along the surface normal. Identify the water molecules residing in the first and second contact layers based on the peaks in the density profiles.
- Evidence: `/app/outputs/density_profiles.png`

### Step 5: Binding energy calculation and scoring
- Role: scored (load-bearing)
- Action: For each system (LiV, KV) and each contact layer (first, second), select 10 independent snapshots from the AIMD trajectory that contain water molecules in that layer. For each snapshot, perform a DFT geometry optimization and compute the binding energy per water molecule as E_b = E_tot - (N_wat * E_wat + E_surf). Average the binding energies across snapshots. Write the four averages to /app/outputs/binding_energies.json with keys 'LiV_first', 'LiV_second', 'KV_first', 'KV_second'.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"type":"object","properties":{"LiV_first":{"type":"number"},"LiV_second":{"type":"number"},"KV_first":{"type":"number"},"KV_second":{"type":"number"}},"required":["LiV_first","LiV_second","KV_first","KV_second"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Average water binding energy per water molecule (in eV) for the first and second contact layers of Li-vermiculite and K-vermiculite surfaces, computed from DFT geometry optimizations on snapshots from AIMD simulations.
- schema:
  - `type`: object
  - `required`: `LiV_first`, `LiV_second`, `KV_first`, `KV_second`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `LiV_first`: eV/H2O
    - `LiV_second`: eV/H2O
    - `KV_first`: eV/H2O
    - `KV_second`: eV/H2O

Notes: Binding energies are used to explain the observed difference in hydrophilicity between LiV and KV. The values are to be compared against the paper-reported values within hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "LiV_first",
          "LiV_second",
          "KV_first",
          "KV_second"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "LiV_first": "eV/H2O",
          "LiV_second": "eV/H2O",
          "KV_first": "eV/H2O",
          "KV_second": "eV/H2O"
        }
      },
      "description": "Average water binding energy per water molecule (in eV) for the first and second contact layers of Li-vermiculite and K-vermiculite surfaces, computed from DFT geometry optimizations on snapshots from AIMD simulations."
    }
  ],
  "notes": "Binding energies are used to explain the observed difference in hydrophilicity between LiV and KV. The values are to be compared against the paper-reported values within hidden tolerances."
}
```

## How you are scored
A hidden verifier will read your `binding_energies.json` and compare each of the four reported binding energies to reference values. Your final reward is the fraction of energies that fall within a hidden tolerance. Simply reporting plausible numbers without faithfully executing the required DFT and AIMD steps will not produce results that match the hidden reference values.
