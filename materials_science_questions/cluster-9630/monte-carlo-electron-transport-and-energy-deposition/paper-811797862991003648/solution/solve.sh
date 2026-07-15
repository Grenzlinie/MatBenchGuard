#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: results_rrl.csv ===
cat > "/app/outputs/results_rrl.csv" << 'FFEOF'
deposition_efficiency,regime,width_nm
40.0,RRL,8.0
FFEOF

# === solve block: results_mtl.csv ===
cat > "/app/outputs/results_mtl.csv" << 'FFEOF'
deposition_efficiency,regime,width_nm
11.0,MTL,21.0
FFEOF
