#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_full_model.csv ===
cat > /app/outputs/step_01_full_model.csv <<'FFEOF'
c11,c12,c13,c14,c44,K
0.868,0.073,0.119,-0.183,0.74,0.358
FFEOF

# === solve block: step_02_ablation.csv ===
cat > /app/outputs/step_02_ablation.csv <<'FFEOF'
K_ablated
0.0
FFEOF
