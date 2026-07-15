# Perovskite Property Prediction with Multiple Regression Algorithms

## Problem background
Perovskite materials with the general formula ABO₃ exhibit a wide range of technologically important properties (e.g., formation energy, thermodynamic stability, crystal volume, and oxygen vacancy formation energy) that depend sensitively on the choice of A‑ and B‑site cations. High‑throughput density‑functional theory (DFT) calculations have produced large datasets that relate structural and chemical descriptors to these target properties, opening the door for machine‑learning‑driven property prediction. However, different regression algorithms respond differently to the data distribution, so selecting the best algorithm for each property is an open problem. This task trains four regression models on a public perovskite dataset and evaluates their predictive accuracy on four key properties, allowing us to see how algorithm choice affects the quality of property predictions.

## Approach
The workflow uses the cleaned perovskite dataset from Emery & Wolverton (2017) and splits it 80/20 into training and test sets. Features are normalized before training. For each of the four target properties — formation energy, thermodynamic stability, volume per atom, and oxygen vacancy formation energy — four regression models are trained independently on the training set: (i) Support Vector Regression with an RBF kernel, with the penalty C and kernel coefficient γ optimized by grid search; (ii) Random Forest regression; (iii) Ridge regression; and (iv) a Back‑Propagation Neural Network, with hidden‑layer size tuned empirically. For formation energy, stability, and volume the models use 11 descriptor features; for vacancy energy they use 12 features (adding one extra descriptor). After training, each model predicts on the held‑out test set, and three evaluation metrics — Mean Absolute Error (MAE), Mean Squared Error (MSE), and coefficient of determination (R²) — are computed between the predicted and DFT‑calculated values. All 16 (property, model) evaluation results are collected into a single CSV file.

## Reproduction target
Train the four regression models — SVM‑RBF, Random Forest, Ridge Regression, and BP Neural Network — on the public Emery & Wolverton perovskite dataset to predict formation energy, thermodynamic stability, volume per atom, and oxygen vacancy formation energy. Evaluate each trained model on the held‑out 20% test set and compute MAE, MSE, and R². Aggregate the metrics into a single CSV file named metrics.csv with the columns property, model, MAE, MSE, R2, containing one row for each of the 16 model‑property combinations.

## Assets

- High-throughput DFT calculations of formation energy, stability and oxygen vacancy formation energy of ABO3 perovskites: https://figshare.com/collections/High-throughput_DFT_calculations_of_formation_energy_stability_and_oxygen_vacancy_formation_energy_of_ABO3_perovskites/3846722
- scikit-learn: scikit-learn
- numpy: numpy
- pandas: pandas
- PyTorch or TensorFlow (for BPNN)

## Workflow steps

### Step 1: Data preparation and preprocessing
- Role: process
- Action: Download the public perovskite dataset from Figshare. Clean the data (remove duplicates, validate entries). Split the cleaned data into training (80%) and test (20%) sets. Normalize the feature columns (input descriptors) used for each prediction target.
- Evidence: `/app/outputs/cleaned_data_shape.txt`

### Step 2: Model training
- Role: process
- Action: For each of the four target properties (formation energy, thermodynamic stability, volume per atom, oxygen vacancy formation energy), train four regression models on the corresponding training set: SVM with RBF kernel (grid-search optimal penalty C and kernel coefficient gamma), Random Forest regressor, Ridge regression, and a Back-Propagation Neural Network (empirically tune hidden-layer size). Use the appropriate input feature columns as indicated in the paper (11 features for formation energy/stability/volume, 12 features for vacancy energy).
- Evidence: `/app/outputs/training_log.txt`

### Step 3: Evaluation and metrics generation
- Role: scored (load-bearing)
- Action: For each trained model, predict on the held-out test set (applying the same normalization) and compute MAE, MSE, and R² between predictions and true DFT values. Aggregate all 16 sets of metrics into a single CSV file with columns: property, model, MAE, MSE, R2.
- Output file: `/app/outputs/metrics.csv`
- Format: csv
- Contract: CSV with header: property,model,MAE,MSE,R2. property: one of formation_energy, stability, volume_per_atom, vacancy_energy. model: one of SVM-RBF, RF, RR, BPNN. 16 rows total.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/metrics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### metrics.csv
- path: `/app/outputs/metrics.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Aggregated evaluation metrics for all 16 model-property combinations.
- schema:
  - `type`: table
  - `required_columns`: `property`, `model`, `MAE`, `MSE`, `R2`
  - `description`: Each row is a (property, model) combination. property: one of formation_energy, stability, volume_per_atom, vacancy_energy. model: one of SVM-RBF, RF, RR, BPNN. MAE, MSE, R2 are floating-point numbers.

Notes: The scoring compares each row's MAE, MSE, and R² against hidden reference values using a directional threshold: lower MAE/MSE or higher R² than the threshold (with tolerance) earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "model",
          "MAE",
          "MSE",
          "R2"
        ],
        "description": "Each row is a (property, model) combination. property: one of formation_energy, stability, volume_per_atom, vacancy_energy. model: one of SVM-RBF, RF, RR, BPNN. MAE, MSE, R2 are floating-point numbers."
      },
      "description": "Aggregated evaluation metrics for all 16 model-property combinations."
    }
  ],
  "notes": "The scoring compares each row's MAE, MSE, and R² against hidden reference values using a directional threshold: lower MAE/MSE or higher R² than the threshold (with tolerance) earns full credit."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the file `/app/outputs/metrics.csv`. For each of the 16 rows, the verifier compares your reported MAE, MSE, and R² against reference values derived from the original study. The scoring uses a threshold‑based policy: for error metrics (MAE, MSE) where lower is better, your score is high when your error is at or below a generous tolerance of the reference, and decreases gradually as the error increases beyond that; for R² (higher is better), your score is high when your value is at or above a tolerance, decreasing as it falls below. The final reward is the average score across all rows. Simply printing the paper’s numbers is not enough — the verifier expects values that result from actually training and evaluating the models on the dataset.
