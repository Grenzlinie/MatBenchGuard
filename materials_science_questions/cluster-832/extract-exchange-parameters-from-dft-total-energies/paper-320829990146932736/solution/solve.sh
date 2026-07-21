#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: coulomb_exchange.json ===
cat > "$OUTDIR/coulomb_exchange.json" <<'EOF'
{
  "J1": 6.242e-4,
  "J2_over_J1": -2.429e-5,
  "K_over_J1": -0.3411
}
EOF

# === solve block: linear_coefficients.json ===
cat > /app/outputs/linear_coefficients.json <<'FFEOF'
{
  "alpha": 1.323e9,
  "beta": 8.042e-3
}
FFEOF

# === solve block: bond_length.txt ===
echo 8.75 > /app/outputs/bond_length.txt
