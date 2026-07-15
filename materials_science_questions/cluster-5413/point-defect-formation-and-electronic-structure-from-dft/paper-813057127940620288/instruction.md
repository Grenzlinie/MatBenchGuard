# Oxygen Vacancy Clustering and Migration in CeO2: First-Principles Study

## Problem background
CeO₂ is a widely studied oxide for catalysis and solid‑oxide fuel cells because its oxygen storage capacity (the ability to easily form and heal oxygen vacancies) largely determines device performance. When oxygen atoms are removed from the lattice, the resulting vacancies can either remain isolated or cluster together. Vacancy clustering is expected to influence ionic conductivity, but the detailed formation, stability, and migration properties of clustered vacancies in pure CeO₂ are not fully understood. This task investigates the thermodynamic stability and kinetic mobility of oxygen vacancy clusters in bulk CeO₂ through first‑principles calculations, aiming to clarify how vacancy–vacancy interactions and the local environment affect oxygen‑ion transport.

## Approach
Use an open‑source DFT code (e.g., Quantum ESPRESSO, CP2K, or GPAW) together with the Atomic Simulation Environment (ASE) for structure manipulation and trajectory analysis. Start from the fluorite CeO₂ primitive cell, validate the chosen exchange‑correlation functional against known bulk properties (lattice constant, band gaps, formation energy of CeO₂). Build 2×2×2 and 3×3×3 supercells to host different vacancy defects. Create five short‑range vacancy‑pair configurations (<100>, <110>, <111>, <100>_e, <111>_e), as well as structures containing a single oxygen vacancy and a <111>‑oriented vacancy pair cluster. For each structure, perform geometry optimisation and compute total energies. Then evaluate defect formation energies in O‑rich and O‑poor limits, taking into account charge states and the position of the Fermi level. Use the climbing‑image nudged elastic band (cNEB) method to calculate minimum energy barriers for a single oxygen vacancy and for the <111> cluster along several crystallographic directions. Perform ab initio molecular dynamics (AIMD) at 1000 K on 3×3×3 supercells with either a single vacancy or the <111> cluster, and analyse the oxygen trajectories to quantify diffusive jumps. Finally, probe the influence of localised Ce³⁺ ions (polarons) on the migration barrier of a single vacancy by placing 0, 1, or 2 Ce³⁺ near the migration path and recomputing the NEB barrier.

## Reproduction target
Produce four scored JSON artifacts under `/app/outputs`:
1. `formation_energies.json` – formation energies of a single oxygen vacancy and the <111> vacancy cluster in different charge states, and the relative total energies of the five short‑range vacancy‑pair configurations, from which the most stable configuration can be identified.
2. `migration_barriers.json` – NEB migration barriers for a single oxygen vacancy and for the <111> cluster along the <100>, <110>, and <111> directions (multiple paths where applicable).
3. `aimd_analysis.json` – analysis of the AIMD production runs (total time, number of vacancy jumps, and a description of the jump pattern) for both the single‑vacancy system and the <111>‑cluster system.
4. `ce3_migration_barriers.json` – barriers for a single vacancy when 0, 1, or 2 Ce³⁺ ions are placed near the migration path.

From these artifacts, the main trends of interest are: the relative stability ordering among the vacancy‑pair configurations, the formation‑energy sign of the <111> cluster under O‑poor conditions, the ratio of cluster‑to‑single‑vacancy migration barriers, the qualitative diffusive behaviour (frequent jumps vs. vibration), and the effect of Ce³⁺ count on the migration barrier.

## Assets

- Quantum ESPRESSO (or CP2K/GPAW): https://www.quantum-espresso.org/
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Validate DFT setup
- Role: process
- Action: Perform a DFT calculation on the primitive CeO2 cell using the chosen functional (e.g., HSE or PBE+U). Compute lattice constant, O2p-Ce4f and O2p-Ce5d band gaps, and formation energy of CeO2. Confirm reasonable agreement with experimental values to ensure the settings are appropriate.
- Evidence: `/app/outputs/validation_output.json`

### Step 2: Prepare supercells and vacancy configurations
- Role: process
- Action: Build 2×2×2 and 3×3×3 CeO2 supercells from the primitive cell. Create the five short-range vacancy pair configurations (<100>, <110>, <111>, <100>_e, <111>_e) in the 2×2×2 supercell, and single-vacancy and <111> cluster structures in the 3×3×3 supercell.
- Evidence: `/app/outputs/supercell_structures.json`

### Step 3: Compute formation energies and relative stability
- Role: scored (load-bearing)
- Action: Optimise the geometry of each vacancy-pair configuration and calculate total energies. Evaluate formation energies using the standard defect formation energy formula for O-rich and O-poor limits. Determine charge-state transition levels for single vacancy and <111> cluster. Record relative total energies of the five configurations to identify the most stable one.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON object with keys 'single_vacancy' (dict of charge states to formation energies in eV), 'cluster_vacancy' (similar), 'relative_stability' (dict mapping configuration name to relative total energy in eV).
- Scoring: scored by hidden verifier

### Step 4: Compute migration barriers for single and clustered vacancies
- Role: scored
- Action: Using the climbing-image nudged elastic band (cNEB) method, compute migration barriers for a single oxygen vacancy along <100>, <110>, <111> directions and for the <111> vacancy cluster along <100> (paths A–D), <110> and <111> directions. Record barrier values for every examined path.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: JSON object with keys 'single_vacancy' and 'cluster_vacancy', each being an object mapping a direction string (e.g., '<100>') to an array of barrier values in eV (one per path).
- Scoring: scored by hidden verifier

### Step 5: Run AIMD simulations of vacancy diffusion
- Role: scored
- Action: Perform ab initio molecular dynamics on 3×3×3 supercells with a single vacancy and with the <111> cluster. Use the PBE functional, NVT ensemble at 1000 K, 1 fs time step, Γ‑point sampling. Run a 2 ps equilibration followed by a 4 ps production run. Analyse oxygen trajectories to count vacancy jumps and characterise diffusion behaviour.
- Output file: `/app/outputs/aimd_analysis.json`
- Format: json
- Contract: JSON object with keys 'single_vacancy_system' and 'cluster_system', each an object with 'total_time_ps' (float), 'num_jumps' (integer), 'jump_pattern' (string).
- Scoring: scored by hidden verifier

### Step 6: Investigate Ce³⁺ influence on migration barriers
- Role: scored
- Action: For a single oxygen vacancy, create models with 0, 1 and 2 Ce³⁺ ions near the migration path. Calculate the migration barrier for each configuration using NEB.
- Output file: `/app/outputs/ce3_migration_barriers.json`
- Format: json
- Contract: JSON array of objects, each with 'model' (string), 'num_Ce3' (integer), 'barrier_eV' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/migration_barriers.json`
- `/app/outputs/aimd_analysis.json`
- `/app/outputs/ce3_migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of single and clustered vacancies and relative stability of five short-range vacancy pair configurations.
- schema:
  - `type`: object
  - `required`: `single_vacancy`, `cluster_vacancy`, `relative_stability`
  - `single_vacancy`: object mapping charge state string (e.g., '0', '2+') to formation energy (eV, float)
  - `cluster_vacancy`: object mapping charge state string to formation energy (eV, float)
  - `relative_stability`: object mapping configuration name (e.g., '<111>', '<100>') to relative total energy (eV, float)

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Migration barriers of single oxygen vacancy and <111> vacancy cluster along different directions.
- schema:
  - `type`: object
  - `required`: `single_vacancy`, `cluster_vacancy`
  - `single_vacancy`: object with direction string keys (e.g., '<100>') each mapping to an array of barrier values (eV, float)
  - `cluster_vacancy`: object with direction string keys each mapping to an array of barrier values (eV, float)

### aimd_analysis.json
- path: `/app/outputs/aimd_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: AIMD simulation analysis comparing diffusion behaviour of a single vacancy and the <111> cluster.
- schema:
  - `type`: object
  - `required`: `single_vacancy_system`, `cluster_system`
  - `single_vacancy_system`:
    - `type`: object
    - `required`: `total_time_ps`, `num_jumps`, `jump_pattern`
    - `total_time_ps`: number
    - `num_jumps`: integer
    - `jump_pattern`: string
  - `cluster_system`:
    - `type`: object
    - `required`: `total_time_ps`, `num_jumps`, `jump_pattern`
    - `total_time_ps`: number
    - `num_jumps`: integer
    - `jump_pattern`: string

### ce3_migration_barriers.json
- path: `/app/outputs/ce3_migration_barriers.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Effect of Ce3+ ion count near the migration path on the single-vacancy migration barrier.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `model`, `num_Ce3`, `barrier_eV`
    - `model`: string
    - `num_Ce3`: integer
    - `barrier_eV`: float

Notes: All quantities are recomputed using an open-source DFT code; exact numerical values may differ from the original VASP+HSE paper. Scoring relies on reproducible trends and thresholds (e.g., <111> cluster is most stable, cluster formation energy negative under O-poor, cluster barriers >1.5× single-vacancy barriers, AIMD jump counts, monotonic barrier increase with Ce3+).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "single_vacancy",
          "cluster_vacancy",
          "relative_stability"
        ],
        "single_vacancy": "object mapping charge state string (e.g., '0', '2+') to formation energy (eV, float)",
        "cluster_vacancy": "object mapping charge state string to formation energy (eV, float)",
        "relative_stability": "object mapping configuration name (e.g., '<111>', '<100>') to relative total energy (eV, float)"
      },
      "description": "Formation energies of single and clustered vacancies and relative stability of five short-range vacancy pair configurations."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "single_vacancy",
          "cluster_vacancy"
        ],
        "single_vacancy": "object with direction string keys (e.g., '<100>') each mapping to an array of barrier values (eV, float)",
        "cluster_vacancy": "object with direction string keys each mapping to an array of barrier values (eV, float)"
      },
      "description": "Migration barriers of single oxygen vacancy and <111> vacancy cluster along different directions."
    },
    {
      "file": "aimd_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "single_vacancy_system",
          "cluster_system"
        ],
        "single_vacancy_system": {
          "type": "object",
          "required": [
            "total_time_ps",
            "num_jumps",
            "jump_pattern"
          ],
          "total_time_ps": "number",
          "num_jumps": "integer",
          "jump_pattern": "string"
        },
        "cluster_system": {
          "type": "object",
          "required": [
            "total_time_ps",
            "num_jumps",
            "jump_pattern"
          ],
          "total_time_ps": "number",
          "num_jumps": "integer",
          "jump_pattern": "string"
        }
      },
      "description": "AIMD simulation analysis comparing diffusion behaviour of a single vacancy and the <111> cluster."
    },
    {
      "file": "ce3_migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "model",
            "num_Ce3",
            "barrier_eV"
          ],
          "model": "string",
          "num_Ce3": "integer",
          "barrier_eV": "float"
        }
      },
      "description": "Effect of Ce3+ ion count near the migration path on the single-vacancy migration barrier."
    }
  ],
  "notes": "All quantities are recomputed using an open-source DFT code; exact numerical values may differ from the original VASP+HSE paper. Scoring relies on reproducible trends and thresholds (e.g., <111> cluster is most stable, cluster formation energy negative under O-poor, cluster barriers >1.5× single-vacancy barriers, AIMD jump counts, monotonic barrier increase with Ce3+)."
}
```

## How you are scored
A hidden verifier reads your submitted JSON artifacts and independently checks them against expected trends and thresholds derived from the original study. Each scored artifact contributes a fixed fraction to the total reward:
- `formation_energies.json`: formation energy values and relative stability of vacancy configurations are checked for consistency with the paper's thermodynamic findings.
- `migration_barriers.json`: the computed barriers for the single vacancy and cluster are compared to verify that their relative magnitudes and direction preferences align with the paper's mobility analysis.
- `aimd_analysis.json`: the jump counts and diffusion patterns are checked to see if they match the paper's description of vacancy motion (high mobility vs. trapping).
- `ce3_migration_barriers.json`: the barrier values for different Ce³⁺ configurations are examined for a trend that is consistent with the paper's analysis of polaron effects.

Because you will use a different DFT code and possibly different computational settings than the original work, absolute numerical values are expected to differ modestly. The verifier applies generous tolerances and focuses on the scientifically robust, reproducible **trends** and **relative comparisons** listed above. Simply reporting the numerical values from the original paper without actually running the calculations will almost certainly fail the trend checks.
