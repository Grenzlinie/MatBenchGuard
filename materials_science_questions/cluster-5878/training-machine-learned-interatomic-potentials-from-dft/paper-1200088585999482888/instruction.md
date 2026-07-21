# Training a Δ-ML Ensemble for Intermolecular Interaction Energy Correction

## Problem background
Accurate quantum mechanical computation of intermolecular interaction energies is essential for predicting crystal structures, understanding molecular recognition in drug design, and developing force fields. The “gold standard” CCSD(T) at the complete basis set limit (CBS) is extremely accurate but scales prohibitively with system size, while cheaper methods (Hartree–Fock, MP2, DFT, SAPT) introduce errors that vary with the chemical system. Selecting an appropriate level of theory that balances accuracy and computational cost remains a major challenge. This task addresses that challenge by building an ensemble of machine-learned correction models that estimate errors for multiple levels of theory and reveal relationships among theoretical methods.

## Approach
The core idea is to train Δ-machine-learning (Δ‑ML) neural networks that predict the difference in interaction energy, ΔE = E_method − E_CCSD(T)/CBS, for a given dimer and a given quantum chemical method. Instead of using hand-crafted descriptors, the models use fixed-length feature vectors (embeddings) extracted from the penultimate layer of a pre-trained atom-pairwise message-passing network (AP‑Net2) that was trained on a large, diverse dimer dataset. For five representative methods spanning wavefunction, DFT, and SAPT levels, separate Δ‑ML models are trained on a subset of the BFDB‑Ext dataset, which provides precomputed interaction energies for thousands of dimers at many levels of theory. To uncover method relationships, all‑to‑all Δ‑ML models are also trained—for each ordered pair of methods, a model learns the energy difference between the two methods. Hierarchical clustering of the pairwise errors then reveals which methods behave similarly, providing a data-driven grouping that can be compared to theoretical expectations.

## Reproduction target
Your objective is to (1) produce test‑set predicted ΔE values for five levels of theory—HF/aug‑cc‑pVDZ/CP, MP2/aug‑cc‑pVQZ/CP, B3LYP/aug‑cc‑pVTZ/CP, B2PLYP‑D3/aug‑cc‑pVTZ/CP, and SAPT0/jun‑cc‑pVDZ—trained on 60% of the BFDB‑Ext dataset (3324 dimers) and evaluated on the held‑out 40% test split, and to compute the per‑method mean absolute error (MAE) from those predictions; and (2) from all‑to‑all Δ‑ML models among the same five methods, compute a pairwise MAE distance matrix and perform hierarchical clustering to assign a cluster label to each method. The two scored deliverables are a CSV of test predictions and true ΔE values (`test_predictions.csv`) and a CSV of method‑to‑cluster assignments (`method_clusters.csv`).

## Assets

- BFDB-Ext dataset
- AP-Net2 pre-trained model: https://github.com/chem-d/AP-Net2

## Workflow steps

### Step 1: Data preparation and train/test split
- Role: process
- Action: Download the BFDB-Ext dataset and filter to the 3,324 dimers with CCSD(T)/CBS/CP reference interaction energies. Extract the five selected levels of theory (HF/aug-cc-pVDZ/CP, MP2/aug-cc-pVQZ/CP, B3LYP/aug-cc-pVTZ/CP, B2PLYP-D3/aug-cc-pVTZ/CP, SAPT0/jun-cc-pVDZ) and compute the target ΔE = E_method − E_CCSD(T)/CBS/CP for each dimer. Randomly split into 60% train / 40% test with a fixed seed.
- Evidence: none

### Step 2: Extract AP-Net2 embeddings
- Role: process
- Action: Using the pre-trained AP-Net2 model, extract the penultimate-layer embedding for every dimer in the full set (train + test). Save the embeddings for reuse.
- Evidence: `/app/outputs/embeddings.npy`

### Step 3: Train Δ‑ML models to CCSD(T)/CBS/CP for five methods
- Role: process
- Action: For each of the five chosen methods, train a feedforward neural network (five hidden layers) to predict ΔE from the AP-Net2 embeddings using the training split, minimizing MSE. Save the trained model weights.
- Evidence: `/app/outputs/delta_models`

### Step 4: Evaluate test MAE for each method
- Role: scored
- Action: For each dimer in the test set, use the trained Δ‑ML models to predict ΔE. Compute the true ΔE from the dataset. Write a CSV with columns dimer_id, method, predicted_delta_energy (kcal/mol), true_delta_energy (kcal/mol). One row per dimer and method.
- Output file: `/app/outputs/test_predictions.csv`
- Format: csv
- Contract: Columns: dimer_id (string), method (string, one of the five selected level‑of‑theory labels), predicted_delta_energy (float, kcal/mol), true_delta_energy (float, kcal/mol)
- Scoring: scored by hidden verifier

### Step 5: Train all‑to‑all Δ‑ML models among the five methods
- Role: process
- Action: For every ordered pair (i,j) of the five chosen methods, train a Δ‑ML model (same architecture as in Step 2) to predict ΔE_ij = E_i − E_j using the same train/test split and embedding inputs. Save the trained models.
- Evidence: `/app/outputs/all_to_all_models`

### Step 6: Hierarchical clustering of methods
- Role: scored (load-bearing)
- Action: From the all‑to‑all Δ‑ML models, compute the test MAE for every ordered pair. Build a 5×5 distance matrix and perform hierarchical clustering (e.g., average linkage). Cut the dendrogram to obtain cluster labels. Write a CSV with columns method, cluster_label (integer).
- Output file: `/app/outputs/method_clusters.csv`
- Format: csv
- Contract: Columns: method (string, same level‑of‑theory label as above), cluster_label (integer)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/test_predictions.csv`
- `/app/outputs/method_clusters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### test_predictions.csv
- path: `/app/outputs/test_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Test‑set predictions and true ΔE values for the five methods. The checker recomputes per‑method MAE and compares to hidden thresholds.
- schema:
  - `type`: table
  - `required_columns`: `dimer_id`, `method`, `predicted_delta_energy`, `true_delta_energy`
  - `units`:
    - `predicted_delta_energy`: kcal/mol
    - `true_delta_energy`: kcal/mol

### method_clusters.csv
- path: `/app/outputs/method_clusters.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Cluster assignments for the five methods from hierarchical clustering. The checker computes adjusted Rand index against hidden expected groupings.
- schema:
  - `type`: table
  - `required_columns`: `method`, `cluster_label`
  - `units`: object

Notes: The checker recomputes MAE from the test_predictions.csv and compares each to a hidden threshold (threshold_or_better logic). For method_clusters.csv, the checker computes adjusted Rand index between the submitted labels and hidden expected clusters, requiring a high value for full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "test_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "dimer_id",
          "method",
          "predicted_delta_energy",
          "true_delta_energy"
        ],
        "units": {
          "predicted_delta_energy": "kcal/mol",
          "true_delta_energy": "kcal/mol"
        }
      },
      "description": "Test‑set predictions and true ΔE values for the five methods. The checker recomputes per‑method MAE and compares to hidden thresholds."
    },
    {
      "file": "method_clusters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "cluster_label"
        ],
        "units": {}
      },
      "description": "Cluster assignments for the five methods from hierarchical clustering. The checker computes adjusted Rand index against hidden expected groupings."
    }
  ],
  "notes": "The checker recomputes MAE from the test_predictions.csv and compares each to a hidden threshold (threshold_or_better logic). For method_clusters.csv, the checker computes adjusted Rand index between the submitted labels and hidden expected clusters, requiring a high value for full credit."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores the two output files, then combines the scores into a final reward between 0 and 1. For `test_predictions.csv`, the verifier will compute the mean absolute error for each of the five methods from your `predicted_delta_energy` column and compare it to a hidden performance threshold; methods that meet or beat the threshold earn full credit for that method, and the stage score reflects how many of the five methods pass. For `method_clusters.csv`, the verifier will compute the adjusted Rand index between your submitted cluster labels and an expected grouping consistent with theoretical method families; a higher index corresponds to a higher stage score. Each stage’s score is weighted, and the final reward is the weighted sum. Reporting numbers that merely match published values without producing the required artifacts will not earn a passing score.
