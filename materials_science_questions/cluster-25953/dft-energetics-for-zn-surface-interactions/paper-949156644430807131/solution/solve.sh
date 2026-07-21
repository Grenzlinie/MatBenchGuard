#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_results.csv ===
cat > "$OUTDIR/dft_results.csv" <<'EOF'
facet,binding_energy_Sn_on_Zn,binding_energy_Zn_on_facet,surface_energy
Zn(002),-2.9,-0.52,1.62
Zn(100),-4.15,-0.90,4.53
Zn(101),-5.93,-1.43,4.17
Sn(200),,-0.92,5.02
Sn(101),,-2.23,2.60
EOF
