#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relative_enthalpies.csv ===
cat > "/app/outputs/relative_enthalpies.csv" <<'FFEOF'
pressure_GPa,structure,relative_enthalpy_meV_per_H2O
0.0,hexagonal,-30.0
0.0,HCP,5.0
0.0,square,35.0
0.0,buckled-rhombic,100.0
1.0,hexagonal,10.0
1.0,HCP,10.0
1.0,square,19.0
1.0,buckled-rhombic,80.0
2.0,HCP,5.0
2.0,buckled-rhombic,40.0
3.0,HCP,5.0
3.0,buckled-rhombic,10.0
4.0,HCP,5.0
4.0,buckled-rhombic,-5.0
5.0,HCP,5.0
5.0,buckled-rhombic,-10.0
FFEOF
