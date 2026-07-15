#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "delta_E": {
    "K_12.5": 15,
    "K_25": 51,
    "La_12.5": 34,
    "La_25": 64
  },
  "Tc": {
    "K_25": 327,
    "La_25": 453
  }
}
EOF
