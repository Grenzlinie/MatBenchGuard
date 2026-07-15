#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_energies.csv ===
cat > /app/outputs/binding_energies.csv <<'FFEOF'
separation_rank,binding_energy_ev
1,0.64
2,0.30
4,0.10
8,0.05
FFEOF
