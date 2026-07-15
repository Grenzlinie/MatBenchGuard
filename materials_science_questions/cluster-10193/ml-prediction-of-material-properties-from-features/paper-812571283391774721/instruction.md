# Feature Importance Analysis for Gradient-Boosted Band Gap Prediction of Photovoltaic Materials

## Problem background
Machine learning can dramatically accelerate the discovery of efficient inorganic photovoltaic materials. A critical step is to extract structure-relevant features from crystal structures and train a regression model to predict band gaps, then reveal which material descriptors most strongly influence the predictions. This task reproduces that feature-importance analysis: a gradient-boosted tree model is trained on a dataset of 2,398 inorganic light-harvesting compounds, using Voronoi-tessellation features, and the resulting feature importance ranking is evaluated to understand what drives band-gap behavior.

## Approach
The core idea is to generate features that capture both the composition and the local crystal-structure environment via Voronoi tessellation, then use recursive feature elimination with cross-validation (RFECV) to select a compact, non-redundant set, train a gradient-boosted regression (GBR) model, and examine the learned feature importances. The training dataset comes from the Computational Materials Repository and the Materials Project, providing crystal structures and high-throughput DFT band gaps. After splitting the data into training and test sets, a pipeline of feature generation, feature selection, model training, and evaluation is executed. Finally, the GBR model's internal feature importance percentages are extracted and ranked, revealing which descriptors the model relies on most heavily.

## Reproduction target
Train a gradient-boosted regression model on 80% of the 2,398 compounds, using Voronoi-tessellation features reduced from 271 to 41 by RFECV. Evaluate the model on the held-out 20% test set, reporting the coefficient of determination (R²), mean absolute error (MAE), and root mean squared error (RMSE). Then produce a CSV file listing all 41 selected features with their importance percentages, sorted from most to least important. The goal is to faithfully execute the feature-importance pipeline; the subsequent verification step will check whether the results align with expectations without revealing those expectations beforehand.

## Assets

- Computational Materials Repository (CMR) - New Light Harvesting Materials project: https://cmr.fysik.dtu.dk
- Materials Project database: https://materialsproject.org
- matminer: https://pypi.org/project/matminer/
- scikit-learn: https://pypi.org/project/scikit-learn/

## Workflow steps

### Step 1: Acquire training dataset
- Role: process
- Action: Retrieve the crystal structures and DFT band gaps for the 2,398 inorganic light-harvesting materials from the CMR New Light Harvesting Materials project and Materials Project database. Split data into 80% training and 20% test sets.
- Evidence: `/app/outputs/data_split_info.json`

### Step 2: Generate Voronoi tessellation features
- Role: process
- Action: Use matminer to compute 271 structure- and composition-dependent features from crystal structures via the Voronoi tessellation method.
- Evidence: `/app/outputs/features_initial.csv`

### Step 3: Feature selection with RFECV
- Role: process
- Action: Apply recursive feature elimination with 10-fold cross-validation using a GBR estimator on the training set to reduce the initial 271 features to a compact set of 41 important features.
- Evidence: `/app/outputs/selected_features.json`

### Step 4: Train GBR model
- Role: process
- Action: Train a gradient-boosted regression model on the training set using the selected 41 features and the known band gaps, with hyperparameter optimization via 10-fold cross-validation.
- Evidence: `/app/outputs/trained_model.pkl`

### Step 5: Evaluate model on test set
- Role: scored
- Action: Use the trained GBR model to predict band gaps on the held-out test set. Compute the coefficient of determination (R²), mean absolute error (MAE), and root mean squared error (RMSE).
- Output file: `/app/outputs/model_evaluation.json`
- Format: json
- Contract: A JSON object with keys: r_squared (float), mae (float, eV), rmse (float, eV).
- Scoring: scored by hidden verifier

### Step 6: Compute feature importance
- Role: scored (load-bearing)
- Action: Extract feature importance percentages from the trained GBR model for all 41 selected features. Sort by importance descending and write a CSV file.
- Output file: `/app/outputs/feature_importances.csv`
- Format: csv
- Contract: CSV with two columns: feature_name (string), importance_percent (float). The top-ranked features should include 'fraction of p-orbital valence', 'fraction of d-orbital valence', 'maximum of electronegativity', 'mean of covalent radius', 'most of melting temperature', etc.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_evaluation.json`
- `/app/outputs/feature_importances.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_evaluation.json
- path: `/app/outputs/model_evaluation.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Model test-set performance metrics (R², MAE, RMSE). R² must meet or exceed the hidden threshold derived from the paper's reported accuracy.
- schema:
  - `type`: object
  - `required`:
    - `r_squared`: number
    - `mae`: number
    - `rmse`: number
  - `units`:
    - `mae`: eV
    - `rmse`: eV

### feature_importances.csv
- path: `/app/outputs/feature_importances.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Feature importance percentages from the trained GBR model, sorted descending. Must contain the key features identified in the paper; importance values are compared to hidden reference values within an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `feature_name`, `importance_percent`
  - `units`:
    - `importance_percent`: percentage

Notes: The DFT screening pipeline is excluded because it relies on the proprietary PWmat package, for which no open-source equivalent can reproduce exact values. This task focuses on the ML feature importance analysis using only public data and open-source tools.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_evaluation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "r_squared": "number",
          "mae": "number",
          "rmse": "number"
        },
        "units": {
          "mae": "eV",
          "rmse": "eV"
        }
      },
      "description": "Model test-set performance metrics (R², MAE, RMSE). R² must meet or exceed the hidden threshold derived from the paper's reported accuracy."
    },
    {
      "file": "feature_importances.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "feature_name",
          "importance_percent"
        ],
        "units": {
          "importance_percent": "percentage"
        }
      },
      "description": "Feature importance percentages from the trained GBR model, sorted descending. Must contain the key features identified in the paper; importance values are compared to hidden reference values within an absolute tolerance."
    }
  ],
  "notes": "The DFT screening pipeline is excluded because it relies on the proprietary PWmat package, for which no open-source equivalent can reproduce exact values. This task focuses on the ML feature importance analysis using only public data and open-source tools."
}
```

## How you are scored
A hidden verifier independently scores each output file. Your model evaluation metrics are compared against a performance threshold (higher R² yields a better score), and your feature importance ranking and percentages are compared against reference values within allowed tolerances. Each scored artifact contributes a weighted share to the final reward. You must run the actual workflow—data acquisition, feature computation, feature selection, model training, and evaluation—because the verifier can distinguish a genuine reproduction from a guess; simply reporting numbers without running the pipeline is unlikely to succeed.
