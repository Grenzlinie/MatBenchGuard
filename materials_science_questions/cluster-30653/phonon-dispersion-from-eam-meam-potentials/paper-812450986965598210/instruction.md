# Temperature-dependent Pd penetration during deposition on Cu(110) using EAM molecular dynamics

## Problem background
When metal atoms are deposited onto a crystalline substrate, their incorporation into the top layers can depend strongly on the substrate temperature. Understanding how penetration varies with temperature is important for controlling epitaxial growth and surface dynamics. This task uses molecular dynamics to study the deposition of Pd atoms onto a Cu(110) surface. The goal is to simulate the process at several temperatures and compute the number of Pd atoms that end up below the first Cu layer after a defined simulation time. The question is how this penetration count changes with temperature.

## Approach
We employ the embedded‑atom method (EAM) potential for Cu‑Pd from Foiles et al. (1986), which describes the many‑body interactions in the metallic system. The simulations are performed with the open‑source LAMMPS code. An atomistic model is built: a thin Cu(110) slab (9 layers) is placed in a periodic cell with a long vacuum gap. 100 Pd atoms are initially placed in the vapour region above the surface; no bottom‑layer atoms are fixed. The initial vapour phase is equilibrated at high temperature while the Cu slab is frozen, then all atoms are released for production runs. Production simulations of 15 ps are run at four temperatures: 300 K, 600 K, 900 K and 1200 K, using a Verlet integrator with a 3 fs timestep. From the final atomic positions at each temperature, the number of Pd atoms whose z‑coordinate lies below the topmost Cu layer is counted. These counts across temperatures will be used to evaluate the temperature dependence of Pd penetration.

## Reproduction target
Your task is to produce a CSV file `penetration_counts.csv` with columns `temperature_K` (the simulation temperature in Kelvin) and `penetration_count` (the number of Pd atoms below the first Cu layer after 15 ps). The file must contain exactly four rows, one for each temperature: 300, 600, 900, and 1200 K. The verifier will examine the computed counts and their relationship across the four temperatures to assess the temperature dependence.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- EAM potential for Cu and Pd (Foiles et al. 1986): https://www.ctcms.nist.gov/potentials/Cu.html

## Workflow steps

### Step 1: Build simulation cell
- Role: process
- Action: Construct a simulation cell with lattice parameters a=21.6880 Å, b=20.4480 Å, c=50.0 Å (c perpendicular to the surface). Place 432 Cu atoms in a 9-layer (110) slab and 100 Pd atoms in a vapor region above the slab. Use three-dimensional periodic boundary conditions and do not fix any bottom-layer atoms.
- Evidence: `/app/outputs/initial_config.data`

### Step 2: Equilibrate vapour phase
- Role: process
- Action: Perform a short high-temperature MD run while fixing all Cu slab atoms, to create a disordered initial vapour phase. Then unfreeze all atoms for the production runs.
- Evidence: `/app/outputs/equilibration.log`

### Step 3: Run deposition simulations at four temperatures
- Role: process
- Action: For each of the four temperatures 300 K, 600 K, 900 K, and 1200 K, run a 15 ps MD simulation with a 3 fs timestep, Verlet integrator, and the EAM potential, using the unconstrained slab. Save the final atomic positions for each temperature.
- Evidence: `/app/outputs/final_positions.xyz`

### Step 4: Compute penetration counts and write CSV
- Role: scored (load-bearing)
- Action: For each temperature, identify the topmost Cu layer and count the number of Pd atoms whose z-coordinate is below that layer. Write the four pairs (temperature, count) to penetration_counts.csv.
- Output file: `/app/outputs/penetration_counts.csv`
- Format: csv
- Contract: temperature_K,penetration_count
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/penetration_counts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### penetration_counts.csv
- path: `/app/outputs/penetration_counts.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Penetration counts of Pd atoms below the first Cu layer for temperatures 300 K, 600 K, 900 K, and 1200 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `penetration_count`
  - `items`:
    - `temperature_K`: integer
    - `penetration_count`: integer

Notes: The scoring is based on the pattern of counts across the four temperatures. No hidden gold on the exact number of penetrating atoms is imposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "penetration_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "penetration_count"
        ],
        "items": {
          "temperature_K": "integer",
          "penetration_count": "integer"
        }
      },
      "description": "Penetration counts of Pd atoms below the first Cu layer for temperatures 300 K, 600 K, 900 K, and 1200 K."
    }
  ],
  "notes": "The scoring is based on the pattern of counts across the four temperatures. No hidden gold on the exact number of penetrating atoms is imposed."
}
```

## How you are scored
A hidden verifier will read your `penetration_counts.csv` and compare the values (and the pattern they form across the four temperatures) against a reference expectation. Your reward is based on how closely your computed counts match the expected temperature dependence. Simply writing numbers without running the simulations will not satisfy the verifier. The scoring is fully automatic and does not require you to match any particular published value exactly — only to reproduce the underlying physical trend.
