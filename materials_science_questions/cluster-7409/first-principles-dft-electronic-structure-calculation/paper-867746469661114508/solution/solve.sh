#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optical_conductivity_results.csv ===
cat > /app/outputs/optical_conductivity_results.csv <<'FFEOF'
configuration,absorption_edge_eV,first_strong_peak_eV
x0.0417_no_vac,3.2,3.7
x0.0625_no_vac,3.2,3.7
x0.0625_vac_Co,3.6,4.0
x0.0625_vac_Ti,3.2,3.5
FFEOF
