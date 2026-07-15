#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: equilibrium_lattice_constants.csv ===
cat > "/app/outputs/equilibrium_lattice_constants.csv" <<'FFEOF'
phase,lattice_constant_a,scheme
Pd,3.873,PBE/PAW
PdH_oct,4.064,PBE/PAW
PdH_mixed,4.116,PBE/PAW
FFEOF
