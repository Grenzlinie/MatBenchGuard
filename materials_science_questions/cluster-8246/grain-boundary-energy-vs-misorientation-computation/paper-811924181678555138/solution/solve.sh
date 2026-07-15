#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: gb_energy_data.csv ===
cat > "$OUTDIR/gb_energy_data.csv" <<'FFEOF'
tilt_axis,angle_deg,energy_Jm2
111,5,1.2
111,10,1.3
111,15,1.4
111,20,1.45
111,25,1.5
111,30,1.55
100,5,0.8
100,10,0.9
100,15,1.0
100,20,1.05
100,25,1.08
100,30,1.1
FFEOF
