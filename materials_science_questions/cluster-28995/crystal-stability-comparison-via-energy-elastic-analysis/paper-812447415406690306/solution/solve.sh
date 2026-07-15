#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: electron_lattice_energy.csv ===
cat > "$OUTDIR/electron_lattice_energy.csv" <<'FFEOF'
element,lattice,energy
hydrogen,bcc,0.0903860
hydrogen,fcc,0.0913073
hydrogen,hcp,0.0661690
helium,bcc,0.224488
helium,fcc,0.219672
helium,hcp,0.189904
carbon,bcc,0.473481
carbon,fcc,0.474871
carbon,hcp,0.435366
iron,bcc,1.034330
iron,fcc,1.036611
iron,hcp,0.989050
FFEOF
