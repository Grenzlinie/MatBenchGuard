# Multimodal Material Property Prediction with Cross-Attention Fusion

## Problem background
Predicting material properties directly from crystal structure is a central challenge in computational materials science, with the potential to greatly accelerate the discovery and design of new functional materials. Graph neural networks (GNNs) have emerged as powerful tools for this task by representing the crystal as a graph and capturing local bonding patterns. However, converting a crystal structure into a graph necessarily discards important global and semi-global information such as the crystal system, symmetry, and the connectivity of repeating structural units. This lost information can be critical for determining certain properties. To recover such missing information, recent work has begun to incorporate natural‑language descriptions of the crystal, generated automatically from the structure, as a second modality. The task is to build a multimodal fusion model that combines the graph representation of a crystal with its textual description to improve prediction accuracy over unimodal models or simpler fusion approaches, evaluated on several important material properties.

## Approach
We implement **CAST**, a cross‑attention‑based multimodal fusion model. The structure is encoded into node embeddings using the **coGN** graph neural network, and the automatically generated text description is encoded into token‑level embeddings using the **MatSciBERT** language model. The core of CAST is a stack of cross‑attention layers that allow every graph node to attend to every text token, fusing the two modalities at a fine‑grained level.

The model is trained in two stages. First, a **masked node prediction (MNP) pretraining** stage is performed on the total energy dataset. A large fraction of graph nodes are randomly masked, and the model must predict the original element type by integrating information from both the remaining nodes and the attended text tokens. This aligns the node and text embeddings and establishes cross‑modal correspondences. Second, the pretrained model is finetuned for each target property — total energy, bandgap, shear modulus, and bulk modulus — by replacing the classification head with a linear regression head and training on the corresponding property‑specific split. The shear and bulk moduli are trained in log‑space. For comparison, baseline unimodal models (coGN alone, MatSciBERT alone) and alternative multimodal fusion strategies (concatenation and contrastive‑learning‑based pretraining) are also evaluated under the same encoder and split regime.

## Reproduction target
Your goal is to reproduce the CAST pipeline and report its predictive performance. Using the Materials Project database, apply the filtering, split, and text‑generation protocol described in Step 1. Then perform masked node prediction pretraining on the total energy training set (Step 2), fine‑tune separate regressors for each of the four properties on their respective train/validation splits (Step 3), and finally generate per‑sample predictions on the held‑out test split for each property (Steps 4‑7). From those predictions, compute the mean absolute error (MAE) for each property and write a summary JSON (Step 8). The objective is to obtain low MAE values relative to the baselines, demonstrating the effectiveness of the CAST architecture and its pretraining strategy.

## Assets

- Materials Project database: https://materialsproject.org/
- Robocrystallographer: https://github.com/materialsproject/robocrystallographer
- coGN (Connectivity Optimized Nested Line Graph Network): https://github.com/aimat-lab/coGN
- MatSciBERT: https://huggingface.co/m3rg-iitd/matscibert

## Workflow steps

### Step 1: Multimodal data preparation
- Role: process
- Action: Download structure and property data from Materials Project, apply the paper's filtering criteria (MatBench filtering plus additional formation energy and modulus constraints), generate textual descriptions using Robocrystallographer, and create train/validation/test splits (80/10/10) by sorting sample IDs separately for each property. Tokenize the text with MatSciBERT tokenizer and construct graph objects for coGN.
- Evidence: none

### Step 2: CAST masked node prediction (MNP) pretraining
- Role: process
- Action: Implement the CAST architecture: coGN as structure encoder, MatSciBERT as text encoder, 4 cross‑attention layers with 8 heads and attention dimension 128. Randomly mask 50% of graph nodes on the total energy training set and train the model to predict the original element types via a classification linear layer, aligning node and text embeddings.
- Evidence: `/app/outputs/pretraining_log.txt`

### Step 3: Finetune CAST regressors for all properties
- Role: process
- Action: Starting from the pretrained CAST model, replace the classification head with a single linear regression head. For each of the four properties (total energy, bandgap, shear modulus, bulk modulus), finetune the model on the corresponding dataset split using the appropriate target values. Save the four finetuned models.
- Evidence: `/app/outputs/finetuning_log.txt`

### Step 4: Generate test predictions for total energy
- Role: scored (load-bearing)
- Action: Using the finetuned total energy regressor, run inference on the test split and produce a CSV file with columns sample_id, true_value, predicted_value.
- Output file: `/app/outputs/predictions_total_energy.csv`
- Format: csv
- Contract: columns: sample_id (str), true_value (float, eV), predicted_value (float, eV)
- Scoring: scored by hidden verifier

### Step 5: Generate test predictions for bandgap
- Role: scored
- Action: Using the finetuned bandgap regressor, run inference on the test split and produce a CSV file with columns sample_id, true_value, predicted_value.
- Output file: `/app/outputs/predictions_bandgap.csv`
- Format: csv
- Contract: columns: sample_id (str), true_value (float, eV), predicted_value (float, eV)
- Scoring: scored by hidden verifier

### Step 6: Generate test predictions for shear modulus
- Role: scored
- Action: Using the finetuned log(shear modulus) regressor, run inference on the test split and produce a CSV file with columns sample_id, true_value, predicted_value.
- Output file: `/app/outputs/predictions_shear_modulus.csv`
- Format: csv
- Contract: columns: sample_id (str), true_value (float, log(GPa)), predicted_value (float, log(GPa))
- Scoring: scored by hidden verifier

### Step 7: Generate test predictions for bulk modulus
- Role: scored
- Action: Using the finetuned log(bulk modulus) regressor, run inference on the test split and produce a CSV file with columns sample_id, true_value, predicted_value.
- Output file: `/app/outputs/predictions_bulk_modulus.csv`
- Format: csv
- Contract: columns: sample_id (str), true_value (float, log(GPa)), predicted_value (float, log(GPa))
- Scoring: scored by hidden verifier

### Step 8: Compute and report MAE summary
- Role: scored
- Action: From the predictions CSV files, compute the MAE for each property and write a JSON file containing the MAE values for all four properties.
- Output file: `/app/outputs/results_summary.json`
- Format: json
- Contract: {"total_energy_mae": float, "bandgap_mae": float, "shear_modulus_mae": float, "bulk_modulus_mae": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions_total_energy.csv`
- `/app/outputs/predictions_bandgap.csv`
- `/app/outputs/predictions_shear_modulus.csv`
- `/app/outputs/predictions_bulk_modulus.csv`
- `/app/outputs/results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions_total_energy.csv
- path: `/app/outputs/predictions_total_energy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑sample predictions on the total energy test set. MAE will be recomputed by the checker from this file.
- schema:
  - `required_columns`: `sample_id`, `true_value`, `predicted_value`
  - `units`:
    - `true_value`: eV
    - `predicted_value`: eV

### predictions_bandgap.csv
- path: `/app/outputs/predictions_bandgap.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑sample predictions on the bandgap test set. MAE will be recomputed by the checker from this file.
- schema:
  - `required_columns`: `sample_id`, `true_value`, `predicted_value`
  - `units`:
    - `true_value`: eV
    - `predicted_value`: eV

### predictions_shear_modulus.csv
- path: `/app/outputs/predictions_shear_modulus.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑sample predictions on the log(shear modulus) test set. MAE will be recomputed by the checker from this file.
- schema:
  - `required_columns`: `sample_id`, `true_value`, `predicted_value`
  - `units`:
    - `true_value`: log(GPa)
    - `predicted_value`: log(GPa)

### predictions_bulk_modulus.csv
- path: `/app/outputs/predictions_bulk_modulus.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑sample predictions on the log(bulk modulus) test set. MAE will be recomputed by the checker from this file.
- schema:
  - `required_columns`: `sample_id`, `true_value`, `predicted_value`
  - `units`:
    - `true_value`: log(GPa)
    - `predicted_value`: log(GPa)

### results_summary.json
- path: `/app/outputs/results_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Self‑reported MAE values for the four properties. The checker compares them against the hidden paper gold and cross‑checks consistency with recomputed MAE from the prediction CSVs.
- schema:
  - `type`: object
  - `required`:
    - `total_energy_mae`: float
    - `bandgap_mae`: float
    - `shear_modulus_mae`: float
    - `bulk_modulus_mae`: float

Notes: The primary scoring uses the raw prediction CSVs to recompute MAE and compare against the paper's reported values with a threshold‑or‑better policy. The summary JSON serves as a fallback T0 check and for consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions_total_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "sample_id",
          "true_value",
          "predicted_value"
        ],
        "units": {
          "true_value": "eV",
          "predicted_value": "eV"
        }
      },
      "description": "Per‑sample predictions on the total energy test set. MAE will be recomputed by the checker from this file."
    },
    {
      "file": "predictions_bandgap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "sample_id",
          "true_value",
          "predicted_value"
        ],
        "units": {
          "true_value": "eV",
          "predicted_value": "eV"
        }
      },
      "description": "Per‑sample predictions on the bandgap test set. MAE will be recomputed by the checker from this file."
    },
    {
      "file": "predictions_shear_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "sample_id",
          "true_value",
          "predicted_value"
        ],
        "units": {
          "true_value": "log(GPa)",
          "predicted_value": "log(GPa)"
        }
      },
      "description": "Per‑sample predictions on the log(shear modulus) test set. MAE will be recomputed by the checker from this file."
    },
    {
      "file": "predictions_bulk_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "sample_id",
          "true_value",
          "predicted_value"
        ],
        "units": {
          "true_value": "log(GPa)",
          "predicted_value": "log(GPa)"
        }
      },
      "description": "Per‑sample predictions on the log(bulk modulus) test set. MAE will be recomputed by the checker from this file."
    },
    {
      "file": "results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "total_energy_mae": "float",
          "bandgap_mae": "float",
          "shear_modulus_mae": "float",
          "bulk_modulus_mae": "float"
        }
      },
      "description": "Self‑reported MAE values for the four properties. The checker compares them against the hidden paper gold and cross‑checks consistency with recomputed MAE from the prediction CSVs."
    }
  ],
  "notes": "The primary scoring uses the raw prediction CSVs to recompute MAE and compare against the paper's reported values with a threshold‑or‑better policy. The summary JSON serves as a fallback T0 check and for consistency."
}
```

## How you are scored
A hidden verifier will examine all scored output artifacts in `/app/outputs`. For each property‑specific predictions CSV, the verifier will recompute the MAE from the `true_value` and `predicted_value` columns and compare it against a hidden reference value using a threshold‑or‑better policy: meeting or exceeding the reference earns full credit for that property, and reward decreases only as the MAE becomes worse. The verifier will also check that the MAE values reported in `results_summary.json` are consistent with those recomputed from the corresponding prediction CSVs. Scores for each property are combined to produce a final reward. Simply reporting a number without genuinely executing the training and inference steps will not produce valid prediction files and will not pass the check.
