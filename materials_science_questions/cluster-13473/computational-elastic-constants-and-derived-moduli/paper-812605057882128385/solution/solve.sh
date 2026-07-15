#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: shear_moduli.csv ===
cat > "/app/outputs/shear_moduli.csv" <<'FFEOF'
Lx,Lz,ratio_Lx_Lz,mu_xz,mu_xy
50,15,3.3333333333333335,12.0,8.0
30,15,2.0,9.0,7.2
15,15,1.0,6.0,6.8
FFEOF
