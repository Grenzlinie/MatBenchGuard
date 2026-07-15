#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: relative_total_energies.json ===
cat > "$OUTDIR/relative_total_energies.json" << 'JSONEOF'
{
  "Mg3Pd5": {
    "conf1": 0.0,
    "conf2": 0.0035,
    "conf3": 1.2432,
    "conf4": 1.2429,
    "formation_energy_fu": -7.43
  },
  "Al3Pd5": {
    "conf1": 0.0,
    "conf2": 0.002265,
    "conf3": 1.6089,
    "conf4": 1.608813,
    "formation_energy_fu": -10.97
  },
  "Ga3Pd5": {
    "conf1": 0.0,
    "conf2": 0.173228,
    "conf3": 1.618081,
    "conf4": 1.616686,
    "formation_energy_fu": -7.12
  }
}
JSONEOF

# === solve block: icohp_analysis.json ===
cat > "$OUTDIR/icohp_analysis.json" << 'JSONEOF'
{
  "Mg3Pd5": {
    "A_A": {
      "total_icohp_per_cell": 10.0232,
      "percentage_contribution": 15.54
    },
    "A_Pd": {
      "total_icohp_per_cell": 47.876,
      "percentage_contribution": 74.24
    },
    "Pd_Pd": {
      "total_icohp_per_cell": 6.5928,
      "percentage_contribution": 10.22
    }
  },
  "Al3Pd5": {
    "A_A": {
      "total_icohp_per_cell": 9.9616,
      "percentage_contribution": 12.39
    },
    "A_Pd": {
      "total_icohp_per_cell": 63.4732,
      "percentage_contribution": 78.98
    },
    "Pd_Pd": {
      "total_icohp_per_cell": 6.9336,
      "percentage_contribution": 8.63
    }
  },
  "Ga3Pd5": {
    "A_A": {
      "total_icohp_per_cell": 8.8512,
      "percentage_contribution": 10.06
    },
    "A_Pd": {
      "total_icohp_per_cell": 73.4116,
      "percentage_contribution": 83.02
    },
    "Pd_Pd": {
      "total_icohp_per_cell": 6.1612,
      "percentage_contribution": 6.97
    }
  }
}
JSONEOF
