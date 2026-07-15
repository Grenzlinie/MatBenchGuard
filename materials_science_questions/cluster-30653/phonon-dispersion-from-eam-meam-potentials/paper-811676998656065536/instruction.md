# Hydrogen Diffusion in Palladium and Niobium via Molecular Dynamics

## Problem background
Hydrogen diffusion in face-centered cubic palladium (Pd) and body-centered cubic niobium (Nb) is of fundamental and applied interest for metal-hydrogen systems. Molecular dynamics (MD) simulations using accurate many-body interatomic potentials can probe the microscopic diffusion mechanism and predict temperature-dependent self-diffusion coefficients. This task exercises such simulations, computing how hydrogen mobility changes with temperature in both metals.

## Approach
The method employs classical MD in the NVT ensemble using two established many-body potentials: an embedded-atom method (EAM) potential for Pd, and a Finnis–Sinclair potential for Nb, with hydrogen atoms introduced as interstitial solutes. Starting from initial configurations of PdH_x and NbH_x with periodic boundary conditions, equilibration and production MD runs are performed at a set of temperatures. Time-averaged mean-square displacements of the hydrogen atoms are extracted, from which self-diffusion constants are calculated via the Einstein relation. Finally, an Arrhenius law is fitted to the temperature-dependent diffusion constants to determine an activation energy and a pre-exponential factor.

## Reproduction target
Compute the self-diffusion coefficients of hydrogen in Pd (EAM potential) and in Nb (Finnis–Sinclair potential) at the specified temperatures (Pd: 600, 700, 800, 900, 1000 K; Nb: 600, 800, 1000 K) using MD. Report the individual diffusion constants and the fitted Arrhenius parameters – activation energy U and pre-exponential factor D0 – for each system.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- EAM potential for Pd by Foiles, Baskes, Daw (1986)
- Finnis-Sinclair potential for Nb-H by Gillan et al.

## Workflow steps

### Step 1: Prepare simulation inputs
- Role: process
- Action: Construct initial atomic configurations for PdH_x (256 Pd + 8 H) and NbH_x (432 Nb + 8 H) with periodic boundary conditions. Obtain the EAM potential for Pd and implement the Finnis-Sinclair Nb-H potential in LAMMPS. Create LAMMPS input scripts for NVT dynamics at the required temperatures (Pd: 600, 700, 800, 900, 1000 K; Nb: 600, 800, 1000 K).
- Evidence: none

### Step 2: Run MD simulations
- Role: process
- Action: For each system and temperature, perform equilibration followed by production MD in the NVT ensemble. Record H atom positions to enable mean-square displacement (MSD) calculation.
- Evidence: none

### Step 3: Compute self-diffusion constants
- Role: scored (load-bearing)
- Action: From the MSD of H atoms computed during production runs, calculate the self-diffusion constant D_s at each temperature using D = <Δr^2>/(6t). Write a CSV file with columns: system, temperature_K, D_cm2_per_s.
- Output file: `/app/outputs/diffusion_constants.csv`
- Format: csv
- Contract: Columns: system (string, 'Pd' or 'Nb'), temperature_K (numeric, Kelvin), D_cm2_per_s (numeric, cm^2/s).
- Scoring: scored by hidden verifier

### Step 4: Fit Arrhenius parameters
- Role: scored
- Action: Using the D_s values from diffusion_constants.csv, perform a linear least-squares fit of ln(D_s) vs 1/T to obtain activation energy U (eV) and prefactor D0 (cm^2/s) for each system. Write the results in a JSON file.
- Output file: `/app/outputs/arrhenius_params.json`
- Format: json
- Contract: JSON object with keys 'Pd' and 'Nb', each an object with keys 'U' (number, eV) and 'D0' (number, cm^2/s).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/diffusion_constants.csv`
- `/app/outputs/arrhenius_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diffusion_constants.csv
- path: `/app/outputs/diffusion_constants.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Hydrogen self-diffusion constants in Pd and Nb at simulated temperatures; the checker refits Arrhenius parameters from this table and compares to paper gold.
- schema:
  - `type`: table
  - `required_columns`: `system`, `temperature_K`, `D_cm2_per_s`
  - `units`:
    - `temperature_K`: K
    - `D_cm2_per_s`: cm^2/s

### arrhenius_params.json
- path: `/app/outputs/arrhenius_params.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent-fitted Arrhenius parameters; the checker refits from diffusion_constants.csv and checks consistency with these reported values.
- schema:
  - `type`: object
  - `required`:
    - `Pd`:
      - `U`: number (eV)
      - `D0`: number (cm^2/s)
    - `Nb`:
      - `U`: number (eV)
      - `D0`: number (cm^2/s)

Notes: The primary scoring is on the Arrhenius parameters recomputed from the D_s values, compared to paper-reported gold with hidden tolerances. The agent's own fit in arrhenius_params.json is used for a consistency check against the checker's refit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diffusion_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "temperature_K",
          "D_cm2_per_s"
        ],
        "units": {
          "temperature_K": "K",
          "D_cm2_per_s": "cm^2/s"
        }
      },
      "description": "Hydrogen self-diffusion constants in Pd and Nb at simulated temperatures; the checker refits Arrhenius parameters from this table and compares to paper gold."
    },
    {
      "file": "arrhenius_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "Pd": {
            "U": "number (eV)",
            "D0": "number (cm^2/s)"
          },
          "Nb": {
            "U": "number (eV)",
            "D0": "number (cm^2/s)"
          }
        }
      },
      "description": "Agent-fitted Arrhenius parameters; the checker refits from diffusion_constants.csv and checks consistency with these reported values."
    }
  ],
  "notes": "The primary scoring is on the Arrhenius parameters recomputed from the D_s values, compared to paper-reported gold with hidden tolerances. The agent's own fit in arrhenius_params.json is used for a consistency check against the checker's refit."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores the artifacts from each scored workflow stage and combines them by weight into a final reward. For the diffusion constants, the verifier will re-analyze your reported D values and optionally check a few of them against independently computed reference values with generous tolerances. The primary score is based on the Arrhenius parameters derived from your diffusion data: the verifier will fit an Arrhenius curve to your submitted D points and compare the resulting parameters to a hidden reference, using tolerant thresholds designed for independent re-runs. Reporting numbers alone is not sufficient; all intermediates must be generated through the simulation workflow.
