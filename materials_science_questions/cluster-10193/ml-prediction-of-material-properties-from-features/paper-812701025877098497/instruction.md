# SVM Regression for Oxygen Storage Capacity from Material Descriptors

## Problem background
Oxygen storage materials (OSMs) are critical components of three-way catalysts in automotive exhaust systems, where they buffer oxygen levels to maintain catalytic efficiency. The oxygen storage capacity (OSC) of an oxide depends on its composition and electronic structure. This task focuses on a materials-informatics study that built a support vector machine (SVM) regression model to predict OSC from descriptors derived from first-principles calculations and atomic properties. The model was trained on a dataset of measured OSC values and seven computed descriptors for a set of metal oxides. The key question is how well such a model can predict OSC under realistic cross-validation, which indicates its usefulness for screening candidate materials.

## Approach
The modeling pipeline consists of: (1) loading the training dataset of metal oxides, each described by seven physics-based features (e.g., cohesive energy, band gap, oxygen p-band center, electronegativity difference, molecular weight per oxygen, and average cation–oxygen distance) and a measured OSC value at 973 K; (2) standardizing the feature matrix to zero mean and unit variance; (3) performing a grid search over feature subsets and SVM hyperparameters (regularization C, RBF kernel coefficient γ, and ε-insensitive tube width) using leave-one-out cross-validation (LOOCV) to select the combination that minimizes prediction error; (4) training the final SVM on the full 57-sample dataset with the best configuration; and (5) generating LOOCV predictions for every sample, i.e., for each sample the model is trained on the other 56 and predicts the held-out one. The primary comparison is between the predicted and measured OSC, summarized by mean absolute error (MAE) and root mean square error (RMSE).

## Reproduction target
Produce a CSV file, loocv_predictions_973K.csv, that contains the leave-one-out cross-validation predictions for every oxide in the training set at 973 K. The file must have columns: compound_name (string), measured_OSC (float, μmol‑O/g), and predicted_OSC (float, μmol‑O/g). This file will be used to recompute the model’s MAE and RMSE on the training data under LOOCV.

## Assets

- OSC training dataset (measured OSC and seven descriptors for 60 oxides): 10.1039/c9ra09886k
- scikit-learn: scikit-learn
- numpy: numpy
- pandas: pandas

## Workflow steps

### Step 1: Load and standardize training dataset
- Role: process
- Action: Read the measured OSC values and the seven computed descriptors for the 60 metal oxides from the ESI file. Filter to samples with valid OSC at 973 K (57 entries). Standardize the feature matrix (zero mean, unit variance).
- Evidence: `/app/outputs/data_summary.json`

### Step 2: SVM regression with grid search and LOOCV
- Role: scored (load-bearing)
- Action: Using scikit-learn, perform grid search over descriptor subsets and SVM hyperparameters with leave-one-out cross-validation on the standardized data. Train the best model on the full training set for 973 K and generate LOOCV predictions for every sample.
- Output file: `/app/outputs/loocv_predictions_973K.csv`
- Format: csv
- Contract: Columns: compound_name (string), measured_OSC (float, μmol-O/g), predicted_OSC (float, μmol-O/g).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/loocv_predictions_973K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### loocv_predictions_973K.csv
- path: `/app/outputs/loocv_predictions_973K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: LOOCV predictions for all training samples at 973 K. The checker recomputes mean absolute error (MAE) and root mean square error (RMSE) from the measured and predicted columns and scores against hidden performance thresholds.
- schema:
  - `type`: table
  - `required_columns`: `compound_name`, `measured_OSC`, `predicted_OSC`
  - `units`:
    - `measured_OSC`: μmol-O/g
    - `predicted_OSC`: μmol-O/g

Notes: The agent must perform a genuine leave-one-out cross-validation. The checker does not verify LOOCV compliance automatically; it trusts the predictions and recomputes the headline errors. Only 57 samples with valid OSC at 973 K are used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "loocv_predictions_973K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound_name",
          "measured_OSC",
          "predicted_OSC"
        ],
        "units": {
          "measured_OSC": "μmol-O/g",
          "predicted_OSC": "μmol-O/g"
        }
      },
      "description": "LOOCV predictions for all training samples at 973 K. The checker recomputes mean absolute error (MAE) and root mean square error (RMSE) from the measured and predicted columns and scores against hidden performance thresholds."
    }
  ],
  "notes": "The agent must perform a genuine leave-one-out cross-validation. The checker does not verify LOOCV compliance automatically; it trusts the predictions and recomputes the headline errors. Only 57 samples with valid OSC at 973 K are used."
}
```

## How you are scored
A hidden verifier reads your loocv_predictions_973K.csv, recomputes the mean absolute error (MAE) and root mean square error (RMSE) from the measured and predicted columns, and compares them to a hidden performance standard. The scoring uses a threshold-or-better policy: lower errors give higher credit, and achieving or surpassing the hidden target earns full credit. Your predictions must be the result of an actual leave-one-out cross-validation procedure; the verifier does not automatically check for LOOCV compliance, but the model is expected to be trained and evaluated as described. The final reward is a weighted combination of all scored artifacts, with the main prediction artifact carrying the largest weight. No credit is given for simply reporting the paper’s numbers or guessing the hidden target; only the output artifacts are evaluated.
