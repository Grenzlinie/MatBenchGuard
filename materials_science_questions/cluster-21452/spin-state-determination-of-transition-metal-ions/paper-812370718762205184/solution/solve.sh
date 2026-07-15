#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_moments.csv ===
cat > /app/outputs/magnetic_moments.csv << 'FFEOF'
site,spin_moment
Co1,0.35
Co2,2.73
O,0.14
FFEOF

# === solve finalize ===
echo "Oracle solve.sh completed."
