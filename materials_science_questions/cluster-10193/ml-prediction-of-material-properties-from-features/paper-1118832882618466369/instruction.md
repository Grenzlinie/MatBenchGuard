# Wavelet-Enhanced Residual Network for Multi-Target Thermoelectric Property Prediction from Composition

## Problem background
Doping significantly enhances thermoelectric performance, but the relationship between chemical composition and properties such as the Seebeck coefficient (S), electrical conductivity (σ), power factor (PF), thermal conductivity (κ), and figure of merit (zT) is highly nonlinear and difficult to predict. Traditional experimental trial-and-error and first-principles calculations are time-consuming and costly. Machine learning offers a route to accelerate discovery by predicting these properties directly from chemical formulas. A key challenge is that subtle changes in dopant type and concentration can cause abrupt changes in thermoelectric behavior, requiring models that capture both inter-system differences and intra-system variations with high accuracy.

## Approach
This work presents WaveTENet, a deep residual network that simultaneously predicts five thermoelectric transport properties from the chemical formula of a doped compound. The pipeline operates in three stages. First, a multi-source feature representation is built: the System-Identified Material Descriptor (SIMD) captures compositional and temperature information along with nearest-cluster statistics; Magpie descriptors add statistical summaries of elemental physical and chemical properties. These two descriptor sets are concatenated and treated as a discrete signal. A single-level Haar wavelet transform is applied, and the resulting approximation and detail coefficients are concatenated with the original features to amplify subtle compositional differences. The enhanced feature vector is min‑max normalized. Second, the WaveTENet architecture processes this feature vector through an input block (linear layer, batch normalization, ReLU), six stacked residual blocks (each containing three linear-BN-ReLU-dropout modules with skip connections), and an output block (BN followed by a linear head) to predict all five targets simultaneously. Training uses mean squared error loss with L₂ regularization, applying target‑specific scaling (σ × 10⁻³, PF × 10⁵) to stabilize training. Third, model performance is assessed via synchronized 10‑fold cross‑validation on the doped subset of the ESTM dataset; the overall R² (coefficient of determination) is computed for each property from the aggregated predictions. Baselines compared include DopNet, CatBoost, and a standard MLP, all trained on the same features without wavelet augmentation, to contextualise the model's predictive power.

## Reproduction target
Train WaveTENet from scratch on the ESTM dataset (doped compounds only) using the described feature‑construction pipeline. Perform a 10‑fold cross‑validation and compute the overall R² score for each of the five target properties: S, σ, PF, κ, and zT. Save the five R² values as a JSON file. The result must reflect the model's predictive accuracy on the doped ESTM data when following the exact feature preprocessing (SIMD + Magpie + Haar wavelet + min‑max normalization) and network architecture detailed in the workflow steps.

## Assets

- ESTM dataset (doped subset): https://github.com/KRICT-DATA/SIMD
- SIMD descriptor generation code: https://github.com/KRICT-DATA/SIMD
- Magpie descriptor library: pymatgen or matminer
- Deep learning framework PyTorch: pytorch
- PyWavelets: PyWavelets
- WaveTENet reference implementation: https://github.com/FlorianTseng/WaveTENet

## Workflow steps

### Step 1: Data preparation and wavelet-enhanced feature construction
- Role: process
- Action: Fetch the ESTM dataset and filter to doped compounds only. Compute SIMD and Magpie descriptors for each composition. Concatenate them, apply a single-level Haar wavelet transform, and concatenate the approximation and detail coefficients with the original features. Apply min-max normalization to obtain the input matrix X. Extract target vectors for S, σ (scaled by 10⁻³), PF (scaled by 10⁵), κ, and zT, keeping the original unscaled values for evaluation.
- Evidence: `/app/outputs/features_and_targets.npy`

### Step 2: WaveTENet model training and 10-fold cross-validation
- Role: process
- Action: Implement the WaveTENet architecture (input block, six stacked residual blocks each containing three Linear-BN-ReLU-Dropout modules with skip connections, output block with BN and linear head) to simultaneously predict S, σ, PF, κ, zT. Train the model on the ESTM training data using mean squared error loss with L2 weight decay and the prescribed target scaling. Perform a synchronized 10-fold cross-validation (identical splits for all five targets). Collect all cross-validated predictions.
- Evidence: `/app/outputs/cv_predictions.npz`

### Step 3: Report overall cross-validated R² scores
- Role: scored (load-bearing)
- Action: Compute the overall R² (coefficient of determination) for each property from the aggregated cross-validated predictions and the true values. Save the results as a JSON file containing the five R² values.
- Output file: `/app/outputs/r2_results.json`
- Format: json
- Contract: {"S": <R2_float>, "sigma": <R2_float>, "PF": <R2_float>, "kappa": <R2_float>, "zT": <R2_float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/r2_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### r2_results.json
- path: `/app/outputs/r2_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The coefficient of determination (R²) for each of the five thermoelectric properties evaluated via 10-fold cross-validation on the doped ESTM dataset.
- schema:
  - `type`: object
  - `required`: `S`, `sigma`, `PF`, `kappa`, `zT`
  - `properties`:
    - `S`:
      - `type`: number
    - `sigma`:
      - `type`: number
    - `PF`:
      - `type`: number
    - `kappa`:
      - `type`: number
    - `zT`:
      - `type`: number
  - `description`: Five keys, each mapping to a floating-point R² value computed over the 10-fold cross-validation.

Notes: The agent must report R² values for all five properties. The model training step must reproduce WaveTENet as described; the process evidence files (features_and_targets.npy, cv_predictions.npz) are required to ensure the pipeline was executed even though only the final JSON is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "r2_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "S",
          "sigma",
          "PF",
          "kappa",
          "zT"
        ],
        "properties": {
          "S": {
            "type": "number"
          },
          "sigma": {
            "type": "number"
          },
          "PF": {
            "type": "number"
          },
          "kappa": {
            "type": "number"
          },
          "zT": {
            "type": "number"
          }
        },
        "description": "Five keys, each mapping to a floating-point R² value computed over the 10-fold cross-validation."
      },
      "description": "The coefficient of determination (R²) for each of the five thermoelectric properties evaluated via 10-fold cross-validation on the doped ESTM dataset."
    }
  ],
  "notes": "The agent must report R² values for all five properties. The model training step must reproduce WaveTENet as described; the process evidence files (features_and_targets.npy, cv_predictions.npz) are required to ensure the pipeline was executed even though only the final JSON is scored."
}
```

## How you are scored
A hidden verifier evaluates each workflow stage's output by comparing the reported values against thresholds derived from the original study. For the scored R² results, the verifier checks that each property's reported R² meets or exceeds a hidden performance threshold; the closer the result is to the original finding (or better), the higher the reward. The verifier also confirms that intermediate process evidence (features_and_targets.npy, cv_predictions.npz) demonstrates that the full pipeline was executed. The final reward is a weighted combination of the per‑property scores, with the main scored artifact (r2_results.json) carrying the largest weight. No single number alone qualifies for full credit—the complete end‑to‑end workflow must be faithfully executed to produce the final cross‑validated metrics.
