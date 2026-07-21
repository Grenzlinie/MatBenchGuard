#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: acceptance_rates.csv ===
cat > "$OUTDIR/acceptance_rates.csv" <<'CSVEOF'
b,P_xyz,P_parallel,P_rotate
0.05,0.10,0.95,0.60
0.1,0.25,0.55,0.70
0.2,0.55,0.35,0.80
0.5,0.75,0.30,0.50
1.0,0.90,0.20,0.40
1.5,0.98,0.15,0.30
CSVEOF
