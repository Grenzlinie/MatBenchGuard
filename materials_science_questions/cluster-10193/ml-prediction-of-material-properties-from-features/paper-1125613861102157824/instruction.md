# ML Prediction of Dielectric Constants from Molecular Descriptors

## Problem background
Polymers with high dielectric constants are crucial for advanced electronic and photovoltaic applications, such as capacitors, flexible electronics, and energy storage. The dielectric constant influences charge separation and transport, directly affecting device efficiency. Discovering new polymers with superior dielectric properties is challenging because the structure–property relationship is complex. Data mining and machine learning offer a route to accelerate this discovery: by calculating quantitative molecular descriptors and building predictive models, it becomes possible to estimate dielectric constants and identify promising candidates from large chemical spaces. This task focuses on reproducing a computational workflow that uses public data and open‑source tools to select the most relevant molecular descriptors via correlation analysis and to compare the predictive performance of several regression models.

## Approach
The workflow follows a standard cheminformatics‑machine‑learning pipeline. First, for every polymer in the dataset, a comprehensive set of molecular descriptors (approximately 1800) is computed with the Mordred package. These descriptors capture topological, geometric, and electronic attributes of the molecules. A feature‑selection step then identifies the descriptors most strongly correlated with the dielectric constant target. Pearson correlation is computed for each descriptor, and the six with the highest absolute correlation are retained as inputs for the machine‑learning models. The dataset is split into training (80 %) and test (20 %) sets. Six regression models are trained on the training set using 5‑fold cross‑validation; model choice and any hyperparameter tuning are left to your judgment. The six models compared are: Linear Regression, Gradient Boosting Regressor, Histogram‑based Gradient Boosting Regressor, Bagging Regressor, Decision Tree Regressor, and Random Forest Regressor. Finally, each model is evaluated on the held‑out test set, and its R² and RMSE on the test set are recorded.

## Reproduction target
Using the public polymer dielectric‑constant dataset from Kuenneth et al. (2021), compute all available Mordred descriptors for each polymer. Select the six descriptors with the highest absolute Pearson correlation with the dielectric constant and output them, along with their correlation coefficients, to /app/outputs/step_01_correlations.csv. Train the six regression models on an 80 % training split with 5‑fold cross‑validation and evaluate their performance on the 20 % test set. Save the per‑model average cross‑validation R² and RMSE to /app/outputs/step_02_model_metrics.csv.

## Assets

- Kuenneth et al. 2021 dielectric constant dataset: https://doi.org/10.1016/j.patter.2021.100238
- Mordred molecular descriptor calculator: mordred
- Python ML ecosystem (scikit-learn, pandas, numpy, matplotlib, seaborn): scikit-learn pandas numpy matplotlib seaborn

## Workflow steps

### Step 1: Acquire dielectric constant dataset
- Role: process
- Action: Download the polymer dielectric constant dataset from Kuenneth et al. 2021 (the dataset published as supplementary material for Patterns 2021, 2, 100238) and load the molecular structures and their dielectric constant values.
- Evidence: `/app/outputs/dataset_downloaded.log`

### Step 2: Generate Mordred molecular descriptors
- Role: process
- Action: For each molecule in the dataset, compute all Mordred descriptors using the Mordred package, producing a descriptor matrix (approximately 1800 descriptors per molecule).
- Evidence: `/app/outputs/mordred_descriptors.npy`

### Step 3: Feature selection via correlation analysis
- Role: scored
- Action: Compute the Pearson correlation of each Mordred descriptor with the dielectric constant target. Identify the six descriptors with the highest absolute correlation and record their descriptor names and correlation coefficients.
- Output file: `/app/outputs/step_01_correlations.csv`
- Format: csv
- Contract: Columns: descriptor_name (string), correlation (float). Contains exactly six rows.
- Scoring: scored by hidden verifier

### Step 4: Train regression models
- Role: process
- Action: Split the dataset into training (80%) and test (20%) sets. Train six regression models (LinearRegression, GradientBoostingRegressor, HistGradientBoostingRegressor, BaggingRegressor, DecisionTreeRegressor, RandomForestRegressor) using 5-fold cross-validation on the training set, with hyperparameter tuning as needed.
- Evidence: `/app/outputs/model_training_summary.json`

### Step 5: Evaluate models and report metrics
- Role: scored (load-bearing)
- Action: Evaluate each trained model on the held-out test set and compute its R² and RMSE on the test set. Save the metrics for all six models.
- Output file: `/app/outputs/step_02_model_metrics.csv`
- Format: csv
- Contract: Columns: model_name (string), R2 (float), RMSE (float). Contains six rows, one per model (LinearRegression, GradientBoostingRegressor, HistGradientBoostingRegressor, BaggingRegressor, DecisionTreeRegressor, RandomForestRegressor).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_correlations.csv`
- `/app/outputs/step_02_model_metrics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_correlations.csv
- path: `/app/outputs/step_01_correlations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Six selected molecular descriptors and their Pearson correlation coefficient with the dielectric constant. The values are compared against paper-reported numbers with a hidden absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `descriptor_name`, `correlation`
  - `items`:
    - `descriptor_name`: string
    - `correlation`: float

### step_02_model_metrics.csv
- path: `/app/outputs/step_02_model_metrics.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Test-set R² and RMSE for the six regression models. A higher R² or a lower RMSE than the paper's reported thresholds is considered equally or more successful; scoring degrades only for worse values.
- schema:
  - `type`: table
  - `required_columns`: `model_name`, `R2`, `RMSE`
  - `items`:
    - `model_name`: string
    - `R2`: float
    - `RMSE`: float

Notes: The downstream screening of 200k monomers and the top-30 polymer selection are excluded because the paper does not provide machine-readable monomer identifiers. This reproduction focuses on the verifiable feature-selection and model-comparison stages.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_correlations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "descriptor_name",
          "correlation"
        ],
        "items": {
          "descriptor_name": "string",
          "correlation": "float"
        }
      },
      "description": "Six selected molecular descriptors and their Pearson correlation coefficient with the dielectric constant. The values are compared against paper-reported numbers with a hidden absolute tolerance."
    },
    {
      "file": "step_02_model_metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_name",
          "R2",
          "RMSE"
        ],
        "items": {
          "model_name": "string",
          "R2": "float",
          "RMSE": "float"
        }
      },
      "description": "Test-set R² and RMSE for the six regression models. A higher R² or a lower RMSE than the paper's reported thresholds is considered equally or more successful; scoring degrades only for worse values."
    }
  ],
  "notes": "The downstream screening of 200k monomers and the top-30 polymer selection are excluded because the paper does not provide machine-readable monomer identifiers. This reproduction focuses on the verifiable feature-selection and model-comparison stages."
}
```

## How you are scored
A hidden verifier independently inspects the two scored output files. For step_01_correlations.csv, it compares each descriptor’s correlation coefficient against a hidden reference value within a specified absolute tolerance; a match within tolerance is required. For step_02_model_metrics.csv, the verifier checks each model’s R² (higher is better) and RMSE (lower is better) against hidden quality thresholds. A result that meets or exceeds a threshold earns full credit, while a worse value reduces the score proportionally. The final reward is a weighted combination of the per‑artifact scores; simply writing the paper’s reported numbers is not sufficient—the artifacts must be produced by executing the actual workflow.
