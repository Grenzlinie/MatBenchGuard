#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: free_energies.json ===
cat > "$OUTDIR/free_energies.json" <<'FFEOF'
{
  "Cu-C3N4": {
    "CO_to_CHO": 0.29,
    "CHO_CO_coupling": 0.36
  },
  "Cu3N(100)": {
    "CO_to_CHO": 0.37,
    "CHO_CO_coupling": -0.21
  },
  "Cu(111)": {
    "CO_to_CHO": 0.82,
    "CHO_CO_coupling": 0.20
  },
  "Cu-C": {
    "CO_to_CHO": 0.82
  }
}
FFEOF
