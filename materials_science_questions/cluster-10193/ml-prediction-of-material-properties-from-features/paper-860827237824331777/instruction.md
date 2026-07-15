# Discover Superconductors with Deep Set Networks Using Elemental Composition

## Problem background
Superconductivity is a rare material property whose discovery has traditionally relied on intuition and trial-and-error. Machine learning offers a path to accelerate this search by predicting candidate superconductors directly from chemical composition, but conventional models are sensitive to the arbitrary ordering of elements in a chemical formula. This work introduces a permutation-invariant neural network architecture that accepts the unordered set of elements in a compound as input, avoiding ordering bias and enabling both classification (superconductor or not) and regression (prediction of the superconducting critical temperature, Tc). Evaluating such a model on an independently curated database of pre‑selected materials provides a stringent test of its ability to generalise beyond its training set and to identify genuinely novel superconducting candidates.

## Approach
A DeepSet neural network is trained to map a material’s elemental composition to a superconducting property. Each distinct element in a compound is represented by a 22‑dimensional vector of elemental properties (e.g., atomic number, electronegativity, covalent radius, thermal conductivity) drawn from the Mendeleev package, together with its stoichiometric integer. These per‑element vectors are transformed by a shared feedforward network (φ) into a latent space, summed across all elements, and passed through a second feedforward network (ρ) to produce a final output.

For regression, the output is a predicted Tc, and the network is trained on the SuperCon database of known superconductors using random 80/20 splits. For classification, the training set is augmented with a large number of non‑superconducting compounds from the Crystallography Open Database (COD) via a “garbage‑in” procedure; the output is a scalar score between 0 and 1, and a compound is labelled superconducting when this score exceeds a fixed decision threshold with majority voting across an ensemble of independently trained models.

The trained models are evaluated on the Hosono database, a collection of 207 materials pre‑selected by domain experts, which was never seen during training. The classifier is also applied to the September 2021 list of minerals published by the International Mineralogical Association (IMA) to screen for previously unrecognised superconducting candidates.

## Reproduction target
Train a DeepSet model for both regression and classification following the pipeline above. Then produce three scored artifacts:

1. A CSV file with the predicted critical temperatures for every material in the Hosono database: for each compound, report the measured Tc, the mean and the standard deviation of the predicted Tc across an ensemble of regression models.
2. A CSV file with the classification results on the same Hosono database: for each compound, report its true label (superconductor or not), the mean raw score across an ensemble of classifiers, and the final binary classification obtained by majority voting at the designated threshold.
3. A CSV file listing all IMA minerals that the ensemble of classifiers labels as superconducting, with their predicted scores and classification labels.

The hidden verifier will recompute the root‑mean‑square error (RMSE) of the Tc predictions and the precision and recall of the classification on the Hosono database, and check that the mineral candidate list contains the expected key compounds. Reproducing the main quantitative performance and the mineral candidate list is the primary goal.

## Assets

- SuperCon database: https://mdr.nims.go.jp/collections/5712mb227
- Crystallography Open Database (COD): https://www.crystallography.net/cod/
- Hosono database (from Konno et al.): https://github.com/tomo835g/Deep-Learning-to-find-Superconductors
- IMA mineral list (September 2021): https://www.ima-mineralogy.org/minlist.htm
- Mendeleev Python package: mendeleev
- DeepSet implementation code: https://github.com/ClaudioPereti/From_individual_elements_to_macroscopic_materials

## Workflow steps

### Step 1: Data preparation and featurization
- Role: process
- Action: Download the SuperCon dataset, COD, Hosono database, and the September 2021 IMA mineral list. For every compound, extract from each distinct element 22 properties using Mendeleev plus the stoichiometric integer, forming the input sets for regression and classification.
- Evidence: none

### Step 2: Train regression DeepSet models
- Role: process
- Action: Train 50 independent DeepSet regression models on random 80/20 splits of the SuperCon dataset. Use latent dimension d=300 and the paper’s architecture (7‑layer φ, 13‑layer ρ, ReLU activations).
- Evidence: none

### Step 3: Evaluate regression on Hosono database
- Role: scored
- Action: Apply the 50 trained regression models to every material in the Hosono database. Compute the mean and standard deviation of predicted critical temperature Tc across models and output the results.
- Output file: `/app/outputs/regression_predictions.csv`
- Format: csv
- Contract: Columns: material_name (string), measured_Tc (float, K), predicted_Tc_mean (float, K), predicted_Tc_std (float, K). One row per Hosono material.
- Scoring: scored by hidden verifier

### Step 4: Train classification DeepSet models
- Role: process
- Action: Train 60 independent DeepSet classifiers using the SuperCon dataset (superconductors) augmented with 50,000 random entries from COD (non‑superconductors). Use d=300 latent dimension and the paper’s architecture (4‑layer φ, 3‑layer ρ + sigmoid output).
- Evidence: none

### Step 5: Evaluate classification on Hosono database (majority rule)
- Role: scored
- Action: For each material in the Hosono database, collect raw scores from all 60 trained classifiers. Compute the mean score and, using a threshold of 0.85 and majority voting across runs, assign a final binary prediction (1 = superconductor, 0 = non‑superconductor). Output the true label and predictions.
- Output file: `/app/outputs/classification_results.csv`
- Format: csv
- Contract: Columns: material_name (string), true_label (int, 1 for superconductor, 0 otherwise), predicted_score (float, mean raw score across models), predicted_class (int, 1 if majority vote passes threshold 0.85 else 0). One row per Hosono material.
- Scoring: scored by hidden verifier

### Step 6: Apply classifier to IMA mineral list
- Role: scored (load-bearing)
- Action: Featurize the IMA mineral list (September 2021) and apply the trained classifiers with the same majority rule (threshold 0.85). Output all minerals classified as superconducting, including the predicted score and classification label.
- Output file: `/app/outputs/ima_classified_candidates.csv`
- Format: csv
- Contract: Columns: mineral_name (string), formula (string), predicted_score (float, mean score across models), classification (string, 'SC' if predicted_class is 1 else 'non-SC'). One row per mineral that is classified as superconducting.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/regression_predictions.csv`
- `/app/outputs/classification_results.csv`
- `/app/outputs/ima_classified_candidates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### regression_predictions.csv
- path: `/app/outputs/regression_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw predictions for the Hosono database. The checker will recompute RMSE between measured_Tc and predicted_Tc_mean and compare to a hidden gold tolerance.
- schema:
  - `type`: table
  - `required_columns`: `material_name`, `measured_Tc`, `predicted_Tc_mean`, `predicted_Tc_std`
  - `units`:
    - `measured_Tc`: K
    - `predicted_Tc_mean`: K
    - `predicted_Tc_std`: K

### classification_results.csv
- path: `/app/outputs/classification_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Classification output for the Hosono database. The checker will recompute precision and recall from true_label vs predicted_class and compare to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `material_name`, `true_label`, `predicted_score`, `predicted_class`

### ima_classified_candidates.csv
- path: `/app/outputs/ima_classified_candidates.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: List of IMA minerals predicted to be superconductors. The checker verifies that key candidates (e.g., Pd3HgTe3, PdBiTe, Pd2NiTe2) appear among the entries.
- schema:
  - `type`: table
  - `required_columns`: `mineral_name`, `formula`, `predicted_score`, `classification`

Notes: All metrics are recomputed from the raw predictions; no self-reported summary is scored. The IMA list step is load-bearing because it requires genuine training of classification models.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "regression_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material_name",
          "measured_Tc",
          "predicted_Tc_mean",
          "predicted_Tc_std"
        ],
        "units": {
          "measured_Tc": "K",
          "predicted_Tc_mean": "K",
          "predicted_Tc_std": "K"
        }
      },
      "description": "Raw predictions for the Hosono database. The checker will recompute RMSE between measured_Tc and predicted_Tc_mean and compare to a hidden gold tolerance."
    },
    {
      "file": "classification_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material_name",
          "true_label",
          "predicted_score",
          "predicted_class"
        ]
      },
      "description": "Classification output for the Hosono database. The checker will recompute precision and recall from true_label vs predicted_class and compare to hidden gold values."
    },
    {
      "file": "ima_classified_candidates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "mineral_name",
          "formula",
          "predicted_score",
          "classification"
        ]
      },
      "description": "List of IMA minerals predicted to be superconductors. The checker verifies that key candidates (e.g., Pd3HgTe3, PdBiTe, Pd2NiTe2) appear among the entries."
    }
  ],
  "notes": "All metrics are recomputed from the raw predictions; no self-reported summary is scored. The IMA list step is load-bearing because it requires genuine training of classification models."
}
```

## How you are scored
A hidden verifier reads your three output CSV files independently. For regression, it computes the RMSE between your predicted mean Tc and the measured Tc across all Hosono materials; lower RMSE is better and meeting or surpassing a reference threshold earns full credit. For classification, it computes precision and recall from your predicted class against the true label using the specified threshold and majority rule; higher is better. For the IMA list, it checks that the file contains the expected candidate minerals among the superconducting entries. The three stages are weighted and combine into a single reward between 0 and 1. Simply reporting numbers from the literature without genuine training and inference will not pass, because the reference metrics and the expected IMA candidates are never disclosed to you. Only a correct execution of the prescribed workflow can produce the right raw artifacts that satisfy the hidden checks.
