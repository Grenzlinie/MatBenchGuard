# Bootstrap Resampling Uncertainty Quantification for MLP XANES Spectra

## Problem background
Deep neural networks can predict X-ray absorption near-edge structure (XANES) spectra from local coordination geometry, but they are often overconfident, making it crucial to quantify the uncertainty of each prediction. This task investigates the reliability of bootstrap resampling as a method for pointwise uncertainty quantification when predicting first-row transition metal K-edge XANES spectra. It evaluates whether the ensemble-derived standard deviation provides a faithful measure of prediction error by computing coverage (fraction of points falling within ±3σ of the true intensity) and the correlation between prediction error and predicted uncertainty across held-out test spectra.

## Approach
For each transition metal element (Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn), the approach is as follows. From the original training set, create 15 bootstrap-resampled training sets, each the same size as the original, by sampling with replacement. Train a multilayer perceptron (MLP) neural network on each resampled set using random weight initialization, yielding an ensemble of 15 models per element. For the held-out test set (250 randomly selected spectra per element not used in training), compute the ensemble's per-energy-point predicted mean (μ_pred) and empirical standard deviation (σ) from the 15 predictions. Then evaluate the quality of the uncertainty estimate by computing: median coverage (percentage of spectral points where |μ_pred − μ_true| ≤ 3σ), P90 (fraction of test samples with ≥90% of points within ±3σ), P80, median percentage error Δμ, Pearson correlation between per-energy-point mean squared error and σ, and Pearson correlation between per-spectrum mean squared error and σ. These metrics assess both the calibration and sharpness of the predicted uncertainties.

## Reproduction target
Evaluate the bootstrap MLP ensemble as described on the held-out test sets of all nine transition metals, and produce a single CSV file summarizing the per-element uncertainty quantification metrics. The CSV must contain columns: element, median_coverage, P90, P80, median_DeltaMu, pearson_rho_energy, pearson_rho_spectrum.

## Assets

- XANESNET Training Data: https://gitlab.com/team-xnet/training-sets
- XANESNET Code: https://gitlab.com/team-xnet/xanesnet

## Workflow steps

### Step 1: Data preparation and train/test split
- Role: process
- Action: Download the XANESNET training data. For each first-row transition metal (Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn), set aside 250 randomly selected samples as the held-out test set; use the remaining samples for training.
- Evidence: `/app/outputs/split_indices.txt`

### Step 2: Bootstrap-resampled MLP training
- Role: process
- Action: For each element, create 15 bootstrap-resampled training sets (each same size as the original training set, sampled with replacement). Train an MLP model on each resampled set using random weight initialization. Save the 15 trained models per element.
- Evidence: none

### Step 3: Ensemble prediction of held-out spectra
- Role: process
- Action: For each element, evaluate the 15 trained MLP models on the 250 held-out samples. Compute per-energy-point predicted mean (μ_predicted) and empirical standard deviation (σ) from the ensemble of 15 predictions.
- Evidence: `/app/outputs/predictions.npy`

### Step 4: Compute uncertainty quantification metrics
- Role: scored (load-bearing)
- Action: For each element, using the true held-out spectra and the predicted μ, σ, compute the following metrics and write them to the CSV: median coverage (percentage of spectral points where |μ_predicted - μ_true| ≤ 3σ), P90 (fraction of held-out samples with ≥90% points within ±3σ), P80 (fraction with ≥80% within ±3σ), median percentage error Δμ (median over held-out spectra of the mean percentage error), Pearson correlation between per-energy-point MSE and σ (ρ_energy), and Pearson correlation between per-spectrum MSE and σ (ρ_spectrum). Output one row per element.
- Output file: `/app/outputs/metrics_summary.csv`
- Format: csv
- Contract: element: string; median_coverage: float; P90: float; P80: float; median_DeltaMu: float; pearson_rho_energy: float; pearson_rho_spectrum: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/metrics_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### metrics_summary.csv
- path: `/app/outputs/metrics_summary.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Summary of per-element uncertainty quantification metrics computed from the bootstrap MLP ensemble.
- schema:
  - `type`: table
  - `required_columns`: `element`, `median_coverage`, `P90`, `P80`, `median_DeltaMu`, `pearson_rho_energy`, `pearson_rho_spectrum`
  - `description`: Each row corresponds to one element (Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn). All metric columns are floating-point numbers.

Notes: All metrics are scored directionally: higher median_coverage, P90, P80, pearson_rho_energy, and pearson_rho_spectrum are better; lower median_DeltaMu is better. The hidden checker compares each metric against toleranced gold values and assigns full credit when the direction meets or exceeds the threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "metrics_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "median_coverage",
          "P90",
          "P80",
          "median_DeltaMu",
          "pearson_rho_energy",
          "pearson_rho_spectrum"
        ],
        "description": "Each row corresponds to one element (Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn). All metric columns are floating-point numbers."
      },
      "description": "Summary of per-element uncertainty quantification metrics computed from the bootstrap MLP ensemble."
    }
  ],
  "notes": "All metrics are scored directionally: higher median_coverage, P90, P80, pearson_rho_energy, and pearson_rho_spectrum are better; lower median_DeltaMu is better. The hidden checker compares each metric against toleranced gold values and assigns full credit when the direction meets or exceeds the threshold."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that independently compares each metric in your CSV against expected reference values. For metrics where higher is better (median_coverage, P90, P80, pearson_rho_energy, pearson_rho_spectrum), meeting or exceeding the reference earns full credit; for median_DeltaMu, lower is better, and meeting or falling below the reference earns full credit. The final reward is a weighted combination of the per-element per-metric scores. Simply copying numbers from a known reference (if accessible) is not sufficient; the verifier assesses the output of your computed workflow.
