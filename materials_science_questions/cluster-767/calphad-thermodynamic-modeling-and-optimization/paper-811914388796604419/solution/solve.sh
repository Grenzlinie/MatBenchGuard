#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: excess_gibbs_parameters.csv ===
cat > "/app/outputs/excess_gibbs_parameters.csv" <<'FFEOF'
parameter,value
A,12350
B,1072
C,-0.57
D,-3.26
FFEOF

# === solve block: eutectic_point.csv ===
cat > "/app/outputs/eutectic_point.csv" <<'FFEOF'
property,value
temperature_C,271.35
composition_at_percent_Bi,99.958
FFEOF
