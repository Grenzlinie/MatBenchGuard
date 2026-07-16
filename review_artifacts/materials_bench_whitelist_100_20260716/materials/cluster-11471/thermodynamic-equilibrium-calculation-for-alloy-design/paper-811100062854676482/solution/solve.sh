#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: cementite_Mn_vs_temperature.csv ===
cat > "${OUTDIR}/cementite_Mn_vs_temperature.csv" <<'EOF'
temperature_C,Mn_content_mass_pct
500,22.0
550,20.0
600,18.5
650,17.0
700,13.0
750,9.0
EOF

# === solve block: equilibrium_austenite_Ms_vs_temperature.csv ===
cat > "${OUTDIR}/equilibrium_austenite_Ms_vs_temperature.csv" <<'EOF'
temperature_C,Ms_C
720,230
760,275
800,325
840,385
880,435
920,465
EOF

# === solve block: paraequilibrium_driving_forces.csv ===
cat > "${OUTDIR}/paraequilibrium_driving_forces.csv" <<'EOF'
temperature_C,driving_force_gamma_cp_J_per_mol,driving_force_gamma_ap_J_per_mol
750,2500,1500
800,2000,1100
850,1600,800
900,1200,500
950,800,300
1000,600,200
EOF

# === solve block: paraequilibrium_austenite_Ms.txt ===
echo '-10' > "${OUTDIR}/paraequilibrium_austenite_Ms.txt"
