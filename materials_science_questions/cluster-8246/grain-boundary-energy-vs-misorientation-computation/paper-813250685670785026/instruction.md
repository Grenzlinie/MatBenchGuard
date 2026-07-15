# DFT computation of mechanical properties of twisted bilayer graphene and bilayer graphene with grain boundaries

## Problem background
Bilayer graphene is a promising two-dimensional material for electronic and mechanical applications. Structural features such as the relative twist angle between layers and the presence of grain boundaries can significantly alter its mechanical properties. Understanding how intrinsic tensile strength, critical failure strain, and Young's modulus depend on twist angle and grain boundary misorientation is essential for predicting device reliability. This task computes these mechanical properties using first-principles density functional theory (DFT) simulations, covering a systematic set of twist angles and grain boundary configurations.

## Approach
The workflow uses the open-source Quantum ESPRESSO code with projector-augmented wave (PAW) pseudopotentials and the PBE exchange-correlation functional, including Grimme D2 van der Waals corrections, to perform DFT calculations. First, atomic supercell models of twisted bilayer graphene (8 twist angles) and bilayer graphene with one layer containing a grain boundary (6 configurations with zigzag and armchair orientations) are built using the Atomic Simulation Environment (ASE). Each structure is fully relaxed (both lattice parameters and atomic positions) to obtain the equilibrium geometry. Uniaxial tensile strain is then applied in 1% increments, with full atomic relaxation at each step, and the resulting stress component along the stretching direction is computed from the stress theorem and rescaled by the ratio Z/d (Z = 2 nm vacuum thickness; d = twice the interlayer distance) to obtain the in-plane sheet stress. Stress-strain curves are collected for every configuration, from which the intrinsic strength (peak stress), critical failure strain (strain at failure), and Young's modulus (elastic slope) are extracted.

## Reproduction target
Produce the following scored output files:

- tBLG_results.csv: for each of the 8 twist angles (5.0°, 7.3°, 9.4°, 13.2°, 21.8°, 32.2°, 38.2°, 42.1°), report the computed intrinsic strength (GPa), critical failure strain (%), and Young's modulus (GPa). The CSV must have columns: twist_angle_deg, intrinsic_strength_GPa, critical_failure_strain_percent, Youngs_modulus_GPa; values rounded to two decimals.

- BLG_GB_results.csv: for each of the 6 grain boundary configurations (zigzag: 7.3°, 13.7°, 22.6°; armchair: 17.5°, 20.9°, 27.4°), report the computed intrinsic strength (GPa), critical failure strain (%), and Young's modulus (GPa). The CSV must have columns: misorientation_angle_deg, orientation_type, intrinsic_strength_GPa, critical_failure_strain_percent, Youngs_modulus_GPa; values rounded to two decimals.

The verifier will check the reported values against hidden reference data and verify that the mechanical properties exhibit certain monotonic trends (e.g., how strength varies with twist angle or misorientation angle).

## Assets

- Quantum ESPRESSO (version 7.2 or later): https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE, version 3.22 or later): https://wiki.fysik.dtu.dk/ase/
- PAW pseudopotentials for carbon (PBE functional, e.g., C.pbe-n-rrkjus_psl.1.0.0.UPF from SSSP library): https://www.materialscloud.org/discover/sssp/table/ptable/pseudopotentials
- Python packages: numpy, scipy, matplotlib: pip install numpy scipy matplotlib

## Workflow steps

### Step 1: Generate initial atomic structures
- Role: process
- Action: Construct supercell models for eight tBLG twist angles (5°, 7.3°, 9.4°, 13.2°, 21.8°, 32.2°, 38.2°, 42.1°) and six BLG-GB configurations (zigzag: 7.3°, 13.7°, 22.6°; armchair: 17.5°, 20.9°, 27.4°) using ASE to create twisted bilayer graphene and grain boundary structures with appropriate supercell sizes.
- Evidence: `/app/outputs/model_summary.txt`

### Step 2: Relax structures with DFT
- Role: process
- Action: Perform full geometry relaxation of all tBLG and BLG-GB supercells using Quantum ESPRESSO with PAW pseudopotentials, PBE functional, Grimme D2 vdW correction, a plane-wave cutoff of 400 eV, and 2 nm vacuum space. Relax both supercell dimensions and atomic positions.
- Evidence: none

### Step 3: Run tensile strain simulations
- Role: process
- Action: For each relaxed structure, apply uniaxial tensile strain along the zigzag direction (tBLG) or perpendicular to the grain boundary line (BLG-GB) in 1% increments. At each strain step, fully relax atomic coordinates, compute the stress component via the stress theorem, and rescale by Z/d (Z=2 nm, d=twice the interlayer distance) to obtain in-plane sheet stress. Record the rescaled stress vs. strain for all configurations in a JSON evidence file.
- Evidence: `/app/outputs/stress_strain_data.json`

### Step 4: Extract tBLG mechanical properties
- Role: scored
- Action: From the stress-strain curves for tBLG configurations, determine the intrinsic tensile strength (peak rescaled stress in GPa), critical failure strain (strain at failure in %), and Young's modulus (slope in the elastic regime in GPa) for each twist angle. Write the results to tBLG_results.csv.
- Output file: `/app/outputs/tBLG_results.csv`
- Format: csv
- Contract: Columns: twist_angle_deg (float), intrinsic_strength_GPa (float), critical_failure_strain_percent (float), Youngs_modulus_GPa (float). One row per twist angle: 5.0, 7.3, 9.4, 13.2, 21.8, 32.2, 38.2, 42.1. Values rounded to two decimals.
- Scoring: scored by hidden verifier

### Step 5: Extract BLG-GB mechanical properties
- Role: scored
- Action: From the stress-strain curves for BLG-GB configurations, determine the intrinsic tensile strength, critical failure strain, and Young's modulus for each grain boundary. Write results to BLG_GB_results.csv.
- Output file: `/app/outputs/BLG_GB_results.csv`
- Format: csv
- Contract: Columns: misorientation_angle_deg (float), orientation_type (string: 'zigzag' or 'armchair'), intrinsic_strength_GPa (float), critical_failure_strain_percent (float), Youngs_modulus_GPa (float). One row per configuration: 7.3/zigzag, 13.7/zigzag, 22.6/zigzag, 17.5/armchair, 20.9/armchair, 27.4/armchair. Values rounded to two decimals.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tBLG_results.csv`
- `/app/outputs/BLG_GB_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tBLG_results.csv
- path: `/app/outputs/tBLG_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed intrinsic strength, critical failure strain, and Young's modulus for twisted bilayer graphene at the listed twist angles.
- schema:
  - `type`: table
  - `required_columns`:
    - `name`: twist_angle_deg
    - `dtype`: float
    - `unit`: degrees
    - `name`: intrinsic_strength_GPa
    - `dtype`: float
    - `unit`: GPa
    - `name`: critical_failure_strain_percent
    - `dtype`: float
    - `unit`: %
    - `name`: Youngs_modulus_GPa
    - `dtype`: float
    - `unit`: GPa
  - `notes`: Exactly 8 rows, one per twist angle: 5.0, 7.3, 9.4, 13.2, 21.8, 32.2, 38.2, 42.1. Values rounded to two decimal places.

### BLG_GB_results.csv
- path: `/app/outputs/BLG_GB_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed intrinsic strength, critical failure strain, and Young's modulus for bilayer graphene with a grain boundary in one layer at the listed misorientation angles.
- schema:
  - `type`: table
  - `required_columns`:
    - `name`: misorientation_angle_deg
    - `dtype`: float
    - `unit`: degrees
    - `name`: orientation_type
    - `dtype`: string
    - `unit`: 
    - `name`: intrinsic_strength_GPa
    - `dtype`: float
    - `unit`: GPa
    - `name`: critical_failure_strain_percent
    - `dtype`: float
    - `unit`: %
    - `name`: Youngs_modulus_GPa
    - `dtype`: float
    - `unit`: GPa
  - `notes`: Exactly 6 rows, one per configuration: 7.3/zigzag, 13.7/zigzag, 22.6/zigzag, 17.5/armchair, 20.9/armchair, 27.4/armchair. Values rounded to two decimal places.

Notes: The checker will compare the reported values in these CSV files against the paper's published reference values using absolute tolerances and verify monotonic trends (e.g., tBLG strength and strain must decrease with increasing twist angle; BLG-GB strength must increase with misorientation angle). The exact tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tBLG_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          {
            "name": "twist_angle_deg",
            "dtype": "float",
            "unit": "degrees"
          },
          {
            "name": "intrinsic_strength_GPa",
            "dtype": "float",
            "unit": "GPa"
          },
          {
            "name": "critical_failure_strain_percent",
            "dtype": "float",
            "unit": "%"
          },
          {
            "name": "Youngs_modulus_GPa",
            "dtype": "float",
            "unit": "GPa"
          }
        ],
        "notes": "Exactly 8 rows, one per twist angle: 5.0, 7.3, 9.4, 13.2, 21.8, 32.2, 38.2, 42.1. Values rounded to two decimal places."
      },
      "description": "Computed intrinsic strength, critical failure strain, and Young's modulus for twisted bilayer graphene at the listed twist angles."
    },
    {
      "file": "BLG_GB_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          {
            "name": "misorientation_angle_deg",
            "dtype": "float",
            "unit": "degrees"
          },
          {
            "name": "orientation_type",
            "dtype": "string",
            "unit": ""
          },
          {
            "name": "intrinsic_strength_GPa",
            "dtype": "float",
            "unit": "GPa"
          },
          {
            "name": "critical_failure_strain_percent",
            "dtype": "float",
            "unit": "%"
          },
          {
            "name": "Youngs_modulus_GPa",
            "dtype": "float",
            "unit": "GPa"
          }
        ],
        "notes": "Exactly 6 rows, one per configuration: 7.3/zigzag, 13.7/zigzag, 22.6/zigzag, 17.5/armchair, 20.9/armchair, 27.4/armchair. Values rounded to two decimal places."
      },
      "description": "Computed intrinsic strength, critical failure strain, and Young's modulus for bilayer graphene with a grain boundary in one layer at the listed misorientation angles."
    }
  ],
  "notes": "The checker will compare the reported values in these CSV files against the paper's published reference values using absolute tolerances and verify monotonic trends (e.g., tBLG strength and strain must decrease with increasing twist angle; BLG-GB strength must increase with misorientation angle). The exact tolerances are hidden."
}
```

## How you are scored
A hidden verifier loads your CSV files and compares each reported intrinsic strength, critical failure strain, and Young's modulus against reference values using pre-set tolerances. It also checks that the set of values for the twisted bilayer graphene configurations and for the grain boundary configurations satisfy specific monotonic relationships (e.g., that strength changes systematically with angle). Each configuration contributes a pass/fail, and the final reward is the fraction of configuration checks that pass, reported as a float between 0 (none pass) and 1 (all pass). Only the two CSV files are scored; intermediate evidence files are not directly graded.
