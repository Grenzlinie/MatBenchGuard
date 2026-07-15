#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: cp_trend.csv ===
cat > "$OUTDIR/cp_trend.csv" <<'EOF'
system,T_Tm,Cp_kB
Al,1.0,3.0
Al,0.9,3.1
Al,0.8,3.2
Al,0.7,3.4
Al,0.6,3.6
Al,0.5,3.9
Al,0.4,4.2
Al,0.3,4.6
Rb,1.0,5.2
Rb,0.9,5.0
Rb,0.8,4.7
Rb,0.7,4.3
Rb,0.6,4.0
Rb,0.5,4.2
Rb,0.4,4.5
Rb,0.3,5.0
EOF
