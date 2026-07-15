#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "lattice_constants": {"a": 7.97, "b": 7.98, "c": 9.14, "unit": "Å"},
  "BN_bond_length": {"crystal": 1.51, "unit": "Å"},
  "lattice_energy_hf": {"value": -33.0, "unit": "kcal/mol"},
  "lattice_energy_mp2": {"value": -30.8, "unit": "kcal/mol"},
  "pair_energies": {
    "(1)-(2)": -16.0,
    "(1)-(3)": -7.3,
    "(1)-(4)": -4.3,
    "(1)-(5)": -3.9,
    "(1)-(6)": -5.2,
    "(1)-(7)": -3.9,
    "(1)-(8)": -0.9,
    "unit": "kcal/mol"
  }
}
FFEOF
