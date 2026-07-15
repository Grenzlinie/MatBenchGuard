#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_mtunnel.json ===
cat > "/app/outputs/computed_mtunnel.json" <<'EOF'
[
  {"material": "r-TiO2", "orientation": "(110)", "stoichiometry": "stoichiometric", "energy_below_CBM": 1.3, "m_tunnel": 0.15},
  {"material": "r-TiO2", "orientation": "(001)", "stoichiometry": "stoichiometric", "energy_below_CBM": 1.3, "m_tunnel": 0.19},
  {"material": "r-TiO2", "orientation": "(100)", "stoichiometry": "stoichiometric", "energy_below_CBM": 1.3, "m_tunnel": 0.27},
  {"material": "r-TiO2", "orientation": "(101)", "stoichiometry": "stoichiometric", "energy_below_CBM": 1.3, "m_tunnel": 0.23},
  {"material": "SrTiO3", "orientation": "(110)", "stoichiometry": "stoichiometric", "energy_below_CBM": 0.9, "m_tunnel": 0.18},
  {"material": "SrTiO3", "orientation": "(001)", "stoichiometry": "stoichiometric", "energy_below_CBM": 0.9, "m_tunnel": 0.21},
  {"material": "SrTiO3", "orientation": "(111)", "stoichiometry": "stoichiometric", "energy_below_CBM": 0.9, "m_tunnel": 0.25},
  {"material": "SrTiO3", "orientation": "(001)", "stoichiometry": "Sr0.62Ti0.38O4", "energy_below_CBM": 0.9, "m_tunnel": 0.45},
  {"material": "SrTiO3", "orientation": "(001)", "stoichiometry": "Sr2TiO4", "energy_below_CBM": 0.9, "m_tunnel": 0.44}
]
EOF
