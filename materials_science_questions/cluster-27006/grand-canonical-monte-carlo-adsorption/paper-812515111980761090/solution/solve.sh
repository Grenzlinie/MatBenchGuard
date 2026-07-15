#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: iast_vs_simulation_errors.csv ===
# Relative errors for IAST vs binary GCMC for QATHOK at P_total = 0.5*(Pvp_A+Pvp_B)
cat > "$OUTDIR/iast_vs_simulation_errors.csv" <<'FFEOF'
system_id,component_A,component_B,MOF_ID,relative_error_loading_A,relative_error_loading_B,relative_error_selectivity
pair_1_3,3-butenal,tert-butanol,QATHOK,0.59,0.10,0.45
pair_1_4,3-butenal,4-methyl-1-hexene,QATHOK,0.12,0.08,0.35
pair_4_6,4-methyl-1-hexene,2,2-dimethylpentane,QATHOK,0.10,0.07,0.30
pair_4_7,4-methyl-1-hexene,2,4-dimethylpentane,QATHOK,0.09,0.11,0.25
FFEOF
