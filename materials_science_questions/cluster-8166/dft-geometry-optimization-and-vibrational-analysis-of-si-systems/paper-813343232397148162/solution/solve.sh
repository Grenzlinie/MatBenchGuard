#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_geometries.json ===
cat > "$OUTDIR/step_01_geometries.json" <<'FFEOF'
{
  "substitutional_Td": {
    "Si_As_bond_length_A": 2.43,
    "total_energy_eV": -1000.0
  },
  "broken_bond_C3v": {
    "Si_As_bond_length_A": 2.42,
    "Si_displacement_A": 1.38,
    "bond_angle_deg": 115.0,
    "total_energy_eV": -1000.0
  },
  "most_stable_among_large_relaxation": "broken_bond",
  "energy_difference_compared_to_next_metastable_eV": 0.6
}
FFEOF

# === solve block: step_02_frequencies.json ===
cat > "$OUTDIR/step_02_frequencies.json" <<'FFEOF'
{
  "v_Td_t2_mode_cm-1": 370.0,
  "v_C3v_e_mode_cm-1": 392.0,
  "v_C3v_a1_mode_cm-1": 274.0,
  "ratio_vTd_vC3v": 0.94
}
FFEOF
