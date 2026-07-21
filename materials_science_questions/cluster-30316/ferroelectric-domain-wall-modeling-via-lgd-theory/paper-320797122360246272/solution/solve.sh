#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: domain_wall_properties.json ===
#!/bin/bash
set -euo pipefail
mkdir -p "${OUTDIR:-/app/outputs}"
cat > "${OUTDIR:-/app/outputs}/domain_wall_properties.json" <<'FFEOF'
{
  "d": 2.001e-7,
  "eta": 2.658e-6,
  "T": 300.0,
  "Tc": 400.0,
  "M": 1.5e-22,
  "c1": 6.0e-13,
  "c2": 6.0e-13,
  "b": 4.24e12,
  "alpha": 6.0e21,
  "omega_perp_sq": 1.2e24
}
FFEOF

# === solve block: local_mode_frequencies.json ===
#!/bin/bash
set -euo pipefail
mkdir -p "${OUTDIR:-/app/outputs}"
cat > "${OUTDIR:-/app/outputs}/local_mode_frequencies.json" <<'FFEOF'
{
  "omega_x1_sq": 1.1e24,
  "omega_x2_sq": 8.0e23,
  "omega_perp_sq": 1.2e24,
  "gap_sq": 2.174944e21,
  "units": "rad^2/s^2"
}
FFEOF
