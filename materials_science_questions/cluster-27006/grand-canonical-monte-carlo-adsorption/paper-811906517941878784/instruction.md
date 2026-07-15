# Water Adsorption and Diffusion in Protein Crystal via GCMC and MD Simulations

## Problem background
Understanding the microscopic behavior of water in protein crystals is crucial for their use as novel nanoporous biomaterials. One key system is orthorhombic lysozyme crystal, where water interacts with the protein surface and diffuses through crystalline pores. Atomistic simulations can probe water adsorption, hydration-shell formation, and diffusion, revealing how protein flexibility and hydration level influence these properties. This task reproduces the computational investigation of water in partially hydrated orthorhombic lysozyme crystal using grand canonical Monte Carlo and molecular dynamics simulations.

## Approach
The computational study combines two simulation methods. Grand canonical Monte Carlo (GCMC) simulations are used to determine water adsorption and desorption isotherms at multiple relative humidities, using the AMBER 2003 force field for the protein and the TIP3P water model. From the equilibrium configurations, the hydration shell around the protein is characterized by the distance distribution of water molecules and the fraction within the first solvation layer. Molecular dynamics (MD) simulations are then run on the GCMC-equilibrated configurations under both rigid-framework and flexible-framework conditions to extract water mean-square displacements and to compute unit-cell lattice parameters as a function of hydration. The pipeline yields (1) adsorption/desorption loadings, (2) the percentage of water in the first hydration shell, (3) the subdiffusion exponent from the power-law fit of MSD, and (4) the average lattice dimensions.

## Reproduction target
Produce four artifacts: (1) an adsorption/desorption isotherm (loading vs. RH) for RH = 5, 20, 50, 80%, (2) a CSV with the percentage of water molecules within the first hydration shell (0.28 nm thickness) and total water count at each RH, (3) a CSV with the subdiffusion exponent γ from MSD fits (10–100 ps) for both rigid and flexible frameworks, and (4) a CSV with the unit-cell lattice parameters a, b, c (nm) from the flexible-framework MD trajectories. The simulation box is built from PDB 1AKI with two unit cells (8 lysozyme molecules, 64 Cl⁻) and uses the standard AMBER03/TIP3P force fields.

## Assets

- Orthorhombic lysozyme crystal structure (PDB 1AKI): https://www.rcsb.org/structure/1AKI
- AMBER 2003 force field (ff03): https://ambermd.org/AmberModels.php
- TIP3P water model: gromacs
- GROMACS molecular dynamics package: https://www.gromacs.org
- RASPA2 (GCMC simulation software): https://github.com/iRASPA/RASPA2

## Workflow steps

### Step 1: Construction of lysozyme crystal simulation box
- Role: process
- Action: Build the atomistic simulation box from PDB 1AKI: assign protonation states consistent with neutral pH (Arg/Lys protonated, Asp/Glu deprotonated), add 8 lysozyme molecules (two unit cells) and 64 Cl- counter-ions. Prepare input files with AMBER03 and TIP3P force fields for subsequent GCMC and MD runs.
- Evidence: `/app/outputs/step_construct_box.pdb`

### Step 2: Estimation of porosity using helium probe
- Role: process
- Action: Compute the free volume and porosity of the simulation box using a helium probe (LJ parameters σ=2.58 Å, ε/kB=10.22 K). Report the porosity value.
- Evidence: `/app/outputs/step_porosity.txt`

### Step 3: Grand Canonical Monte Carlo (GCMC) adsorption simulation
- Role: process
- Action: Run GCMC adsorption simulations at T=300 K for RH = 5%, 20%, 50%, 80% (water chemical potentials derived from the corresponding partial pressures, Psat = 3.1 kPa). Use AMBER03/TIP3P force fields, Ewald summation for electrostatics, and a total of 20,000 cycles with 5,000 moves per cycle. Record equilibrium water configurations and loadings.
- Evidence: `/app/outputs/step_gcmc_adsorption_loadings.json`

### Step 4: Computation of hydration shell water percentage
- Role: scored
- Action: From GCMC adsorption configurations at each RH, compute the number distribution N_n(r) of water molecules as a function of distance from the nearest protein atom and determine the percentage of water within the first hydration shell (distance ≤ 0.28 nm). Output a CSV with columns RH, percentage_in_shell, total_water.
- Output file: `/app/outputs/step_2_hydration_shell.csv`
- Format: csv
- Contract: CSV with columns: RH (integer), percentage_in_shell (float, %), total_water (integer). One row per RH (5,20,50,80).
- Scoring: scored by hidden verifier

### Step 5: Grand Canonical Monte Carlo (GCMC) desorption simulation
- Role: process
- Action: Starting from the high-RH adsorption configuration, run GCMC desorption by lowering water chemical potentials corresponding to RH 80%, 50%, 20%, 5%, obtaining equilibrium loadings for the desorption branch.
- Evidence: `/app/outputs/step_gcmc_desorption_loadings.json`

### Step 6: Construction of adsorption/desorption isotherm
- Role: scored
- Action: Compile the adsorption and desorption loadings (water molecules per simulation box) at RH = 5%, 20%, 50%, 80% from the GCMC runs. Output a JSON array with objects containing RH, loading_adsorption, loading_desorption.
- Output file: `/app/outputs/step_1_adsorption_isotherm.json`
- Format: json
- Contract: Array of objects, each with keys: RH (number), loading_adsorption (number), loading_desorption (number).
- Scoring: scored by hidden verifier

### Step 7: Molecular dynamics (MD) simulations of hydrated crystal
- Role: process
- Action: For each RH, prepare two sets of GCMC-equilibrated configurations: one for a rigid protein framework (NVT at 300 K) and one for a flexible protein framework (NPT at 300 K and 1 bar). Run 5.5 ns MD simulations using GROMACS with AMBER03/TIP3P, PME electrostatics, Berendsen thermostat/barostat. Discard the first 0.5 ns for equilibration; retain the final 5 ns trajectory for analysis.
- Evidence: none

### Step 8: Computation of water subdiffusion exponent γ
- Role: scored (load-bearing)
- Action: From the rigid and flexible MD trajectories at each RH, calculate the mean-square displacement (MSD) of water molecules as a function of time. Fit MSD to a power law MSD ∝ t^γ over the time window 10–100 ps. Output a CSV with columns: RH, rigid_gamma, flexible_gamma.
- Output file: `/app/outputs/step_3_subdiffusion_exponents.csv`
- Format: csv
- Contract: CSV with columns: RH (integer), rigid_gamma (float, unitless), flexible_gamma (float, unitless). One row per RH.
- Scoring: scored by hidden verifier

### Step 9: Extraction of lattice parameters
- Role: scored
- Action: From the flexible-framework NPT MD trajectories at each RH, compute the average unit cell dimensions a, b, c. Output a CSV with columns: RH, a, b, c (in nm).
- Output file: `/app/outputs/step_4_lattice_parameters.csv`
- Format: csv
- Contract: CSV with columns: RH (integer), a (float, nm), b (float, nm), c (float, nm). One row per RH.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_2_hydration_shell.csv`
- `/app/outputs/step_1_adsorption_isotherm.json`
- `/app/outputs/step_3_subdiffusion_exponents.csv`
- `/app/outputs/step_4_lattice_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_2_hydration_shell.csv
- path: `/app/outputs/step_2_hydration_shell.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Percentage of water molecules within the first hydration shell (0.28 nm) at each relative humidity.
- schema:
  - `type`: table
  - `required_columns`: `RH`, `percentage_in_shell`, `total_water`
  - `units`:
    - `percentage_in_shell`: %
    - `total_water`: count

### step_1_adsorption_isotherm.json
- path: `/app/outputs/step_1_adsorption_isotherm.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adsorption and desorption isotherm loadings (water molecules per simulation box) at RH = 5%, 20%, 50%, 80%.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `RH`, `loading_adsorption`, `loading_desorption`
    - `properties`:
      - `RH`: number
      - `loading_adsorption`: number
      - `loading_desorption`: number

### step_3_subdiffusion_exponents.csv
- path: `/app/outputs/step_3_subdiffusion_exponents.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Subdiffusion exponent gamma for water in rigid and flexible protein frameworks.
- schema:
  - `type`: table
  - `required_columns`: `RH`, `rigid_gamma`, `flexible_gamma`
  - `units`:
    - `rigid_gamma`: unitless
    - `flexible_gamma`: unitless

### step_4_lattice_parameters.csv
- path: `/app/outputs/step_4_lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average unit cell dimensions a, b, c (nm) from flexible-framework NPT MD simulations.
- schema:
  - `type`: table
  - `required_columns`: `RH`, `a`, `b`, `c`
  - `units`:
    - `a`: nm
    - `b`: nm
    - `c`: nm

Notes: All scored quantities are checked against the paper's reported values with appropriate tolerances. The isotherm should exhibit Type-IV shape and H4 hysteresis (desorption branch above adsorption at intermediate RH).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_2_hydration_shell.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "RH",
          "percentage_in_shell",
          "total_water"
        ],
        "units": {
          "percentage_in_shell": "%",
          "total_water": "count"
        }
      },
      "description": "Percentage of water molecules within the first hydration shell (0.28 nm) at each relative humidity."
    },
    {
      "file": "step_1_adsorption_isotherm.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "RH",
            "loading_adsorption",
            "loading_desorption"
          ],
          "properties": {
            "RH": "number",
            "loading_adsorption": "number",
            "loading_desorption": "number"
          }
        }
      },
      "description": "Adsorption and desorption isotherm loadings (water molecules per simulation box) at RH = 5%, 20%, 50%, 80%."
    },
    {
      "file": "step_3_subdiffusion_exponents.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "RH",
          "rigid_gamma",
          "flexible_gamma"
        ],
        "units": {
          "rigid_gamma": "unitless",
          "flexible_gamma": "unitless"
        }
      },
      "description": "Subdiffusion exponent gamma for water in rigid and flexible protein frameworks."
    },
    {
      "file": "step_4_lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "RH",
          "a",
          "b",
          "c"
        ],
        "units": {
          "a": "nm",
          "b": "nm",
          "c": "nm"
        }
      },
      "description": "Average unit cell dimensions a, b, c (nm) from flexible-framework NPT MD simulations."
    }
  ],
  "notes": "All scored quantities are checked against the paper's reported values with appropriate tolerances. The isotherm should exhibit Type-IV shape and H4 hysteresis (desorption branch above adsorption at intermediate RH)."
}
```

## How you are scored
The submitted artifacts are evaluated by a hidden verifier that compares your computed quantities to reference results derived from the published study. Each output file (isotherm, hydration shell percentages, subdiffusion exponents, lattice parameters) is checked independently, and the scores are combined into a final aggregate reward using preset weights. The verifier uses appropriate tolerance margins that account for differences in simulation codes, seeds, and numerical settings, so a faithful re-implementation of the described workflow is expected to score well. You do not need to hit exact numbers; the goal is to demonstrate that your simulations reproduce the key physical trends and quantitative features.
