#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predictions.json ===
cat > /app/outputs/predictions.json <<'FFEOF'
[
  {"d_n":5,"x":4,"strong_sigma_donor":false,"predicted_structure":"C","radical_note":""},
  {"d_n":6,"x":4,"strong_sigma_donor":false,"predicted_structure":"B","radical_note":""},
  {"d_n":7,"x":4,"strong_sigma_donor":false,"predicted_structure":"A","radical_note":""},
  {"d_n":6,"x":4,"strong_sigma_donor":true,"predicted_structure":"A","radical_note":"diradical"},
  {"d_n":5,"x":6,"strong_sigma_donor":false,"predicted_structure":"C","radical_note":""},
  {"d_n":6,"x":6,"strong_sigma_donor":false,"predicted_structure":"B","radical_note":""},
  {"d_n":7,"x":6,"strong_sigma_donor":false,"predicted_structure":"A","radical_note":""},
  {"d_n":6,"x":6,"strong_sigma_donor":true,"predicted_structure":"A","radical_note":"diradical"}
]
FFEOF
