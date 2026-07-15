# Random Forest Prediction of Local Properties from XANES Spectra using Multiscale Polynomial Featurization

## Problem background
X-ray absorption near-edge structure (XANES) spectra encode rich information about the local atomic and electronic structure of materials, but extracting quantitative structural properties directly from spectra is challenging. Heuristic rules exist for a few elements and properties, but they often fail for many compounds. This work explores whether machine learning models can learn to predict three local properties of the absorbing atom — coordination number, mean nearest-neighbor distance, and Bader charge — from a XANES spectrum alone, using a large public dataset of computed spectra covering eight 3d transition metals. The goal is to develop models that are accurate yet interpretable, enabling the identification of which spectral regions and features drive the predictions.

## Approach
A dataset of post-edge-normalized XANES spectra on a 100-point energy grid is used, covering the metals Ti, V, Cr, Mn, Fe, Co, Ni, Cu. Each spectrum has ground-truth labels for coordination number (discrete: 4, 5, or 6), mean nearest-neighbor distance (Å), and Bader charge (e). Two types of featurization are introduced: pointwise (raw 100-point vector) and a novel multiscale polynomial featurization. The polynomial approach partitions the energy range into 4, 5, 10, and 20 equally sized segments, fits a cubic polynomial a0 + a1*x + a2*x² + a3*x³ (with x centred at the segment midpoint) in each segment, and collects the 156 coefficients plus the white-line energy (Argmax of the spectrum) to form a 157-dimensional feature vector. For each metal separately, random forest models are trained for classification (coordination) and regression (distance, charge). Training uses an 80/10/10 random train/validation/test split; for coordination, random oversampling of minority classes is applied to combat class imbalance. The entire train/test cycle is repeated 10 times with different random seeds, and ensemble predictions are produced (majority vote for classification, arithmetic mean for regression). Model performance is evaluated on the held-out test set, reporting accuracy and per-class F1 (coordination), and R² and MAE (distance, charge). All code, data, and the featurization logic are publicly available, allowing a full re-implementation.

## Reproduction target
Download the provided dataset from the public repository, implement the multiscale polynomial featurization, train the random forest models for all eight metals and three properties, and output the full set of test-set predictions and computed performance metrics. Specifically, produce CSV files containing for each metal the true and predicted values for coordination, distance, and charge for every test spectrum, and a JSON file that summarizes per-metal metrics (accuracy, F1, R², MAE) averaged over the 10 repeats. The resulting artifacts should correspond to the main model-evaluation results reported in the published study, to be verified by a hidden scoring procedure.

## Assets

- Pointwise XANES spectra and labels for 8 transition metals: https://data.matr.io
- scikit-learn: scikit-learn
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Acquire the XANES dataset
- Role: process
- Action: Download the post‑edge‑normalized XANES spectra (100 uniformly spaced energy grid) and the associated labels (coordination number, mean nearest‑neighbor distance, Bader charge) for eight 3d transition metals (Ti, V, Cr, Mn, Fe, Co, Ni, Cu) from the public TRI data-sharing site (https://data.matr.io). Parse the files into structured arrays suitable for featurization.
- Evidence: `/app/outputs/data_prep.log`

### Step 2: Generate multiscale polynomial features
- Role: process
- Action: For each spectrum, implement the multiscale polynomial featurization: partition the 100‑point energy range into N=4,5,10,20 equally sized contiguous partitions; within each partition, fit a cubic polynomial a0 + a1*x + a2*x² + a3*x³ with x centered at the partition midpoint; collect all 156 coefficients and append the white‑line energy (Argmax of the spectrum) to form a 157‑dimensional feature vector.
- Evidence: `/app/outputs/features.log`

### Step 3: Train random forest models
- Role: process
- Action: For each metal separately, using the polynomial features and corresponding labels, train a random forest classifier for coordination number and random forest regressors for mean nearest‑neighbor distance and Bader charge. Use an 80/10/10 random train/validation/test split, with random oversampling of minority classes for coordination. Repeat the entire train/test cycle 10 times with different random seeds. Save the trained models (optional).
- Evidence: `/app/outputs/training_summary.log`

### Step 4: Output coordination predictions
- Role: scored (load-bearing)
- Action: For each metal, using the trained ensemble models (10 repeats), generate test‑set predictions for coordination number via majority vote. Write a CSV file with columns metal, spectrum_index, true_coordination, predicted_coordination, covering all test spectra across all metals.
- Output file: `/app/outputs/predictions_coordination.csv`
- Format: csv
- Contract: metal,spectrum_index,true_coordination,predicted_coordination
- Scoring: scored by hidden verifier

### Step 5: Output distance predictions
- Role: scored
- Action: For each metal, using the trained ensemble regressors, generate test‑set predictions for mean nearest‑neighbor distance via arithmetic mean. Write a CSV file with columns metal, spectrum_index, true_distance, predicted_distance.
- Output file: `/app/outputs/predictions_distance.csv`
- Format: csv
- Contract: metal,spectrum_index,true_distance,predicted_distance
- Scoring: scored by hidden verifier

### Step 6: Output Bader charge predictions
- Role: scored
- Action: For each metal, using the trained ensemble regressors, generate test‑set predictions for Bader charge via arithmetic mean. Write a CSV file with columns metal, spectrum_index, true_charge, predicted_charge.
- Output file: `/app/outputs/predictions_charge.csv`
- Format: csv
- Contract: metal,spectrum_index,true_charge,predicted_charge
- Scoring: scored by hidden verifier

### Step 7: Compute and record performance metrics
- Role: scored
- Action: From the test‑set predictions, compute accuracy and per‑class F1 for coordination, and R² and MAE for distance and charge, for each metal. Output the results in a structured JSON file.
- Output file: `/app/outputs/metrics.json`
- Format: json
- Contract: {
  "coordination": {
    "Ti": {"accuracy": float, "f1_4": float, "f1_5": float, "f1_6": float},
    ... (all 8 metals)
  },
  "distance": {
    "Ti": {"R2": float, "MAE": float},
    ... (all 8 metals)
  },
  "charge": {
    "Ti": {"R2": float, "MAE": float},
    ... (all 8 metals)
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions_coordination.csv`
- `/app/outputs/predictions_distance.csv`
- `/app/outputs/predictions_charge.csv`
- `/app/outputs/metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions_coordination.csv
- path: `/app/outputs/predictions_coordination.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: File must contain the test‑set true and predicted coordination numbers for every metal. The checker recomputes accuracy and F1 scores from these predictions and compares to paper‑reported gold values.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `spectrum_index`, `true_coordination`, `predicted_coordination`
  - `units`: object

### predictions_distance.csv
- path: `/app/outputs/predictions_distance.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: File must contain the test‑set true and predicted mean nearest‑neighbor distances for every metal. The checker recomputes R² and MAE (in Å) and compares to paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `spectrum_index`, `true_distance`, `predicted_distance`
  - `units`:
    - `true_distance`: Å
    - `predicted_distance`: Å

### predictions_charge.csv
- path: `/app/outputs/predictions_charge.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: File must contain the test‑set true and predicted Bader charges for every metal. The checker recomputes R² and MAE (in elementary charge) and compares to paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `spectrum_index`, `true_charge`, `predicted_charge`
  - `units`:
    - `true_charge`: e
    - `predicted_charge`: e

### metrics.json
- path: `/app/outputs/metrics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent‑reported metrics computed from the test‑set predictions. The checker verifies consistency with the metrics recomputed from the prediction CSV files (difference < 0.01).
- schema:
  - `type`: object
  - `required`: `coordination`, `distance`, `charge`
  - `items`:
    - `coordination`:
      - `type`: object
      - `description`: per‑metal classification metrics; each metal object must contain accuracy, f1_4, f1_5, f1_6 (all floats)
    - `distance`:
      - `type`: object
      - `description`: per‑metal regression metrics; each metal object must contain R2, MAE (floats)
    - `charge`:
      - `type`: object
      - `description`: per‑metal regression metrics; each metal object must contain R2, MAE (floats)

Notes: The task reproduces only the multiscale polynomial featurization branch of the paper. The raw prediction CSV files are scored by recomputing the headline metrics against hidden true labels; the metrics.json serves as a consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions_coordination.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "spectrum_index",
          "true_coordination",
          "predicted_coordination"
        ],
        "units": {}
      },
      "description": "File must contain the test‑set true and predicted coordination numbers for every metal. The checker recomputes accuracy and F1 scores from these predictions and compares to paper‑reported gold values."
    },
    {
      "file": "predictions_distance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "spectrum_index",
          "true_distance",
          "predicted_distance"
        ],
        "units": {
          "true_distance": "Å",
          "predicted_distance": "Å"
        }
      },
      "description": "File must contain the test‑set true and predicted mean nearest‑neighbor distances for every metal. The checker recomputes R² and MAE (in Å) and compares to paper‑reported values."
    },
    {
      "file": "predictions_charge.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "spectrum_index",
          "true_charge",
          "predicted_charge"
        ],
        "units": {
          "true_charge": "e",
          "predicted_charge": "e"
        }
      },
      "description": "File must contain the test‑set true and predicted Bader charges for every metal. The checker recomputes R² and MAE (in elementary charge) and compares to paper‑reported values."
    },
    {
      "file": "metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "coordination",
          "distance",
          "charge"
        ],
        "items": {
          "coordination": {
            "type": "object",
            "description": "per‑metal classification metrics; each metal object must contain accuracy, f1_4, f1_5, f1_6 (all floats)"
          },
          "distance": {
            "type": "object",
            "description": "per‑metal regression metrics; each metal object must contain R2, MAE (floats)"
          },
          "charge": {
            "type": "object",
            "description": "per‑metal regression metrics; each metal object must contain R2, MAE (floats)"
          }
        }
      },
      "description": "Agent‑reported metrics computed from the test‑set predictions. The checker verifies consistency with the metrics recomputed from the prediction CSV files (difference < 0.01)."
    }
  ],
  "notes": "The task reproduces only the multiscale polynomial featurization branch of the paper. The raw prediction CSV files are scored by recomputing the headline metrics against hidden true labels; the metrics.json serves as a consistency check."
}
```

## How you are scored
A hidden automated verifier scores each required output artifact independently. The verifier will recompute the performance metrics (accuracy, F1, R², MAE) directly from your raw prediction CSV files and compare them to hidden reference values. It will also check that the metrics.json file is consistent with those recomputed values. No metric thresholds or target numbers are provided in advance; you must faithfully execute the workflow steps and produce correct artifacts to obtain a high score. Each scored stage contributes a weight to the final reward, and the total reward is in the range [0,1].
