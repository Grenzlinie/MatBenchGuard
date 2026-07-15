#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_energies.csv ===
cat > "$OUTDIR/surface_energies.csv" <<'FFEOF'
surface,termination,relaxed_surface_energy_J_m2
001,2Fe,o; 4O,1.97
011,2Fe,o; 4O,1.97
111,8.5O,2.01
012,2Fe,o; 4O,1.89
112,2Fe,o; 4O,1.86
122,2Fe,o; 4O,2.23
FFEOF

# === solve block: attachment_energies.csv ===
cat > /app/outputs/attachment_energies.csv <<'FFEOF'
surface,termination,relaxed_attachment_energy_eV
001,Fe,t,12.6
011,2Fe,o; 4O,12.5
111,2Fe,o,8.4
012,2Fe,o; 4O,42.4
112,2Fe,o; 4O,38.6
122,2Fe,o; 4O,35.0
FFEOF
