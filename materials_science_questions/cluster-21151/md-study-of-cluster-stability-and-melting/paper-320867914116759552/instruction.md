# Structural outcome probabilities of vacancy‑containing Al clusters under heating

## Problem background
In nanomaterials, structural disorder such as monovacancies introduced during compaction can profoundly alter the thermal stability and crystallographic phase of metal nanoparticles. Understanding how vacancy concentration drives structural transformations in aluminum clusters is important for designing nanocrystalline materials with tailored properties. This task investigates, via classical molecular dynamics, the influence of vacancy fraction (20%, 25%, 30%) on the structural evolution (FCC, amorphous, decahedral, icosahedral) of aluminum clusters of diameter 3 nm and 4 nm under heating. The objective is to compute the probabilities of different structural outcomes and the temperature intervals where each structure appears.

## Approach
Spherical FCC aluminum clusters of diameter 3 nm and 4 nm are created by cutting from the Al FCC lattice. Random vacancy removal produces initial disordered configurations with fractions 20%, 25%, and 30%. Each cluster is relaxed at 60 K and then heated in constant-temperature (NVT) molecular dynamics using the Cleri–Rosato TB‑SMA potential and a Nosé–Hoover thermostat. Multiple independent simulations per condition are run. The atomic trajectories are analysed with a structure identification method (e.g., Common Neighbor Analysis) to classify each run as FCC or amorphous after relaxation, and as Dh, Ih, FCC, twinned FCC, or complex during heating, together with the associated temperature windows. The per‑simulation classifications are then aggregated to obtain the structural outcome probabilities and dominant temperature intervals for each size–vacancy combination.

## Reproduction target
Compute the aggregate structural outcome probabilities for Al clusters of diameter 3 nm and 4 nm with vacancy fractions 20%, 25%, and 30%. For each condition, report:
- After relaxation at 60 K: the percentage of clusters that are FCC and the percentage that are amorphous.
- After heating: the percentage of clusters that exhibit Dh, Ih, FCC, twinned FCC, and complex structures, and the most commonly observed temperature interval (minimum and maximum in K) for each structure.
The task culminates in the scored JSON file `disorder_structural_outcomes.json`, whose exact schema is given under Step 4 and the Output Contract.

## Assets

- Cleri–Rosato TB‑SMA potential for Al: 10.1103/PhysRevB.48.22
- LAMMPS molecular dynamics simulator: https://www.lammps.org/

## Workflow steps

### Step 1: Generate initial atomic coordinates
- Role: process
- Action: Generate spherical FCC Al clusters of diameter 3 nm and 4 nm by cutting a sphere from the Al FCC lattice. For each size, randomly remove atoms to achieve vacancy fractions of 20%, 25%, and 30%. Write coordinate files in a format suitable for MD (e.g. XYZ or LAMMPS data).
- Evidence: `/app/outputs/initial_clusters.xyz`

### Step 2: Run MD simulations of vacancy‑containing clusters
- Role: process
- Action: For each cluster condition (size × vacancy fraction), perform NVT molecular dynamics using the Cleri–Rosato TB‑SMA potential with a time step of 1 fs and a Nosé–Hoover thermostat. Relax the clusters at 60 K for 1 ns, then heat from 60 K to a temperature high enough to observe all structural transitions (e.g. 600–800 K) with a step of 10 K and a hold time of 0.5 ns at each temperature. Run multiple independent simulations (at least 10) for each condition. Save atomic trajectories for later structural analysis.
- Evidence: `/app/outputs/md_simulation_log.txt`

### Step 3: Classify structure per simulation
- Role: scored (load-bearing)
- Action: Analyze each MD trajectory using a suitable structure identification method (e.g. Common Neighbor Analysis or polyhedral template matching). For each trajectory, record the structure observed after the 1 ns relaxation (FCC or amorphous) and the dominant structure formed during heating (Dh, Ih, FCC, twinned_FCC, or complex), along with the temperature interval (T_min, T_max) where that structure first appears and remains stable. Write the results to a single CSV file.
- Output file: `/app/outputs/per_simulation_classification.csv`
- Format: csv
- Contract: CSV with columns: size_nm (float), vacancy_fraction (float), run_id (int), relaxation_structure (string: 'FCC' or 'amorphous'), heating_structure (string: 'Dh','Ih','FCC','twinned_FCC','complex'), T_min_K (float), T_max_K (float). Each row corresponds to one independent simulation.
- Scoring: scored by hidden verifier

### Step 4: Compute aggregate structural outcome probabilities
- Role: scored
- Action: From the per‑simulation classification data, compute for each condition (size, vacancy fraction) the percentage of clusters that exhibit each structure after relaxation and after heating, and the most commonly observed temperature intervals for each structure. Write the aggregates to a JSON file.
- Output file: `/app/outputs/disorder_structural_outcomes.json`
- Format: json
- Contract: JSON object with keys for each condition (e.g., 'D3nm_vac20'). Each value is an object with 'relaxation_stage' (object with 'FCC_percent' and 'amorphous_percent'), 'heating_stage' (object with 'Dh_percent','Ih_percent','FCC_percent','twinned_FCC_percent','complex_percent'), and 'temperature_intervals' (object with keys for each structure, each containing 'T_min_K' and 'T_max_K').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/per_simulation_classification.csv`
- `/app/outputs/disorder_structural_outcomes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### per_simulation_classification.csv
- path: `/app/outputs/per_simulation_classification.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw per-simulation structural classification for all runs. The checker recomputes the aggregate outcome probabilities and temperature intervals from this file.
- schema:
  - `type`: table
  - `required_columns`: `size_nm`, `vacancy_fraction`, `run_id`, `relaxation_structure`, `heating_structure`, `T_min_K`, `T_max_K`
  - `units`:
    - `size_nm`: nm
    - `vacancy_fraction`: 
    - `run_id`: 
    - `relaxation_structure`: 
    - `heating_structure`: 
    - `T_min_K`: K
    - `T_max_K`: K

### disorder_structural_outcomes.json
- path: `/app/outputs/disorder_structural_outcomes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate structural outcome probabilities and dominant temperature intervals. The checker compares these against the paper’s reference values (hidden) within tolerances.
- schema:
  - `type`: object
  - `description`: Top-level JSON object with keys for each condition (e.g., 'D3nm_vac20'). Each condition contains 'relaxation_stage' (object with 'FCC_percent' and 'amorphous_percent'), 'heating_stage' (object with 'Dh_percent','Ih_percent','FCC_percent','twinned_FCC_percent','complex_percent'), and 'temperature_intervals' (object with keys 'Dh','Ih','FCC', each containing 'T_min_K' and 'T_max_K').

Notes: The checker recomputes the aggregate statistics from per_simulation_classification.csv and then compares those recomputed values to the paper‑reported percentages and temperature intervals with appropriate tolerances. It also cross‑checks disorder_structural_outcomes.json against the recomputed aggregates for self‑consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "per_simulation_classification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "size_nm",
          "vacancy_fraction",
          "run_id",
          "relaxation_structure",
          "heating_structure",
          "T_min_K",
          "T_max_K"
        ],
        "units": {
          "size_nm": "nm",
          "vacancy_fraction": "",
          "run_id": "",
          "relaxation_structure": "",
          "heating_structure": "",
          "T_min_K": "K",
          "T_max_K": "K"
        }
      },
      "description": "Raw per-simulation structural classification for all runs. The checker recomputes the aggregate outcome probabilities and temperature intervals from this file."
    },
    {
      "file": "disorder_structural_outcomes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Top-level JSON object with keys for each condition (e.g., 'D3nm_vac20'). Each condition contains 'relaxation_stage' (object with 'FCC_percent' and 'amorphous_percent'), 'heating_stage' (object with 'Dh_percent','Ih_percent','FCC_percent','twinned_FCC_percent','complex_percent'), and 'temperature_intervals' (object with keys 'Dh','Ih','FCC', each containing 'T_min_K' and 'T_max_K')."
      },
      "description": "Aggregate structural outcome probabilities and dominant temperature intervals. The checker compares these against the paper’s reference values (hidden) within tolerances."
    }
  ],
  "notes": "The checker recomputes the aggregate statistics from per_simulation_classification.csv and then compares those recomputed values to the paper‑reported percentages and temperature intervals with appropriate tolerances. It also cross‑checks disorder_structural_outcomes.json against the recomputed aggregates for self‑consistency."
}
```

## How you are scored
A hidden verifier evaluates your outputs independently.
- It reads `/app/outputs/per_simulation_classification.csv` and recomputes the aggregate structural outcome probabilities and temperature intervals from that raw data.
- It then compares those recomputed aggregates to stored reference values (with appropriate tolerances) and checks that `/app/outputs/disorder_structural_outcomes.json` is internally consistent with the recomputed aggregates.
- Each scored output contributes a portion of the total reward. Simply reporting a number that matches the reference is insufficient; the verifier expects genuine execution documented by the per‑simulation raw classification.
