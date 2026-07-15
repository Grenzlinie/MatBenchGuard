# MD Shock-Induced Chemistry in Anthracene

## Problem background
Shock waves passing through organic molecular crystals can trigger chemical reactions such as polymerization and fragmentation. Studying these processes is important for understanding impact chemistry in cometary collisions, energetic materials, and planetary science. Anthracene is a large, anisotropic unsaturated hydrocarbon that forms molecular crystals with different packing arrangements along its crystallographic axes. Molecular dynamics (MD) simulations with a reactive bond-order potential allow the direct observation of shock-induced bond breaking and formation, revealing what products are generated and whether the outcome depends on the shock orientation. This task investigates shock-induced chemistry in anthracene by simulating flyer-plate impacts along two crystal directions and quantifying the resulting carbon-cluster product distributions.

## Approach
The approach uses classical MD with the AIREBO reactive potential, which describes bond breaking and formation for hydrocarbons. An anthracene crystal cell is first minimized from experimental crystallographic parameters (monoclinic, P2_1/a). Then, two large slab-like crystal segments (40320 atoms, 1680 molecules) are set up with a gap between them and periodic boundary conditions transverse to the intended shock direction. The segments are launched toward each other at a relative velocity of 12 km/s, generating a flyer-plate shock. Two independent simulations are run: one with the shock propagating along the a-axis and the other along the c-axis. After at least 5 ps, the final atomic configuration is analyzed to identify all connected carbon clusters (ignoring hydrogen) and record the number of carbon atoms in each cluster. This yields the carbon-cluster product distribution for each orientation, which can be compared to understand any orientation dependence.

## Reproduction target
Produce the carbon-cluster product distributions from flyer-plate shock simulations of anthracene at 12 km/s impact velocity along both the a-axis and c-axis. For each simulation, output a CSV file containing the size (number of carbon atoms) of every connected carbon cluster present in the final snapshot at 5 ps. The hidden verifier will compare the two cluster-size lists to reference distributions derived from published simulation data to assess how faithfully the reproduced results capture the key chemical outcomes.

## Assets

- Anthracene experimental crystal structure: 1100001
- LAMMPS molecular dynamics package with AIREBO potential: https://www.lammps.org/

## Workflow steps

### Step 1: Minimize anthracene crystal structure with AIREBO potential
- Role: process
- Action: Using the experimental anthracene crystal structure (monoclinic, space group P2_1/a, COD 1100001), perform energy minimization with the AIREBO potential in LAMMPS to obtain the equilibrium unit cell and atomic positions. Save minimized structure as a LAMMPS data file.
- Evidence: `/app/outputs/equilibrium_structure.data`

### Step 2: Run flyer-plate shock MD simulation along a-axis
- Role: process
- Action: Set up a flyer-plate shock simulation from the minimized structure: 40320 atoms (1680 anthracene molecules), slab geometry with periodic boundary conditions transverse to shock direction, zero-temperature initial conditions, relative flyer velocity 12 km/s, shock along crystallographic a-axis. Run for at least 5 ps using AIREBO potential. Save the final atomic snapshot.
- Evidence: `/app/outputs/shock_a_axis_final.dump`

### Step 3: Run flyer-plate shock MD simulation along c-axis
- Role: process
- Action: Set up a flyer-plate shock simulation from the minimized structure: 40320 atoms, shock along crystallographic c-axis, all other parameters identical (0 K, 12 km/s, 5 ps, periodic transverse BC). Save the final atomic snapshot.
- Evidence: `/app/outputs/shock_c_axis_final.dump`

### Step 4: Compute carbon cluster distribution for a-axis shock
- Role: scored (load-bearing)
- Action: Load the a-axis final snapshot, identify connected carbon clusters (carbon atoms within bonding cutoff, ignoring hydrogen), and record the size of each cluster in carbon atoms.
- Output file: `/app/outputs/cluster_sizes_a_axis.csv`
- Format: csv
- Contract: CSV file with header 'cluster_size', one integer per row (one row per identified cluster).
- Scoring: scored by hidden verifier

### Step 5: Compute carbon cluster distribution for c-axis shock
- Role: scored
- Action: Load the c-axis final snapshot, identify connected carbon clusters (carbon atoms within bonding cutoff, ignoring hydrogen), and record the size of each cluster in carbon atoms.
- Output file: `/app/outputs/cluster_sizes_c_axis.csv`
- Format: csv
- Contract: CSV file with header 'cluster_size', one integer per row (one row per identified cluster).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cluster_sizes_a_axis.csv`
- `/app/outputs/cluster_sizes_c_axis.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cluster_sizes_a_axis.csv
- path: `/app/outputs/cluster_sizes_a_axis.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Carbon cluster sizes (number of carbons per connected cluster) identified from the a-axis shock simulation at 12 km/s and 5 ps.
- schema:
  - `type`: table
  - `required_columns`: `cluster_size`
  - `units`: object

### cluster_sizes_c_axis.csv
- path: `/app/outputs/cluster_sizes_c_axis.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Carbon cluster sizes from the c-axis shock simulation at 12 km/s and 5 ps.
- schema:
  - `type`: table
  - `required_columns`: `cluster_size`
  - `units`: object

Notes: The checker will recompute histograms from these CSVs and compare to hidden gold values from the paper (e.g., 28-carbon dimer count, unreacted 14-carbon count, fragmentation patterns).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cluster_sizes_a_axis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster_size"
        ],
        "units": {}
      },
      "description": "Carbon cluster sizes (number of carbons per connected cluster) identified from the a-axis shock simulation at 12 km/s and 5 ps."
    },
    {
      "file": "cluster_sizes_c_axis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster_size"
        ],
        "units": {}
      },
      "description": "Carbon cluster sizes from the c-axis shock simulation at 12 km/s and 5 ps."
    }
  ],
  "notes": "The checker will recompute histograms from these CSVs and compare to hidden gold values from the paper (e.g., 28-carbon dimer count, unreacted 14-carbon count, fragmentation patterns)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently processes your output artifacts. Each workflow stage's output contributes to a final reward on a 0–1 scale, with the scoring weights designed so that the main cluster-size comparisons carry the most weight. The verifier recomputes histograms and structural properties (such as relative abundances of different cluster sizes) from your CSV files and compares them to hidden reference values. Your score increases as your cluster distributions better match the expected patterns; full credit is attainable for results that closely reproduce the reference. Note that simply reporting a number without producing the required intermediate artifacts does not satisfy the task — the verifier bases its judgment on the actual cluster-size data you submit.
