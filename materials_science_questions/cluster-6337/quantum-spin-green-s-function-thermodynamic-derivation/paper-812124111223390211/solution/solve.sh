#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/write_results.py

# === solve block: chi_qzz_values.csv ===
echo 'chi_qzz_values.csv written'
