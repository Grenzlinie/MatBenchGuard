#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: tc_o_distances.json ===
cat > "$OUTDIR/tc_o_distances.json" <<'EOF'
{
  "tc_o_distance_25C": 1.98,
  "tc_o_distance_600C": 1.79
}
EOF

# === solve block: energy_difference.json ===
cat > "$OUTDIR/energy_difference.json" <<'EOF'
{
  "energy_difference_subsurface_surface": 2.5
}
EOF

# === solve block: doping_thermodynamics.json ===
cat > "$OUTDIR/doping_thermodynamics.json" <<'EOF'
{
  "keq_undoped": 0.15,
  "deltaG_undoped": 14.2,
  "keq_Ni": 0.56,
  "deltaG_Ni": 4.3,
  "keq_Zn": 2.79,
  "deltaG_Zn": -7.7,
  "keq_Co": 21.80,
  "deltaG_Co": -23.1
}
EOF
