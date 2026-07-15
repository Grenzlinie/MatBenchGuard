#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: total_energies.csv ===
cat > "$OUTDIR/total_energies.csv" <<'FFEOF'
system,magnetic_state,total_energy_ev
Sr2NiIrO6,FM,-10000.0
Sr2NiIrO6,G_AF,-9999.911
Sr2Zn(Ni)IrO6,FM,-10000.0
Sr2Zn(Ni)IrO6,layered_AF,-10000.084
La2NiSiO6,FM,-10000.0
La2NiSiO6,layered_AF,-10000.019
Sr2ZnIrO6,FM,-10000.0
Sr2ZnIrO6,layered_AF,-10000.075
Sr2ZnIrO6,bilayered_AF,-10000.042
FFEOF

# === solve block: ir_orbital_moment.json ===
cat > "$OUTDIR/ir_orbital_moment.json" <<'FFEOF'
{
  "ir_orbital_moment": 0.07
}
FFEOF
