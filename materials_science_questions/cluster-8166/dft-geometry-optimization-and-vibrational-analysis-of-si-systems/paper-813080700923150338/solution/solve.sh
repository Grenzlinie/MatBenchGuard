#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'FFEOF'
{
  "C2H2_bridge_intact": 3.35,
  "C2H2_bridge_broken": 3.63,
  "C2H2_crossdimer_R": 3.75,
  "C2H2_crossdimer_A": 3.6,
  "C2H2_crossdimer_D": 3.5,
  "CH3_dangling_bond_one": 3.28,
  "CH3_dangling_bond_two": 3.21,
  "CH3_second_layer": 2.36
}
FFEOF
