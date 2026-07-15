#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_metrics.csv ===
cat > "$OUTDIR/step_01_metrics.csv" <<'CSVEOF'
energy_keV,storage_time_hours,secondary_count
5.0,1.5,120
10.0,3.0,300
20.0,6.0,700
CSVEOF
