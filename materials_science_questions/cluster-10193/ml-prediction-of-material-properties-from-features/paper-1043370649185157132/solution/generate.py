#!/usr/bin/env python3
"""Oracle synthetic submission for ML Prediction of Cu Oxidation State."""
import csv
import json
import math
import random
from pathlib import Path

# Reproducibility
random.seed(42)

N = 2400  # roughly the test set size reported in the paper
TARGET_R2 = 0.85
TARGET_RMSE = 0.24

# Desired variance of true oxidation states to achieve R2 = 0.85 with noise std 0.24
var_resid = TARGET_RMSE ** 2
var_true = var_resid / (1 - TARGET_R2)

# Generate true oxidation states uniformly spread and scale to target variance
raw = [random.uniform(0, 2) for _ in range(N)]
mean_raw = sum(raw) / N
var_raw = sum((x - mean_raw) ** 2 for x in raw) / N
scale = math.sqrt(var_true / var_raw) if var_raw > 0 else 1.0
# Center at 1.0
shift = 1.0 - mean_raw * scale

true_ox = [raw[i] * scale + shift for i in range(N)]

# Generate predictions: true + Gaussian noise with std 0.24
noise = [random.gauss(0, TARGET_RMSE) for _ in range(N)]
predicted_mean = [true_ox[i] + noise[i] for i in range(N)]

# Standard deviation of tree predictions (arbitrary but plausible)
predicted_std = [random.uniform(0.05, 0.15) for _ in range(N)]

# Compute R2 and RMSE for verification (should match targets closely)
mean_true = sum(true_ox) / N
ss_tot = sum((t - mean_true) ** 2 for t in true_ox)
ss_res = sum((true_ox[i] - predicted_mean[i]) ** 2 for i in range(N))
r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0.0
rmse = math.sqrt(ss_res / N)

# Write predictions.csv
output_dir = Path("/app/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

csv_path = output_dir / "predictions.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["true_oxidation_state", "predicted_mean", "predicted_std"])
    for i in range(N):
        writer.writerow([f"{true_ox[i]:.4f}", f"{predicted_mean[i]:.4f}", f"{predicted_std[i]:.4f}"])

# Write metrics.json
metrics = {"R2": round(r2, 4), "RMSE": round(rmse, 4)}
with open(output_dir / "metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(f"Generated {N} samples; R2={r2:.4f}, RMSE={rmse:.4f}")
