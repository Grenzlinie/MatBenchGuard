# Scalar Elasto-Plastic Model with Rejuvenation: Stress-Strain, Yield Stress Evolution, and Localization

## Problem background
Amorphous solids such as glasses deform plastically via localized rearrangements known as shear transformations. These rearrangements interact through long-range elastic fields, leading to complex collective behavior including strain hardening, yield stress evolution, and shear band localization. Mesoscopic elasto-plastic models (EPMs) aim to capture these phenomena with a reduced description in which the material is discretized into cells that yield when local stress exceeds a threshold. A key challenge is connecting such mesoscopic models to the underlying atomistic disorder: what distributions of yield thresholds and post-yield slip increments, and what renewal rule for thresholds after a plastic event, reproduce the plastic behavior observed in atomistic simulations? This task explores a simple scalar EPM in which the renewal distribution is taken from a “rejuvenated” glass quenched near the mode-coupling transition, and the slip increment mean depends quadratically on the local threshold. The objective is to assess whether this approach can reproduce the strain-induced evolution of mean yield stress and the localization dynamics observed in atomistic simulations of a well-annealed glass.

## Approach
The reproduction proceeds in two main stages. First, atomistic simulations of a binary Lennard-Jones glass are performed using LAMMPS to prepare three glasses with different thermal histories (a gradually quenched glass, a fast-quenched glass, and a glass quenched from near the mode-coupling temperature). The frozen-matrix method is used to measure the local yield stress distributions for each glass and the average elastic moduli. Second, a scalar EPM on a periodic square lattice is implemented: each cell carries a local shear stress and a yield threshold; plastic events add a random slip increment drawn from an exponential distribution whose mean depends quadratically on the current threshold; the event also renews the threshold by drawing from a specified distribution (in the rejuvenation scenario, the MCT distribution). The model parameters (two coefficients controlling the slip-increment mean) are tuned by requiring the mesoscopic stress-strain curve for the gradually quenched glass to match the corresponding atomistic curve in peak stress and flow stress. After calibration, the EPM is run under athermal quasistatic shear to large strain, and three quantities are recorded: the macroscopic stress, the spatial average of the local yield stress, and a localization index based on the fourth moment of the plastic strain field.

## Reproduction target
Produce three CSV files from the calibrated rejuvenation EPM simulation for the gradually quenched glass, spanning shear strain from 0 to 5:

- /app/outputs/stage1_stress_strain.csv: two columns, strain and stress, capturing the macroscopic stress-strain curve.
- /app/outputs/stage2_mean_yield_stress.csv: two columns, strain and mean_threshold, capturing the evolution of the spatially averaged local yield stress.
- /app/outputs/stage3_localization_index.csv: two columns, strain and LOC, capturing the localization index.

The model must be tuned to match the atomistic reference for stress-strain (the reference curve obtained from the atomistic AQS simulation). The exact target values for these curves are not specified.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov
- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Atomistic glass preparation and local yield stress measurement
- Role: process
- Action: Using LAMMPS, prepare three binary Lennard-Jones glasses (ESL, GQ, MCT) following the protocols in Barbot et al. (Phys. Rev. E 97, 033001). Execute the frozen matrix method to measure the local yield stress distributions P(sigma_c) for each glass and the elastic moduli (mu, K). Save the resulting histograms/tables and mean moduli as intermediate files.
- Evidence: `/app/outputs/step01_yield_stress_data.csv`

### Step 2: Slip-increment distribution parameter fitting
- Role: process
- Action: Implement the scalar EPM with the extracted distributions (GQ initial, MCT renewal) and the exponential slip-increment distribution with mean epsilon_0(sigma_c) = c0 + c1*sigma_c^2. Tune c0 and c1 by running mesoscopic simulations for the GQ glass at multiple (c0,c1) values to match the atomistic GQ stress-strain reference (plateau flow stress and peak stress). Record the chosen (c0,c1) as a fitted-parameters file.
- Evidence: `/app/outputs/step02_fitted_parameters.json`

### Step 3: Macroscopic stress-strain curve from rejuvenation EPM simulation
- Role: scored (load-bearing)
- Action: Run the scalar EPM on an N×N periodic lattice (N=16 or larger) with the fitted (c0,c1) and the distributions obtained in step_atomistic, using the rejuvenation renewal rule (draw from MCT distribution). Apply athermal quasistatic shear up to strain=5. Record the macroscopic stress Sigma at regular strain intervals and write a two-column CSV (strain, stress).
- Output file: `/app/outputs/stage1_stress_strain.csv`
- Format: csv
- Contract: Two-column CSV: 'strain' (float, shear strain gamma), 'stress' (float, macroscopic shear stress Sigma)
- Scoring: scored by hidden verifier

### Step 4: Mean local yield stress evolution from rejuvenation EPM simulation
- Role: scored (load-bearing)
- Action: From the same EPM simulation as step_stress_strain, compute the spatially averaged local yield stress (mean over all cells of their current sigma_c^ij) at the same strain values. Write a two-column CSV (strain, mean_threshold).
- Output file: `/app/outputs/stage2_mean_yield_stress.csv`
- Format: csv
- Contract: Two-column CSV: 'strain' (float), 'mean_threshold' (float, spatial average of cell local yield stress)
- Scoring: scored by hidden verifier

### Step 5: Localization index evolution from rejuvenation EPM simulation
- Role: scored (load-bearing)
- Action: From the same EPM simulation, compute the localization index LOC(gamma) = sum(epsilon_ij^4) / (sum(epsilon_ij^2)^2) where epsilon_ij is the local plastic strain field. Record LOC at the same strain values. Write a two-column CSV (strain, LOC).
- Output file: `/app/outputs/stage3_localization_index.csv`
- Format: csv
- Contract: Two-column CSV: 'strain' (float), 'LOC' (float, localization index as defined in paper)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stage1_stress_strain.csv`
- `/app/outputs/stage2_mean_yield_stress.csv`
- `/app/outputs/stage3_localization_index.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stage1_stress_strain.csv
- path: `/app/outputs/stage1_stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Macroscopic stress-strain curve Sigma(gamma) for the GQ glass with rejuvenation. Scored by RMSE against hidden reference curve; lower RMSE is better.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: arbitrary unit

### stage2_mean_yield_stress.csv
- path: `/app/outputs/stage2_mean_yield_stress.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Evolution of the spatially averaged local yield stress bar_sigma_c(gamma) for the GQ glass. Scored by RMSE and qualitative trend (initial increase, subsequent decrease) against hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `mean_threshold`
  - `units`:
    - `strain`: dimensionless
    - `mean_threshold`: arbitrary unit

### stage3_localization_index.csv
- path: `/app/outputs/stage3_localization_index.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Localization index LOC(gamma) for the GQ glass. Scored by RMSE and qualitative check of peak and subsequent decay against hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `LOC`
  - `units`:
    - `strain`: dimensionless
    - `LOC`: dimensionless

Notes: The three scored artifacts are produced by a single EPM simulation run; they are separated for scoring clarity. The hidden checker holds digitised reference curves from the paper and evaluates RMSE within tolerances, plus qualitative feature checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stage1_stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "arbitrary unit"
        }
      },
      "description": "Macroscopic stress-strain curve Sigma(gamma) for the GQ glass with rejuvenation. Scored by RMSE against hidden reference curve; lower RMSE is better."
    },
    {
      "file": "stage2_mean_yield_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "mean_threshold"
        ],
        "units": {
          "strain": "dimensionless",
          "mean_threshold": "arbitrary unit"
        }
      },
      "description": "Evolution of the spatially averaged local yield stress bar_sigma_c(gamma) for the GQ glass. Scored by RMSE and qualitative trend (initial increase, subsequent decrease) against hidden reference."
    },
    {
      "file": "stage3_localization_index.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "LOC"
        ],
        "units": {
          "strain": "dimensionless",
          "LOC": "dimensionless"
        }
      },
      "description": "Localization index LOC(gamma) for the GQ glass. Scored by RMSE and qualitative check of peak and subsequent decay against hidden reference."
    }
  ],
  "notes": "The three scored artifacts are produced by a single EPM simulation run; they are separated for scoring clarity. The hidden checker holds digitised reference curves from the paper and evaluates RMSE within tolerances, plus qualitative feature checks."
}
```

## How you are scored
Each of the three scored artifacts will be evaluated by a hidden verifier. For each curve, the verifier compares your computed values to a reference curve using a quantitative error metric and checks that the required qualitative trends are present. The three component scores are then weighted and combined to produce a final reward between 0 and 1. Simply reporting a number is not sufficient—the verifier computes the metric directly from your CSV files. The better the agreement with the reference and the clearer the trends, the higher your score.
