#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" << 'FFEOF'
[
  {"compound": "OsP2", "indirect_gap_eV": 0.78, "direct_gap_eV": 1.03},
  {"compound": "OsAs2", "indirect_gap_eV": 0.71, "direct_gap_eV": 0.90},
  {"compound": "OsSb2", "indirect_gap_eV": 0.33, "direct_gap_eV": 0.75}
]
FFEOF

# === solve block: seebeck_coefficient.csv ===
python3 /solution/generate_seebeck.py "$OUTDIR/seebeck_coefficient.csv"
