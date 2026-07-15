#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: nucleation.csv ===
cat > "$OUTDIR/nucleation.csv" <<'FFEOF'
r_crit_m,undercooling_K
1.0e-9,3.0
FFEOF

# === solve block: heat_transfer.csv ===
python3 /solution/compute_heat_transfer.py > "$OUTDIR/heat_transfer.csv"
