# ANN prediction of cyclic strain-hardening exponent and cyclic strength coefficient of steels from monotonic tensile properties

## Problem background
Predicting the cyclic strain-hardening exponent (n') and cyclic strength coefficient (K') of steels is essential for fatigue life estimation using the cyclic Ramberg–Osgood equation. These cyclic properties are usually determined from time-consuming and expensive cyclic tests, whereas monotonic tensile properties (yield stress, ultimate tensile strength, Brinell hardness, percent reduction in area) are readily available. An approximate method based on low-cycle fatigue properties (the compatibility equation) can estimate n' and K' but often yields substantial errors. This task investigates whether an artificial neural network (MLP) trained on monotonic tensile data can provide more accurate estimates of n' and K' than the compatibility equation.

## Approach
The approach uses a multilayer perceptron (MLP) neural network with one hidden layer to predict n' and K' separately. The input features are yield stress (σ_y), ultimate tensile strength (S_u), Brinell hardness (BHN), and percent reduction in area (RA%). The input features are normalized to the range [-1, 1] using training-set statistics.

For each property, an MLP is trained on a random split of the provided steel dataset, with the network employing hyperbolic tangent activation in the hidden layer and mean squared error (MSE) as the loss function. The optimal number of hidden neurons is searched in the range 2–10 using a validation procedure (e.g., a validation split or cross-validation), and the best model is selected based on the lowest validation MSE. Training can use the Levenberg–Marquardt algorithm or a suitable open‑source equivalent (such as Adam).

As a baseline, n' and K' are also calculated for every sample using the compatibility equation from the available fatigue constants in the dataset: n' = b / c and K' = fatigue strength coefficient / (fatigue ductility coefficient)^{b/c}.

After training, the best MLP models are used to predict on a held-out test set that was not seen during training or model selection. The mean relative error (MRE) of both the ANN predictions and the compatibility‑equation predictions will be evaluated on this test set. The comparison of these errors determines the relative predictive quality of the two methods.

## Reproduction target
The task requires the following:

- Train an MLP to predict n' and a separate MLP to predict K', using the provided steel properties dataset.
- For each property, split the data into training and test sets (e.g., 60/22 for n' and 36/12 for K'), normalize the inputs, and perform the architecture search to select the best model.
- Compute the compatibility‑equation predictions for all samples using the fatigue constants in the dataset.
- Generate two CSV files (`n_prime_predictions.csv` and `K_prime_predictions.csv`) containing the test‑set sample IDs, the true target values, the ANN predictions, and the compatibility‑equation predictions.
- The verifier will then compute the mean relative error (MRE) for both methods on each property and assess the predictive accuracy.

## Assets

- Steel monotonic and cyclic properties dataset

## Workflow steps

### Step 1: Load and preprocess data
- Role: process
- Action: Load the provided steel properties CSV. For n' prediction, use all 82 samples; for K' prediction, use only samples with a non-null K' value (48 samples). Split each dataset randomly into training and holdout test sets (e.g., 60/22 for n', 36/12 for K'). Normalize input features (yield stress, ultimate tensile strength, Brinell hardness, percent reduction in area) to the range [-1, 1] using training-set statistics.
- Evidence: none

### Step 2: Compute compatibility-equation predictions
- Role: process
- Action: Using the fatigue constants (b, c, fatigue strength coefficient, fatigue ductility coefficient) from the dataset, compute predicted n' (n'_eq2 = b/c) and predicted K' (K'_eq2 = fatigue strength coefficient / (fatigue ductility coefficient)^(b/c)) for every sample. These will serve as the baseline for comparison.
- Evidence: none

### Step 3: Train MLP for cyclic strain-hardening exponent n'
- Role: process
- Action: Train a multilayer perceptron (MLP) neural network with one hidden layer to predict n' from the normalized input features (yield stress, ultimate tensile strength, Brinell hardness, percent reduction in area). Use hyperbolic tangent activation for hidden neurons and mean squared error (MSE) loss. Explore architectures with hidden neuron counts from 2 to 10 using a validation split or cross-validation; select the best model based on lowest validation MSE. Use the Levenberg-Marquardt back-propagation algorithm or a suitable open-source equivalent (e.g., Adam optimizer).
- Evidence: `/app/outputs/n_prime_model.pth`

### Step 4: Train MLP for cyclic strength coefficient K'
- Role: process
- Action: Train a separate MLP for K' prediction using the same input features and similar architecture search (hidden neurons 2–10). Select the best model based on validation MSE.
- Evidence: `/app/outputs/K_prime_model.pth`

### Step 5: Evaluate n' predictions
- Role: scored (load-bearing)
- Action: Using the best trained n' model, predict n' for all test set samples. Also retrieve the pre-computed Eq.2 predictions and the true target n' for the same test samples. Write a CSV file containing these values.
- Output file: `/app/outputs/n_prime_predictions.csv`
- Format: csv
- Contract: CSV with columns: sample_id (string), target_n_prime (float), ann_prediction_n (float), eq2_prediction_n (float). One row per test sample.
- Scoring: scored by hidden verifier

### Step 6: Evaluate K' predictions
- Role: scored (load-bearing)
- Action: Using the best trained K' model, predict K' for all test set samples. Also retrieve the pre-computed Eq.2 predictions and the true target K' for the same test samples. Write a CSV file.
- Output file: `/app/outputs/K_prime_predictions.csv`
- Format: csv
- Contract: CSV with columns: sample_id (string), target_K_prime (float), ann_prediction_K (float), eq2_prediction_K (float). One row per test sample.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/n_prime_predictions.csv`
- `/app/outputs/K_prime_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### n_prime_predictions.csv
- path: `/app/outputs/n_prime_predictions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Test set predictions for cyclic strain-hardening exponent n'. The checker computes mean relative error (MRE) for ANN and Eq.2 predictions and evaluates predictive performance.
- schema:
  - `type`: table
  - `required_columns`: `sample_id`, `target_n_prime`, `ann_prediction_n`, `eq2_prediction_n`
  - `units`:
    - `target_n_prime`: dimensionless
    - `ann_prediction_n`: dimensionless
    - `eq2_prediction_n`: dimensionless

### K_prime_predictions.csv
- path: `/app/outputs/K_prime_predictions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Test set predictions for cyclic strength coefficient K'. The checker computes mean relative error (MRE) for ANN and Eq.2 predictions and evaluates predictive performance.
- schema:
  - `type`: table
  - `required_columns`: `sample_id`, `target_K_prime`, `ann_prediction_K`, `eq2_prediction_K`
  - `units`:
    - `target_K_prime`: MPa
    - `ann_prediction_K`: MPa
    - `eq2_prediction_K`: MPa

Notes: The checker inspects the CSV columns and computes evaluation metrics; scoring is based on the predictive performance of the submitted ANN and Eq.2 values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "n_prime_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample_id",
          "target_n_prime",
          "ann_prediction_n",
          "eq2_prediction_n"
        ],
        "units": {
          "target_n_prime": "dimensionless",
          "ann_prediction_n": "dimensionless",
          "eq2_prediction_n": "dimensionless"
        }
      },
      "description": "Test set predictions for cyclic strain-hardening exponent n'. The checker computes mean relative error (MRE) for ANN and Eq.2 predictions and evaluates predictive performance."
    },
    {
      "file": "K_prime_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample_id",
          "target_K_prime",
          "ann_prediction_K",
          "eq2_prediction_K"
        ],
        "units": {
          "target_K_prime": "MPa",
          "ann_prediction_K": "MPa",
          "eq2_prediction_K": "MPa"
        }
      },
      "description": "Test set predictions for cyclic strength coefficient K'. The checker computes mean relative error (MRE) for ANN and Eq.2 predictions and evaluates predictive performance."
    }
  ],
  "notes": "The checker inspects the CSV columns and computes evaluation metrics; scoring is based on the predictive performance of the submitted ANN and Eq.2 values."
}
```

## How you are scored
Your submission is scored by a hidden verifier that inspects the two scored output files. For each file, the verifier verifies the required columns and format, then computes the mean relative error (MRE) from the columns `target_*`, `ann_prediction_*`, and `eq2_prediction_*`. The reward for each property is based on the accuracy of the ANN predictions relative to the compatibility‑equation baseline on the test set. The overall reward is a weighted combination of the two scores. The verifier does not simply check whether you reported a specific number; it uses the actual predicted values you provide to calculate the error metrics. Your job is to train the models to the best of your ability and produce the prediction files as accurately as possible.
