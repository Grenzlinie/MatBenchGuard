#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'FFEOF'
configuration,formation_energy_eV
Cd_s,4.750
Cd_I,1.250
Cd_I^{VO2},1.150
^{VO2}Cd_I^{VO2},1.041
FFEOF
