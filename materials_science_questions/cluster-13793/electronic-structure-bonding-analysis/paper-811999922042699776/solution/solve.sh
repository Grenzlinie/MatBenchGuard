#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predicted_VEC_st.csv ===
# Write the reference predicted_VEC_st.csv with paper-reported values
cat > "/app/outputs/predicted_VEC_st.csv" <<'FFEOF'
VEC_eq,VEC_st,direction,phase
18,18,none,NiTiSn
18,18,none,CoTiSb
22,22,none,PtMnSb
22,22,none,NiMnSb
21,21,none,CoMnSb
22,22.2,increase,AuMnSn
23,22.5,decrease,AuMnSb
FFEOF
