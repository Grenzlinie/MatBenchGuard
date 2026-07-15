#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_adsorption_energies.csv ===
cat > /app/outputs/step_01_adsorption_energies.csv <<'FFEOF'
system,adsorbate,E_ads_eV
Pd,H2,-0.5927
PdNb,H2,-0.4740
PdCu,H2,-0.5357
Pd,H2S,-0.700
PdNb,H2S,-0.803
PdCu,H2S,-0.429
FFEOF
