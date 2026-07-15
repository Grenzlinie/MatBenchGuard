# Angular melting temperature of small binary Coulomb clusters using MD simulation

## Problem background
Recent experiments have realized three-dimensional isotropic clusters of charged particles (Coulomb balls) in dusty plasmas. These systems exhibit rich structural and melting behaviors. For binary mixtures with two species of different charges, the ground-state configuration and mechanical stability depend on the charge ratio $\beta$ and the number of particles of each type. This work investigates how the angular melting temperature (the temperature at which angular order is lost) changes as $\beta$ is varied, and whether the transition from highly stable "magic" clusters to less stable "normal" clusters occurs sharply or gradually. Your task is to compute angular melting temperatures for a set of binary clusters and to examine the ground-state energy as a function of $\beta$ to detect possible structural phase transitions.

## Approach
The physical system consists of $N$ particles in a three-dimensional harmonic trap, interacting via unscreened Coulomb repulsion. The potential energy (in dimensionless units) is the sum of a harmonic term and pairwise Coulomb terms, with the interaction strength between unlike particles scaled by $\beta$.

You will first determine the ground-state configuration for each $(N, N_B, \beta)$ system using a combination of Monte Carlo sampling and local Newton-type minimization. Then, for the selected systems, you will perform molecular dynamics simulations: repeatedly heat the cluster, allow it to relax using the velocity Verlet algorithm, and measure the mean-squared angular displacement of neighboring particles as a function of temperature. From these curves, you will extract the angular melting temperature $T_c$ using a Lindemann-like criterion: the temperature at which the displacement deviates from its low-temperature linear trend.

Additionally, for $N=12, N_B=3$ you will compute the numerical derivative of the ground-state energy with respect to $\beta$ over a dense grid, to probe for discontinuities.

## Reproduction target
Produce two CSV files:

1. `energy_derivative.csv` for $N=12$, $N_B=3$. This file must contain columns `beta`, `E`, `dE_dbeta`, covering $\beta$ from 0.5 to 1.0 in steps of at most 0.01 (at least 51 rows). The derivative should be computed numerically from ground-state energies.

2. `tc_table.csv` containing angular melting temperatures for the following 22 parameter sets:
   - $N=12, N_B=3$ with $\beta \in \{1.0, 0.9, 0.8, 0.75, 0.65, 0.5\}$
   - $N=12, N_B=11$ with $\beta \in \{1.0, 0.8, 0.6, 0.4, 0.2\}$
   - $N=38, N_B=4$ with $\beta \in \{1.0, 0.8, 0.6, 0.5, 0.4\}$
   - $N=38, N_B=7$ with $\beta \in \{1.0, 0.9, 0.8, 0.7\}$
   - $N=38, N_B=33$ with $\beta \in \{1.0, 0.8, 0.6, 0.5, 0.4\}$

The file must have columns `N`, `NB`, `beta`, `Tc`, with one row per parameter set. All temperatures and energies are in the dimensionless units defined by the problem setup. You must implement all methods from scratch using only the listed public packages.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Ground state configuration search
- Role: process
- Action: For each (N, NB, beta) combination used in later steps (N=12,NB=3 with beta from 0.5 to 1.0 in steps of 0.01; and the specific (N,NB,beta) sets: N=12,NB=3 beta in {1.0,0.9,0.8,0.75,0.65,0.5}; N=12,NB=11 beta in {1.0,0.8,0.6,0.4,0.2}; N=38,NB=4 beta in {1.0,0.8,0.6,0.5,0.4}; N=38,NB=7 beta in {1.0,0.9,0.8,0.7}; N=38,NB=33 beta in {1.0,0.8,0.6,0.5,0.4}), find the lowest-energy equilibrium configuration using Monte Carlo simulation supplemented by the modified Newton method with the dimensionless potential energy function (harmonic trap + Coulomb repulsion with charge ratio beta). Record the atomic coordinates and total energy for each system.
- Evidence: `/app/outputs/ground_state_energies.csv`

### Step 2: First derivative of ground-state energy
- Role: scored
- Action: Using the ground-state energies E obtained for N=12, NB=3 over a dense set of beta values from 0.5 to 1.0 (step size <=0.01), compute the numerical derivative dE/dbeta. Write a CSV file with columns beta, E, dE_dbeta.
- Output file: `/app/outputs/energy_derivative.csv`
- Format: csv
- Contract: CSV with required columns: beta (float), E (float), dE_dbeta (float). At least 51 rows covering [0.5,1.0] uniformly.
- Scoring: scored by hidden verifier

### Step 3: Molecular dynamics simulation of angular displacement
- Role: process
- Action: For each (N, NB, beta) system listed in the Tc step (see below), perform heating cycles: scale velocities to increase temperature, relax using the velocity Verlet algorithm, and measure the mean-squared angular displacement (as defined in the paper using the angle between position vectors of neighboring particles) as a function of temperature. Use the ground-state configurations from the ground-state search as initial structures. Save the resulting Δα(T) curves for melting temperature analysis.
- Evidence: `/app/outputs/delta_alpha_curves.pkl`

### Step 4: Angular melting temperature Tc
- Role: scored (load-bearing)
- Action: From the Δα(T) data for each system, extract the angular melting temperature Tc using a Lindemann-like criterion: identify the temperature at which the angular displacement deviates rapidly from its low-temperature linear behavior. Produce a CSV file with columns N, NB, beta, Tc for the following systems: N=12,NB=3 beta in {1.0,0.9,0.8,0.75,0.65,0.5}; N=12,NB=11 beta in {1.0,0.8,0.6,0.4,0.2}; N=38,NB=4 beta in {1.0,0.8,0.6,0.5,0.4}; N=38,NB=7 beta in {1.0,0.9,0.8,0.7}; N=38,NB=33 beta in {1.0,0.8,0.6,0.5,0.4}.
- Output file: `/app/outputs/tc_table.csv`
- Format: csv
- Contract: CSV with required columns: N (int), NB (int), beta (float), Tc (float). Each of the specified parameter combinations appears exactly once (22 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_derivative.csv`
- `/app/outputs/tc_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_derivative.csv
- path: `/app/outputs/energy_derivative.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ground-state energy derivative curve for N=12,NB=3. The checker will verify the existence of a sharp discontinuity in dE_dbeta around beta ≈ 0.865, indicating a first-order structural phase transition.
- schema:
  - `type`: table
  - `required_columns`: `beta`, `E`, `dE_dbeta`

### tc_table.csv
- path: `/app/outputs/tc_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Angular melting temperatures for a set of binary cluster systems. The checker will compare each Tc value to the paper-reported reference within appropriate tolerances and verify overall trend patterns.
- schema:
  - `type`: table
  - `required_columns`: `N`, `NB`, `beta`, `Tc`

Notes: All temperatures and energies are reported in the paper's dimensionless units. The ground-state search and MD pipeline must be implemented from scratch using only the listed public packages; no reference code or pre-computed configurations are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_derivative.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta",
          "E",
          "dE_dbeta"
        ]
      },
      "description": "Ground-state energy derivative curve for N=12,NB=3. The checker will verify the existence of a sharp discontinuity in dE_dbeta around beta ≈ 0.865, indicating a first-order structural phase transition."
    },
    {
      "file": "tc_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "NB",
          "beta",
          "Tc"
        ]
      },
      "description": "Angular melting temperatures for a set of binary cluster systems. The checker will compare each Tc value to the paper-reported reference within appropriate tolerances and verify overall trend patterns."
    }
  ],
  "notes": "All temperatures and energies are reported in the paper's dimensionless units. The ground-state search and MD pipeline must be implemented from scratch using only the listed public packages; no reference code or pre-computed configurations are provided."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. The verifier will independently score each artifact:

- `energy_derivative.csv` is scored structurally: the verifier will examine the series `dE_dbeta` to check for a sharp discontinuity at a specific $\beta$ value, which would indicate a first-order structural phase transition. The magnitude and location of any jump, along with overall smoothness elsewhere, contribute to the score.

- `tc_table.csv` is scored by comparing your computed $T_c$ values to hidden reference values for each parameter set. The comparison uses appropriate tolerances for the domain; large deviations or incorrect trends will reduce the score. The overall pattern of $T_c$ as a function of $\beta$ and $N_B$ is also considered.

The verifier combines the scores from both artifacts (with the Tc table carrying the larger weight) into a final reward between 0 and 1. Simply reporting numbers or fabricating results without executing the required simulations will not produce correct values and will be detected.
