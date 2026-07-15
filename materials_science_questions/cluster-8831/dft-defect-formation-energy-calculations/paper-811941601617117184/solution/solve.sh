#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: dft_results.json ===
# The agent must compute these values using DFT.
cat > "$OUTDIR/dft_results.json" <<'FFEOF'
{
  "lattice_parameter_a": 0.0,
  "band_gap_eV": 0.0
}
FFEOF
