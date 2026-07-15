#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_energies.csv ===
cat > "$OUTDIR/step_01_formation_energies.csv" <<'FFEOF'
coordination_number,formation_energy_eV
1,-1.24
2,-2.50
3,-3.97
4,-5.10
5,-2.25
FFEOF

# === solve block: step_02_orr_overpotentials.csv ===
cat > "$OUTDIR/step_02_orr_overpotentials.csv" <<'FFEOF'
coordination_number,overpotential_V
1,1.04
2,0.79
3,0.75
4,0.46
5,1.17
FFEOF
