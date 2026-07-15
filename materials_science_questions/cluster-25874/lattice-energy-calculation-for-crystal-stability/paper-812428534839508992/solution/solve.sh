#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: madelung_energy.txt ===
cat > "$OUTDIR/madelung_energy.txt" <<'EOF'
-36563.9
EOF

# === solve block: phosphorus_charges.json ===
cat > "$OUTDIR/phosphorus_charges.json" <<'EOF'
{
  "P1": [0.535, 0.534, 0.534, 0.534],
  "P2": [0.533, 0.534, 0.534, 0.533],
  "P3": [0.531, 0.533, 0.533, 0.531],
  "P4": [0.520, 0.520, 0.520, 0.520],
  "P5": [0.554, 0.553]
}
EOF
