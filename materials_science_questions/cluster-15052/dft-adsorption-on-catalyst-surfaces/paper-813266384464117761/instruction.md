# DFT Adsorption and Dissociation of O2 on Graphene and N-Doped Graphene

## Problem background
Graphene and nitrogen-doped graphene are investigated as possible catalysts for the oxygen reduction reaction in Li-air batteries. Understanding how molecular O2 physically adsorbs, how atomic O chemically binds, and how O2 dissociates on these surfaces is essential for evaluating their catalytic activity. This task reproduces the computational modeling of these processes.

## Approach
The adsorption and dissociation processes are modeled with first-principles density functional theory (DFT) using the generalized gradient approximation (GGA) with the PW91 exchange-correlation functional. A 4×4 graphene supercell (32 C atoms) and a single-N-substituted analog (replacing one C with N) are constructed, each with a 15 Å vacuum layer. The workflow includes: (i) relaxing isolated O2 and O atom reference energies, (ii) searching for the most stable O2 physisorbed geometry on each surface, (iii) identifying the most stable single O atom chemisorption sites and computing their adsorption energies, and (iv) determining the O2 dissociation pathways and energy barriers via climbing-image nudged elastic band (CI-NEB) calculations. All energy comparisons are performed consistently with the same DFT settings, and the results for pristine and N-doped graphene are contrasted to assess the effect of nitrogen doping.

## Reproduction target
For both pristine and single-N-substituted graphene, compute and report: (1) the O2 physisorption geometry (vertical adsorption heights and O–O bond length) and the corresponding adsorption energy, (2) the preferred single O atom chemisorption site, its adsorption energy, and the associated C–O bond length(s), and (3) the O2 dissociation energy barrier. All reported quantities must be self-consistently derived from the DFT production steps described in the workflow.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotential Library (PW91): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax pristine and N-doped graphene slabs
- Role: process
- Action: Build a 4×4 graphene unit cell (32 C atoms) and a single-N-substituted unit cell, both with 15 Å vacuum along z. Perform DFT relaxation using the GGA-PW91 exchange-correlation functional and appropriate pseudopotentials. Relax atomic positions until forces are below 0.05 eV/Å. Save relaxed coordinates and total energies for use in subsequent adsorption energy calculations.
- Evidence: `/app/outputs/slab_relaxation.log`

### Step 2: Reference energies of free O2 and O atom
- Role: process
- Action: Compute the total energy of an isolated O2 molecule and an isolated O atom in a vacuum box using the same DFT settings (PW91, cutoff, k-point sampling). Save these reference energies for later evaluation of adsorption energies.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: O2 physisorption on pristine and N-doped graphene
- Role: scored
- Action: Place an O2 molecule in multiple initial orientations (parallel and perpendicular) on the relaxed pristine graphene slab and on the relaxed N-doped graphene slab. Relax each combined system to find the equilibrium adsorption geometry. For each surface, calculate the adsorption energy using E_ad = -½[E(slab+O2) - E(slab) - E(O2)]. Output the adsorption energy, the vertical adsorption height(s) (distance from graphene plane to nearest O atom), and the O–O bond length in the adsorbed state.
- Output file: `/app/outputs/physisorption_results.json`
- Format: json
- Contract: {"pristine": {"adsorption_energy_eV": float, "o2_vertical_height_A": float, "o_o_bond_length_A": float}, "n_doped": {"adsorption_energy_eV": float, "o1_vertical_height_A": float, "o2_vertical_height_A": float, "o_o_bond_length_A": float}}
- Scoring: scored by hidden verifier

### Step 4: Single O atom chemisorption on both surfaces
- Role: scored
- Action: Test O atom adsorption at candidate high-symmetry sites: on pristine graphene at bridge and top sites; on N-doped graphene at top, bridge, and edge sites near the N dopant. For each surface, identify the most stable site by comparing total energies. Compute the adsorption energy using E_ad = -[E(slab+O) - E(slab) - E(O)]. Report the site designation, adsorption energy, and the relevant C–O bond length(s) for the most stable configuration on each surface.
- Output file: `/app/outputs/chemisorption_results.json`
- Format: json
- Contract: {"pristine": {"site": "bridge", "adsorption_energy_eV": float, "c_o_bond_lengths_A": [float, float]}, "n_doped": {"site": "top", "adsorption_energy_eV": float, "c_o_bond_length_A": float}}
- Scoring: scored by hidden verifier

### Step 5: O2 dissociation barriers on pristine and N-doped graphene
- Role: scored (load-bearing)
- Action: From the physisorbed O2 initial state (step 3) and a searched final state of two chemisorbed O atoms at the most stable sites (based on step 4 results and additional two-O configuration sampling), compute the minimum energy path for O2 dissociation on each surface using the climbing-image nudged elastic band (CI-NEB) method. Report the dissociation energy barrier for pristine graphene and for N-doped graphene.
- Output file: `/app/outputs/dissociation_results.json`
- Format: json
- Contract: {"pristine": {"energy_barrier_eV": float}, "n_doped": {"energy_barrier_eV": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/physisorption_results.json`
- `/app/outputs/chemisorption_results.json`
- `/app/outputs/dissociation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### physisorption_results.json
- path: `/app/outputs/physisorption_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: O2 physisorption geometries and adsorption energies on pristine and N-doped graphene.
- schema:
  - `type`: object
  - `required`:
    - `pristine.adsorption_energy_eV`: number (eV)
    - `pristine.o2_vertical_height_A`: number (Å)
    - `pristine.o_o_bond_length_A`: number (Å)
    - `n_doped.adsorption_energy_eV`: number (eV)
    - `n_doped.o1_vertical_height_A`: number (Å)
    - `n_doped.o2_vertical_height_A`: number (Å)
    - `n_doped.o_o_bond_length_A`: number (Å)

### chemisorption_results.json
- path: `/app/outputs/chemisorption_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single O atom chemisorption site, energy, and bond lengths on pristine and N-doped graphene.
- schema:
  - `type`: object
  - `required`:
    - `pristine.site`: string (e.g., 'bridge')
    - `pristine.adsorption_energy_eV`: number (eV)
    - `pristine.c_o_bond_lengths_A`: array of two numbers (Å)
    - `n_doped.site`: string (e.g., 'top')
    - `n_doped.adsorption_energy_eV`: number (eV)
    - `n_doped.c_o_bond_length_A`: number (Å)

### dissociation_results.json
- path: `/app/outputs/dissociation_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: O2 dissociation energy barriers on pristine and N-doped graphene.
- schema:
  - `type`: object
  - `required`:
    - `pristine.energy_barrier_eV`: number (eV)
    - `n_doped.energy_barrier_eV`: number (eV)

Notes: Quantities are compared to hidden reference values within tolerances. Trends (N-doped adsorption energy > pristine, N-doped dissociation barrier < pristine) are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "physisorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine.adsorption_energy_eV": "number (eV)",
          "pristine.o2_vertical_height_A": "number (Å)",
          "pristine.o_o_bond_length_A": "number (Å)",
          "n_doped.adsorption_energy_eV": "number (eV)",
          "n_doped.o1_vertical_height_A": "number (Å)",
          "n_doped.o2_vertical_height_A": "number (Å)",
          "n_doped.o_o_bond_length_A": "number (Å)"
        }
      },
      "description": "O2 physisorption geometries and adsorption energies on pristine and N-doped graphene."
    },
    {
      "file": "chemisorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine.site": "string (e.g., 'bridge')",
          "pristine.adsorption_energy_eV": "number (eV)",
          "pristine.c_o_bond_lengths_A": "array of two numbers (Å)",
          "n_doped.site": "string (e.g., 'top')",
          "n_doped.adsorption_energy_eV": "number (eV)",
          "n_doped.c_o_bond_length_A": "number (Å)"
        }
      },
      "description": "Single O atom chemisorption site, energy, and bond lengths on pristine and N-doped graphene."
    },
    {
      "file": "dissociation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine.energy_barrier_eV": "number (eV)",
          "n_doped.energy_barrier_eV": "number (eV)"
        }
      },
      "description": "O2 dissociation energy barriers on pristine and N-doped graphene."
    }
  ],
  "notes": "Quantities are compared to hidden reference values within tolerances. Trends (N-doped adsorption energy > pristine, N-doped dissociation barrier < pristine) are also verified."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored output files (physisorption_results.json, chemisorption_results.json, and dissociation_results.json). Each file is checked against reference values for the requested quantities and for the expected relative trend between pristine and N-doped surfaces. The per-stage scores are weighted and combined into a final reward in [0,1]. Simply reporting a number is not sufficient; the submitted artifacts must pass structural validation and the quantitative comparisons imposed by the verifier.
