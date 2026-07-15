# Molecular Dynamics Analysis of Self-Reflection and Molecular Exchange in Evaporation-Condensation

## Problem background
Transport phenomena at liquid-vapor interfaces are central to many scientific and engineering processes. The condensation coefficient α quantifies the fraction of vapor molecules that condense upon colliding with the liquid surface. However, experimental values scatter widely, and the underlying molecular mechanisms remain debated. In particular, classical models treat condensation as a unimolecular process, but there is evidence that 'molecular exchange' events—where an incident vapor molecule drives another molecule out of the liquid—may also contribute. This work uses molecular dynamics (MD) simulations to directly observe and classify individual surface collision events for two pure liquids (argon and water) over a range of temperatures. The goal is to compute the self-reflection ratio, the molecular exchange ratio, and the condensation coefficient, and to understand how these quantities depend on temperature and on the nature of the fluid.

## Approach
The investigation proceeds by running microcanonical (NVE) MD simulations of a liquid slab in equilibrium with its vapor. Pure argon is modelled with a standard Lennard-Jones potential, and pure water with the TIP4P rigid model. An initial liquid slab is prepared in a periodic box; after equilibration the system naturally establishes a vapour–liquid coexistence. Long production trajectories are collected to gather sufficient statistics of surface collisions. From the trajectories, vapour molecules that approach the liquid surface are identified. Each incident event is classified by examining the fate of the incident molecule and the response of the liquid: (i) condensation — the molecule remains in the liquid; (ii) self-reflection — it bounces back into the vapour without dislodging another molecule; (iii) molecular exchange — the incident molecule strikes the surface and, within a short time window, a different molecule escapes into the vapour. The fractions of incident events that are self-reflection (β_self) and molecular exchange (β_exch) are computed, and the condensation coefficient is obtained as α = 1 − (β_self + β_exch). This analysis is repeated for several temperatures for each substance, producing a set of coefficients that characterize the surface dynamics.

## Reproduction target
For pure argon at T = 80 K, 100 K, 120 K, and for pure water at T = 350 K, 425 K, 500 K, compute the self-reflection ratio β_self, the molecular exchange ratio β_exch, and the condensation coefficient α. Report all values in the file `/app/outputs/results.csv` with one row per condition and columns: system (either 'argon' or 'water'), temperature_K, beta_self, beta_exch, alpha. The hidden verifier will check the correctness of these coefficients and will also verify that the data satisfy expected physical constraints (e.g., α = 1 − (β_self + β_exch), all ratios between 0 and 1) and that they capture a plausible temperature dependence and a non‑negligible role for the molecular exchange channel.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/download
- Lennard-Jones parameters for argon (ε=0.996 kJ/mol, σ=0.3405 nm)
- TIP4P water model parameters

## Workflow steps

### Step 1: System Setup
- Role: process
- Action: Build initial liquid slab configurations for pure argon (Lennard-Jones parameters ε=0.996 kJ/mol, σ=0.3405 nm) and pure water (TIP4P model) in a periodic box with a liquid film. Prepare the following simulation conditions: for argon, temperatures T = 80 K, 100 K, 120 K; for water, temperatures T = 350 K, 425 K, 500 K.
- Evidence: none

### Step 2: Run MD Simulations
- Role: process
- Action: Perform microcanonical (NVE) MD simulations for each system and temperature. Equilibrate and collect production trajectories of sufficient length to obtain good statistics for event counting. Save processed event data or the full trajectories for later analysis.
- Evidence: `/app/outputs/trajectory.log`

### Step 3: Compute Coefficients
- Role: scored (load-bearing)
- Action: From the trajectories, identify vapor molecules incident on the liquid-vapor interface. Classify each incident event as condensation, self-reflection, or molecular exchange using a residence-time or similar criterion. Compute β_self (fraction of incident self-reflected), β_exch (fraction molecular exchange), and α = 1 - (β_self + β_exch). Output a CSV table with one row per simulated condition.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: system (string, 'argon' or 'water'), temperature_K (float), beta_self (float), beta_exch (float), alpha (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed self-reflection ratio, molecular exchange ratio, and condensation coefficient for each system and temperature.
- schema:
  - `type`: table
  - `required_columns`: `system`, `temperature_K`, `beta_self`, `beta_exch`, `alpha`
  - `units`:
    - `temperature_K`: K
    - `beta_self`: 1
    - `beta_exch`: 1
    - `alpha`: 1

Notes: The checker will compare the reported coefficients to hidden reference values from the original study (using tolerance to account for statistical fluctuations) and verify that molecular exchange is non-zero and that the condensation coefficient decreases with increasing temperature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "temperature_K",
          "beta_self",
          "beta_exch",
          "alpha"
        ],
        "units": {
          "temperature_K": "K",
          "beta_self": "1",
          "beta_exch": "1",
          "alpha": "1"
        }
      },
      "description": "Computed self-reflection ratio, molecular exchange ratio, and condensation coefficient for each system and temperature."
    }
  ],
  "notes": "The checker will compare the reported coefficients to hidden reference values from the original study (using tolerance to account for statistical fluctuations) and verify that molecular exchange is non-zero and that the condensation coefficient decreases with increasing temperature."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.csv`. It compares the reported β_self, β_exch, and α values to independently determined reference values, using tolerances appropriate to the statistical nature of the simulations and the inevitable differences between implementations. It also checks that the data obey the required structural relations (e.g., α = 1 − (β_self + β_exch)) and that the trend in α with temperature is physically sound. The verifier combines these objective checks into a single reward score between 0 and 1. Submitting a correctly formatted CSV is necessary; the reward is primarily determined by the accuracy of the computed coefficients and the consistency of the reported trends.
