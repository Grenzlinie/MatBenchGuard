#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: co_phase2_orbital_moment.txt ===
echo '-0.66' > "$OUTDIR/co_phase2_orbital_moment.txt"

# === solve block: co_phase3_orbital_moment.txt ===
echo '-0.06' > "$OUTDIR/co_phase3_orbital_moment.txt"

# === solve block: orbital_order_classification.json ===
cat > "$OUTDIR/orbital_order_classification.json" <<'FFEOF'
{
  "I41/amd": "complex",
  "I41/a": "A-type real"
}
FFEOF

# === solve block: conductivity_values.json ===
cat > "$OUTDIR/conductivity_values.json" <<'FFEOF'
{
  "x0.0": 10,
  "x0.5": 15,
  "x1.0": 25
}
FFEOF
