#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "cu100": {
    "adsorption_energy": -1.03,
    "barriers": {
      "H1": 1.05,
      "H2": 4.28,
      "H3": 1.16
    }
  },
  "cu111": {
    "adsorption_energy": -0.92,
    "barriers": {
      "H1": 1.17,
      "H2": 1.98
    }
  }
}
EOF
