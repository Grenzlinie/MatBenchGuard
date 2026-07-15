# Evaluating ML Accuracy for Bond Stretch and Torsional Potential Curves

## Problem background
Machine learning methods have been proposed as surrogates for time-consuming quantum mechanical calculations, promising rapid energy predictions once trained. While most efforts have focused on single-point energies at optimized geometries, an important open question is how well these methods perform across full potential energy curves — including bond stretching away from equilibrium and torsional conformational changes. This task evaluates the accuracy of several leading ML approaches for predicting bond-stretch potential energy curves and torsional potentials, using public datasets (ANI-1, ANI-1x) and reference density functional theory (DFT) calculations. The evaluation examines both qualitative behavior (correct equilibrium bond length, repulsive wall, long-range attractive forces, absence of spurious minima) and quantitative error near equilibrium.

## Approach
The workflow implements and compares four ML methods: two pretrained deep neural network potentials (ANI-1x and ANI-2x), a newly trained deep convolutional neural network (“Colorful CNN”) using libmolgrid, and a kernel ridge regression model built on the FCHL representation (FCHL/KRR) using the QML package. The Colorful CNN is trained on the full ANI-1x dataset, while FCHL/KRR is trained on a carefully selected subset of 5000 nonequilibrium geometries from ANI-1 to limit computational cost. All models predict total energies for a specified test suite of bond-stretch geometries (17 molecules, scanned in 0.1 Å steps) and dihedral scans (biphenyl, sucrose, dialanine, diglycine). The reference energies are DFT total SCF energies computed at the ωB97X/6-31G(d) level and are provided as part of the test set. From these predictions, a battery of evaluation metrics is computed: for bond stretches, per-molecule qualitative criteria (whether the minimum, repulsive wall, attractive forces, and spurious minima are correctly captured) together with the median mean absolute percent error (MAPE) within ±0.25 Å of the reference equilibrium bond length; for 1-D dihedral scans, the lowest-energy angle and the barrier between the lowest and highest conformer; and for 2-D torsion scans, the mean absolute error (MAE) between predicted and reference energies over the full grid.

## Reproduction target
Produce the following quantitative results:
1. For each of the 17 bond-stretch molecules and each of the four ML methods, compute:
   - whether the predicted lowest-energy geometry matches the DFT equilibrium bond length (r0_correct, 1/0);
   - whether a repulsive wall is correctly predicted under compression (repulsive_wall_correct, 1/0);
   - whether anharmonic attractive forces are captured beyond the equilibrium bond length (attractive_forces_correct, 1/0);
   - whether any spurious local or global minima appear after 2 Å (spurious_minima, 1/0);
   - the median mean absolute percent error (MAPE) over the energy values in the range r0 ± 0.25 Å.
   The results must be written to /app/outputs/bond_stretch_metrics.csv.
2. For biphenyl and sucrose dihedral scans, for each method, identify the lowest-energy dihedral angle (theta0, in degrees) and the energy barrier between the lowest and highest energy conformer (kcal/mol). Write to /app/outputs/dihedral_summary.csv.
3. For the 2-D torsion scans of dialanine and diglycine, compute the mean absolute error (MAE) between the predicted energies and the DFT reference energies over all (phi, psi) grid points. Write to /app/outputs/torsion_2d_mae.csv.
The task is considered successful if the computed metrics, obtained by re-running the training and evaluation pipeline, are consistent with the expected reference values within reasonable tolerances of a re-run (different seeds/implementations), with lower error always treated as improvement.

## Assets

- ANI-1 dataset (nonequilibrium geometries and energies): https://github.com/aiqm/ANI-1_release
- ANI-1x dataset: https://github.com/aiqm/ani1x_intermediate
- Pretrained ANI-1x model: https://github.com/aiqm/ani1x_intermediate
- Pretrained ANI-2x model: https://github.com/aiqm/ani2x_intermediate
- ml-benchmark repository (code, test geometries, reference DFT energies): https://github.com/hutchisonlab/ml-benchmark
- QML (Quantum Machine Learning) package: https://github.com/qmlcode/qml
- libmolgrid library: https://github.com/gnina/libmolgrid
- scikit-learn: scikit-learn

## Workflow steps

### Step 1: Prepare FCHL training subset
- Role: process
- Action: From the ANI-1 dataset, create a training subset of exactly 5000 nonequilibrium geometries. Randomly select 1000 molecules with up to 7 heavy atoms, then take 5 nonequilibrium geometries per selected molecule, excluding any molecule that appears in the test set (provided in the ml-benchmark repository).
- Evidence: `/app/outputs/fchl_subset_info.csv`

### Step 2: Train FCHL/KRR model
- Role: process
- Action: Using the QML package, train an FCHL representation plus kernel ridge regression (KRR) model on the 5000-geometry subset created in the previous step.
- Evidence: `/app/outputs/fchl_model.pkl`

### Step 3: Train Colorful CNN model
- Role: process
- Action: Using the code and configuration from the ml-benchmark repository, train a deep convolutional neural network (Colorful CNN) on the full ANI-1x dataset. The architecture consists of six modules separated by pooling, each with seven convolutional layers.
- Evidence: `/app/outputs/colorful_cnn_model.pt`

### Step 4: Acquire test set geometries and reference DFT energies
- Role: process
- Action: Obtain from the ml-benchmark repository the test set molecule geometries for all bond stretches (17 molecules, 0.1 Å increments) and dihedral scans (biphenyl, sucrose, dialanine, diglycine; 20° or 15° steps) and the corresponding reference total SCF energies (kcal/mol) computed at the ωB97X/6-31G(d) level. Organize into a structured CSV mapping each geometry ID to its coordinates and reference energy.
- Evidence: `/app/outputs/testset_reference.csv`

### Step 5: Generate ML energy predictions for all test geometries
- Role: process
- Action: Using the four models (pretrained ANI-1x, pretrained ANI-2x, the trained Colorful CNN, and the trained FCHL/KRR), predict the total energy for every geometry in the test set. Produce a CSV file (all_predictions.csv) containing the predictions and the reference energies.
- Evidence: `/app/outputs/all_predictions.csv`

### Step 6: Compute bond stretch metrics
- Role: scored (load-bearing)
- Action: From the predictions and reference energies, analyze the bond stretch data for the 17 molecules. For each method, compute: (1) whether the lowest predicted energy point matches the DFT equilibrium bond length (r0_correct, 1/0); (2) whether a repulsive wall is correctly predicted under compression (repulsive_wall_correct, 1/0); (3) whether anharmonic attractive forces are captured beyond r0 (attractive_forces_correct, 1/0); (4) whether any spurious minima appear after 2 Å (spurious_minima, 1/0); and (5) the median mean absolute percent error (MAPE) over the energy values in the range r0 ± 0.25 Å. Write the results to /app/outputs/bond_stretch_metrics.csv.
- Output file: `/app/outputs/bond_stretch_metrics.csv`
- Format: csv
- Contract: Columns: molecule, method, r0_correct (int), repulsive_wall_correct (int), attractive_forces_correct (int), spurious_minima (int), median_MAPE (float). One row per molecule per method. Methods: ANI-1x, ANI-2x, Colorful_CNN, FCHL_KRR. Molecules: benzene_CC, benzene_CH, methanol, methane, CO, H2, ethylene, water, acetylene, hydrogen_cyanide, N2, ammonia, biphenyl, aspartame, sucrose, dialanine, diglycine.
- Scoring: scored by hidden verifier

### Step 7: Compute dihedral scan summary
- Role: scored
- Action: From the predictions, extract the dihedral scan energies for biphenyl and sucrose. For each method, identify the lowest energy dihedral angle (theta0, in degrees) and compute the energy barrier between the lowest and highest energy conformer found in the scan (in kcal/mol). Write the results to /app/outputs/dihedral_summary.csv.
- Output file: `/app/outputs/dihedral_summary.csv`
- Format: csv
- Contract: Columns: molecule, method, theta0_deg (int), barrier_energy_kcal_per_mol (float). Molecules: biphenyl, sucrose. Methods: ANI-1x, ANI-2x, Colorful_CNN, FCHL_KRR.
- Scoring: scored by hidden verifier

### Step 8: Compute 2D torsion scan MAE
- Role: scored
- Action: From the predictions, for dialanine and diglycine, compute the mean absolute error (MAE) between the predicted energies and the DFT reference energies over all scanned (phi, psi) grid points. Write the MAE values to /app/outputs/torsion_2d_mae.csv.
- Output file: `/app/outputs/torsion_2d_mae.csv`
- Format: csv
- Contract: Columns: molecule, method, MAE_kcal_per_mol (float). Molecules: dialanine, diglycine. Methods: ANI-1x, ANI-2x, Colorful_CNN, FCHL_KRR.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bond_stretch_metrics.csv`
- `/app/outputs/dihedral_summary.csv`
- `/app/outputs/torsion_2d_mae.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bond_stretch_metrics.csv
- path: `/app/outputs/bond_stretch_metrics.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Per-molecule qualitative criteria counts and median MAPE for bond stretches; improvement over paper is not penalized.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `method`, `r0_correct`, `repulsive_wall_correct`, `attractive_forces_correct`, `spurious_minima`, `median_MAPE`
  - `units`:
    - `r0_correct`: 1/0
    - `repulsive_wall_correct`: 1/0
    - `attractive_forces_correct`: 1/0
    - `spurious_minima`: 1/0
    - `median_MAPE`: float

### dihedral_summary.csv
- path: `/app/outputs/dihedral_summary.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Lowest-energy dihedral angle and barrier for biphenyl and sucrose; checked within ±10° and ±20% tolerance.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `method`, `theta0_deg`, `barrier_energy_kcal_per_mol`
  - `units`:
    - `theta0_deg`: degrees (integer)
    - `barrier_energy_kcal_per_mol`: kcal/mol

### torsion_2d_mae.csv
- path: `/app/outputs/torsion_2d_mae.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Mean absolute error of 2D torsion scan energies; lower MAE is better.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `method`, `MAE_kcal_per_mol`
  - `units`:
    - `MAE_kcal_per_mol`: kcal/mol

Notes: All models must be trained or used as specified. The solver must produce all three scored CSV files under /app/outputs. The checker will compare against paper-reported values with appropriate tolerances and directional scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bond_stretch_metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "method",
          "r0_correct",
          "repulsive_wall_correct",
          "attractive_forces_correct",
          "spurious_minima",
          "median_MAPE"
        ],
        "units": {
          "r0_correct": "1/0",
          "repulsive_wall_correct": "1/0",
          "attractive_forces_correct": "1/0",
          "spurious_minima": "1/0",
          "median_MAPE": "float"
        }
      },
      "description": "Per-molecule qualitative criteria counts and median MAPE for bond stretches; improvement over paper is not penalized."
    },
    {
      "file": "dihedral_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "method",
          "theta0_deg",
          "barrier_energy_kcal_per_mol"
        ],
        "units": {
          "theta0_deg": "degrees (integer)",
          "barrier_energy_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Lowest-energy dihedral angle and barrier for biphenyl and sucrose; checked within ±10° and ±20% tolerance."
    },
    {
      "file": "torsion_2d_mae.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "method",
          "MAE_kcal_per_mol"
        ],
        "units": {
          "MAE_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Mean absolute error of 2D torsion scan energies; lower MAE is better."
    }
  ],
  "notes": "All models must be trained or used as specified. The solver must produce all three scored CSV files under /app/outputs. The checker will compare against paper-reported values with appropriate tolerances and directional scoring."
}
```

## How you are scored
A hidden automated verifier will read the three scored output files produced by your pipeline. For bond_stretch_metrics.csv, it will aggregate the per-molecule qualitative criteria into total counts per method and compare them against hidden reference values, allowing a small integer tolerance; it will also compare the median MAPE values, awarding full credit for results at or below the reference threshold (lower error is better) and partial credit for higher errors within a relative margin. For dihedral_summary.csv, it will check the lowest-energy angle within an angular tolerance and the barrier energy within a relative tolerance, again awarding full credit for meeting or exceeding the reference. For torsion_2d_mae.csv, it will compare the reported MAE values against hidden benchmarks, with full credit for values at or below the expected MAE and diminishing credit for larger errors. The final reward is a weighted sum of the scores from each artifact. Simply reporting the paper’s numbers without executing the training and evaluation steps will not produce valid intermediate artifacts and will not pass the verifier’s consistency checks.
