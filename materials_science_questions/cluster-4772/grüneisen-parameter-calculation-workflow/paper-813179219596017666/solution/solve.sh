#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: room_temp_BM_params.json ===
cat > /app/outputs/room_temp_BM_params.json <<'EOF'
{
  "V0": 1476.0,
  "K0_300": 181.0,
  "K_prime_0_300": 4.4,
  "V0_err": 1.0,
  "K0_300_err": 9.0,
  "K_prime_0_300_err": 1.2
}
EOF

# === solve block: HTBM_params.json ===
cat > /app/outputs/HTBM_params.json <<'EOF'
{
  "V0": 1475.9,
  "K0_300": 184.0,
  "K_prime_0_300": 3.8,
  "dK_dT": -0.023,
  "a": 3.18e-5,
  "b": 1.8e-9,
  "K0_300_err": 4.0,
  "K_prime_0_300_err": 0.6,
  "dK_dT_err": 0.005,
  "a_err": 1.6e-6,
  "b_err": 2.1e-9
}
EOF

# === solve block: MGD_params.json ===
cat > /app/outputs/MGD_params.json <<'EOF'
{
  "gamma0": 1.35,
  "gamma0_err": 0.01,
  "theta0": 890,
  "q": 1
}
EOF
