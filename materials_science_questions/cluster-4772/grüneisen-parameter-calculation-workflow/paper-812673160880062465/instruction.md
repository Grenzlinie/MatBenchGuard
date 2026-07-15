# MULTI-WAVE ACOUSTIC RESONANCE AND INDUCTION TIME REDUCTION IN REACTIVE MATERIALS

## Problem background
Rapid initiation of condensed-phase explosives involves complex interactions among multiple high-frequency acoustic waves and the material's microstructure. The goal is to understand how nonlinear resonance can dramatically shorten the induction time before a thermal runaway. The target of this task is to numerically simulate the asymptotic model of multiwave acoustic resonance with microstructure for an ideal gas with adiabatic exponent γ=3. By computing blowup times and maximum sound amplitudes across a range of relative phases, the agent will quantify the reduction in induction time and identify the dominant mechanisms (inert resonance, chemical-acoustic linear superposition, and pressure-sensitive effects).

## Approach
The model describes three high-frequency wave amplitudes (one entropy microstructure and two counter-propagating sound waves) that evolve through coupled nonlinear equations. The reaction chemistry enters either through a temperature-sensitive or a pressure-sensitive rate, with coefficients derived from the ideal-gas equation of state. The approach is to implement numerical solvers for the governing systems using operator splitting with three fractional steps: Burgers dynamics (random choice method), inert acoustic resonance (exact FFT-based solver), and combustion (forward Euler). The simulation is run for a set of relative phases between the initial sound waves, and the key quantities (maximum sound amplitude, blowup time, and blowing-up mode) are extracted.

## Reproduction target
Produce a CSV file that aggregates the following quantities for the ideal gas model with γ=3 and relative phases φ ∈ {0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875}:
- Maximum sound amplitude (max Σ) from inert acoustic resonance.
- Blowup time t* from chemical-acoustic linear resonance (temperature-dependent chemistry alone).
- Blowup time t* and the blowing-up mode (Entropy, Left sound, or Right sound) from the full temperature-dependent system.
- Blowup times t* for φ=0.125 and φ=0.5 from the pressure-sensitive system with a large initial entropy kernel.
The CSV must have one row per phase and columns: phi, inert_max, chem_acoustic_tstar, full_tstar, blowup_mode, pressure_tstar_phi125, pressure_tstar_phi5. Pressure columns are empty except for the two specified φ values.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute ideal-gas coefficients from γ=3
- Role: process
- Action: Compute coefficients A, B, α1, α2, α3 using the polytropic ideal-gas formulas with γ=3.
- Evidence: `/app/outputs/coefficients.txt`

### Step 2: Run inert acoustic resonance simulations
- Role: process
- Action: Solve the inert system (38) with A=0.2, B=0.25, initial data (40) for each φ in {0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875}. Record the maximum sound amplitude (max Σ) for each case.
- Evidence: `/app/outputs/inert_log.txt`

### Step 3: Run chemical-acoustic linear resonance simulations
- Role: process
- Action: Solve the reduced system (46) with α1=α2=α3=1/3 (γ=3), initial data (50) for the same φ set. Record blowup time t* for each φ.
- Evidence: `/app/outputs/chem_acoustic_log.txt`

### Step 4: Run full temperature-dependent system simulations
- Role: process
- Action: Solve the full system (41) with A=1, B=0.25, α1=α3=1/3, α2=1/3 (γ=3), initial data (51) for the same φ set. Record blowup time t* and the blowing‑up mode (Entropy, Left sound, or Right sound).
- Evidence: `/app/outputs/full_temp_log.txt`

### Step 5: Run pressure-sensitive system simulations with large entropy kernel
- Role: process
- Action: Solve the pressure‑sensitive system (52) with A=1, B=0.25, α=2 (γ=3), initial data (56) for φ=0.125 and φ=0.5. Record blowup time t* for each.
- Evidence: `/app/outputs/pressure_log.txt`

### Step 6: Write reproduction results CSV
- Role: scored (load-bearing)
- Action: Aggregate all recorded values into a CSV file with columns: phi, inert_max, chem_acoustic_tstar, full_tstar, blowup_mode, pressure_tstar_phi125, pressure_tstar_phi5.
- Output file: `/app/outputs/reproduction_results.csv`
- Format: csv
- Contract: phi (float), inert_max (float), chem_acoustic_tstar (float), full_tstar (float), blowup_mode (string), pressure_tstar_phi125 (float or empty), pressure_tstar_phi5 (float or empty)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.csv
- path: `/app/outputs/reproduction_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing reproduced numerical results for the ideal gas model with γ=3: inert resonance max amplitude, chemical-acoustic linear resonance blowup time, full temperature-dependent system blowup time and mode, and pressure-sensitive system blowup times for φ=0.125,0.5.
- schema:
  - `type`: table
  - `required_columns`: `phi`, `inert_max`, `chem_acoustic_tstar`, `full_tstar`, `blowup_mode`, `pressure_tstar_phi125`, `pressure_tstar_phi5`

Notes: The CSV must have one row for each φ in {0,0.125,0.25,0.375,0.5,0.625,0.75,0.875}. Numeric columns must be floats; blowup_mode must be one of 'Entropy', 'Left sound', 'Right sound', or empty. Pressure columns may be empty except for the two specified φ values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi",
          "inert_max",
          "chem_acoustic_tstar",
          "full_tstar",
          "blowup_mode",
          "pressure_tstar_phi125",
          "pressure_tstar_phi5"
        ]
      },
      "description": "CSV containing reproduced numerical results for the ideal gas model with γ=3: inert resonance max amplitude, chemical-acoustic linear resonance blowup time, full temperature-dependent system blowup time and mode, and pressure-sensitive system blowup times for φ=0.125,0.5."
    }
  ],
  "notes": "The CSV must have one row for each φ in {0,0.125,0.25,0.375,0.5,0.625,0.75,0.875}. Numeric columns must be floats; blowup_mode must be one of 'Entropy', 'Left sound', 'Right sound', or empty. Pressure columns may be empty except for the two specified φ values."
}
```

## How you are scored
A hidden verifier independently compares the contents of your CSV against reference values derived from the original study. Each numeric column is scored by how many entries fall within the verifier's tolerance; the blowup_mode column is scored by exact string match. The final reward is the fraction of entries that satisfy the criteria. Simply reporting the paper's published numbers is not sufficient — the verifier will compare your reproduced results to its hidden gold using predefined tolerances.
