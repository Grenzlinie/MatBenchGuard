#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: energy_differences.csv ===
cat > "$OUTDIR/energy_differences.csv" <<'FFEOF'
neighbor,delta_E_meV
1,555
2,289
3,0
4,245
FFEOF
