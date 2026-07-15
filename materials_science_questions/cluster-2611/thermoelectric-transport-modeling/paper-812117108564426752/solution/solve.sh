#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermopower_table.csv ===
cat > /app/outputs/thermopower_table.csv <<'EOF'
doping_fraction,S_muV_per_K
0.05,-5.2
0.25,-9.3
0.50,-18.3
0.75,-29.4
0.80,-41.2
EOF
