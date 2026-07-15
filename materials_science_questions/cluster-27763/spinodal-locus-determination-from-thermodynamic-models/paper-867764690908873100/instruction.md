# Spinodal phase behavior and power-law aggregation kinetics of a three-state protein model

## Problem background
Proteins can misfold and aggregate, a process implicated in many diseases. This task studies the competition between single-protein folding and inter-protein aggregation using a three-state lattice-gas model. The model distinguishes unfolded (U), misfolded (M), and folded (F) states and includes attractive interactions between misfolded proteins. The thermodynamic phase diagram and non-equilibrium aggregation kinetics are of primary interest: the model yields a spinodal line and a distribution of aggregate sizes whose early-time form is expected to follow a power law. Your job is to compute the mean-field spinodal/coexistence densities and the power-law exponent of the early-time aggregate size distribution.

## Approach
The analysis combines mean-field theory and dynamic Monte Carlo simulations. Mean-field treatment: starting from the three-state lattice Hamiltonian, you derive the grand potential density, minimize it to obtain constitutive relations, and numerically solve for the spinodal condition (determinant of Hessian = 0) and the coexistence curve (Maxwell equal-pressure construction). This yields the coexistence and spinodal densities as functions of temperature. For kinetics, you implement a 3D lattice dynamic Monte Carlo simulation with local state-change moves (U ↔ F, U ↔ M, etc.) and diffusion moves. The system is initialized entirely in the unfolded state and quenched to a metastable condition (protocol 3: density = 15.67 mM, temperature below the critical point and above the folding pseudo-transition temperature). At an early simulation time, before the system reaches a steady state, you record the cluster-size distribution of misfolded proteins and fit a power law to the small-aggregate region to extract the characteristic exponent.

## Reproduction target
Compute the mean-field spinodal and coexistence densities at a range of temperatures spanning the critical point, and verify that the critical temperature (location of the maximum spinodal density) and the relative ordering of spinodal densities at low vs. high temperature exhibit the expected behavior. Perform dynamic Monte Carlo simulation for the specified quench protocol and extract the power-law exponent describing the early-time cluster size distribution; report this exponent as a single number. Your outputs must be placed in the specified files under `/app/outputs` and will be compared against hidden reference criteria.

## Assets

- Python scientific computing environment: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Mean-field calculation of phase diagram and spinodal
- Role: scored
- Action: Derive the grand potential density from the three-state lattice Hamiltonian, minimize to obtain constitutive relations, and numerically solve for the spinodal condition (determinant of Hessian = 0) and coexistence (equal-pressure Maxwell construction) as functions of temperature. Output the computed coexistence densities (low/high) and spinodal densities (low/high) for a range of temperatures spanning the critical point.
- Output file: `/app/outputs/mean_field_spinodal_coexistence.csv`
- Format: csv
- Contract: type=table; columns={'T': 'float (temperature in J/kB)', 'rho_coex_low': 'float (low coexistence density)', 'rho_coex_high': 'float (high coexistence density)', 'rho_spin_low': 'float (low spinodal density)', 'rho_spin_high': 'float (high spinodal density)'}
- Scoring: scored by hidden verifier

### Step 2: Dynamic Monte Carlo simulation of aggregation kinetics
- Role: process
- Action: Implement the 3D lattice model with the given parameters. Initialize all proteins in the unfolded (U) state, quench to the metastable condition corresponding to protocol 3 (density = 15.67 mM, temperature below Tc and above Tf, e.g. T ≈ 0.5 J). Run dynamic Monte Carlo with state-change and diffusion moves. Record cluster sizes of misfolded (M) proteins at an early simulation time (e.g., a few thousand MCS) before the source/sink steady state sets in.
- Evidence: `/app/outputs/early_cluster_sizes.csv`

### Step 3: Extract power-law exponent from early-time aggregate size distribution
- Role: scored (load-bearing)
- Action: From the recorded early-time cluster-size distribution, fit a power law P(n) ~ n^(-tau) to the small-aggregate region (e.g., n from 1 up to a cutoff). Extract the exponent tau and write it to a text file.
- Output file: `/app/outputs/power_law_exponent.txt`
- Format: txt
- Contract: type=number; description=single float value; the fitted power-law exponent tau
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mean_field_spinodal_coexistence.csv`
- `/app/outputs/power_law_exponent.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mean_field_spinodal_coexistence.csv
- path: `/app/outputs/mean_field_spinodal_coexistence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Mean-field spinodal and coexistence densities as a function of temperature, computed from the lattice model constitutive relations.
- schema:
  - `required_columns`: `T`, `rho_coex_low`, `rho_coex_high`, `rho_spin_low`, `rho_spin_high`
  - `columns`:
    - `T`: float (temperature in J/kB)
    - `rho_coex_low`: float (low coexistence density)
    - `rho_coex_high`: float (high coexistence density)
    - `rho_spin_low`: float (low spinodal density)
    - `rho_spin_high`: float (high spinodal density)

### power_law_exponent.txt
- path: `/app/outputs/power_law_exponent.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Power-law exponent of the early-time aggregate size distribution, fitted from dynamic Monte Carlo simulation.
- schema:
  - `type`: number
  - `description`: fitted power-law exponent tau

Notes: The mean-field spinodal CSV is checked for structural properties (critical temperature and reentrance) rather than exact numeric match. The power-law exponent is compared to a hidden reference value with an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mean_field_spinodal_coexistence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "T",
          "rho_coex_low",
          "rho_coex_high",
          "rho_spin_low",
          "rho_spin_high"
        ],
        "columns": {
          "T": "float (temperature in J/kB)",
          "rho_coex_low": "float (low coexistence density)",
          "rho_coex_high": "float (high coexistence density)",
          "rho_spin_low": "float (low spinodal density)",
          "rho_spin_high": "float (high spinodal density)"
        }
      },
      "description": "Mean-field spinodal and coexistence densities as a function of temperature, computed from the lattice model constitutive relations."
    },
    {
      "file": "power_law_exponent.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "number",
        "description": "fitted power-law exponent tau"
      },
      "description": "Power-law exponent of the early-time aggregate size distribution, fitted from dynamic Monte Carlo simulation."
    }
  ],
  "notes": "The mean-field spinodal CSV is checked for structural properties (critical temperature and reentrance) rather than exact numeric match. The power-law exponent is compared to a hidden reference value with an appropriate tolerance."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s output artifact and combines them by weight into a final reward. For `mean_field_spinodal_coexistence.csv`, it checks structural properties: the critical temperature location and the reentrance of the low-density spinodal line. For `power_law_exponent.txt`, it compares your reported exponent to a hidden reference value with an appropriate tolerance. Only the artifacts you produce are evaluated; merely quoting numbers from the paper is insufficient and will not earn credit.
