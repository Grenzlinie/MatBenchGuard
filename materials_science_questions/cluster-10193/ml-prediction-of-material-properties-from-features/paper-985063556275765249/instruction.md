# ML Prediction of Grain Boundary Segregation Energies and Occupancy States in NbMoTaW Alloy

## Problem background
In chemically complex concentrated alloys such as the refractory quaternary NbMoTaW, predicting interfacial solute segregation is critical for microstructural design, but direct atomistic simulations across the vast compositional space are computationally prohibitive. This task builds a computational pipeline that combines atomistic simulations with machine learning to efficiently estimate grain boundary segregation energies and occupancy states over a wide range of alloy compositions.

## Approach
The method first generates a polycrystalline NbMoTaW model and prepares 14 equiatomic base configurations. For each base-solute pair, site-specific segregation energies at zero temperature are obtained by sequentially substituting solute atoms at interface sites and comparing the relaxed energy to a bulk reference mode. Separately, hybrid Monte Carlo/molecular dynamics simulations at room temperature for solute concentrations from 5 at.% up to equiatomic provide binary occupancy labels for interface sites. Local atomic environments are vectorized using SOAP descriptors and reduced to 10 principal components. An artificial neural network regressor is trained on the SOAP-PCA features to predict segregation energies (regression target). An XGBoost classifier is then trained on the same features plus true segregation energies to predict occupancy states (classification target). Finally, a full machine learning pipeline is evaluated where the true segregation energies are replaced by the regression predictions, and the classifier's accuracy on this predicted input is assessed. The regressor performance is measured by mean absolute error and mean squared error on a held-out test set; the classifier's accuracy is evaluated on a stratified test split.

## Reproduction target
The objective is to compute and report three scored outputs from the full pipeline:
1. For the regressor, produce per-sample true vs. predicted segregation energies on the test split; the metrics MAE and MSE will be recomputed from this output.
2. For the classifier using true segregation energies, produce per-sample true occupancy states, predicted probabilities, and predicted binary states on the test split; classification accuracy will be recomputed.
3. For the full ML pipeline (predicted segregation energies replacing true energies), produce the same per-sample predictions on the test split; accuracy will again be recomputed.
The training must cover all chemical interactions (single-element and multi-element bases) up to equiatomic solute concentration, and the reported predictions must come from models trained as described in the workflow steps.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- Atomsk model builder: https://atomsk.univ-lille.fr/
- ASE Atomic Simulation Environment
- QUIP library (quippy-ase)
- Moment Tensor Potential for NbMoTaW: Available from Yin et al., Nat. Commun. 12, 4873 (2021); file NbMoTaW_MTF.mtp.
- TensorFlow / Keras
- XGBoost
- scikit-learn, matplotlib, seaborn, pandas, numpy
- OVITO visualization tool: https://www.ovito.org/

## Workflow steps

### Step 1: Generate polycrystalline NbMoTaW model
- Role: process
- Action: Use Atomsk to create a 50×50×50 Å³ simulation box with four randomly oriented grains of NbMoTaW and save the initial atomic configuration.
- Evidence: `/app/outputs/initial_polycrystal.data`

### Step 2: Prepare relaxed base configurations (A1)
- Role: process
- Action: Using LAMMPS with the MTP potential, create and relax 14 equiatomic base configurations (single-element and multi-element combinations) via NVT annealing and conjugate gradient minimization.
- Evidence: `/app/outputs/relaxed_bases.tar.gz`

### Step 3: Compute site-specific segregation energies at 0 K (A2)
- Role: process
- Action: For each compatible solute and each base, substitute solute atoms at interface sites, perform energy minimization, compute bulk binding energy mode, and calculate segregation energies as the difference. Collect all (base, solute, site) energies.
- Evidence: `/app/outputs/segregation_energies.csv`

### Step 4: Perform MC/MD simulations for occupancy labels (A3)
- Role: process
- Action: Run hybrid MC/MD simulations at room temperature for each base with solute concentrations from 5 at.% to equiatomic in 5 at.% increments, and assign binary occupancy labels (1 if solute-occupied, 0 otherwise) after equilibration.
- Evidence: `/app/outputs/mcmd_states.csv`

### Step 5: Preprocessing: SOAP vectorization and PCA
- Role: process
- Action: Compute SOAP descriptors (r_max=6 Å, l_max=12, n_max=12, sigma=1 Å) for all interface sites, standardize features, apply PCA to retain 10 principal components, and save the reduced features and PCA model.
- Evidence: `/app/outputs/pca_features.npy`

### Step 6: Train ANN regression model
- Role: process
- Action: Split the segregation-energy dataset into train/validation/test (70/20/10). Train an ANN regression model (ReLU, Adam, dropout, batch norm) to predict segregation energies from SOAP-PCA features and save the trained model.
- Evidence: `/app/outputs/ann_regression_model.h5`

### Step 7: Evaluate regression model and output predictions
- Role: scored
- Action: Apply the trained ANN to the held-out test set. Write a CSV file with true segregation energy and predicted segregation energy for each test sample.
- Output file: `/app/outputs/step_01_regression_predictions.csv`
- Format: csv
- Contract: CSV with columns: true_segregation_energy (float, eV), predicted_segregation_energy (float, eV).
- Scoring: scored by hidden verifier

### Step 8: Train XGBoost classifier using true segregation energies
- Role: process
- Action: Prepare classification dataset (SOAP-PCA features + true segregation energies, MC/MD states), split 80/20 stratified, train an XGBoost classifier and save the trained model.
- Evidence: `/app/outputs/xgboost_classifier_true.pkl`

### Step 9: Evaluate classifier with true energies and output predictions
- Role: scored
- Action: Apply the trained XGBoost model to the classification test set. Write a CSV file with true occupancy state, predicted probability, and predicted state.
- Output file: `/app/outputs/step_02_classification_predictions_true_energies.csv`
- Format: csv
- Contract: CSV with columns: true_state (0 or 1), predicted_probability (float), predicted_state (0 or 1).
- Scoring: scored by hidden verifier

### Step 10: Evaluate full ML pipeline using M1-predicted energies
- Role: scored (load-bearing)
- Action: For the classification test set, use the trained ANN regression model to predict segregation energies (in place of true energies). Feed these predicted energies together with SOAP-PCA features into the trained XGBoost classifier. Write a CSV file with true occupancy state, predicted probability, and predicted state.
- Output file: `/app/outputs/step_03_classification_predictions_predicted_energies.csv`
- Format: csv
- Contract: CSV with columns: true_state (0 or 1), predicted_probability (float), predicted_state (0 or 1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_regression_predictions.csv`
- `/app/outputs/step_02_classification_predictions_true_energies.csv`
- `/app/outputs/step_03_classification_predictions_predicted_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_regression_predictions.csv
- path: `/app/outputs/step_01_regression_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Regressor predictions on the held-out test set. Each row contains the true and predicted segregation energy (eV) for one interface site.
- schema:
  - `type`: table
  - `required_columns`: `true_segregation_energy`, `predicted_segregation_energy`
  - `units`:
    - `true_segregation_energy`: eV
    - `predicted_segregation_energy`: eV

### step_02_classification_predictions_true_energies.csv
- path: `/app/outputs/step_02_classification_predictions_true_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Classifier predictions using true segregation energies. true_state is 0 or 1, predicted_probability is the model's probability for state 1, predicted_state is binarised (0 or 1).
- schema:
  - `type`: table
  - `required_columns`: `true_state`, `predicted_probability`, `predicted_state`

### step_03_classification_predictions_predicted_energies.csv
- path: `/app/outputs/step_03_classification_predictions_predicted_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Classifier predictions using segregation energies predicted by the ANN (fully ML pipeline). Same schema as step_02.
- schema:
  - `type`: table
  - `required_columns`: `true_state`, `predicted_probability`, `predicted_state`

Notes: The checker recomputes regression MAE and MSE from step_01, and classification accuracy from step_02 and step_03, and evaluates them according to the hidden verification specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_regression_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "true_segregation_energy",
          "predicted_segregation_energy"
        ],
        "units": {
          "true_segregation_energy": "eV",
          "predicted_segregation_energy": "eV"
        }
      },
      "description": "Regressor predictions on the held-out test set. Each row contains the true and predicted segregation energy (eV) for one interface site."
    },
    {
      "file": "step_02_classification_predictions_true_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "true_state",
          "predicted_probability",
          "predicted_state"
        ]
      },
      "description": "Classifier predictions using true segregation energies. true_state is 0 or 1, predicted_probability is the model's probability for state 1, predicted_state is binarised (0 or 1)."
    },
    {
      "file": "step_03_classification_predictions_predicted_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "true_state",
          "predicted_probability",
          "predicted_state"
        ]
      },
      "description": "Classifier predictions using segregation energies predicted by the ANN (fully ML pipeline). Same schema as step_02."
    }
  ],
  "notes": "The checker recomputes regression MAE and MSE from step_01, and classification accuracy from step_02 and step_03, and evaluates them according to the hidden verification specification."
}
```

## How you are scored
A hidden verifier will independently score each of the three required output files. The verifier recomputes regression MAE and MSE from the submitted predictions, and classification accuracy from the submitted state predictions. The overall score is a weighted combination of these recomputed metrics, with each stage contributing a portion of the total reward. The verifier compares the recomputed metrics against hidden, domain-appropriate thresholds that reflect a successful reproduction. It is not enough to simply report the paper’s published numbers; your actual computed predictions must meet or exceed the required performance levels set by the verifier.
