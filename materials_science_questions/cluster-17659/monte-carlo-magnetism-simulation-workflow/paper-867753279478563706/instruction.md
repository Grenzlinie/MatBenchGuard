# Simulating magnetization dynamics in a 1D layered spin chain

## Problem background
Layered magnetic materials with strong intra-layer exchange and long-range dipolar interactions can be reduced to an effective one-dimensional chain of classical spins. In this model, each spin represents a whole ferromagnetic layer, and the Hamiltonian includes hard-axis anisotropies, nearest-neighbor exchange, and mean-field terms from the long-range part of dipolar forces. The model predicts a second-order phase transition and spontaneous magnetization reversals below a critical energy. This task addresses the numerical simulation of the spin-chain dynamics at two energies to examine the magnetization behaviour.

## Approach
The effective one-dimensional spin chain Hamiltonian is simulated by numerically integrating the torque equations of motion. The system consists of N identical classical spins with a large out-of-plane anisotropy, a smaller in-plane anisotropy, an interlayer exchange coupling, and all-to-all mean-field interactions along the easy axis. The equations are simplified by noting that the out-of-plane component is slaved to the in-plane angles. The resulting coupled differential equations are integrated using a standard ODE solver (e.g., Runge-Kutta). Two distinct total energies are prepared: one below the predicted critical energy and one above it. For each energy, the dynamics is evolved for a long time interval, the initial transient is discarded, and the dimensionless magnetization (the average of the z components of the spins) is recorded as a function of time.

## Reproduction target
Implement the effective 1D spin chain model for N=100 layers with parameters B_x=15, B_y=0.2, ω_ex=0.3 (in units of ω_M=1, i.e., ω_M=1). Simulate the dynamics at total dimensionless energies ε=0.2 and ε=0.4, each for at least 1×10^5 dimensionless time units. After discarding the first 10% of the time series as transient, write the dimensionless time and the dimensionless magnetization m(t) = (1/N) Σ s_J^z(t) to two CSV files: `/app/outputs/magnetization_low_energy.csv` and `/app/outputs/magnetization_high_energy.csv`. The simulation outputs will be evaluated based on structural properties of the magnetization time series; ensure the implementation faithfully reproduces the model dynamics.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Simulate spin chain at low energy (ε=0.2)
- Role: scored (load-bearing)
- Action: Implement the effective 1D spin chain model (Hamiltonian with parameters N=100 layers, B_x=15, B_y=0.2, ω_ex=0.3, ω_M=1; torque equations). Initialize spins near the +z direction with small perturbations. Set total energy ε=0.2. Integrate equations of motion for at least 1e5 dimensionless time units, record magnetization m(t) at regular intervals. Discard the first 10% of the time series as transient and write the remaining time and magnetization to magnetization_low_energy.csv.
- Output file: `/app/outputs/magnetization_low_energy.csv`
- Format: csv
- Contract: CSV file with header. Columns: time (float, dimensionless time), magnetization (float, dimensionless magnetization m = (1/N) Σ s_J^z). One row per output timestep after equilibration.
- Scoring: scored by hidden verifier

### Step 2: Simulate spin chain at high energy (ε=0.4)
- Role: scored (load-bearing)
- Action: Using the same model and implementation, set total energy ε=0.4. Simulate and record magnetization m(t), discarding the first 10% as transient. Write time and magnetization to magnetization_high_energy.csv.
- Output file: `/app/outputs/magnetization_high_energy.csv`
- Format: csv
- Contract: CSV file with header. Columns: time (float, dimensionless time), magnetization (float, dimensionless magnetization m). One row per output timestep after equilibration.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_low_energy.csv`
- `/app/outputs/magnetization_high_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_low_energy.csv
- path: `/app/outputs/magnetization_low_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetization time series at ε=0.2. The verifier performs a structural audit of the time series.
- schema:
  - `type`: table
  - `required_columns`: `time`, `magnetization`
  - `units`:
    - `time`: dimensionless
    - `magnetization`: dimensionless

### magnetization_high_energy.csv
- path: `/app/outputs/magnetization_high_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetization time series at ε=0.4. The verifier performs a structural audit of the time series.
- schema:
  - `type`: table
  - `required_columns`: `time`, `magnetization`
  - `units`:
    - `time`: dimensionless
    - `magnetization`: dimensionless

Notes: The verifier evaluates structural properties of the submitted CSV files after discarding an initial transient. Exact parameter values are as specified; the agent must implement the 1D spin chain model described in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_low_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "magnetization"
        ],
        "units": {
          "time": "dimensionless",
          "magnetization": "dimensionless"
        }
      },
      "description": "Magnetization time series at ε=0.2. The verifier performs a structural audit of the time series."
    },
    {
      "file": "magnetization_high_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "magnetization"
        ],
        "units": {
          "time": "dimensionless",
          "magnetization": "dimensionless"
        }
      },
      "description": "Magnetization time series at ε=0.4. The verifier performs a structural audit of the time series."
    }
  ],
  "notes": "The verifier evaluates structural properties of the submitted CSV files after discarding an initial transient. Exact parameter values are as specified; the agent must implement the 1D spin chain model described in the instruction."
}
```

## How you are scored
A hidden verifier reads both CSV files. It evaluates structural properties of the magnetization time series (e.g., aspects related to sign changes and mean amplitude) after discarding an initial transient. The exact scoring algorithm is not disclosed, but a correct implementation of the model dynamics at the prescribed energies will satisfy the verifier. The reward value is between 0 and 1. There is no requirement to match a specific numerical value from the original paper.
