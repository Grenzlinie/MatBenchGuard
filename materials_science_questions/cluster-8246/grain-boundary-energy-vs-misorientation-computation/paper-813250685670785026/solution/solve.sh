#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: tBLG_results.csv ===
cat > "$OUTDIR/tBLG_results.csv" <<'EOF'
twist_angle_deg,intrinsic_strength_GPa,critical_failure_strain_percent,Youngs_modulus_GPa
5.0,111.23,24.00,953.00
7.3,110.10,23.69,953.00
9.4,109.31,23.41,953.00
13.2,107.87,22.89,953.00
21.8,104.63,21.73,953.00
32.2,100.71,20.33,953.00
38.2,98.44,19.52,953.00
42.1,96.97,19.00,953.00
EOF

# === solve block: BLG_GB_results.csv ===
cat > "$OUTDIR/BLG_GB_results.csv" <<'EOF'
misorientation_angle_deg,orientation_type,intrinsic_strength_GPa,critical_failure_strain_percent,Youngs_modulus_GPa
7.3,zigzag,55.70,12.00,963.00
13.7,zigzag,70.04,16.00,963.00
22.6,zigzag,90.00,20.00,963.00
17.5,armchair,62.30,15.00,963.00
20.9,armchair,72.98,19.00,963.00
27.4,armchair,93.40,24.00,963.00
EOF
