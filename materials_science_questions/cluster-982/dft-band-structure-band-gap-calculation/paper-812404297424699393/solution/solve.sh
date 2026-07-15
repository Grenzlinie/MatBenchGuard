#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
cat <<'EOF' > "$OUTDIR/results.json"
{
  "Ed_plus": 5.14,
  "D_plus": 3.0,
  "iota_LA": 1.42e-14,
  "L_plus": 3000.0,
  "mu": 115.0,
  "phi_plus": 2.60,
  "phi_ps": 1.45
}
EOF
