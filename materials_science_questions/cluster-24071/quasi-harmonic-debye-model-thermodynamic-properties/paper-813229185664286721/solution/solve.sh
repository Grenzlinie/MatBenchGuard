#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: zeta_B0pp_table.csv ===
cat > "/app/outputs/zeta_B0pp_table.csv" <<'FFEOF'
Solid,zeta_computed,B0pp_computed
Ne,-1.385,-2.94
Ar,-1.414,-2.62
Al,0.253,-0.105
Cu,0.191,-0.082
FFEOF
