#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: poisson_ratios_neutral.csv ===
cat > "$OUTDIR/poisson_ratios_neutral.csv" <<'FFEOF'
material,v_zx,v_zy,v_yx,v_xy
SnS,-0.004,0.404,0.422,0.961
SnSe,-0.210,0.352,0.423,0.851
GeS,-0.208,0.411,0.420,1.401
GeSe,0.583,-0.433,0.391,1.039
FFEOF

# === solve block: poisson_zy_doping.csv ===
cat > /app/outputs/poisson_zy_doping.csv <<'FFEOF'
doping_electrons_per_atom,v_zy
0.0,-0.433
0.025,-0.1
0.050,0.2
0.075,0.55
0.100,0.895
FFEOF

# === solve block: poisson_zx_strain.csv ===
cat > /app/outputs/poisson_zx_strain.csv <<'FFEOF'
strain_eps_x,v_zx
0.0,0.583
0.02,0.583
0.04,0.583
0.05,0.583
0.055,0.583
0.06,-0.433
0.07,-0.433
0.08,-0.433
0.10,-0.433
0.12,-0.433
0.14,-0.433
FFEOF
