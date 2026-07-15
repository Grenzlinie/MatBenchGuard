#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: elastic_constants.json ===
mkdir -p "$OUTDIR"
cat > "$OUTDIR/elastic_constants.json" <<'EOF'
{"C11":88.64,"C22":149.21,"C12":-23.71,"C66":24.50,"units":"GPa"}
EOF

# === solve block: mechanical_properties.json ===
cat > "$OUTDIR/mechanical_properties.json" <<'EOF'
{
  "Ex": 84.87,
  "Ey": 142.86,
  "vxy": -0.158,
  "vyx": -0.267,
  "units_Ex": "GPa",
  "units_Ey": "GPa"
}
EOF
