# Frenkel–Kontorova Chain Magic Size and Friction Calculation

## Problem background
The one-dimensional Frenkel-Kontorova (FK) model captures the essential physics of nanoscale clusters sliding on a crystalline substrate. An atomic chain with harmonic nearest-neighbour springs moves in a periodic potential, creating a competition between the natural interatomic spacing and the substrate periodicity. This competition can produce a “magic size” effect: at a particular cluster size, the activation energy for diffusion is minimised, and the cluster may slide with greatly reduced friction. This task reproduces the numerical study of the magic size effect at a specific lattice misfit and interaction strength. You will compute three key quantities for cluster sizes N=7,8,9,10,11: the activation energy for diffusion, the critical depinning force under a constant external drive, and the maximum spring force during stick‑slip motion when pulled by a spring. The goal is to determine which cluster size yields the smallest values for all three quantities.

## Approach
The potential energy of the FK chain is E_t = Σ_i U0 (1 – cos(2π x_i / a)) + Σ_i (k/2)(x_{i+1} – x_i – b)^2, with a=1, U0=1, m=1. The system is specified by the dimensionless misfit b/a = 0.887 and the interaction ratio k a^2 / U0 = 800. All dynamics are at zero temperature with a linear friction coefficient μ = 3√(U0/(m a^2)). The workflow consists of four stages: 1. Energy minimisation: Find the relaxed minimum-energy configuration for each N by numerical optimisation. 2. Activation energy: Constrain one atom at a substrate potential maximum and compute the energy barrier as the difference between the maximum and minimum total energy along this constrained path. 3. Constant-force depinning: Integrate the Langevin equation with a uniform external force on all atoms. For each N, sweep the force to find the smallest value that produces sustained centre-of-mass translation (critical depinning force). 4. Spring-driven stick‑slip: Simulate dynamics where the cluster’s centre of mass is coupled to a pulling spring with constant K_s = 10 U0/a^2 moving at velocity v_s = 0.01 √(U0/m). Record the spring force time series and extract its maximum value. The results are written to three CSV files.

## Reproduction target
You must produce three CSV files:
- activation_energy_vs_N.csv: two columns, N (integer) and activation_energy (float, units of U0).
- critical_force_vs_N.csv: two columns, N (integer) and critical_force (float, units of U0/a).
- max_spring_force_vs_N.csv: two columns, N (integer) and max_spring_force (float, units of U0/a).
These files should contain the computed values for N=7,8,9,10,11. Your results will be examined to identify whether a single cluster size achieves the minimum value for all three quantities.

## Assets

- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Compute minimum energy configurations
- Role: process
- Action: For each cluster size N=7,8,9,10,11, minimize the total Frenkel-Kontorova energy (substrate potential U0*(1-cos(2π x_i/a)) and harmonic springs with equilibrium distance b) by varying atomic positions. Obtain the relaxed minimum-energy configuration without any atom constrained at a potential peak. Store these configurations as initial states for later dynamics steps.
- Evidence: `/app/outputs/min_energy_configs.json`

### Step 2: Compute activation energy for diffusion
- Role: scored (load-bearing)
- Action: Using the minimum energy configurations as starting points, compute the total energy as a function of the position of a single atom constrained at a substrate potential peak. Find the maximum and minimum energy along this path. The difference is the activation energy. Report the activation energy for each N in a CSV file.
- Output file: `/app/outputs/activation_energy_vs_N.csv`
- Format: csv
- Contract: columns: [N (int), activation_energy (float)]
- Scoring: scored by hidden verifier

### Step 3: Compute critical depinning force
- Role: scored
- Action: Integrate the Langevin equation at T=0 with friction coefficient μ=3 and a constant external force applied to all atoms. Use the minimum energy configuration as initial condition. For each N, determine the smallest force that leads to sustained center-of-mass motion after a transient. Report this critical force in a CSV file.
- Output file: `/app/outputs/critical_force_vs_N.csv`
- Format: csv
- Contract: columns: [N (int), critical_force (float)]
- Scoring: scored by hidden verifier

### Step 4: Compute maximum spring force in stick-slip motion
- Role: scored
- Action: Simulate the spring-driven Langevin dynamics with spring constant K_s=10 and pulling velocity v_s=0.01. Use the minimum energy configuration as initial condition. For each N, record the time series of the spring force and extract the maximum value during stick-slip motion. Report this maximum spring force in a CSV file.
- Output file: `/app/outputs/max_spring_force_vs_N.csv`
- Format: csv
- Contract: columns: [N (int), max_spring_force (float)]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energy_vs_N.csv`
- `/app/outputs/critical_force_vs_N.csv`
- `/app/outputs/max_spring_force_vs_N.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energy_vs_N.csv
- path: `/app/outputs/activation_energy_vs_N.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Activation energy for cluster diffusion for each cluster size N=7,8,9,10,11.
- schema:
  - `type`: table
  - `required_columns`: `N`, `activation_energy`
  - `units`:
    - `N`: dimensionless
    - `activation_energy`: U0

### critical_force_vs_N.csv
- path: `/app/outputs/critical_force_vs_N.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical depinning force under constant driving force for each cluster size N=7,8,9,10,11.
- schema:
  - `type`: table
  - `required_columns`: `N`, `critical_force`
  - `units`:
    - `N`: dimensionless
    - `critical_force`: U0/a

### max_spring_force_vs_N.csv
- path: `/app/outputs/max_spring_force_vs_N.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum spring force during stick-slip motion for each cluster size N=7,8,9,10,11.
- schema:
  - `type`: table
  - `required_columns`: `N`, `max_spring_force`
  - `units`:
    - `N`: dimensionless
    - `max_spring_force`: U0/a

Notes: The checker verifies that N=9 exhibits the smallest value among the tested sizes (magic size property) and that the magnitudes are consistent with expected physical ranges for the given model parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energy_vs_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "activation_energy"
        ],
        "units": {
          "N": "dimensionless",
          "activation_energy": "U0"
        }
      },
      "description": "Activation energy for cluster diffusion for each cluster size N=7,8,9,10,11."
    },
    {
      "file": "critical_force_vs_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "critical_force"
        ],
        "units": {
          "N": "dimensionless",
          "critical_force": "U0/a"
        }
      },
      "description": "Critical depinning force under constant driving force for each cluster size N=7,8,9,10,11."
    },
    {
      "file": "max_spring_force_vs_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "max_spring_force"
        ],
        "units": {
          "N": "dimensionless",
          "max_spring_force": "U0/a"
        }
      },
      "description": "Maximum spring force during stick-slip motion for each cluster size N=7,8,9,10,11."
    }
  ],
  "notes": "The checker verifies that N=9 exhibits the smallest value among the tested sizes (magic size property) and that the magnitudes are consistent with expected physical ranges for the given model parameters."
}
```

## How you are scored
A hidden verifier scores each output file. The scoring combines:
- Structural monotonicity check: the value for a candidate magic size N* must be strictly less than the values for N*‑1 and N*+1 (within a small tolerance to absorb numerical noise).
- Magnitude check: your computed values are compared to hidden reference values to ensure they are in the correct physical range; values that differ by more than a reasonable threshold are penalised.
The three artifacts contribute equally to the total reward. You must write the files in the exact format described; missing or incorrectly formatted files receive zero points.
