#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: carbonyl_results.csv ===
cat > "$OUTDIR/carbonyl_results.csv" <<'EOF'
species,adsorption_energy,hydroxy_TS1_barrier,alkoxy_TS1_barrier
formaldehyde,-104,90,65
acetaldehyde,-69,110,63
propionaldehyde,-72,121,58
acetone,-43,127,53
butyraldehyde,-67,126,65
MEK,-33,64,58
EOF
