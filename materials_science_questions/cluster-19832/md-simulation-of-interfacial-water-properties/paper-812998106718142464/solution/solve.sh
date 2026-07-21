#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_pvdf_water_interaction_energies.csv ===
cat > /app/outputs/step_01_pvdf_water_interaction_energies.csv <<'HEREDOC'
surface,interaction_type,value,uncertainty
crystal,LJ,-45,1
crystal,Coulomb,-28,4
crystal,total,-73,5
amorphous,LJ,-47,1
amorphous,Coulomb,-85,6
amorphous,total,-132,6
HEREDOC
