#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: defect_formation_volumes.json ===
cat > /app/outputs/defect_formation_volumes.json <<'EOF'
{
  "stoichiometric": {
    "Fe_vacancy": {"ΔV": -0.2, "Ω̃": 0.5},
    "Al_vacancy": {"ΔV": -0.7, "Ω̃": 0.6},
    "Fe_antistructure": {"ΔV": -0.4, "Ω̃": -0.2},
    "Al_antistructure": {"ΔV": 0.4, "Ω̃": 0.2}
  },
  "Fe0.52Al0.48": {
    "Fe_vacancy": {"ΔV": -0.2, "Ω̃": 0.55},
    "Al_vacancy": {"ΔV": -0.7, "Ω̃": 0.5},
    "Fe_antistructure": {"ΔV": -0.4, "Ω̃": 0.0},
    "Al_antistructure": {"ΔV": 0.4, "Ω̃": 0.05}
  }
}
EOF
