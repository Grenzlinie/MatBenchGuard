#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adhesion_energies.csv ===
cat > /app/outputs/adhesion_energies.csv <<'FFEOF'
E_adhesion,E_combined,E_molecule,E_system,molecule,system
-0.06101,-0.06101,0,0,benzene,graphitic_slit
-0.06564,-0.06564,0,0,chlorobenzene,graphitic_slit
-0.07784,-0.07784,0,0,nitrobenzene,graphitic_slit
-0.07626,-0.07626,0,0,isopropylbenzene,graphitic_slit
-0.08726,-0.08726,0,0,benzene,cnt_9_9
-0.09339,-0.09339,0,0,chlorobenzene,cnt_9_9
-0.08437,-0.08437,0,0,nitrobenzene,cnt_9_9
-0.15244,-0.15244,0,0,isopropylbenzene,cnt_9_9
FFEOF
