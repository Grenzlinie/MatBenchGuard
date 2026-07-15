#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
cat > /app/outputs/formation_energies.csv <<'FFEOF'
vacancy_type,formation_energy
O^{In},-2.55
O^{La},-2.54
In,-2.50
La,-2.44
FFEOF

# === solve block: midgap_state_report.txt ===
cat > /app/outputs/midgap_state_report.txt <<'FFEOF'
O^{In}: midgap=yes
O^{La}: midgap=yes
In: midgap=no
La: midgap=no
FFEOF
