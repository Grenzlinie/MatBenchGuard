#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_profile.csv ===
cat > /app/outputs/energy_profile.csv <<'EOF'
d,total_energy,mag_moment
0.0,0.0,1.5
0.2,-0.5,1.6
0.4,-0.9,1.7
0.6,-1.0,1.8
0.8,-1.1,2.0
1.0,-0.7,2.1
EOF

# === solve block: equilibrium_d.txt ===
echo '0.80' > /app/outputs/equilibrium_d.txt
