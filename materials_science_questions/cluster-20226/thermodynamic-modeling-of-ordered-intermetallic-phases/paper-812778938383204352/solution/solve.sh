#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_equilibrium_concentrations.json ===
cat > /app/outputs/step_01_equilibrium_concentrations.json <<'EOF'
{
  "phases": [
    {"phase": "A(B)", "C_L": 0.979, "C_R": 1.0, "width": 0.021},
    {"phase": "AB3", "C_L": 0.246, "C_R": 0.264, "width": 0.018},
    {"phase": "AB", "C_L": 0.491, "C_R": 0.509, "width": 0.018},
    {"phase": "A3B", "C_L": 0.736, "C_R": 0.754, "width": 0.018},
    {"phase": "B(A)", "C_L": 0.0, "C_R": 0.021, "width": 0.021}
  ]
}
EOF

# === solve block: step_02_A3B_growth_DW.csv ===
cat > /app/outputs/step_02_A3B_growth_DW.csv <<'EOF'
phase,growth_DW,Matano_DW
A3B,7.8e-14,7.0e-14
EOF

# === solve block: step_03_AB_growth_DW.csv ===
cat > /app/outputs/step_03_AB_growth_DW.csv <<'EOF'
phase,growth_DW,Matano_DW
AB,7.4e-14,7.8e-14
EOF
