#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_barrier_lowering.json ===
cat > /app/outputs/dft_barrier_lowering.json <<'FFEOF'
{
  "clean_barrier_eV": 0.85,
  "OH_barrier_eV": 0.694,
  "barrier_lowering_meV": 156
}
FFEOF
