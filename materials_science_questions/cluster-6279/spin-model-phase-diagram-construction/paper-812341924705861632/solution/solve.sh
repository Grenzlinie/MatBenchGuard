#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: phase_boundaries.csv ===
python3 -c "
import sys
sys.path.insert(0, '/solution')
from write_outputs import write_phase_boundaries
write_phase_boundaries()
"

# === solve block: heat_adsorption.csv ===
python3 -c "
import sys
sys.path.insert(0, '/solution')
from write_outputs import write_heat_adsorption
write_heat_adsorption()
"

# === solve block: adsorption_isobars.csv ===
python3 -c "
import sys
sys.path.insert(0, '/solution')
from write_outputs import write_adsorption_isobars
write_adsorption_isobars()
"
