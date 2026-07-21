#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reorganization_table.csv ===
cat > "$OUTDIR/reorganization_table.csv" <<'EOF'
medium,gamma,lambda_exp,lambda_out_calc,lambda_out_exp
water,0.5500,50.52,24.57,24.57
methanol-water 0.033,0.5486,50.35,24.51,24.41
methanol-water 0.060,0.5472,50.73,24.45,24.79
methanol-water 0.112,0.5445,51.46,24.31,25.52
methanol-water 0.169,0.5419,51.87,24.21,25.93
methanol-water 0.200,0.5406,51.88,24.15,25.94
methanol-water 0.265,0.5383,51.99,24.04,26.04
glycerol-water 0.020,0.5403,50.67,24.14,24.73
glycerol-water 0.036,0.5333,50.26,23.82,24.31
glycerol-water 0.077,0.5182,49.84,23.14,23.90
glycerol-water 0.131,0.5031,48.33,22.47,22.39
glycerol-water 0.165,0.4956,48.12,22.14,22.17
glycerol-water 0.233,0.4834,48.20,21.56,22.26
LiNO3 0.6,0.5438,50.58,24.29,24.64
LiNO3 1.0,0.5402,50.51,24.12,24.65
LiNO3 2.0,0.5319,51.63,23.75,25.69
LiNO3 3.0,0.5214,51.68,23.29,25.74
LiNO3 4.0,0.5069,51.63,22.64,25.69
LiNO3 5.0,0.4858,51.89,21.70,25.69
EOF
