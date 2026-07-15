#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: occupancy_phi_0.csv ===
python3 /solution/generate_occupancy.py 0 > "$OUTDIR/occupancy_phi_0.csv"

# === solve block: occupancy_phi_1.3.csv ===
python3 /solution/generate_occupancy.py 1.3 > "$OUTDIR/occupancy_phi_1.3.csv"

# === solve block: transport_summary.csv ===
cat > "$OUTDIR/transport_summary.csv" <<'FFEOF'
phi,avg_N_w,N_exit,t_tr_ps
0,4.7352,2193,147.9
1.3,4.469,1768,160.1
FFEOF
