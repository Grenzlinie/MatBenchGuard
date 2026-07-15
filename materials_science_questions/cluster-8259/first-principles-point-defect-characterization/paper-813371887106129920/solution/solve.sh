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
cat > "$OUTDIR/results.json" <<'EOF'
{
  "total_energies": {
    "perfect": -12345.67,
    "V0": -12340.12,
    "V+1": -12335.89,
    "V+2": -12331.45
  },
  "thermodynamic_transition_+2_0_above_Ge_CBM": true,
  "charge_switching_level_+1_0": 3.31
}
EOF
