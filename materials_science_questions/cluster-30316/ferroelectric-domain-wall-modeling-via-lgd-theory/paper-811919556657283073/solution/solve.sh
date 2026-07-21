#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: polarization_tunneling_freq.txt ===
cat > /app/outputs/polarization_tunneling_freq.txt <<'FFEOF'
7.5e3
FFEOF

# === solve block: domain_wall_tunneling_freq.txt ===
cat > /app/outputs/domain_wall_tunneling_freq.txt <<'FFEOF'
8.8e2
FFEOF
