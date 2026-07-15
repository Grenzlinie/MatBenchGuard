#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: rho_results.json ===
cat > "$OUTDIR/rho_results.json" <<'FFEOF'
{"rho_thermal": 1.411, "rho_vibrational": 0.907}
FFEOF
