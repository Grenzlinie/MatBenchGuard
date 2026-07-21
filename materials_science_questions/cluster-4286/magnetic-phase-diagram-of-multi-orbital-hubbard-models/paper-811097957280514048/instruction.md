# Magnetic phase diagram of the single-band Hubbard model via Hartree-Fock

## Problem background
The single-band Hubbard model on a square lattice captures the competition between electron hopping and on-site Coulomb repulsion. At low hole doping, strong correlations give rise to magnetically ordered ground states whose nature is not settled by perturbation theory alone. Within the self-consistent Hartree-Fock approximation with unrestricted spin directions, the model can sustain several candidate phases: spin-density waves that evolve into vertical domain walls, diagonal domain walls, and isolated ferromagnetic polarons. The central challenge is to determine, for a fixed low doping, the energetic ordering of these phases as the dimensionless interaction strength U/t is varied, and to resolve whether the spin configurations remain collinear. This task reproduces those computations and compares the resulting phase boundaries and collinearity status against the findings reported in the literature.

## Approach
Implement the self-consistent Hartree-Fock mean-field approximation for the single-band Hubbard model on a square lattice, keeping both longitudinal and transverse spin components (unrestricted local spin direction). The Hartree-Fock Hamiltonian is diagonalised iteratively until the change in spin and charge expectation values falls below a tight convergence threshold. The simulation is carried out in rectangular supercells elongated perpendicular to domain walls—(33,0)×(0,2) for vertical walls and (33,33)×(1,-1) for diagonal walls—and in a square supercell of at least 10×10 for polarons. Hole doping is fixed at δ=1/32. For each phase, calculations are performed at U/t = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. The total energy per site (in units of the hopping t) is extracted for every converged solution. The crossover U/t values are identified as the midpoints where the lowest-energy phase changes. Finally, the global spin quantization axis is determined for all converged solutions with U/t ≤ 20, and the maximum angular deviation of any spin vector from that axis is computed to verify whether all solutions are collinear within a 5-degree tolerance.

## Reproduction target
For the single-band Hubbard model on a square lattice at hole doping δ=1/32, using the self-consistent unrestricted Hartree-Fock treatment: (1) compute the total energy per site for the vertical domain-wall, diagonal domain-wall, and polaron phases at U/t = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, and record them in a CSV table; (2) from these energies, determine the crossover U/t midpoints where the favoured phase changes from vertical walls to diagonal walls, and from diagonal walls to polarons; (3) verify that for all converged spin solutions with U/t ≤ 20, the spin expectation vectors are collinear, i.e., their angular deviation from a common axis is less than 5°, and report the status together with the maximum observed angular deviation.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Self-consistent Hartree-Fock simulation of the Hubbard model
- Role: process
- Action: Implement the self-consistent Hartree-Fock approximation for the single-band Hubbard model on a square lattice with unrestricted spin directions. Use rectangular supercells (33,0)×(0,2) for vertical domain walls, (33,33)×(1,-1) for diagonal domain walls, and a square supercell of at least 10×10 for polarons. Fix hole doping δ=1/32. For each phase, run calculations at U/t = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Converge using a criterion based on change in spin and charge expectation values. Store converged total energy per site, spin vectors, and charge densities for each (phase, U/t) combination.
- Evidence: `/app/outputs/converged_spins_charge.npz`

### Step 2: Phase energy table
- Role: scored (load-bearing)
- Action: From the simulation output, compile the total energy per site for each (phase, U/t). Output a CSV with columns U_over_t, phase, energy_per_site for all U/t values and phases.
- Output file: `/app/outputs/phase_energies.csv`
- Format: csv
- Contract: columns: U_over_t (float), phase (string: one of vertical_wall, diagonal_wall, polaron), energy_per_site (float). Rows for U/t = 2,4,6,8,10,12,14,16,18,20 for each phase.
- Scoring: scored by hidden verifier

### Step 3: Crossover U/t values
- Role: scored
- Action: Using the energies from step_02, identify the lowest-energy phase at each U/t and compute the crossover U/t midpoints where the favored phase changes: vertical → diagonal walls and diagonal walls → polarons. Output a JSON file with these two crossover values.
- Output file: `/app/outputs/crossover_values.json`
- Format: json
- Contract: {"vertical_to_diagonal_crossover_U_over_t": <float>, "diagonal_to_polaron_crossover_U_over_t": <float>}
- Scoring: scored by hidden verifier

### Step 4: Collinearity verification
- Role: scored
- Action: For each converged solution with U/t ≤ 20, compute the global spin quantization axis and the maximum angular deviation of any spin vector from that axis. If all deviations are <5°, declare the spins collinear. Output a JSON file.
- Output file: `/app/outputs/collinearity_result.json`
- Format: json
- Contract: {"collinear_for_U_t_le_20": <boolean>, "max_angular_deviation_degrees": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_energies.csv`
- `/app/outputs/crossover_values.json`
- `/app/outputs/collinearity_result.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_energies.csv
- path: `/app/outputs/phase_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV with columns U_over_t (float), phase (string: vertical_wall, diagonal_wall, polaron), energy_per_site (float). Rows for U/t = 2,4,6,8,10,12,14,16,18,20 for each phase.
- schema:
  - `type`: table
  - `required_columns`: `U_over_t`, `phase`, `energy_per_site`

### crossover_values.json
- path: `/app/outputs/crossover_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON object with two crossover U/t midpoints derived from the lowest-energy phase data.
- schema:
  - `type`: object
  - `required`:
    - `vertical_to_diagonal_crossover_U_over_t`: float
    - `diagonal_to_polaron_crossover_U_over_t`: float

### collinearity_result.json
- path: `/app/outputs/collinearity_result.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: JSON object with collinearity boolean and maximum angular deviation. The checker verifies that collinear_for_U_t_le_20 is true and max_angular_deviation_degrees < 5.
- schema:
  - `type`: object
  - `required`:
    - `collinear_for_U_t_le_20`: boolean
    - `max_angular_deviation_degrees`: float

Notes: The simulation produces a raw evidence file (converged_spins_charge.npz) which is not scored but required for downstream steps. The checker recomputes crossover U/t values from phase_energies.csv and compares them to paper-reported references with tolerance. Collinearity result is verified against the 5-degree bound.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "U_over_t",
          "phase",
          "energy_per_site"
        ]
      },
      "description": "CSV with columns U_over_t (float), phase (string: vertical_wall, diagonal_wall, polaron), energy_per_site (float). Rows for U/t = 2,4,6,8,10,12,14,16,18,20 for each phase."
    },
    {
      "file": "crossover_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "vertical_to_diagonal_crossover_U_over_t": "float",
          "diagonal_to_polaron_crossover_U_over_t": "float"
        }
      },
      "description": "JSON object with two crossover U/t midpoints derived from the lowest-energy phase data."
    },
    {
      "file": "collinearity_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "collinear_for_U_t_le_20": "boolean",
          "max_angular_deviation_degrees": "float"
        }
      },
      "description": "JSON object with collinearity boolean and maximum angular deviation. The checker verifies that collinear_for_U_t_le_20 is true and max_angular_deviation_degrees < 5."
    }
  ],
  "notes": "The simulation produces a raw evidence file (converged_spins_charge.npz) which is not scored but required for downstream steps. The checker recomputes crossover U/t values from phase_energies.csv and compares them to paper-reported references with tolerance. Collinearity result is verified against the 5-degree bound."
}
```

## How you are scored
A hidden verifier reads the three output files and scores each one independently against reference values, tolerances, and structural checks. The phase energies CSV is used to recompute the lowest-energy phase at each U/t; the derived crossover midpoints are compared to expected hidden gold values with an appropriate tolerance. The crossover JSON is similarly checked against those hidden references. The collinearity result is verified: the boolean must be true and the reported maximum angular deviation must be below 5°. Each scored artefact contributes a weight to the final [0,1] reward. Simply printing a number is not enough; the submission must follow the required file formats and schemas exactly.
