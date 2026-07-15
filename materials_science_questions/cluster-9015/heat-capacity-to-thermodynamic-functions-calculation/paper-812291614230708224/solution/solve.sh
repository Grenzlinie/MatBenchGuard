#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: entropy_contributions.json ===
cat > /app/outputs/entropy_contributions.json <<'EOF'
{
  "Bi": {
    "extrapolated_0_56.2_K": 3.13,
    "graphical_56.2_298.1_K": 9.31,
    "total_S_298_K": 12.44
  },
  "Bi2O3": {
    "extrapolated_0_56.2_K": 6.22,
    "graphical_56.2_298.1_K": 29.96,
    "total_S_298_K": 36.18
  }
}
EOF

# === solve block: free_energy.json ===
cat > /app/outputs/free_energy.json <<'EOF'
{
  "free_energy_Bi2O3": -118000,
  "unit": "cal"
}
EOF
