# Mechanical properties and failure mechanisms of borophene allotropes under uniaxial tension

## Problem background
Two‑dimensional (2D) materials are promising building blocks for future nanotechnology. Among them, borophene—a monolayer of boron atoms—exists in several allotropes with distinct atomic structures, including arrangements that contain vacant hexagonal sites or continuous rows of atoms. Understanding the mechanical response and failure modes of these allotropes under tensile loading is important for their integration into robust devices. This task investigates the tensile mechanical properties (Young’s modulus, yield stress, yield strain) and the failure mechanisms of five borophene allotropes (labelled S1 through S5), and contrasts them with two reference 2D materials: graphene and hexagonal boron nitride (h‑BN).

## Approach
The procedure uses classical molecular dynamics (MD) with the ReaxFF reactive force field. For each structure (S1–S5, graphene, h‑BN), a periodic sheet of approximately 5 nm × 5 nm is constructed from the known lattice parameters. The simulation is performed with LAMMPS, employing the appropriate ReaxFF parameter set for each material (a boron parameterisation for the borophene allotropes, a C/H set for graphene, and a B/N set for h‑BN). After an equilibration stage in an NPT ensemble at 300 K to relax the structure, the sheet is subjected to uniaxial tensile deformation at a constant engineering strain rate along two orthogonal directions (armchair and zigzag). Stress–strain data are recorded throughout the deformation. From the resulting stress–strain curves, the linear elastic slope yields the Young’s modulus, the maximum stress gives the yield stress, and the corresponding strain is the yield strain. The final atomic configuration at failure is examined to classify the failure mechanism as one of three types: ‘cracking’ (the sheet separates into distinct parts), ‘nanopore’ (multiple holes form without a clean cleavage), or ‘cleavage’ (a clean break, expected for graphene/h‑BN).

## Reproduction target
Produce a single CSV file, `mechanical_properties.csv`, containing one row for each combination of structure and loading direction. The rows must be labelled as `<structure>_armchair` and `<structure>_zigzag` for the seven structures: S1, S2, S3, S4, S5, graphene, and h‑BN. Each row must report:

- `Young_modulus_GPa_nm` (float): the Young’s modulus extracted from the linear elastic slope of the stress–strain curve, in units of GPa·nm.
- `yield_stress_GPa` (float): the maximum stress on the stress–strain curve, in GPa.
- `yield_strain` (float): the engineering strain at which the yield stress is reached.
- `failure_mechanism` (string): one of `'cracking'`, `'nanopore'`, or `'cleavage'`.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- ReaxFF parameter file for boron: 10.1021/jp1029408
- ReaxFF parameter file for C/H (graphene): 10.1021/jp074964f
- ReaxFF parameter file for B/N (h-BN)
- Borophene structure coordinates and lattice parameters: 10.1039/C6CP05117J

## Workflow steps

### Step 1: Atomic structure generation and MD tensile testing simulations
- Role: process
- Action: Construct atomic configurations for borophene allotropes S1, S2, S3, S4, S5, graphene, and h-BN sheets of approximately 5 nm × 5 nm using published lattice parameters. For each structure, run NPT equilibration at 300 K with LAMMPS and the appropriate ReaxFF potential, then apply uniaxial tensile deformation at a strain rate of 0.0001 1/ps along armchair and zigzag directions. Record stress–strain data and final trajectory frames.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Property extraction and failure classification
- Role: scored (load-bearing)
- Action: From the stress–strain curves, compute Young's modulus from the linear elastic slope, yield stress as the maximum stress, and yield strain. Analyze the final atomic configurations to classify the failure mechanism: 'cracking', 'nanopore', or 'cleavage' (for graphene/h-BN). Compile all results for every structure and loading direction into a CSV file.
- Output file: `/app/outputs/mechanical_properties.csv`
- Format: csv
- Contract: Columns: structure (string, e.g. 'S1_armchair', 'S1_zigzag', 'graphene_armchair', ...), Young_modulus_GPa_nm (float), yield_stress_GPa (float), yield_strain (float, optional), failure_mechanism (string: 'cracking' | 'nanopore' | 'cleavage'). One row per simulation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_properties.csv
- path: `/app/outputs/mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mechanical properties and failure classification from MD tensile tests.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `Young_modulus_GPa_nm`, `yield_stress_GPa`, `yield_strain`, `failure_mechanism`
  - `units`:
    - `Young_modulus_GPa_nm`: GPa·nm
    - `yield_stress_GPa`: GPa
    - `yield_strain`: dimensionless

Notes: Yield strain is not required for scoring but is included for completeness. The hidden checker compares Young's modulus and yield stress against reference values with a tolerance, and failure_mechanism against known labels.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "Young_modulus_GPa_nm",
          "yield_stress_GPa",
          "yield_strain",
          "failure_mechanism"
        ],
        "units": {
          "Young_modulus_GPa_nm": "GPa·nm",
          "yield_stress_GPa": "GPa",
          "yield_strain": "dimensionless"
        }
      },
      "description": "Mechanical properties and failure classification from MD tensile tests."
    }
  ],
  "notes": "Yield strain is not required for scoring but is included for completeness. The hidden checker compares Young's modulus and yield stress against reference values with a tolerance, and failure_mechanism against known labels."
}
```

## How you are scored
Your submitted `mechanical_properties.csv` is evaluated automatically by a hidden verifier. For each row, the verifier compares your reported Young’s modulus and yield stress against confidential reference values using tolerances that account for legitimate implementation spread. The failure mechanism string is checked against an expected label. The reward is a weighted combination of the quantitative mechanical properties and the failure mechanism classification, with greater weight placed on the mechanical properties. The scoring function rewards accuracy monotonically: the closer your computed values are to the expected ones (or the more favourable the values are, when a directional metric is used), the higher your credit. You do not need to exactly reproduce a specific table entry from the literature; only a valid CSV file following the output contract is required.
