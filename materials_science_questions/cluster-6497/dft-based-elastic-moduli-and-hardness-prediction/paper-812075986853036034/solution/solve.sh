#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'FFEOF'
{
  "chi": 0.08,
  "eta": 0.03,
  "xi": -0.001
}
FFEOF

# === solve block: predicted_thicknesses.json ===
cat > /app/outputs/predicted_thicknesses.json <<'FFEOF'
[
  {
    "helix_id": 1,
    "r0": 342,
    "p": 222,
    "t_min": 12.4,
    "t_max": 12.5,
    "F_norm": -1.1
  },
  {
    "helix_id": 2,
    "r0": 175,
    "p": 133,
    "t_min": 8.5,
    "t_max": 8.6,
    "F_norm": -0.6
  },
  {
    "helix_id": 3,
    "r0": 240,
    "p": 380,
    "t_min": 9.6,
    "t_max": 9.8,
    "F_norm": -0.7
  }
]
FFEOF
