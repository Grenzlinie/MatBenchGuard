#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: core_widths_pair_potential.csv ===
cat > "$OUTDIR/core_widths_pair_potential.csv" <<'FFEOF'
position_a0,core_width_a0,configuration_type
-2.5,1.77,2C
-1.5,1.77,2C
-0.5,1.68,2C
0,1.94,4C
0.5,2.83,4C
1.5,2.83,4C
2.5,1.77,2C
homogeneous,1.6,2C
FFEOF

# === solve block: core_widths_nbody_potential.csv ===
cat > "$OUTDIR/core_widths_nbody_potential.csv" <<'FFEOF'
position_a0,core_width_a0,configuration_type
-2.5,1.77,4C
-1.5,1.77,2C
-0.5,1.68,2C
0,1.94,4C
0.5,2.83,9C
1.5,2.83,5C
2.5,1.77,4C
homogeneous,3.0,4C
FFEOF
