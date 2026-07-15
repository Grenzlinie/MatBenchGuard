#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: barriers.json ===
cat > /app/outputs/barriers.json <<'FFEOF'
{"gamma_alumina_barrier": 2.2, "eta_alumina_barrier": 5.0}
FFEOF

# === solve block: neb_gamma_alumina.xyz ===
python3 /solution/generate_xyz.py gamma /app/outputs/neb_gamma_alumina.xyz

# === solve block: neb_eta_alumina.xyz ===
python3 /solution/generate_xyz.py eta /app/outputs/neb_eta_alumina.xyz
