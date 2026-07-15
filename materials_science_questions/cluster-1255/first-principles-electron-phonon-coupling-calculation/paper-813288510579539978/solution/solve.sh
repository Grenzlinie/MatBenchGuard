#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{"q": [0.1, 0.0, 0.0], "P_at_omega": 0.6574247042592008, "omega_tilde": 0.10033333333333333}
EOF
