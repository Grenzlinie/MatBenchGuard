# Machine Learning Prediction of Perovskite Catalytic Properties Using Elemental Features

## Problem background
Perovskite oxides are widely studied catalysts for the oxygen reduction and evolution reactions in solid oxide fuel cells and electrolyzers. Discovering new high-performing perovskite compositions requires fast and accurate predictions of catalytic properties such as oxygen surface exchange rates (k*, k_chem), oxygen diffusivities (D*, D_chem), and area specific resistance (ASR). Traditional high-throughput screening often relies on the DFT-calculated O p-band center as a descriptor, which is computationally expensive. This work investigates whether machine learning models that use only computationally inexpensive elemental features can achieve predictive accuracy comparable to or better than models that use the DFT-derived O p-band center, potentially enabling much faster screening of new materials.

## Approach
This task compares two modeling approaches for predicting perovskite catalytic properties at 500 °C using a published database of 749 experimental data points (Jacobs et al., 2023).

First, the perovskite compositions are represented via elemental features generated with the MAST‑ML ElementalFeatureGenerator, yielding composition‑weighted averages, maxima, minima, differences, and categorical encodings of tabulated elemental properties. For each of the five target properties (k*, D*, k_chem, D_chem, ASR), two regression models are trained:
- A random forest regressor that uses only the elemental features. For ASR, the model additionally includes one‑hot encoding of the electrolyte type.
- A univariate linear regression model that uses only the DFT‑calculated O p‑band center as the sole feature.

Both types of models are evaluated via 25 repeats of 5‑fold cross‑validation on the same dataset. The average mean absolute error (MAE) over all splits is computed for each property and each model. Finally, the percentage reduction in average MAE when moving from the O p‑band center linear regression to the elemental‑feature random forest is calculated as:
`percent_reduction = 100 × (MAE_ML − MAE_O_pband) / MAE_O_pband`.
The results for all five properties are collected into a single output file.

## Reproduction target
Produce a CSV file (`comparison_results.csv`) that contains, for each of the five catalytic properties at 500 °C (k*, D*, k_chem, D_chem, ASR), the average cross‑validation MAE for the random forest model (MAE_ML), the average cross‑validation MAE for the O p‑band center linear regression model (MAE_O_pband), and the computed percentage reduction in MAE (percent_reduction). The values must be derived from 25 repeats of 5‑fold cross‑validation on the full public dataset. The CSV must have exactly the columns `property`, `MAE_ML`, `MAE_O_pband`, `percent_reduction`.

## Assets

- Perovskite catalytic properties database (Jacobs et al., 2023): https://arxiv.org/abs/2310.17744
- MAST-ML (MAterials Simulation Toolkit for Machine Learning): https://github.com/uw-cmg/MAST-ML

## Workflow steps

### Step 1: Load and preprocess perovskite database
- Role: process
- Action: Load the Jacobs et al. perovskite database and extract compositions, target property values (k*, D*, k_chem, D_chem, ASR) at 500°C, DFT-calculated O p-band center values, and electrolyte types. Preprocess into a structured tabular format ready for feature generation.
- Evidence: `/app/outputs/preprocessed_data.csv`

### Step 2: Generate elemental features
- Role: process
- Action: Using MAST-ML's ElementalFeatureGenerator, compute composition-based elemental features (composition-weighted averages, maxima, minima, differences, and categorical encodings of tabulated elemental properties) for every perovskite composition.
- Evidence: `/app/outputs/elemental_features.csv`

### Step 3: Train random forest models with elemental features
- Role: process
- Action: For each target property at 500°C (k*, D*, k_chem, D_chem, ASR), train a random forest regressor using the elemental features generated in the previous step. For ASR, additionally include one-hot encoding of electrolyte type.
- Evidence: `/app/outputs/rf_models.pkl`

### Step 4: Train O p-band center linear regression models
- Role: process
- Action: For each target property at 500°C, train a univariate linear regression model using the DFT-calculated O p-band center as the sole feature.
- Evidence: `/app/outputs/lr_models.pkl`

### Step 5: Cross-validate and compute MAE and percentage reduction
- Role: scored (load-bearing)
- Action: Using the trained random forest and linear regression models, perform 25 repeats of 5-fold cross-validation on the dataset for each catalytic property at 500°C. For each split compute the MAE. Average over all splits to obtain the mean MAE for the random forest (MAE_ML) and for the linear model (MAE_O_pband). Compute the percentage reduction as 100 * (MAE_ML - MAE_O_pband) / MAE_O_pband. Write a CSV file with columns: property, MAE_ML, MAE_O_pband, percent_reduction.
- Output file: `/app/outputs/comparison_results.csv`
- Format: csv
- Contract: Columns: property (string: one of k*, D*, k_chem, D_chem, ASR), MAE_ML (float), MAE_O_pband (float), percent_reduction (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/comparison_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### comparison_results.csv
- path: `/app/outputs/comparison_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the average MAE values from 25×5-fold cross-validation and the computed percentage reduction when using elemental-feature random forest relative to O p-band center linear regression, for each of five catalytic properties at 500°C.
- schema:
  - `type`: table
  - `required_columns`: `property`, `MAE_ML`, `MAE_O_pband`, `percent_reduction`
  - `units`: object

Notes: The checker will recompute percent_reduction from the provided MAE values as a consistency check and then compare each percent_reduction against hidden gold values with a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "comparison_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "MAE_ML",
          "MAE_O_pband",
          "percent_reduction"
        ],
        "units": {}
      },
      "description": "CSV containing the average MAE values from 25×5-fold cross-validation and the computed percentage reduction when using elemental-feature random forest relative to O p-band center linear regression, for each of five catalytic properties at 500°C."
    }
  ],
  "notes": "The checker will recompute percent_reduction from the provided MAE values as a consistency check and then compare each percent_reduction against hidden gold values with a tolerance."
}
```

## How you are scored
A hidden verifier program reads your `comparison_results.csv`. It first recomputes the `percent_reduction` from the `MAE_ML` and `MAE_O_pband` columns to check internal consistency. It then compares each property’s `percent_reduction` against a hidden gold standard based on the paper’s reported values, using an absolute tolerance. Full credit (score = 1.0) is awarded if all five properties are within tolerance; fractional credit is proportional to the number of properties within tolerance. Reporting the correct numbers is not enough—the verifier also checks the internal consistency of the reported MAE values.
