#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_structural_params.json ===
cat > /app/outputs/step_01_structural_params.json <<'FFEOF'
{
  "Zr3N4": {
    "a0": 6.837,
    "B0": 211,
    "Bprime": 6.61
  },
  "Hf3N4": {
    "a0": 6.578,
    "B0": 232,
    "Bprime": 5.95
  }
}
FFEOF

# === solve block: step_02_elastic_constants.json ===
cat > /app/outputs/step_02_elastic_constants.json <<'FFEOF'
{
  "Zr3N4": {
    "C11": 310.13,
    "C12": 75.53,
    "C44": 122.43,
    "B": 153.73,
    "G": 120.32,
    "E": 280.54,
    "nu": 0.19
  },
  "Hf3N4": {
    "C11": 358.93,
    "C12": 51.02,
    "C44": 148.47,
    "B": 153.66,
    "G": 150.66,
    "E": 346.23,
    "nu": 0.12
  }
}
FFEOF

# === solve block: step_03_sound_velocities_debye.json ===
cat > /app/outputs/step_03_sound_velocities_debye.json <<'FFEOF'
{
  "Zr3N4": {
    "rho": 6.838,
    "vt": 17.595,
    "vl": 6.778,
    "vm": 9.429,
    "theta_D": 651.69
  },
  "Hf3N4": {
    "rho": 13.831,
    "vt": 0.990,
    "vl": 5.062,
    "vm": 1.132,
    "theta_D": 81.42
  }
}
FFEOF

# === solve block: step_04_optical_constants.json ===
cat > /app/outputs/step_04_optical_constants.json <<'FFEOF'
{
  "Zr3N4": {
    "epsilon0": 11.91,
    "n0": 3.45
  },
  "Hf3N4": {
    "epsilon0": 8,
    "n0": 2.88
  }
}
FFEOF
