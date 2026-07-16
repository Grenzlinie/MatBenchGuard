#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: U_J_values.csv ===
cat > "$OUTDIR/U_J_values.csv" <<'EOF'
material,subspace,U,J
CZTS,Cu 3d,9.68,0.86
CZTS,Sn 5s,2.50,0.67
CZTS,S 3p,4.74,0.57
CZGS,Cu 3d,10.02,0.89
CZGS,Ge 4s,3.11,0.79
CZGS,S 3p,4.65,0.57
EOF

# === solve block: bandgaps.csv ===
cat > "$OUTDIR/bandgaps.csv" <<'EOF'
material,functional,bandgap
CZTS,PBE+U_eff,1.47
CZTS,PBE+U+J,1.17
CZTS,PBE+BLOR,1.47
CZGS,PBE+U_eff,1.88
CZGS,PBE+U+J,1.58
CZGS,PBE+BLOR,1.88
EOF

# === solve block: defect_formation_energies.csv ===
cat > "$OUTDIR/defect_formation_energies.csv" <<'EOF'
material,formation_energy
CZTS,0.580
CZGS,0.505
EOF
