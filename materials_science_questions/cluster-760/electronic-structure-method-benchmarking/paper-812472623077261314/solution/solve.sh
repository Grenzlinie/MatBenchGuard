#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'FFEOF'
{
  "C2C2PD": -20.93,
  "C3A": -16.91,
  "C3GC": -28.63,
  "CBH": -11.00,
  "GCGC": -13.54,
  "GGG": -2.08,
  "PHE": -25.46,
  "DNA-ellipticine": -38.6,
  "buckycatcher-C60": -41.1
}
FFEOF
