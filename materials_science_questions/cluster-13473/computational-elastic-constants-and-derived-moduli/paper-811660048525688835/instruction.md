# Mechanical Properties of Defective Graphene Sheets from MD Simulations

## Problem background
Graphene, a single layer of carbon atoms arranged in a honeycomb lattice, exhibits exceptional mechanical strength and elasticity. Structural defects, particularly vacancies (missing carbon atoms), are known to degrade these properties. When multiple vacancies are present, their stress concentration fields may overlap if the defects are close, leading to a greater reduction in strength than a single isolated vacancy. As the separation distance increases, the interaction weakens, and at some threshold distance the double vacancy is expected to behave mechanically like a single vacancy. This task investigates the effect of double vacancy separation distance on the mechanical properties of single-layer graphene sheets (SLGSs) and aims to determine the threshold separation distance beyond which double vacancies revert to single-vacancy behaviour.

## Approach
Molecular dynamics (MD) simulations using the Tersoff-Brenner potential are employed to model carbon-carbon interactions. Initial atomistic models of square graphene sheets (8.5 nm side, ∼2950 atoms) are built: a perfect sheet, a sheet with a single missing atom (single vacancy, SV), and nine sheets containing two missing atoms (double vacancy, DV) separated by distances ranging from 4.26 Å to 68.16 Å along the loading direction. An additional rectangular sheet (14 nm × 5 nm) with three vacancies at the expected threshold distance is also constructed. Each configuration is energy-minimised and equilibrated at 300 K for 3 ps under a Nose-Hoover thermostat with a 1 fs time step. Uniaxial tensile loading is then applied in the zigzag (longitudinal) direction by incrementally displacing one end by 0.05 Å and relaxing for 2 ps after each step; axial stress and engineering strain are recorded until fracture. From the resulting stress–strain curves, Young’s modulus (initial linear slope), critical stress (maximum stress), and critical strain (strain at failure) are extracted for every sample. The threshold distance is defined as the smallest studied double-vacancy separation where the critical stress reduction relative to the single-vacancy case falls below 0.5 %. The approach thus compares the mechanical properties across all defect configurations and determines the threshold separation distance from the computed strength reduction trend.

## Reproduction target
Compute and report the mechanical properties (Young’s modulus, critical stress, critical strain) for each of the following graphene configurations:
- A perfect 8.5 nm square sheet.
- A square sheet containing a single vacancy (SV).
- Nine square sheets with double vacancies at separation distances 4.26, 8.52, 17.04, 25.56, 34.08, 42.60, 51.12, 59.64, and 68.16 Å.
- A rectangular 14 nm × 5 nm sheet containing three vacancies spaced 46.86 Å apart.
Determine the threshold separation distance D_thr (in Å) as the smallest double-vacancy separation among the nine distances for which the critical stress is within 0.5% of the single-vacancy critical stress. Save all results in `/app/outputs/simulation_results.json` following the specified JSON schema. The JSON must contain an array of sample objects (each with sample_id, type, separation distance, Young_modulus_TPa, critical_stress_GPa, critical_strain_percent) and the single number `threshold_distance_Angstrom`.

## Assets

- LAMMPS: https://www.lammps.org/
- Python 3 with scientific packages: numpy, scipy

## Workflow steps

### Step 1: Build and equilibrate graphene atomic models
- Role: process
- Action: Generate initial atomic coordinates for all required graphene configurations: perfect 8.5 nm square sheet (~2950 atoms), sheet with a single vacancy, nine sheets with double vacancies at separation distances 4.26 Å, 8.52 Å, 17.04 Å, 25.56 Å, 34.08 Å, 42.60 Å, 51.12 Å, 59.64 Å, 68.16 Å, and a rectangular 14 nm × 5 nm sheet with triple vacancies at 46.86 Å spacing. Perform energy minimization and equilibrate each system at 300 K for 3 ps using LAMMPS with the Tersoff-Brenner potential, Nose-Hoover thermostat, and a 1 fs timestep.
- Evidence: none

### Step 2: Run MD tensile simulations
- Role: process
- Action: For each equilibrated configuration, apply uniaxial tensile loading in the longitudinal (zigzag) direction by incrementally displacing one end by 0.05 Å and relaxing for 2 ps after each step, while recording the axial stress and engineering strain. Continue loading until fracture. Produce stress-strain data for every sample.
- Evidence: none

### Step 3: Extract mechanical properties and threshold distance
- Role: scored (load-bearing)
- Action: From the stress-strain curves, compute for each sample: Young's modulus (initial linear-elastic slope), critical stress (maximum stress), and critical strain (strain at failure). Determine the threshold separation distance D_thr as the smallest double-vacancy separation distance (from the nine simulated) where the critical stress reduction relative to the single-vacancy case falls below 0.5%. Report all results in a single JSON file.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: JSON object with keys: 'samples' (array of sample objects, each with sample_id (string), type (string: 'perfect','SV','DV','TV'), separation_distance_Angstrom (number, null for perfect/SV), Young_modulus_TPa (number), critical_stress_GPa (number), critical_strain_percent (number)), and 'threshold_distance_Angstrom' (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mechanical properties computed for each graphene configuration and the threshold separation distance where double vacancies behave like a single vacancy.
- schema:
  - `type`: object
  - `required`: `samples`, `threshold_distance_Angstrom`
  - `properties`:
    - `samples`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `sample_id`, `type`, `Young_modulus_TPa`, `critical_stress_GPa`, `critical_strain_percent`
        - `properties`:
          - `sample_id`:
            - `type`: string
          - `type`:
            - `type`: string
            - `enum`: `perfect`, `SV`, `DV`, `TV`
          - `separation_distance_Angstrom`:
            - `type`: number
          - `Young_modulus_TPa`:
            - `type`: number
          - `critical_stress_GPa`:
            - `type`: number
          - `critical_strain_percent`:
            - `type`: number
    - `threshold_distance_Angstrom`:
      - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "samples",
          "threshold_distance_Angstrom"
        ],
        "properties": {
          "samples": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "sample_id",
                "type",
                "Young_modulus_TPa",
                "critical_stress_GPa",
                "critical_strain_percent"
              ],
              "properties": {
                "sample_id": {
                  "type": "string"
                },
                "type": {
                  "type": "string",
                  "enum": [
                    "perfect",
                    "SV",
                    "DV",
                    "TV"
                  ]
                },
                "separation_distance_Angstrom": {
                  "type": "number"
                },
                "Young_modulus_TPa": {
                  "type": "number"
                },
                "critical_stress_GPa": {
                  "type": "number"
                },
                "critical_strain_percent": {
                  "type": "number"
                }
              }
            }
          },
          "threshold_distance_Angstrom": {
            "type": "number"
          }
        }
      },
      "description": "Mechanical properties computed for each graphene configuration and the threshold separation distance where double vacancies behave like a single vacancy."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `simulation_results.json` and compares each reported mechanical property against reference values derived from the original paper. For every sample, it checks Young’s modulus, critical stress, and critical strain with appropriate tolerances that account for the expected spread of an independent MD re-run. The verifier also validates the threshold distance by ensuring it satisfies the 0.5 % strength‑reduction criterion and is the smallest among the nine simulated distances that meets it. Each sample’s properties and the threshold distance contribute a weighted fraction to a total score between 0 and 1. Submitting the correct file with the required structure is necessary but not sufficient—the numerical values must be the result of genuine simulations; fabricated or guessed numbers are unlikely to pass the tolerance checks.
