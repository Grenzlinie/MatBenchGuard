#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_07_adsorption_energies.json ===
cat > /app/outputs/step_07_adsorption_energies.json <<'EOF'
{
  "n-hexane": 9.2,
  "n-heptane": 10.6,
  "n-octane": 12.0,
  "benzene": 8.4,
  "toluene": 9.8
}
EOF

# === solve block: step_08_energy_contributions.json ===
cat > /app/outputs/step_08_energy_contributions.json <<'EOF'
{
  "C6_pct": 82,
  "C8_pct": 13,
  "C10_pct": 3,
  "induction_pct": 2,
  "repulsion_pct": 45
}
EOF
