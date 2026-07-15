# MD simulations of defected graphene: Young's modulus and thermal conductivity

## Problem background
Monolayer graphene exhibits outstanding mechanical stiffness and thermal conductivity, but structural defects such as monatomic vacancies and Stone-Wales dislocations can alter these properties. Understanding how the concentration and type of defect affect Young's modulus and thermal transport is essential for evaluating the quality of graphene in applications. This task investigates those effects using molecular dynamics, with the goal of computing how these properties change as a function of defect concentration and temperature.

## Approach
Molecular dynamics (MD) simulations are performed on square monolayer graphene sheets (6 nm side, periodic boundary conditions) using the AIREBO potential to describe carbon–carbon interactions. Defect configurations are created by introducing monatomic vacancies and Stone-Wales dislocations at concentrations ranging from 0% (pristine) to approximately 4%. Each structure is equilibrated at 300 K and 1 atm, then subjected to two types of simulation: uniaxial tensile loading to extract the Young's modulus from the stress–strain response, and equilibrium Green-Kubo runs to obtain the in-plane thermal conductivity by integrating the heat flux autocorrelation function. Temperature-dependent thermal conductivity is also investigated by repeating the Green-Kubo procedure for pristine graphene and for a sheet with 2% monatomic vacancies at several temperatures between 100 K and 500 K. All results are compared between defect types and against the defect-free baseline.

## Reproduction target
Compute the Young's modulus and thermal conductivity of monolayer graphene containing monatomic vacancies and Stone-Wales dislocations at 300 K, for defect concentrations from 0% to ~4%. Additionally, compute the thermal conductivity of pristine graphene and of a graphene sheet with 2% monatomic vacancies at temperatures of 100, 150, 200, 250, 300, 350, 400, 450, and 500 K. Write the results to the specified CSV output files with the required columns.

## Assets

- LAMMPS: https://lammps.sandia.gov/download.html
- AIREBO potential: lammps

## Workflow steps

### Step 1: Generate defected graphene structures
- Role: process
- Action: Create atomic configurations of square monolayer graphene sheets (6 nm side, periodic boundary conditions) with desired defect types (monatomic vacancies, Stone‑Wales dislocations) and concentrations (0% to ~4%). Output LAMMPS data files for each configuration.
- Evidence: none

### Step 2: Equilibrate structures
- Role: process
- Action: For each generated structure, run NPT equilibration at T=300 K and P=1 atm using a Nosé‑Hoover thermostat for 500 ps. Save the equilibrated configuration.
- Evidence: `/app/outputs/equil.log`

### Step 3: Tensile test and Young's modulus
- Role: scored (load-bearing)
- Action: Perform uniaxial tensile loading on each equilibrated structure (relax the perpendicular direction), collect stress–strain data, and extract the Young's modulus from the linear elastic region. Write the computed modulus for each defect type and concentration to the output CSV.
- Output file: `/app/outputs/mechanical_results.csv`
- Format: csv
- Contract: defect_type (string: 'pristine','vacancy','SW'), concentration (float, fraction), Youngs_modulus_TPa (float)
- Scoring: scored by hidden verifier

### Step 4: Thermal conductivity at 300 K
- Role: scored
- Action: From the equilibrated configurations, switch to microcanonical ensemble (NVE), collect atomic velocities, compute the heat flux autocorrelation, and integrate using the Green‑Kubo formula to obtain the thermal conductivity at 300 K. Average over multiple independent runs (3 samples × 2 runs). Write the results for each defect type and concentration in the CSV.
- Output file: `/app/outputs/thermal_results.csv`
- Format: csv
- Contract: defect_type (string), concentration (float, fraction), thermal_conductivity_WmK (float)
- Scoring: scored by hidden verifier

### Step 5: Temperature‑dependent thermal conductivity
- Role: scored
- Action: For pristine graphene and for graphene with 2% monatomic vacancies, run Green‑Kubo simulations after NPT equilibration at several temperatures (e.g., 100, 150, 200, 250, 300, 350, 400, 450, 500 K). Extract the thermal conductivity at each temperature and write the data to the CSV.
- Output file: `/app/outputs/thermal_vs_temp.csv`
- Format: csv
- Contract: defect_type (string), concentration (float, fraction), temperature_K (float), thermal_conductivity_WmK (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_results.csv`
- `/app/outputs/thermal_results.csv`
- `/app/outputs/thermal_vs_temp.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_results.csv
- path: `/app/outputs/mechanical_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Young's modulus of defected graphene sheets as a function of defect type and concentration, extracted from MD tensile tests. Checker compares to paper‑reported values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `concentration`, `Youngs_modulus_TPa`

### thermal_results.csv
- path: `/app/outputs/thermal_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity at 300 K of defected graphene from equilibrium Green‑Kubo MD. Checker compares to paper‑reported values and inverse‑linear fits.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `concentration`, `thermal_conductivity_WmK`

### thermal_vs_temp.csv
- path: `/app/outputs/thermal_vs_temp.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature‑dependent thermal conductivity of pristine and 2%‑vacancy graphene. Checker verifies the peak location and magnitude against the paper.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `concentration`, `temperature_K`, `thermal_conductivity_WmK`

Notes: The process steps (structure generation and equilibration) are required to produce the starting configurations for the scored simulations. The temperature‑dependent step may be omitted if compute resources are limited, but it is part of the full reproduction target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "concentration",
          "Youngs_modulus_TPa"
        ]
      },
      "description": "Young's modulus of defected graphene sheets as a function of defect type and concentration, extracted from MD tensile tests. Checker compares to paper‑reported values with tolerance."
    },
    {
      "file": "thermal_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "concentration",
          "thermal_conductivity_WmK"
        ]
      },
      "description": "Thermal conductivity at 300 K of defected graphene from equilibrium Green‑Kubo MD. Checker compares to paper‑reported values and inverse‑linear fits."
    },
    {
      "file": "thermal_vs_temp.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "concentration",
          "temperature_K",
          "thermal_conductivity_WmK"
        ]
      },
      "description": "Temperature‑dependent thermal conductivity of pristine and 2%‑vacancy graphene. Checker verifies the peak location and magnitude against the paper."
    }
  ],
  "notes": "The process steps (structure generation and equilibration) are required to produce the starting configurations for the scored simulations. The temperature‑dependent step may be omitted if compute resources are limited, but it is part of the full reproduction target."
}
```

## How you are scored
A hidden verifier independently inspects each scored output file. For the mechanical and thermal properties, it compares the values you report at the requested defect concentrations and temperatures against hidden reference targets. Agreement within an acceptable range yields full credit; larger deviations reduce the score according to a monotonic scale. The verifier also assesses whether the trends among defect types, concentrations, and temperatures are physically consistent. The final reward is a weighted combination of the scores from all scored artifacts.
