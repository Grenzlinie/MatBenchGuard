#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: mae_results.json ===
cat > "$OUTDIR/mae_results.json" <<'FFEOF'
[
  {
    "system": "Fe@B",
    "magnetic_moment_muB": 1,
    "MAE_meV": 1.19,
    "easy_axis": "in-plane"
  },
  {
    "system": "Mn@B",
    "magnetic_moment_muB": 2,
    "MAE_meV": -0.63,
    "easy_axis": "out-of-plane"
  },
  {
    "system": "Sc@B",
    "magnetic_moment_muB": 0,
    "MAE_meV": null,
    "easy_axis": "none"
  },
  {
    "system": "Co@B",
    "magnetic_moment_muB": 0,
    "MAE_meV": null,
    "easy_axis": "none"
  }
]
FFEOF
