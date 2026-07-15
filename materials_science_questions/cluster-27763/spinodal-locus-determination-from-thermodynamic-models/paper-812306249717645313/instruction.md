# Scaling Exponents of a Long-Range Ising Model near the Spinodal

## Problem background
Metastable states of ferromagnetic Ising models with long-range interactions exhibit behaviour that can deviate strongly from classical nucleation theory when the system is quenched close to the mean‑field spinodal. Spinodal‑assisted nucleation theory predicts that near the spinodal the quasistatic susceptibility and the properties of nucleating droplets follow scaling laws with specific mean‑field exponents. This task investigates a two‑dimensional long‑range Ising model (LRIM) with Glauber (heat‑bath) dynamics. The goal is to compute, from Monte Carlo simulations, the scaling of the quasistatic susceptibility, the mean percolation cluster size, the radius of gyration of nucleating droplets, and the mass of nucleating droplets as a function of the reduced external field for several interaction ranges.

## Approach
The core approach is to implement a two‑dimensional LRIM on a square lattice of linear size L=150 with periodic boundary conditions. Each spin interacts ferromagnetically with all spins inside a square interaction box of side length 2R+1; the coupling constant is J = 1/q where q = (2R+1)^2 − 1. The system evolves under Glauber heat‑bath dynamics. Simulations are performed at temperature T = (4/9) T_c for four interaction ranges R ∈ {5, 7, 15, 25}.

Near the spinodal the external field H is varied so that the system remains metastable. The reduced field ΔH = (H_s − H)/H_s is used, where H_s is the spinodal field obtained from the mean‑field equation of state. For each (R, ΔH) a long metastable run (1500 Monte Carlo steps per spin) is performed. From these runs the quasistatic susceptibility χ_qs is computed as N(⟨m²⟩_ms − ⟨m⟩_ms²), where m is the magnetization per spin and the averages are taken only over metastable configurations.

Up‑spins are then mapped to a correlated bond percolation problem: every pair of neighbouring up‑spins (within the interaction range) is connected with probability p = 1 − exp(−4 J β (1−ρ_s)), where ρ_s is the density of up‑spins at the spinodal. The mean cluster size ⟨s⟩ = Σ_s s² n_s is measured for each (R, ΔH).

For deeper quenches that lead to rapid nucleation (within ~20–40 MCS), separate simulations are performed. The nucleating droplet is identified using the percolation mapping: it is taken as the largest percolation cluster at the first Monte Carlo step in which it becomes the largest cluster in the system. Its radius of gyration R_G is measured and normalized by R; its mass is the number of up‑spins it contains. These measurements are recorded for each (R, ΔH) at which nucleation is observed.

## Reproduction target
Produce the following four scored CSV files under /app/outputs:

- `chi_qs_vs_DeltaH.csv`: quasistatic susceptibility χ_qs vs reduced field ΔH for each R.
- `mean_cluster_size_vs_DeltaH.csv`: mean percolation cluster size ⟨s⟩ vs ΔH for each R.
- `droplet_radius_vs_DeltaH.csv`: normalized radius of gyration R_G/R vs ΔH for each R.
- `droplet_mass_vs_DeltaH.csv`: nucleating droplet mass M_ND vs ΔH for each R.

Each file must contain rows for the interaction ranges R=5,7,15,25 at multiple values of ΔH. The hidden verifier will perform a log‑log linear regression (log10(quantity) vs log10(Delta_H)) separately for each R and extract the scaling exponent (slope). The goal is to obtain slopes that approach the mean‑field predictions as R increases, and for the largest R to lie within a predefined tolerance of the predicted exponents.

## Assets

- Python scientific computing stack (NumPy, SciPy, Matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Curie-Weiss partition function evaluation (reference)
- Role: process
- Action: Numerically evaluate the Curie-Weiss partition function for N=10^7 spins to obtain the mean-field quasistatic susceptibility χ_qs as a function of ΔH. This produces a reference curve confirming the asymptotic slope γ=1/2.
- Evidence: `/app/outputs/curie_weiss_reference.log`

### Step 2: Metastable LRIM Monte Carlo simulations
- Role: process
- Action: Implement the 2D LRIM with periodic boundaries, lattice size L=150, coupling J=1/q, q=(2R+1)^2-1, and Glauber heat-bath dynamics. For each interaction range R=5,7,15,25 run simulations at several external fields H in the metastable regime, each for 1500 MCS per spin. Record spin configurations or bulk magnetization statistics as needed.
- Evidence: `/app/outputs/metastable_simulations.log`

### Step 3: Quasistatic susceptibility measurement
- Role: scored (load-bearing)
- Action: From the metastable simulation results compute the quasistatic susceptibility χ_qs = N(⟨m²⟩_ms − ⟨m⟩_ms²) for each (R, ΔH) and write the data.
- Output file: `/app/outputs/chi_qs_vs_DeltaH.csv`
- Format: csv
- Contract: columns: R (int), Delta_H (float), chi_qs (float)
- Scoring: scored by hidden verifier

### Step 4: Mean percolation cluster size computation
- Role: scored (load-bearing)
- Action: From the same metastable configurations, map up-spins to percolation sites and bond with probability p=1-exp(-4Jβ(1-ρ_s)). Compute the mean cluster size ⟨s⟩ = Σ_s s² n_s for each (R, ΔH) and write the data.
- Output file: `/app/outputs/mean_cluster_size_vs_DeltaH.csv`
- Format: csv
- Contract: columns: R (int), Delta_H (float), mean_cluster_size (float)
- Scoring: scored by hidden verifier

### Step 5: Nucleation LRIM simulations for droplet analysis
- Role: process
- Action: Run LRIM simulations at external fields H deep enough to induce nucleation within ~20-40 MCS, for each R. Record spin configurations at the time of droplet formation.
- Evidence: `/app/outputs/nucleation_simulations.log`

### Step 6: Nucleating droplet radius of gyration
- Role: scored (load-bearing)
- Action: From the nucleation runs, identify the nucleating droplet as the largest percolation cluster at the first Monte Carlo step it dominates. Measure its radius of gyration R_G, normalize by R, and write the data.
- Output file: `/app/outputs/droplet_radius_vs_DeltaH.csv`
- Format: csv
- Contract: columns: R (int), Delta_H (float), radius_of_gyration_over_R (float)
- Scoring: scored by hidden verifier

### Step 7: Nucleating droplet mass
- Role: scored (load-bearing)
- Action: For the same identified droplets, compute the mass (number of up-spins) and write the data.
- Output file: `/app/outputs/droplet_mass_vs_DeltaH.csv`
- Format: csv
- Contract: columns: R (int), Delta_H (float), mass (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chi_qs_vs_DeltaH.csv`
- `/app/outputs/mean_cluster_size_vs_DeltaH.csv`
- `/app/outputs/droplet_radius_vs_DeltaH.csv`
- `/app/outputs/droplet_mass_vs_DeltaH.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi_qs_vs_DeltaH.csv
- path: `/app/outputs/chi_qs_vs_DeltaH.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Quasistatic susceptibility as a function of reduced field for each interaction range. The checker performs log-log linear regression and compares the slope to the predicted mean-field exponent γ=1/2.
- schema:
  - `type`: table
  - `required_columns`: `R`, `Delta_H`, `chi_qs`
  - `units`:
    - `Delta_H`: dimensionless
    - `chi_qs`: dimensionless

### mean_cluster_size_vs_DeltaH.csv
- path: `/app/outputs/mean_cluster_size_vs_DeltaH.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mean percolation cluster size vs reduced field. The checker regresses the slope and compares to -1/2.
- schema:
  - `type`: table
  - `required_columns`: `R`, `Delta_H`, `mean_cluster_size`
  - `units`:
    - `Delta_H`: dimensionless
    - `mean_cluster_size`: dimensionless

### droplet_radius_vs_DeltaH.csv
- path: `/app/outputs/droplet_radius_vs_DeltaH.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized radius of gyration of nucleating droplets vs reduced field. The slope is compared to the predicted exponent ν=1/4.
- schema:
  - `type`: table
  - `required_columns`: `R`, `Delta_H`, `radius_of_gyration_over_R`
  - `units`:
    - `Delta_H`: dimensionless
    - `radius_of_gyration_over_R`: dimensionless

### droplet_mass_vs_DeltaH.csv
- path: `/app/outputs/droplet_mass_vs_DeltaH.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mass of nucleating droplets vs reduced field. The slope is compared to the predicted exponent -1.
- schema:
  - `type`: table
  - `required_columns`: `R`, `Delta_H`, `mass`
  - `units`:
    - `Delta_H`: dimensionless
    - `mass`: dimensionless

Notes: The solver must implement the LRIM simulation, Glauber heat-bath dynamics, percolation mapping, and cluster analysis. All raw data is produced by running the simulations; no external datasets are needed. The checker recomputes log-log slopes from the submitted CSV files and compares them to theoretical mean-field predictions within tolerance, also verifying monotonic convergence as R increases.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chi_qs_vs_DeltaH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "Delta_H",
          "chi_qs"
        ],
        "units": {
          "Delta_H": "dimensionless",
          "chi_qs": "dimensionless"
        }
      },
      "description": "Quasistatic susceptibility as a function of reduced field for each interaction range. The checker performs log-log linear regression and compares the slope to the predicted mean-field exponent γ=1/2."
    },
    {
      "file": "mean_cluster_size_vs_DeltaH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "Delta_H",
          "mean_cluster_size"
        ],
        "units": {
          "Delta_H": "dimensionless",
          "mean_cluster_size": "dimensionless"
        }
      },
      "description": "Mean percolation cluster size vs reduced field. The checker regresses the slope and compares to -1/2."
    },
    {
      "file": "droplet_radius_vs_DeltaH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "Delta_H",
          "radius_of_gyration_over_R"
        ],
        "units": {
          "Delta_H": "dimensionless",
          "radius_of_gyration_over_R": "dimensionless"
        }
      },
      "description": "Normalized radius of gyration of nucleating droplets vs reduced field. The slope is compared to the predicted exponent ν=1/4."
    },
    {
      "file": "droplet_mass_vs_DeltaH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "Delta_H",
          "mass"
        ],
        "units": {
          "Delta_H": "dimensionless",
          "mass": "dimensionless"
        }
      },
      "description": "Mass of nucleating droplets vs reduced field. The slope is compared to the predicted exponent -1."
    }
  ],
  "notes": "The solver must implement the LRIM simulation, Glauber heat-bath dynamics, percolation mapping, and cluster analysis. All raw data is produced by running the simulations; no external datasets are needed. The checker recomputes log-log slopes from the submitted CSV files and compares them to theoretical mean-field predictions within tolerance, also verifying monotonic convergence as R increases."
}
```

## How you are scored
A hidden verifier reads each CSV file you produce. For each file it groups the data by R, performs a linear regression of log10(quantity) against log10(Delta_H), and extracts the slope. It compares the slope for each R to a reference value (not revealed to you) and checks that (i) the slope for the largest R (R=25) is within a specified tolerance of the predicted mean‑field exponent, and (ii) the slopes become closer to the predicted value as R gets larger (monotonic convergence). A score is assigned per file based on how many of these checks are satisfied, and the final reward is a weighted sum of the per‑file scores. Simply reporting a number is not enough; the verifier recomputes the slopes from your raw data. Ensure your CSV files contain accurate measured values and cover a sufficient range of ΔH for a meaningful regression.
