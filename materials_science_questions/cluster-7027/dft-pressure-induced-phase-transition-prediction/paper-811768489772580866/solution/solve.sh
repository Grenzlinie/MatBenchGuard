#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: transition_results.json ===
cat > "/app/outputs/transition_results.json" <<'FFEOF'
[
  {
    "model": "CIM-DQ",
    "Pt_GPa": 194,
    "delta_V_percent": -1.68
  },
  {
    "model": "CIM no polarization",
    "Pt_GPa": 18,
    "delta_V_percent": -3.57
  }
]
FFEOF

# === solve finalize ===
echo "All outputs written."
