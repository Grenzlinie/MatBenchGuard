# Orientational Order Parameter and Specific Heat of Lamellar Patterns on Flat and Spherical Surfaces

## Problem background
Particles with short-range attraction and long-range repulsion (SALR) self-assemble into lamellar stripes. This work investigates how surface curvature (flat versus spherical) influences the orientational ordering and thermal properties of such patterns. An orientational order parameter based on the moments of inertia of local orientation vectors is introduced and applied to both topologies.

## Approach
The approach uses molecular dynamics (MD) simulations with the open-source HOOMD-blue package. Two systems of equal area are simulated: (1) a flat square domain with periodic boundary conditions (toroidal, TBC) containing 975 particles, and (2) a sphere of radius 13.78σ with 900 particles constrained to its surface (SBC). Both systems employ the same SALR pair potential – a Lennard-Jones core plus a Yukawa tail (parameters: ε=1.0, σ=1.0×10⁻³, α=6, A=1.27, ξ=2, cut-off 8σ). Starting from high temperature, each system is cooled in steps down to low temperature; at each temperature the potential energy is logged. From the trajectory, structural and thermodynamic observables are computed: (i) an orientational order parameter Op, constructed by selecting particle pairs within a stripe (distance √7σ < r < 3.5σ), forming normalized vectors, including both directions, and calculating the moments of inertia of the resulting point cloud (Op = 1 − I₁/I₂); (ii) the canonical specific heat per particle c_V from the variance of the potential energy; (iii) the number of clusters M (distance cut-off r < 1.41σ); (iv) the size of the largest cluster n_max. The workflow produces temperature-dependent curves for both boundary conditions, allowing a comparison of curvature effects on orientational ordering and thermal response.

## Reproduction target
Run the two cooling simulations and produce the temperature-dependent observables. Write the results for the flat surface to `tbc_observables.csv` and for the spherical surface to `sbc_observables.csv`. Each file must contain the columns: temperature, N_clusters, n_max, Op, c_V. The goal is to obtain the Op(T) and c_V(T) curves for both geometries over the temperature range ≈0.03–0.20 and to examine how surface curvature affects the shape of these curves.

## Assets

- HOOMD-blue: https://github.com/glotzerlab/hoomd-blue

## Workflow steps

### Step 1: Run TBC MD simulations
- Role: process
- Action: Perform MD simulations of N=975 SALR particles on a square domain with side length L=51.52σ under periodic boundary conditions (toroidal), using HOOMD-blue. Use the SALR potential defined in the paper (Lennard-Jones + Yukawa with ε=1.0, σ=1.0e-3, α=6, A=1.27, ξ=2, cut-off 8σ). Gradually cool the system from kBT≈0.20 to ≈0.03, sampling intermediate temperatures. Log the potential energy at each temperature.
- Evidence: `/app/outputs/tbc_simulation.log`

### Step 2: Compute TBC observables
- Role: scored (load-bearing)
- Action: From the TBC simulation trajectory, compute for each temperature: (i) the orientational order parameter Op (select particle pairs within the same stripe satisfying √7σ < r < 3.5σ, form normalized vectors, include both directions, construct a point cloud of terminal points, compute principal moments of inertia I1≤I2, set Op = 1 - I1/I2); (ii) the canonical specific heat per particle c_V from the variance of the potential energy; (iii) the number of clusters M (cut-off r<1.41σ); (iv) the size of the largest cluster n_max. Write results to tbc_observables.csv.
- Output file: `/app/outputs/tbc_observables.csv`
- Format: csv
- Contract: temperature (float), N_clusters (int), n_max (int), Op (float), c_V (float)
- Scoring: scored by hidden verifier

### Step 3: Run SBC MD simulations
- Role: process
- Action: Perform MD simulations of N=900 SALR particles constrained to move on a sphere of radius R=13.78σ, using HOOMD-blue. Use the same SALR potential as TBC. Cool from kBT≈0.20 to ≈0.03, sampling intermediate temperatures. Log the potential energy at each temperature.
- Evidence: `/app/outputs/sbc_simulation.log`

### Step 4: Compute SBC observables
- Role: scored (load-bearing)
- Action: From the SBC simulation trajectory, compute for each temperature: (i) the orientational order parameter Op (using the same moment-of-inertia method, pair selection, and vector normalization applied in the 3D embedding space); (ii) the specific heat c_V; (iii) the number of clusters M (cut-off r<1.41σ); (iv) the size of the largest cluster n_max. Write results to sbc_observables.csv.
- Output file: `/app/outputs/sbc_observables.csv`
- Format: csv
- Contract: temperature (float), N_clusters (int), n_max (int), Op (float), c_V (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tbc_observables.csv`
- `/app/outputs/sbc_observables.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tbc_observables.csv
- path: `/app/outputs/tbc_observables.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with temperature-dependent observables (cluster counts, largest cluster size, orientational order parameter, specific heat) for the flat surface (toroidal boundary conditions).
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `N_clusters`, `n_max`, `Op`, `c_V`

### sbc_observables.csv
- path: `/app/outputs/sbc_observables.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with temperature-dependent observables for the spherical surface (spherical boundary conditions).
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `N_clusters`, `n_max`, `Op`, `c_V`

Notes: The agent must produce both CSV files. The structural checker will verify qualitative trends (sharpness of Op rise, number of c_V peaks) without requiring bit-level agreement with the paper's exact numerical values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tbc_observables.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "N_clusters",
          "n_max",
          "Op",
          "c_V"
        ]
      },
      "description": "CSV file with temperature-dependent observables (cluster counts, largest cluster size, orientational order parameter, specific heat) for the flat surface (toroidal boundary conditions)."
    },
    {
      "file": "sbc_observables.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "N_clusters",
          "n_max",
          "Op",
          "c_V"
        ]
      },
      "description": "CSV file with temperature-dependent observables for the spherical surface (spherical boundary conditions)."
    }
  ],
  "notes": "The agent must produce both CSV files. The structural checker will verify qualitative trends (sharpness of Op rise, number of c_V peaks) without requiring bit-level agreement with the paper's exact numerical values."
}
```

## How you are scored
A hidden verifier reads your two CSV files and computes a reward. It checks: (1) the files contain the required columns and a reasonable number of temperature points; (2) the structural features of the Op(T) and c_V(T) curves – specifically, whether Op rises sharply or gradually as temperature decreases, and whether c_V exhibits one or two distinct maxima. No exact numerical agreement with any reference is required. The final reward is a weighted combination of these checks.
