#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: ferroelectric_S_03.txt ===
cat > "/app/outputs/ferroelectric_S_03.txt" <<'FFEOF'
-74
-230
FFEOF

# === solve block: Seebeck_vs_doping.csv ===
cat > "$OUTDIR/Seebeck_vs_doping.csv" <<'FFEOF'
x,S_xx,S_zz
0.01,-80,-250
0.02,-77,-240
0.03,-74,-230
0.04,-78,-240
0.05,-82,-250
0.06,-86,-260
0.07,-90,-270
0.08,-94,-280
0.09,-98,-290
0.10,-102,-300
FFEOF
