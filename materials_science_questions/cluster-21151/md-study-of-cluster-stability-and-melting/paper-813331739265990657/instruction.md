# Mesoscale Multi-Particle Collision Model: Shear Viscosity from Stress Autocorrelation

## Problem background
The multi-particle collision (MPC) model is a particle-based mesoscopic method for fluid dynamics that alternates between free streaming of particles and multi-particle collisions that rotate velocities inside cells. The collisions conserve mass, momentum, and energy, and the model is known to yield the Navier–Stokes equations on long distance and time scales. A central test of the model's consistency with continuum hydrodynamics is the computation of shear viscosity from the stress–stress autocorrelation function via a discrete Green–Kubo formula. This task reproduces that test by implementing the three-dimensional MPC dynamics and computing the shear viscosity and its underlying autocorrelation curve.

## Approach
The system consists of a large number of particles moving in a periodic box. The dynamics proceeds in two alternating phases: (1) free streaming, where particles move according to their velocities for a fixed time interval τ; (2) multi-particle collisions, where the box is partitioned into a regular grid of cells and, within each cell, the velocities of all particles are rotated by a fixed angle about a randomly chosen axis. This collision rule preserves the cell's total mass, momentum, and energy. The off-diagonal stress component σ_xy is recorded at each time step during a long production run. From this trajectory the stress autocorrelation function C(t) = ⟨σ_xy(0) σ_xy(t)⟩ is computed by averaging over time origins. The shear viscosity η is then obtained by discrete summation: η = (m²ρ / (2 k_B T N)) Σ_ℓ C(t_ℓ) τ, where m is the particle mass, ρ is the number density, N is the total number of particles, k_B is Boltzmann's constant, and T is the temperature. The simulation parameters are: three-dimensional box with 32×32×32 cells, average density ρ = 10.0 particles per cell, temperature k_B T = 1/3 (in simulation units where m=1, τ=1, cell length=1), and rotation angle ±π/2 about a randomly chosen axis. The system is first equilibrated and then a production phase of at least 10000 steps is carried out so that the autocorrelation decays to near zero within a few time units.

## Reproduction target
The concrete objective is to execute the MPC simulation described above, compute the stress autocorrelation function from the production run, and integrate it to obtain the shear viscosity. The required outputs are:

- stress_autocorrelation.csv: a two-column CSV file with lag time (in units of τ) and the normalized autocorrelation C(t)/C(0).
- shear_viscosity.json: a JSON file containing a single key "shear_viscosity" whose value is the computed viscosity in simulation units.

The simulation must run long enough that the autocorrelation decays to near zero and the integrated viscosity reaches a plateau. The target is the full autocorrelation curve and the final viscosity value; both will be compared against independently computed references.

## Assets

- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Run MPCD simulation
- Role: process
- Action: Implement the multi-particle collision (MPC) algorithm with free streaming and random rotations of velocities in cells. Initialize N particles in a periodic 3D box partitioned into 32×32×32 cells, with average density ρ=10.0 particles per cell and temperature kB T=1/3. Use rotation angle ±π/2 about random axes. Equilibrate the system and then run a production phase long enough for the stress autocorrelation to decay to near zero (e.g., at least 10000 time steps). Record the off-diagonal stress component σ_xy at every step and save the trajectory as a NumPy array.
- Evidence: `/app/outputs/stress_trajectory.npy`

### Step 2: Compute stress autocorrelation function
- Role: scored (load-bearing)
- Action: From the saved off-diagonal stress trajectory, compute the stress–stress autocorrelation function C(t) = ⟨σ_xy(0) σ_xy(t)⟩ averaged over time origins. Write the result as a CSV file with columns 'time' and 'autocorrelation'.
- Output file: `/app/outputs/stress_autocorrelation.csv`
- Format: csv
- Contract: Two columns: time (float, lag time in units of τ) and autocorrelation (float, dimensionless C(t)/C(0)). Header row required.
- Scoring: scored by hidden verifier

### Step 3: Compute shear viscosity
- Role: scored
- Action: Using the autocorrelation function from the previous step, compute the shear viscosity η according to the discrete Green–Kubo formula described in the method: η = (m²ρ / (2 kB T N)) * Σ_{ℓ} C(ℓτ) * τ, with appropriate units. Write the result as a JSON object with key 'shear_viscosity'.
- Output file: `/app/outputs/shear_viscosity.json`
- Format: json
- Contract: A JSON object containing a single key 'shear_viscosity' with a numeric value (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_autocorrelation.csv`
- `/app/outputs/shear_viscosity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_autocorrelation.csv
- path: `/app/outputs/stress_autocorrelation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress autocorrelation function curve. The checker will compare it to a hidden reference curve using mean squared error.
- schema:
  - `type`: table
  - `required_columns`: `time`, `autocorrelation`
  - `units`:
    - `time`: reduced time units (tau)
    - `autocorrelation`: dimensionless

### shear_viscosity.json
- path: `/app/outputs/shear_viscosity.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Shear viscosity value. The checker will recompute viscosity by integrating the provided autocorrelation and also compare the submitted value to a hidden reference.
- schema:
  - `type`: object
  - `required`: `shear_viscosity`
  - `units`:
    - `shear_viscosity`: simulation units (m=1, tau=1, cell=1)

Notes: Both scored artifacts are derived from the raw stress trajectory of the MPCD simulation. The verification recomputes the viscosity from the autocorrelation CSV and compares both the curve shape and the integrated value to reference data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_autocorrelation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "autocorrelation"
        ],
        "units": {
          "time": "reduced time units (tau)",
          "autocorrelation": "dimensionless"
        }
      },
      "description": "Stress autocorrelation function curve. The checker will compare it to a hidden reference curve using mean squared error."
    },
    {
      "file": "shear_viscosity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "shear_viscosity"
        ],
        "units": {
          "shear_viscosity": "simulation units (m=1, tau=1, cell=1)"
        }
      },
      "description": "Shear viscosity value. The checker will recompute viscosity by integrating the provided autocorrelation and also compare the submitted value to a hidden reference."
    }
  ],
  "notes": "Both scored artifacts are derived from the raw stress trajectory of the MPCD simulation. The verification recomputes the viscosity from the autocorrelation CSV and compares both the curve shape and the integrated value to reference data."
}
```

## How you are scored
A hidden verifier inspects each scored output artifact and computes a combined reward. The scoring is staged and weighted:

1. Autocorrelation (stress_autocorrelation.csv): the verifier checks the file format, verifies that the autocorrelation decays to near zero within a reasonable range, and compares the submitted curve against a hidden reference autocorrelation function using a similarity metric (e.g., mean squared error). A close match earns full credit; a poor match reduces the score.
2. Shear viscosity (shear_viscosity.json): the verifier independently recomputes the viscosity by numerically integrating the autocorrelation from your CSV file and compares that value, as well as your self-reported "shear_viscosity" field, to a hidden reference viscosity derived from a validated model. If the recomputed viscosity meets or exceeds a quality threshold relative to the reference, full credit is given; otherwise the score decreases as the result deviates.

The final reward is a weighted combination of the scores from these two artefacts, with the viscosity carrying the primary weight. Simply reporting the paper’s numbers is not sufficient: the verifier re-derives the comparison from your raw output and checks internal consistency.
