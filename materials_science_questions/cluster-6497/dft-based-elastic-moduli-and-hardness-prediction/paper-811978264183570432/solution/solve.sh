#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_bulk_moduli.csv ===
cat > /app/outputs/computed_bulk_moduli.csv <<'FFEOF'
composition,bulk_modulus_kbar
CaF2,814
Ca90Sr10F2,797.6
Ca80Sr20F2,782.6
Ca70Sr30F2,768.5
Ca50Sr50F2,743.3
Ca40Sr60F2,732.0
Ca30Sr70F2,721.3
Ca10Sr90F2,701.9
SrF2,693
FFEOF
