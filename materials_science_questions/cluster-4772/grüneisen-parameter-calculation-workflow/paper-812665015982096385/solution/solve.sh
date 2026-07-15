#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: grueneisen_results.json ===
python3 /solution/write_grueneisen.py

# === solve block: trend_check.txt ===
printf 'Barite trend: M-O higher than SO4 (True)\nCelestine trend: M-O higher than SO4 (True)\n' > /app/outputs/trend_check.txt
