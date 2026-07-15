# Alloy Melting Temperature Prediction via Deep Neural Network from Composition Descriptors

## Problem background
Accurate prediction of alloy melting temperatures is crucial for materials design, but simple composition-weighted averages (Vegard's law) often deviate significantly from true values. This task addresses predicting the melting temperature (liquidus) of binary alloys from composition-based physical descriptors using machine learning.

## Approach
Build a deep neural network (MeltNet) that takes seven physically motivated descriptors — VEC, electronegativity difference, atomic radius difference, ideal mixing entropy, formation enthalpy (from Materials Project), average fusion entropy, and fusion-entropy-weighted average melting point — and predicts the excess melting temperature ΔT = T - T_bar, where T_bar is the composition-weighted average melting point. The model is trained on liquidus temperatures computed using pycalphad with NIMS tdb files for 287 binary systems. A 5‑fold cross-validation by system (not composition) evaluates generalization, and an ensemble of 100 sub-models per fold (trained on random 75% subsets) is compared against a single model. The primary metric is mean absolute error (MAE) of the predicted melting temperature.

## Reproduction target
Produce a JSON file `/app/outputs/meltnet_results.json` containing the per-fold test MAE and overall MAE (in Kelvin) for both the single MeltNet model and the ensemble average across five cross-validation folds. The file must include keys: `single_fold_mae` (array of 5 numbers), `ensemble_fold_mae` (array of 5 numbers), `overall_single_mae` (number), and `overall_ensemble_mae` (number).

## Assets

- NIMS Computational Phase Diagram Database (tdb files): https://cpddb.nims.go.jp/en/
- pycalphad: pycalphad
- Materials Project API: https://materialsproject.org/
- PyTorch: torch
- Elemental properties dataset
- Binary systems list: `/app/data/binary_systems.txt` (one system per line, e.g., Ag-Au)

## Workflow steps

### Step 1: Generate liquidus dataset and compute descriptors
- Role: process
- Action: For each binary system listed in `/app/data/binary_systems.txt` (one pair per line, e.g., Ag-Au), download the corresponding tdb file from the NIMS database (https://cpddb.nims.go.jp/en/) if not already present. Then use pycalphad to compute liquidus temperatures for that system with composition step 0.01 (endpoints excluded). For each composition, calculate the seven input features (VEC, electronegativity difference Δχ, atomic radius difference δ, ideal mixing entropy ΔS_mix, formation enthalpy ΔH_f from Materials Project, average fusion entropy S_fus, fusion-entropy-weighted average melting point T_tilde) and the target excess melting temperature ΔT = T - T_bar. Save the processed dataset for training.
- Evidence: `/app/outputs/processed_dataset.csv`

### Step 2: 5-fold cross-validation of single MeltNet model
- Role: process
- Action: Implement MeltNet DNN (3 hidden layers, 48 nodes per layer, L1 loss) in PyTorch using the fixed hyperparameters reported in the paper. Partition the 287 binary systems into 5 folds. For each fold, train on 4 folds and test on the held-out fold. Record the test set predicted ΔT values and corresponding true ΔT values.
- Evidence: `/app/outputs/single_predictions.csv`

### Step 3: Ensemble training with 100 random subsets per fold
- Role: process
- Action: For each fold, generate 100 random training subsets (each 75% of the training compositions) and train a MeltNet model on each subset using the same fixed hyperparameters. Compute the ensemble mean prediction on the test fold. Record the ensemble predicted ΔT and true values.
- Evidence: `/app/outputs/ensemble_predictions.csv`

### Step 4: Compute and save cross-validated MAE metrics
- Role: scored (load-bearing)
- Action: From the saved single and ensemble test predictions, compute the per-fold MAE and overall MAE for both single and ensemble predictions. Write the results as a JSON file with keys: single_fold_mae (list of 5 floats, K), ensemble_fold_mae (list of 5 floats, K), overall_single_mae (float, K), overall_ensemble_mae (float, K).
- Output file: `/app/outputs/meltnet_results.json`
- Format: json
- Contract: JSON object with required keys: single_fold_mae (array of 5 numbers, units: Kelvin), ensemble_fold_mae (array of 5 numbers, units: Kelvin), overall_single_mae (number, units: Kelvin), overall_ensemble_mae (number, units: Kelvin).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/meltnet_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### meltnet_results.json
- path: `/app/outputs/meltnet_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: MAE values of single and ensemble MeltNet predictions across 5-fold cross-validation, compared to hidden reference values from the paper.
- schema:
  - `type`: object
  - `required`:
    - `single_fold_mae`: array of 5 floats (Kelvin)
    - `ensemble_fold_mae`: array of 5 floats (Kelvin)
    - `overall_single_mae`: float (Kelvin)
    - `overall_ensemble_mae`: float (Kelvin)

Notes: The agent must execute the full pipeline (data generation, descriptor computation, single-model cross-validation, ensemble training) and compute the MAE values. The checker will compare each reported MAE to hidden gold values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "meltnet_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "single_fold_mae": "array of 5 floats (Kelvin)",
          "ensemble_fold_mae": "array of 5 floats (Kelvin)",
          "overall_single_mae": "float (Kelvin)",
          "overall_ensemble_mae": "float (Kelvin)"
        }
      },
      "description": "MAE values of single and ensemble MeltNet predictions across 5-fold cross-validation, compared to hidden reference values from the paper."
    }
  ],
  "notes": "The agent must execute the full pipeline (data generation, descriptor computation, single-model cross-validation, ensemble training) and compute the MAE values. The checker will compare each reported MAE to hidden gold values with tolerances."
}
```

## How you are scored
A hidden verifier will read your `meltnet_results.json` and compare each reported MAE (single and ensemble, per-fold and overall) against the corresponding paper-reported values. The metric is directional (lower MAE is better); results that meet or exceed (i.e., are less than or equal to) the hidden reference within an allowed tolerance will earn full credit for each comparison, and the final reward is a weighted combination of these comparisons. Intermediate prediction files (`processed_dataset.csv`, `single_predictions.csv`, `ensemble_predictions.csv`) must also be present as evidence that the workflow was executed, but they are not directly scored. Simply outputting the correct numbers without running the pipeline will not pass.
