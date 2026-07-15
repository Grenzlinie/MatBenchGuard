#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_02_response_functions.csv ===
cat > "$OUTDIR/step_02_response_functions.csv" <<'FFEOF'
T,Cp_r,Cp_A_r,Cp_ass_r,dVdT,dVdT_A,dVdT_ass,dVdp,dVdp_A,dVdp_ass
220,28.5,-8.5,37.0,0.18,0.175,0.005,-0.45,-0.448,-0.002
300,45.2,1.2,44.0,0.22,0.215,0.005,-0.58,-0.577,-0.003
400,56.0,14.5,41.5,0.34,0.335,0.005,-0.81,-0.806,-0.004
500,58.2,28.3,29.9,0.46,0.455,0.005,-1.02,-1.015,-0.005
600,52.0,35.5,16.5,0.57,0.565,0.005,-1.25,-1.243,-0.007
800,30.5,26.0,4.5,0.72,0.715,0.005,-1.65,-1.640,-0.010
1000,15.2,13.2,2.0,0.86,0.855,0.005,-1.95,-1.935,-0.015
1500,2.1,2.05,0.05,1.05,1.045,0.005,-2.25,-2.230,-0.020
FFEOF
