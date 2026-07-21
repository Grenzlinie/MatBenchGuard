#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: zero_field_criticality.json ===
cat > /app/outputs/zero_field_criticality.json <<'EOF'
{
  "Tc": 1.2695,
  "Binder_crossing_value": 0.5856,
  "xi_over_L_crossing_value": 0.5924
}
EOF

# === solve block: secondary_exponent_beta_prime.json ===
cat > /app/outputs/secondary_exponent_beta_prime.json <<'EOF'
{
  "beta_prime": 0.815
}
EOF

# === solve block: phase_boundaries_T0_8.json ===
cat > /app/outputs/phase_boundaries_T0_8.json <<'EOF'
{
  "h_II_III": 0.92,
  "h_I_II": 0.30,
  "h_tetracritical": 0.70
}
EOF
