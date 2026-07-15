# Thermal Correlation Length Criterion for Microstructural Clustering

## Problem background
Fluids with competing short-range attractions and long-range repulsions can form equilibrium structures with intermediate-range order (IRO), including particle clusters. It has been proposed that cluster formation occurs when the thermal correlation length ξ_T—the characteristic decay length of density fluctuations encoded in the IRO pre-peak of the static structure factor S(k)—exceeds the characteristic repulsive lengthscale ξ_R. This task aims to compute ξ_T and cluster state for a model short-range attractive long-range repulsive (SL) fluid, both monodisperse and polydisperse, to investigate this relationship across multiple attraction strengths.

## Approach
We study a model SL fluid whose pair potential consists of a short-range attractive well and a long-range repulsive tail. In reduced units (length scaled by particle diameter d, energy scaled by k_BT), the potential is
ϕ_SL(r) = 4βϵ ( r^{-2α} – r^{-α}) + βA exp(–r/ξ_R) / (r/ξ_R)
with α = 100, repulsive strength βA and repulsive range ξ_R, and attractive strength βϵ. The corresponding polydisperse ternary mixture (20% small, 60% medium with d=1, 20% large) uses size shifts Δ_d = 0.158 and energy shifts Δ_ϵ = 0.25 to frustrate crystallisation.

Molecular dynamics simulations in the NVT ensemble (LAMMPS) generate equilibrium particle configurations at packing fraction φ = 0.125 with N = 2960 particles, temperature k_BT = 1.0, time-step 0.0005, and cutoff 8.0, for several βϵ values.

From the trajectories we compute the radial distribution function g(r) and numerically invert it to obtain the static structure factor S(k). The thermal correlation length ξ_T is extracted from the IRO pre-peak of S(k) by an inverse Lorentzian fit: S(k) ≈ S(k*)/[1 + (k – k*)^2 d^2 ξ_T^2], where k* is the pre-peak position.

Cluster analysis: for each configuration, we compute cluster size distributions (CSDs) using a distance cutoff equal to the attractive-well range (the first zero-crossing of ϕ_SL for r > d). A state point is classified as fluid (no CSD peak), clustered (CSD peak at an intermediate aggregate size n* with 1 ≪ n* ≪ N), or percolated (CSD peak at n* ≈ N).

## Reproduction target
Produce the following scored artifacts under /app/outputs:
  - S_k_at_peak.csv: the structure factor S(k) vs. wavenumber k for the monodisperse system at βϵ = 5.0, φ = 0.125, ξ_R = 2, βA = 0.20.
  - xi_T_monodisperse.csv: for each simulated monodisperse βϵ (at least 4.5, 5.0, 5.2; extra points are allowed), report attractive_strength (βϵ), packing_fraction (0.125), xi_T (the fitted thermal correlation length), and clustering_state (one of 'fluid', 'clustered', 'percolated').
  - xi_T_polydisperse.csv: same columns for the ternary polydisperse SL fluid at the same packing fraction and repulsive parameters, for the same βϵ values.
All computations must be based on your own MD simulations and post-processing.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/download.html
- Python scientific stack (numpy, scipy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: MD simulation of monodisperse SL fluid
- Role: process
- Action: Set up LAMMPS input for the monodisperse SL pair potential with parameters: α=100, ξ_R=2, βA=0.20, N=2960, temperature=1.0 (reduced units), time-step=0.0005, cutoff=8.0. Perform NVT simulations at packing fraction φ=0.125 for attractive strengths βϵ = 4.5, 5.0, 5.2 to generate equilibrium trajectories.
- Evidence: `/app/outputs/simulation_log_monodisperse.txt`

### Step 2: MD simulation of polydisperse SL fluid
- Role: process
- Action: Set up LAMMPS input for the ternary polydisperse mixture with composition 20% small, 60% medium (d=1), 20% large, size shift Δ_d=0.158, energy shift Δ_ϵ=0.25, and the same repulsive parameters (ξ_R=2, βA=0.20). Perform NVT simulations at φ=0.125 for βϵ = 4.5, 5.0, 5.2 to obtain equilibrium trajectories.
- Evidence: `/app/outputs/simulation_log_polydisperse.txt`

### Step 3: Compute g(r) and S(k) from monodisperse trajectories
- Role: process
- Action: For each monodisperse simulation (each βϵ), compute the radial distribution function g(r) from the particle configurations and numerically Fourier invert to obtain the static structure factor S(k).
- Evidence: none

### Step 4: Save S(k) for monodisperse at βϵ=5.0
- Role: scored
- Action: From the computed monodisperse S(k) at βϵ=5.0, φ=0.125, save the wavenumber k and S(k) data as S_k_at_peak.csv.
- Output file: `/app/outputs/S_k_at_peak.csv`
- Format: csv
- Contract: Two columns: k (float, wavenumber in units of 1/d), S(k) (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Extract ξ_T and cluster classification for monodisperse
- Role: process
- Action: For each monodisperse S(k), identify the IRO pre-peak at k*, fit S(k*)/S(k) to 1+(k−k*)² d² ξ_T² to obtain the thermal correlation length ξ_T. From the simulation configurations, compute cluster size distributions using a distance cutoff equal to the attractive well range (first zero-crossing of the pair potential for x>1), and classify each state point as fluid (no CSD peak), clustered (CSD peak at n* with 1≪n*≪N), or percolated (CSD peak at n*≃N).
- Evidence: `/app/outputs/xiT_csd_monodisperse_intermediate.json`

### Step 6: Output monodisperse ξ_T and clustering results
- Role: scored (load-bearing)
- Action: Write xi_T_monodisperse.csv containing attractive_strength (βϵ), packing_fraction (φ=0.125), xi_T, and clustering_state for each simulated monodisperse state point.
- Output file: `/app/outputs/xi_T_monodisperse.csv`
- Format: csv
- Contract: Columns: attractive_strength (float, dimensionless), packing_fraction (float, dimensionless), xi_T (float, dimensionless thermal correlation length), clustering_state (string: 'fluid', 'clustered', or 'percolated').
- Scoring: scored by hidden verifier

### Step 7: Analyze polydisperse simulations
- Role: process
- Action: For the polydisperse trajectories, compute g(r) and S(k); from each S(k) extract ξ_T via the inverse Lorentzian fit; compute cluster size distributions using the same attractive-well cutoff and classify each state point as fluid, clustered, or percolated.
- Evidence: `/app/outputs/xiT_csd_polydisperse_intermediate.json`

### Step 8: Output polydisperse ξ_T and clustering results
- Role: scored (load-bearing)
- Action: Write xi_T_polydisperse.csv with attractive_strength (βϵ), packing_fraction (φ=0.125), xi_T, and clustering_state for each simulated polydisperse state point.
- Output file: `/app/outputs/xi_T_polydisperse.csv`
- Format: csv
- Contract: Same columns as xi_T_monodisperse.csv: attractive_strength (float), packing_fraction (float), xi_T (float), clustering_state (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/S_k_at_peak.csv`
- `/app/outputs/xi_T_monodisperse.csv`
- `/app/outputs/xi_T_polydisperse.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### S_k_at_peak.csv
- path: `/app/outputs/S_k_at_peak.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Supporting evidence: static structure factor at βϵ=5.0, φ=0.125 for the monodisperse SL fluid. Used to verify the quality of the IRO pre-peak fitting.
- schema:
  - `type`: table
  - `required_columns`: `k`, `S(k)`
  - `units`:
    - `k`: 1/d (dimensionless)
    - `S(k)`: dimensionless

### xi_T_monodisperse.csv
- path: `/app/outputs/xi_T_monodisperse.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal correlation length and cluster classification for the monodisperse SL fluid at multiple attractive strengths.
- schema:
  - `type`: table
  - `required_columns`: `attractive_strength`, `packing_fraction`, `xi_T`, `clustering_state`
  - `units`:
    - `attractive_strength`: dimensionless (βϵ)
    - `packing_fraction`: dimensionless (φ)
    - `xi_T`: dimensionless (thermal correlation length)
    - `clustering_state`: string ('fluid', 'clustered', 'percolated')

### xi_T_polydisperse.csv
- path: `/app/outputs/xi_T_polydisperse.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal correlation length and cluster classification for the ternary polydisperse SL fluid at multiple attractive strengths.
- schema:
  - `type`: table
  - `required_columns`: `attractive_strength`, `packing_fraction`, `xi_T`, `clustering_state`
  - `units`:
    - `attractive_strength`: dimensionless (βϵ)
    - `packing_fraction`: dimensionless (φ)
    - `xi_T`: dimensionless (thermal correlation length)
    - `clustering_state`: string ('fluid', 'clustered', 'percolated')

Notes: The agent’s reported ξ_T values and clustering labels will be compared to paper‑reported results (hidden). The clustering_state is expected to be consistent with the ξ_T ≥ ξ_R criterion, but no reference value is given.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "S_k_at_peak.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "k",
          "S(k)"
        ],
        "units": {
          "k": "1/d (dimensionless)",
          "S(k)": "dimensionless"
        }
      },
      "description": "Supporting evidence: static structure factor at βϵ=5.0, φ=0.125 for the monodisperse SL fluid. Used to verify the quality of the IRO pre-peak fitting."
    },
    {
      "file": "xi_T_monodisperse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "attractive_strength",
          "packing_fraction",
          "xi_T",
          "clustering_state"
        ],
        "units": {
          "attractive_strength": "dimensionless (βϵ)",
          "packing_fraction": "dimensionless (φ)",
          "xi_T": "dimensionless (thermal correlation length)",
          "clustering_state": "string ('fluid', 'clustered', 'percolated')"
        }
      },
      "description": "Thermal correlation length and cluster classification for the monodisperse SL fluid at multiple attractive strengths."
    },
    {
      "file": "xi_T_polydisperse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "attractive_strength",
          "packing_fraction",
          "xi_T",
          "clustering_state"
        ],
        "units": {
          "attractive_strength": "dimensionless (βϵ)",
          "packing_fraction": "dimensionless (φ)",
          "xi_T": "dimensionless (thermal correlation length)",
          "clustering_state": "string ('fluid', 'clustered', 'percolated')"
        }
      },
      "description": "Thermal correlation length and cluster classification for the ternary polydisperse SL fluid at multiple attractive strengths."
    }
  ],
  "notes": "The agent’s reported ξ_T values and clustering labels will be compared to paper‑reported results (hidden). The clustering_state is expected to be consistent with the ξ_T ≥ ξ_R criterion, but no reference value is given."
}
```

## How you are scored
A hidden verifier will independently evaluate each output artifact by comparing your computed ξ_T values to hidden reference values and by checking the consistency of your clustering labels against the expected relationship between ξ_T and ξ_R. The verifier may also inspect intermediate evidence (simulation logs, S(k) fitting quality) to confirm that the pipeline was executed. Scoring uses tolerance windows and trend checks; simply copying known benchmark numbers will not succeed. Each scored artifact contributes a weighted share to the final reward. You must genuinely run the simulations and analysis; the verifier can detect inconsistencies that result from skipping the actual computations.
