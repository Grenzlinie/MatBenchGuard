#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: vacancy_formation_energies.csv ===
cat > /app/outputs/vacancy_formation_energies.csv <<'FFEOF'
pressure,formation_energy_Bi,formation_energy_Cu
0,0.14,1.08
3,0.22,1.18
6,0.30,1.32
9,0.40,1.50
FFEOF
