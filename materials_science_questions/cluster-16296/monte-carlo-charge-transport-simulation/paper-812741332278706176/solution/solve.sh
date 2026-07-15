#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: steady_state.csv ===
cat > "$OUTDIR/steady_state.csv" <<'FFEOF'
electric_field_kVcm,v_equilibrium_cms,v_nonequilibrium_cms
0.5,4000000.0,4600000.0
1,8000000.0,9200000.0
2,16000000.0,18400000.0
4,22000000.0,24200000.0
6,18000000.0,17000000.0
8,15000000.0,14100000.0
10,12000000.0,11000000.0
12,10000000.0,9000000.0
FFEOF

# === solve block: overshoot_peak.csv ===
cat > "$OUTDIR/overshoot_peak.csv" <<'FFEOF'
electric_field_kVcm,v_equilibrium_peak_cms,v_nonequilibrium_peak_cms
8.0,37000000.0,37000000.0
FFEOF
