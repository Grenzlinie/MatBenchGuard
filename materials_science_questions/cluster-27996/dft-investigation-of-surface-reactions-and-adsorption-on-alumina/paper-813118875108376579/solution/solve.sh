#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: adsorption_results.csv ===
cat > "$OUTDIR/adsorption_results.csv" <<'CSVEOF'
system,band_gap_eV,adsorption_energy_eV,mulliken_charge_e,aim_charge_e,average_energy_gap_variation_percent
Ge_isolated,1.43,,,,,
A1,1.39,-1.76,1.032,0.432,2.88
A2,1.41,-1.75,1.024,0.426,1.42
A3,1.42,-1.82,1.072,0.448,0.7
B1,1.13,-1.95,1.087,0.453,26.55
B2,1.04,-1.93,1.091,0.457,37.5
B3,1.02,-1.92,1.09,0.456,40.2
CSVEOF
