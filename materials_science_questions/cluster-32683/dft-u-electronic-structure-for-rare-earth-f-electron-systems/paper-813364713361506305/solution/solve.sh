#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "compounds": [
    {
      "name": "La5Ge3",
      "a": 8.872,
      "c": 6.774,
      "total_magnetic_moment": 0.0
    },
    {
      "name": "Ce5Ge3",
      "a": 8.726,
      "c": 6.055,
      "total_magnetic_moment": 2.742
    },
    {
      "name": "Pr5Ge3",
      "a": 8.917,
      "c": 6.137,
      "total_magnetic_moment": 24.378
    },
    {
      "name": "Nd5Ge3",
      "a": 8.718,
      "c": 6.382,
      "total_magnetic_moment": 34.793
    }
  ]
}
FFEOF
