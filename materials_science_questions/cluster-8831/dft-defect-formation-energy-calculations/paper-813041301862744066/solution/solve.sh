#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: effective_formation_energies.csv ===
cat > "$OUTDIR/effective_formation_energies.csv" <<'EOF'
defect,E_eff
Fe_vac_alpha,1.25
Fe_vac_gamma,2.27
Al_vac,1.39
Fe_anti_Al,0.0
Al_anti_gamma,0.0
Al_anti_alpha,1.82
EOF
