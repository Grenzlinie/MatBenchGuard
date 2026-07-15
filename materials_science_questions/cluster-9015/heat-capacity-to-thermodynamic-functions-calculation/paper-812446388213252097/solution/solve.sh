#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: thn_thermo.json ===
cat > "$OUTDIR/thn_thermo.json" <<'EOF'
{
  "S": 56.0,
  "H_minus_H0": 8450,
  "neg_G_minus_H0": 8250
}
EOF

# === solve block: un_magnetic_bounds.json ===
cat > "$OUTDIR/un_magnetic_bounds.json" <<'EOF'
{
  "delta_H_M_lower": 25,
  "delta_H_M_upper": 57,
  "delta_S_M_lower": 0.7,
  "delta_S_M_upper": 1.3
}
EOF
