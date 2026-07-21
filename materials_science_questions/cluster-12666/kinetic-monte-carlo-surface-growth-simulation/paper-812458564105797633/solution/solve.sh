#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: Sk_curves.csv ===
python3 /solution/helper.py Sk_curves /app/outputs/Sk_curves.csv

# === solve block: alpha_distributions.csv ===
python3 /solution/helper.py alpha /app/outputs/alpha_distributions.csv

# === solve block: analytical_relation.csv ===
python3 /solution/helper.py rel /app/outputs/analytical_relation.csv
