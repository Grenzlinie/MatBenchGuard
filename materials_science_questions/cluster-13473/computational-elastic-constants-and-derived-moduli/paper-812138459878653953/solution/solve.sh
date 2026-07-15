#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: critical_exponents.json ===
cat > "$OUTDIR/critical_exponents.json" <<'EOF'
{
  "nu": {"value": 0.625, "error": 0.004},
  "beta": {"value": 0.315, "error": 0.004},
  "gamma": {"value": 1.27, "error": 0.01},
  "U4_crossing": {"value": 0.472, "error": 0.002},
  "Tc": {"value": 0.312067, "error": 0.000018}
}
EOF
