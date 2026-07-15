# Kinetic Correlations of High-Propensity Lithium Ions in Lithium Metasilicate Glass

## Problem background
Lithium metasilicate (Li₂SiO₃) glass is a model system for studying ionic conduction in structurally disordered solids, with potential implications for solid-state battery electrolytes. The mechanisms responsible for lithium-ion mobility remain under debate: some models emphasize random percolation over static energy barriers, others highlight strong ion-ion correlations, and yet others stress the coupling between mobile ions and the glassy network. A complete understanding requires quantifying how the motions of highly mobile lithium ions are kinetically correlated with their neighboring lithium ions and with the surrounding oxygen network. This task addresses that question by computationally measuring the normalized kinetic correlation coefficients between lithium ions and their nearest neighbors, and determining the fraction of high-propensity lithium ions that exhibit above-average correlation with each species.

## Approach
The work uses classical Molecular Dynamics (MD) simulations of Li₂SiO₃ glass with a well-established Gilbert-Ida interatomic potential. After preparing an equilibrated glass structure at 700 K, the Isoconfigurational Ensemble (IC) method is applied: a large number of short, independent NVE trajectories are launched from the same initial atomic configuration but with different randomized initial velocities. The per-ion propensity — the mean squared displacement over the ensemble — is computed at the heterogeneity time t* (~40 ps), when lithium dynamics deviate most strongly from Gaussian behavior. Lithium ions with propensity exceeding a fixed threshold (1.96 Å², corresponding to a displacement larger than half the first Li-Li radial distribution function peak) are categorized as high-propensity (LiHP). For every Li-Li and Li-O pair within the first coordination shells (cutoffs determined from the respective partial radial distribution functions), a Pearson-like correlation coefficient K_{i-j} is calculated from the IC displacements. From these, each lithium ion's average correlation to its nearest Li and O neighbors is derived, then normalized by the system-wide mean to obtain K*_{Li-Li} and K*_{Li-O}. The analysis then determines whether LiHP ions exhibit above-average K*_{Li-Li} and K*_{Li-O} more frequently than expected by chance, thereby testing the hypothesis of cooperative lithium motion.

## Reproduction target
From a fully specified lithium metasilicate glass system (3456 atoms: 1152 Li, 570 Si, 1728 O at the experimental density), execute the complete MD preparation protocol: high-temperature equilibration, controlled cooling to 700 K, and final equilibration. Then, using the final configuration, generate 1000 isoconfigurational NVE trajectories, each of 40 ps duration, with initial velocities drawn from the Maxwell-Boltzmann distribution at 700 K. Post-process all trajectories to compute for every lithium ion its propensity at 40 ps, the normalized kinetic correlations K*_{Li-Li} and K*_{Li-O} (as defined in the approach), and a boolean flag indicating whether the ion is a high-propensity lithium ion (propensity > 1.96 Å²). Store these results as a CSV file with columns: li_id (int), propensity (float, Å²), K_star_LiLi (float), K_star_LiO (float), is_lihp (bool). The primary quantity of interest is the fraction of LiHPs that exhibit a nearest-lithium normalized correlation K*_{Li-Li} greater than 1. A secondary quantity is the analogous fraction with K*_{Li-O} > 1 for LiHPs.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- Gilbert-Ida interatomic potential parameters for Li₂SiO₃ (Habasaki 1992)

## Workflow steps

### Step 1: System Construction and High-Temperature Equilibration
- Role: process
- Action: Create a cubic simulation box with 3456 atoms (1152 Li, 570 Si, 1728 O) at the experimental density of lithium metasilicate glass. Assign Maxwell-Boltzmann velocities at 3000 K and equilibrate in the NVE ensemble for 2 ns using LAMMPS with the Gilbert-Ida potential.
- Evidence: `/app/outputs/equilibration_log.txt`

### Step 2: Glass Formation via Cooling
- Role: process
- Action: Cool the system from 3000 K to 700 K in two steps (3000→2000 K and 2000→700 K) using NPT ensemble with a linear temperature ramp, each step over 2 ns. Include NPT equilibration runs at 2000 K and 700 K.
- Evidence: `/app/outputs/cooling_log.txt`

### Step 3: Final Equilibration at 700 K
- Role: process
- Action: At 700 K, perform final equilibration: alternating NVE/NVT runs of 100 ps each for 2 ns, then a 2 ns NVE run. The final configuration serves as the starting point for IC trajectories.
- Evidence: `/app/outputs/final_config.restart`

### Step 4: Isoconfigurational Ensemble Generation
- Role: process
- Action: From the final configuration, launch 1000 independent NVE trajectories, each 40 ps long, with initial velocities randomly drawn from the Maxwell-Boltzmann distribution at 700 K. Record atomic positions periodically for analysis.
- Evidence: `/app/outputs/ic_traj_0.dump`

### Step 5: Compute Propensity and Normalized Correlations for Lithium Ions
- Role: scored (load-bearing)
- Action: From the IC trajectories, compute for every lithium ion its propensity (mean squared displacement over the IC ensemble at t=40 ps). Identify high-propensity lithium ions (LiHPs) as those with propensity > 1.96 Å². For all Li-Li and Li-O pairs within the first coordination shells, calculate Pearson-like correlation coefficients K_{i-j} from the IC displacements, then compute for each Li the average correlation to nearest Li and O neighbours, the global averages, and the normalized K*_{Li-Li} and K*_{Li-O}. Output a CSV file containing per-lithium data.
- Output file: `/app/outputs/step_05_results.csv`
- Format: csv
- Contract: Columns: li_id (int), propensity (float, Å²), K_star_LiLi (float), K_star_LiO (float), is_lihp (bool). Approximately 1152 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_05_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_05_results.csv
- path: `/app/outputs/step_05_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Per-lithium data: propensity, normalized Li-Li and Li-O kinetic correlations, and LiHP flag. The fraction of LiHPs with K_star_LiLi > 1 is extracted and compared to the paper-reported reference.
- schema:
  - `type`: table
  - `required_columns`: `li_id`, `propensity`, `K_star_LiLi`, `K_star_LiO`, `is_lihp`
  - `units`:
    - `propensity`: Å²

Notes: The hidden checker will read this CSV, validate the columns, compute the fraction of rows where is_lihp is True and K_star_LiLi > 1.0, and compare to the paper’s reported value (~0.85) with an appropriate tolerance. An optional secondary check may verify that the fraction of LiHPs with K_star_LiO > 1.0 is not predominantly above average.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_05_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "li_id",
          "propensity",
          "K_star_LiLi",
          "K_star_LiO",
          "is_lihp"
        ],
        "units": {
          "propensity": "Å²"
        }
      },
      "description": "Per-lithium data: propensity, normalized Li-Li and Li-O kinetic correlations, and LiHP flag. The fraction of LiHPs with K_star_LiLi > 1 is extracted and compared to the paper-reported reference."
    }
  ],
  "notes": "The hidden checker will read this CSV, validate the columns, compute the fraction of rows where is_lihp is True and K_star_LiLi > 1.0, and compare to the paper’s reported value (~0.85) with an appropriate tolerance. An optional secondary check may verify that the fraction of LiHPs with K_star_LiO > 1.0 is not predominantly above average."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your output files. For the scored stage (Step 5), the verifier loads `step_05_results.csv`, validates the schema, and computes the fraction of rows where `is_lihp` is True and `K_star_LiLi > 1.0`, and optionally the fraction where `is_lihp` is True and `K_star_LiO > 1.0`. These fractions are compared to reference values derived from the original study using tolerances that account for stochastic variations and implementation differences. The reward for this stage depends on how closely your computed fractions match the expected values. The total reward is a weighted combination of the scores across all scored workflow stages. To achieve a high score, you must faithfully execute the simulation pipeline and produce a CSV whose derived fractions fall within the acceptable tolerance window; simply reporting a known value without genuine computation will not succeed.
