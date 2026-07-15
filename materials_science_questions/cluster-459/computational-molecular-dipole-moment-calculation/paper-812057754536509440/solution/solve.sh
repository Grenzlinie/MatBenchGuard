#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: proton_affinities.json ===
cat > /app/outputs/proton_affinities.json <<'EOF'
{
  "methionine": {
    "N": 223.2,
    "O": 197.2,
    "S": 211.4
  },
  "methionine_sulfoxide": {
    "N": 217.1,
    "O": 195.0,
    "SO": 241.2
  },
  "methionine_sulfone": {
    "N": 221.5,
    "O": 200.6,
    "SO2": 216.8
  }
}
EOF

# === solve block: most_favorable_sites.json ===
cat > /app/outputs/most_favorable_sites.json <<'EOF'
{
  "methionine": "N",
  "methionine_sulfoxide": "SO",
  "methionine_sulfone": "N"
}
EOF

# === solve block: dipole_moments.json ===
cat > /app/outputs/dipole_moments.json <<'EOF'
{
  "methionine": 2.1,
  "methionine_sulfoxide": 5.5,
  "methionine_sulfone": 5.4
}
EOF
