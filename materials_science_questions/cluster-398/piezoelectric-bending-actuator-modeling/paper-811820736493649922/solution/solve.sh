#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR="/app/outputs"

# === solve block: computed_results.json ===
cat > "$OUTDIR/computed_results.json" <<'FFEOF'
{
  "diffraction_angle_rad": 0.031,
  "diffraction_efficiency": 0.063,
  "excitation_voltage_V": 40,
  "flexural_wavelength_m": 1.6e-5,
  "piezo_thickness_um": 140,
  "wave_amplitude_um": 0.02
}
FFEOF
