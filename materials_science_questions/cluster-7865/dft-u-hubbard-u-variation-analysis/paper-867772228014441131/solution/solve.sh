#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: kondo_temperatures.json ===
cat > "$OUTDIR/kondo_temperatures.json" <<'EOF'
{
  "Co_44": 1.0,
  "Co_88": 1.0,
  "Fe_88": 0.0001
}
EOF

# === solve block: zero_bias_conductances.json ===
cat > "$OUTDIR/zero_bias_conductances.json" <<'EOF'
{
  "Co_44": 1.0,
  "Co_88": 1.0,
  "Fe_88": 0.0
}
EOF
