# Cell Traction Force Prediction from Fluorescence Microscopy Images

## Problem background
Traction Force Microscopy (TFM) traditionally requires imaging fluorescent beads in gels to compute cell traction forces. However, bead displacement calculation is non-trivial and requires dedicated fluorescent channels. This task explores a deep learning method that predicts per-pixel traction forces directly from a single fluorescence image of the cell, bypassing bead imaging and reconstruction. The method uses a Bayesian neural network that also outputs uncertainty estimates. The key result is the pixel‑wise Mean Absolute Error (MAE) between predicted forces and ground‑truth forces on a held‑out test cell.

## Approach
The core idea is to train a modified Tiramisu dense U‑Net architecture to map a cell fluorescence image to two outputs: log‑transformed force mean and variance. The network uses dropout layers kept active during inference to model epistemic uncertainty. Training minimizes a Kullback–Leibler divergence loss that corresponds to maximum likelihood estimation under a log‑normal distribution. The dataset consists of time‑lapse sequences of HT1080 fibrosarcoma cells, each with paired fluorescence images and ground‑truth traction force maps obtained from classical TFM (provided). The data is split into training (12 cells), validation (11 cells), and one held‑out test cell. Preprocessing includes applying a cosine‑tapered window to force maps to suppress boundary artefacts, log‑transforming images, and augmenting training pairs with spatial transformations and salt noise.

## Reproduction target
Using the provided Zenodo HT1080 TFM dataset (DOI: 10.5281/zenodo.3484797), implement the network architecture and training procedure as described in the workflow steps. Evaluate on the held‑out test cell (181 frames): for each frame, predict the force map and compute the MAE against the ground‑truth force map (with Tukey mask applied). Store per‑frame MAE values and the overall mean MAE in a JSON file `/app/outputs/results.json` with shape: `{"per_frame_mae": [float, ...] (length 181), "overall_mean_mae": float}`.

## Assets

- HT1080 Traction Force Microscopy Dataset: https://zenodo.org/records/3484797
- InSilicoTFM reference implementation: https://github.com/wahlby-lab/InSilicoTFM

## Workflow steps

### Step 1: Data preprocessing and augmentation
- Role: process
- Action: Preprocess the raw dataset images and force maps: apply a 10% cosine-tapered (Tukey) window mask to force maps; extract cell regions via thresholding and morphological operations; apply random spatial augmentations (horizontal/vertical flips, rotations, random crops to 256×256) and salt noise; then log-transform the images with ln(max(1, x)). Generate training and validation batches.
- Evidence: `/app/outputs/preprocessing_log.txt`

### Step 2: Model training
- Role: process
- Action: Implement the modified Tiramisu dense U-Net architecture with two output heads (linear activation for log-force mean, softplus² for log-variance). Train using the KL divergence loss, Adam optimizer with L2 weight decay 1e-4, gradient clipping (max L2 norm 1.0), dropout rate 20% kept active during training and inference, batch size 8, for 200 epochs (50 steps per epoch). Use the training set and monitor on the validation set. Save the trained model weights.
- Evidence: `/app/outputs/model_checkpoint.pt`

### Step 3: Evaluation and MAE calculation
- Role: scored (load-bearing)
- Action: Load the trained model and apply it to the test cell images (181 frames) using a single forward pass (T=1, no Monte Carlo dropout sampling). Compute per-pixel predicted force using the formula exp(μ + σ²/2), where μ and σ² are the two output channels from the network (log-force mean and variance). For each frame, compute the mean absolute error (MAE) between the predicted force map and the ground-truth force map (with Tukey mask applied). Output a JSON file containing the per-frame MAE list and the overall mean MAE across all frames.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: { "per_frame_mae": [float, ...] (length 181, one per test-cell frame), "overall_mean_mae": float }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored artifact containing the per-frame and overall Mean Absolute Error of force predictions on the test cell. The overall mean MAE is compared to the paper-reported target; lower is better.
- schema:
  - `type`: object
  - `properties`:
    - `per_frame_mae`:
      - `type`: array
      - `minItems`: 181
      - `maxItems`: 181
      - `items`:
        - `type`: number
        - `minimum`: 0
    - `overall_mean_mae`:
      - `type`: number
      - `minimum`: 0
  - `required`: `per_frame_mae`, `overall_mean_mae`

Notes: The per_frame_mae list must contain exactly 181 non-negative floats. The overall_mean_mae is the arithmetic mean of those values. Scoring uses a threshold_or_better policy: if the agent's overall_mean_mae is at or below the hidden gold, full reward is given; above it, reward decays linearly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "per_frame_mae": {
            "type": "array",
            "minItems": 181,
            "maxItems": 181,
            "items": {
              "type": "number",
              "minimum": 0
            }
          },
          "overall_mean_mae": {
            "type": "number",
            "minimum": 0
          }
        },
        "required": [
          "per_frame_mae",
          "overall_mean_mae"
        ]
      },
      "description": "Scored artifact containing the per-frame and overall Mean Absolute Error of force predictions on the test cell. The overall mean MAE is compared to the paper-reported target; lower is better."
    }
  ],
  "notes": "The per_frame_mae list must contain exactly 181 non-negative floats. The overall_mean_mae is the arithmetic mean of those values. Scoring uses a threshold_or_better policy: if the agent's overall_mean_mae is at or below the hidden gold, full reward is given; above it, reward decays linearly."
}
```

## How you are scored
A hidden verifier loads your `results.json` and checks that `per_frame_mae` is a list of exactly 181 non‑negative numbers and that `overall_mean_mae` is a non‑negative number. The verifier then compares your `overall_mean_mae` to a hidden reference threshold using a threshold‑or‑better policy: lower MAE is better. If your overall mean MAE is at or below the threshold, you receive full reward (1.0); if it is above the threshold, the reward decays linearly to zero based on how far above it is. The verifier does not use any cutoff other than the threshold. Note that the paper’s reported MAE serves only as the hidden oracle target; you do not need to guess it — reproduce the workflow genuinely.
