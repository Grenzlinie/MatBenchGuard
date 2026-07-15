# DFT Activation Barriers and Formation Energies for Methane Oxidation on Graphene-Confined FeN4

## Problem background
Direct conversion of methane to value-added chemicals at low temperature is a major challenge in catalysis. Methane is exceptionally stable and its conversion typically requires high temperatures. Single-atom catalysts that operate at room temperature could offer a more efficient and sustainable route. Density functional theory (DFT) calculations are used to investigate the atomic-scale mechanism and to understand why certain transition metals are more active for this reaction.

## Approach
The computational model is a 5×5 graphene supercell containing a single metal atom coordinated by four nitrogen atoms (M–N4). The active site is formed by adsorbing two oxygen atoms, one on each side of the metal, creating an O–M–N4–O motif. All DFT calculations employ the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation, a plane-wave kinetic energy cutoff of 400 eV, and gamma‑centred k‑point sampling. Transition states for C–H bond cleavage of methane are located with the climbing-image nudged elastic band (CI-NEB) method, considering two mechanistic pathways: a radical hydrogen-abstraction pathway and a concerted hydroxylation pathway. The formation energy of the O–M–N4–O site is defined relative to the bare M–N4 slab and an isolated O2 molecule. By computing these quantities for Fe and for several other 3d metals (Cr, Mn, Fe, Co), one can examine the relative ordering of formation energies and their relationship to catalytic activity.

## Reproduction target
For the Fe–N4/graphene system, compute (a) the formation energy of the O–FeN4–O active site relative to FeN4 + O2, and (b) the activation energy barriers for the first C–H bond cleavage of methane via the radical and concerted mechanisms on O–FeN4–O. For the set of metals M = Cr, Mn, Fe, Co, compute (c) the formation energies of the corresponding O–M–N4–O sites. Report all computed energies and barriers in the specified JSON output files. The hidden verifier will assess the agreement of your computed values with the reference values and their relative ordering (e.g., which of the two mechanisms gives the lower barrier, and where Fe sits in the formation energy ordering across the four metals).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP efficiency library v1.2): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build and relax FeN4/graphene model
- Role: process
- Action: Construct a 5×5 graphene supercell containing a single Fe atom coordinated by four N atoms (FeN4) and perform geometry optimization using DFT (PBE, 400 eV cutoff, gamma‑centred k‑points).
- Evidence: `/app/outputs/feN4_optimized.xyz`

### Step 2: Compute O-FeN4-O formation energy and C–H activation barriers
- Role: scored (load-bearing)
- Action: Starting from the relaxed FeN4/graphene model, adsorb two oxygen atoms (one on each side of the Fe) to form the O–FeN4–O motif and optimize its geometry. Compute the formation energy E_form = E(O–FeN4–O) – E(FeN4) – E(O2). Using the climbing image nudged elastic band (CI-NEB) method, locate the transition states for the first C–H bond cleavage of methane via (i) a radical hydrogen-abstraction pathway and (ii) a concerted hydroxylation pathway; report the corresponding activation energy barriers (in eV) relative to the co‑adsorbed state of methane on O–FeN4–O.
- Output file: `/app/outputs/step_01_energy_barriers.json`
- Format: json
- Contract: { "radical_barrier_eV": float, "concerted_barrier_eV": float, "forming_energy_OFeN4O_eV": float }
- Scoring: scored by hidden verifier

### Step 3: Compute O-MN4-O formation energies for other metals
- Role: scored
- Action: For M = Cr, Mn, Fe, Co, construct analogous M–N4/graphene models, form the O–MN4–O motif (adsorb two O atoms), and compute the formation energy relative to MN4 + O2. For Fe, use the same methodology as in step 2 to obtain a consistent value.
- Output file: `/app/outputs/step_02_volcano_data.json`
- Format: json
- Contract: { "formation_energies": { "Cr": float, "Mn": float, "Fe": float, "Co": float } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_barriers.json`
- `/app/outputs/step_02_volcano_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_barriers.json
- path: `/app/outputs/step_01_energy_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Activation energy barriers for radical hydrogen‑abstraction and concerted hydroxylation on O–FeN4–O, and the formation energy of the O–FeN4–O site, compared to paper‑reported values with tolerance; ordering check (radical < concerted) is also applied.
- schema:
  - `type`: object
  - `required`:
    - `radical_barrier_eV`: float
    - `concerted_barrier_eV`: float
    - `forming_energy_OFeN4O_eV`: float

### step_02_volcano_data.json
- path: `/app/outputs/step_02_volcano_data.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of O–MN4–O for Cr, Mn, Fe, Co; the hidden checker verifies that Fe has an intermediate formation energy (volcano optimum) among them.
- schema:
  - `type`: object
  - `required`:
    - `formation_energies`:
      - `Cr`: float
      - `Mn`: float
      - `Fe`: float
      - `Co`: float

Notes: All DFT calculations are performed with the open‑source Quantum ESPRESSO code and the SSSP PBE pseudopotentials. The CI‑NEB barriers and formation energies are compared to the paper’s values within physically motivated tolerances; the volcano check enforces the relative ordering of formation energies without requiring absolute agreement with a specific reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "radical_barrier_eV": "float",
          "concerted_barrier_eV": "float",
          "forming_energy_OFeN4O_eV": "float"
        }
      },
      "description": "Activation energy barriers for radical hydrogen‑abstraction and concerted hydroxylation on O–FeN4–O, and the formation energy of the O–FeN4–O site, compared to paper‑reported values with tolerance; ordering check (radical < concerted) is also applied."
    },
    {
      "file": "step_02_volcano_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "formation_energies": {
            "Cr": "float",
            "Mn": "float",
            "Fe": "float",
            "Co": "float"
          }
        }
      },
      "description": "Formation energies of O–MN4–O for Cr, Mn, Fe, Co; the hidden checker verifies that Fe has an intermediate formation energy (volcano optimum) among them."
    }
  ],
  "notes": "All DFT calculations are performed with the open‑source Quantum ESPRESSO code and the SSSP PBE pseudopotentials. The CI‑NEB barriers and formation energies are compared to the paper’s values within physically motivated tolerances; the volcano check enforces the relative ordering of formation energies without requiring absolute agreement with a specific reference."
}
```

## How you are scored
Each scored step produces a JSON output file that is read by a hidden verifier after the run. The verifier extracts the reported scalar values, compares them to hidden reference values, and checks the required relative ordering of the barriers and formation energies. The checks use prescribed tolerances appropriate to the computational method. The final reward is a weighted combination of the individual step scores; the sum of the weights is approximately 1. The verifier does not re-run any DFT calculations; your reward depends solely on the contents of the files you write under `/app/outputs`.
