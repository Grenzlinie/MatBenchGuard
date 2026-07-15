# Cooling-rate dependence of tensile strength of amorphous silica from MD simulations

## Problem background
Amorphous silica glass (a-SiO₂) is a widely used material whose mechanical properties, particularly tensile strength, are crucial for reliability in many technological applications. The cooling rate during quenching from the melt is a processing parameter that may affect the resulting glass structure and its mechanical behavior. Understanding this relationship is important for interpreting experimental observations and designing glass with tailored performance. This task investigates the influence of cooling rate on the tensile strength of silica glass using classical molecular dynamics simulations.

## Approach
Classical molecular dynamics simulations will be performed using the LAMMPS simulator with the Vashishta three-body potential for SiO₂, which captures both two-body (steric repulsion, charge transfer) and three-body (angular bond bending, bond stretching) covalent interactions. Amorphous SiO₂ structures will be generated at multiple cooling rates by heating a random atomic configuration to a high temperature and then quenching to room temperature. The structural properties of the resulting glasses will be characterized by partial radial distribution functions (Si–O, O–O, Si–Si). Uniaxial tensile loading will be applied at a constant strain rate to obtain stress–strain curves and extract the tensile strength (maximum stress). By comparing results across different cooling rates, the dependence of tensile strength on cooling rate can be examined.

## Reproduction target
Using LAMMPS and the Vashishta potential, generate amorphous silica glass configurations at least two distinct cooling rates, compute the partial radial distribution functions for Si–O, O–O, and Si–Si pairs, and extract the first‑peak positions (most probable nearest‑neighbor distances). Perform uniaxial tensile loading simulations and extract the tensile strength (maximum stress) for each cooling rate. Output the PRDF first‑peak positions to `/app/outputs/prdf_results.csv` and the tensile strength values to `/app/outputs/tensile_strength_results.csv`.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/

## Workflow steps

### Step 1: System initialization and random configuration
- Role: process
- Action: Create a cuboid simulation cell of dimensions ~15×11×4 nm³ containing 47,988 SiO2 atoms with periodic boundary conditions. Initialize random atomic positions and define the two-body + three-body covalent interaction potential (Vashishta) with a cut-off of 5.5 Å.
- Evidence: `/app/outputs/lammps_input_setup.log`

### Step 2: Heating–quenching MD to generate amorphous samples
- Role: process
- Action: Generate multiple amorphous SiO2 samples by heating the initial random configuration to 8000 K (NVT, 200 ps), quenching to 300 K with at least two different cooling rates (e.g., factor of 10 apart) under NVT, and equilibrating at 300 K for 200 ps under NPT. Save the final equilibrated configurations for each cooling rate.
- Evidence: `/app/outputs/quench_rates.lammpstrj`

### Step 3: Compute partial radial distribution functions
- Role: process
- Action: For each equilibrated sample, compute the partial radial distribution functions g_SiO(r), g_OO(r), g_SiSi(r) using the standard definition n_αβ(r)δr = 4πr² δr ρ c_β g_αβ(r) (or equivalent LAMMPS compute). Output the raw g(r) data for each pair and cooling rate.
- Evidence: `/app/outputs/prdf_raw.csv`

### Step 4: Extract first‑peak positions from PRDFs
- Role: scored
- Action: From each equilibrated sample's PRDF data, locate the first peak maximum (most probable nearest-neighbour distance) for each atom-type pair: Si-O, O-O, Si-Si. Report the pair and the first-peak distance in Å. If multiple cooling rates were used, report one row per pair (the peak should be cooling-rate independent).
- Output file: `/app/outputs/prdf_results.csv`
- Format: csv
- Contract: CSV with columns: pair (one of Si-O, O-O, Si-Si) and r_first_peak (float, units of Å). At least three rows.
- Scoring: scored by hidden verifier

### Step 5: Uniaxial tensile loading MD simulation
- Role: process
- Action: Apply uniaxial tensile deformation to each equilibrated sample at a constant strain rate of 0.001 ps⁻¹ under NPT conditions along the chosen loading axis. Compute the virial stress tensor at every time step and output the stress–strain data (engineering strain vs stress) for each cooling rate.
- Evidence: `/app/outputs/stress_strain_data.csv`

### Step 6: Extract tensile strength and report cooling-rate trend
- Role: scored (load-bearing)
- Action: From each stress–strain curve, identify the maximum stress (tensile strength). Report the cooling rate (in K/ps) and the corresponding tensile strength (in GPa). If multiple independent samples were generated for the same cooling rate, report the average tensile strength for that rate.
- Output file: `/app/outputs/tensile_strength_results.csv`
- Format: csv
- Contract: CSV with columns: cooling_rate (float, units of K/ps) and tensile_strength (float, units of GPa). At least two rows with distinct cooling rates.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/prdf_results.csv`
- `/app/outputs/tensile_strength_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### prdf_results.csv
- path: `/app/outputs/prdf_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: First-peak positions of the partial radial distribution functions for Si-O, O-O, and Si-Si pairs. These are compared to known interatomic distances from prior simulation and experiment.
- schema:
  - `type`: table
  - `required_columns`: `pair`, `r_first_peak`
  - `units`:
    - `r_first_peak`: Å

### tensile_strength_results.csv
- path: `/app/outputs/tensile_strength_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Tensile strength (maximum stress) for each cooling rate. The relation that higher cooling rate leads to lower tensile strength is verified by checking monotonic decreasing order in the submitted rows.
- schema:
  - `type`: table
  - `required_columns`: `cooling_rate`, `tensile_strength`
  - `units`:
    - `cooling_rate`: K/ps
    - `tensile_strength`: GPa

Notes: The agent must generate amorphous samples at multiple cooling rates and perform full tensile loading simulations, not merely report a guessed trend. The structural audit on tensile strength checks monotonic decrease; the reference match on PRDF checks proximity to established distances (within a hidden tolerance). At least two cooling rates must appear in the tensile strength output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "prdf_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pair",
          "r_first_peak"
        ],
        "units": {
          "r_first_peak": "Å"
        }
      },
      "description": "First-peak positions of the partial radial distribution functions for Si-O, O-O, and Si-Si pairs. These are compared to known interatomic distances from prior simulation and experiment."
    },
    {
      "file": "tensile_strength_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "cooling_rate",
          "tensile_strength"
        ],
        "units": {
          "cooling_rate": "K/ps",
          "tensile_strength": "GPa"
        }
      },
      "description": "Tensile strength (maximum stress) for each cooling rate. The relation that higher cooling rate leads to lower tensile strength is verified by checking monotonic decreasing order in the submitted rows."
    }
  ],
  "notes": "The agent must generate amorphous samples at multiple cooling rates and perform full tensile loading simulations, not merely report a guessed trend. The structural audit on tensile strength checks monotonic decrease; the reference match on PRDF checks proximity to established distances (within a hidden tolerance). At least two cooling rates must appear in the tensile strength output."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact. The PRDF first‑peak positions will be compared against known interatomic distances for silica glasses with a tolerance that accounts for normal numerical spread. The tensile strength values across cooling rates will be checked for a structural relationship (a monotonic trend) without requiring agreement with any specific paper‑reported absolute value. A larger weight is given to the tensile strength trend, while the PRDF peaks also carry meaningful weight. The final reward is a number between 0 and 1 combining the results from all scored stages.
