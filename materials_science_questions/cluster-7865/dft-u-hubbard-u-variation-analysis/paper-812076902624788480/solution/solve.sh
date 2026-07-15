#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "configurations": [
    {
      "magnetic_ordering": "AFM",
      "total_energy_meV": 0,
      "spin_moment_muB": 0.91,
      "band_gap_eV": 1.71
    },
    {
      "magnetic_ordering": "F+AF",
      "total_energy_meV": 0.6,
      "spin_moment_muB": 0.91,
      "band_gap_eV": 1.66
    },
    {
      "magnetic_ordering": "AF+F",
      "total_energy_meV": 54,
      "spin_moment_muB": 0.92,
      "band_gap_eV": 1.5
    },
    {
      "magnetic_ordering": "FM",
      "total_energy_meV": 53,
      "spin_moment_muB": 0.93,
      "band_gap_eV": 1.35
    }
  ],
  "derived_exchange_couplings": {
    "J_inter_K": 7,
    "J_intra_K": 626
  }
}
FFEOF
