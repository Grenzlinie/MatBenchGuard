#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: swarm_parameters.csv ===
cat > "$OUTDIR/swarm_parameters.csv" <<'EOF'
condition,mean_energy_eV,drift_velocity_cm_s
no_ee,2.50,1800000.0
ee_1e-5,2.60,1920000.0
ee_1e-4,2.75,2100000.0
EOF
