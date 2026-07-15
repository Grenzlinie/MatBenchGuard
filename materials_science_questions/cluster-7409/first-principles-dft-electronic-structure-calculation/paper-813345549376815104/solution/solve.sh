#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: electronic_structure_results.json ===
cat > "$OUTDIR/electronic_structure_results.json" <<'FFEOF'
{
  "VCP": {
    "band_gap_eV": 2.20,
    "in_gap_levels": [
      {"energy_above_VBM_eV": 1.30, "dominant_orbital": "Pr_4f"},
      {"energy_above_VBM_eV": 2.06, "dominant_orbital": "Pr_4f"}
    ],
    "binding_energy_eV": -3.30,
    "average_Pr_O_bond_length_A": 2.43
  },
  "ZCP": {
    "band_gap_eV": 2.20,
    "in_gap_levels": [
      {"energy_above_VBM_eV": 1.22, "dominant_orbital": "Pr_4f"},
      {"energy_above_VBM_eV": 2.00, "dominant_orbital": "Pr_4f"}
    ],
    "binding_energy_eV": -0.02,
    "average_Pr_O_bond_length_A": 2.44
  },
  "ZTP": {
    "band_gap_eV": 2.20,
    "in_gap_levels": [
      {"energy_above_VBM_eV": 1.20, "dominant_orbital": "Pr_4f"},
      {"energy_above_VBM_eV": 1.92, "dominant_orbital": "Pr_4f"}
    ],
    "binding_energy_eV": -3.16,
    "average_Pr_O_bond_length_A": 2.42
  }
}
FFEOF
