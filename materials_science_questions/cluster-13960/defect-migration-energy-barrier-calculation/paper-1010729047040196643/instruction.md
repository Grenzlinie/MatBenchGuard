# Oxygen Self-Diffusion and Migration Barriers in Fluorite High-Entropy Oxides

## Problem background
High-entropy oxides (HEOs) with a fluorite crystal structure are being explored as ion-conducting materials for energy devices such as solid oxide fuel cells. Introducing multiple cations into the fluorite lattice creates substantial configurational entropy, but the impact of this entropy stabilization on oxygen ion mobility is not fully understood. This work uses classical atomistic simulations—molecular dynamics (MD) and static transition-state calculations—to determine oxygen self-diffusion coefficients and oxygen vacancy migration barriers in fluorite HEOs and to compare them with those of conventional yttria-stabilized zirconia (Z8Y). The key question is whether the multi-cation environment enhances or suppresses oxygen diffusion.

## Approach
The simulations rely on empirical Buckingham pair potentials whose parameters for the Y-Zr-O, Ce-O, Hf-O, Gd-O, La-O, and Pr-O systems have been published. The computational workflow has two main branches: (1) MD for long-time oxygen transport, and (2) nudged elastic band (NEB) calculations for local oxygen vacancy migration barriers.

For MD, large 8×8×8 fluorite supercells are built with random cation assignments for the chosen compositions. Oxygen vacancies are introduced to maintain charge neutrality. After an equilibration series (a high-temperature anneal, NPT runs at target temperatures to fix the cell dimensions, and a short fixed-volume relaxation), production runs are performed in the NVE ensemble. The oxygen mean squared displacement (MSD) is recorded as a function of time. The oxygen diffusivity D at each temperature and configuration is extracted from the long-time linear regime of the MSD via the Einstein relation. An Arrhenius fit to D(T) then yields the activation energy Ea and the pre-exponential factor D0 for each composition.

For barrier analysis, the climbing-image NEB method as implemented in the GULP code is applied to oxygen vacancy jumps in 6.25% Y-doped ZrO2 with varying amounts of isovalent Ce and Hf substitution (0%, 33%, 66%). The transition-state energy and the energies of the initial and final states are obtained, from which the reaction energy Er and the barrier energy Eb are calculated. By comparing the distributions of Eb and Er across random cation configurations and vacancy positions, the effect of isovalent mixing on oxygen vacancy trapping can be assessed.

## Reproduction target
Compute the oxygen self-diffusion coefficient D as a function of temperature T (at least three temperatures, e.g. 1000 K, 1500 K, 2000 K) for two compositions: HEO_A (Zr_{0.29}Hf_{0.29}Ce_{0.29}Gd_{0.07}Y_{0.07}O_{1.86}, corresponding to x=0.14) and Z8Y (ZrO2 + 8 mol% Y2O3). For each composition, use at least two independent random cation configurations. From the D(T) data, extract the Arrhenius activation energy Ea and pre-exponential D0 for each composition.

Also compute the oxygen vacancy migration barrier energy Eb and reaction energy Er for Y-doped ZrO2 with 6.25% Y and isovalent Ce+Hf substitution fractions of 0, 33, and 66 at %. Generate at least five random cation/vacancy configurations for each substitution level and perform NEB calculations. Compile the results into the two required output files (see the workflow steps and output contract). All reported values must be derived from your own simulations; do not copy numbers from any auxiliary source.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- GULP lattice dynamics and transition-state code: https://gulp.curtin.edu.au/gulp/
- Buckingham interatomic potential parameters for Y-Zr-O, Ce-O, Hf-O, Gd-O, La-O, Pr-O

## Workflow steps

### Step 1: Supercell generation and cation assignment
- Role: process
- Action: Construct 8×8×8 fluorite supercells for HEO_A (x=0.14), Z8Y, and Y-doped ZrO2 with 6.25% Y and Ce+Hf fractions 0, 0.33, 0.66. Randomly assign cations and introduce oxygen vacancies for charge balance. Generate input files for LAMMPS.
- Evidence: `/app/outputs/supercell_generation.log`

### Step 2: MD equilibration series
- Role: process
- Action: For each composition and at least two random cation configurations, run LAMMPS equilibration: anneal at 1500 K, 2 ns NPT at target temperatures (at least three temperatures, e.g., 1000, 1500, 2000 K), average cell parameters, and 50 ps fixed-cell relaxation.
- Evidence: `/app/outputs/equilibration.log`

### Step 3: Production NVE molecular dynamics
- Role: process
- Action: For each composition/configuration/temperature, run NVE production for up to 10 ns in LAMMPS, recording oxygen mean squared displacement (MSD) vs time. Store raw MSD data in msd_data.csv.
- Evidence: `/app/outputs/msd_data.csv`

### Step 4: Diffusivity extraction and Arrhenius analysis
- Role: scored (load-bearing)
- Action: From the raw MSD data, fit the Einstein relation to the long-time linear regime for each configuration/temperature to obtain oxygen diffusivity D. Then, for each composition, fit the Arrhenius relation to the set of D(T) points to derive activation energy Ea and pre-exponential D0. Write the results to md_diffusivity_results.csv.
- Output file: `/app/outputs/md_diffusivity_results.csv`
- Format: csv
- Contract: CSV with columns: composition (str), config_index (int), temperature_K (float), D_cm2_s1 (float), MSD_fit_R2 (float), and optionally Ea_eV (float), D0_cm2_s1 (float). At minimum, rows for HEO_A (x=0.14) and Z8Y, each with at least two configurations and three temperatures.
- Scoring: scored by hidden verifier

### Step 5: GULP NEB calculations for oxygen vacancy migration
- Role: process
- Action: For each 6.25% Y-doped composition with Ce+Hf fractions 0, 0.33, 0.66, generate at least five random vacancy configurations and perform climbing-image NEB calculations using GULP. Output GULP log files.
- Evidence: `/app/outputs/gulp_neb_output.log`

### Step 6: NEB barrier and reaction energy analysis
- Role: scored (load-bearing)
- Action: Parse GULP output logs to extract transition-state energy and end-point energies, compute reaction energy E_r and barrier energy E_b. Write the compiled results to neb_barrier_results.csv.
- Output file: `/app/outputs/neb_barrier_results.csv`
- Format: csv
- Contract: CSV with columns: composition_label (str, e.g., 'Y6.25%_CeHf0', 'Y6.25%_CeHf33', 'Y6.25%_CeHf66'), config_index (int), vacancy_index (int), E_ts_eV (float), E_r_eV (float), E_b_eV (float). At minimum, results for each Ce+Hf fraction with at least five vacancy hops.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/md_diffusivity_results.csv`
- `/app/outputs/neb_barrier_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### md_diffusivity_results.csv
- path: `/app/outputs/md_diffusivity_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Oxygen diffusivity per configuration/temperature and per-composition Arrhenius parameters for HEO_A (x=0.14) and Z8Y.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `config_index`, `temperature_K`, `D_cm2_s1`, `MSD_fit_R2`
  - `optional_columns`: `Ea_eV`, `D0_cm2_s1`
  - `row_count_minimum`: 12

### neb_barrier_results.csv
- path: `/app/outputs/neb_barrier_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Oxygen vacancy migration barrier and reaction energies for Y-doped ZrO2 with 0%, 33%, and 66% Ce+Hf isovalent substitution.
- schema:
  - `type`: table
  - `required_columns`: `composition_label`, `config_index`, `vacancy_index`, `E_ts_eV`, `E_r_eV`, `E_b_eV`
  - `row_count_minimum`: 15

Notes: All values must be derived from the simulation workflows; do not copy numbers from auxiliary sources. The md_diffusivity_results.csv must be based on the agent's own MD production data (msd_data.csv). The neb_barrier_results.csv must be extracted from the agent's own GULP runs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "md_diffusivity_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "config_index",
          "temperature_K",
          "D_cm2_s1",
          "MSD_fit_R2"
        ],
        "optional_columns": [
          "Ea_eV",
          "D0_cm2_s1"
        ],
        "row_count_minimum": 12
      },
      "description": "Oxygen diffusivity per configuration/temperature and per-composition Arrhenius parameters for HEO_A (x=0.14) and Z8Y."
    },
    {
      "file": "neb_barrier_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_label",
          "config_index",
          "vacancy_index",
          "E_ts_eV",
          "E_r_eV",
          "E_b_eV"
        ],
        "row_count_minimum": 15
      },
      "description": "Oxygen vacancy migration barrier and reaction energies for Y-doped ZrO2 with 0%, 33%, and 66% Ce+Hf isovalent substitution."
    }
  ],
  "notes": "All values must be derived from the simulation workflows; do not copy numbers from auxiliary sources. The md_diffusivity_results.csv must be based on the agent's own MD production data (msd_data.csv). The neb_barrier_results.csv must be extracted from the agent's own GULP runs."
}
```

## How you are scored
A hidden verifier independently scores each of the scored output files. It compares your reported diffusivity values, activation energies, and barrier energies against a gold reference derived from the published work. The comparison uses tolerances that account for the inherent variability of classical-potential simulations and different computational implementations. The verifier awards full credit when your results match or improve upon the reference quality; credit decreases as the deviation grows. The final reward is a weighted combination of the scores from the two output tables. Providing only a verbal claim or a subset of the required columns will not receive full credit.
