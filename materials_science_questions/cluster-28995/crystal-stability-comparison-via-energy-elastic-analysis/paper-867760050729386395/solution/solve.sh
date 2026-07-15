#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: results_fixed_Yp.json ===
python3 /solution/generate_results.py fixed_yp

# === solve block: results_catalyzed.json ===
python3 /solution/generate_results.py catalyzed
