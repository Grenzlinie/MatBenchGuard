#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_energies.csv ===
cat > /app/outputs/adsorption_energies.csv <<'FFEOF'
configuration,E_ads
N1-NH3,-2.02
N2-NH3,-2.44
N3-NH3,-2.77
B-NH3,-2.25
Mo-NO,-0.84
O-NO,-0.68
H-NO,-0.70
FFEOF
