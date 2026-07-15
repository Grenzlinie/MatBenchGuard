#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: bulk_lattice_constant.json ===
cat > "$OUTDIR/bulk_lattice_constant.json" <<'FFEOF'
{
  "a_angstrom": 8.090
}
FFEOF

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'FFEOF'
{
  "NH3_110": -1.774,
  "NH3_111": -1.638,
  "NH3_100": -1.354,
  "NH2_110": -2.850,
  "NH_110": -3.560,
  "N_110": -4.669
}
FFEOF
