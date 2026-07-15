#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_boundary_energy.json ===
cat > /app/outputs/step_01_boundary_energy.json <<'EOF'
{
  "grain_boundary_energy": 0.09,
  "surface_energy": 0.92,
  "work_of_cohesion": 1.75
}
EOF

# === solve block: step_02_migration_barriers.csv ===
cat > /app/outputs/step_02_migration_barriers.csv <<'EOF'
distance_from_interface,mechanism,activation_energy
0.0,O-O,1.00
0.2,O-O,0.98
0.4,O-O,0.94
0.6,O-O,0.87
0.8,O-O,0.80
1.0,O-O,0.76
1.2,O-O,0.74
0.0,O-T-O_boundary_vac,0.46
0.2,O-T-O_boundary_vac,0.40
0.4,O-T-O_boundary_vac,0.35
0.6,O-T-O_boundary_vac,0.31
0.8,O-T-O_boundary_vac,0.27
1.0,O-T-O_boundary_vac,0.25
1.2,O-T-O_boundary_vac,0.23
0.0,O-T-O_bulk_vac,0.46
0.2,O-T-O_bulk_vac,0.39
0.4,O-T-O_bulk_vac,0.34
0.6,O-T-O_bulk_vac,0.30
0.8,O-T-O_bulk_vac,0.26
1.0,O-T-O_bulk_vac,0.24
1.2,O-T-O_bulk_vac,0.23
EOF
