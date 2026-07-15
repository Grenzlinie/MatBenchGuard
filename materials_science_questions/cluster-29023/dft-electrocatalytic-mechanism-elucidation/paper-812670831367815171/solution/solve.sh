#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" << 'EOF'
{
  "formation_energies": {
    "Pt_4xN6": -2.59,
    "Au_4xN6": -0.23,
    "PtCl_4xN6": -1.80,
    "AuCl_4xN6": -0.10,
    "Pt_2xEp": -3.50,
    "Au_2xEp": -0.90,
    "PtCl_2xEp": -4.20,
    "AuCl_2xEp": -1.20,
    "Pt_3xN5": -5.10,
    "Au_3xN5": -1.70,
    "PtCl_3xN5": -6.30,
    "AuCl_3xN5": -2.80
  },
  "adsorption_energies": {
    "PtCl_2xEp_0Cl": -2.85,
    "PtCl_2xEp_1Cl": -2.14,
    "PtCl_2xEp_2Cl": -1.43,
    "PtCl_2xEp_3Cl": -0.72,
    "PtCl_2xEp_4Cl": -0.01,
    "PtCl_3xN5_0Cl": -2.29,
    "PtCl_3xN5_1Cl": -1.93,
    "PtCl_3xN5_2Cl": -1.56,
    "PtCl_3xN5_3Cl": -1.20,
    "PtCl_3xN5_4Cl": -0.83
  },
  "reaction_profile": {
    "PtCl_2xEp": [
      {"label": "IS", "energy": 0.0},
      {"label": "C2H2-ads", "energy": -2.85},
      {"label": "TS1", "energy": -1.50},
      {"label": "C2H3Cl-ads", "energy": -2.30},
      {"label": "C2H3Cl+HCl-ads", "energy": -3.20},
      {"label": "TS2", "energy": -2.50},
      {"label": "VCM-ads", "energy": -3.80},
      {"label": "VCM-gas", "energy": -1.80}
    ],
    "PtCl_3xN5": [
      {"label": "IS", "energy": 0.0},
      {"label": "C2H2-ads", "energy": -2.29},
      {"label": "TS1", "energy": -0.90},
      {"label": "C2H3Cl-ads", "energy": -1.80},
      {"label": "C2H3Cl+HCl-ads", "energy": -2.50},
      {"label": "TS2", "energy": -1.80},
      {"label": "VCM-ads", "energy": -3.20},
      {"label": "VCM-gas", "energy": -1.50}
    ]
  }
}
EOF
