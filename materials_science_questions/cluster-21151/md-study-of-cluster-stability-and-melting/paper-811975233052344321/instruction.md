# Relaxation Dynamics of Diffusion-Limited Aggregation Clusters

## Problem background
Diffusion-limited aggregation (DLA) on a square lattice produces tenuous, fractal clusters that are far from thermal equilibrium. When such clusters are allowed to relax toward equilibrium via single-particle hops that favor lower energy, the initially connected aggregate may evolve into a collection of smaller disconnected clusters. It is not obvious how the number of clusters and the total energy evolve in time, how the relaxation depends on the allowed hopping distance, or whether the aggregate's fractal dimension changes during this process. Understanding this relaxation behaviour and its dependence on the hopping radius and surface tension is relevant for modelling long-term evolution of fluid injected into a porous medium, yet it remains an open computational question.

## Approach
We first generate a DLA cluster on a square lattice using random walkers that stick irreversibly on contact; optionally, surface tension can be introduced via a curvature-dependent sticking probability. The resulting aggregate serves as the starting non-equilibrium configuration. We then allow the cluster to relax via zero-temperature Kawasaki dynamics: at each step a perimeter particle is selected at random and attempts to hop to a site within a prescribed hopping radius. The move is accepted if its local nearest-neighbour energy decreases; if the energy is unchanged it is accepted with 50% probability, otherwise it is rejected. Time is measured in Monte Carlo steps per particle (MCS/particle). During the relaxation we periodically record three observables: (i) the total nearest-neighbour attractive energy per particle, (ii) the number of disconnected clusters (identified via nearest-neighbour connectivity), and (iii) the effective fractal dimension computed from the radial particle density relative to the centre of mass. By sweeping at least two hopping radii without surface tension and one run with a small surface tension, we can extract how these observables depend on the simulation conditions. To mitigate statistical fluctuations we average over multiple independent random-number sequences.

## Reproduction target
The objective is to compute the time-resolved relaxation dynamics of DLA clusters and collect the resulting time series in a single CSV file. You must run simulations for at least two distinct hopping radii (e.g., radii that include 8 and 36 nearest lattice sites) with zero surface tension, plus one additional run with a surface tension of approximately 0.1 and any hopping radius. For each condition, record the evolution of energy, cluster count, and effective fractal dimension over many MCS/particle. All measured time series must be saved to `/app/outputs/relaxation_results.csv` with the columns: `hopping_radius`, `surface_tension`, `mcs_per_particle`, `energy`, `cluster_count`, `fractal_dimension`. The hidden verifier will then analyse the time series — looking for characteristic physical behaviours such as the shape of the cluster count versus time curve, the energy decay profile, and the stability of the fractal dimension — and compare the final values against reference benchmarks to produce a score.

## Assets

- Python 3 with numpy, scipy, matplotlib

## Workflow steps

### Step 1: Generate DLA cluster
- Role: process
- Action: Implement diffusion-limited aggregation on a square lattice with optional surface tension via curvature-dependent sticking probability. Produce an initial aggregate with a specified number of particles.
- Evidence: `/app/outputs/dla_config.txt`

### Step 2: Relax cluster and record observables
- Role: scored (load-bearing)
- Action: Load the DLA cluster. Perform zero-temperature Kawasaki dynamics: randomly select a perimeter particle, attempt to hop to a site within a given hopping radius, accept with Metropolis rule (lower energy: always; same energy: 50% probability). Measure time in Monte Carlo steps per particle (MCS/particle). Periodically record the total energy (per particle), the number of disconnected clusters (via nearest-neighbor connectivity), and the effective fractal dimension (from radial density relative to center of mass). Run for at least two hopping radii (e.g., 8 and 36 nearest sites) with zero surface tension, and one run with surface tension ~0.1. Average over multiple random sequences. Produce a single CSV file with all time series.
- Output file: `/app/outputs/relaxation_results.csv`
- Format: csv
- Contract: Columns: hopping_radius (int), surface_tension (float), mcs_per_particle (float), energy (float, average nearest-neighbor bond energy per particle), cluster_count (int), fractal_dimension (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxation_results.csv
- path: `/app/outputs/relaxation_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of relaxation for multiple conditions: average energy per particle, number of disconnected clusters, and effective fractal dimension as functions of Monte Carlo steps per particle.
- schema:
  - `type`: table
  - `required_columns`: `hopping_radius`, `surface_tension`, `mcs_per_particle`, `energy`, `cluster_count`, `fractal_dimension`
  - `units`:
    - `energy`: nearest-neighbor bond energy per particle

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "hopping_radius",
          "surface_tension",
          "mcs_per_particle",
          "energy",
          "cluster_count",
          "fractal_dimension"
        ],
        "units": {
          "energy": "nearest-neighbor bond energy per particle"
        }
      },
      "description": "Time series of relaxation for multiple conditions: average energy per particle, number of disconnected clusters, and effective fractal dimension as functions of Monte Carlo steps per particle."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will examine your submitted CSV file. First it will check that the file exists, is valid CSV, and contains the required columns and sufficient data rows for the three requested parameter combinations. Then it will compute a score for the relaxation dynamics: it will extract the time series for each condition, verify structural patterns (e.g., the qualitative shape of the cluster count and energy curves, the fractal dimension stability, and the dependence on hopping radius), and compare the late-time energy and cluster count values against hidden reference benchmarks (within appropriate tolerances). The reward is a single float between 0 and 1 that reflects how well the observed dynamics match the expected behavior; a higher reward indicates better agreement. The verifier does *not* know how you obtained the data, but it can detect fabricated or trivial solutions because such solutions fail the structural and trend checks. To succeed, you must perform an honest simulation and save the resulting observables as described.
