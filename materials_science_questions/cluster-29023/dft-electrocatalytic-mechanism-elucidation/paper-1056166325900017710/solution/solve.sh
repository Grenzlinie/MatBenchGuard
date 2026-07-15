#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: interaction_energies.csv ===
cat > "$OUTDIR/interaction_energies.csv" <<'FFEOF'
system,vdW,Elec,total
PEF/COFs,-177.104,-69.05,-246.154
OFL/COFs,-108.46,-38.83,-147.29
NOR/COFs,-76.95,-44.69,-121.64
PEF/CNTs@COFs,-133.931,-109.394,-243.325
OFL/CNTs@COFs,-323.306,-35.32,-358.626
NOR/CNTs@COFs,-285.44,-63.33,-348.77
FFEOF

# === solve block: free_energy_minima.csv ===
cat > "$OUTDIR/free_energy_minima.csv" <<'FFEOF'
system,free_energy_minimum
PEF/COFs,-400.41
OFL/CNTs@COFs,-734.27
FFEOF
