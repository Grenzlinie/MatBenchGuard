# Spin-glass Transition and Quasilong-range Order in Site-diluted Dipolar Ising Model via Monte Carlo

## Problem background
The site-diluted dipolar Ising model describes magnetic systems where Ising spins are randomly placed on a fraction of sites of a simple cubic lattice and interact via long-range dipole-dipole forces. Disorder and frustration are inherent in this model, making it a candidate for spin-glass behaviour. An open question is whether such a model exhibits a spin-glass phase at low concentrations, and if so, what is the transition temperature and the nature of the glassy order (e.g., quasi-long-range order vs conventional spin-glass order). Reproducing the transition temperature and the signature of quasi-long-range order for a specific concentration x=0.35 is the target of this task.

## Approach
To probe the spin-glass transition, we use parallel tempered Monte Carlo (TMC) simulations. The TMC method allows the system to overcome free-energy barriers by exchanging configurations between replicas at nearby temperatures. We simulate the Ising model on a cubic lattice with periodic boundary conditions, with a given concentration of occupied sites x=0.35, for several linear system sizes L=4,6,8,10. The Edwards-Anderson overlap parameter q measures the similarity of spin configurations in two independent replicas. A finite-size correlation-length ratio ξ_L/L is computed from the overlap using its Fourier transform at the smallest non-zero wavevector; this ratio is expected to be scale-invariant at the transition temperature, allowing the determination of T_sg from the crossing of curves for different L. Below the transition, the variance of the overlap q2 should decay algebraically with the number of spins N, with an exponent that characterises the nature of the order. The task is to implement this simulation and analysis to compute the transition temperature and the exponent.

## Reproduction target
For the site-diluted dipolar Ising model at concentration x=0.35, run parallel tempered Monte Carlo simulations for sizes L=4,6,8,10 over a broad temperature range. Compute the correlation-length ratio ξ_L/L as a function of scaled temperature T/x and output the data in xi_over_L_vs_T.csv. Compute the mean squared overlap q2 as a function of the number of dipoles N for at least two low temperatures, and output in q2_vs_N.csv. From these data, determine the spin-glass transition temperature T_sg (or the scaled transition temperature T_sg/x) and the exponent η characterising the algebraic decay of q2, and report these in summary_results.json. The hidden verifier will then compare your extracted T_sg/x and η against the paper's hidden reference values, and also check the raw data for consistency.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Run parallel tempered Monte Carlo simulations
- Role: process
- Action: Implement the site-diluted parallel-axis dipolar Ising model on a simple cubic lattice with periodic boundary conditions (Hamiltonian with dipolar interactions). Apply parallel tempered Monte Carlo for concentration x=0.35, system sizes L=4,6,8,10, over a temperature range covering the transition (suggested T/x from 0.1 to 2.0). Measure the Edwards-Anderson overlap q and compute the correlation length ξ_L (using the relation involving q**2 and the Fourier component q(k) at k=(2π/L,0,0)) after proper equilibration. Perform disorder averaging over multiple realizations.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Output xi_over_L_vs_T.csv
- Role: scored (load-bearing)
- Action: From the simulation data, compute the ensemble-averaged finite-size correlation-length ratio ξ_L/L for each (L,T) and compile a CSV with columns T_div_x, L, xi_over_L, error. The CSV must contain data for all four L at enough temperature points to resolve the crossing region.
- Output file: `/app/outputs/xi_over_L_vs_T.csv`
- Format: csv
- Contract: columns: T_div_x (float), L (int), xi_over_L (float), error (float).
- Scoring: scored by hidden verifier

### Step 3: Output q2_vs_N.csv
- Role: scored
- Action: From the simulation data, extract the mean squared overlap q2 as a function of number of dipoles N (which depends on L and the occupancy fraction x) for at least two temperatures below T_sg (e.g., T/x=0.286 and 0.571). Write a CSV with columns T, L, N, q2, error.
- Output file: `/app/outputs/q2_vs_N.csv`
- Format: csv
- Contract: columns: T (float), L (int), N (int), q2 (float), error (float).
- Scoring: scored by hidden verifier

### Step 4: Extract T_sg and η (summary_results.json)
- Role: scored
- Action: Analyze xi_over_L_vs_T.csv to determine the crossing temperature T_sg/x (e.g., by finding the temperature where the spread of ξ_L/L across L is minimized, or by pairwise intersections) and fit q2_vs_N.csv data to q2 ~ N^{-p} to obtain the exponent p and compute η = 3p - 1. Write the results as a JSON file.
- Output file: `/app/outputs/summary_results.json`
- Format: json
- Contract: JSON object with keys: Tsg_over_x (float), Tsg (float), eta (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/xi_over_L_vs_T.csv`
- `/app/outputs/q2_vs_N.csv`
- `/app/outputs/summary_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### xi_over_L_vs_T.csv
- path: `/app/outputs/xi_over_L_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Finite-size correlation-length ratio vs scaled temperature for x=0.35.
- schema:
  - `type`: table
  - `required_columns`: `T_div_x`, `L`, `xi_over_L`, `error`

### q2_vs_N.csv
- path: `/app/outputs/q2_vs_N.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Overlap variance vs system size for selected low temperatures.
- schema:
  - `type`: table
  - `required_columns`: `T`, `L`, `N`, `q2`, `error`

### summary_results.json
- path: `/app/outputs/summary_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Derived spin-glass transition temperature and quasi-long-range order exponent.
- schema:
  - `type`: object
  - `required`:
    - `Tsg_over_x`: float
    - `Tsg`: float
    - `eta`: float

Notes: The checker will recompute the crossing temperature from xi_over_L_vs_T.csv and the decay exponent from q2_vs_N.csv, then compare against reference values with appropriate tolerances. The summary_results.json is used as a secondary check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "xi_over_L_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_x",
          "L",
          "xi_over_L",
          "error"
        ]
      },
      "description": "Finite-size correlation-length ratio vs scaled temperature for x=0.35."
    },
    {
      "file": "q2_vs_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "L",
          "N",
          "q2",
          "error"
        ]
      },
      "description": "Overlap variance vs system size for selected low temperatures."
    },
    {
      "file": "summary_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Tsg_over_x": "float",
          "Tsg": "float",
          "eta": "float"
        }
      },
      "description": "Derived spin-glass transition temperature and quasi-long-range order exponent."
    }
  ],
  "notes": "The checker will recompute the crossing temperature from xi_over_L_vs_T.csv and the decay exponent from q2_vs_N.csv, then compare against reference values with appropriate tolerances. The summary_results.json is used as a secondary check."
}
```

## How you are scored
The hidden verifier will independently recompute the crossing temperature from your xi_over_L_vs_T.csv data, fit q2_vs_N.csv to a power law to obtain the exponent, and compare the derived scalars to hidden values from the original paper. It also checks your summary_results.json for consistency with these analyses. Each output file (xi_over_L_vs_T.csv, q2_vs_N.csv, summary_results.json) contributes a fraction to the final score, weighted towards the ability to reproduce the transition temperature and the decay exponent. Submitting accurate simulation data and careful analysis is essential; mere guesswork will not suffice.
