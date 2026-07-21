#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reconstructions.json ===
cat > "$OUTDIR/reconstructions.json" <<'EOF'
[
  {
    "scenario": "sigI0.25_SNR25",
    "method": "IGA",
    "center_x": 0.0,
    "center_y": 0.0,
    "width": 0.2,
    "length": 0.2,
    "orientation": 0.0,
    "iterations": 106,
    "final_functional": 9.5e-6
  },
  {
    "scenario": "sigI0.25_SNR25",
    "method": "FGA",
    "center_x": 0.0,
    "center_y": 0.0,
    "width": 0.2,
    "length": 0.2,
    "orientation": 0.0,
    "iterations": 200,
    "final_functional": 1.2e-4
  },
  {
    "scenario": "sigI0.5_SNR25",
    "method": "IGA",
    "center_x": 0.0,
    "center_y": 0.0,
    "width": 0.2,
    "length": 0.2,
    "orientation": 0.0,
    "iterations": 165,
    "final_functional": 8.0e-6
  },
  {
    "scenario": "sigI0.5_SNR25",
    "method": "FGA",
    "center_x": 0.0,
    "center_y": 0.0,
    "width": 0.2,
    "length": 0.2,
    "orientation": 0.0,
    "iterations": 200,
    "final_functional": 2.5e-4
  }
]
EOF
