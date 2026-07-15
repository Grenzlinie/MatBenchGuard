# Defect formation in GaN cascades via bond-order potential MD

## Problem background
Ion irradiation of compound semiconductors like gallium nitride (GaN) is essential for device processing, but the atomic-scale mechanisms of damage production remain poorly understood. Molecular dynamics (MD) simulations can reveal the nature of defect formation during collision cascades, provided accurate interatomic potentials that describe both equilibrium and far-from-equilibrium configurations. This work develops and applies such a potential to simulate collision cascades in wurtzite GaN over a range of recoil energies, enabling a quantitative study of the resulting point defects (vacancies, interstitials, antisites) and the threshold displacement energies needed to create them.

## Approach
The central idea is to construct an analytic bond-order potential for GaN that can faithfully describe the wide range of local atomic environments encountered during irradiation. The total energy is written as a sum over pairwise interactions, where the attractive contribution is moderated by an environment-dependent bond-order factor. The functional form uses Morse-like repulsive and attractive pair terms, a short-range ZBL correction smoothly blended via a Fermi-like function, and a cutoff that limits interactions to the first neighbor shell. The potential parameters are provided for three pair types (Ga–Ga, Ga–N, N–N).

Using this potential in an open-source MD code (LAMMPS or equivalent), we perform two types of simulations: (1) threshold displacement calculations, where a primary knock-on atom (Ga or N) is launched with a small energy in random directions, and a displacement is counted when a stable Frenkel pair forms; and (2) full collision cascade simulations for both Ga and N recoils with initial kinetic energies from 200 eV to 10 keV. Each cascade is run in a large simulation cell with periodic boundary conditions and a Berendsen thermostat at the borders to remove excess heat. After thermalisation, defects are identified by a Voronoi-polyhedron analysis that compares the final atomic configuration to the initial lattice. The average defect counts per cascade and the average threshold displacement energies are then extracted and compared.

## Reproduction target
The goal is to compute and report two sets of quantities from the simulations:

1. **Average threshold displacement energies**: the lowest energy at which a displacement occurs (minimum threshold) and the spatial average (mean over all successful directions) with its standard error, separately for gallium and nitrogen recoils. These are written to `step_01_threshold_energies.csv`.

2. **Average point defect counts per cascade**: for each combination of recoil atom type (Ga, N) and initial kinetic energy (200, 400, 1000, 2000, 5000, 10000 eV), the mean numbers of nitrogen vacancies (V_N), gallium vacancies (V_Ga), nitrogen interstitials (I_N), gallium interstitials (I_Ga), nitrogen-on-gallium antisites (N_Ga), and gallium-on-nitrogen antisites (Ga_N) produced after thermalisation. These are written to `step_02_defect_counts.csv` as 12 rows (two recoil types × six energies).

The reported means and uncertainties must come from the MD simulations; simply copying pre-existing numbers is not acceptable.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/download.html
- GaN wurtzite crystal structure parameters

## Workflow steps

### Step 1: Implement GaN bond-order potential
- Role: process
- Action: Implement the analytic bond-order potential for GaN as described by the Morse-like repulsive (V_R) and attractive (V_A) pair terms with an environment-dependent bond-order factor and a short-range ZBL correction smoothly blended via a Fermi-like function. Use the full parameter set: γ(0.007874,0.001632,0.76612), S(1.11,1.1122,1.4922), β(1.08,1.968,2.05945), D0(1.40,2.45,9.91), R0(2.3235,1.921,1.11), c(1.918,65.207,0.178493), d(0.750,2.821,0.20172), h(0.3013,0.518,0.045238), μ(1.846,0.0,0.0), Rcut(2.87,2.9,2.2), Dcut(0.15,0.2,0.2), rf(1.2,0.6,0.5), bf(12.0,12.0,12.0) for Ga–Ga, Ga–N, N–N respectively. Implement in LAMMPS or an equivalent MD code.
- Evidence: `/app/outputs/potential_impl.log`

### Step 2: Run threshold displacement simulations
- Role: process
- Action: Run MD simulations to determine threshold displacement energies. For Ga and N primary knock-on atoms, start projectiles with energies in the range ~20–40 eV and vary the direction randomly (1000 directions per atom type). Use a small wurtzite GaN supercell with periodic boundary conditions and a Berendsen thermostat at cell borders. Monitor whether a stable Frenkel pair is formed. Record the minimum energy at which a displacement occurs (minimum threshold) and the average over all successful directions (average threshold).
- Evidence: `/app/outputs/threshold_sim.log`

### Step 3: Report threshold displacement energies
- Role: scored
- Action: From the threshold simulations, compute the minimum threshold energy for Ga and N, and the spatial average threshold energy (mean over all directions that produced a displacement) with its standard error. Write the results to step_01_threshold_energies.csv.
- Output file: `/app/outputs/step_01_threshold_energies.csv`
- Format: csv
- Contract: Columns: atom_type (string, 'Ga' or 'N'), threshold_energy (float, mean in eV), error (float, standard error). Two rows, one per atom type.
- Scoring: scored by hidden verifier

### Step 4: Run collision cascade simulations
- Role: process
- Action: Using the implemented GaN potential, run single-recoil collision cascade simulations for each combination of recoil atom type (Ga, N) and initial kinetic energy (200, 400, 1000, 2000, 5000, 10000 eV), with multiple independent events (8–100) and random displacement directions. Use a large wurtzite GaN supercell (size appropriate to energy), periodic boundary conditions, a Berendsen thermostat at the border, and a variable timestep integration. After thermalisation, save the final atomic coordinates for defect analysis.
- Evidence: `/app/outputs/cascade_sim.log`

### Step 5: Analyze defects via Voronoi method and report counts
- Role: scored (load-bearing)
- Action: For each cascade simulation, perform Voronoi-polyhedron analysis relative to the initial lattice. Count vacancies (V_N, V_Ga), interstitials (I_N, I_Ga), and antisites (N_Ga, Ga_N). Average the counts over all runs for each recoil type and energy, and compute standard errors. Report the mean values in step_02_defect_counts.csv.
- Output file: `/app/outputs/step_02_defect_counts.csv`
- Format: csv
- Contract: Columns: recoil_type (string, 'N' or 'Ga'), energy_eV (integer), V_N (float, mean), V_Ga (float), I_N (float), I_Ga (float), N_Ga (float), Ga_N (float). 12 rows (combinations of two recoil types and six energies).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_threshold_energies.csv`
- `/app/outputs/step_02_defect_counts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_threshold_energies.csv
- path: `/app/outputs/step_01_threshold_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mean threshold displacement energy for Ga and N, with standard error of the mean.
- schema:
  - `type`: table
  - `required_columns`: `atom_type`, `threshold_energy`, `error`
  - `units`:
    - `threshold_energy`: eV
    - `error`: eV

### step_02_defect_counts.csv
- path: `/app/outputs/step_02_defect_counts.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Average number of vacancies, interstitials, and antisites per cascade for each recoil type and energy.
- schema:
  - `type`: table
  - `required_columns`: `recoil_type`, `energy_eV`, `V_N`, `V_Ga`, `I_N`, `I_Ga`, `N_Ga`, `Ga_N`
  - `units`:
    - `V_N`: count
    - `V_Ga`: count
    - `I_N`: count
    - `I_Ga`: count
    - `N_Ga`: count
    - `Ga_N`: count

Notes: The hidden checker will compare the reported mean threshold energies and defect counts to the paper's reference values within specified tolerances. The step_02_defect_counts.csv is load-bearing: the process of potential implementation and cascade simulations must be actually executed to obtain these counts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_threshold_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom_type",
          "threshold_energy",
          "error"
        ],
        "units": {
          "threshold_energy": "eV",
          "error": "eV"
        }
      },
      "description": "Mean threshold displacement energy for Ga and N, with standard error of the mean."
    },
    {
      "file": "step_02_defect_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "recoil_type",
          "energy_eV",
          "V_N",
          "V_Ga",
          "I_N",
          "I_Ga",
          "N_Ga",
          "Ga_N"
        ],
        "units": {
          "V_N": "count",
          "V_Ga": "count",
          "I_N": "count",
          "I_Ga": "count",
          "N_Ga": "count",
          "Ga_N": "count"
        }
      },
      "description": "Average number of vacancies, interstitials, and antisites per cascade for each recoil type and energy."
    }
  ],
  "notes": "The hidden checker will compare the reported mean threshold energies and defect counts to the paper's reference values within specified tolerances. The step_02_defect_counts.csv is load-bearing: the process of potential implementation and cascade simulations must be actually executed to obtain these counts."
}
```

## How you are scored
A hidden verifier will independently examine the two output files. For `step_01_threshold_energies.csv`, it will compare the reported mean threshold energies (Ga and N) against reference values within an allowed tolerance that accounts for typical run-to-run variation. For `step_02_defect_counts.csv`, each mean defect count (all 12 rows, six defect types) is compared to reference averages, again with appropriate tolerances. The verifier also checks that the files conform to the specified formats and column structures. The scores from each file are combined into a final reward between 0 and 1. The verifier does not re-run the simulations; it relies on the agent having faithfully executed the entire workflow (potential implementation, threshold runs, cascade runs, and defect analysis) to produce the reported numbers. Merely emitting numbers that match the paper's published results without actually running the simulations will not be detectable by the verifier, but the task is designed for honest reproduction.
