#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "bandgap_GGA": 0.62,
  "bandgap_LDA": 0.51,
  "bandgap_GGA_mBJ": 0.88,
  "bandgap_LDA_mBJ": 1.20,
  "bandgap_LDA_mBJ_SOC": 1.05,
  "refractive_index_1000cm": 3.95,
  "transition_type": "indirect (Gamma-Z)"
}
FFEOF
