#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: poling_voltages.csv ===
cat > "$OUTDIR/poling_voltages.csv" << 'EOF'
design,thickness_um,voltage_V
single,220,6200
single,250,6500
single,280,6800
dual,220,5750
dual,250,5800
dual,280,5850
EOF
