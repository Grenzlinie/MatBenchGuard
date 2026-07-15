#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation.json ===
cat > "$OUTDIR/step_01_formation.json" << 'EOF'
{
  "divacancies": [
    {
      "label": "V2V3",
      "FEVH2_eV": 2.11,
      "V_V_distance_ang": 2.492
    },
    {
      "label": "V1V2",
      "FEVH2_eV": 2.33,
      "V_V_distance_ang": 2.751
    },
    {
      "label": "V2V6",
      "FEVH2_eV": 2.72,
      "V_V_distance_ang": 3.010
    }
  ]
}
EOF

# === solve block: step_02_diffusion.json ===
cat > "$OUTDIR/step_02_diffusion.json" << 'EOF'
{
  "x_axis": {
    "most_favorable_mechanism": "sequential intermediate",
    "rate_determining_step_energy_eV": 1.01,
    "path_length_ang": 2.75
  },
  "y_axis": {
    "most_favorable_mechanism": "simultaneous intermediate",
    "rate_determining_step_energy_eV": 1.01,
    "path_length_ang": 2.75
  },
  "z_axis": {
    "most_favorable_mechanism": "sequential direct",
    "rate_determining_step_energy_eV": 0.93,
    "path_length_ang": 3.01
  }
}
EOF
