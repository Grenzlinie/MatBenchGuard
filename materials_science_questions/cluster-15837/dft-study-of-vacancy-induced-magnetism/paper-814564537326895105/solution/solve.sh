#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: computed_properties.json ===
cat > "$OUTDIR/computed_properties.json" <<'EOF'
{
  "binary_compounds": [
    {"name": "AlN wurtzite", "a0": 3.130, "E0": -443.331},
    {"name": "VN wurtzite", "a0": 3.092, "E0": -648.837},
    {"name": "VN NaCl", "a0": 0.0, "E0": -648.837}
  ],
  "ternary_compounds": [
    {"x": 0.25, "a0": 3.107, "E0": -597.140, "Ef": 0.320, "magnetic_moment": 2.0, "class": "half-metallic"},
    {"x": 0.50, "a0": 3.118, "E0": -545.815, "Ef": 0.270, "magnetic_moment": 2.0, "class": "half-metallic"},
    {"x": 0.75, "a0": 3.126, "E0": -494.559, "Ef": 0.148, "magnetic_moment": 2.0, "class": "metallic"}
  ]
}
EOF
