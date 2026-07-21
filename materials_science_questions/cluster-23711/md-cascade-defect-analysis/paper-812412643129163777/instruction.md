# Defect Formation in GaN Cascades via Molecular Dynamics

## Problem background
Ion irradiation of gallium nitride (GaN) is important for semiconductor device processing, but the microscopic mechanisms of damage production remain poorly understood. Molecular dynamics (MD) simulations can provide atomic-level insight into defect formation during collision cascades, provided a reliable interatomic potential is available. This task reproduces such a simulation study: you will implement a custom analytic bond-order potential for GaN, run MD simulations of ion-irradiation cascades at various recoil energies, and quantify the resulting point defect production and the threshold displacement energies for Ga and N atoms.

## Approach
The core of the approach is an analytic bond-order potential. The total energy is written as a sum over bonds, where each bond has a repulsive pair-like term and an attractive term moderated by an environment-dependent bond-order factor. The pair terms use Morse-like functional forms parameterized from the dimer properties, and the bond-order depends on the local coordination through a square-root dependence. A smooth cutoff function limits the interaction range. To handle close encounters during ion irradiation, the potential is blended with a ZBL universal repulsive potential at short distances. The interactions for all three pairs (Ga–Ga, Ga–N, N–N) are described by a single set of parameters that you must implement in LAMMPS (or an equivalent MD code).

With this potential, you will first determine the threshold displacement energy for Ga and N atoms by simulating at least 1000 random directions and recording the minimum kinetic energy that creates a stable Frenkel pair. Then you will run collision cascades in bulk wurtzite GaN for both nitrogen and gallium recoils at initial recoil energies of 200, 400, 1000, 2000, 5000, and 10000 eV. The simulation cell is chosen large enough to avoid self-interaction, and a Berendsen thermostat at the boundaries removes excess heat. After each cascade, point defects (vacancies, interstitials, antisites) are identified using a Voronoi polyhedron method or an equivalent Wigner–Seitz analysis. Finally, you compare the total vacancy production to the prediction of the Kinchin–Pease model, using your own average displacement energies as input.

## Reproduction target
You must produce three scored artifacts from your own simulations:

1. **Threshold displacement energies** – the spatial average and standard error of the minimum displacement energy for Ga and N atoms, obtained from at least 1000 random directions, written to `threshold_energies.json`.

2. **Average point defect counts per cascade** – for both N and Ga recoils, at each of the six recoil energies (200, 400, 1000, 2000, 5000, 10000 eV), report the mean number (over cascades) of N vacancies (V_N), Ga vacancies (V_Ga), N interstitials (I_N), Ga interstitials (I_Ga), N-on-Ga antisites (N_Ga), and Ga-on-N antisites (Ga_N). Write these as `defect_counts.csv`.

3. **Kinchin–Pease comparison** – compute the Kinchin–Pease predicted number of displaced atoms for each recoil type and energy using the appropriate average displacement energy (Ga_average for Ga recoils, N_average for N recoils) and compare it with the total number of vacancies (V_N + V_Ga) from your defect analysis. Report the recoil type, energy, total vacancy count, and KP prediction in `kinchin_pease_comparison.csv`.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/

## Workflow steps

### Step 1: Implement the GaN interatomic potential
- Role: process
- Action: Implement the analytic bond-order potential for GaN in LAMMPS (or an equivalent MD code) using the functional forms (Morse-like pair terms, bond-order factor, smooth blending with the ZBL short-range repulsion) and the parameter set (Ga-Ga, Ga-N, N-N) provided below. The implementation must correctly handle all element pairs, the cutoff function, and the environmental bond-order term.

| ij | Ga-Ga | Ga-N | N-N |
| --- | --- | --- | --- |
| γ | 0.007874 | 0.001632 | 0.76612 |
| S | 1.11 | 1.1122 | 1.4922 |
| β (Å⁻¹) | 1.08 | 1.968 | 2.05945 |
| D_e (eV) | 1.40 | 2.45 | 9.91 |
| R_e (Å) | 2.3235 | 1.921 | 1.11 |
| c | 1.918 | 65.207 | 0.178493 |
| d | 0.750 | 2.821 | 0.20172 |
| h = cos(θ₀) | 0.3013 | 0.518 | 0.045238 |
| μ (Å⁻¹) | 1.846 | 0.0 | 0.0 |
| R_cut (Å) | 2.87 | 2.9 | 2.2 |
| D_cut (Å) | 0.15 | 0.2 | 0.2 |
| r_f (Å) | 1.2 | 0.6 | 0.5 |
| b_f (Å⁻¹) | 12.0 | 12.0 | 12.0 |
- Evidence: `/app/outputs/potential_test.log`

### Step 2: Determine threshold displacement energies
- Role: scored
- Action: Using the implemented potential, run MD simulations to find the minimum and average displacement energy for Ga and N atoms. Sample at least 1000 random directions. For each direction, increase the initial kinetic energy until a stable Frenkel pair is created; record the minimum energy that creates a defect. Compute the spatial average and standard error. Output the results as threshold_energies.json.
- Output file: `/app/outputs/threshold_energies.json`
- Format: json
- Contract: {"Ga_average": number (eV), "Ga_error": number (eV), "N_average": number (eV), "N_error": number (eV)}
- Scoring: scored by hidden verifier

### Step 3: Run cascade simulations
- Role: process
- Action: Run MD simulations of collision cascades in bulk wurtzite GaN. For both N and Ga recoil types, simulate cascades at initial recoil energies of 200, 400, 1000, 2000, 5000, and 10000 eV. Use a simulation cell size that avoids self-interaction, Berendsen thermostat at the boundaries, and a variable timestep. Run at least 8 independent cascades per energy/recoil combination to gather statistics.
- Evidence: `/app/outputs/cascade_log.txt`

### Step 4: Defect analysis and reporting
- Role: scored (load-bearing)
- Action: For each cascade, identify point defects using the Voronoi polyhedron method (or equivalent Wigner-Seitz analysis). Compute the average numbers of N vacancies (V_N), Ga vacancies (V_Ga), N interstitials (I_N), Ga interstitials (I_Ga), N-on-Ga antisites (N_Ga), and Ga-on-N antisites (Ga_N) per cascade for each recoil type and energy, along with the standard error of the mean. Format the results as defect_counts.csv as specified.
- Output file: `/app/outputs/defect_counts.csv`
- Format: csv
- Contract: columns: recoil_type (string: Ga or N), energy_eV (int), V_N (float), V_Ga (float), I_N (float), I_Ga (float), N_Ga (float), Ga_N (float). Each row is a recoil-type/energy combination; all values are means over cascades.
- Scoring: scored by hidden verifier

### Step 5: Kinchin–Pease comparison
- Role: scored
- Action: Using the average displacement energies obtained in step_02 (Ga_average, N_average), compute the Kinchin–Pease predicted number of displaced atoms for each recoil energy according to E_D being the average displacement energy for the recoil atom type. Compare this prediction with the total number of vacancies (V_N + V_Ga) from step_04 for each recoil type and energy. Write a CSV with the total vacancies, the KP prediction, and the recoil/energy identifiers.
- Output file: `/app/outputs/kinchin_pease_comparison.csv`
- Format: csv
- Contract: columns: recoil_type (string: Ga or N), energy_eV (int), total_vacancies (float), kp_predicted_vacancies (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/threshold_energies.json`
- `/app/outputs/defect_counts.csv`
- `/app/outputs/kinchin_pease_comparison.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### threshold_energies.json
- path: `/app/outputs/threshold_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Average threshold displacement energies for Ga and N atoms, determined by sampling at least 1000 random directions.
- schema:
  - `type`: object
  - `required`:
    - `Ga_average`: number (eV)
    - `Ga_error`: number (eV)
    - `N_average`: number (eV)
    - `N_error`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Ga_average`: eV
    - `Ga_error`: eV
    - `N_average`: eV
    - `N_error`: eV

### defect_counts.csv
- path: `/app/outputs/defect_counts.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Average point defect counts per cascade for each recoil type and energy, determined by Voronoi polyhedron analysis.
- schema:
  - `type`: table
  - `required`:
    - `recoil_type`: string
    - `energy_eV`: int
  - `items`: object
  - `required_columns`: `recoil_type`, `energy_eV`, `V_N`, `V_Ga`, `I_N`, `I_Ga`, `N_Ga`, `Ga_N`
  - `units`:
    - `V_N`: count (mean over cascades)
    - `V_Ga`: count
    - `I_N`: count
    - `I_Ga`: count
    - `N_Ga`: count
    - `Ga_N`: count

### kinchin_pease_comparison.csv
- path: `/app/outputs/kinchin_pease_comparison.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Comparison of simulated total vacancy production to the Kinchin–Pease prediction using the agent's own displacement energies.
- schema:
  - `type`: table
  - `required`:
    - `recoil_type`: string
    - `energy_eV`: int
  - `items`: object
  - `required_columns`: `recoil_type`, `energy_eV`, `total_vacancies`, `kp_predicted_vacancies`
  - `units`:
    - `total_vacancies`: count
    - `kp_predicted_vacancies`: count

Notes: All scored artifacts are compared against hidden reference values derived from the paper with appropriate tolerances. Step 4 (defect_counts.csv) is load-bearing: correct counts require genuine execution of the potential implementation and cascade simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "threshold_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Ga_average": "number (eV)",
          "Ga_error": "number (eV)",
          "N_average": "number (eV)",
          "N_error": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Ga_average": "eV",
          "Ga_error": "eV",
          "N_average": "eV",
          "N_error": "eV"
        }
      },
      "description": "Average threshold displacement energies for Ga and N atoms, determined by sampling at least 1000 random directions."
    },
    {
      "file": "defect_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required": {
          "recoil_type": "string",
          "energy_eV": "int"
        },
        "items": {},
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
          "V_N": "count (mean over cascades)",
          "V_Ga": "count",
          "I_N": "count",
          "I_Ga": "count",
          "N_Ga": "count",
          "Ga_N": "count"
        }
      },
      "description": "Average point defect counts per cascade for each recoil type and energy, determined by Voronoi polyhedron analysis."
    },
    {
      "file": "kinchin_pease_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {
          "recoil_type": "string",
          "energy_eV": "int"
        },
        "items": {},
        "required_columns": [
          "recoil_type",
          "energy_eV",
          "total_vacancies",
          "kp_predicted_vacancies"
        ],
        "units": {
          "total_vacancies": "count",
          "kp_predicted_vacancies": "count"
        }
      },
      "description": "Comparison of simulated total vacancy production to the Kinchin–Pease prediction using the agent's own displacement energies."
    }
  ],
  "notes": "All scored artifacts are compared against hidden reference values derived from the paper with appropriate tolerances. Step 4 (defect_counts.csv) is load-bearing: correct counts require genuine execution of the potential implementation and cascade simulations."
}
```

## How you are scored
A hidden verifier evaluates each scored output file independently. The verifier compares your reported values to hidden reference values derived from the original study, using tolerances that account for legitimate run-to-run variability and implementation differences. For threshold energies, it checks that your averages fall within an acceptable range of the reference. For defect counts, each mean count is compared per recoil/energy combination. For the Kinchin–Pease comparison, the verifier verifies that your `kp_predicted_vacancies` are computed correctly from your own displacement energies using the standard Kinchin–Pease formula, and that the total vacancy counts are consistent with the sum of V_N and V_Ga in your `defect_counts.csv`. The reward is monotonic: better-than-reference results (e.g., more realistic damage production) are never penalized. Your final score is a weighted combination of the stage scores; merely reporting the paper's numbers without executing the simulations will not pass the structural consistency checks.
