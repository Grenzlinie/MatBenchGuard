#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: velocity_highT.csv ===
python3 /solution/generate_csv.py --beta 0.92 --output /app/outputs/velocity_highT.csv --A 1.0 --tmin 0.1 --tmax 1000 --npoints 200

# === solve block: velocity_lowT.csv ===
python3 /solution/generate_csv.py --beta 1.0 --output /app/outputs/velocity_lowT.csv --A 1.0 --tmin 0.1 --tmax 1000 --npoints 200

# === solve block: beta_results.json ===
python3 /solution/write_beta_json.py --beta_highT 0.92 --beta_lowT 1.0 --output /app/outputs/beta_results.json
