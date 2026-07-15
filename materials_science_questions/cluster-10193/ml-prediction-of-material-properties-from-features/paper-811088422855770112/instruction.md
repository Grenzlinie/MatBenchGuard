# Band gap screening for solar cell materials using partitioned machine learning models

## Problem background
Designing efficient materials for photovoltaics often requires identifying compounds whose electronic band gap falls within a specific energy window (approximately 0.9–1.7 eV for single-junction solar cells). Large databases of density functional theory (DFT) calculations now contain band gaps for tens of thousands of crystalline compounds, making it possible to train machine learning models that can rapidly screen compositions for this property. The challenge is to build models that accurately predict whether an unseen compound's true band gap lies inside the target range, even when the model is only trained on composition-based descriptors and limited training examples.

## Approach
We employ a general-purpose machine learning framework based on 145 composition-derived attributes (stoichiometric features, elemental property statistics, electronic structure fractions, and ionic compound indicators). These attributes are computed using the Magpie library (or its successor matminer). Two modelling strategies are compared:

1. **Single global model** – A Random Subspace ensemble of reduced-error pruning decision trees (or an equivalent decision tree ensemble) is trained on 90% of the available data to regress the DFT band gap directly. For each compound in the held-out 10%, the model's prediction is used to estimate the likelihood that the true band gap lies in the target window, and the 30 most likely candidates are selected.

2. **Hierarchical partitioned model** – The training data is first classified by a coarse band gap interval predictor (e.g., 0–1.5 eV vs. >1.5 eV). Each interval is then subdivided according to whether the compound contains a halogen, a chalcogen, or a pnictogen element. Within each resulting chemical subgroup, a separate Random Subspace + REPTree regression model is trained. Test compounds are routed through the interval classifier and the appropriate subgroup model to obtain a band gap prediction, and the top 30 candidates for the target window are selected analogously.

The relative performance of the two strategies is assessed on the same random 90/10 split of the OQMD entries that are also listed in the Inorganic Crystal Structure Database (ICSD).

## Reproduction target
The goal is to reproduce the simulated solar cell material screening experiment using the OQMD-ICSD subset (≈25,085 compounds). Split the dataset randomly into 90% training and 10% test. Compute the 145 compositional attributes for every compound. Train both the single global model and the hierarchical partitioned model (with the interval classifier and chemical-group splitting) on the training portion. For each model, use the corresponding predictions on the test portion to identify the 30 compounds that are most likely to have a true DFT band gap between 0.9 and 1.7 eV. Record the selected compositions, their predicted band gaps, and their actual DFT-calculated band gaps in the specified CSV files. The scored metric is the fraction of those 30 compounds whose actual band gap lies inside the target window. The checker will assess the relative performance of the two models.

## Assets

- Open Quantum Materials Database (OQMD): http://oqmd.org
- Magpie / matminer library: https://github.com/hackingmaterials/matminer
- Weka machine learning library (or scikit-learn equivalent): https://www.cs.waikato.ac.nz/ml/weka/

## Workflow steps

### Step 1: Acquire OQMD-ICSD band gap dataset
- Role: process
- Action: Obtain the OQMD database and filter to the ~25,085 compound entries that are also present in the ICSD. Extract the composition and DFT-computed band gap energy for each compound.
- Evidence: `/app/outputs/dataset_info.json`

### Step 2: Compute compositional attributes
- Role: process
- Action: For each of the 25,085 compositions, compute the set of 145 compositional attributes using the Magpie (or matminer) library.
- Evidence: `/app/outputs/features.npy`

### Step 3: Train single global regression model
- Role: process
- Action: Split the dataset randomly into 90% training and 10% test sets. Train a Random Subspace + REPTree (or equivalent decision tree ensemble) regression model on the training portion to predict the band gap energy from the computed attributes.
- Evidence: `/app/outputs/global_model.txt`

### Step 4: Select top-30 solar cell candidates using single global model
- Role: scored (load-bearing)
- Action: For each compound in the withheld 10% test set, use the single global model to predict the band gap. Select the 30 compounds with the highest predicted probability of having a band gap in the solar-cell-relevant range 0.9–1.7 eV. Save the selected compositions, their predicted band gaps, and their actual DFT-calculated band gaps.
- Output file: `/app/outputs/single_model_top30.csv`
- Format: csv
- Contract: Columns: composition (string, chemical formula), predicted_band_gap (float, eV), actual_band_gap (float, eV). Exactly 30 rows.
- Scoring: scored by hidden verifier

### Step 5: Train hierarchical partitioned model
- Role: process
- Action: On the same 90% training split, first train a classifier to predict the band gap interval (e.g., 0–1.5 eV, >1.5 eV). Partition the training data by the predicted interval and then by the presence of halogen, chalcogen, or pnictogen elements. Within each resulting chemical subgroup, train a separate Random Subspace + REPTree regression model.
- Evidence: `/app/outputs/partitioned_model_structure.txt`

### Step 6: Select top-30 solar cell candidates using partitioned model
- Role: scored (load-bearing)
- Action: For each compound in the withheld 10% test set, use the hierarchical partitioned model to predict the band gap (route the compound through the interval classifier and the appropriate chemical subgroup model). Select the 30 compounds with the highest predicted probability of being in the 0.9–1.7 eV range. Save the selected compositions, predicted band gaps, and actual band gaps.
- Output file: `/app/outputs/partitioned_model_top30.csv`
- Format: csv
- Contract: Columns: composition (string, chemical formula), predicted_band_gap (float, eV), actual_band_gap (float, eV). Exactly 30 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_model_top30.csv`
- `/app/outputs/partitioned_model_top30.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_model_top30.csv
- path: `/app/outputs/single_model_top30.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Selected candidates from the single global model. The verifier recomputes the fraction of rows where actual_band_gap is between 0.9 and 1.7 eV and compares it against a hidden threshold.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `predicted_band_gap`, `actual_band_gap`
  - `units`:
    - `predicted_band_gap`: eV
    - `actual_band_gap`: eV
  - `row_count`: 30

### partitioned_model_top30.csv
- path: `/app/outputs/partitioned_model_top30.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Selected candidates from the hierarchical partitioned model. The verifier recomputes the fraction of rows where actual_band_gap is between 0.9 and 1.7 eV and compares it against a hidden threshold.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `predicted_band_gap`, `actual_band_gap`
  - `units`:
    - `predicted_band_gap`: eV
    - `actual_band_gap`: eV
  - `row_count`: 30

Notes: The checker independently counts compounds with actual band gap in the target range (0.9–1.7 eV) for each output file and scores the success rates against the paper's reported performance thresholds using a threshold_or_better policy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_model_top30.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "predicted_band_gap",
          "actual_band_gap"
        ],
        "units": {
          "predicted_band_gap": "eV",
          "actual_band_gap": "eV"
        },
        "row_count": 30
      },
      "description": "Selected candidates from the single global model. The verifier recomputes the fraction of rows where actual_band_gap is between 0.9 and 1.7 eV and compares it against a hidden threshold."
    },
    {
      "file": "partitioned_model_top30.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "predicted_band_gap",
          "actual_band_gap"
        ],
        "units": {
          "predicted_band_gap": "eV",
          "actual_band_gap": "eV"
        },
        "row_count": 30
      },
      "description": "Selected candidates from the hierarchical partitioned model. The verifier recomputes the fraction of rows where actual_band_gap is between 0.9 and 1.7 eV and compares it against a hidden threshold."
    }
  ],
  "notes": "The checker independently counts compounds with actual band gap in the target range (0.9–1.7 eV) for each output file and scores the success rates against the paper's reported performance thresholds using a threshold_or_better policy."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted artifacts. For each scored output file (`single_model_top30.csv` and `partitioned_model_top30.csv`), the checker computes the fraction of selected compounds whose actual band gap falls in the 0.9–1.7 eV range. This fraction is compared against hidden reference thresholds (derived from the literature) using a threshold‑or‑better policy: meeting or exceeding the expected rate earns full credit for that artifact, while lower rates receive proportionally less credit. The two success fractions are also compared to confirm that the partitioned model outperforms the single model. The final reward is a weighted combination of the scores from these checks. Process steps are not directly scored, but the verifier may inspect their evidence files to confirm that the required workflow was executed.
