# SVR with XRD Descriptor for Predicting Total Energy of Si Alloys

## Problem background
Silicon-based anodes for multivalent cation batteries (e.g., Li, Na, Mg, Ca) offer high gravimetric energy densities but suffer from structural instability and volume expansion. Predictive modeling of thermodynamic stability (e.g., total energy per atom) of Si alloys can accelerate material screening and support the design of more stable anode materials. The target of this task is to build a machine learning model that predicts the total energy per atom for novel Si alloy compositions, using only structural descriptors derived from the crystal structures.

## Approach
A support vector regression (SVR) model is trained using the X-ray diffraction (XRD) pattern as the structural descriptor. The dataset consists of inorganic Si–A alloy structures (A = Li, Na, K, Mg, Ca, Al) retrieved from the Materials Project database. The training set includes structures where A is Li, K, Mg, or Ca, and the test set comprises Na-containing and Al-containing Si alloys identified by a provided list of Materials Project IDs. The XRD descriptor is computed for all structures using open-source libraries (e.g., pymatgen/matminer). An exhaustive grid search over SVR hyperparameters (C, gamma, epsilon) with an RBF kernel and repeated 5-fold cross-validation is performed on the training data to select the best model. The final model is evaluated by predicting total energy per atom on the unseen test structures and computing the root mean square error (RMSE).

## Reproduction target
Train an SVR model using the XRD structural descriptor and hyperparameters optimized by GridSearchCV on Si–A alloy structures from the Materials Project with A = Li, K, Mg, Ca as the training set. Use the trained model to predict the total energy per atom (in eV/atom) for the 15 test structures (Na- and Al-containing Si alloys) whose Materials Project IDs are provided in the bundled test_ids.csv file. Output the per-sample predictions as a CSV file (predictions.csv) and compute the root mean square error (RMSE) between the predictions and the actual total energy per atom values, writing the RMSE as a single float to test_rmse.txt.

## Assets

- Materials Project database: https://materialsproject.org
- Test structure MP IDs
- pymatgen: pymatgen
- matminer: matminer
- scikit-learn: scikit-learn
- numpy: numpy
- pandas: pandas

## Workflow steps

### Step 1: Dataset retrieval and splitting
- Role: process
- Action: Query the Materials Project database through its API to obtain all inorganic crystal structures containing Si and the elements A = Li, Na, K, Mg, Ca, Al (A_x Si_y alloys). Extract total energy per atom. Partition into training set (A = Li, K, Mg, Ca) and test set (12 Na‑containing + 3 Al‑containing structures identified by the MP IDs in the bundled test_ids.csv).
- Evidence: `/app/outputs/dataset_info.json`

### Step 2: XRD descriptor computation
- Role: process
- Action: For all training and test structures, compute the X-ray diffraction (XRD) pattern descriptor using the matminer or pymatgen library.
- Evidence: none

### Step 3: SVR hyperparameter tuning and training
- Role: process
- Action: Perform exhaustive grid search over SVR hyperparameters (C, gamma, epsilon) using GridSearchCV with RBF kernel and repeated 5-fold cross-validation on the training set with XRD descriptors and total energy per atom target. Select the best hyperparameters and train a final SVR model on the full training set.
- Evidence: `/app/outputs/training_info.json`

### Step 4: Test set prediction
- Role: scored (load-bearing)
- Action: Use the final SVR model to predict total energy per atom for the 15 test structures. Write a CSV file with structure ID and predicted value.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: structure_id (string, Materials Project ID), predicted_total_energy_per_atom (float, eV/atom)
- Scoring: scored by hidden verifier

### Step 5: Compute test RMSE
- Role: scored (load-bearing)
- Action: Calculate the root mean square error (RMSE) between the predicted and actual total energy per atom values for the 15 test structures. Write the RMSE as a single float to a text file.
- Output file: `/app/outputs/test_rmse.txt`
- Format: txt
- Contract: single floating-point number, eV/atom
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`
- `/app/outputs/test_rmse.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-sample predicted total energy per atom for the 15 test structures. The checker will recompute RMSE against hidden true values and score the reproduction based on the recomputed metric.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `predicted_total_energy_per_atom`
  - `units`:
    - `predicted_total_energy_per_atom`: eV/atom

### test_rmse.txt
- path: `/app/outputs/test_rmse.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The agent-reported test RMSE. The checker verifies that this value meets or exceeds the hidden threshold (the paper-reported RMSE with tolerance) and is consistent with the recomputed RMSE from predictions.csv.
- schema:
  - `type`: text
  - `field`: rmse
  - `units`: eV/atom

Notes: Task covers only the total energy/atom prediction using XRD descriptor and Grid Search CV, as scoped from the paper. Formation energy and packing fraction predictions are omitted to keep the task minimal.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "predicted_total_energy_per_atom"
        ],
        "units": {
          "predicted_total_energy_per_atom": "eV/atom"
        }
      },
      "description": "Per-sample predicted total energy per atom for the 15 test structures. The checker will recompute RMSE against hidden true values and score the reproduction based on the recomputed metric."
    },
    {
      "file": "test_rmse.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "field": "rmse",
        "units": "eV/atom"
      },
      "description": "The agent-reported test RMSE. The checker verifies that this value meets or exceeds the hidden threshold (the paper-reported RMSE with tolerance) and is consistent with the recomputed RMSE from predictions.csv."
    }
  ],
  "notes": "Task covers only the total energy/atom prediction using XRD descriptor and Grid Search CV, as scoped from the paper. Formation energy and packing fraction predictions are omitted to keep the task minimal."
}
```

## How you are scored
A hidden verifier re-computes the RMSE from your predictions.csv using hidden true total-energy values for the same test structures. It then compares the recomputed RMSE against a hidden reference threshold. Meeting or exceeding the threshold earns full credit; credit degrades monotonically as the error increases above the threshold. Additionally, the RMSE you report in test_rmse.txt is verified for consistency with the recomputed RMSE. Each scored output contributes a weighted fraction to the total reward.
