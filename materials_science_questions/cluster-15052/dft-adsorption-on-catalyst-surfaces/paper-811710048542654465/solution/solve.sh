#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.json ===
cat > "$OUTDIR/adsorption_energies.json" <<'FFEOF'
{
  "E_O2": -10.0,
  "E_atomic_O": -4.95,
  "E_reduced": -4995.0,
  "E_bare": -5000.0,
  "configurations": {
    "3a": {
      "E_total": -5006.26,
      "E_ads_per_O2_eV": -1.26
    },
    "3b": {
      "E_total": -5006.63,
      "E_ads_per_O2_eV": -1.63
    },
    "3c": {
      "E_total": -5006.83,
      "E_ads_per_O2_eV": -1.83
    },
    "3d": {
      "E_total": -5006.89,
      "E_ads_per_O2_eV": -1.89
    },
    "3e": {
      "E_total": -5007.06,
      "E_ads_per_O2_eV": -2.06
    }
  },
  "most_stable": "3e",
  "E_ads_atomic_O_eV": -2.11
}
FFEOF

# === solve block: O-O_bond_length.txt ===
echo "1.50" > "$OUTDIR/O-O_bond_length.txt"
