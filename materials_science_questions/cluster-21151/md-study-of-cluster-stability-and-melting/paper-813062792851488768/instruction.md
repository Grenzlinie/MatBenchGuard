# MD Simulation of Argon Cluster Formation and Stability

## Problem background
The formation and stability of microclusters in compressed gases are relevant to nucleation, catalysis, and interface phenomena. This task investigates argon cluster formation in the gas phase using molecular dynamics (MD) simulations. Two potential models are compared: a simple two-body Lennard-Jones potential (model A) and a combination of the Lennard-Jones potential with three-body Axilrod-Teller interactions (model B). The simulations are performed at two temperatures (273 K and 150 K). The question is how the inclusion of three-body interactions affects the cluster size distribution and cluster lifetimes under these conditions.

## Approach
Run classical MD simulations of 108 argon atoms in a cubic box with periodic boundary conditions at the specified density and temperatures. For each temperature, perform two independent simulations: one using the LJ potential only (model A) and one using the LJ plus AT potential (model B). After thermalization and equilibration, record averaged atomic coordinates over the production period. From the resulting trajectories, identify clusters using a geometric criterion: two atoms belong to the same aggregate if their separation is less than a cutoff radius R_cl = 2.00σ, where σ is the argon LJ radius. A quasi-stability filter is applied: a cluster is counted only if it persists with the same set of atoms for at least the characteristic oscillation period of an Ar₂ dimer (~500 integration steps). For each condition, compute (a) the total number of cluster occurrences for each size (counting every appearance) and (b) the number of unique clusters (distinct sets of atoms) for each size. The average lifetime in picoseconds of clusters of a given size is computed as (all_clusters_count / unique_clusters_count) × 0.2 ps, where 0.2 ps is the time interval between successive recorded frames (100 integration steps of 2e-15 s each). The output is a single CSV file reporting all quantities per cluster size for each model and temperature.

## Reproduction target
Produce a CSV file containing the cluster size distribution data for all four conditions: model A at 273 K and 150 K, and model B at 273 K and 150 K. For each (temperature, model, cluster_size) combination, report the all-clusters count, the unique-clusters count, and the average lifetime in picoseconds.

## Assets

- Molecular dynamics simulation engine (ASE, LAMMPS, or custom Python code): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Run MD simulations
- Role: process
- Action: Run four molecular dynamics simulations of 108 argon atoms in a cubic box of side 4.254 nm with periodic boundary conditions: (1) model A at 273 K, (2) model A at 150 K, (3) model B at 273 K, (4) model B at 150 K. Initialize atoms on an fcc lattice, thermalize, then run for 30000 integration steps (time step 20e-16 s) recording averaged coordinates every 100 steps after thermalization. Exclude the last 500 steps from recording. Store trajectories for subsequent analysis.
- Evidence: `/app/outputs/trajectories`

### Step 2: Compute cluster distributions and lifetimes
- Role: scored (load-bearing)
- Action: For each trajectory, identify clusters using a geometric criterion: two atoms belong to the same cluster if their distance is less than R_cl = 2.00 * sigma = 6.81 Å. Apply a quasi-stability filter: a cluster is counted only if it persists with the same set of atoms for at least ~500 integration steps (one Ar2 oscillation period). Compute (a) total number of occurrences for each cluster size, and (b) number of unique clusters (distinct atom sets) for each size. Compute the average lifetime in picoseconds for each cluster size as (all_clusters_count / unique_clusters_count) × 0.2 ps, where 0.2 ps is the time between recorded frames (100 integration steps × 2e-15 s/step = 2e-13 s = 0.2 ps). Write all results, including the average_lifetime_ps column, to cluster_results.csv.
- Output file: `/app/outputs/cluster_results.csv`
- Format: csv
- Contract: temperature (int), model (string: 'A' or 'B'), cluster_size (int), all_clusters_count (int), unique_clusters_count (int), average_lifetime_ps (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cluster_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cluster_results.csv
- path: `/app/outputs/cluster_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The main reproduction output: cluster size distributions (all occurrences and unique clusters) and average lifetime (computed as (all_clusters_count/unique_clusters_count)*0.2 ps) per size for four conditions (model A/B, 273 K/150 K). The hidden checker compares each row against digitized gold values from the paper's figures using tolerances.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `model`, `cluster_size`, `all_clusters_count`, `unique_clusters_count`, `average_lifetime_ps`
  - `units`:
    - `temperature`: K
    - `model`: string (A or B)
    - `cluster_size`: dimensionless
    - `all_clusters_count`: count
    - `unique_clusters_count`: count
    - `average_lifetime_ps`: ps

Notes: The agent must produce exactly this CSV. Average lifetime must be computed as (all_clusters_count/unique_clusters_count)*0.2 ps, where 0.2 ps is the time between recorded frames (100 integration steps of 2e-15 s each). The hidden checker reads the reported values directly and compares them to hidden reference values (digitized from the paper) with per-row tolerances. The process step (md_simulations) is required to generate the trajectories that feed this analysis; its evidence is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cluster_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "model",
          "cluster_size",
          "all_clusters_count",
          "unique_clusters_count",
          "average_lifetime_ps"
        ],
        "units": {
          "temperature": "K",
          "model": "string (A or B)",
          "cluster_size": "dimensionless",
          "all_clusters_count": "count",
          "unique_clusters_count": "count",
          "average_lifetime_ps": "ps"
        }
      },
      "description": "The main reproduction output: cluster size distributions (all occurrences and unique clusters) and average lifetime (computed as (all_clusters_count/unique_clusters_count)*0.2 ps) per size for four conditions (model A/B, 273 K/150 K). The hidden checker compares each row against digitized gold values from the paper's figures using tolerances."
    }
  ],
  "notes": "The agent must produce exactly this CSV. Average lifetime must be computed as (all_clusters_count/unique_clusters_count)*0.2 ps, where 0.2 ps is the time between recorded frames (100 integration steps of 2e-15 s each). The hidden checker reads the reported values directly and compares them to hidden reference values (digitized from the paper) with per-row tolerances. The process step (md_simulations) is required to generate the trajectories that feed this analysis; its evidence is not scored."
}
```

## How you are scored
A hidden verifier reads your submitted `cluster_results.csv` and compares the values for each row that matches a (temperature, model, cluster_size) entry present in a hidden set of reference values. The all_clusters_count, unique_clusters_count, and average_lifetime_ps are checked against these references. Passing rows that fall within a pre-defined tolerance contribute a point; rows that do not pass or are missing receive zero. The final reward is the fraction of checked rows that pass, weighted equally across the reported conditions and cluster sizes.
