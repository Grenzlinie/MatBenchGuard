# DFT Prediction of Spintronic Transitions in Mn2Sn under Uniform Strain

## Problem background
Mn2Sn in the C1b-type Heusler structure is a binary compound whose electronic and magnetic properties are of interest for spintronics. Under varying lattice strain, this material may transition between different spintronic states, including fully-compensated ferrimagnetic half-metal, spin-gapless semiconductor, and other configurations. The task is to compute these states as a function of uniform compressive strain and determine the sequence of transitions.

## Approach
Use first-principles density functional theory (DFT) with an open-source plane-wave code (e.g., Quantum ESPRESSO) and standard GGA pseudopotentials. Perform spin-polarized calculations in the antiferromagnetic configuration (antiparallel Mn spins) for the C1b Heusler crystal structure. First, compute reference energies for isolated atoms and bulk elemental crystals. Then relax the Mn2Sn unit cell to the equilibrium lattice constant and obtain the total and atom-resolved magnetic moments. Compute elastic constants (C11, C12, C44) via the stress-strain method and derive bulk modulus, shear modulus, Young's modulus, and Pugh's ratio. For a set of compressed lattice constants (5.80, 5.52, 5.50, 5.46, 5.43 Å), calculate band structures and extract indirect band gaps (majority: G-X, minority: X-L) to classify the spintronic state at each strain. Also compute formation and cohesive energies to assess stability.

## Reproduction target
Produce the following three artifacts:
- equilibrium_properties.json: equilibrium lattice constant, total and site-projected magnetic moments, formation energy, cohesive energy.
- elastic_constants.json: elastic stiffness coefficients and derived mechanical moduli (bulk, shear, Young's moduli, B/G).
- uniform_strain_classification.csv: for each of the five compressed lattice constants, the indirect band gaps and a classification label (one of FCF-HM, FCF-SGS, FCF-S, ZG-FCF-HM) based on whether the gaps indicate metallic, semiconducting, or zero-gap behavior.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP pseudopotential library (Mn and Sn): https://www.materialscloud.org/discover/sssp/table
- Mn2Sn Heusler C1b structure

## Workflow steps

### Step 1: Compute reference total energies of Mn and Sn
- Role: process
- Action: Perform DFT total energy calculations for isolated Mn and Sn atoms and for bulk Mn and Sn in their ground-state structures to obtain reference energies for cohesion and formation energy formulas.
- Evidence: none

### Step 2: Geometry optimization and ground-state determination of Mn2Sn
- Role: process
- Action: Run variable-cell relaxation of the C1b-type Mn2Sn structure in the antiferromagnetic configuration (antiparallel Mn spins) to determine the equilibrium lattice constant and the total and atom-resolved magnetic moments.
- Evidence: none

### Step 3: Record equilibrium properties and stability energies
- Role: scored (load-bearing)
- Action: From the optimized structure and reference energies, compute the equilibrium lattice constant, total and atomic magnetic moments, formation energy, and cohesion energy. Write the results to equilibrium_properties.json.
- Output file: `/app/outputs/equilibrium_properties.json`
- Format: json
- Contract: {"lattice_constant_angstrom": float, "total_magnetic_moment_muB": float, "Mn_A_moment_muB": float, "Mn_B_moment_muB": float, "Sn_moment_muB": float, "formation_energy_eV": float, "cohesive_energy_eV": float}
- Scoring: scored by hidden verifier

### Step 4: Calculate elastic constants and derived moduli
- Role: scored
- Action: Apply small strains to the optimized Mn2Sn unit cell and compute the stress response to extract the cubic elastic constants C11, C12, C44. Use the Voigt-Reuss-Hill relations to derive bulk modulus B, shear modulus G, Young's modulus E, and Pugh's ratio B/G. Write the results to elastic_constants.json.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"C11_GPa": float, "C12_GPa": float, "C44_GPa": float, "Bulk_modulus_GPa": float, "Shear_modulus_GPa": float, "Youngs_modulus_GPa": float, "B_over_G": float}
- Scoring: scored by hidden verifier

### Step 5: Compute band structures under uniform compressive strain
- Role: process
- Action: For lattice constants a = 5.80, 5.52, 5.50, 5.46, 5.43 Å, perform spin-polarized DFT band structure calculations on the C1b Mn2Sn fully-compensated ferrimagnetic state, saving the eigenvalues along the high-symmetry k-path that includes G, X, and L points.
- Evidence: none

### Step 6: Classify spintronic phases from strain-dependent bands
- Role: scored
- Action: From the band structure data, extract the indirect band gaps in the majority-spin channel (G-X) and minority-spin channel (X-L). Determine the spintronic classification for each lattice constant (FCF-HM, FCF-SGS, FCF-S, ZG-FCF-HM) based on gap criteria. Write the table to uniform_strain_classification.csv.
- Output file: `/app/outputs/uniform_strain_classification.csv`
- Format: csv
- Contract: lattice_constant, majority_indirect_gap_eV, minority_indirect_gap_eV, classification
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_properties.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/uniform_strain_classification.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_properties.json
- path: `/app/outputs/equilibrium_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant, total and site-projected magnetic moments, formation energy, and cohesive energy of Mn2Sn.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_angstrom`: float
    - `total_magnetic_moment_muB`: float
    - `Mn_A_moment_muB`: float
    - `Mn_B_moment_muB`: float
    - `Sn_moment_muB`: float
    - `formation_energy_eV`: float
    - `cohesive_energy_eV`: float

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic stiffness coefficients and derived mechanical moduli for Mn2Sn.
- schema:
  - `type`: object
  - `required`:
    - `C11_GPa`: float
    - `C12_GPa`: float
    - `C44_GPa`: float
    - `Bulk_modulus_GPa`: float
    - `Shear_modulus_GPa`: float
    - `Youngs_modulus_GPa`: float
    - `B_over_G`: float

### uniform_strain_classification.csv
- path: `/app/outputs/uniform_strain_classification.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Indirect band gaps and spintronic classification for Mn2Sn at five compressed lattice constants (5.80, 5.52, 5.50, 5.46, 5.43 Å).
- schema:
  - `type`: table
  - `required_columns`: `lattice_constant`, `majority_indirect_gap_eV`, `minority_indirect_gap_eV`, `classification`

Notes: All outputs must be placed under /app/outputs. The checker compares reported values to hidden paper-reported targets with tolerances. Tetragonal distortion and intermediate lattice constants are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_angstrom": "float",
          "total_magnetic_moment_muB": "float",
          "Mn_A_moment_muB": "float",
          "Mn_B_moment_muB": "float",
          "Sn_moment_muB": "float",
          "formation_energy_eV": "float",
          "cohesive_energy_eV": "float"
        }
      },
      "description": "Equilibrium lattice constant, total and site-projected magnetic moments, formation energy, and cohesive energy of Mn2Sn."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11_GPa": "float",
          "C12_GPa": "float",
          "C44_GPa": "float",
          "Bulk_modulus_GPa": "float",
          "Shear_modulus_GPa": "float",
          "Youngs_modulus_GPa": "float",
          "B_over_G": "float"
        }
      },
      "description": "Elastic stiffness coefficients and derived mechanical moduli for Mn2Sn."
    },
    {
      "file": "uniform_strain_classification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice_constant",
          "majority_indirect_gap_eV",
          "minority_indirect_gap_eV",
          "classification"
        ]
      },
      "description": "Indirect band gaps and spintronic classification for Mn2Sn at five compressed lattice constants (5.80, 5.52, 5.50, 5.46, 5.43 Å)."
    }
  ],
  "notes": "All outputs must be placed under /app/outputs. The checker compares reported values to hidden paper-reported targets with tolerances. Tetragonal distortion and intermediate lattice constants are not required."
}
```

## How you are scored
A hidden verifier independently scores each output artifact. equilibrium_properties.json and elastic_constants.json are compared to reference values; uniform_strain_classification.csv is compared to the expected classification sequence. Each scored artifact contributes a portion of the total reward. The verifier checks that the computed lattice constant, magnetic moments, energies, elastic moduli, and classifications are consistent with the reference within allowed tolerances. The final score is the weighted sum of individual stage scores.
