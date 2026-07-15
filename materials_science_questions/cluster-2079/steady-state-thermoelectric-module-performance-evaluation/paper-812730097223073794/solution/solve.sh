#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_device_performance.csv ===
cat > "$OUTDIR/step_01_device_performance.csv" <<'FFEOF'
Delta_T_K,V0_mV,Pmax_nW,R_int_Ohm
11,63.855,77.45,16368
17,98.685,189.10,16368
22,127.71,349.78,16368
35,203.175,668.38,16368
FFEOF
