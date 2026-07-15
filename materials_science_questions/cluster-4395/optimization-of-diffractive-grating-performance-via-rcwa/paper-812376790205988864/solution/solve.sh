#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: filter_alpha_rp.csv ===
python3 /solution/generate.py filter_alpha_rp

# === solve block: resonator_alpha_vs_Lambda.csv ===
python3 /solution/generate.py resonator_alpha_vs_Lambda

# === solve block: resonator_Rp_vs_lambda.csv ===
python3 /solution/generate.py resonator_Rp_vs_lambda

# === solve block: brillouin_diagram.csv ===
python3 /solution/generate.py brillouin_diagram
