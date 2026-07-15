#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" << 'EOF'
{
  "rGO_basal": 0.83,
  "B_rGO_basal": -0.49,
  "Nq_rGO_basal": -0.02,
  "NB_rGO_B_atom": -0.81
}
EOF
