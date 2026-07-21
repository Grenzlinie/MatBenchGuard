#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: angular_width_static.csv ===
cat > "/app/outputs/angular_width_static.csv" <<'EOF'
incidence_energy_eV,angular_width_deg
0.03,25.0
0.1,22.0
0.5,12.0
1.0,10.0
10.0,18.0
100.0,55.0
EOF

# === solve block: angular_width_600K.csv ===
cat > "/app/outputs/angular_width_600K.csv" <<'EOF'
incidence_energy_eV,angular_width_deg
0.03,45.0
0.1,40.0
0.5,35.0
1.0,18.0
10.0,25.0
100.0,60.0
EOF

# === solve block: sticking_probability_600K.csv ===
cat > "/app/outputs/sticking_probability_600K.csv" <<'EOF'
incidence_energy_eV,sticking_probability
0.03,0.55
0.1,0.35
0.5,0.02
1.0,0.0
10.0,0.0
100.0,0.25
EOF
