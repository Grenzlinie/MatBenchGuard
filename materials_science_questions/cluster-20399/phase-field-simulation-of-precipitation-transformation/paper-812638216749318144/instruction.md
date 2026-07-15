# Cahn-Hilliard phase-field simulation of liquid phase separation free energy

## Problem background
Cu-Fe alloys undergo liquid phase separation during rapid solidification, giving rise to Fe-rich droplets that coalesce and coarsen within a Cu-rich matrix. Understanding the evolution of these Fe nuclei is crucial for controlling the microstructure and properties of the alloy. The Cahn-Hilliard phase-field model provides a continuum description of spinodal decomposition and Ostwald ripening, capturing the dynamics of the concentration field. A key diagnostic of the phase separation process is the time evolution of the total free energy of the system, which reflects the progressive reduction in interfacial area and the approach to equilibrium.

## Approach
The simulation employs the Cahn-Hilliard equation with a double-well free energy density f(c) = A c² (1−c)², where A is a positive constant. The total free energy F = ∫[f(c) + (κ/2)(∇c)²] dV includes a gradient energy term penalizing sharp interfaces, with gradient energy coefficient κ. A constant mobility M governs the diffusive flux. The concentration field is discretized on a uniform 3D grid with periodic boundary conditions in all directions. The system is initialized with small random fluctuations around the average composition to trigger spinodal decomposition. Time integration is performed with explicit Euler steps. At each time step, the total free energy (volume plus gradient contributions) is computed from the discrete representation and recorded together with the time step index. The evolution should be followed long enough to capture the initial rapid phase separation and the subsequent coarsening (Ostwald ripening) regime. All quantities are treated as dimensionless; the agent chooses numerical parameters (A, κ, M, grid size, time step) that yield physically meaningful dynamics.

## Reproduction target
Produce a CSV file `free_energy_curve.csv` containing columns `time_step` (integer) and `free_energy` (float). The file must contain at least 100 rows spanning the transient and near-equilibrium stages of the phase separation process. The simulation should be implemented as described in the Approach, and the recorded energy trace should correspond to the total free energy computed from the concentration field at each saved time step.

## Assets

- Python with NumPy: numpy

## Workflow steps

### Step 1: Cahn-Hilliard phase-field simulation of Fe core evolution
- Role: scored (load-bearing)
- Action: Implement the Cahn-Hilliard model with a double-well free energy f(c)=A*c^2*(1-c)^2, gradient energy term, and constant mobility. Use a 3D grid with periodic boundary conditions and explicit Euler time integration. Initialize concentration field with small random fluctuations around the average composition. Simulate for enough time steps to capture the initial rapid phase separation and subsequent Ostwald ripening. At each time step, compute the total free energy and record it with the time step index.
- Output file: `/app/outputs/free_energy_curve.csv`
- Format: csv
- Contract: CSV with header: time_step,free_energy. At least 100 rows covering the transient and near-equilibrium regime.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_curve.csv
- path: `/app/outputs/free_energy_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV with columns time_step (int) and free_energy (float). At least 100 rows covering the transient and near-equilibrium regime.
- schema:
  - `type`: table
  - `required_columns`: `time_step`, `free_energy`
  - `column_types`:
    - `time_step`: integer
    - `free_energy`: float
  - `units`:
    - `time_step`: dimensionless
    - `free_energy`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_step",
          "free_energy"
        ],
        "column_types": {
          "time_step": "integer",
          "free_energy": "float"
        },
        "units": {
          "time_step": "dimensionless",
          "free_energy": "dimensionless"
        }
      },
      "description": "CSV with columns time_step (int) and free_energy (float). At least 100 rows covering the transient and near-equilibrium regime."
    }
  ],
  "notes": ""
}
```

## How you are scored
The verifier first checks that `free_energy_curve.csv` is present, well-formed, and contains the required columns with at least 100 rows of numeric data. It then performs a structural analysis of the `free_energy` values to evaluate whether they exhibit the expected qualitative behavior for a system undergoing phase separation and coarsening. The final score is a weighted combination of these checks, with the structural audit carrying the primary weight. Simply reporting a plausible-looking number is not sufficient; the verifier rewards genuine simulation output.
