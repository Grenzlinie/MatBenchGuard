#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: heat_of_mixing.json ===
cat > /app/outputs/heat_of_mixing.json <<'EOF'
{
  "Zr53Sn1_Em": -1.248,
  "Zr53Nb1_Em": 0.639,
  "Zr52Sn1Nb1_a_Em": -0.599,
  "Zr52Sn1Nb1_c_Em": -0.589
}
EOF
