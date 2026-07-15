#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nitro_group_charges.csv ===
cat > "/app/outputs/nitro_group_charges.csv" <<'FFEOF'
tautomer,q_NO2
ANTONO-1,0.550
ANTONO-2,0.537
ANTONO-3,0.976
ANTONO-4,0.201
ANTONO-5,0.112
ANTONO-6,0.135
ANTONO-7,0.210
ANTONO-8,0.536
ANTONO-9,0.159
ANTONO-10,0.126
ANTONO-11,0.511
ANTONO-12,0.566
ANTONO-13,0.229
ANTONO-14,0.176
ANTONO-15,0.059
FFEOF
