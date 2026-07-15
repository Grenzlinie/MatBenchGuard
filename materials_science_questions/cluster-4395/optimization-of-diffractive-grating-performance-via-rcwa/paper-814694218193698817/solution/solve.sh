#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: impedance_and_reflectance.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /app/outputs/impedance_and_reflectance.csv <<'FFEOF'
design_name,resonance_wavelength_nm,S11_amplitude,S11_phase_deg,Z_real,Z_imag,reflectance_0deg,reflectance_20deg,reflectance_36deg
Au nanodisk array,1480,0.05,180.0,0.9523809523809523,0.0,0.0025,0.005,0.01
Pd wire array (p=450nm),720,0.0995,-84.3,1.0,-0.2,0.0099,0.20,0.35
Pd wire array (p=300nm),690,0.03,180.0,0.9417475728155339,0.0,0.0009,0.01,0.03
Disordered Au nanodisk (single),780,0.0,0.0,1.0,0.0,,,
FFEOF
