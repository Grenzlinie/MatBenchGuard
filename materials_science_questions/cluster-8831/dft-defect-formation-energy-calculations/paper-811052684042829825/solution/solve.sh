#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_bandgap.txt ===
cat > /app/outputs/step_01_bandgap.txt <<'EOF'
1.7
2.8
EOF

# === solve block: step_02_defect_formation_energies.txt ===
cat > /app/outputs/step_02_defect_formation_energies.txt <<'EOF'
0.77
0.77
EOF

# === solve block: step_03_p_diffusion_barrier.txt ===
cat > /app/outputs/step_03_p_diffusion_barrier.txt <<'EOF'
0.013
EOF

# === solve block: step_04_conductivity_ratio.txt ===
cat > /app/outputs/step_04_conductivity_ratio.txt <<'EOF'
1e15
EOF
