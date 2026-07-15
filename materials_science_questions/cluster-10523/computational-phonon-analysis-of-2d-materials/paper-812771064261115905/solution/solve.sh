#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_conductivities.csv ===
cat > /app/outputs/thermal_conductivities.csv <<'FFEOF'
condition,thermal_conductivity
pristine,820.0
vacancy_0.5,196.8
vacancy_1.0,114.8
coated_0.5_3nm,326.7
coated_1.0_3nm,275.5
FFEOF
