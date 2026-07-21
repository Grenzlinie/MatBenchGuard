# MD Tensile Testing of Defective Graphene: Poisson's Ratio and Young's Modulus from 5-8-5 Vacancy Simulations

## Problem background
Graphene is a one-atom-thick carbon sheet with exceptional mechanical properties. Introducing 5-8-5 double vacancy defects can alter the material's conformation and may produce a wrinkled structure. Under uniaxial tension this wrinkling could lead to a negative Poisson's ratio (auxetic behaviour) at ambient temperature. The goal is to investigate, through molecular dynamics simulations, whether and to what extent the Poisson's ratio and Young's modulus of defective graphene depend on defect concentration, and whether auxeticity can be engineered by tuning the concentration of such defects.

## Approach
Build a pristine graphene sheet of ~28800 carbon atoms with armchair direction along the tensile axis. Create defective variants by removing a controlled fraction of neighbouring atom pairs (0.5 %, 1.0 %, 2.0 %, 3.0 % of atoms) and reconstructing bonds to form 5-8-5 double vacancies. For each system, including the pristine case, perform classical molecular dynamics simulations using the AIREBO interatomic potential at 300 K, with periodic boundary conditions in the transverse in-plane direction and constrained edge atoms along the tensile direction. Apply uniaxial tensile engineering strain up to 10 % along the armchair direction, recording the box dimensions and the stress tensor at regular strain intervals. Post-process the trajectories to obtain the instantaneous Poisson's ratio (negative ratio of transverse strain increment to axial strain increment) and Young's modulus (ratio of axial stress increment to axial strain increment) for every defect concentration and strain step. The output is a single CSV that allows a direct quantitative comparison of the mechanical response across all concentrations and strain levels.

## Reproduction target
Produce a single CSV file containing, for each defect concentration (0 %, 0.5 %, 1.0 %, 2.0 %, 3.0 %) and for every recorded step of the applied uniaxial engineering strain (0 … 10 %), the simulation box dimensions Lx, Ly, Lz, the computed Poisson's ratio and Young's modulus. The table must allow an independent assessment of whether a negative Poisson's ratio emerges for any concentration, how the mechanical properties evolve with strain, and how they depend on the defect fraction. The file must comply with the output schema described under the Output Contract.

## Assets

- LAMMPS: https://www.lammps.org/

## Workflow steps

### Step 1: Construct pristine graphene sheet
- Role: process
- Action: Generate atomic coordinates of a graphene sheet containing approximately 28800 carbon atoms with armchair orientation along the x-axis and lateral dimensions about 25 nm × 29 nm, and write the configuration in LAMMPS data format.
- Evidence: `/app/outputs/pristine.data`

### Step 2: Generate 5-8-5 double vacancy defect configurations
- Role: process
- Action: For each target defect concentration p = 0.5%, 1.0%, 2.0%, and 3.0%, randomly remove the corresponding number of neighboring atom pairs (72, 144, 288, 432 pairs respectively) and reconstruct bonds to form 5-8-5 topology, producing separate defective LAMMPS data files.
- Evidence: `/app/outputs/defective_systems`

### Step 3: Run MD tensile testing simulations
- Role: process
- Action: For each defect concentration (including p=0% pristine), run LAMMPS with the AIREBO interatomic potential at T=300 K, periodic boundary conditions in the y-direction, constrained atoms at the x-edges, and apply uniaxial tensile strain along x up to 10%, recording engineering strain, simulation box dimensions Lx, Ly, Lz, and the stress tensor at regular intervals.
- Evidence: `/app/outputs/trajectories`

### Step 4: Compute Poisson's ratio and Young's modulus
- Role: scored (load-bearing)
- Action: From the simulation outputs, compute engineering strain, Lx, Ly, Lz, the instantaneous Poisson's ratio as the negative ratio of transverse to axial strain increments, and Young's modulus as the ratio of axial stress to axial strain increment. Output a single CSV file with all defect concentrations and all strain steps.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with columns: defect_concentration (float), engineering_strain (float), Lx_nm (float), Ly_nm (float), Lz_nm (float), poisson_ratio (float), young_modulus_GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV with the computed Poisson's ratio and Young's modulus for each defect concentration and strain step. The checker will verify that the auxetic behavior (negative Poisson's ratio) is achieved for the highest defect concentrations, that the trend across concentrations is monotonic, and that the pristine Young's modulus is consistent with the known value ~1 TPa.
- schema:
  - `type`: table
  - `required_columns`: `defect_concentration`, `engineering_strain`, `Lx_nm`, `Ly_nm`, `Lz_nm`, `poisson_ratio`, `young_modulus_GPa`

Notes: Only the single scored CSV is required. The process steps produce intermediate LAMMPS data files and trajectories; these are not scored but must be generated to obtain the final CSV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_concentration",
          "engineering_strain",
          "Lx_nm",
          "Ly_nm",
          "Lz_nm",
          "poisson_ratio",
          "young_modulus_GPa"
        ]
      },
      "description": "CSV with the computed Poisson's ratio and Young's modulus for each defect concentration and strain step. The checker will verify that the auxetic behavior (negative Poisson's ratio) is achieved for the highest defect concentrations, that the trend across concentrations is monotonic, and that the pristine Young's modulus is consistent with the known value ~1 TPa."
    }
  ],
  "notes": "Only the single scored CSV is required. The process steps produce intermediate LAMMPS data files and trajectories; these are not scored but must be generated to obtain the final CSV."
}
```

## How you are scored
A hidden verifier reads your simulation_results.csv and evaluates it against a set of quantitative checks. It verifies that the data covers all required defect concentrations and strain steps, recomputes intermediate metrics where needed, and compares the reported Poisson's ratios and Young's moduli against known reference trends and values (not disclosed to you). Your final reward is a weighted combination of scores from each scored artifact stage; simply printing expected numbers without executing the simulation pipeline will not satisfy the hidden checks.
