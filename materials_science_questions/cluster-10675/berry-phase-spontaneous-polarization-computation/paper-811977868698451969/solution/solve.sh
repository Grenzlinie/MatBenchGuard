#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dipole_results.json ===
cat <<'EOF' > "$OUTDIR/dipole_results.json"
{
  "paraelectric": [
    {"ion_label": "1 (NH4+ I)", "total_dipole_D": -0.091, "pa_D": -0.091, "pb_D": 0.001, "pc_D": 0.0},
    {"ion_label": "2 (NH4+ II)", "total_dipole_D": -0.167, "pa_D": -0.147, "pb_D": 0.078, "pc_D": 0.0},
    {"ion_label": "3 (BeF4^2-)", "total_dipole_D": 0.209, "pa_D": 0.175, "pb_D": -0.116, "pc_D": 0.0}
  ],
  "ferroelectric": [
    {"ion_label": "1 (NH4+ I)", "total_dipole_D": -0.663, "pa_D": -0.638, "pb_D": 0.108, "pc_D": -0.146},
    {"ion_label": "1' (NH4+ I)", "total_dipole_D": -0.412, "pa_D": 0.410, "pb_D": -0.043, "pc_D": -0.011},
    {"ion_label": "2 (NH4+ II)", "total_dipole_D": 0.216, "pa_D": 0.051, "pb_D": 0.209, "pc_D": 0.023},
    {"ion_label": "2' (NH4+ II)", "total_dipole_D": 0.569, "pa_D": 0.007, "pb_D": 0.113, "pc_D": 0.557},
    {"ion_label": "3 (BeF4^2-)", "total_dipole_D": 0.540, "pa_D": -0.341, "pb_D": -0.148, "pc_D": -0.391},
    {"ion_label": "3' (BeF4^2-)", "total_dipole_D": 0.609, "pa_D": 0.0, "pb_D": -0.209, "pc_D": -0.572}
  ],
  "total_Ps_muC_per_cm2": 0.21
}
EOF
