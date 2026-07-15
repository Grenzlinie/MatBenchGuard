# Prediction of Cocrystal Melting Temperature using Artificial Neural Network

## Problem background
Molecular cocrystals are multi-component solids that can tailor pharmaceutical properties such as solubility, stability, and bioavailability. The melting temperature of a cocrystal is a key physicochemical property that influences processing and performance. Predicting this temperature from the characteristics of the constituent molecules is challenging because it depends on a complex interplay of intermolecular forces, crystal packing, and molecular descriptors. Data-driven machine learning methods have been applied to model such structure-property relationships without requiring explicit knowledge of all underlying physical mechanisms. This task aims to build a quantitative model that estimates cocrystal melting temperatures from a set of computed molecular and crystal descriptors using an artificial neural network.

## Approach
A feedforward artificial neural network (ANN) is trained to map eight input descriptors – including lattice energy, electrostatic-to-van der Waals energy ratio, molecular weights, packing density, acidity differences, and the melting points of the individual components – to the cocrystal melting temperature. The network architecture consists of an input layer, one hidden layer with sigmoid activation functions, and a single output neuron representing the predicted temperature. Training is performed by backpropagation, minimizing the mean squared error between predicted and experimental temperatures. The available set of 61 cocrystals is split into a 55-sample training set and a 6-sample validation set. All input features are normalized to a common range, and the final predictions are converted back to Kelvin. Model performance is evaluated by calculating the average relative error on both the training and validation subsets.

## Reproduction target
Using the provided cocrystal dataset, train the ANN model on the predefined training split and generate melting temperature predictions for all 61 cocrystals. Save the results to a CSV file that includes the cocrystal name, experimental temperature, predicted temperature, and whether each sample belongs to the training or validation set. The verifier will compute the average relative error separately for the training and validation groups from your predictions. The target is to obtain errors that fall within an acceptable tolerance of the values achieved in the original study, demonstrating that the model has successfully learned the underlying structure–temperature relationship.

## Assets

- Cocrystal dataset
- NumPy: https://pypi.org/project/numpy/
- Pandas: https://pypi.org/project/pandas/
- scikit-learn: https://pypi.org/project/scikit-learn/

## Workflow steps

### Step 1: Data loading and train/validation split
- Role: process
- Action: Load the provided cocrystal_dataset.csv, normalize the 8 input features to [0,1] using training set statistics, and split the data: reserve the 6 cocrystals (THP:SAC, CAF:4F3NAN, INA:ADA, INA:4HBA, INA:GTA, NA:GTA) as the validation set; use the remaining 55 as the training set.
- Evidence: `/app/outputs/split_info.json`

### Step 2: ANN model training
- Role: process
- Action: Train a feedforward neural network regression model with architecture 8-8-1 (8 input neurons, one hidden layer with 8 neurons, 1 output neuron), sigmoid activation in hidden and output layers, backpropagation with learning rate 0.3 and momentum 0.5. Use the 55-sample training set to minimize mean squared error.
- Evidence: `/app/outputs/model.pkl`

### Step 3: Generate predictions
- Role: scored (load-bearing)
- Action: Apply the trained model to all 61 samples (after appropriate inverse-normalization of the output to the original Kelvin scale). Create predictions.csv with columns: cocrystal_name, experimental_Tm (K), predicted_Tm (K), split ('training' or 'validation').
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: columns: cocrystal_name (string), experimental_Tm (float, K), predicted_Tm (float, K), split (string: 'training' or 'validation'); 61 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV containing the cocrystal name, experimental melting temperature, predicted melting temperature, and split designation (training/validation) for all 61 cocrystals.
- schema:
  - `type`: table
  - `required_columns`: `cocrystal_name`, `experimental_Tm`, `predicted_Tm`, `split`
  - `units`:
    - `experimental_Tm`: K
    - `predicted_Tm`: K

Notes: The checker recomputes the average relative error for training and validation sets from this file and compares each to a hidden gold threshold (paper-reported values + tolerance) using a threshold_or_better policy. The validation split must list exactly the six specified cocrystals.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cocrystal_name",
          "experimental_Tm",
          "predicted_Tm",
          "split"
        ],
        "units": {
          "experimental_Tm": "K",
          "predicted_Tm": "K"
        }
      },
      "description": "CSV containing the cocrystal name, experimental melting temperature, predicted melting temperature, and split designation (training/validation) for all 61 cocrystals."
    }
  ],
  "notes": "The checker recomputes the average relative error for training and validation sets from this file and compares each to a hidden gold threshold (paper-reported values + tolerance) using a threshold_or_better policy. The validation split must list exactly the six specified cocrystals."
}
```

## How you are scored
A hidden verifier will examine your output files after the workflow finishes. Each scored stage contributes a weighted fraction to the overall reward (a number between 0 and 1). The verifier recomputes the required metrics from your raw artifacts and compares them against confidential reference thresholds. Reporting a metric value without executing the corresponding workflow stage will not satisfy the requirement; the submitted artifacts must be the genuine products of the specified steps. There is no need to guess the exact numbers from the literature – the checker will determine whether your model’s performance meets the hidden criteria.
