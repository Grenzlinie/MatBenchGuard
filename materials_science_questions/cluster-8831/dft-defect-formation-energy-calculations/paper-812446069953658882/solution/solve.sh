#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'FFEOF'
metal,configuration,formation_energy_ev
Cu,octahedral,3.40
Cu,tetrahedral,4.66
Cu,crowdion,5.46
Ag,octahedral,3.04
Ag,tetrahedral,4.16
Ag,crowdion,4.86
Au,octahedral,2.91
Au,tetrahedral,4.05
Au,crowdion,4.76
FFEOF
