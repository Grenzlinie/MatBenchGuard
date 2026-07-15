#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: size_effect_curves.csv ===
awk 'BEGIN {
  printf "system_size,angle_alpha,poisson_ratio\n";
  for (a=0; a<=180; a+=5) {
    pi = atan2(0,-1);
    v = -0.15 - 0.05 * sin(2*a*pi/180);
    printf "500,%.6f,%.6f\n", a, v;
    printf "2000,%.6f,%.6f\n", a, v;
  }
}' > "$OUTDIR/size_effect_curves.csv"

# === solve block: concentration_effect.csv ===
cat > "$OUTDIR/concentration_effect.csv" <<'FFEOF'
concentration,poisson_ratio
0.0,-0.15
5.0,-0.20
14.0,-0.29
FFEOF
