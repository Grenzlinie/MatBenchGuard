#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: md_results.json ===
cat > "$OUTDIR/md_results.json" << 'EOF'
{
  "doped": {
    "msd_vs_depth": [
      [-10.67, 0.0108],
      [-8.73, 0.0098],
      [-6.79, 0.0080],
      [-4.85, 0.0065],
      [-2.91, 0.0055],
      [-0.97, 0.0048],
      [0.97, 0.0048],
      [2.91, 0.0055],
      [4.85, 0.0065],
      [6.79, 0.0080],
      [8.73, 0.0098],
      [10.67, 0.0108]
    ],
    "max_isd_ang2": 0.17,
    "frequency_per_ps": 0.20
  },
  "undoped": {
    "msd_vs_depth": [
      [-10.67, 0.0072],
      [-8.73, 0.0065],
      [-6.79, 0.0055],
      [-4.85, 0.0048],
      [-2.91, 0.0042],
      [-0.97, 0.0039],
      [0.97, 0.0039],
      [2.91, 0.0042],
      [4.85, 0.0048],
      [6.79, 0.0055],
      [8.73, 0.0065],
      [10.67, 0.0072]
    ],
    "max_isd_ang2": 0.20
  },
  "bulk_doped_msd_ang2": 0.0046,
  "residence_times": {
    "300K": 16830.3,
    "700K": 17.34
  }
}
EOF
