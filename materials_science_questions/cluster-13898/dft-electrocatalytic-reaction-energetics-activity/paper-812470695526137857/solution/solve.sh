#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: free_energy_diagram.csv ===
cat > "$OUTDIR/free_energy_diagram.csv" <<'CSVEOF'
model,intermediate,free_energy
Pt-N1-C,clean,0.0
Pt-N1-C,OOH,0.2
Pt-N1-C,O,0.4
Pt-N1-C,OH,0.2
Pt-N2-C,clean,0.0
Pt-N2-C,OOH,0.3
Pt-N2-C,O,0.6
Pt-N2-C,OH,0.3
Pt-N3-C,clean,0.0
Pt-N3-C,OOH,0.4
Pt-N3-C,O,0.8
Pt-N3-C,OH,0.4
Pt-N4-C,clean,0.0
Pt-N4-C,OOH,0.5
Pt-N4-C,O,1.0
Pt-N4-C,OH,0.5
CSVEOF
