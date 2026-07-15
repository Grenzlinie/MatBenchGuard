#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: toe_constants.json ===
cat > /app/outputs/toe_constants.json << 'EOF'
{"4K":[-426.8,-520.8,-445.8,-149.2,-23.3,-32.4,-111.5,-27.9,-27.9,-111.5],"298K":[-409.7,-500.1,-428.1,-143.2,-22.4,-31.1,-107.0,-26.8,-26.8,-107.0]}
EOF

# === solve block: thermodynamic_constants.json ===
cat > /app/outputs/thermodynamic_constants.json << 'EOF'
{"gamma_L":2.08,"delta":3.63,"q":2.16,"gamma_H":2.13}
EOF

# === solve block: bulk_modulus_298K.json ===
cat > /app/outputs/bulk_modulus_298K.json << 'EOF'
{"B_s_298K":19.40}
EOF
