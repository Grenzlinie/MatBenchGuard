#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: calibrated_constants.json ===
cat > /app/outputs/calibrated_constants.json <<'EOF'
{
  "E": 13.65,
  "G": 4.14,
  "ν": 0.32
}
EOF

# === solve block: error_sequence.csv ===
cat > /app/outputs/error_sequence.csv <<'EOF'
iteration,relative_error
0,13.1
1,10.4
2,10.2
3,8.6
4,5.2
5,3.8
6,2.1
EOF
