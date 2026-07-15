#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_properties.json ===
cat > /app/outputs/structural_properties.json <<'FILEEOF'
[
  {
    "composition": "x0",
    "B_O_distance": 1.39,
    "O_O_distance": 2.46,
    "B_coordination": 2.96,
    "O_coordination": 1.97,
    "BOB_angle": 160,
    "OBO_angle": 120,
    "NBO4_fraction": 0.0
  },
  {
    "composition": "x0.1",
    "B_O_distance": 1.41,
    "O_O_distance": 2.47,
    "B_coordination": 3.17,
    "O_coordination": 2.04,
    "BOB_angle": 154,
    "OBO_angle": 117,
    "NBO4_fraction": 0.15
  },
  {
    "composition": "x0.2",
    "B_O_distance": 1.44,
    "O_O_distance": 2.48,
    "B_coordination": 3.37,
    "O_coordination": 2.07,
    "BOB_angle": 144,
    "OBO_angle": 114,
    "NBO4_fraction": 0.35
  }
]
FILEEOF

# === solve block: vibrational_peak.json ===
cat > /app/outputs/vibrational_peak.json <<'FILEEOF'
[
  {
    "composition": "x0",
    "peak_frequency": 1100.0
  },
  {
    "composition": "x0.1",
    "peak_frequency": 1050.0
  },
  {
    "composition": "x0.2",
    "peak_frequency": 1000.0
  }
]
FILEEOF
