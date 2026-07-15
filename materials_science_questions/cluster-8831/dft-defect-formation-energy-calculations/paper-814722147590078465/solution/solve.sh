#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_04_single_cu_results.json ===
cat > "$OUTDIR/step_04_single_cu_results.json" <<'EOF'
{
  "10-0": {
    "stable_magnetic_state": "FM",
    "total_magnetic_moment": 1.0,
    "Cu_partial_magnetic_moment": 0.57,
    "Cu_O_bond_length": 1.85,
    "spin_polarization": 1.0,
    "half_metallic": true
  },
  "5-0": {
    "stable_magnetic_state": "FM",
    "total_magnetic_moment": 1.0,
    "Cu_partial_magnetic_moment": 0.58,
    "Cu_O_bond_length": 1.85,
    "spin_polarization": 1.0,
    "half_metallic": true
  }
}
EOF

# === solve block: step_05_close_cu_results.json ===
cat > "$OUTDIR/step_05_close_cu_results.json" <<'FFEOF'
{
  "10-0": {
    "stable_magnetic_state": "AFM",
    "band_gap": 0.66,
    "energy_difference_deltaE": -0.4147,
    "semiconducting": true
  },
  "5-0": {
    "stable_magnetic_state": "AFM",
    "band_gap": 0.78,
    "energy_difference_deltaE": -0.6127,
    "semiconducting": true
  }
}
FFEOF

# === solve block: step_06_far_cu_results.json ===
cat > "$OUTDIR/step_06_far_cu_results.json" <<'FFEOF'
[
  {
    "configuration_id": "a",
    "stable_magnetic_state": "FM",
    "total_magnetic_moment": 2.0,
    "Cu_partial_magnetic_moment": 0.57,
    "spin_polarization": 1.0
  },
  {
    "configuration_id": "b",
    "stable_magnetic_state": "FM",
    "total_magnetic_moment": 2.0,
    "Cu_partial_magnetic_moment": 0.57,
    "spin_polarization": 1.0
  },
  {
    "configuration_id": "c",
    "stable_magnetic_state": "FM",
    "total_magnetic_moment": 2.0,
    "Cu_partial_magnetic_moment": 0.57,
    "spin_polarization": 1.0
  }
]
FFEOF

# === solve finalize ===
echo "All outputs written."
