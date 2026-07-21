# Predicting solid solubility limits from Hume-Rothery parameters using artificial neural networks

## Problem background
Hume-Rothery's rules provide qualitative guidance for predicting solid solubility in binary alloys based on atomic size, electrochemical (electronegativity) and valence differences. This work investigates whether artificial neural networks (ANNs) can learn a quantitative mapping from those same parameters to the maximum solid solubility limit (in at.%) for the 60 alloy systems originally examined by Hume-Rothery. The aim is to determine how well a properly trained network can capture the underlying relationship and to evaluate the resulting regression performance as a possible refinement over the original qualitative rules.

## Approach
A feed‑forward backpropagation neural network with two hidden layers is employed. Input features are functionalized as: size factor = (d_solute - d_solvent)/d_solvent (using atomic diameters), valence as an integer, and electronegativity difference = χ_solute - χ_solvent. The network uses a tan‑sigmoid activation in the first hidden layer and a linear (identity) output layer with one neuron. Training is performed with Bayesian Regularization to improve generalization. The 60 alloy samples are partitioned into five groups; a looped redistribution selects the testing split (4 groups for training, 1 for testing) and the optimal number of neurons in the first hidden layer that minimize a composite criterion φ = |M-1| + (1-R) + |B / B_max|, where M is the slope, B the intercept of the linear regression of predicted versus experimental solubility, and B_max is the maximum experimental solubility in the whole dataset. Once the best split and network configuration are found, per‑sample predictions on the chosen test set are generated, and the full set of regression metrics (R, M, B, mean absolute error, φ) is computed.

## Reproduction target
Implement the ANN workflow using the 60-alloy dataset compiled from standard phase-diagram handbooks. Produce two scored artifacts: (1) a CSV file (`testing_predictions.csv`) containing the per‑sample experimental and predicted solubility values for the selected test set (~12 alloys), and (2) a JSON file (`final_metrics.json`) containing the regression metrics derived from those predictions: correlation coefficient R, slope M, intercept B, mean absolute error (at.%), and the composite parameter φ = |M-1| + (1-R) + |B / B_max|. The metrics will be evaluated against hidden reference thresholds to assess the quality of the reproduction.

## Assets

- 60-alloy solubility and atomic parameter dataset
- NumPy: numpy
- Pandas: pandas
- Scikit-learn: scikit-learn
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Data compilation
- Role: process
- Action: Compile the 60-alloy dataset from the specified handbooks (Massalski, Moffatt, ASM Handbook, Stark & Wallace, Aylward & Findlay). For each alloy system, record solvent, solute, atomic diameters (or radii converted to diameters), valence, electronegativity, and the maximum solid solubility limit in at.%. Save the raw table as a CSV file.
- Evidence: `/app/outputs/60_alloy_raw.csv`

### Step 2: Feature engineering and scaling
- Role: process
- Action: Functionalize inputs: size factor = (d_solute - d_solvent)/d_solvent (use atomic diameters); valence as integer; electronegativity difference = χ_solute - χ_solvent. Apply min‑max scaling to map all inputs and the target solubility to the range [-1, 1]. Save the scaled feature matrix and target vector.
- Evidence: `/app/outputs/scaled_data.csv`

### Step 3: ANN training and hyperparameter optimization
- Role: process
- Action: Build a feed‑forward backpropagation network with two hidden layers: first hidden layer using tanh activation, second hidden layer linear (identity) with one neuron (solubility output). Train using Bayesian Regularization. Partition the 60 samples into 5 groups; use a 4:1 training:testing split. For a range of candidate numbers of neurons in the first hidden layer, loop over the 5-fold splits, train on 4 groups and test on the held-out group. For each test, compute linear regression of predicted vs experimental solubility and evaluate φ = |M-1| + (1-R) + |B/B_max| (where B_max is the maximum solubility in the dataset). Select the neuron count and fold split that minimize φ. Save the trained model and the indices of the selected test set.
- Evidence: `/app/outputs/best_model.pkl and test_split_indices.json`

### Step 4: Test set prediction generation
- Role: scored (load-bearing)
- Action: Load the best model and the chosen test split. Generate predicted solubility values for each system in the test set. Create a CSV file with columns: solvent, solute, experimental solubility (at.%), and predicted solubility (at.%).
- Output file: `/app/outputs/testing_predictions.csv`
- Format: csv
- Contract: CSV with header: solvent (str), solute (str), experimental_solubility_at_pct (float), predicted_solubility_at_pct (float). Number of rows equals test set size (~12).
- Scoring: scored by hidden verifier

### Step 5: Compute and report evaluation metrics
- Role: scored
- Action: Using the predictions from testing_predictions.csv, fit a linear regression (experimental vs predicted) to obtain slope M, intercept B, and correlation coefficient R. Compute mean absolute error (mean modulus of error) in at.% and φ = |M-1| + (1-R) + |B/B_max|, where B_max is the maximum experimental solubility in the dataset. Write these values to a JSON file.
- Output file: `/app/outputs/final_metrics.json`
- Format: json
- Contract: JSON object with keys: R (float), M (float), B (float), mean_absolute_error_at_pct (float), phi (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/testing_predictions.csv`
- `/app/outputs/final_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### testing_predictions.csv
- path: `/app/outputs/testing_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑sample predictions on the selected test set; the checker recomputes regression metrics (R, M, B, MAE, φ) from these values and compares them against hidden reference thresholds.
- schema:
  - `type`: table
  - `required_columns`: `solvent`, `solute`, `experimental_solubility_at_pct`, `predicted_solubility_at_pct`
  - `units`:
    - `experimental_solubility_at_pct`: at.%
    - `predicted_solubility_at_pct`: at.%

### final_metrics.json
- path: `/app/outputs/final_metrics.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Structure‑checked summary of the evaluation metrics; the primary scoring is based on the recomputed metrics from the CSV.
- schema:
  - `type`: object
  - `required`:
    - `R`: float
    - `M`: float
    - `B`: float
    - `mean_absolute_error_at_pct`: float
    - `phi`: float

Notes: The checker independently recomputes linear regression metrics from testing_predictions.csv and applies threshold‑or‑better scoring. The final_metrics.json file is only audited for presence of the required keys.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "testing_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "solvent",
          "solute",
          "experimental_solubility_at_pct",
          "predicted_solubility_at_pct"
        ],
        "units": {
          "experimental_solubility_at_pct": "at.%",
          "predicted_solubility_at_pct": "at.%"
        }
      },
      "description": "Per‑sample predictions on the selected test set; the checker recomputes regression metrics (R, M, B, MAE, φ) from these values and compares them against hidden reference thresholds."
    },
    {
      "file": "final_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "R": "float",
          "M": "float",
          "B": "float",
          "mean_absolute_error_at_pct": "float",
          "phi": "float"
        }
      },
      "description": "Structure‑checked summary of the evaluation metrics; the primary scoring is based on the recomputed metrics from the CSV."
    }
  ],
  "notes": "The checker independently recomputes linear regression metrics from testing_predictions.csv and applies threshold‑or‑better scoring. The final_metrics.json file is only audited for presence of the required keys."
}
```

## How you are scored
A hidden verifier independently scores each output. From the `testing_predictions.csv` predictions, the verifier recomputes the linear regression metrics (R, M, B, mean absolute error, φ) and applies a threshold‑or‑better policy: if the recomputed metric meets or exceeds a hidden reference threshold, you earn full credit for that metric; otherwise, partial credit is awarded based on how close the value is to the threshold. The `final_metrics.json` file is checked to ensure it contains all required keys (R, M, B, mean_absolute_error_at_pct, phi) and that they are numeric, but the scoring primarily depends on the recomputed quantities from the CSV, not on the self‑reported JSON values. The combined reward across all scored stages yields your final score.
