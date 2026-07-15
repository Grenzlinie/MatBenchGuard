# Variational Bayesian Neural Network Regression for Superconducting Critical Temperature Prediction

## Problem background
Superconducting materials exhibit zero electrical resistance below a critical temperature ($T_c$). Discovering new high-$T_c$ superconductors is expensive and time-consuming, so data-driven models that predict $T_c$ from elemental and formula-derived features can accelerate screening. This work focuses on building a probabilistic machine learning model that not only predicts $T_c$ but also provides intrinsic uncertainty estimates. The goal is to train a generative Bayesian neural network regression model and assess its predictive accuracy on a curated superconductor dataset.

## Approach
The core method is a Variational Bayesian Neural Network (VBNN) regression model. In contrast to a standard deterministic neural network, a Bayesian neural network places a prior distribution over the weights and learns a posterior distribution through variational inference. This formulation naturally captures prediction uncertainty and avoids overfitting via a Kullback-Leibler divergence penalty in the training objective. The model is trained using the Stochastic Gradient Variational Bayes (SGVB) algorithm, which employs a reparameterization trick to enable efficient gradient-based optimization of the evidence lower bound (ELBO). The network architecture is a feedforward design with one hidden layer. After training on a 70% random split of the dataset, the model predicts $T_c$ on the held-out 30% test split, and performance is quantified with the coefficient of determination ($R^2$) and root mean squared error (RMSE).

## Reproduction target
Train a Variational Bayesian Neural Network regression model on the Hamidieh 2018 curation of the SuperCon database (available from the UCI Machine Learning Repository). Use a 70% training / 30% test random split, a feedforward network with one hidden layer of 100 units, and the SGVB optimizer. Train for 1000 epochs with batch size 10. After training, apply the model to the test set features and output a CSV file containing the true and predicted $T_c$ values for every test sample. Then, from those predictions compute and record the $R^2$ and RMSE in a JSON file. The required final artifacts are `test_predictions.csv` and `metrics.json`.

## Assets

- Superconductivity Data (Hamidieh 2018 curation): https://archive.ics.uci.edu/ml/datasets/Superconductivity+Data
- TensorFlow: tensorflow
- Bayesian deep learning library (ZhuSuan or equivalent): zhusuan

## Workflow steps

### Step 1: Data loading and train-test split
- Role: process
- Action: Download the Superconductivity dataset from the UCI repository, load the features and Tc target, and randomly split into 70% training and 30% test sets. Prepare feature matrices and target vectors for model training.
- Evidence: `/app/outputs/data_prep_log.txt`

### Step 2: Variational Bayesian Neural Network model training
- Role: process
- Action: Train a Variational Bayesian Neural Network (VBNN) regression model on the training set. Use a feedforward network with one hidden layer of 100 units, a Gaussian variational posterior, and the Stochastic Gradient Variational Bayes (SGVB) optimization algorithm. Train for 1000 epochs with batch size 10.
- Evidence: `/app/outputs/training_log.txt`

### Step 3: Generate Tc predictions on the test set
- Role: scored (load-bearing)
- Action: Apply the trained VBNN model to the test set features and output a CSV file with true and predicted Tc values for every test sample.
- Output file: `/app/outputs/test_predictions.csv`
- Format: csv
- Contract: CSV with header: y_true, y_pred. Each row contains a floating-point true Tc value and the corresponding model-predicted Tc value.
- Scoring: scored by hidden verifier

### Step 4: Compute R² and RMSE evaluation metrics
- Role: scored
- Action: From the test predictions, compute the coefficient of determination (R²) and root mean squared error (RMSE) in Kelvin. Write the results to a JSON file.
- Output file: `/app/outputs/metrics.json`
- Format: json
- Contract: JSON object with keys: R2 (float, coefficient of determination) and RMSE (float, root mean squared error in Kelvin).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/test_predictions.csv`
- `/app/outputs/metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### test_predictions.csv
- path: `/app/outputs/test_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-sample test set predictions. The checker may recompute R² and RMSE from these values to validate the submission.
- schema:
  - `type`: table
  - `required_columns`: `y_true`, `y_pred`
  - `units`:
    - `y_true`: Kelvin
    - `y_pred`: Kelvin

### metrics.json
- path: `/app/outputs/metrics.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Headline R² and RMSE metrics. The checker compares these values against hidden gold values using threshold_or_better: higher R² and lower RMSE are better, and meeting or exceeding the reference earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `R2`: float (coefficient of determination)
    - `RMSE`: float (root mean squared error in Kelvin)

Notes: The '100 hidden layers' mention in the paper is interpreted as 100 hidden units in a single hidden layer. Exact random seed and weight initialization are not specified; reproduction is expected to achieve similar performance within tolerance. The solving agent may need a GPU for reasonable training time.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "test_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "y_true",
          "y_pred"
        ],
        "units": {
          "y_true": "Kelvin",
          "y_pred": "Kelvin"
        }
      },
      "description": "Per-sample test set predictions. The checker may recompute R² and RMSE from these values to validate the submission."
    },
    {
      "file": "metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "R2": "float (coefficient of determination)",
          "RMSE": "float (root mean squared error in Kelvin)"
        }
      },
      "description": "Headline R² and RMSE metrics. The checker compares these values against hidden gold values using threshold_or_better: higher R² and lower RMSE are better, and meeting or exceeding the reference earns full credit."
    }
  ],
  "notes": "The '100 hidden layers' mention in the paper is interpreted as 100 hidden units in a single hidden layer. Exact random seed and weight initialization are not specified; reproduction is expected to achieve similar performance within tolerance. The solving agent may need a GPU for reasonable training time."
}
```

## How you are scored
A hidden verifier examines your submitted `test_predictions.csv` and `metrics.json`. It first confirms the files exist, have the correct structure, and contain valid numeric data. It then evaluates the quality of the reproduction by comparing your reported $R^2$ and RMSE against reference values (or by recomputing the metrics from your raw predictions). Higher $R^2$ and lower RMSE indicate better performance and earn higher scores. The final reward is a weighted combination of checks across the two artifacts. Merely printing the paper's published numbers is insufficient; the submitted files must be genuine outputs of executing the full workflow described in the steps. The exact scoring thresholds and reference values are kept secret to prevent gaming, but an accurate reproduction following the prescribed method will achieve a high score.
