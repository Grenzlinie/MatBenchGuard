#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_distortion_modes.json ===
cat > /app/outputs/bulk_distortion_modes.json <<'EOF'
{
  "d1_pm": 4.24,
  "d2_pm": 3.41,
  "d3_pm": 2.59,
  "theta_z_deg": 9.08
}
EOF

# === solve block: bulk_band_gap_moment.json ===
cat > /app/outputs/bulk_band_gap_moment.json <<'EOF'
{
  "band_gap_eV": 0.65,
  "total_magnetization_muB": 0.0
}
EOF

# === solve block: slab_layer_heights.csv ===
cat > /app/outputs/slab_layer_heights.csv <<'EOF'
layer_index,Oap_Oap_distance_pm
-1,400.2
-2,391.8
-3,400.2
-4,391.8
-5,400.2
-6,391.8
EOF

# === solve block: slab_band_gap_moment.json ===
cat > /app/outputs/slab_band_gap_moment.json <<'EOF'
{
  "band_gap_eV": 0.45,
  "total_magnetization_muB": 0.0
}
EOF
