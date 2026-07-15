#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: plane_strain_moduli.json ===
cat > "$OUTDIR/plane_strain_moduli.json" <<'FFEOF'
{
  "EB_AFM_MPa": 42.40,
  "EB_FESEM_MPa": 35.74
}
FFEOF
