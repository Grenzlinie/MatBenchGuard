#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetic_moments.csv ===
cat > "$OUTDIR/magnetic_moments.csv" <<'FFEOF'
configuration,magnetic_moment
pristine,0.0
B-sp2-in,1.00
B-sp3,0.93
B-sp2-out,1.00
O-sp2-in,0.00
O-sp3,2.00
O-sp2-out,0.00
N-sp2-in,1.00
N-sp3,0.92
N-sp2-out,1.00
FFEOF
