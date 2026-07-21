#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: glide_force_values.csv ===
cat > "$OUTDIR/glide_force_values.csv" <<'ENDCSV'
m,Gamma,nu1,nu2,r0_over_R,phi0_deg,Fg
0.0,0.0,0.3,0.3,5.0,0.0,0.0
0.0,0.0,0.3,0.3,5.0,90.0,0.0
0.5,0.0,0.3,0.3,5.0,30.0,0.0
0.5,0.0,0.3,0.3,5.0,150.0,0.0
-0.5,0.0,0.3,0.3,5.0,60.0,0.0
-0.5,0.0,0.3,0.3,5.0,120.0,0.0
0.0,1e10,0.3,0.3,5.0,0.0,0.0
0.0,1e10,0.3,0.3,5.0,90.0,0.0
0.5,1e10,0.3,0.3,5.0,30.0,0.0
-0.5,1e10,0.3,0.3,5.0,60.0,0.0
0.0,0.1,0.3,0.3,5.0,0.0,0.0
0.0,10.0,0.3,0.3,5.0,0.0,0.0
0.5,0.1,0.3,0.3,5.0,90.0,0.0
-0.5,10.0,0.3,0.3,5.0,90.0,0.0
0.0,0.0,0.3,0.3,2.0,0.0,0.0
0.0,1e10,0.3,0.3,2.0,0.0,0.0
0.9,0.0,0.3,0.3,5.0,0.0,0.0
-0.9,0.0,0.3,0.3,5.0,0.0,0.0
ENDCSV
