#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_conductivity.csv ===
cat > "$OUTDIR/thermal_conductivity.csv" << 'EOF'
system,kappa_300
Si46,16.0
Na8Si46,2.7
K8Si46,5.2
Ba8Si46,1.0
Ge46,14.5
K8Ge44□2,1.1
Ba8Ge43□3,
EOF
