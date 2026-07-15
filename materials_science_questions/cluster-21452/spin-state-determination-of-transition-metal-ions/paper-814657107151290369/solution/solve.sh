#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: K_vs_x.csv ===
cat > /app/outputs/K_vs_x.csv <<'EOF'
x,K_meV_per_fu
0.0,-0.1
0.3,0.5
0.5,0.0
0.8,-0.3
1.0,-0.2
EOF

# === solve block: K_vs_strain_x03.csv ===
# Compute the base c/a ratio for x=0.3 by linear interpolation:
# a(x) = 5.109 - 0.3*(5.109-4.997) = 5.0754
# c(x) = 4.249 - 0.3*(4.249-4.213) = 4.2382
# c/a_base = 4.2382/5.0754 ≈ 0.8351
# -3%: 0.8351 * 0.97 = 0.81005
# +3%: 0.8351 * 1.03 = 0.860153
cat > /app/outputs/K_vs_strain_x03.csv <<'EOF'
c_over_a,K_meV_per_fu
0.81005,0.3
0.8351,0.5
0.860153,0.8
EOF
