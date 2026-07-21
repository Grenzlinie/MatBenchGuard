#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: case_1_results.json ===
python3 /solution/generate_profiles.py case1 > $OUTDIR/case_1_results.json

# === solve block: case_2_results.json ===
python3 /solution/generate_profiles.py case2 > $OUTDIR/case_2_results.json

# === solve block: case_3_results.json ===
python3 /solution/generate_profiles.py case3 > $OUTDIR/case_3_results.json
