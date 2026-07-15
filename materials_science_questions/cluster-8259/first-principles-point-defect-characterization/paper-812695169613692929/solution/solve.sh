#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: properties.json ===
cat > $OUTDIR/properties.json <<'EOF'
[
  {"defect": "pristine", "formation_energy": 0, "band_gap": 1.988, "magnetic_moment": 0},
  {"defect": "SV(5|9)", "formation_energy": 2.424, "band_gap": 0.516, "magnetic_moment": 0.997},
  {"defect": "DV(5|8|5)-1", "formation_energy": 2.842, "band_gap": 1.305, "magnetic_moment": 0},
  {"defect": "DV(555|777)", "formation_energy": 2.836, "band_gap": 1.467, "magnetic_moment": 0},
  {"defect": "DV(5555|6|7777)", "formation_energy": 2.933, "band_gap": 1.507, "magnetic_moment": 0},
  {"defect": "DV(5|8|5)-2", "formation_energy": 2.950, "band_gap": 1.146, "magnetic_moment": 0},
  {"defect": "SW(55|77)-1", "formation_energy": 1.470, "band_gap": 1.758, "magnetic_moment": 0},
  {"defect": "SW(55|77)-2", "formation_energy": 1.404, "band_gap": 1.784, "magnetic_moment": 0}
]
EOF

# === solve block: currents_26V.json ===
cat > /app/outputs/currents_26V.json <<'EOF'
[
  {"defect": "pristine", "current_zigzag": 0.052, "current_armchair": 0.109},
  {"defect": "SV(5|9)", "current_zigzag": 3.080, "current_armchair": 2.155},
  {"defect": "DV(5|8|5)-1", "current_zigzag": 0.398, "current_armchair": 0.524},
  {"defect": "DV(555|777)", "current_zigzag": 0.276, "current_armchair": 0.256},
  {"defect": "DV(5555|6|7777)", "current_zigzag": 0.934, "current_armchair": 0.922},
  {"defect": "DV(5|8|5)-2", "current_zigzag": 0.770, "current_armchair": 0.384},
  {"defect": "SW(55|77)-1", "current_zigzag": 0.155, "current_armchair": 0.394},
  {"defect": "SW(55|77)-2", "current_zigzag": 0.193, "current_armchair": 0.612}
]
EOF
