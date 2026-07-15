#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_phase_vs_polar.csv ===
cat > /app/outputs/step_01_phase_vs_polar.csv <<'EOF'
polar_angle,phase_shift
37.0,0.52
50.0,0.63
60.0,0.74
EOF

# === solve block: step_02_phase_vs_azimuth.csv ===
cat > /app/outputs/step_02_phase_vs_azimuth.csv <<'EOF'
azimuth_offset,phase_shift
-4.0,0.55
-3.0,0.62
-2.0,0.70
-1.0,0.85
0.0,0.74
1.0,0.95
2.0,0.82
3.0,0.70
4.0,0.60
EOF
