# Mechanical Properties of Cr-Nb Bicrystal Nanocylinders from Molecular Dynamics Simulations

## Problem background
This task explores how the mechanical response of Cr–Nb bicrystal nanocylinders depends on the crystallographic orientation of the applied tensile load. Molecular dynamics simulations are performed for three directions (<100>, <110>, <111>) at constant strain rate, and the resulting stress–strain curves are analyzed to extract elastic and strength properties. The computed values of Young's modulus, yield strength, ultimate tensile strength, total elongation at failure, and work of deformation for each orientation provide insight into the atomic-scale mechanisms of deformation and failure in these bicrystals.

## Approach
The approach uses classical molecular dynamics with an interatomic pair potential derived from the Rose universal energy function. The potential parameters for Cr–Cr, Nb–Nb, and Cr–Nb are taken from published empirical data. Cylindrical bicrystal models are constructed with the Cr–Nb interface aligned along the tensile axis for each of the three orientations. Constant-strain-rate tensile simulations are performed at a temperature of 300 K, elongating the specimen until failure. The simulations track per-step atomic positions, energy, and stress. From the engineering stress–strain curves, the linear-elastic region yields Young's modulus, the yield point is identified (e.g., by a 0.2% offset criterion), and the ultimate tensile strength, total elongation at failure, and work of deformation up to failure are computed. The outputs are compiled into a single table comparing these properties across the three loading directions.

## Reproduction target
Produce a CSV file, `/app/outputs/tensile_properties.csv`, containing the computed Young's modulus, yield strength, ultimate tensile strength, total elongation at failure, and work of deformation for Cr–Nb bicrystals pulled in tension along the <100>, <110>, and <111> crystallographic directions. The CSV must have one row per orientation and include the columns: `orientation`, `elongation_at_failure_percent`, `Young_modulus_GPa`, `yield_strength_GPa`, `total_elongation_percent`, `work_of_deformation_GJm3`, `ultimate_strength_GPa`. All values should be derived from the simulated stress–strain curves using the specified simulation protocol and analysis criteria.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/

## Workflow steps

### Step 1: Construct interatomic pair potentials
- Role: process
- Action: Implement the universal Rose energy function U = U0(1+a)exp(-a) with a = b(1 - r/r0) + c(1 - r/r0)^2 + d(1 - r/r0)^3. Use the following potential parameters:
  - Cr–Cr: b=5.58, c=2.79, d=5.58, U0=−0.6345 eV, r0=0.262 nm, rk=0.350 nm
  - Nb–Nb: b=5.19, c=0.64, d=3.11, U0=−1.1274 eV, r0=0.297 nm, rk=0.400 nm
  - Cr–Nb: b=4.80, c=−1.51, d=0.63, U0=−0.8810 eV, r0=0.280 nm, rk=0.375 nm
  Create the required potential definition (e.g., tabulated potentials or analytic formulas) for the chosen MD engine.
- Evidence: `/app/outputs/potential_parameters.txt`

### Step 2: Generate bicrystal initial configurations
- Role: process
- Action: Build cylindrical Cr-Nb bicrystal models for each tensile orientation using the following geometric parameters:
  - <100>: 1168 atoms total (712 Cr + 456 Nb), length 4.63 nm (2.24 nm Cr + 2.39 nm Nb), Cr diameter 2.080 nm, Nb diameter 1.980 nm.
  - <110>: 1190 atoms total (702 Cr + 488 Nb), length 4.81 nm (2.36 nm Cr + 2.45 nm Nb), Cr diameter 2.060 nm, Nb diameter 2.034 nm.
  - <111>: 1221 atoms total (637 Cr + 584 Nb), length 3.93 nm (1.70 nm Cr + 2.23 nm Nb), Cr diameter 2.355 nm, Nb diameter 2.349 nm.
  Ensure the crystallographic orientation aligns the tensile axis along the given direction and that the Cr-Nb interface consists of a single chain of atoms through the centre.
- Evidence: `/app/outputs/initial_configurations.log`

### Step 3: Run MD tensile simulation
- Role: process
- Action: For each orientation, perform a constant-strain-rate molecular dynamics tensile simulation at 300 K. Elongate the bicrystal by 0.0001 nm per iteration with a time step of 5 fs, applying thermalization every 50 iterations. Continue until failure (loss of load-bearing ability). Record per-step atomic positions, potential energy, number of pair interactions, and stress.
- Evidence: `/app/outputs/simulation_summary.json`

### Step 4: Derive mechanical properties and export results
- Role: scored (load-bearing)
- Action: From the simulation trajectories, compute the engineering stress‑strain curves for each orientation. Determine Young's modulus (initial linear region), yield stress (using a 0.2% offset or equivalent consistent criterion), ultimate tensile strength, total elongation at failure, and work of deformation up to failure. Report all values in a single CSV file.
- Output file: `/app/outputs/tensile_properties.csv`
- Format: csv
- Contract: Columns: orientation (string), elongation_at_failure_percent (float), Young_modulus_GPa (float), yield_strength_GPa (float), total_elongation_percent (float), work_of_deformation_GJm3 (float), ultimate_strength_GPa (float). One row per orientation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tensile_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tensile_properties.csv
- path: `/app/outputs/tensile_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Derived mechanical properties for Cr-Nb bicrystals pulled along <100>, <110>, <111>. Checker applies tolerances: elongation ±2%, modulus ±10 GPa, strength ±1.5 GPa, work of deformation ±0.1 GJ/m³, and verifies elongation ordering <100> > <110> > <111>.
- schema:
  - `type`: table
  - `required_columns`: `orientation`, `elongation_at_failure_percent`, `Young_modulus_GPa`, `yield_strength_GPa`, `total_elongation_percent`, `work_of_deformation_GJm3`, `ultimate_strength_GPa`
  - `units`:
    - `Young_modulus_GPa`: GPa
    - `yield_strength_GPa`: GPa
    - `ultimate_strength_GPa`: GPa
    - `elongation_at_failure_percent`: percent
    - `total_elongation_percent`: percent
    - `work_of_deformation_GJm3`: GJ/m^3

Notes: Only the mechanical properties CSV is scored. The simulation engines may be LAMMPS or an equivalent MD code.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tensile_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "orientation",
          "elongation_at_failure_percent",
          "Young_modulus_GPa",
          "yield_strength_GPa",
          "total_elongation_percent",
          "work_of_deformation_GJm3",
          "ultimate_strength_GPa"
        ],
        "units": {
          "Young_modulus_GPa": "GPa",
          "yield_strength_GPa": "GPa",
          "ultimate_strength_GPa": "GPa",
          "elongation_at_failure_percent": "percent",
          "total_elongation_percent": "percent",
          "work_of_deformation_GJm3": "GJ/m^3"
        }
      },
      "description": "Derived mechanical properties for Cr-Nb bicrystals pulled along <100>, <110>, <111>. Checker applies tolerances: elongation ±2%, modulus ±10 GPa, strength ±1.5 GPa, work of deformation ±0.1 GJ/m³, and verifies elongation ordering <100> > <110> > <111>."
    }
  ],
  "notes": "Only the mechanical properties CSV is scored. The simulation engines may be LAMMPS or an equivalent MD code."
}
```

## How you are scored
A hidden verifier independently checks each workflow stage's output artifact and combines the results into a final reward. The verifier reads your `tensile_properties.csv` and compares the reported mechanical property values for each orientation against a hidden reference; it also checks that your simulation evidence (potential parameters, initial configurations, simulation summary) is internally consistent. The final score reflects how well your computed results match the reference values and that your workflow has correctly executed each required step.
