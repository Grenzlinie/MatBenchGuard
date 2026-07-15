# Screening Bond-Orientational Fingerprints for Atomic Charge Prediction

## Problem background
A representation of atomic environments that combines atomic numbers and bond-orientational order parameters is proposed to encode both chemical species and structural information. A family of 504 candidate fingerprints is systematically designed and applied to the molecules in the QM9 dataset, which contains 133 885 small organic molecules made of carbon, hydrogen, oxygen, nitrogen, and fluorine. The central problem is to determine whether a compact subset of these fingerprints can accurately predict Open Babel atomic charges and molecular dipole moments, and to evaluate the robustness of such predictions across different molecular geometries. The reproduction effort will screen the fingerprints via supervised machine learning, rank them by importance, and evaluate the regression performance of the selected top‑60 fingerprints.

## Approach
For every atom in a molecule, neighbour sets are built at four cutoff radii (1.50, 1.75, 2.00, and 2.50 Å). The 18 implant functions F are defined as follows (N is the number of neighbors in the neighbor set, a_j is the atomic number of neighbor j, r_ij is the distance, and all sums run over neighbors k ∈ N_b(r_c,i)):

F1 = 1
F2 = 1/N
F3 = r_ij
F4 = r_ij^{-1} / Σ_k r_ik^{-1}
F5 = a_j
F6 = a_j / Σ_k a_k
F7 = a_j r_ij^{-1}
F8 = a_j r_ij^{-1} / Σ_k a_k r_ik^{-1}
F9 = a_j^{1.5} r_ij^{-1}
F10 = a_j^{1.5} r_ij^{-1} / Σ_k a_j^{1.5} r_ik^{-1}
F11 = a_j^{1.5} r_ij
F12 = a_j^{1.5} r_ij / Σ_k a_j^{1.5} r_ik
F13 = a_j exp[-4(r_ij - 1.5)^2]
F14 = (a_j exp[-4(r_ij - 1.5)^2]) / Σ_k a_k exp[-4(r_ik - 1.5)^2]
F15 = a_j exp[-4(r_ij - 2.0)^2]
F16 = (a_j exp[-4(r_ij - 2.0)^2]) / Σ_k a_k exp[-4(r_ik - 2.0)^2]
F17 = a_j exp[-4(r_ij - 2.5)^2]
F18 = (a_j exp[-4(r_ij - 2.5)^2]) / Σ_k a_k exp[-4(r_ik - 2.5)^2]

These implant functions are embedded into bond-orientational order parameters via spherical harmonics:

q_{lm}(r_c, F, i) = Σ_{j ∈ N_b(r_c,i)} F(a_j, r_ij, r_c) Y_{lm}(r_ij)

Q_l(r_c, F, i) = √[ (4π/(2l+1)) Σ_{m=-l}^{l} |q_{lm}|^2 ]

with the degree l ∈ {4, 6, 8, 12, 15, 18, 20}. Each combination of cutoff r_c (1.50, 1.75, 2.00, 2.50 Å), implant function F, and degree l yields one fingerprint component, producing 504 fingerprint components per atom. Appending the atomic number a_i gives a 505‑element vector d_i per atom. Appending the atomic number gives a 505‑element vector per atom, and the collection of all atomic vectors forms the global descriptor matrix D. A random‑forest regressor (default scikit‑learn hyperparameters) is trained to predict Open Babel GAFF atomic charges using D. Feature importances are extracted from the trained forest, and the 504 fingerprint components are ranked. The top 60 components are selected for subsequent regression. The workflow proceeds in three evaluation regimes: (1) train and evaluate on GAFF‑optimized geometries (charge prediction and dipole‑moment reconstruction); (2) train and evaluate on DFT‑optimized geometries from QM9 (robustness); (3) transfer prediction where the model trained on GAFF data is used to predict charges for DFT geometries. All evaluations use five‑fold cross‑validation and report per‑element (H, C, N, O, F) and total R², MAE, MSE; molecular dipole‑moment R² is reported for regimes (1) and (2).

## Reproduction target
Implement the full fingerprint computation for all molecules in the QM9 dataset. Use Open Babel to assign GAFF atomic charges and, where required, GAFF‑optimized geometries. Train a random‑forest regressor to predict these charges, rank all 504 fingerprint components by importance, and select the top 60. Evaluate regression performance on GAFF‑optimized geometries: report per‑element (H, C, N, O, F) and total R², MAE, MSE, and the molecular dipole‑moment R². Then, using the DFT‑optimized geometries from QM9, assign GAFF charges (no geometry optimization) and evaluate the same set of 60 fingerprints by training and testing on these DFT geometries; report the same metrics (including dipole R²). Finally, take the random‑forest model trained on GAFF data and predict charges for the DFT geometries; report per‑element and total R², MAE, MSE (dipole‑moment R² is not required for this transfer scenario). Produce the following scored artifacts: the list of top‑60 fingerprints, the regression metrics for GAFF structures, the regression metrics for DFT structures, and the transfer‑prediction metrics.

## Assets

- QM9 dataset: http://quantum-machine.org/datasets/
- Open Babel: https://openbabel.org/
- scikit‑learn: https://scikit-learn.org/
- numpy: numpy

## Workflow steps

### Step 1: Generate GAFF geometries and charges for QM9
- Role: process
- Action: Use Open Babel to generate GAFF‑optimized molecular geometries and assign per‑atom GAFF atomic charges for every molecule in the QM9 dataset.
- Evidence: `/app/outputs/gaff_generation.log`

### Step 2: Compute full 505‑dimensional descriptors from GAFF geometries
- Role: process
- Action: For each atom in the GAFF geometries, compute neighbor sets N_b(r_c,i) for cutoffs r_c ∈ {1.50,1.75,2.00,2.50} Å. Evaluate the 18 implant functions F1–F18 (defined above) and compute the bond-orientational order parameters Q_l(r_c,F,i) using the spherical-harmonic definitions given above for l ∈ {4,6,8,12,15,18,20}. Append the atomic number a_i to form a 505‑element vector d_i; assemble the global descriptor matrix D_gaff.
- Evidence: `/app/outputs/descriptor_shape.txt`

### Step 3: Random forest training on full descriptors and importance ranking
- Role: process
- Action: Train a RandomForestRegressor on D_gaff and the GAFF charges using scikit‑learn with default parameters. Perform fivefold cross‑validation and extract feature importances for the 504 fingerprint components (excluding the atomic number feature).
- Evidence: `/app/outputs/full_feature_importances.csv`

### Step 4: Select top 60 fingerprints
- Role: scored
- Action: Sort the fingerprint components by importance (highest first), take the top 60, and write their identifiers (l, r_c (Å), F_name) and importance values to a CSV file.
- Output file: `/app/outputs/top_60_fingerprints.csv`
- Format: csv
- Contract: CSV with columns: rank (int), l (int), rc (float, Å), F_name (string), importance (float). One row per fingerprint, sorted by rank ascending.
- Scoring: scored by hidden verifier

### Step 5: Evaluate charge and dipole moment prediction on GAFF geometries
- Role: scored
- Action: Using only the top 60 fingerprint features plus the atomic number, train a new RandomForestRegressor on D_gaff with fivefold cross‑validation. Predict charges for all atoms; compute per‑element (H, C, N, O, F) and total R², MAE, MSE. Also compute molecular dipole moments from the predicted charges and GAFF atomic positions, and calculate the R² between those dipole moments and the Open Babel dipole moments.
- Output file: `/app/outputs/regression_results_gaff.json`
- Format: json
- Contract: JSON object with keys: 'atom_types' (object with keys H, C, N, O, F, each an object with keys R2, MAE, MSE), 'total' (object with R2, MAE, MSE), 'dipole_moment_R2' (float).
- Scoring: scored by hidden verifier

### Step 6: Compute GAFF charges for DFT geometries
- Role: process
- Action: Use Open Babel to assign GAFF atomic charges to the DFT‑optimized geometries from QM9 (no geometry optimization, only charge assignment).
- Evidence: `/app/outputs/dft_charges_count.txt`

### Step 7: Compute 60‑fingerprint descriptors from DFT geometries
- Role: process
- Action: For each atom in the DFT geometries, compute the same 60 selected fingerprint components (using the definitions from s4) plus the atomic number, forming the descriptor matrix D_dft.
- Evidence: `/app/outputs/dft_descriptor_shape.txt`

### Step 8: Robustness evaluation on DFT geometries (train on DFT, evaluate on DFT)
- Role: scored (load-bearing)
- Action: Using the top 60 features, train a new RandomForestRegressor on D_dft and the GAFF charges assigned to DFT geometries, with fivefold cross‑validation. Predict charges, compute per‑element and total R², MAE, MSE, and the molecular dipole moment R².
- Output file: `/app/outputs/regression_results_dft.json`
- Format: json
- Contract: Same structure as regression_results_gaff.json.
- Scoring: scored by hidden verifier

### Step 9: Transfer prediction (train on GAFF, predict on DFT)
- Role: scored (load-bearing)
- Action: Take the random forest model trained on GAFF data (from step s5), predict atomic charges for the DFT descriptor matrix D_dft, and compare with the GAFF charges assigned to the DFT geometries. Compute per‑element and total R², MAE, MSE (dipole moment is not reported for this transfer scenario).
- Output file: `/app/outputs/transfer_prediction_results.json`
- Format: json
- Contract: Same structure as regression_results_gaff.json, but without the 'dipole_moment_R2' key.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/top_60_fingerprints.csv`
- `/app/outputs/regression_results_gaff.json`
- `/app/outputs/regression_results_dft.json`
- `/app/outputs/transfer_prediction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### top_60_fingerprints.csv
- path: `/app/outputs/top_60_fingerprints.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: List of the top 60 fingerprints identified by the screening, with their importance scores.
- schema:
  - `type`: table
  - `required_columns`: `rank`, `l`, `rc`, `F_name`, `importance`
  - `units`:
    - `rc`: Å

### regression_results_gaff.json
- path: `/app/outputs/regression_results_gaff.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Regression metrics for charge prediction and dipole moment reconstruction on GAFF-optimized geometries.
- schema:
  - `type`: object
  - `required`: `atom_types`, `total`, `dipole_moment_R2`
  - `items`:
    - `atom_types`:
      - `type`: object
      - `required`: `H`, `C`, `N`, `O`, `F`
      - `items`:
        - `R2`: float
        - `MAE`: float
        - `MSE`: float
    - `total`:
      - `R2`: float
      - `MAE`: float
      - `MSE`: float
    - `dipole_moment_R2`: float

### regression_results_dft.json
- path: `/app/outputs/regression_results_dft.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Regression metrics for charge prediction and dipole moment reconstruction on DFT geometries (trained and evaluated on DFT).
- schema:
  - `type`: object
  - `required`: `atom_types`, `total`, `dipole_moment_R2`
  - `items`:
    - `atom_types`:
      - `type`: object
      - `required`: `H`, `C`, `N`, `O`, `F`
      - `items`:
        - `R2`: float
        - `MAE`: float
        - `MSE`: float
    - `total`:
      - `R2`: float
      - `MAE`: float
      - `MSE`: float
    - `dipole_moment_R2`: float

### transfer_prediction_results.json
- path: `/app/outputs/transfer_prediction_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Regression metrics for transfer prediction: model trained on GAFF data, evaluated on DFT geometries (dipole moment not included).
- schema:
  - `type`: object
  - `required`: `atom_types`, `total`
  - `items`:
    - `atom_types`:
      - `type`: object
      - `required`: `H`, `C`, `N`, `O`, `F`
      - `items`:
        - `R2`: float
        - `MAE`: float
        - `MSE`: float
    - `total`:
      - `R2`: float
      - `MAE`: float
      - `MSE`: float

Notes: All scoring is result-level compare against the paper's reported values. For R², MAE, MSE the policy is threshold_or_better (meeting or exceeding paper performance earns full credit). The top‑60 fingerprint list is scored by reference match with tolerances on importance values and exact identifier matching.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "top_60_fingerprints.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rank",
          "l",
          "rc",
          "F_name",
          "importance"
        ],
        "units": {
          "rc": "Å"
        }
      },
      "description": "List of the top 60 fingerprints identified by the screening, with their importance scores."
    },
    {
      "file": "regression_results_gaff.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "atom_types",
          "total",
          "dipole_moment_R2"
        ],
        "items": {
          "atom_types": {
            "type": "object",
            "required": [
              "H",
              "C",
              "N",
              "O",
              "F"
            ],
            "items": {
              "R2": "float",
              "MAE": "float",
              "MSE": "float"
            }
          },
          "total": {
            "R2": "float",
            "MAE": "float",
            "MSE": "float"
          },
          "dipole_moment_R2": "float"
        }
      },
      "description": "Regression metrics for charge prediction and dipole moment reconstruction on GAFF-optimized geometries."
    },
    {
      "file": "regression_results_dft.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "atom_types",
          "total",
          "dipole_moment_R2"
        ],
        "items": {
          "atom_types": {
            "type": "object",
            "required": [
              "H",
              "C",
              "N",
              "O",
              "F"
            ],
            "items": {
              "R2": "float",
              "MAE": "float",
              "MSE": "float"
            }
          },
          "total": {
            "R2": "float",
            "MAE": "float",
            "MSE": "float"
          },
          "dipole_moment_R2": "float"
        }
      },
      "description": "Regression metrics for charge prediction and dipole moment reconstruction on DFT geometries (trained and evaluated on DFT)."
    },
    {
      "file": "transfer_prediction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "atom_types",
          "total"
        ],
        "items": {
          "atom_types": {
            "type": "object",
            "required": [
              "H",
              "C",
              "N",
              "O",
              "F"
            ],
            "items": {
              "R2": "float",
              "MAE": "float",
              "MSE": "float"
            }
          },
          "total": {
            "R2": "float",
            "MAE": "float",
            "MSE": "float"
          }
        }
      },
      "description": "Regression metrics for transfer prediction: model trained on GAFF data, evaluated on DFT geometries (dipole moment not included)."
    }
  ],
  "notes": "All scoring is result-level compare against the paper's reported values. For R², MAE, MSE the policy is threshold_or_better (meeting or exceeding paper performance earns full credit). The top‑60 fingerprint list is scored by reference match with tolerances on importance values and exact identifier matching."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact: the top‑60 fingerprint list, the regression results for GAFF geometries, the regression results for DFT geometries, and the transfer‑prediction results. For each artifact the verifier compares the reported quantities to a hidden reference derived from the original study; the comparison uses threshold‑or‑better semantics for directional metrics (where higher R² is better, and lower MAE/MSE are better) and reference matching for the fingerprint identifiers and importance values. Meeting or exceeding the reference performance earns full credit for that artifact; performing worse reduces the score. The final reward is a weighted combination of the individual artifact scores. Your solution must produce exactly the output files and schemas described in the workflow steps; the verifier will not accept deviations.
