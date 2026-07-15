#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_values.csv ===
cat > "$OUTDIR/dft_values.csv" <<'CSVEOF'
molecule,mu_x,mu_y,mu_z,mu_total,L,D,L_D
3F,5.52,-0.29,9.91,11.35,19.69,5.95,3.31
4F,5.53,-0.29,9.99,11.43,20.95,5.97,3.51
CSVEOF
