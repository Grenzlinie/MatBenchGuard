# 2D Material Thermodynamic Stability Classification and Formation Energy Prediction

## Problem background
Two-dimensional (2D) materials hold great promise for a wide range of applications, but any candidate must first be thermodynamically stable. Computing stability from first principles is expensive when thousands of compounds are considered, making it a bottleneck in high-throughput screening. This work addresses that problem by building machine learning models that can rapidly classify the thermodynamic stability of 2D materials into low, medium, or high stability, and predict the formation energy of the most stable candidates, using only composition and structural prototype information without requiring knowledge of atomic positions.

## Approach
The approach leverages a publicly available database of DFT-computed 2D materials (C2DB) to train supervised models. Each material is represented by statistical functions (average, weighted average, minimum, maximum, standard deviation) of its constituent atoms' fundamental properties, plus a categorical label for its structural prototype. A first model uses a gradient-boosted decision tree classifier (XGBoost) to assign one of three stability classes. To improve performance, the SISSO (sure independence screening and sparsifying operator) method is used in a multi-task fashion to automatically discover composite nonlinear features that separate stability classes across prototypes; the best of these are added to the feature set. A second, 3‑dimensional SISSO regression model is trained on the high‑stability materials to predict formation energy. The trained classifier and regression model are then applied to novel compounds GaAsSe₄ and AlAsTe₄ placed in two different prototypes (MoS₂ and CdI₂), and the predictions are validated by DFT formation energy calculations using the PBE exchange‑correlation functional and projector‑augmented wave pseudopotentials.

## Reproduction target
Train the thermodynamic stability classifier and the formation energy regression model on the C2DB database (version 2018‑12) using the feature set described above. Apply the trained models to predict the stability class and formation energy of GaAsSe₄ and AlAsTe₄, each placed in both the MoS₂ and CdI₂ prototypes. Then perform DFT total‑energy calculations for these four compounds as well as for the elemental reference states, and compute the DFT formation energies per atom. Finally, compile the ML predictions, the DFT formation energies, the cross‑validated RMSE of the formation energy regression model, and the classifier’s cross‑validated AUC scores into a single JSON file named `validation_results.json` (see output contract for schema).

## Assets

- C2DB 2D Materials Database v2018-12: https://cmr.fysik.dtu.dk/c2db/c2db.html
- Atomic properties table: https://pubs.acs.org/doi/suppl/10.1021/acsami.9b14530
- XGBoost Python package: xgboost
- scikit-learn: scikit-learn
- SISSO Python implementation: https://github.com/rouyang2017/SISSO
- Open-source DFT code (Quantum ESPRESSO or GPAW): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare training data from C2DB
- Role: process
- Action: Download the C2DB v2018-12 database, filter to non-magnetic materials. Compute stability labels (low if formation energy > 0, high if formation energy < 0 and energy above convex hull < 0.2 eV/atom, medium otherwise). Compute statistical functions (average, weighted average, max, min, standard deviation) of the atomic properties listed in Table 1 and include prototype label encoding as features.
- Evidence: `/app/outputs/c2db_features_labels.csv`

### Step 2: Discover SISSO composite features
- Role: process
- Action: Using the SISSO method in a multi-task approach, generate composite nonlinear features from the primary feature set. Select the top six features that best separate stability classes across prototypes and append them to the feature set.
- Evidence: `/app/outputs/sisso_features.log`

### Step 3: Train XGBoost stability classifier
- Role: process
- Action: Train a gradient-boosted decision tree classifier (XGBoost) on the full feature set (atomic stats + SISSO features + prototype). Perform stratified 5-fold cross-validation to obtain ROC-AUC for each class and record feature importances. Save the trained model.
- Evidence: `/app/outputs/classifier_model.pkl`

### Step 4: Train SISSO regression model for formation energy (high-stability class)
- Role: process
- Action: Train a 3D SISSO regression model on the high‑stability class materials to predict formation energy. Perform 5‑fold cross‑validation to compute the RMSE. Save the model coefficients.
- Evidence: `/app/outputs/regression_model_params.json`

### Step 5: Compute ML predictions for validation compounds
- Role: process
- Action: For GaAsSe4 and AlAsTe4 in both MoS2 and CdI2 prototypes, compute the feature vectors (including SISSO features) and apply the trained XGBoost classifier to obtain the predicted stability class, and the SISSO regression model to obtain the predicted formation energy. Save these intermediate predictions.
- Evidence: `/app/outputs/ml_predictions.json`

### Step 6: Perform DFT formation energy calculations
- Role: process
- Action: For GaAsSe4 and AlAsTe4 in MoS2 and CdI2 structures, as well as for the constituent elements in their reference states, perform DFT total‑energy calculations using the PBE functional and PAW pseudopotentials with an open‑source plane‑wave code. Compute formation energies per atom as ΔH_f = (E_total − sum of elemental reference energies) / N_atoms.
- Evidence: `/app/outputs/dft_total_energies.log`

### Step 7: Compile validation results
- Role: scored (load-bearing)
- Action: Combine the ML predicted classes and formation energies from step 05 with the DFT formation energies from step 06, the regression model’s cross‑validated RMSE from step 04, and the classifier’s AUC scores from step 03 into a single JSON file according to the output schema.
- Output file: `/app/outputs/validation_results.json`
- Format: json
- Contract: A single JSON object matching the schema in the Output contract section below. It must contain a `compounds` array of exactly four objects (one per validation compound, each with string fields `name`, `prototype`, `predicted_class`, `dft_code` and numeric fields `predicted_formation_energy` and `dft_formation_energy` in eV/atom), a numeric field `regression_model_rmse` (eV/atom), and an object `classification_performance` with a string `method` and an object `test_auc` containing numeric fields `low`, `medium`, `high`.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/validation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### validation_results.json
- path: `/app/outputs/validation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the ML stability predictions, DFT formation energies, regression RMSE, and classification AUC for the validation compounds GaAsSe4 and AlAsTe4.
- schema:
  - `type`: object
  - `required`: `compounds`, `regression_model_rmse`, `classification_performance`
  - `properties`:
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `prototype`, `predicted_class`, `predicted_formation_energy`, `dft_formation_energy`, `dft_code`
        - `properties`:
          - `name`:
            - `type`: string
          - `prototype`:
            - `type`: string
          - `predicted_class`:
            - `type`: string
          - `predicted_formation_energy`:
            - `type`: number
            - `unit`: eV/atom
          - `dft_formation_energy`:
            - `type`: number
            - `unit`: eV/atom
          - `dft_code`:
            - `type`: string
          - `notes`:
            - `type`: string
    - `regression_model_rmse`:
      - `type`: number
      - `unit`: eV/atom
    - `classification_performance`:
      - `type`: object
      - `required`: `method`, `test_auc`
      - `properties`:
        - `method`:
          - `type`: string
        - `test_auc`:
          - `type`: object
          - `required`: `low`, `medium`, `high`
          - `properties`:
            - `low`:
              - `type`: number
            - `medium`:
              - `type`: number
            - `high`:
              - `type`: number
        - `notes`:
          - `type`: string

Notes: The scored artifact combines predictions and DFT results; the checker compares reported formation energies and RMSE to hidden reference values with appropriate tolerances, and verifies that predicted classes match the expected prototype-dependent stability (low for MoS2, high for CdI2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "validation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "compounds",
          "regression_model_rmse",
          "classification_performance"
        ],
        "properties": {
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "prototype",
                "predicted_class",
                "predicted_formation_energy",
                "dft_formation_energy",
                "dft_code"
              ],
              "properties": {
                "name": {
                  "type": "string"
                },
                "prototype": {
                  "type": "string"
                },
                "predicted_class": {
                  "type": "string"
                },
                "predicted_formation_energy": {
                  "type": "number",
                  "unit": "eV/atom"
                },
                "dft_formation_energy": {
                  "type": "number",
                  "unit": "eV/atom"
                },
                "dft_code": {
                  "type": "string"
                },
                "notes": {
                  "type": "string"
                }
              }
            }
          },
          "regression_model_rmse": {
            "type": "number",
            "unit": "eV/atom"
          },
          "classification_performance": {
            "type": "object",
            "required": [
              "method",
              "test_auc"
            ],
            "properties": {
              "method": {
                "type": "string"
              },
              "test_auc": {
                "type": "object",
                "required": [
                  "low",
                  "medium",
                  "high"
                ],
                "properties": {
                  "low": {
                    "type": "number"
                  },
                  "medium": {
                    "type": "number"
                  },
                  "high": {
                    "type": "number"
                  }
                }
              },
              "notes": {
                "type": "string"
              }
            }
          }
        }
      },
      "description": "JSON file containing the ML stability predictions, DFT formation energies, regression RMSE, and classification AUC for the validation compounds GaAsSe4 and AlAsTe4."
    }
  ],
  "notes": "The scored artifact combines predictions and DFT results; the checker compares reported formation energies and RMSE to hidden reference values with appropriate tolerances, and verifies that predicted classes match the expected prototype-dependent stability (low for MoS2, high for CdI2)."
}
```

## How you are scored
A hidden verifier will read your `validation_results.json` and compare its contents against reference values derived from the original paper. It checks the DFT formation energies, the predicted stability classes, the regression RMSE, and the classification AUC scores. Each quantity is compared with an appropriate tolerance or correctness criterion, and the individual scores are combined into a final reward between 0 and 1. Supplying the paper's exact numbers without executing the workflow will not achieve full credit; the reward reflects how well your computed results match the expected physical and statistical outcomes.
