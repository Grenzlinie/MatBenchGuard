#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: defect_energies.csv ===
cat > "$OUTDIR/defect_energies.csv" <<'FFEOF'
defect,diffusion_prefactor,formation_energy,migration_energy
Si vacancy,0.0110,3.25,7.39
C vacancy,0.0151,2.63,6.10
FFEOF
