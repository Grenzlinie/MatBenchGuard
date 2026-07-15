# DFT Energetics of AlCl Disproportionation on Al(110) Surface

## Problem background
The disproportionation reaction 3AlCl(g) → 2Al(s) + AlCl₃(g) on aluminum surfaces is a key step in a carbothermic reduction and chlorination process for aluminum production. Understanding the reaction mechanism and energetics on the Al(110) surface is essential for controlling the process. This task investigates three possible surface reaction mechanisms (A, B, C) using plane-wave density functional theory (DFT). The main question is the thermodynamic favorability of these pathways, determined by computing adsorption/desorption energies, elementary step reaction energies, and the resulting overall reaction energies for each mechanism.

## Approach
The computational approach employs periodic plane-wave DFT with the GGA-PBE exchange-correlation functional and ultrasoft pseudopotentials. An Al(110) surface is modeled with a six-layer p(6×3) slab and a vacuum gap. The workflow consists of: (i) optimizing the clean slab and isolated AlCl and AlCl₃ molecules; (ii) optimizing a comprehensive set of surface + adsorbate configurations that represent all reactant, product, and co-adsorbate states appearing in the elementary steps of mechanisms A, B, and C; (iii) computing adsorption and desorption energies from total-energy differences; (iv) evaluating reaction energies for each elementary surface step; and (v) combining these into surface-only and general reaction energies for the three mechanisms. This protocol yields a set of quantitative energetic comparisons that identify the preferred reaction path.

## Reproduction target
Produce three scored artifacts that together characterize the energetics of AlCl disproportionation on Al(110):
1. **ads_des_energies.json** – the adsorption energy of AlCl and the desorption energies of AlCl and AlCl₃.
2. **reaction_energies.csv** – the reaction energy for each elementary surface step (A2–A4, B2–B3, C2–C3 defined in the workflow steps).
3. **general_energies.json** – the surface-only reaction energy and the general reaction energy for mechanisms A, B, and C.
All energies are reported in eV. The combination of these numbers allows a direct comparison of the three mechanisms without requiring any external data.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python 3: python3

## Workflow steps

### Step 1: Build and optimize clean Al(110) slab
- Role: process
- Action: Construct a periodic Al(110) surface slab model with a p(6×3) surface unit cell, 6 atomic layers, and a vacuum gap of at least 10 Å. Perform a variable-cell relaxation (ions + cell) using DFT (GGA-PBE, ultrasoft pseudopotentials) to obtain the optimized clean surface geometry and its total energy.
- Evidence: `/app/outputs/slab_log.txt`

### Step 2: Optimize gas-phase AlCl and AlCl3 molecules
- Role: process
- Action: Isolate a single AlCl molecule and a single AlCl3 molecule in large supercells (same cell dimensions as the slab, keeping vacuum) and relax their atomic positions with the same DFT settings. Obtain their optimized total energies.
- Evidence: `/app/outputs/gas_phase_energies.txt`

### Step 3: Optimize all required adsorbed configurations
- Role: process
- Action: Place each adsorbate (AlCl, Cl, AlCl2, AlCl3, Al) on the optimized Al(110) slab in the specific co-adsorption arrangements described in the paper (AlCl at fourfold hollow; AlCl+Cl; AlCl2+Cl; AlCl2 at fourfold hollow; AlCl3 at bridge; AlCl+AlCl; AlCl+AlCl2; AlCl2+AlCl2; and product configurations such as Al+Cl, AlCl2, AlCl3, AlCl2+Al, AlCl3+Al, AlCl3+AlCl). For each system, perform a full geometry optimization (ions only, keeping slab bottom layers fixed if desired) using the same DFT settings. Record the total energy of each optimized system.
- Evidence: `/app/outputs/adsorbate_energies.json`

### Step 4: Compute adsorption and desorption energies
- Role: scored (load-bearing)
- Action: Using the total energies from the clean slab, gas-phase molecules, and adsorbate configurations, calculate the adsorption energy of AlCl on Al(110) as E_ads(AlCl) = E(slab+AlCl) - E(slab) - E(AlCl); the desorption energy of AlCl as E_des(AlCl) = -E_ads(AlCl); and the desorption energy of AlCl3 as E_des(AlCl3) = E(slab) + E(AlCl3) - E(slab+AlCl3). Write the computed values to ads_des_energies.json.
- Output file: `/app/outputs/ads_des_energies.json`
- Format: json
- Contract: {"E_ads_AlCl": <float>, "E_des_AlCl": <float>, "E_des_AlCl3": <float>}
- Scoring: scored by hidden verifier

### Step 5: Compute elementary reaction energies
- Role: scored (load-bearing)
- Action: For each elementary surface reaction step (A2: AlCl(∗) → Al(∗)+Cl(∗); A3: AlCl(∗)+Cl(∗) → AlCl2(∗); A4: AlCl2(∗)+Cl(∗) → AlCl3(∗); B2: 2AlCl(∗) → AlCl2(∗)+Al(∗); B3: AlCl2(∗)+AlCl(∗) → AlCl3(∗)+Al(∗); C2: 2AlCl(∗) → AlCl2(∗)+Al(∗); C3: 2AlCl2(∗) → AlCl(∗)+AlCl3(∗)), compute the reaction energy as E(products) − E(reactants) using the total energies of the optimized reactant and product adsorbate configurations. Write the results to reaction_energies.csv with columns step_id and reaction_energy (eV).
- Output file: `/app/outputs/reaction_energies.csv`
- Format: csv
- Contract: Columns: step_id (string), reaction_energy (float).
- Scoring: scored by hidden verifier

### Step 6: Compile mechanism-level energetics
- Role: scored (load-bearing)
- Action: For each mechanism A, B, C, sum the surface-only reaction energies using the step energies from the elementary steps. Then add the adsorption contributions (three times E_ads(AlCl) for A and B; four times for C) and the desorption contributions (once for AlCl3 in all three, and once for AlCl in mechanism C). Obtain the surface-only reaction energy and the general reaction energy for each mechanism. Write the results to general_energies.json.
- Output file: `/app/outputs/general_energies.json`
- Format: json
- Contract: {"mechanism_A": {"surface_only_energy": <float>, "general_energy": <float>}, "mechanism_B": {"surface_only_energy": <float>, "general_energy": <float>}, "mechanism_C": {"surface_only_energy": <float>, "general_energy": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ads_des_energies.json`
- `/app/outputs/reaction_energies.csv`
- `/app/outputs/general_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ads_des_energies.json
- path: `/app/outputs/ads_des_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adsorption and desorption energies of AlCl and AlCl3 on Al(110) computed from DFT total energies.
- schema:
  - `type`: object
  - `required`:
    - `E_ads_AlCl`: float (eV)
    - `E_des_AlCl`: float (eV)
    - `E_des_AlCl3`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `E_ads_AlCl`: eV
    - `E_des_AlCl`: eV
    - `E_des_AlCl3`: eV

### reaction_energies.csv
- path: `/app/outputs/reaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elementary reaction energies and forward activation energies for steps A2‑A4, B2‑B3, C2‑C3 computed from DFT total energies.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `step_id`, `reaction_energy`, `activation_energy`
  - `units`:
    - `reaction_energy`: eV
    - `activation_energy`: eV

### general_energies.json
- path: `/app/outputs/general_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Surface-only and general reaction energies for mechanisms A, B, C of 3AlCl(g) → 2Al(∗) + AlCl3(g) on Al(110).
- schema:
  - `type`: object
  - `required`:
    - `mechanism_A`: object with surface_only_energy (float) and general_energy (float)
    - `mechanism_B`: object with surface_only_energy (float) and general_energy (float)
    - `mechanism_C`: object with surface_only_energy (float) and general_energy (float)
  - `items`:
    - `surface_only_energy`: float (eV)
    - `general_energy`: float (eV)
  - `required_columns`:
  - `units`:
    - `surface_only_energy`: eV
    - `general_energy`: eV

Notes: All energies are reported in eV. The checker compares against reference values with tolerances accounting for toolchain differences (open-source DFT code vs. proprietary CASTEP). Activation energies are forward barriers (E_a) from Table II.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ads_des_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "E_ads_AlCl": "float (eV)",
          "E_des_AlCl": "float (eV)",
          "E_des_AlCl3": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "E_ads_AlCl": "eV",
          "E_des_AlCl": "eV",
          "E_des_AlCl3": "eV"
        }
      },
      "description": "Adsorption and desorption energies of AlCl and AlCl3 on Al(110) computed from DFT total energies."
    },
    {
      "file": "reaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "step_id",
          "reaction_energy",
          "activation_energy"
        ],
        "units": {
          "reaction_energy": "eV",
          "activation_energy": "eV"
        }
      },
      "description": "Elementary reaction energies and forward activation energies for steps A2‑A4, B2‑B3, C2‑C3 computed from DFT total energies."
    },
    {
      "file": "general_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "mechanism_A": "object with surface_only_energy (float) and general_energy (float)",
          "mechanism_B": "object with surface_only_energy (float) and general_energy (float)",
          "mechanism_C": "object with surface_only_energy (float) and general_energy (float)"
        },
        "items": {
          "surface_only_energy": "float (eV)",
          "general_energy": "float (eV)"
        },
        "required_columns": [],
        "units": {
          "surface_only_energy": "eV",
          "general_energy": "eV"
        }
      },
      "description": "Surface-only and general reaction energies for mechanisms A, B, C of 3AlCl(g) → 2Al(∗) + AlCl3(g) on Al(110)."
    }
  ],
  "notes": "All energies are reported in eV. The checker compares against reference values with tolerances accounting for toolchain differences (open-source DFT code vs. proprietary CASTEP). Activation energies are forward barriers (E_a) from Table II."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact. It compares your reported energies to reference values that represent the correct physical result, using tolerances that account for the use of an open-source DFT code and different pseudopotentials. The verifier also checks the relative energetic ordering of the three mechanisms as a structural consistency requirement. Each artifact carries a portion of the total reward; all three must be produced for full credit. Merely reporting numbers is not enough—the energies must be physically consistent with an honest reproduction of the DFT workflow.
