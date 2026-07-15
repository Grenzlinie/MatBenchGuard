# Classical MD Lattice Parameter Reproduction for Oxide Ion Conductor CeNbO4 and CeNbO4.25

## Problem background
CeNbO4.25 is an oxide ion conductor with promising anisotropic diffusion properties that are closely tied to its crystal structure. Reproducing the equilibrium lattice parameters of CeNbO4 and its oxidized form CeNbO4.25 through classical molecular dynamics (MD) simulations provides a computational check of the material's cell geometry. The task involves using empirical Buckingham pair potentials to run MD and extract time-averaged lattice constants from the simulations.

## Approach
Classical MD simulations with the provided Buckingham potential parameters will be performed on the two crystal structures (CeNbO4 and CeNbO4.25). The workflow consists of: converting the CIF structures and potential parameters into LAMMPS input files and building suitable supercells; running NPT molecular dynamics at 298 K with an equilibration and production phase; and extracting the time-averaged lattice constants a, b, c (Å) and angle beta (°) from the production trajectory. Finally, the computed values are compared to known experimental reference lattice parameters by computing percent differences using the formula: (computed − experimental) / experimental × 100%.

## Reproduction target
Produce a JSON file (`lattice_parameters.json`) containing the computed MD lattice parameters and the corresponding percent deviations for both phases. The experimental reference values that must be used for the percent differences are:
- CeNbO4: a = 7.261 Å, b = 11.403 Å, c = 5.162 Å, beta = 130.53°
- CeNbO4.25: a = 14.373 Å, b = 22.792 Å, c = 11.832 Å, beta = 105.07°

The output JSON must have the keys `CeNbO4` and `CeNbO4_25`, each containing the fields `a`, `b`, `c`, `beta`, and the corresponding `percent_diff_a`, `percent_diff_b`, `percent_diff_c`, `percent_diff_beta`.

## Assets

- LAMMPS: https://lammps.sandia.gov
- CeNbO4 crystal structure
- CeNbO4.25 crystal structure
- Buckingham potential parameters

## Workflow steps

### Step 1: Prepare simulation inputs
- Role: process
- Action: Convert the provided crystal structure files (CeNbO4 CIF, CeNbO4.25 CIF) and the Buckingham potential parameters file into LAMMPS input data files and scripts. Build appropriate supercells for the MD simulations.
- Evidence: `/app/outputs/lammps_inputs.zip`

### Step 2: Run molecular dynamics simulations
- Role: process
- Action: Execute LAMMPS MD simulations for CeNbO4 and CeNbO4.25 at 298 K. Include an equilibration phase and a production run of sufficient length to obtain converged time-averaged cell parameters.
- Evidence: `/app/outputs/md_logs.zip`

### Step 3: Extract lattice parameters and compute deviations
- Role: scored (load-bearing)
- Action: From the production trajectories, compute the time-averaged lattice constants a, b, c (Å) and angle beta (°) for CeNbO4 and CeNbO4.25. Using the experimental reference values (provided in the task description), calculate percent differences as (computed - experimental) / experimental × 100%. Output the results in the specified JSON file.
- Output file: `/app/outputs/lattice_parameters.json`
- Format: json
- Contract: { "CeNbO4": { "a": float, "b": float, "c": float, "beta": float, "percent_diff_a": float, "percent_diff_b": float, "percent_diff_c": float, "percent_diff_beta": float }, "CeNbO4_25": { "a": float, "b": float, "c": float, "beta": float, "percent_diff_a": float, "percent_diff_b": float, "percent_diff_c": float, "percent_diff_beta": float } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.json
- path: `/app/outputs/lattice_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed MD lattice parameters (a,b,c,beta) and percent deviations from experimental values for CeNbO4 and CeNbO4.25.
- schema:
  - `type`: object
  - `required`:
    - `CeNbO4`:
      - `a`: number (Å)
      - `b`: number (Å)
      - `c`: number (Å)
      - `beta`: number (degrees)
      - `percent_diff_a`: number
      - `percent_diff_b`: number
      - `percent_diff_c`: number
      - `percent_diff_beta`: number
    - `CeNbO4_25`:
      - `a`: number (Å)
      - `b`: number (Å)
      - `c`: number (Å)
      - `beta`: number (degrees)
      - `percent_diff_a`: number
      - `percent_diff_b`: number
      - `percent_diff_c`: number
      - `percent_diff_beta`: number

Notes: The experimental reference lattice parameters are provided within the task instructions; the agent must compute deviations from those fixed values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "CeNbO4": {
            "a": "number (Å)",
            "b": "number (Å)",
            "c": "number (Å)",
            "beta": "number (degrees)",
            "percent_diff_a": "number",
            "percent_diff_b": "number",
            "percent_diff_c": "number",
            "percent_diff_beta": "number"
          },
          "CeNbO4_25": {
            "a": "number (Å)",
            "b": "number (Å)",
            "c": "number (Å)",
            "beta": "number (degrees)",
            "percent_diff_a": "number",
            "percent_diff_b": "number",
            "percent_diff_c": "number",
            "percent_diff_beta": "number"
          }
        }
      },
      "description": "Computed MD lattice parameters (a,b,c,beta) and percent deviations from experimental values for CeNbO4 and CeNbO4.25."
    }
  ],
  "notes": "The experimental reference lattice parameters are provided within the task instructions; the agent must compute deviations from those fixed values."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `lattice_parameters.json`. It compares each of the eight primary lattice‑parameter dimensions (a, b, c, beta for CeNbO4 and for CeNbO4.25) to expected values derived from honest MD runs. The overall reward is the fraction of these dimensions that fall within an acceptable precision range. You must run the actual MD simulations; attempting to fabricate or guess the numbers will not reliably satisfy all eight constraints and will result in a low score.
