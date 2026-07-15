#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: as31ga_properties.json ===
cat > "$OUTDIR/as31ga_properties.json" <<'FFEOF'
{
  "Eg": 1.348,
  "Eg_type": "direct",
  "magnetic_moment": 0.0
}
FFEOF

# === solve block: as31ge_properties.json ===
cat > "$OUTDIR/as31ge_properties.json" <<'FFEOF'
{
  "total_moment": 1.0,
  "Eg_up": 1.402,
  "Eg_down": 0.331,
  "Ge_moment": 0.524
}
FFEOF
