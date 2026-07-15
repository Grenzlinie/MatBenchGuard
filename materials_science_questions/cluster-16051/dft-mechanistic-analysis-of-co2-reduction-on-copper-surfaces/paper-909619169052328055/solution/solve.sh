#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: free_energies.json ===
cat > /app/outputs/free_energies.json <<'EOF'
[
  {"surface": "Cu(111)", "intermediate": "*OCHO", "free_energy_eV": 0.34},
  {"surface": "Cu(111)", "intermediate": "*COOH", "free_energy_eV": 0.43},
  {"surface": "Cu(111)", "intermediate": "*H", "free_energy_eV": -0.15},
  {"surface": "S-adsorbed Cu(111)", "intermediate": "*OCHO", "free_energy_eV": 0.10},
  {"surface": "S-adsorbed Cu(111)", "intermediate": "*COOH", "free_energy_eV": 0.65},
  {"surface": "S-adsorbed Cu(111)", "intermediate": "*H", "free_energy_eV": 0.43}
]
EOF
