#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results_table.json ===
mkdir -p /app/outputs
cat > /app/outputs/results_table.json <<'EOF'
{
  "crystal_A": {
    "packing_coefficient": 0.72,
    "ppe_MRK": -92.4,
    "ppe_GVF": -110.9
  },
  "crystal_B": {
    "packing_coefficient": 0.72,
    "ppe_MRK": -94.2,
    "ppe_GVF": -112.0
  },
  "crystal_C": {
    "packing_coefficient": 0.72,
    "ppe_MRK_mean": -93.1,
    "ppe_GVF_mean": -111.3
  }
}
EOF
