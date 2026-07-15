#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_fractions.csv ===
cat > /app/outputs/phase_fractions.csv <<'EOF'
depth_um,f_graphite,f_ferrite,f_pearlite,f_austenite,f_ledeburite,f_martensite
0,0.0,0.0,0.0,0.0,0.92,0.08
100,0.02,0.25,0.0,0.18,0.50,0.05
200,0.04,0.60,0.0,0.25,0.10,0.01
300,0.1165,0.8835,0.0,0.0,0.0,0.0
400,0.1165,0.8835,0.0,0.0,0.0,0.0
EOF

# === solve block: layer_thickness.json ===
cat > /app/outputs/layer_thickness.json <<'EOF'
{
  "case": "V2",
  "ledeburite_martensite_layer_thickness_um": 220
}
EOF
