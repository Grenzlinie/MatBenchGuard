# Evaluating ML Model Exploration Power via Forward Cross-Validation on Materials Properties

## Problem background
Materials discovery, such as finding new superconductors with higher critical temperatures or materials with extremely low thermal conductivity, requires predictive models that can identify compounds with property values outside the domain of known materials. Traditional evaluation methods like random k-fold cross-validation measure a model's interpolation performance (predicting within the training distribution), but they do not assess its exploration capability—the ability to accurately predict properties for materials that are outliers relative to training data. Quantifying this explorative power is essential because many promising discoveries lie beyond the range of properties seen in existing datasets. This task addresses the challenge of properly evaluating and benchmarking machine learning models for explorative materials property prediction.

## Approach
The core idea is to use k-fold forward cross-validation (kmFCV) instead of random splitting. In this method, all samples are first sorted by the target property value. The sorted list is partitioned into k equal-sized folds. For k-fold FCV, at each step the model is trained on the first i folds and tested on the (i+1)-th fold, so the validation set always lies beyond the training set's property range. A more general variant, k-fold m-step FCV, introduces a gap: the test fold is m steps ahead of the last training fold. Additionally, the exploration accuracy E_accuracy is defined as the fraction of test samples whose predicted value exceeds the maximum property value in the training set, providing a direct measure of a model's ability to predict out-of-domain values.

This task benchmarks the exploration performance of five machine learning models across three materials properties:
- Datasets: formation energy (MPFE-35K) and band gap (MPBG-20K) from the Materials Project, and superconducting critical temperature (SC-6K) from SuperCon.
- Models and representations: 1-Nearest-Neighbor with Magpie features, Random Forest with Magpie features, a Multi-Layer Perceptron with one-hot composition encoding, a Convolutional Neural Network with Periodic Table Representation (PTR) images, and the Crystal Graph Convolutional Neural Network (CGCNN) utilizing crystal structure graphs. (CGCNN is not applied to the SuperCon dataset because it lacks structural data.)
The evaluation uses 100-fold random CV, 100-fold FCV (m=1), and for the formation energy dataset with one-hot encoding, additional 100-fold FCV with m=2 and m=3. All models are trained on the representation subsets (compounds composed only of elements covered by PTR) for the main benchmark, and 1NN/RF/MLP with one-hot encoding are also evaluated on the full (complete) datasets. The goal is to compute standard regression metrics (MAE, RMSE, R²) and exploration accuracy for each model/dataset/split, providing a comprehensive comparison of interpolation vs. exploration performance.

## Reproduction target
For the three materials properties (formation energy, band gap, superconducting critical temperature), perform the following using 100-fold CV and 100-fold FCV (k=100, m=1) on the representation sets:
- Compute MAE, RMSE, and R² for each model (1NN-Magpie, RF-Magpie, MLP-Onehot, CNN-PTR, CGCNN; exclude CGCNN for superconducting Tc).
- For FCV, also compute exploration accuracy E_accuracy.
Additionally, on the formation energy dataset with one-hot composition representation, evaluate Random Forest and MLP using 100-fold FCV with m=1,2,3 and report MAE and E_accuracy for each m.
Finally, on the complete datasets (full sets, not filtered to PTR elements) with one-hot composition, evaluate 1NN, RF, and MLP using 100-fold CV and FCV, and report MAE.
Aggregate all metrics into a single JSON file named benchmark_results.json following the schema described in the output contract. The file must contain top-level keys for each property, with model_results arrays, m_step_results (formation energy only), and onehot results for the complete datasets.

## Assets

- kmFCV repository (pre-filtered datasets): https://github.com/buptxz/kmFCV
- scikit-learn: scikit-learn
- matminer: matminer
- pymatgen: pymatgen
- PyTorch: torch
- CGCNN implementation: https://github.com/txie-93/cgcnn

## Workflow steps

### Step 1: Data download and representation set filtering
- Role: process
- Action: Download the three filtered datasets (MPFE-35K, MPBG-20K, SC-6K) from the kmFCV repository. Further filter each to include only compounds whose elements are covered by the periodic table representation (PTR), creating the representation sets MPFE-18K, MPBG-10K, SC-2.8K.
- Evidence: `/app/outputs/datasets_filtered.log`

### Step 2: Compute material descriptors and prepare crystal graph inputs
- Role: process
- Action: For all datasets (complete and representation sets), compute Magpie features using matminer, one-hot composition vectors, and PTR image representation. Export crystal structure json files for CGCNN. Save feature matrices to disk.
- Evidence: `/app/outputs/features_computed.log`

### Step 3: Run full benchmark: CV, FCV, and m-step FCV evaluations
- Role: scored (load-bearing)
- Action: For each dataset and model combination specified in the reproduction target, perform 100-fold random-split CV and 100-fold forward FCV (k=100, m=1). For formation energy with one-hot representation, also run 100-fold FCV with m=2 and m=3. Train and evaluate 1NN, RF, MLP, CNN, and CGCNN on representation sets; train and evaluate 1NN, RF, and MLP on complete datasets with one-hot representation. Compute MAE, RMSE, R², and exploration accuracy E_accuracy. Aggregate all metrics into a single JSON file.
- Output file: `/app/outputs/benchmark_results.json`
- Format: json
- Contract: A JSON object with keys: 'formation_energy', 'band_gap', 'superconducting_Tc' (each an object with 'model_results': list of objects with keys 'model', 'cv_MAE', 'cv_RMSE', 'cv_R2', 'fcv_MAE', 'fcv_RMSE', 'fcv_R2', 'fcv_E_accuracy'; and for 'formation_energy' also 'm_step_results': list of objects with keys 'model', 'm', 'cv_MAE', 'fcv_MAE', 'fcv_E_accuracy'); plus 'formation_energy_complete_onehot', 'band_gap_complete_onehot', 'superconducting_Tc_complete_onehot' (each a list of objects with keys 'model', 'cv_MAE', 'fcv_MAE').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/benchmark_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### benchmark_results.json
- path: `/app/outputs/benchmark_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Aggregated benchmark metrics covering all model/dataset combinations. The metrics are directional (lower MAE/RMSE better; higher R²/E_accuracy better).
- schema:
  - `type`: object
  - `required`:
    - `formation_energy`: object containing model_results and m_step_results
    - `band_gap`: object containing model_results
    - `superconducting_Tc`: object containing model_results
    - `formation_energy_complete_onehot`: array of objects
    - `band_gap_complete_onehot`: array of objects
    - `superconducting_Tc_complete_onehot`: array of objects
  - `items`:
    - `model_results_item`:
      - `model`: string
      - `cv_MAE`: number (float)
      - `cv_RMSE`: number (float)
      - `cv_R2`: number (float)
      - `fcv_MAE`: number (float)
      - `fcv_RMSE`: number (float)
      - `fcv_R2`: number (float)
      - `fcv_E_accuracy`: number (float; 0-1)
    - `m_step_results_item`:
      - `model`: string
      - `m`: integer
      - `cv_MAE`: number (float)
      - `fcv_MAE`: number (float)
      - `fcv_E_accuracy`: number (float; 0-1)
    - `onehot_result_item`:
      - `model`: string
      - `cv_MAE`: number (float)
      - `fcv_MAE`: number (float)
  - `description`: Top-level keys for each property, containing model_results arrays and (for formation_energy) m_step_results. Additional keys for complete-set one-hot encoding results.

Notes: The checker compares the agent's reported metrics to hidden paper gold values using threshold-or-better tolerances and also checks structural relationships (e.g., FCV MAE > CV MAE, 1NN/RF E_accuracy ≈ 0). All gold values and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "benchmark_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "formation_energy": "object containing model_results and m_step_results",
          "band_gap": "object containing model_results",
          "superconducting_Tc": "object containing model_results",
          "formation_energy_complete_onehot": "array of objects",
          "band_gap_complete_onehot": "array of objects",
          "superconducting_Tc_complete_onehot": "array of objects"
        },
        "items": {
          "model_results_item": {
            "model": "string",
            "cv_MAE": "number (float)",
            "cv_RMSE": "number (float)",
            "cv_R2": "number (float)",
            "fcv_MAE": "number (float)",
            "fcv_RMSE": "number (float)",
            "fcv_R2": "number (float)",
            "fcv_E_accuracy": "number (float; 0-1)"
          },
          "m_step_results_item": {
            "model": "string",
            "m": "integer",
            "cv_MAE": "number (float)",
            "fcv_MAE": "number (float)",
            "fcv_E_accuracy": "number (float; 0-1)"
          },
          "onehot_result_item": {
            "model": "string",
            "cv_MAE": "number (float)",
            "fcv_MAE": "number (float)"
          }
        },
        "description": "Top-level keys for each property, containing model_results arrays and (for formation_energy) m_step_results. Additional keys for complete-set one-hot encoding results."
      },
      "description": "Aggregated benchmark metrics covering all model/dataset combinations. The metrics are directional (lower MAE/RMSE better; higher R²/E_accuracy better)."
    }
  ],
  "notes": "The checker compares the agent's reported metrics to hidden paper gold values using threshold-or-better tolerances and also checks structural relationships (e.g., FCV MAE > CV MAE, 1NN/RF E_accuracy ≈ 0). All gold values and tolerances are hidden."
}
```

## How you are scored
Your submitted benchmark_results.json will be evaluated by a hidden verifier. The verifier compares your reported metrics (MAE, RMSE, R², E_accuracy) to independently established reference values using appropriate tolerances. Scoring is threshold-or-better for directional metrics: for MAE and RMSE (lower is better) your value only needs to be at or below a threshold; for R² and E_accuracy (higher is better) it must be at or above a threshold. The verifier also checks structural consistency: for every model and dataset, the FCV MAE must be strictly greater than the CV MAE, and for 1NN and Random Forest models, the exploration accuracy must be approximately zero. The final reward is a weighted combination of all checks. Executing the full workflow and producing the required output file is necessary; reporting the paper's numbers without running the pipeline will not pass all structural and metric checks.
