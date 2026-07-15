#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetic_properties.json ===
cat > "$OUTDIR/magnetic_properties.json" <<'EOF'
[
  {
    "x": 0.0,
    "magnetic_moment_muB_per_fu": 0.815,
    "ground_state": "A-AFM"
  },
  {
    "x": 0.25,
    "magnetic_moment_muB_per_fu": 0.95,
    "ground_state": "FM"
  },
  {
    "x": 0.5,
    "magnetic_moment_muB_per_fu": 0.8,
    "ground_state": "FM"
  },
  {
    "x": 0.75,
    "magnetic_moment_muB_per_fu": 0.4,
    "ground_state": "FM"
  },
  {
    "x": 1.0,
    "magnetic_moment_muB_per_fu": 0.0,
    "ground_state": "NM"
  }
]
EOF

# === solve block: ferroelectric_properties.json ===
cat > "$OUTDIR/ferroelectric_properties.json" <<'EOF'
{
  "cis": {
    "unstrained": {
      "double_well_depth_meV_per_fu": 80,
      "polar_space_group": "Pmc2_1"
    },
    "out_of_plane_strain": {
      "double_well_depth_meV_per_fu": 238,
      "polar_space_group": "Pmc2_1"
    },
    "in_plane_strain": {
      "double_well_depth_meV_per_fu": 83,
      "polar_space_group": "Pm"
    }
  },
  "trans": {
    "unstrained": {
      "double_well_depth_meV_per_fu": 37,
      "polar_space_group": "I4cm"
    },
    "out_of_plane_strain": {
      "double_well_depth_meV_per_fu": 68,
      "polar_space_group": "I4cm"
    },
    "in_plane_strain": {
      "double_well_depth_meV_per_fu": 0,
      "polar_space_group": "Fmmm"
    }
  }
}
EOF
