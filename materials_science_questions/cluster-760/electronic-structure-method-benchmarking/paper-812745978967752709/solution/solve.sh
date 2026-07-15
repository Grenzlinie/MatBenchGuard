#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_ordering.json ===
cat > /app/outputs/energy_ordering.json <<'EOF'
{
  "S6_total_energy_hartree": -1380.5178,
  "PRC_total_energy_hartree": -1380.5046,
  "delta_E_kcal_per_mol": 8.3
}
EOF

# === solve block: binding_enthalpy.json ===
cat > /app/outputs/binding_enthalpy.json <<'EOF'
{
  "net_binding_enthalpy_kcal_per_mol": 185.4,
  "level": "B3LYP/6-31+G**"
}
EOF
