#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: corundum_mass_frac_1400C.csv ===
cat > "/app/outputs/corundum_mass_frac_1400C.csv" <<'FFEOF'
Co_percent,corundum_mass_frac
3,0.0015
6,0.0020
12,0.0025
FFEOF
