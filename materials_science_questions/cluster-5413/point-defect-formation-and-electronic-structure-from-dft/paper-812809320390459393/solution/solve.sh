#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: motif_properties.json ===
cat > "$OUTDIR/motif_properties.json" <<'JSONEOF'
{
  "A": {
    "delta_H_eV": 0.0,
    "H1_chemical_shifts_ppm": [3.4, 3.4]
  },
  "G": {
    "delta_H_eV": 0.0,
    "H1_chemical_shifts_ppm": [3.3, 3.3, 3.5, 3.5]
  },
  "H": {
    "delta_H_eV": 0.22,
    "H1_chemical_shifts_ppm": [1.9, 1.9, 6.8, 6.8]
  },
  "I": {
    "delta_H_eV": 0.33,
    "H1_chemical_shifts_ppm": [1.5, 1.5, 6.3, 6.3]
  },
  "J": {
    "delta_H_eV": 0.37,
    "H1_chemical_shifts_ppm": [2.2, 3.8, 6.8, 8.6]
  }
}
JSONEOF

# === solve finalize ===
# No further steps required
