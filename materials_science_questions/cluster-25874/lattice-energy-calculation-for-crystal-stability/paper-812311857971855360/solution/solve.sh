#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: observed_lattice_energy.json ===
cat > /app/outputs/observed_lattice_energy.json <<'FFEOF'
{
  "total": -101.3,
  "van_der_Waals": -61.2,
  "Coulombic": -11.0,
  "hydrogen_bond": -29.1
}
FFEOF

# === solve block: alternative_lattice_energy.json ===
cat > /app/outputs/alternative_lattice_energy.json <<'FFEOF'
{
  "total": -79.1,
  "van_der_Waals": -63.0,
  "Coulombic": -7.0,
  "hydrogen_bond": -9.1
}
FFEOF

# === solve block: minimized_cell_parameters.json ===
cat > /app/outputs/minimized_cell_parameters.json <<'FFEOF'
{
  "observed": {
    "a": 5.88,
    "b": 5.41,
    "c": 7.12,
    "alpha": 83.6,
    "beta": 96.9,
    "gamma": 103.1
  },
  "alternative": {
    "a": 9.88,
    "b": 7.94,
    "c": 6.51,
    "alpha": 90.4,
    "beta": 154.1,
    "gamma": 87.8
  }
}
FFEOF

# === solve finalize ===
echo "Oracle artifacts written."
