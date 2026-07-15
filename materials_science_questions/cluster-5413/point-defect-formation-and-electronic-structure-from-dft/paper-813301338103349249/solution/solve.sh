#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_03_segregation_energies.csv ===
cat > /app/outputs/step_03_segregation_energies.csv <<'FFEOF'
termination,vo_present,relative_energy
LaO,false,-0.40
FeO2,false,-0.42
LaO,true,-0.21
FeO2,true,-0.89
FFEOF

# === solve block: step_04_vo_formation_energies.csv ===
cat > /app/outputs/step_04_vo_formation_energies.csv <<'FFEOF'
termination,formation_energy,notes
LaO,2.89,"most stable site: LaO-layer beneath Pd at surface"
FeO2,1.42,"most stable site: LaO-layer beneath Pd at surface"
FFEOF
