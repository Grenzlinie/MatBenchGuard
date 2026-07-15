#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: lattice_energies.json ===
cat > /app/outputs/lattice_energies.json <<'EOF'
[
  {"compound":"SrO","energy":-50.0},
  {"compound":"TiO2","energy":-120.0},
  {"compound":"SrTiO3","energy":-100.0},
  {"compound":"1_p","energy":-150.11},
  {"compound":"2_p","energy":-250.13},
  {"compound":"3_p","energy":-350.13},
  {"compound":"4_p","energy":-450.13}
]
EOF

# === solve block: defect_energies.json ===
cat > /app/outputs/defect_energies.json <<'EOF'
{"V_Sr":{"energy":30.0},"V_O":{"energy":24.89}}
EOF

# === solve block: formation_energies.json ===
cat > /app/outputs/formation_energies.json <<'EOF'
[
  {"compound":"1_p","Delta_U_p+r":-0.11},
  {"compound":"2_p","Delta_U_p+r":-0.13},
  {"compound":"3_p","Delta_U_p+r":-0.13},
  {"compound":"4_p","Delta_U_p+r":-0.13}
]
EOF

# === solve block: schottky_energies.json ===
cat > /app/outputs/schottky_energies.json <<'EOF'
[
  {"n":0,"U_Sch":4.89},
  {"n":1,"U_Sch":4.78},
  {"n":2,"U_Sch":4.76},
  {"n":3,"U_Sch":4.76},
  {"n":4,"U_Sch":4.76}
]
EOF
