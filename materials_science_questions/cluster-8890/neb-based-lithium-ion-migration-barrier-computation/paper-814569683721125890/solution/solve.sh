#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: voltage_profile.csv ===
cat > "$OUTDIR/voltage_profile.csv" << 'EOF'
x,V
0.25,1.50
0.5,1.35
0.75,1.25
1.0,1.06
EOF

# === solve block: structural_properties.json ===
cat > "$OUTDIR/structural_properties.json" << 'EOF'
{
  "volume_expansion_percent": 5.0,
  "band_gap_LiNb2O2F3_eV": 1.0,
  "interlayer_distance_delithiated_A": 3.97,
  "interlayer_distance_lithiated_A": 4.97
}
EOF

# === solve block: migration_barrier.json ===
cat > "$OUTDIR/migration_barrier.json" << 'EOF'
{
  "activation_energy_eV": 0.79,
  "pathway": "01"
}
EOF
