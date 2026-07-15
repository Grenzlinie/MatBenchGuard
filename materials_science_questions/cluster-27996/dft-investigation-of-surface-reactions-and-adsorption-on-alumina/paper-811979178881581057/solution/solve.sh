#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "adsorption_energy_eV": 5.74,
  "C-H_bond_length_angstrom": 1.10,
  "C-O_bond_length_angstrom": 1.23,
  "H-C-H_angle_degrees": 118.4,
  "NBO_charge_H2CO_e": 0.12,
  "vas_CH_cm-1": 3009,
  "vs_CH_cm-1": 2897,
  "v_CO_cm-1": 1701,
  "ds_CH2_cm-1": 1492
}
EOF
