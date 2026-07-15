#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: hopfield_parameters.json ===
cat > "$OUTDIR/hopfield_parameters.json" <<'EOF'
{
  "5.4": {
    "lattice_constant_bohr": 5.4,
    "pressure_gpa": 128.0,
    "eta_F_ev_per_ang2": 17.5,
    "eta_pd_contribution_ev_per_ang2": 13.7
  },
  "5.6": {
    "lattice_constant_bohr": 5.6,
    "pressure_gpa": 82.0,
    "eta_F_ev_per_ang2": 13.9,
    "eta_pd_contribution_ev_per_ang2": 11.3
  }
}
EOF
