#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: topological_invariants.json ===
cat > /app/outputs/topological_invariants.json <<'EOF'
{
  "N_spinless_mu_positive": 1.0,
  "N_spinless_mu_negative": 0.0,
  "N_spinful_mu_positive": 2.0,
  "N_spinful_mu_negative": 0.0
}
EOF

# === solve block: planar_invariants.json ===
cat > /app/outputs/planar_invariants.json <<'EOF'
{
  "N_K_mu_positive": 2.0,
  "N_K_mu_negative": 0.0,
  "spin_Hall_conductance": 0.15915494309189535
}
EOF
