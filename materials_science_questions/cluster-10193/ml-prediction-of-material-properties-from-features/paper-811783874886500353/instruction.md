# Prediction of Zeolite Framework Crystal Structures from XRD Peaks via GRNN and RBF

## Problem background
Zeolites are microporous crystalline aluminosilicates with widespread industrial use. Identifying the crystal structure of an unknown zeolite from X-ray diffraction (XRD) data is a challenging task that usually involves complex crystallographic analysis. A fast, simple alternative would be to directly relate a small set of XRD peak angles to key structural properties using statistical or machine-learning methods. This work investigates whether artificial neural networks can predict the minimum pore dimension (r1), maximum pore dimension (r2), framework density (fd), and the unit-cell edge lengths (a, b, c) of a zeolite solely from the 2θ angles of its eight highest-intensity XRD peaks. The goal is to quantify the prediction accuracy in terms of average relative error for each method and each target.

## Approach
Two neural network architectures are employed: Generalized Regression Neural Networks (GRNN) and Radial Basis Function (RBF) networks. The RBF network uses a fixed hidden layer of 15 Gaussian neurons. A dataset of 131 zeolites is compiled from publicly available crystal structure databases and simulated XRD patterns. For each zeolite, the eight most intense 2θ peak angles form the input vector, and the six structural parameters (r1, r2, fd, a, b, c) are the corresponding target values. All input features and each output variable are normalized independently to the range [0,1]. Model evaluation is carried out via fivefold cross-validation with fixed splits. For each method and each target, the spread (σ) parameter is optimized: within each fold, σ is swept over a range of values and the value minimizing the test-fold relative error is selected; these optimal spreads are then averaged across folds. The cross-validation predictions are re-run using this averaged spread, and the overall average relative error d_m (in %) is computed across all test examples. The procedure is repeated for all six targets, yielding 12 d_m values.

## Reproduction target
Produce a CSV file `results/performance.csv` containing the average relative errors d_m (in %) for GRNN and RBF predictions of all six structural targets (r1, r2, fd, a, b, c). The table must have exactly 12 rows, each with the columns `method` (one of 'GRNN' or 'RBF'), `target` (one of 'r1', 'r2', 'fd', 'a', 'b', 'c'), and `d_m` (a floating point number representing the percentage error). The d_m values must be obtained by strictly following the fivefold cross-validation and spread-optimization protocol described in the workflow steps, using the dataset that you assemble from the public zeolite resources.

## Assets

- Zeolite structure and XRD data (IZA-SC database / Atlas of Zeolite Framework Types / Collection of Simulated XRD Powder Patterns): http://www.iza-structure.org/databases/

## Workflow steps

### Step 1: Acquire and prepare zeolite dataset
- Role: process
- Action: Obtain crystal structures and corresponding XRD patterns for 131 zeolites from the public IZA-SC database or the literature atlases (Treacy & Higgins 2001, Baerlocher et al. 2001). For each zeolite, extract the 2θ angles of the eight highest-intensity XRD peaks, and collect ground-truth structural parameters: minimum pore dimension r1, maximum pore dimension r2, framework density fd, and unit-cell edge lengths a, b, c. Assemble a CSV dataset with columns: sample_id, peak1, ..., peak8, r1, r2, fd, a, b, c.
- Evidence: `/app/outputs/raw_dataset.csv`

### Step 2: Normalize data and create cross-validation splits
- Role: process
- Action: Normalize all input features (eight peak angles) and each target variable separately to the range [0,1] using linear min-max scaling. Partition the 131 examples into five fixed disjoint subsets: four subsets of 26 examples and one subset of 27 examples. Save the normalized dataset and the fixed fivefold partition indices for reproducibility.
- Evidence: `/app/outputs/splits.json`

### Step 3: Train GRNN and RBF models and compute average relative errors
- Role: scored (load-bearing)
- Action: Implement GRNN (General Regression Neural Network) and RBF (Radial Basis Function network with 15 hidden neurons) regression models. For each method and each of the six targets (r1, r2, fd, a, b, c) perform fivefold cross-validation using the fixed splits: within each fold, sweep the spread parameter σ over a grid of values, record the spread minimizing test-set relative error; average the optimal spreads across folds; re-run the fivefold predictions with this averaged spread; compute the average relative error d_m (%) across all test samples. Report the 12 d_m values as a CSV table.
- Output file: `/app/outputs/performance.csv`
- Format: csv
- Contract: CSV with three columns: method (string, one of 'GRNN' or 'RBF'), target (string, one of 'r1', 'r2', 'fd', 'a', 'b', 'c'), d_m (float, percentage). Exactly 12 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/performance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### performance.csv
- path: `/app/outputs/performance.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Table of average relative errors (d_m in %) for GRNN and RBF predictions of six zeolite structural parameters from XRD peak angles.
- schema:
  - `type`: table
  - `required_columns`: `method`, `target`, `d_m`
  - `units`:
    - `d_m`: percent

Notes: Only the d_m values for GRNN and RBF are scored. Multilinear regression baseline and halved-training-data analysis are excluded per scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results/performance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "target",
          "d_m"
        ],
        "units": {
          "d_m": "percent"
        }
      },
      "description": "Table of average relative errors (d_m in %) for GRNN and RBF predictions of six zeolite structural parameters from XRD peak angles."
    }
  ],
  "notes": "Only the d_m values for GRNN and RBF are scored. Multilinear regression baseline and halved-training-data analysis are excluded per scope."
}
```

## How you are scored
A hidden verifier will read your `results/performance.csv` and compare each of the 12 reported d_m values against the corresponding reference values from the original study. The comparison uses a threshold‑or‑better policy: for each method–target pair, if your reported average relative error is less than or equal to the reference value plus a small fixed tolerance, you receive full credit for that entry; otherwise, you receive zero credit. The final reward is the fraction of the 12 entries that pass. The verifier does not re‑run your training pipeline; it scores only the final d_m values you report. Do not attempt to guess or look up the reference values—they are hidden. Your job is to faithfully implement the data preparation and modelling workflow, produce a correct `results/performance.csv`, and let the verifier judge the outcome.
