#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate_ref_csv.py

# === solve block: main_mse.csv ===
# written by /solution/generate_ref_csv.py

# === solve block: extrapolation_mse.csv ===
# written by /solution/generate_ref_csv.py

# === solve block: noise_matching_mse.csv ===
# written by /solution/generate_ref_csv.py

# === solve block: augmentation_mse.csv ===
# written by /solution/generate_ref_csv.py

# === solve finalize ===
# nothing extra
