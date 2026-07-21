#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetization_curves.csv ===
cat > /app/outputs/magnetization_curves.csv <<'FFEOF'
U,delta_G_m0.35,delta_G_m0.30
FFEOF

# === solve block: phase_diagram.csv ===
cat > /app/outputs/phase_diagram.csv <<'FFEOF'
J_over_U,U_c
FFEOF

# === solve finalize ===
python3 /solution/generate.py
