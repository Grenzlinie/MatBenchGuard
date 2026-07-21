# Hybrid Graph Kernel for Molecular Atomization Energy Prediction

## Problem background
Predicting molecular properties from structure is a central challenge in quantum machine learning. A promising direction is to use graph-based descriptors that capture local atomic environments. This task concerns a recently proposed hybrid maximum probability path (HMPP) kernel that combines a graph contribution, based on maximum probability paths through Gaussian-weighted adjacency matrices, with a Coulomb label contribution that encodes finer geometric details. The kernel is used with kernel ridge regression (KRR) to predict atomization energies of organic molecules. The objective is to implement the HMPP kernel and evaluate its prediction accuracy on the QM7 dataset as a function of training set size.

## Approach
The HMPP kernel operates on local atomic environments defined by a cutoff radius. Within each environment, atoms carry their elemental identity as labels, and a weighted adjacency matrix is constructed by computing Gaussian overlaps between atom-centered Gaussians parametrized by covalent radii and a width parameter; an edge is added when the overlap exceeds a small threshold. A modified Floyd-Warshall algorithm then computes maximum probability paths (MPPs) between all atom pairs, each path denoted by the product of its edge weights and labeled by the sequence of atomic species along the path. Additionally, a Coulomb label vector is assigned to each atom, consisting of normalized Coulomb potential terms between the central atom and all neighbors sorted by distance. The overall kernel is a convex combination: k = (1-α) * k_MPP + α * k_Coulomb, where the MPP kernel is a sum over path pairs that match exactly in label sequence, with each pair compared via a Laplacian kernel of the path probabilities, and the Coulomb kernel is a sum over all pairs of Coulomb vectors of the two environments compared via a Laplacian kernel. KRR is then trained on atomization energies using this hybrid kernel. Hyperparameters (cutoff radius, Gaussian width, decay factors for the two Laplacian kernels, and hybridization weight α) are obtained through a grid search minimizing the RMSE on a validation set. The trained model is evaluated on held-out test molecules, and the mean absolute error (MAE) and root mean square error (RMSE) are reported in kcal/mol.

## Reproduction target
Train KRR models with the HMPP kernel to predict atomization energies of the QM7 dataset. Use the five-fold split from Rupp et al.: the first fold provides training subsets of the first N molecules for N = 100, 300, 500, and 1000; folds 2+3 serve as the validation set for hyperparameter optimization; folds 4+5 are the test set. For each training size, after finding the best hyperparameters on the validation set, train a KRR model on the training subset and predict the atomization energies for all test molecules. Report the MAE and RMSE (kcal/mol) for N = 100, 300, 500, 1000. Additionally, record the optimal hyperparameters (cutoff radius, Gaussian width, decay parameters β1, β2, and hybridization weight α).

## Assets

- QM7 dataset: https://www.quantum-machine.org/datasets/
- NumPy: numpy
- SciPy: scipy
- scikit-learn: scikit-learn

## Workflow steps

### Step 1: Prepare QM7 dataset and splits
- Role: process
- Action: Download the QM7 dataset (atomization energies and molecular geometries). Create the 5-fold split as described in Rupp et al.: use the first fold for training, folds 2+3 for validation, folds 4+5 for test. From the first fold, extract training subsets with the first N molecules for N = 100, 300, 500, 1000. Save the split indices for reproducibility.
- Evidence: `/app/outputs/split_indices.json`

### Step 2: Hyperparameter optimization for HMPP kernel
- Role: scored
- Action: Implement the HMPP kernel: construct localized graphs with Gaussian-weighted adjacency, compute maximum probability paths via a modified Floyd-Warshall algorithm, compute Coulomb label vectors, and hybrid kernel combining an MPP kernel and a Coulomb kernel. Using the validation folds (2+3), perform a grid search over the hyperparameters (cutoff radius, Gaussian width, kernel decay parameters, hybridization weight) to minimize RMSE of atomization energies. Save the best hyperparameters.
- Output file: `/app/outputs/hyperparameters.json`
- Format: json
- Contract: Object with keys: r_cut (float, Å), gamma (float, Å), beta1 (float), beta2 (float), alpha (float).
- Scoring: scored by hidden verifier

### Step 3: Train HMPP KRR models on QM7 training subsets
- Role: process
- Action: For each training size N = 100, 300, 500, 1000, using the optimal hyperparameters, compute the HMPP kernel matrix between training molecules and between training and test molecules. Train kernel ridge regression models to predict atomization energies (target values) on the training set. Store the trained model parameters (e.g., dual coefficients) for each N.
- Evidence: `/app/outputs/training_log.json`

### Step 4: Evaluate HMPP predictions and compute MAE/RMSE
- Role: scored (load-bearing)
- Action: For each training size N, apply the trained KRR model to the test set (folds 4+5) to predict atomization energies. Compute the mean absolute error (MAE) and root mean square error (RMSE) in kcal/mol between predictions and the reference energies. Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys '100', '300', '500', '1000'; each value is an object with keys 'MAE' (float, kcal/mol) and 'RMSE' (float, kcal/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hyperparameters.json`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hyperparameters.json
- path: `/app/outputs/hyperparameters.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Best hyperparameters found for the HMPP kernel; verified to contain the required numeric entries.
- schema:
  - `type`: object
  - `properties`:
    - `r_cut`:
      - `type`: number
      - `description`: cutoff radius in Å
    - `gamma`:
      - `type`: number
      - `description`: Gaussian width parameter in Å
    - `beta1`:
      - `type`: number
      - `description`: decay parameter for MPP kernel
    - `beta2`:
      - `type`: number
      - `description`: decay parameter for Coulomb kernel
    - `alpha`:
      - `type`: number
      - `description`: hybridization weight
  - `required`: `r_cut`, `gamma`, `beta1`, `beta2`, `alpha`

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Atomization energy prediction errors (MAE and RMSE) for the HMPP kernel on the QM7 test set for four training sizes. The hidden checker compares these to reference thresholds and verifies that errors decrease monotonically with training size.
- schema:
  - `type`: object
  - `properties`:
    - `100`:
      - `type`: object
      - `properties`:
        - `MAE`:
          - `type`: number
          - `description`: mean absolute error (kcal/mol)
        - `RMSE`:
          - `type`: number
          - `description`: root mean square error (kcal/mol)
      - `required`: `MAE`, `RMSE`
    - `300`:
      - `type`: object
      - `properties`:
        - `MAE`:
          - `type`: number
        - `RMSE`:
          - `type`: number
      - `required`: `MAE`, `RMSE`
    - `500`:
      - `type`: object
      - `properties`:
        - `MAE`:
          - `type`: number
        - `RMSE`:
          - `type`: number
      - `required`: `MAE`, `RMSE`
    - `1000`:
      - `type`: object
      - `properties`:
        - `MAE`:
          - `type`: number
        - `RMSE`:
          - `type`: number
      - `required`: `MAE`, `RMSE`
  - `required`: `100`, `300`, `500`, `1000`

Notes: The check for monotonic decrease is part of scoring but the thresholds themselves are hidden. Only HMPP results on the QM7 dataset are required; SOAP/GRAPE comparisons are not part of this reproduction task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hyperparameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "r_cut": {
            "type": "number",
            "description": "cutoff radius in Å"
          },
          "gamma": {
            "type": "number",
            "description": "Gaussian width parameter in Å"
          },
          "beta1": {
            "type": "number",
            "description": "decay parameter for MPP kernel"
          },
          "beta2": {
            "type": "number",
            "description": "decay parameter for Coulomb kernel"
          },
          "alpha": {
            "type": "number",
            "description": "hybridization weight"
          }
        },
        "required": [
          "r_cut",
          "gamma",
          "beta1",
          "beta2",
          "alpha"
        ]
      },
      "description": "Best hyperparameters found for the HMPP kernel; verified to contain the required numeric entries."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "100": {
            "type": "object",
            "properties": {
              "MAE": {
                "type": "number",
                "description": "mean absolute error (kcal/mol)"
              },
              "RMSE": {
                "type": "number",
                "description": "root mean square error (kcal/mol)"
              }
            },
            "required": [
              "MAE",
              "RMSE"
            ]
          },
          "300": {
            "type": "object",
            "properties": {
              "MAE": {
                "type": "number"
              },
              "RMSE": {
                "type": "number"
              }
            },
            "required": [
              "MAE",
              "RMSE"
            ]
          },
          "500": {
            "type": "object",
            "properties": {
              "MAE": {
                "type": "number"
              },
              "RMSE": {
                "type": "number"
              }
            },
            "required": [
              "MAE",
              "RMSE"
            ]
          },
          "1000": {
            "type": "object",
            "properties": {
              "MAE": {
                "type": "number"
              },
              "RMSE": {
                "type": "number"
              }
            },
            "required": [
              "MAE",
              "RMSE"
            ]
          }
        },
        "required": [
          "100",
          "300",
          "500",
          "1000"
        ]
      },
      "description": "Atomization energy prediction errors (MAE and RMSE) for the HMPP kernel on the QM7 test set for four training sizes. The hidden checker compares these to reference thresholds and verifies that errors decrease monotonically with training size."
    }
  ],
  "notes": "The check for monotonic decrease is part of scoring but the thresholds themselves are hidden. Only HMPP results on the QM7 dataset are required; SOAP/GRAPE comparisons are not part of this reproduction task."
}
```

## How you are scored
A hidden verifier independently evaluates each stage of the workflow and combines the scores into a final reward (a float between 0 and 1). The `hyperparameters.json` file is audited for the presence of the required numeric fields. The `results.json` file is the main scored artifact: the verifier compares your reported MAE and RMSE for each training size against hidden reference values; your errors must meet or beat the expected accuracy (with tolerances), and they must exhibit the required trend — namely, both MAE and RMSE must decrease strictly as the training size grows (e.g., MAE at 100 must be larger than MAE at 300, which must be larger than MAE at 500, which must be larger than MAE at 1000). The rewards are weighted to emphasize the prediction accuracy on the test set. Simply copying numbers from the literature will not pass, because the verifier checks internal consistency and the specific numerical thresholds that only a correct implementation can satisfy.
