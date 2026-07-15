# Predicting Formation Energies of Disordered Alloys with ALIGNN Trained on Ordered Structures

## Problem background
High-entropy alloys (HEAs) offer a vast design space with tunable properties, but density functional theory (DFT) simulations of chemically disordered structures are expensive. A recently published open DFT dataset provides formation energies for a large number of multi-component alloy structures, including both small ordered cells and larger special quasirandom structures (SQSs) that approximate random disorder. This task investigates whether a machine learning model trained exclusively on the simpler, smaller ordered structures can accurately predict the formation energies of the more complex SQS structures. The target quantity is the mean absolute error (MAE) of the model’s predictions on a held-out set of SQS structures, quantifying the out-of-distribution generalization ability.

## Approach
Use the Atomistic Line Graph Neural Network (ALIGNN), a graph neural network that represents crystal structures as atom and bond-angle graphs. Train ALIGNN using the formation energies of all ordered structures (unit cells with 8 or fewer atoms) from the public dataset as the target. After training, apply the model to predict the formation energy of every SQS structure (unit cells with 27 or more atoms) in the dataset, without any further retraining or finetuning on SQS data. Finally, compute the mean absolute error (MAE) between the predicted and DFT‑computed formation energies (both in eV/atom) across all SQS structures. The training follows standard procedures for formation energy prediction; the model must learn to generalize from small, ordered periodic cells to larger, chemically disordered cells.

## Reproduction target
Produce a CSV file (`sqs_predictions.csv`) containing, for every SQS structure in the dataset (unit cells ≥ 27 atoms), three columns: `structure_id` (a unique identifier), `true_formation_energy` (the DFT‑computed formation energy, in eV/atom), and `predicted_formation_energy` (the model’s predicted formation energy, in eV/atom). The hidden verifier will compute the overall MAE from these values and compare it against a predetermined acceptance threshold. The goal is to achieve an MAE that demonstrates effective generalization from ordered to disordered structures.

## Assets

- Multi-component alloy DFT formation energy dataset: https://doi.org/10.5281/zenodo.10854500
- ALIGNN (Atomistic Line Graph Neural Network): https://github.com/usnistgov/alignn

## Workflow steps

### Step 1: Data acquisition and splitting
- Role: process
- Action: Download the public DFT formation energy dataset from Zenodo (DOI:10.5281/zenodo.10854500). Parse all structures and separate them into two sets: ordered structures (≤8 atoms) for training, and SQS structures (≥27 atoms) for testing. Extract the formation energy target for each structure.
- Evidence: `/app/outputs/split_summary.json`

### Step 2: Train ALIGNN on ordered structures
- Role: process
- Action: Train an ALIGNN model on the formation energies of the ordered structures (≤8 atoms) using the ALIGNN implementation. The model learns to map atomic structure to formation energy.
- Evidence: `/app/outputs/trained_model.pt`

### Step 3: Predict formation energies of SQS structures
- Role: scored (load-bearing)
- Action: Use the trained ALIGNN model to predict the formation energy for every SQS structure (≥27 atoms) in the test set. For each structure record the structure identifier, the true DFT formation energy (eV/atom), and the model's predicted formation energy (eV/atom).
- Output file: `/app/outputs/sqs_predictions.csv`
- Format: csv
- Contract: columns: structure_id, true_formation_energy (eV/atom), predicted_formation_energy (eV/atom)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sqs_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sqs_predictions.csv
- path: `/app/outputs/sqs_predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Per-structure predictions on the SQS test set (Ordered→SQS), used to compute out-of-distribution mean absolute error (MAE) in eV/atom.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `true_formation_energy`, `predicted_formation_energy`
  - `units`:
    - `true_formation_energy`: eV/atom
    - `predicted_formation_energy`: eV/atom

Notes: Single scored generalization task: Ordered→SQS. The approved plan scoped this task to the Ordered→SQS out-of-distribution generalization, which is the paper's primary quantitative headline for ALIGNN. The solve infrastructure supports only the three originally configured output artifacts (split_summary.json, trained_model.pt, sqs_predictions.csv), so additional generalization tasks (Low→High, Equi→Non-equi) cannot be added without creating new solve blocks, which is a system-level change outside this repair's scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sqs_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "true_formation_energy",
          "predicted_formation_energy"
        ],
        "units": {
          "true_formation_energy": "eV/atom",
          "predicted_formation_energy": "eV/atom"
        }
      },
      "description": "Per-structure predictions on the SQS test set (Ordered→SQS), used to compute out-of-distribution mean absolute error (MAE) in eV/atom."
    }
  ],
  "notes": "Single scored generalization task: Ordered→SQS. The approved plan scoped this task to the Ordered→SQS out-of-distribution generalization, which is the paper's primary quantitative headline for ALIGNN. The solve infrastructure supports only the three originally configured output artifacts (split_summary.json, trained_model.pt, sqs_predictions.csv), so additional generalization tasks (Low→High, Equi→Non-equi) cannot be added without creating new solve blocks, which is a system-level change outside this repair's scope."
}
```

## How you are scored
An automated verifier will inspect your submitted output artifacts. The primary scored artifact is `sqs_predictions.csv`. The verifier will:
- Confirm the file contains at least the minimum required number of SQS entries.
- Compute the mean absolute error (MAE) between the `true_formation_energy` and `predicted_formation_energy` columns.
- Compare that MAE against a hidden reference value using a threshold‑or‑better policy (lower MAE is better; exceeding the threshold yields higher reward, while a substantially worse MAE results in lower or no reward).

Additional light‑weight checks (e.g., correct column names, valid numeric values) contribute a small fraction of the total score. The final reward is a weighted sum across all checks and lies between 0 and 1. Reporting the paper’s numbers without running the required training and evaluation will not satisfy the scoring because the verifier independently recomputes the metric from your raw predictions.
