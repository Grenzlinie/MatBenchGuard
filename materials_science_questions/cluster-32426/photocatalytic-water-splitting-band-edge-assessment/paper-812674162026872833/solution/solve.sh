#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: o1p_properties.json ===
cat > "$OUTDIR/o1p_properties.json" <<'EOF'
{
  "band_gap_hse06": 1.34,
  "exciton_binding_energy": 0.34,
  "CBM_oxygen_vacuum": -5.81,
  "VBM_oxygen_vacuum": -7.15,
  "CBM_phosphorus_vacuum": -3.26,
  "VBM_phosphorus_vacuum": -4.60,
  "hole_mobility_Y": 18320,
  "STH_efficiency": 22.77
}
EOF
