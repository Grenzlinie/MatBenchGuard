# Predicting Cloud Point Temperatures of Polymer Solutions from Molecular Descriptors

## Problem background
Binary polymer–solvent phase behavior governs processing, purification, and formulation of polymeric materials. Thermodynamic models often provide only qualitative agreement, and predicting cloud point temperatures quantitatively across many chemistries and conditions is challenging. This task uses a curated database of cloud point measurements (6524 points, 21 polymers, 61 solvents) and machine learning to build models that predict cloud point temperatures from molecular descriptors of polymer repeat units and solvents, together with state variables (molecular weight, concentration, pressure, phase direction). The objective is to achieve accurate predictions on held-out test data and to assess how well the models extrapolate to polymer–solvent systems for which only a small number of cloud points are available.

## Approach
The approach encodes each polymer repeat unit SMILES and each solvent SMILES with RDKit molecular descriptors, retaining only non‑constant, finite descriptors (96 polymer descriptors and 120 solvent descriptors). These are concatenated with state descriptors (log Mw, PDI, sqrt(volume fraction), log(pressure)) and the one‑phase direction. All continuous features are standardized to zero mean and unit variance. The data are split stratified by polymer–solvent pair into 80% training, 10% validation, and 10% test sets. Two regression models—XGBoost and a feed‑forward neural network (TensorFlow/Keras)—are trained with early stopping on validation RMSE. Hyperparameters may be tuned with Hyperopt. After training, cloud point temperatures are predicted on the test set and recorded alongside the corresponding inputs. An extrapolation analysis is performed by leaving out one polymer entirely, training the XGBoost model on the remaining data, and then incrementally adding 0, 5, 10, 20, and 50 randomly chosen cloud points from the left‑out polymer to the training set (averaging over multiple random repeats). The test RMSE for that polymer is recorded at each addition level to evaluate how quickly the model adapts to a new polymer–solvent system.

## Reproduction target
Using the curated cloud point dataset available from the Polymer Property Predictor and Database (3PDb), the reproduction target is to:
- Train XGBoost and feed‑forward neural network regression models on the dataset using a stratified 80/10/10 train/validation/test split.
- Report the root‑mean‑squared error (RMSE) of cloud point temperature predictions on the test set for each model.
- Perform a leave‑one‑polymer‑out experiment with XGBoost, measuring the test RMSE for that polymer as a function of the number of cloud points added to the training set (0, 5, 10, 20, 50 added points, averaged over multiple random seeds), and demonstrate that the predictive error on the left‑out polymer decreases as more data points are added.

## Assets

- Curated Cloud Point Dataset: https://pppdb.uchicago.edu/
- RDKit: rdkit-pypi
- XGBoost: xgboost
- TensorFlow: tensorflow
- Hyperopt: hyperopt

## Workflow steps

### Step 1: Data retrieval and preparation
- Role: process
- Action: Fetch the curated cloud point dataset from the 3PDb website. Load the data and verify it contains the required fields: polymer repeat unit SMILES, solvent SMILES, Mw, PDI, volume fraction, pressure, one-phase direction, and observed cloud point temperature. Apply any filtering described in the paper (e.g., PDI < 6, minimum two points per polymer–solvent pair) to obtain exactly 6524 points.
- Evidence: `/app/outputs/data_loading.log`

### Step 2: Feature engineering and data splitting
- Role: process
- Action: Using RDKit, compute the full set of molecular descriptors for each polymer repeat unit SMILES and each solvent SMILES. Reduce to the non‑constant, finite descriptors (96 polymer descriptors and 120 solvent descriptors as described in the paper). Concatenate with state variables (log Mw, PDI, sqrt(volume fraction), log(pressure), one‑phase direction). Standardize all continuous features to zero mean and unit variance. Split the data stratified by polymer–solvent pair into 80% train, 10% validation, 10% test.
- Evidence: `/app/outputs/feature_processing.log`

### Step 3: Model training
- Role: process
- Action: Train an XGBoost regressor and a feed‑forward neural network (TensorFlow/Keras) on the training set. Use early stopping based on validation RMSE. Optionally tune hyperparameters (e.g., with Hyperopt) to minimize validation RMSE. Save the trained models.
- Evidence: `/app/outputs/model_training.log`

### Step 4: Test set evaluation
- Role: scored (load-bearing)
- Action: For both trained models (XGBoost and ANN), predict cloud point temperatures on the held-out test set. Write a CSV with each test sample's polymer SMILES, solvent SMILES, Mw, PDI, volume fraction, pressure, one‑phase direction, observed temperature, and the predicted temperatures from both models.
- Output file: `/app/outputs/step_01_test_predictions.csv`
- Format: csv
- Contract: Columns: polymer_SMILES (string), solvent_SMILES (string), Mw (float), PDI (float), volume_fraction (float), pressure (float), one_phase_direction (string, 'positive' or 'negative'), observed_temperature (float), predicted_temperature_XGBoost (float), predicted_temperature_ANN (float). One row per test sample.
- Scoring: scored by hidden verifier

### Step 5: Extrapolation analysis
- Role: scored (load-bearing)
- Action: Select a polymer with limited data (e.g., poly(vinyl alcohol) or polyisobutylene). Perform a leave‑one‑polymer‑out experiment using XGBoost: (a) train on all data except that polymer, evaluate RMSE on its held‑out test set; (b) incrementally add 5, 10, 20, 50 randomly chosen cloud points from that polymer to the training set, retrain, and record RMSE on the remaining test data for that polymer. Repeat each addition 10 times with different random seeds and average the RMSE. Write a CSV summarizing the results.
- Output file: `/app/outputs/step_02_extrapolation_results.csv`
- Format: csv
- Contract: Columns: polymer (string), num_added_cloud_points (int), RMSE (float). Rows for the levels 0, 5, 10, 20, 50, with the averaged RMSE across repeats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_test_predictions.csv`
- `/app/outputs/step_02_extrapolation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_test_predictions.csv
- path: `/app/outputs/step_01_test_predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Per-sample test set predictions for cloud point temperature. The verifier will compute RMSE between observed_temperature and each predicted column, then check that both RMSE values are at or below the hidden paper-derived threshold.
- schema:
  - `type`: table
  - `required_columns`: `polymer_SMILES`, `solvent_SMILES`, `Mw`, `PDI`, `volume_fraction`, `pressure`, `one_phase_direction`, `observed_temperature`, `predicted_temperature_XGBoost`, `predicted_temperature_ANN`
  - `units`:
    - `Mw`: g/mol
    - `pressure`: MPa
    - `observed_temperature`: °C
    - `predicted_temperature_XGBoost`: °C
    - `predicted_temperature_ANN`: °C

### step_02_extrapolation_results.csv
- path: `/app/outputs/step_02_extrapolation_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Extrapolation RMSE as a function of the number of added cloud points for a specific polymer. The verifier will read the RMSE value at num_added_cloud_points=20 and check that it is at or below the hidden paper-derived threshold.
- schema:
  - `type`: table
  - `required_columns`: `polymer`, `num_added_cloud_points`, `RMSE`
  - `units`:
    - `RMSE`: °C

Notes: The test set evaluation must be performed for both the XGBoost and ANN models. The extrapolation analysis may be conducted with the XGBoost model only, using a polymer that has few data points in the curated set.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_test_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "polymer_SMILES",
          "solvent_SMILES",
          "Mw",
          "PDI",
          "volume_fraction",
          "pressure",
          "one_phase_direction",
          "observed_temperature",
          "predicted_temperature_XGBoost",
          "predicted_temperature_ANN"
        ],
        "units": {
          "Mw": "g/mol",
          "pressure": "MPa",
          "observed_temperature": "°C",
          "predicted_temperature_XGBoost": "°C",
          "predicted_temperature_ANN": "°C"
        }
      },
      "description": "Per-sample test set predictions for cloud point temperature. The verifier will compute RMSE between observed_temperature and each predicted column, then check that both RMSE values are at or below the hidden paper-derived threshold."
    },
    {
      "file": "step_02_extrapolation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "polymer",
          "num_added_cloud_points",
          "RMSE"
        ],
        "units": {
          "RMSE": "°C"
        }
      },
      "description": "Extrapolation RMSE as a function of the number of added cloud points for a specific polymer. The verifier will read the RMSE value at num_added_cloud_points=20 and check that it is at or below the hidden paper-derived threshold."
    }
  ],
  "notes": "The test set evaluation must be performed for both the XGBoost and ANN models. The extrapolation analysis may be conducted with the XGBoost model only, using a polymer that has few data points in the curated set."
}
```

## How you are scored
A hidden verifier independently reads your output CSV files, recomputes the RMSE metrics from the observed and predicted columns, and compares them to hidden reference thresholds derived from the original study. The verifier also reads the extrapolation results and checks the RMSE trend at a specific number of added cloud points. Credit is awarded proportionally to how well your models' metrics meet or exceed these hidden thresholds; a better result is never penalized. Each scored stage (test set predictions and extrapolation analysis) contributes a share of the final reward; you must produce both output files to receive full credit. Reporting numbers alone without correctly executing the full pipeline will not succeed, as the verifier can reject submissions that fail structural or consistency checks.
