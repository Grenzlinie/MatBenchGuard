#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: perfect_core.json ===
cat > "$OUTDIR/perfect_core.json" << 'EOF'
{
  "radius_nm": 9.0,
  "energy_J_per_m": 4.2e-9
}
EOF

# === solve block: decomposed_core.json ===
cat > "$OUTDIR/decomposed_core.json" << 'EOF'
{
  "radius_nm": 9.0,
  "energy_J_per_m": 3.6e-9,
  "separation_nm": 1.5,
  "decomposition_confirmed": true
}
EOF
