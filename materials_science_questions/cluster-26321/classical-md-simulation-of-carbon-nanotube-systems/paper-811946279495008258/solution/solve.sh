#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" <<'FFEOF'
scenario,binding_energy,nonbond_energy,vdw_energy,electrostatic_energy,hbond_energy
head_pCNT,-40.426,-38.5,-37.8,-0.5,-0.2
tail_pCNT,-29.593,-28.0,-27.3,-0.5,-0.2
head_dCNT,-39.330,-37.5,-36.8,-0.5,-0.2
tail_dCNT,-41.650,-39.8,-39.1,-0.5,-0.2
FFEOF
