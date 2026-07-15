#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ir_peak_assignments.csv ===
cat > "$OUTDIR/ir_peak_assignments.csv" <<'FFEOF'
frequency,direction,dominant_species
59,in_plane,Na
88,in_plane,Na
115,mixed,"Al, Os, Na"
146,out_of_plane,Na
162,out_of_plane,"Na, Al"
192,out_of_plane,"Al, Os"
217,in_plane,"Al, Os"
246,in_plane,"Al, Os"
FFEOF

# === solve block: thermodynamic_properties.json ===
cat > "$OUTDIR/thermodynamic_properties.json" <<'FFEOF'
{"Cv":410,"S":300,"U":370,"F":280}
FFEOF
