# Mechanical Deformation Effect on Guest Diffusion in ZIF-8

## Problem background
Metal-organic frameworks (MOFs) are porous crystalline materials whose guest diffusion properties can be tuned by mechanical deformation. Understanding how tensile and shear strain affect the motion of small gas molecules inside a MOF is important for elastic strain engineering of gas separation and storage materials. This task focuses on the prototypical zeolitic imidazolate framework ZIF-8, which features flexible 6-membered ring gates that control guest transport. The objective is to investigate, by means of molecular dynamics simulations, the relationship between mechanical deformation and the self-diffusion of hydrogen (H₂) and carbon dioxide (CO₂) inside the ZIF-8 framework.

## Approach
The approach employs classical molecular dynamics (MD) simulations using the LAMMPS package. A 2×2×2 supercell of ZIF-8 is built with periodic boundary conditions, using the published lattice parameter and a force field developed for ZIF-8. Guest molecules are modelled with established force fields: H₂ as a single-site Lennard‑Jones particle and CO₂ using the EPM2 model. After energy minimization and equilibration, the empty framework is subjected to small incremental uniaxial tensile strain along the z direction and shear strain on the {100} planes; stress–strain curves are constructed and the Young’s modulus and shear modulus extracted. Separate guest-loaded systems (low loadings of H₂ and CO₂) are then equilibrated and subjected to the same deformation modes in stepwise fashion, with relaxation at each strain step. For each target strain (0%, 7%, 10% in both deformation modes), long NVE production runs are performed. Self-diffusion coefficients are computed from the mean-square displacement via the Einstein relation. The trajectories are also analyzed to obtain ensemble-averaged C2–C2 long bond lengths, which define the size of the 6-membered ring gates. The comparison across strain types and magnitudes reveals how deformation influences guest diffusion and whether the effect correlates with changes in gate size.

## Reproduction target
Compute the following quantities:
- The Young’s modulus and shear modulus of the empty ZIF-8 framework.
- The self-diffusion coefficients of H₂ and CO₂ inside ZIF-8 under uniaxial tensile strain of 0%, 7%, and 10%, and under shear strain of 0%, 7%, and 10%, all from NVE ensemble simulations.
- The average length of the C2–C2 long bonds that define the 6-membered ring gate, for the same six strain conditions.
The results must be reported in the specified output files (moduli.json, diffusion_results.csv, c2c2_average_lengths.csv) with the required formats and units. The aim is to produce a complete, self-consistent dataset that allows one to evaluate the effect of mechanical deformation on guest diffusion from first principles.

## Assets

- LAMMPS: https://lammps.org
- ZIF-8 force field (Zheng et al., J. Phys. Chem. C 2012, 116, 933): 10.1021/jp210378q
- H₂ single-site Lennard‑Jones parameters (Grazzi et al., Phys. Rev. B 2002, 66, 144303): 10.1103/PhysRevB.66.144303
- CO₂ EPM2 model (Harris & Yung, J. Phys. Chem. 1995, 99, 12021): 10.1021/j100031a034
- ZIF-8 crystal structure (space group I-43m, a=16.985 Å): 10.1039/B205564F

## Workflow steps

### Step 1: Build ZIF-8 supercell and assign force field
- Role: process
- Action: Construct a 2×2×2 supercell of ZIF-8 with periodic boundary conditions using the published lattice parameter (16.985 Å). Assign the published ZIF-8 force field, single‑site H₂ LJ parameters, and EPM2 CO₂ model.
- Evidence: none

### Step 2: Energy minimization and NVT equilibration of empty ZIF-8
- Role: process
- Action: Perform conjugate gradient minimization at 0 K, then equilibrate the empty framework at 300 K for 10 ns in the NVT ensemble using a Langevin thermostat.
- Evidence: none

### Step 3: Calculate elastic moduli of empty ZIF-8
- Role: scored
- Action: Apply small incremental uniaxial tensile strain along z and shear strain on {100} planes. Collect atomistic stress data, build stress‑strain curves, and extract Young’s modulus and shear modulus via linear fitting.
- Output file: `/app/outputs/moduli.json`
- Format: json
- Contract: {"young_modulus_GPa": <float>, "shear_modulus_GPa": <float>}
- Scoring: scored by hidden verifier

### Step 4: Insert guest H₂ and CO₂ and equilibrate
- Role: process
- Action: Place a small number of H₂ and CO₂ molecules (e.g., 10 each) into separate copies of the empty ZIF-8 supercell. Equilibrate at 300 K to obtain guest‑loaded starting configurations.
- Evidence: none

### Step 5: Tensile deformation NVE MD runs
- Role: process
- Action: For each guest system (H₂/ZIF-8 and CO₂/ZIF-8), apply uniaxial tensile strain along z in ~1% increments, relaxing at each strain. At target strains 0%, 7%, 10%, run 50 ns NVE production, saving configurations every 0.5 ps.
- Evidence: none

### Step 6: Shear deformation NVE MD runs
- Role: process
- Action: For each guest system, apply shear strain on {100} planes in ~1% increments, relaxing at each strain. At target strains 0%, 7%, 10%, run 50 ns NVE production, saving configurations every 0.5 ps.
- Evidence: none

### Step 7: Compute guest diffusion coefficients
- Role: scored (load-bearing)
- Action: From the saved NVE production coordinates (steps 4 and 5), calculate mean‑square displacements and extract self‑diffusion coefficients via the Einstein relation for each guest type, deformation mode, and target strain. Compile all results.
- Output file: `/app/outputs/diffusion_results.csv`
- Format: csv
- Contract: guest (string), strain_type (string: tensile|shear), strain_value (float), diffusion_coefficient_m2_per_s (float)
- Scoring: scored by hidden verifier

### Step 8: Compute average C2–C2 long bond lengths
- Role: scored
- Action: Using the same NVE trajectories, identify all C2–C2 long bond lengths in the 6‑membered ring gates and compute the ensemble average for each strain condition (0%, 7%, 10% tensile and shear).
- Output file: `/app/outputs/c2c2_average_lengths.csv`
- Format: csv
- Contract: strain_type (string: tensile|shear), strain_value (float), avg_c2c2_length_angstrom (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/moduli.json`
- `/app/outputs/diffusion_results.csv`
- `/app/outputs/c2c2_average_lengths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### moduli.json
- path: `/app/outputs/moduli.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Elastic moduli of empty ZIF-8: Young's modulus and shear modulus.
- schema:
  - `type`: object
  - `required`:
    - `young_modulus_GPa`: number
    - `shear_modulus_GPa`: number
  - `units`:
    - `young_modulus_GPa`: GPa
    - `shear_modulus_GPa`: GPa

### diffusion_results.csv
- path: `/app/outputs/diffusion_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Self‑diffusion coefficients of H₂ and CO₂ under tensile and shear strain at 0%, 7%, 10%.
- schema:
  - `type`: table
  - `required_columns`: `guest`, `strain_type`, `strain_value`, `diffusion_coefficient_m2_per_s`
  - `items`:
    - `guest`: string
    - `strain_type`: one of tensile, shear
    - `strain_value`: float
    - `diffusion_coefficient_m2_per_s`: float

### c2c2_average_lengths.csv
- path: `/app/outputs/c2c2_average_lengths.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ensemble‑averaged C2–C2 long bond lengths that define the 6MR gate size under each strain.
- schema:
  - `type`: table
  - `required_columns`: `strain_type`, `strain_value`, `avg_c2c2_length_angstrom`
  - `items`:
    - `strain_type`: one of tensile, shear
    - `strain_value`: float
    - `avg_c2c2_length_angstrom`: float

Notes: The workflow covers NVE‑ensemble simulations only. NPT results are excluded. The agent must run long production MD trajectories; external GPU/accelerator access is recommended.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "young_modulus_GPa": "number",
          "shear_modulus_GPa": "number"
        },
        "units": {
          "young_modulus_GPa": "GPa",
          "shear_modulus_GPa": "GPa"
        }
      },
      "description": "Elastic moduli of empty ZIF-8: Young's modulus and shear modulus."
    },
    {
      "file": "diffusion_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "guest",
          "strain_type",
          "strain_value",
          "diffusion_coefficient_m2_per_s"
        ],
        "items": {
          "guest": "string",
          "strain_type": "one of tensile, shear",
          "strain_value": "float",
          "diffusion_coefficient_m2_per_s": "float"
        }
      },
      "description": "Self‑diffusion coefficients of H₂ and CO₂ under tensile and shear strain at 0%, 7%, 10%."
    },
    {
      "file": "c2c2_average_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_type",
          "strain_value",
          "avg_c2c2_length_angstrom"
        ],
        "items": {
          "strain_type": "one of tensile, shear",
          "strain_value": "float",
          "avg_c2c2_length_angstrom": "float"
        }
      },
      "description": "Ensemble‑averaged C2–C2 long bond lengths that define the 6MR gate size under each strain."
    }
  ],
  "notes": "The workflow covers NVE‑ensemble simulations only. NPT results are excluded. The agent must run long production MD trajectories; external GPU/accelerator access is recommended."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each of the three required output files. The verifier checks that the elastic moduli are physically plausible and within an acceptable range relative to a hidden reference; that the diffusion coefficients exhibit the correct qualitative trends (namely, the expected dependence on strain type and magnitude) and quantitative consistency; and that the C2–C2 bond length averages are consistent with the structural response to deformation. The final score is a weighted combination of these checks, with the largest weight placed on the diffusion coefficient results. The verifier’s criteria and tolerances are based on the original study’s reported values and are not disclosed in advance. You must therefore produce results by faithfully executing the described simulation protocol; simply reporting arbitrary numbers or copying values from elsewhere will not yield a high score.
