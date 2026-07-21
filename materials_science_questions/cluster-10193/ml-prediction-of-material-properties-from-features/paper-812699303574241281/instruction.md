# Support Vector Regression Prediction of Phosphor Thermal Quenching Temperature from Compositional Features

## Problem background
Solid-state white lighting demands phosphors that maintain their emission intensity at elevated operating temperatures. Eu³⁺-substituted oxide phosphors can serve as the red component, but their performance often degrades due to thermal quenching. The key indicator is T50, the temperature at which the emission intensity drops to 50% of its room-temperature value. Screening phosphors with high T50 experimentally is costly and time-consuming. This work develops a machine-learning approach to predict T50 directly from chemical composition, using a support vector regression model trained on a curated set of 134 experimentally measured phosphor compositions and their T50 values extracted from the literature.

## Approach
The method uses compositional features derived from elemental properties. For each phosphor composition, 35 elemental variables (e.g., atomic number, electronegativity, covalent radius) are obtained from a periodic table database. Each variable is aggregated across the constituent elements via five stoichiometrically weighted statistics: weighted average, difference, maximum, minimum, and standard deviation, yielding 175 compositional features. Three additional non-compositional features are added: host crystal system, host space group, and Eu³⁺ substitution concentration.  
- **Host crystal system** is encoded as an integer: cubic=1, hexagonal=2, trigonal=3, tetragonal=4, orthorhombic=5, monoclinic=6, triclinic=7.  
- **Host space group** is encoded as its international space group number (1–230).  
- **Eu³⁺ substitution concentration** is kept as a numeric value (e.g., a percentage or fraction as given in the literature).  

This yields an initial set of 178 features. All features are standardized to zero mean and unit variance. Recursive feature elimination (RFE) with a linear SVR estimator and leave-one-out cross-validation is used to select the optimal subset of features. Hyperparameters (cost C and epsilon) are tuned via exhaustive grid search with leave-one-out cross-validation. The final model is a support vector regression with a linear kernel using the selected features and the optimal hyperparameters. Leave-one-out cross-validation is performed on the full 134-sample dataset to obtain a predicted T50 for every compound.

## Reproduction target
Produce a CSV file with columns composition, experimental_t50 (K), and predicted_t50 (K) containing the leave-one-out cross-validated T50 predictions for all 134 phosphors. Compute the coefficient of determination (r²) and mean absolute error (MAE) between the experimental and predicted T50 values, and write these two metrics to a JSON file.

## Assets

- Supporting Information Tables S1 and S2 with the training data (134 phosphor compositions, experimental T50 values, and supplementary feature list) – see resources.json for access details.
- Elemental property data (35 elemental variables): mendeleev
- scikit-learn: scikit-learn
- numpy: numpy
- pandas: pandas

## Workflow steps

### Step 1: Extract and curate training data
- Role: process
- Action: Obtain the Supporting Information tables (Table S2). Extract the 134 phosphor compositions and their experimental T50 values. Apply the sanitization criteria: only retain T50 values reached within the measurement window (no extrapolation) and measurements starting at room temperature (~300 K). Ensure the final curated dataset contains exactly 134 compounds.

### Step 2: Construct initial 178 features and standardize
- Role: process
- Action: For each composition, compute 35 elemental properties for each constituent element (atomic number, atomic weight, Mendeleev number, covalent radius, etc.) using public periodic table data. Aggregate each property via weighted average, difference, maximum, minimum, and standard deviation using stoichiometric weights. Add the three non‑compositional features: host crystal system (encoded 1–7), host space group (1–230), and Eu³⁺ substitution concentration (numeric) as available from Table S2. Standardize all features to zero mean and unit variance.

### Step 3: Recursive feature elimination to select the optimal feature subset
- Role: process
- Action: Use a linear SVR estimator and leave-one-out cross-validation to recursively eliminate the five least important features per iteration. Monitor the cross‑validated coefficient of determination (r²) as a function of feature count and determine the optimal subset of features (the exact number will emerge from the RFE analysis). Record the indices of the selected features.

### Step 4: Hyperparameter tuning via grid search
- Role: process
- Action: Using only the selected features, perform an exhaustive grid search over cost C in {0.3, 1, 3, 10, 30, 100} and epsilon ε in {0.001, 0.01, 0.1, 1} with leave-one-out cross-validation. Identify the combination with the highest average r² and save the optimal hyperparameters.

### Step 5: Leave-one-out cross-validated predictions
- Role: scored (load-bearing)
- Action: Train a support vector regression model with linear kernel, using the optimal hyperparameters obtained from Step 4 on the selected features. Perform leave-one-out cross-validation on the entire 134‑sample curated dataset to obtain predicted T50 for every compound. Write a CSV file with columns: composition, experimental_t50 (K), predicted_t50 (K).
- Output file: `/app/outputs/step_01_predictions.csv`
- Format: csv
- Contract: composition (string), experimental_t50 (float, K), predicted_t50 (float, K); header row, comma-separated.
- Scoring: scored by hidden verifier

### Step 6: Compute and report performance metrics
- Role: scored
- Action: From the leave-one-out predictions, compute the coefficient of determination (r²) and mean absolute error (MAE) between experimental and predicted T50. Write these two metrics to a JSON file.
- Output file: `/app/outputs/step_02_metrics.json`
- Format: json
- Contract: {"r2": float, "mae": float}   (MAE is in Kelvin)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_predictions.csv`
- `/app/outputs/step_02_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_predictions.csv
- path: `/app/outputs/step_01_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Leave-one-out cross-validated predicted T50 values for the 134 phosphor compositions.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `experimental_t50`, `predicted_t50`
  - `units`:
    - `experimental_t50`: K
    - `predicted_t50`: K

### step_02_metrics.json
- path: `/app/outputs/step_02_metrics.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Performance metrics (r² and MAE) computed from the LOO predictions.
- schema:
  - `type`: object
  - `required`:
    - `r2`: float
    - `mae`: float
  - `units`:
    - `mae`: K

Notes: The checker recomputes r² and MAE from step_01_predictions.csv and compares against predefined thresholds. step_02_metrics.json is validated for consistency with the recomputed metrics.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "experimental_t50",
          "predicted_t50"
        ],
        "units": {
          "experimental_t50": "K",
          "predicted_t50": "K"
        }
      },
      "description": "Leave-one-out cross-validated predicted T50 values for the 134 phosphor compositions."
    },
    {
      "file": "step_02_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "r2": "float",
          "mae": "float"
        },
        "units": {
          "mae": "K"
        }
      },
      "description": "Performance metrics (r² and MAE) computed from the LOO predictions."
    }
  ],
  "notes": "The checker recomputes r² and MAE from step_01_predictions.csv and compares against predefined thresholds. step_02_metrics.json is validated for consistency with the recomputed metrics."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. The predictions CSV is used to recompute r² and MAE; those recomputed metrics are compared against predefined performance thresholds. The self‑reported metrics JSON is cross‑checked for consistency with the recomputed values and validated for correct format. The final reward is a weighted combination of the scores for all required artifacts.