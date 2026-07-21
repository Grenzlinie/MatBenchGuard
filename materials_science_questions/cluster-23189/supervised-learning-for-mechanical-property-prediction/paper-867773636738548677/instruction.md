# NPLIC: Neural Network Piecewise Linear Interface Construction

## Problem background
In multiphase flow simulations, volume of fluid (VOF) methods track fluid interfaces by a scalar field α. For accurate flux calculations, the interface must be reconstructed geometrically. Piecewise Linear Interface Construction (PLIC) is the most common technique: given the interface normal and the volume fraction, it computes the constant C that positions a plane to split a cell into parts with the given volume fractions. For complex mesh cells (e.g., triangles, tetrahedra), the PLIC calculation involves complex geometry and can be slow, motivating the use of data‑driven alternatives. The present task builds and evaluates a neural network that directly predicts the PLIC constant C from the normal orientation angles and volume fraction, for four common mesh types: square, cubic, triangular, and tetrahedral.

## Approach
A fully‑connected multilayer perceptron (MLP) with one hidden layer of 48 neurons and ReLU activation maps the normal‑orientation angles and volume fraction α₀ to the plane constant C. For 2D square and triangular meshes the inputs are the polar angle θ and α₀; for 3D cubic and tetrahedral meshes they are the azimuthal φ, polar θ, and α₀. Triangular and tetrahedral cells are first normalized to unit shapes via an affine transformation Q, so the network only uses the transformed normal angles and α₀. The training data are synthetic. Normal orientations are sampled as follows:
- 2D meshes (square, triangular): S_n = { [cos θ, sin θ] : θ ∈ (π / N_n) · {0, 1, ..., N_n} }, with N_n = 100.
- 3D meshes (cubic, tetrahedral): S_n = { [cos φ sin θ, sin φ sin θ, cos θ] : φ ∈ (π/(2 N_n)) · {1, 2, ..., 2 N_n}, θ ∈ (π/N_n) · {0, 1, ..., N_n} }, with N_n = 40.
Volume fractions α₀ are sampled non‑uniformly to increase resolution near 0 and 1:
S_α = {10^{-k} for k = 5, ..., 9} ∪ {10^{-4} + (m-1)/(N_α-1) · (1 - 2·10^{-4}) for m = 1, ..., N_α} ∪ {1 - 10^{-k} for k = 5, ..., 9}.
In 3D, N_α = 20; in 2D, N_α = 100.
The exact C for each (orientation, α₀) pair is computed using analytical PLIC algorithms (e.g., Scardovelli & Zaleski for rectangles, López et al. for triangles/tetrahedra). The full dataset is split into 70% training, 20% test, and 10% validation. Four separate MLPs are trained – one for each mesh type – using a mean‑squared error loss, the Adam optimizer, early stopping on validation loss, and up to 100 k training epochs. Each model is trained three times with different random seeds; the final prediction is the average over the three runs.

## Reproduction target
Implement the synthetic dataset generation for all four mesh types (square, cubic, triangular, tetrahedral) following the described discretization procedure and exact PLIC solvers. Train four separate MLPs – one per mesh type – each with 48 hidden neurons, using three random seeds. Evaluate each seed on the held‑out test set (20% of the full dataset) and compute Mean Squared Error (MSE) and Mean Absolute Error (MAE). Average these two metrics over the three seeds for each mesh type. Produce a JSON file `/app/outputs/test_metrics.json` containing the averaged MSE and MAE for each mesh type. The hidden verifier will compare your reported metrics against independently obtained reference values; the target is to achieve errors that are at least as good as those references (lower is better). No specific numerical expectation is provided in the instructions.

## Assets

- PyTorch: https://pytorch.org

## Workflow steps

### Step 1: Synthetic PLIC dataset generation
- Role: process
- Action: Generate input-output pairs (normal orientation angles, volume fraction α0 → plane constant C) for square, cubic, triangular, and tetrahedral meshes using the discretization formulas for normal orientations and volume fractions described in the method. Compute exact C via analytical PLIC algorithms (e.g., Scardovelli & Zaleski for rectangles, López et al. for triangles/tetrahedra). Output dataset sizes as evidence.
- Evidence: `/app/outputs/dataset_sizes.json`

### Step 2: NPLIC model training
- Role: process
- Action: For each mesh type, randomly split the generated dataset into 70% training, 20% testing, 10% validation. Train a separate fully-connected MLP with one hidden layer of 48 neurons, ReLU activation in hidden layer, linear output neuron, using mean-squared error loss, Adam optimizer, early stopping, max epochs, batch size as described. Train each model three times with different random seeds. Keep the final trained models for evaluation.
- Evidence: `/app/outputs/training_log.txt`

### Step 3: Test set evaluation and metrics
- Role: scored (load-bearing)
- Action: For each mesh type and each of the three training runs, compute predictions on the held-out test set (20% of the full dataset). Calculate MSE and MAE between predictions and ground truth for each run, then average these metrics over the three seeds. Write a JSON file /app/outputs/test_metrics.json containing the averaged MSE and MAE for square, cubic, triangular, and tetrahedral meshes.
- Output file: `/app/outputs/test_metrics.json`
- Format: json
- Contract: JSON object with top-level keys 'square', 'cubic', 'triangular', 'tetrahedral'. Each value is an object with numeric keys 'mse' and 'mae'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/test_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### test_metrics.json
- path: `/app/outputs/test_metrics.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Averaged test MSE and MAE for each mesh type over three random seeds. Lower values correspond to better predictive accuracy. The checker compares these numbers against paper-reported references with a tolerance factor: target ≤ reference × 1.5.
- schema:
  - `type`: object
  - `required`: `square`, `cubic`, `triangular`, `tetrahedral`
  - `properties`:
    - `square`:
      - `type`: object
      - `required`: `mse`, `mae`
      - `properties`:
        - `mse`:
          - `type`: number
        - `mae`:
          - `type`: number
    - `cubic`:
      - `type`: object
      - `required`: `mse`, `mae`
      - `properties`:
        - `mse`:
          - `type`: number
        - `mae`:
          - `type`: number
    - `triangular`:
      - `type`: object
      - `required`: `mse`, `mae`
      - `properties`:
        - `mse`:
          - `type`: number
        - `mae`:
          - `type`: number
    - `tetrahedral`:
      - `type`: object
      - `required`: `mse`, `mae`
      - `properties`:
        - `mse`:
          - `type`: number
        - `mae`:
          - `type`: number

Notes: Only the final test metrics are scored. The synthetic dataset generation and model training must be executed by the agent; no pre-made artifacts are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "test_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "square",
          "cubic",
          "triangular",
          "tetrahedral"
        ],
        "properties": {
          "square": {
            "type": "object",
            "required": [
              "mse",
              "mae"
            ],
            "properties": {
              "mse": {
                "type": "number"
              },
              "mae": {
                "type": "number"
              }
            }
          },
          "cubic": {
            "type": "object",
            "required": [
              "mse",
              "mae"
            ],
            "properties": {
              "mse": {
                "type": "number"
              },
              "mae": {
                "type": "number"
              }
            }
          },
          "triangular": {
            "type": "object",
            "required": [
              "mse",
              "mae"
            ],
            "properties": {
              "mse": {
                "type": "number"
              },
              "mae": {
                "type": "number"
              }
            }
          },
          "tetrahedral": {
            "type": "object",
            "required": [
              "mse",
              "mae"
            ],
            "properties": {
              "mse": {
                "type": "number"
              },
              "mae": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Averaged test MSE and MAE for each mesh type over three random seeds. Lower values correspond to better predictive accuracy. The checker compares these numbers against paper-reported references with a tolerance factor: target ≤ reference × 1.5."
    }
  ],
  "notes": "Only the final test metrics are scored. The synthetic dataset generation and model training must be executed by the agent; no pre-made artifacts are provided."
}
```

## How you are scored
The hidden verifier reads `/app/outputs/test_metrics.json` and compares each reported MSE and MAE (for square, cubic, triangular, tetrahedral meshes) to a hidden reference baseline. For every mesh type and metric, full credit is awarded if the reported value is less than or equal to the reference. If a value exceeds the reference, partial credit is assigned proportionally to the number of passing metrics. The verifier does not re‑run training; it only checks the numbers you report. The intermediate steps (dataset generation and model training) are not directly scored but you must produce the accompanying evidence files (`dataset_sizes.json` and `training_log.txt`). The final reward is a number between 0 and 1 that reflects how many of the eight metrics (four mesh types × two metrics) meet the threshold. There is no extra credit for exceeding the reference.
