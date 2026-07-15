#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nucleation_kinetics.csv ===
cat > /app/outputs/nucleation_kinetics.csv <<'CSVEOF'
time,arrangement,number_density
100.0,random,0.0
100.0,regular,1000000.0
100.0,homogeneous,2000000.0
...
CSVEOF
