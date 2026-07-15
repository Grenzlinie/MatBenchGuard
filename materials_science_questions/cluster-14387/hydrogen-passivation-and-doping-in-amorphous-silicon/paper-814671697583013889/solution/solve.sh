#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dos_slab.csv ===
{ echo "energy_eV,total_dos"; python3 /solution/gen_dos.py slab; } > "$OUTDIR/dos_slab.csv"

# === solve block: dos_isolated_H.csv ===
python3 /solution/gen_dos.py isolated > "$OUTDIR/dos_isolated_H.csv"

# === solve block: dos_two_H.csv ===
python3 /solution/gen_dos.py two > "$OUTDIR/dos_two_H.csv"

# === solve block: dos_three_H.csv ===
python3 /solution/gen_dos.py three > "$OUTDIR/dos_three_H.csv"

# === solve block: summary.json ===
cat > "$OUTDIR/summary.json" << 'FFEOF'
{
  "slab": {
    "band_gap_width_eV": 5.5,
    "has_gap_states": false,
    "gap_states_energies_eV": []
  },
  "isolated_H": {
    "band_gap_width_eV": 5.5,
    "has_gap_states": true,
    "gap_states_energies_eV": [0.0]
  },
  "two_H": {
    "band_gap_width_eV": 5.5,
    "has_gap_states": false,
    "gap_states_energies_eV": []
  },
  "three_H": {
    "band_gap_width_eV": 5.5,
    "has_gap_states": true,
    "gap_states_energies_eV": [-0.8, 0.3]
  }
}
FFEOF
