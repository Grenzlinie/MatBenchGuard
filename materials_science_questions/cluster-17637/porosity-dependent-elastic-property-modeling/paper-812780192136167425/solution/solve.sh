#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: mrv_size.json ===
cat > /app/outputs/mrv_size.json <<'FFEOF'
{
  "L_f_d": 24
}
FFEOF

# === solve block: effective_moduli.csv ===
cat > /app/outputs/effective_moduli.csv <<'FFEOF'
type,C_D_percent,C_d_percent,E_eff_GPa
1,80,20,2.0
2,60,40,1.736
3,40,60,1.439
4,20,80,0.971
FFEOF
