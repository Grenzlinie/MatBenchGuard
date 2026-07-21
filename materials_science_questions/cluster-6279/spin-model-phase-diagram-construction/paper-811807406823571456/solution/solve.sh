#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: xi_over_L_vs_T.csv ===
python3 /solution/generate.py xi_over_L_vs_T.csv

# === solve block: q2_vs_N.csv ===
python3 /solution/generate.py q2_vs_N.csv

# === solve block: summary_results.json ===
python3 /solution/generate.py summary_results.json
