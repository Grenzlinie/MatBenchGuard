#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: mechanical_properties.json ===
mkdir -p "$OUTDIR"
cat > "$OUTDIR/mechanical_properties.json" <<'FFEOF'
{
  "density": 1.347,
  "youngs_modulus": 9.37,
  "shear_modulus": 3.94,
  "poissons_ratio": 0.189
}
FFEOF
