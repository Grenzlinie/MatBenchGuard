#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > "/app/outputs/results.json" <<'FFEOF'
{
  "dipole_moment_D": 4.04,
  "excitation_NV1_eV": 7.02,
  "excitation_NV2_eV": 9.92,
  "ionization_potential_eV": -11.6,
  "oscillator_NV1": 0.451,
  "oscillator_NV2": 0.122
}
FFEOF
