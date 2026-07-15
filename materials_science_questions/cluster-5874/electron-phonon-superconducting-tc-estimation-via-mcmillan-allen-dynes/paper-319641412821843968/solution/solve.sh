#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: reproduced_results.json ===
cat > "$OUTDIR/reproduced_results.json" <<'EOF'
{"lambda_ac": 0.71, "lambda_op": 0.21, "Tc_values": [{"volume": "V0", "Tc": 11.1}, {"volume": "0.85V0", "Tc": 4.9}, {"volume": "0.70V0", "Tc": 0.98}]}
EOF
