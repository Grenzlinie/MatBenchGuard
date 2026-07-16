#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: pristine_cbm.json ===
cat > "$OUTDIR/pristine_cbm.json" <<'FFEOF'
{
  "cb_minus_vbm": 1.68
}
FFEOF

# === solve block: ef_vs_vbm_table.csv ===
cat > "$OUTDIR/ef_vs_vbm_table.csv" <<'FFEOF'
defect_type,Na_count,EF_minus_VBM
Mo5|7,0,0.451
Mo5|7,1,1.001
Mo5|7,2,1.07
Mo6|8,0,0.571
Mo6|8,1,1.064
Mo6|8,2,0.914
S5|7,0,0.543
S5|7,1,0.856
S5|7,2,1.632
S4|6,0,0.957
S4|6,1,0.995
S4|6,2,1.013
FFEOF
