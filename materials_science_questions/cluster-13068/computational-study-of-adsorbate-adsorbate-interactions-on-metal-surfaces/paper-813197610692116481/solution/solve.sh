#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_adsorption_energies.csv ===
cat > "$OUTDIR/step_01_adsorption_energies.csv" <<'FFEOF'
adsorption_energy_eV,height_A,site
-3.10,2.08,hcp
-3.06,2.11,fcc
-3.06,2.09,bridge
-2.57,2.12,top
FFEOF

# === solve block: step_02_diffusion_barrier.txt ===
echo '0.04' > "$OUTDIR/step_02_diffusion_barrier.txt"
