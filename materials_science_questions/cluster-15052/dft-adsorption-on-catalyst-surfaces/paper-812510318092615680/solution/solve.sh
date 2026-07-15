#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_barriers.csv ===
cat > /app/outputs/energy_barriers.csv <<'FFEOF'
system,step_number,barrier_ev
Ni-Cu-OOH,1,4.91
Ni-Cu-OOH,2,0.85
Ni-Cu-OOH,3,0.92
Ni-Cu-OOH,4,1.10
Ni-Cu-OOH,5,0.55
Ni-Cu-Fe-OOH,1,1.08
Ni-Cu-Fe-OOH,2,0.65
Ni-Cu-Fe-OOH,3,0.78
Ni-Cu-Fe-OOH,4,0.72
Ni-Cu-Fe-OOH,5,-0.20
FFEOF
