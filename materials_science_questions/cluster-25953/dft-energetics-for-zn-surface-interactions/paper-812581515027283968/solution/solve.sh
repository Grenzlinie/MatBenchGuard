#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'EOF'
{
  "TiO2_001": -0.63,
  "TiO2_100": -0.95,
  "TiO2_101": -0.45,
  "Zn_001": -0.68,
  "Zn_100": -0.86
}
EOF
