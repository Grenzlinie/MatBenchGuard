# Magnetization Switching in 4-State Clock Model via Monte Carlo Simulation

## Problem background
Biaxial single-domain ferromagnetic nanoparticles can possess two perpendicular easy axes, making them attractive for high-density magnetic recording. Reliable operation requires understanding how the magnetization switches from a metastable orientation to the stable state and how the switching time and the required switching field depend on material parameters and system size. The 4-state clock model on a square lattice captures two stable directions separated by two intermediate orientations. In the symmetric limit (vanishing asymmetry parameter A=0) the model maps to two decoupled Ising models, enabling theoretical predictions for the switching dynamics. This task requires you to compute the mean magnetization switching lifetime and its relative standard deviation, as well as the switching field, for the symmetric 4-state clock model without prior access to the paper's numerical results.

## Approach
Implement a kinetic Monte Carlo simulation of the two-dimensional square-lattice 4-state clock model with periodic boundary conditions and Glauber single-spin-flip dynamics. Spins can point along four directions: the initial direction e0, the opposite stable direction e2, and two perpendicular intermediate states e1 and e3. Only ±90° rotations to a neighboring state are attempted, each with probability 1/2. The energy includes nearest-neighbour ferromagnetic exchange J and an applied magnetic field H directed along e2. The simulation temperature is fixed at 0.8 times the zero-field critical temperature Tc of the symmetric model. The asymmetry parameter A is set to zero throughout. All spins are initialized in the e0 state. The stopping criterion S_∩ is used: record the first Monte Carlo time (in units of Monte Carlo steps per spin, MCSS) when both constituent Ising magnetizations, obtained from the clock model mapping, reach zero.

For the lifetime measurement, use a lattice of linear size L=32 and conduct at least 1000 independent runs for each inverse field value J/|H|, covering a range that spans the single-droplet and multi-droplet regimes. For the switching field, simulate the lattice sizes L=8, 16, 32, 64, 100 at a series of applied field magnitudes. For each (L, |H|) pair, run at least 1000 independent realizations, each tracked for a fixed waiting time of 200 MCSS. Record a binary flag (1 if the system has switched within the waiting time, 0 otherwise). From the collected first-passage times compute, for each inverse field, the mean lifetime and the relative standard deviation (ratio of the root-mean-square deviation to the mean). From the switching flags compute the switching probability for each (L, |H|) and determine the field magnitude H_sw at which the switching probability equals 0.5 (interpolate between data points). Store the analyzed results in the specified JSON output files.

## Reproduction target
Produce two JSON artifacts inside /app/outputs:

1. `/app/outputs/lifetime_data.json` : a JSON array of objects, each with keys
   - `inverse_field` (number, J/|H|),
   - `mean_lifetime` (number, MCSS),
   - `relative_std` (number, dimensionless).
   These values must be computed for L=32 at the inverse field values J/|H| = 2, 4, 6, 8, 10, 12, 14.

2. `/app/outputs/switching_field_data.json` : a JSON array of objects, each with keys
   - `L` (integer, lattice size),
   - `H_sw` (number, |H|/J, dimensionless).
   These values must be computed for L = 8, 16, 32, 64, 100 using a waiting time of 200 MCSS.

All simulations use the symmetric model (A=0), applied field along the e2 direction, and temperature 0.8 Tc.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Monte Carlo simulation of symmetric clock model
- Role: process
- Action: Implement and run a Monte Carlo simulation of the 2D square-lattice 4-state clock model with periodic boundary conditions using Glauber dynamics (nearest-neighbour exchange J, applied field H along e2). Set asymmetry parameter A=0, initial spins all along e0, temperature T=0.8Tc. For lifetime measurements: use L=32 and at least 1000 independent runs for each inverse field J/|H| in {2, 4, 6, 8, 10, 12, 14}; record the first-passage time (in MCSS) according to the S_∩ stopping criterion for each run. For switching-field measurements: for each L in {8,16,32,64,100}, for a range of |H| values, simulate at least 1000 runs with waiting time tw=200 MCSS and record a binary flag (1 if switched, 0 otherwise) for each run/field combination. Store the raw per-run data in intermediate files.
- Evidence: `/app/outputs/lifetime_raw.csv, switching_raw.csv`

### Step 2: Lifetime analysis for L=32
- Role: scored (load-bearing)
- Action: From the raw per-run first-passage times for L=32, compute the mean lifetime ⟨τ⟩ and the relative standard deviation r = √(⟨τ²⟩-⟨τ⟩²)/⟨τ⟩ for each inverse field value J/|H| in {2, 4, 6, 8, 10, 12, 14}. Write the results as a JSON array of objects to lifetime_data.json.
- Output file: `/app/outputs/lifetime_data.json`
- Format: json
- Contract: JSON array of objects, each with keys: 'inverse_field' (number, J/|H|), 'mean_lifetime' (number, MCSS), 'relative_std' (number, dimensionless).
- Scoring: scored by hidden verifier

### Step 3: Switching field determination
- Role: scored (load-bearing)
- Action: From the raw per-run switching flags (1/0) for each L and |H|, compute the switching probability p_sw for each field magnitude. For each L, determine the switching field H_sw such that p_sw ≈ 0.5 (interpolate between data points). Write the results as a JSON array of objects to switching_field_data.json.
- Output file: `/app/outputs/switching_field_data.json`
- Format: json
- Contract: JSON array of objects, each with keys: 'L' (integer, lattice size), 'H_sw' (number, |H|/J, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lifetime_data.json`
- `/app/outputs/switching_field_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lifetime_data.json
- path: `/app/outputs/lifetime_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mean lifetime and relative standard deviation of the symmetric clock model at L=32 for J/|H| = 2,4,6,8,10,12,14.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `inverse_field`, `mean_lifetime`, `relative_std`
    - `properties`:
      - `inverse_field`:
        - `type`: number
      - `mean_lifetime`:
        - `type`: number
      - `relative_std`:
        - `type`: number

### switching_field_data.json
- path: `/app/outputs/switching_field_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Switching field H_sw (|H|/J) as a function of lattice size L for tw=200 MCSS.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `L`, `H_sw`
    - `properties`:
      - `L`:
        - `type`: integer
      - `H_sw`:
        - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lifetime_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "inverse_field",
            "mean_lifetime",
            "relative_std"
          ],
          "properties": {
            "inverse_field": {
              "type": "number"
            },
            "mean_lifetime": {
              "type": "number"
            },
            "relative_std": {
              "type": "number"
            }
          }
        }
      },
      "description": "Mean lifetime and relative standard deviation of the symmetric clock model at L=32 for J/|H| = 2,4,6,8,10,12,14."
    },
    {
      "file": "switching_field_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "L",
            "H_sw"
          ],
          "properties": {
            "L": {
              "type": "integer"
            },
            "H_sw": {
              "type": "number"
            }
          }
        }
      },
      "description": "Switching field H_sw (|H|/J) as a function of lattice size L for tw=200 MCSS."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each of your output files. For lifetime_data.json, it compares your computed mean lifetime and relative standard deviation at each inverse field against hidden reference values derived from the paper's reported measurements. For switching_field_data.json, it compares your H_sw for each lattice size against hidden reference values. The comparisons use tolerances appropriate for a re-implemented simulation; meeting or exceeding the reference accuracy earns full credit, while larger deviations reduce the stage score. The final reward is a weighted combination of the two stage scores. The verifier also validates that your files contain the required fields and that all values are finite numbers. Simply hardcoding the paper's final numbers, even if they are known to you, will not satisfy the pipeline requirements and will be detected by structural checks.
