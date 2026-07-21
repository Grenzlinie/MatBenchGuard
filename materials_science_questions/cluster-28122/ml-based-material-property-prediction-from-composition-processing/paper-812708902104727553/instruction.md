# GBRT-based superalloy corrosion rate prediction from composition and time

## Problem background
Hot corrosion of superalloy components in aero‑engines (combustion chambers, turbine disks, etc.) can degrade performance and limit service life. Experimental testing is costly and slow, so there is strong interest in constructing data‑driven models that can predict the corrosion rate from the alloy's chemical composition and the exposure time, and that can identify which alloying elements are most influential. This task reproduces the development of a Gradient Boosting Regression Tree (GBRT) model that forecasts the hot‑corrosion rate of several typical superalloys from their main elemental concentrations and the corrosion time, and that evaluates the predictive performance as well as the relative importance of each input feature.

## Approach
The modeling is performed on a dataset built from five superalloys (GH3625, GH2132, GH605, GH3536, GH4738) whose bulk chemical compositions are tabulated (weight percents of up to 11 elements) and whose corrosion rates were measured at four exposure times (25 h, 50 h, 75 h, 100 h). This gives 60 examples; each is represented by 12 numerical features (the 11 composition percentages plus corrosion time) and a continuous target (corrosion rate in g/(m²·h)). A Gradient Boosting Regression Tree (GBRT) regressor from scikit‑learn is trained. The dataset is repeatedly split into random 90 % training and 10 % test subsets, with 10 such random repetitions. For each training subset, the hyper‑parameters (number of trees and maximum tree depth) are chosen by an inner grid search that uses 8‑fold cross‑validation. The best model from each outer split is then evaluated on its held‑out test set, and the test‑set mean squared error (MSE) and coefficient of determination (R²) are averaged across the 10 repetitions. Finally, the trained GBRT model’s built‑in feature importance scores are extracted, quantifying the contribution of each of the 12 inputs to the prediction of corrosion rate.

## Reproduction target
Build the 60‑sample dataset from the inline‑provided data. Implement the repeated train‑test split, hyper‑parameter tuning, and cross‑validation scheme described above using scikit‑learn’s GradientBoostingRegressor and GridSearchCV. After training, compute two output artifacts: (i) `metrics.json` containing the average test‑set MSE and R² over the 10 random splits; (ii) `feature_importance.json` containing the importance score for each of the 12 input features. The specific feature names are: 'Ni', 'Cr', 'Mo', 'Nb', 'Fe', 'Co', 'Si', 'Mn', 'Ti', 'Al', 'C', 'time'. Both output files must be written to `/app/outputs`.

## Assets

- scikit-learn: scikit-learn
- numpy: numpy
- pandas: pandas

## Workflow steps

### Step 1: Dataset assembly
- Role: process
- Action: Assemble the feature matrix (main chemical composition elements plus corrosion time) and target vector (corrosion rate) from the provided experimental data. The dataset contains 60 samples, each composed of alloy composition percentages for the relevant elements and corrosion rate measurements at multiple time points. One-hot encoding is not needed; use the numerical percentages and time as features.
- Evidence: none

### Step 2: GBRT model training and hyperparameter tuning
- Role: process
- Action: Implement a GradientBoostingRegressor from scikit-learn. Randomly split the dataset into 90% training and 10% test sets, repeating 10 times. For each training set, perform hyperparameter tuning using GridSearchCV over n_estimators and max_depth with 8-fold cross-validation and retain the best model for each split.
- Evidence: none

### Step 3: Model evaluation
- Role: scored (load-bearing)
- Action: For each of the 10 trained models, compute the mean squared error (MSE) and coefficient of determination (R²) on its held-out test set. Average the test MSE and test R² across the 10 runs. Write the averages to metrics.json with keys 'test_mse' and 'test_r2'.
- Output file: `/app/outputs/metrics.json`
- Format: json
- Contract: { "type": "object", "required": ["test_mse", "test_r2"], "properties": { "test_mse": {"type": "number"}, "test_r2": {"type": "number"} } }
- Scoring: scored by hidden verifier

### Step 4: Feature importance extraction
- Role: scored
- Action: Extract the feature_importances_ array from the best model (averaged across the 10 splits if desired) and map each of the 12 input feature names (e.g., 'Ni', 'Cr', 'Mo', 'Nb', 'Fe', 'Co', 'Si', 'Mn', 'Ti', 'Al', 'C', 'time') to its importance score. Write a JSON object mapping feature name to importance to feature_importance.json. All 12 features must be present.
- Output file: `/app/outputs/feature_importance.json`
- Format: json
- Contract: { "type": "object", "additionalProperties": {"type": "number"}, "minProperties": 12, "maxProperties": 12 }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/metrics.json`
- `/app/outputs/feature_importance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### metrics.json
- path: `/app/outputs/metrics.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Averaged test set mean squared error and R² score over 10 random train-test splits. The agent's model performance is compared against the paper's reported thresholds (hidden gold). Full credit for meeting or exceeding the expected threshold; worse results receive partial credit.
- schema:
  - `type`: object
  - `required`: `test_mse`, `test_r2`
  - `properties`:
    - `test_mse`:
      - `type`: number
    - `test_r2`:
      - `type`: number

### feature_importance.json
- path: `/app/outputs/feature_importance.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Feature importance scores for all 12 input features. The checker verifies that the sum of importances is approximately 1.0 and that the top-7 features (by importance) include 'time', 'Mn', 'Co', 'Al', 'Ni', 'Ti', 'Mo' with 'time' ranked highest.
- schema:
  - `type`: object
  - `additionalProperties`:
    - `type`: number
  - `minProperties`: 12
  - `maxProperties`: 12

Notes: The experimental dataset is provided inline in the instruction; no external data download is required. The scoring for metrics.json uses a threshold_or_better policy (test_mse and test_r2 thresholds hidden). Feature importance is validated structurally against the paper's reported ranking.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "test_mse",
          "test_r2"
        ],
        "properties": {
          "test_mse": {
            "type": "number"
          },
          "test_r2": {
            "type": "number"
          }
        }
      },
      "description": "Averaged test set mean squared error and R² score over 10 random train-test splits. The agent's model performance is compared against the paper's reported thresholds (hidden gold). Full credit for meeting or exceeding the expected threshold; worse results receive partial credit."
    },
    {
      "file": "feature_importance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "additionalProperties": {
          "type": "number"
        },
        "minProperties": 12,
        "maxProperties": 12
      },
      "description": "Feature importance scores for all 12 input features. The checker verifies that the sum of importances is approximately 1.0 and that the top-7 features (by importance) include 'time', 'Mn', 'Co', 'Al', 'Ni', 'Ti', 'Mo' with 'time' ranked highest."
    }
  ],
  "notes": "The experimental dataset is provided inline in the instruction; no external data download is required. The scoring for metrics.json uses a threshold_or_better policy (test_mse and test_r2 thresholds hidden). Feature importance is validated structurally against the paper's reported ranking."
}
```

## How you are scored
A hidden verifier independently scores each workflow artifact. For `metrics.json`, the verifier compares your reported test MSE and R² to withheld performance thresholds using a threshold‑or‑better policy: meeting or exceeding the expected standard yields full credit, while lower‑quality predictions receive proportionally less. For `feature_importance.json`, the verifier performs a structural audit that checks (1) whether the importance scores sum to approximately 1.0, and (2) whether the ranking of features (which elements and time are most influential) matches a reference ordering derived from the underlying physical behaviour. The exact ordering is not disclosed; your model must capture the correct relative importance through proper training and evaluation. The final reward is a weighted combination of the scores from the two checks, with the predictive performance carrying the largest weight.
