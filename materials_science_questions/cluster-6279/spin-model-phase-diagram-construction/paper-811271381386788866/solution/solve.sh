#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: tricritical_points.json ===
cat > "$OUTDIR/tricritical_points.json" <<'EOF'
[
  {
    "alpha": 0.0,
    "p": 0.0,
    "T_t": 2.390,
    "h_t": 2.784,
    "exists": true
  },
  {
    "alpha": 0.0,
    "p": 0.1,
    "T_t": 2.260,
    "h_t": 2.994,
    "exists": true
  },
  {
    "alpha": 0.0,
    "p": 0.2,
    "T_t": 2.039,
    "h_t": 3.268,
    "exists": true
  },
  {
    "alpha": 0.0,
    "p": 0.3,
    "T_t": 1.482,
    "h_t": 3.654,
    "exists": true
  },
  {
    "alpha": 0.5,
    "p": 0.0,
    "T_t": 1.769,
    "h_t": 2.795,
    "exists": true
  },
  {
    "alpha": 0.5,
    "p": 0.1,
    "T_t": 1.610,
    "h_t": 2.997,
    "exists": true
  },
  {
    "alpha": 0.5,
    "p": 0.2,
    "T_t": 1.328,
    "h_t": 3.249,
    "exists": true
  },
  {
    "alpha": 0.5,
    "p": 0.3,
    "T_t": 0.441,
    "h_t": 3.462,
    "exists": true
  }
]
EOF
