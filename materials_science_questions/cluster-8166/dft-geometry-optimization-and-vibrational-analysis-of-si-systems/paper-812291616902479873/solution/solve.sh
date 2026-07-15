#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_bcp_analysis.csv ===
cat > "$OUTDIR/step_01_bcp_analysis.csv" <<'CSVEOF'
n,method,R_SiN,rho,laplacian,d_Si
0,6-31G(d)//AM1,2.277,0.0380,0.0978,37.8
1,6-31G(d)//AM1,2.325,0.0375,0.0557,39.0
2,6-31G(d)//AM1,2.459,0.0315,0.0361,40.7
3,6-31G(d)//AM1,2.527,0.0301,0.0351,41.7
0,6-31G(d)//6-31G(d),2.066,0.0550,0.2403,37.9
1,6-31G(d)//6-31G(d),2.175,0.0465,0.1474,38.0
CSVEOF

# === solve block: step_02_energy_cost.txt ===
echo '4.0' > "$OUTDIR/step_02_energy_cost.txt"
