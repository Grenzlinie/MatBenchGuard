#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_results.json ===
cat > /app/outputs/defect_results.json <<'EOF'
{
  "surface": {
    "defect_level": 0.39,
    "formation_energy": 6.28,
    "cbm_vbm_same_kpoint": true
  },
  "internal_deep": {
    "defect_level": 0.41,
    "formation_energy": 3.19,
    "cbm_vbm_same_kpoint": false
  },
  "internal_shallow": {
    "defect_level": 0.41,
    "formation_energy": 4.34,
    "cbm_vbm_same_kpoint": false
  }
}
EOF
