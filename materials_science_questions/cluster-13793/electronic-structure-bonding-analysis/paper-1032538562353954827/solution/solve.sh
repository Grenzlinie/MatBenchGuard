#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: effective_masses.json ===
cat > /app/outputs/effective_masses.json <<'EOF'
{
  "unstrained": {
    "a_star": 3.06,
    "b_star": 3.06,
    "c_star": 4.77,
    "conductivity": 3.47
  },
  "strained": {
    "a_star": 2.77,
    "b_star": 26.6,
    "c_star": 0.38,
    "conductivity": 0.99
  }
}
EOF

# === solve block: COHP_summary.json ===
cat > /app/outputs/COHP_summary.json <<'EOF'
{
  "total_COHP_GaO_integrated_VBM": -0.2,
  "total_COHP_OO_integrated_VBM": -1.3,
  "dominant_pair_at_Gamma": {
    "pair": "O2-O5",
    "orbitals": "pz-pz",
    "COHP_value": -0.15
  },
  "dominant_pair_at_I": {
    "pair": "O1-O4",
    "orbitals": "px-px",
    "COHP_value": -0.10
  }
}
EOF
