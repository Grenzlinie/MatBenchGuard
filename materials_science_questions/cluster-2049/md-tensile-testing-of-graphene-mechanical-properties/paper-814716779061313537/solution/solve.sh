#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_const_strain_check.txt ===
cat > /app/outputs/step_01_const_strain_check.txt <<'FFEOF'
Σ vanishes: True
FFEOF

# === solve block: step_02_pseudomag_field.csv ===
python3 /solution/compute_bz.py
