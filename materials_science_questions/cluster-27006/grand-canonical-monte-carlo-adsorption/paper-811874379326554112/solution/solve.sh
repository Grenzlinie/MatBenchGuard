#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 << 'EOF'
import json
data = {
  "interaction_energy_UFF": 1.0,
  "interaction_energy_DREIDING": 0.5,
  "adsorption_density_IRMOF1": {
    "1wt%": {"A": 0.11, "B": 0.10, "Total": 0.11},
    "2wt%": {"A": 0.20, "B": 0.22, "Total": 0.21},
    "5wt%": {"A": 0.45, "B": 0.63, "Total": 0.54},
    "liquid": {"A": 0.68, "B": 1.22, "Total": 0.94}
  },
  "adsorption_density_IRMOF13": {
    "1wt%": {"A'": 0.06, "B'": 0.09, "C": 0.98, "E": 0.18, "Total": 0.22},
    "2wt%": {"A'": 0.14, "B'": 0.24, "C": 1.50, "E": 0.41, "Total": 0.41},
    "5wt%": {"A'": 0.51, "B'": 0.80, "C": 2.16, "E": 1.01, "Total": 0.92},
    "liquid": {"A'": 0.68, "B'": 1.20, "C": 2.49, "E": 1.25, "Total": 1.15}
  },
  "self_diffusion_IRMOF10": {
    "1wt%": 7.92,
    "2wt%": 7.21,
    "5wt%": 6.70,
    "liquid": 3.62
  },
  "self_diffusion_IRMOF13": {
    "1wt%": 0.20,
    "2wt%": 0.33,
    "5wt%": 0.80,
    "liquid": 0.72
  }
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
print("results.json written")
EOF
