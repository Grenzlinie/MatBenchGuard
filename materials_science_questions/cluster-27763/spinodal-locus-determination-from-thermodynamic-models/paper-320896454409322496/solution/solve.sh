#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_Ds_values.csv ===
cat > /app/outputs/step_01_Ds_values.csv <<'FFEOF'
temperature,D_s_VACF,D_s_MSD,D_c_Ds_char_func
85,1.91,1.91,0.138
100,3.62,3.59,0.182
FFEOF

# === solve block: step_02_spinodal_binodal.txt ===
cat > /app/outputs/step_02_spinodal_binodal.txt <<'FFEOF'
60
80
FFEOF
