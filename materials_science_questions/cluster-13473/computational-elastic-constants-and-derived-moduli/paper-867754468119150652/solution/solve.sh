#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_C_r_data.csv ===
python3 /solution/generate_csvs.py

# === solve block: step_02_ell_c.csv ===
cat > /app/outputs/step_02_ell_c.csv <<'EOF'
delta_z,ell_c
0.05,0.983869
0.2,0.491934
0.8,0.245967
EOF
