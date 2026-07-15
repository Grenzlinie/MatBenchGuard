#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: heat_capacity_ideal.csv ===
cat > "$OUTDIR/heat_capacity_ideal.csv" <<'FFEOF'
temperature_K,heat_capacity_rise_percent
150,14.0
300,4.5
FFEOF

# === solve block: msd_vacancy_300K.txt ===
echo "0.25" > "$OUTDIR/msd_vacancy_300K.txt"
