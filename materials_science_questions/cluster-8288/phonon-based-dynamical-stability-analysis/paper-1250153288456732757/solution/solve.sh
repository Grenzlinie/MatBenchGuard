#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: step_01_elastic_properties.json ===
cat > "$OUTDIR/step_01_elastic_properties.json" <<'EOF'
{
  "C11": 728,
  "C12": 20,
  "C13": 85,
  "C33": 1161,
  "C44": 160,
  "C66": 70,
  "B_V": 333,
  "G_V": 320,
  "H_V": 58
}
EOF

# === solve block: step_02_phonon.json ===
cat > "$OUTDIR/step_02_phonon.json" <<'EOF'
{
  "max_frequency_THz": 60
}
EOF
