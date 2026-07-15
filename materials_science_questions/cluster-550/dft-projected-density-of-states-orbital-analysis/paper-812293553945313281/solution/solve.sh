#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json << 'EOF'
[
  {
    "compound": "SiH2",
    "direct_gap_eV": 4.53,
    "vbm_symmetry": "B2g",
    "cbm_symmetry": "B3u"
  },
  {
    "compound": "SiHMe",
    "direct_gap_eV": 4.24,
    "vbm_symmetry": "B_g",
    "cbm_symmetry": "B_u"
  },
  {
    "compound": "SiHPh",
    "direct_gap_eV": 3.73,
    "vbm_symmetry": "B_g",
    "cbm_symmetry": "B_u"
  },
  {
    "compound": "SiMePh",
    "direct_gap_eV": 3.61,
    "vbm_symmetry": "B_g",
    "cbm_symmetry": "B_u"
  }
]
EOF
