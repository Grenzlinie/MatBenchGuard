#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "leading_symmetries": [
    "d_{x^2-y^2}",
    "d_{3z^2-r^2}"
  ],
  "Tc_3D": 0.0067,
  "Tc_2D": 0.042,
  "Tc_ratio": 0.1595238095238095
}
EOF
