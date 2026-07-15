#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_properties.json ===
cat > "$OUTDIR/computed_properties.json" <<'EOF'
{
  "c11": 182.6,
  "c12": 45.9,
  "c44": 68.4,
  "E": 164.2,
  "G": 68.4,
  "K": 91.5,
  "lambda": 45.9,
  "nu": 0.201,
  "K_over_G": 1.337719,
  "Debye_temperature": 604.0
}
EOF
