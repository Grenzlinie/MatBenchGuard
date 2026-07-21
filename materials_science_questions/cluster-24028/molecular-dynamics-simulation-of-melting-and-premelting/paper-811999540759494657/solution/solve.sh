#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: predicted_phase_leads.csv ===
cat > "$OUTDIR/predicted_phase_leads.csv" <<'FFEOF'
experiment_id,predicted_phase_lead_um
1,230
2,-50
3,-33
4,-1
5,308
6,-15
7,-68
8,-20
FFEOF
