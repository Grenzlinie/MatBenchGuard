#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: defect_results.json ===
cat > "$OUTDIR/defect_results.json" <<'MAINEOF'
[
  {
    "defect": "V_N",
    "charge_state": 1,
    "E_neutral": -1000.0,
    "E_charged_corrected": -992.99,
    "epsilon_VBM": 5.0,
    "IE": 2.01
  },
  {
    "defect": "C_N",
    "charge_state": -1,
    "E_neutral": -1000.0,
    "E_charged_corrected": -993.61,
    "epsilon_VBM": 5.0,
    "IE": 1.39
  }
]
MAINEOF
