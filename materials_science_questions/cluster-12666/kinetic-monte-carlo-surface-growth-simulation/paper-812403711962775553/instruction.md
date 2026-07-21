# Kinetic Monte Carlo Simulation of Surface Growth with Site-Dependent Reaction Rates

## Problem background
Chemical vapor deposition (CVD) is a common thin‑film growth technique, yet the kinetic mechanisms that shape the island morphology during early‑stage deposition remain less well understood than for physical vapor deposition (PVD). A central question is whether site‑specific chemical reactivity—precursor decomposition that is faster on existing metallic clusters than on the bare substrate—can dominate the evolution of island structure, producing larger islands and a signature size distribution. The iron pentacarbonyl / Si(100) system serves as a model case for probing this question with kinetic Monte Carlo (KMC) simulations. Here, simulations compare two growth modes: one where the reaction probability depends on the surface site type (CVD) and one with random deposition (PVD). The outputs are the average cluster size as a function of sub‑monolayer coverage and the island‑size distribution at a fixed coverage. The task is to implement the KMC model and to check whether site‑preferential reactivity alone can generate the structural trends observed in such a system.

## Approach
A lattice‑gas kinetic Monte Carlo simulation is performed on a 256×256 square grid with periodic boundaries. Each deposition attempt is accepted with a constant sticking coefficient. Decomposition is treated as a thermally activated process with different activation energies on bare Si and on Fe sites; desorption from Si is also included. Reaction probabilities are computed from an Arrhenius factor at the growth temperature (200 °C). No adatom surface diffusion or cluster breakup is allowed, and a single atom already constitutes a stable cluster (critical nucleus size = 1). The simulation is run for both a CVD mode (site‑dependent reaction probabilities) and a PVD mode (every incident atom sticks) to build island configurations at coverages from 0.05 ML to 0.25 ML. From these configurations, the average number of atoms per island is computed at each coverage, and the size distribution is tabulated at 0.25 ML. Comparing CVD to PVD isolates the effect of differential reaction kinetics.

## Reproduction target
Produce two comma‑separated tables:

1. `average_cluster_sizes.csv` with columns `coverage_ML`, `avg_cluster_size_CVD_atoms`, `avg_cluster_size_PVD_atoms`. The table must include rows for coverages 0.05, 0.10, 0.15, 0.20, and 0.25 ML.

2. `island_size_distribution.csv` with columns `size_atoms` (integer), `count_CVD`, `count_PVD`. This table gives the island‑size distribution at 0.25 ML coverage.

The evaluation looks for two structural trends without requiring any specific numerical values:
- In every row of `average_cluster_sizes.csv`, the CVD average size is strictly larger than the PVD average size.
- In `island_size_distribution.csv`, the `count_CVD` values as a function of `size_atoms` form a non‑increasing sequence (no local peak).

## Assets

- Python scientific stack (numpy, matplotlib, scipy): numpy matplotlib scipy

## Workflow steps

### Step 1: Run kinetic Monte Carlo simulations
- Role: process
- Action: Implement a kinetic Monte Carlo simulation of Fe deposition on a 256×256 square lattice with periodic boundaries. Use activation energies 0.40 eV (decomposition on Si), 0.14 eV (on Fe), desorption barrier 0.35 eV, sticking coefficient 0.1, critical nucleus size 1, no adatom diffusion, no detachment. Run CVD (site‑dependent reaction probabilities) and PVD (random deposition). Simulate at 200°C (473 K) for coverages 0.05, 0.10, 0.15, 0.20, and 0.25 ML. Save the raw island configurations or cluster size lists for each condition to a file for downstream analysis.
- Evidence: `/app/outputs/simulation_results.npz`

### Step 2: Compute average cluster sizes vs. coverage
- Role: scored (load-bearing)
- Action: Load the simulation data from Step 1. For each coverage and each growth mode (CVD, PVD) compute the average number of atoms per island. Write a table with columns coverage_ML, avg_cluster_size_CVD_atoms, avg_cluster_size_PVD_atoms.
- Output file: `/app/outputs/average_cluster_sizes.csv`
- Format: csv
- Contract: coverage_ML (float), avg_cluster_size_CVD_atoms (float), avg_cluster_size_PVD_atoms (float)
- Scoring: scored by hidden verifier

### Step 3: Compute island size distribution at 0.25 ML
- Role: scored (load-bearing)
- Action: Load the simulation data from Step 1 for the 0.25 ML runs. Bin island sizes by number of atoms and count how many islands fall into each bin for CVD and PVD. Write a table with columns size_atoms, count_CVD, count_PVD.
- Output file: `/app/outputs/island_size_distribution.csv`
- Format: csv
- Contract: size_atoms (int), count_CVD (int), count_PVD (int)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/average_cluster_sizes.csv`
- `/app/outputs/island_size_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### average_cluster_sizes.csv
- path: `/app/outputs/average_cluster_sizes.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of average cluster sizes vs. coverage for CVD and PVD growth. The structural check verifies CVD size > PVD size for all rows.
- schema:
  - `required_columns`: `coverage_ML`, `avg_cluster_size_CVD_atoms`, `avg_cluster_size_PVD_atoms`
  - `units`:
    - `coverage_ML`: dimensionless (monolayer fraction)
    - `avg_cluster_size_CVD_atoms`: atoms
    - `avg_cluster_size_PVD_atoms`: atoms

### island_size_distribution.csv
- path: `/app/outputs/island_size_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Island size distribution at 0.25 ML coverage. The structural check verifies CVD count is a monotonically decreasing function of size_atoms.
- schema:
  - `required_columns`: `size_atoms`, `count_CVD`, `count_PVD`
  - `units`:
    - `size_atoms`: atoms
    - `count_CVD`: integer
    - `count_PVD`: integer

Notes: Both scored files are derived from the KMC simulation step. Scoring relies on trend verification (structural audit) without exact numeric tolerances, as described in the task plan.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "average_cluster_sizes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "coverage_ML",
          "avg_cluster_size_CVD_atoms",
          "avg_cluster_size_PVD_atoms"
        ],
        "units": {
          "coverage_ML": "dimensionless (monolayer fraction)",
          "avg_cluster_size_CVD_atoms": "atoms",
          "avg_cluster_size_PVD_atoms": "atoms"
        }
      },
      "description": "Table of average cluster sizes vs. coverage for CVD and PVD growth. The structural check verifies CVD size > PVD size for all rows."
    },
    {
      "file": "island_size_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "size_atoms",
          "count_CVD",
          "count_PVD"
        ],
        "units": {
          "size_atoms": "atoms",
          "count_CVD": "integer",
          "count_PVD": "integer"
        }
      },
      "description": "Island size distribution at 0.25 ML coverage. The structural check verifies CVD count is a monotonically decreasing function of size_atoms."
    }
  ],
  "notes": "Both scored files are derived from the KMC simulation step. Scoring relies on trend verification (structural audit) without exact numeric tolerances, as described in the task plan."
}
```

## How you are scored
A hidden verifier reads your two output tables. It checks the required file format and then verifies the structural trends:
1. For every coverage, it tests that `avg_cluster_size_CVD_atoms` > `avg_cluster_size_PVD_atoms`.
2. For the distribution, it checks that the `count_CVD` column is monotonically non‑increasing with increasing `size_atoms` (i.e., counts never rise as size grows; a peak is absent).

The final reward (0–1) is a weighted combination of partial scores for each trend. Submitting files with the correct format but violating either trend reduces the score proportionally. There is no penalty for run‑to‑run numerical variation; the score depends only on whether your computed results satisfy these inequality and monotonicity conditions.
