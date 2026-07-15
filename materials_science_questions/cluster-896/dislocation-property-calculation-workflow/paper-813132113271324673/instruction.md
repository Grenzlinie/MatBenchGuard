# Stored Deformation Energy from Dislocation Density-Based Crystal Viscoplasticity

## Problem background
In crystalline metals, plastic deformation accumulates dislocations, storing energy in the lattice. This stored energy provides a driving force for microstructural evolution such as strain-induced boundary migration during thermomechanical processing. Predicting how stored deformation energy depends on crystal orientation, strain, and grain interactions is essential for understanding recrystallization and texture development in polycrystalline metals.

## Approach
We use a finite-deformation, dislocation-density-based crystal viscoplasticity model. The model decomposes the deformation gradient into elastic and plastic parts, with plastic flow arising from slip on the 12 standard FCC slip systems. A dislocation density variable on each slip system evolves with a generation/annihilation law that couples to the resolved shear stress and hardening. The free energy includes a defect energy term proportional to the total dislocation density, from which the stored deformation energy is computed. The constitutive equations are time-integrated implicitly in a finite element framework.

To calibrate the model, the material parameters (elastic constants, Burgers vector, flow rule coefficients, hardening constants, and initial dislocation density) are given. The model is verified by simulating uniaxial tension of <111> and <100> aluminum single crystals and comparing stress-strain response against known hardening behavior. Once calibrated, the model is applied to plane-strain compression of two bicrystals with flat grain boundaries: one with <001>/<111> orientations and another with <001>/<634> orientations. For each bicrystal, the volume-averaged stored deformation energy per grain is computed.

## Reproduction target
For the <111> and <100> single crystals, produce the volume-averaged stored deformation energy (in MJ/m³) at several strain points up to 0.34 uniaxial tensile strain. For the <001>/<111> and <001>/<634> bicrystals, produce the volume-averaged stored deformation energy (in MJ/m³) inside each grain after 34% plane-strain compressive strain. Additionally, produce the volume-averaged engineering stress-strain curves for the two single-crystal orientations as a calibration check.

## Assets

- FCC slip system definitions: 10.1016/S0022-5096(01)00139-9
- Finite element solver: https://fenicsproject.org/
- Aluminum single crystal material parameters

## Workflow steps

### Step 1: Constitutive model implementation
- Role: process
- Action: Implement the finite-deformation crystal viscoplasticity constitutive equations (multiplicative decomposition, resolved shear stress, viscoplastic flow rule, dislocation density evolution) and the implicit time integration algorithm in an open-source finite element framework. Use the material parameters given in the instruction.
- Evidence: `/app/outputs/implementation_log.txt`

### Step 2: Single crystal stress-strain verification
- Role: scored
- Action: Simulate uniaxial tension of <111> and <100> oriented aluminum single crystals at 273 K with a constant true strain rate of 1.7e-5 s^{-1} up to 34% strain. Compute volume-averaged engineering stress-strain curves and output the data.
- Output file: `/app/outputs/stress_strain_single_crystals.csv`
- Format: csv
- Contract: Columns: strain (unitless), stress_111 (MPa), stress_100 (MPa). Multiple rows from strain 0 to 0.34.
- Scoring: scored by hidden verifier

### Step 3: Single crystal stored energy vs. strain
- Role: scored (load-bearing)
- Action: From the single crystal simulations, compute the stored deformation energy ( a μ b^2 Σ ρ^α ) as a function of strain for the <111> and <100> orientations. Output volume-averaged stored energy at multiple strain points up to 0.34.
- Output file: `/app/outputs/stored_energy_single_crystals.csv`
- Format: csv
- Contract: Columns: strain (unitless), stored_energy_111 (MJ/m^3), stored_energy_100 (MJ/m^3). Rows at least at strains 0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.34.
- Scoring: scored by hidden verifier

### Step 4: Bicrystal plane-strain compression simulation
- Role: scored (load-bearing)
- Action: Simulate plane-strain compression of two aluminum bicrystals: <001>/<111> and <001>/<634>. Use a mesh of 2000 C3D8-type elements, a flat grain boundary normal to the loading direction, and apply a compressive true strain of 34% along direction 2 at a true strain rate of 1.7e-3 s^{-1} at 298 K. Restrict lateral faces and bottom face appropriately. Compute the volume-averaged stored deformation energy within each grain and save the results.
- Output file: `/app/outputs/stored_energy_bicrystals.csv`
- Format: csv
- Contract: Columns: bicrystal (string label, e.g. Bicrystal_001_111), grain (string, e.g. 001, 111, 634), stored_energy_avg (MJ/m^3). One row per grain.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_single_crystals.csv`
- `/app/outputs/stored_energy_single_crystals.csv`
- `/app/outputs/stored_energy_bicrystals.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_single_crystals.csv
- path: `/app/outputs/stress_strain_single_crystals.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Volume-averaged engineering stress-strain curves for <111> and <100> single crystals under uniaxial tension up to 34% strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_111`, `stress_100`
  - `units`:
    - `strain`: unitless
    - `stress_111`: MPa
    - `stress_100`: MPa

### stored_energy_single_crystals.csv
- path: `/app/outputs/stored_energy_single_crystals.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Volume-averaged stored deformation energy vs. strain for <111> and <100> single crystals, derived from the same simulations.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stored_energy_111`, `stored_energy_100`
  - `units`:
    - `strain`: unitless
    - `stored_energy_111`: MJ/m^3
    - `stored_energy_100`: MJ/m^3

### stored_energy_bicrystals.csv
- path: `/app/outputs/stored_energy_bicrystals.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Volume-averaged stored deformation energy in each grain of <001>/<111> and <001>/<634> aluminum bicrystals after 34% plane-strain compression.
- schema:
  - `type`: table
  - `required_columns`: `bicrystal`, `grain`, `stored_energy_avg`
  - `units`:
    - `stored_energy_avg`: MJ/m^3

Notes: The stress-strain verification file is scored with low weight; the stored energy single-crystal and bicrystal files are the main scored reproductions. All artifacts must be produced by the agent's own implementation of the model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_single_crystals.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_111",
          "stress_100"
        ],
        "units": {
          "strain": "unitless",
          "stress_111": "MPa",
          "stress_100": "MPa"
        }
      },
      "description": "Volume-averaged engineering stress-strain curves for <111> and <100> single crystals under uniaxial tension up to 34% strain."
    },
    {
      "file": "stored_energy_single_crystals.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stored_energy_111",
          "stored_energy_100"
        ],
        "units": {
          "strain": "unitless",
          "stored_energy_111": "MJ/m^3",
          "stored_energy_100": "MJ/m^3"
        }
      },
      "description": "Volume-averaged stored deformation energy vs. strain for <111> and <100> single crystals, derived from the same simulations."
    },
    {
      "file": "stored_energy_bicrystals.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "bicrystal",
          "grain",
          "stored_energy_avg"
        ],
        "units": {
          "stored_energy_avg": "MJ/m^3"
        }
      },
      "description": "Volume-averaged stored deformation energy in each grain of <001>/<111> and <001>/<634> aluminum bicrystals after 34% plane-strain compression."
    }
  ],
  "notes": "The stress-strain verification file is scored with low weight; the stored energy single-crystal and bicrystal files are the main scored reproductions. All artifacts must be produced by the agent's own implementation of the model."
}
```

## How you are scored
A hidden verifier evaluates each scored artifact independently and combines their scores by weight to form the final reward. The verifier checks your computed stored-energy values and stress-strain curves against hidden reference expectations derived from the underlying physics and calibration targets. You must submit the required CSV files with the specified columns; missing or malformed outputs will receive no credit. Producing the correct physical behavior (e.g., correct hardening trends, plausible stored-energy magnitudes, and the expected grain-to-grain differences in bicrystals) through your own implementation is required; simply copying numbers from any source other than your own simulation is not sufficient.
