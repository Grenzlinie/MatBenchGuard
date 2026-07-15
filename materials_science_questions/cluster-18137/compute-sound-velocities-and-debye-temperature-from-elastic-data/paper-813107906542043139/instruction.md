# Compute Elastic, Mechanical, and Thermodynamic Properties of BCC FeCrCoMnAl High-Entropy Alloys from First Principles

## Problem background
Body‑centered cubic FeCrCoMnAlₓ high‑entropy alloys are promising structural materials. First‑principles calculations can reveal how the aluminium content influences fundamental mechanical and thermal properties such as single‑crystal elastic constants, polycrystalline moduli, sound velocities, Debye temperature, Curie temperature, and ideal tensile strength. Understanding these trends is essential for alloy design.

## Approach
Use density‑functional theory (DFT) with the PBE exchange‑correlation functional. Model the random bcc solid solutions with special quasirandom structures (SQS) generated for the target compositions. Perform total‑energy calculations for ferromagnetic and paramagnetic states to obtain equilibrium structures and Curie‑temperature estimates. Compute elastic constants via small energy‑strain distortions, derive polycrystalline moduli by Voigt–Reuss–Hill averaging, calculate sound velocities and the Debye temperature from the moduli and mass density, and determine the ideal tensile strength along [001] from a stress–strain curve with lateral relaxation. An open‑source DFT code such as Quantum ESPRESSO is suitable.

## Reproduction target
Compute single‑crystal elastic constants C₁₁, C₁₂, C₄₄ for compositions x = 0.6 and x = 1.0. For x = 1.0 also compute the full set of polycrystalline moduli (bulk modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio ν, Zener anisotropy A_Z, and Pugh ratio B/G), the sound velocities (v_L, v_T, v_m) and Debye temperature θ_D, the Curie temperature T_C from the ferromagnetic–paramagnetic energy difference, and the ideal tensile strength (peak stress and strain) under [001] tension. All results are to be written as structured CSV files in the specified formats.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Fe, Cr, Co, Mn, Al: https://pseudopotentials.quantum-espresso.org/
- ATAT (mcsqs): https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/
- thermo_pw (optional): https://github.com/dalcorso/thermo_pw

## Workflow steps

### Step 1: DFT structural optimization and magnetic energy calculation
- Role: process
- Action: For FeCrCoMnAl_x with x=0.6 and 1.0, construct bcc SQS supercells. Perform DFT total-energy calculations to relax the volume for both ferromagnetic (FM) and paramagnetic (PM) states, obtaining equilibrium lattice parameter (or Wigner-Seitz radius) and total energies E_FM and E_PM. Save these results in optimization_results.json.
- Evidence: `/app/outputs/optimization_results.json`

### Step 2: Single-crystal elastic constants
- Role: scored (load-bearing)
- Action: Using the equilibrium structures from step 1, apply small strain tensors and fit energy-strain curves to obtain the three independent elastic constants C11, C12, C44 for both x=0.6 and 1.0. Store results in elastic_constants.csv.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: Columns: composition (float), C11 (GPa), C12 (GPa), C44 (GPa). Exactly two rows.
- Scoring: scored by hidden verifier

### Step 3: Polycrystalline mechanical properties
- Role: scored
- Action: From the elastic constants for x=1.0, compute the polycrystalline bulk modulus B, shear modulus G (Voigt-Reuss-Hill average), Young's modulus E, Poisson's ratio v, Zener anisotropy A_Z, and Pugh ratio B/G using standard formulas. Write the results to polycrystalline_moduli.csv.
- Output file: `/app/outputs/polycrystalline_moduli.csv`
- Format: csv
- Contract: Columns: composition, B, G, E, v, A_Z, B_over_G. One row for x=1.0.
- Scoring: scored by hidden verifier

### Step 4: Sound velocities and Debye temperature
- Role: scored
- Action: Using B and G from step 3 for x=1.0, together with the mass density ρ obtained from the equilibrium lattice parameter and molar mass, compute the transverse vT, longitudinal vL, and average vm sound velocities, then the Debye temperature θD. Output to debye_temperature.csv.
- Output file: `/app/outputs/debye_temperature.csv`
- Format: csv
- Contract: Columns: composition, theta_D, vL, vT, vm. Units as indicated.
- Scoring: scored by hidden verifier

### Step 5: Curie temperature estimation
- Role: scored
- Action: From the FM and PM total energies for x=1.0 obtained in step 1, estimate the Curie temperature using the mean-field formula where Tc depends on the energy difference and Al concentration. Write the result to curie_temperature.csv.
- Output file: `/app/outputs/curie_temperature.csv`
- Format: csv
- Contract: Columns: composition, T_C. One row for x=1.0.
- Scoring: scored by hidden verifier

### Step 6: Ideal tensile strength along [001]
- Role: scored
- Action: For the x=1.0 bcc structure, apply uniaxial strain along [001] with relaxation of perpendicular lattice vectors, compute the stress-strain curve, and identify the maximum stress sigma_m and the strain epsilon_m at which it occurs. Write to ideal_tensile_strength.csv.
- Output file: `/app/outputs/ideal_tensile_strength.csv`
- Format: csv
- Contract: Columns: composition, sigma_max, epsilon_max. One row for x=1.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/polycrystalline_moduli.csv`
- `/app/outputs/debye_temperature.csv`
- `/app/outputs/ideal_tensile_strength.csv`
- `/app/outputs/curie_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Single-crystal elastic constants for x=0.6 and 1.0. Columns: composition (float), C11 (GPa), C12 (GPa), C44 (GPa).
- schema:
  - `type`: table
  - `required_columns`: `composition`, `C11`, `C12`, `C44`

### polycrystalline_moduli.csv
- path: `/app/outputs/polycrystalline_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Polycrystalline moduli and derived ratios for x=1.0. B, G, E in GPa; v, A_Z, B_over_G dimensionless.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `B`, `G`, `E`, `v`, `A_Z`, `B_over_G`

### debye_temperature.csv
- path: `/app/outputs/debye_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sound velocities and Debye temperature for x=1.0. theta_D in K; velocities in m/s.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `theta_D`, `vL`, `vT`, `vm`

### ideal_tensile_strength.csv
- path: `/app/outputs/ideal_tensile_strength.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ideal tensile strength for x=1.0 under [001] tension. sigma_max in GPa, epsilon_max as fraction.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `sigma_max`, `epsilon_max`

### curie_temperature.csv
- path: `/app/outputs/curie_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Curie temperature for x=1.0 in K.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `T_C`

Notes: The polycrystalline_moduli.csv column naming includes 'B_over_G' for the Pugh ratio. All numeric comparisons will be performed with hidden tolerances appropriate for DFT reproducibility.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "C11",
          "C12",
          "C44"
        ]
      },
      "description": "Single-crystal elastic constants for x=0.6 and 1.0. Columns: composition (float), C11 (GPa), C12 (GPa), C44 (GPa)."
    },
    {
      "file": "polycrystalline_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "B",
          "G",
          "E",
          "v",
          "A_Z",
          "B_over_G"
        ]
      },
      "description": "Polycrystalline moduli and derived ratios for x=1.0. B, G, E in GPa; v, A_Z, B_over_G dimensionless."
    },
    {
      "file": "debye_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "theta_D",
          "vL",
          "vT",
          "vm"
        ]
      },
      "description": "Sound velocities and Debye temperature for x=1.0. theta_D in K; velocities in m/s."
    },
    {
      "file": "ideal_tensile_strength.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "sigma_max",
          "epsilon_max"
        ]
      },
      "description": "Ideal tensile strength for x=1.0 under [001] tension. sigma_max in GPa, epsilon_max as fraction."
    },
    {
      "file": "curie_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "T_C"
        ]
      },
      "description": "Curie temperature for x=1.0 in K."
    }
  ],
  "notes": "The polycrystalline_moduli.csv column naming includes 'B_over_G' for the Pugh ratio. All numeric comparisons will be performed with hidden tolerances appropriate for DFT reproducibility."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s output artifact. Each artifact is compared to a reference target using appropriate tolerances, and the stage scores are combined by their assigned weights to produce the final reward. Reporting paper‑reported numbers without executing the full workflow will not earn credit; the verifier assesses the correctness of the computed results.
