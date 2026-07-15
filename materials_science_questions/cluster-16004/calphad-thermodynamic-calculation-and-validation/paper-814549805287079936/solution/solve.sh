#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pure_apb_energy.txt ===
echo '318' > "$OUTDIR/pure_apb_energy.txt"

# === solve block: dopant_apb_energies.csv ===
cat > "$OUTDIR/dopant_apb_energies.csv" <<'CSVEOF'
concentration,temperature,APB_energy,delta_APB_energy
1,400,325,10
1,1600,317,2
CSVEOF

# === solve finalize ===
echo "All outputs written."
