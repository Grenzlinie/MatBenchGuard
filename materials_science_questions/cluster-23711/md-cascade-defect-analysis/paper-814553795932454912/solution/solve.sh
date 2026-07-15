#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: threshold_displacement_energies.csv ===
cat > "${OUTDIR}/threshold_displacement_energies.csv" <<'CSVEOF'
structure,pka_type,direction,ed_value
unfaulted,C,[001],19
unfaulted,Si,[001],95
ISF_AC,C,[001],64
ISF_AC,Si,[001],69
CSVEOF
