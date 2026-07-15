#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_structural_metrics.json ===
cat > /app/outputs/step_01_structural_metrics.json <<'FFEOF'
{
  "temp_120_K": {
    "Fe_N_bonds": [1.971, 1.971, 2.019, 2.019, 1.952, 1.952],
    "Fe_N_av": 1.981,
    "trigonal_distortion_Phi": 3.7,
    "octahedral_distortion_Sigma": 53.4,
    "Fe_N3_C12_angle": 171.2,
    "intermolecular_contacts": {
      "C1...C10_i": 3.526,
      "C2...C9_i": 3.507,
      "C2...C10_i": 3.488,
      "C3...C7_i": 3.443,
      "C3...C8_i": 3.586,
      "C3...C12_i": 3.589,
      "C4...C7_i": 3.434,
      "C4...C8_i": 3.460,
      "C5...C8_i": 3.575,
      "C10...C12_i": 3.616,
      "C1...C4_ii": 3.589,
      "C2...C4_ii": 3.543,
      "C4...C12_ii": 3.457,
      "C3...C6_ii": 3.439,
      "C2...C6_ii": 3.522,
      "C2...C5_ii": 3.434,
      "C1...C5_ii": 3.375,
      "C12...C5_ii": 3.524,
      "C8...C9_iii": 3.579
    }
  },
  "temp_325_K": {
    "Fe_N_bonds": [2.154, 2.154, 2.167, 2.167, 2.116, 2.116],
    "Fe_N_av": 2.146,
    "trigonal_distortion_Phi": 5.4,
    "octahedral_distortion_Sigma": 72.8,
    "Fe_N3_C12_angle": 168.7,
    "intermolecular_contacts": {
      "C1...C10_i": 3.543,
      "C2...C9_i": 3.589,
      "C2...C10_i": 3.617,
      "C3...C7_i": 3.456,
      "C3...C8_i": 3.668,
      "C3...C12_i": 3.659,
      "C4...C7_i": 3.517,
      "C4...C8_i": 3.629,
      "C5...C8_i": 3.687,
      "C10...C12_i": 3.556,
      "C1...C4_ii": 3.599,
      "C2...C4_ii": 3.582,
      "C4...C12_ii": 3.551,
      "C3...C6_ii": 3.548,
      "C2...C6_ii": 3.632,
      "C2...C5_ii": 3.529,
      "C1...C5_ii": 3.440,
      "C12...C5_ii": 3.618,
      "C8...C9_iii": 3.586
    }
  },
  "Delta_Fe_N_av": 0.165
}
FFEOF
