#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: results_step_03.csv ===
cat > "$OUTDIR/results_step_03.csv" <<'FFEOF'
U_t,m_sQ,E_diff
7,0.0,-0.01
8,0.05,-0.04
9,0.20,-0.08
10,0.40,-0.15
FFEOF
