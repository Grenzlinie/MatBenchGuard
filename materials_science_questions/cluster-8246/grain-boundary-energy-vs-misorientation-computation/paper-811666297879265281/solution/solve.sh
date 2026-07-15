#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energy_estimates.json ===
python3 << 'EOF'
import json, math

G = 4e9  # N/m^2

def gamma(b_meters, theta_deg):
    theta_rad = math.radians(theta_deg)
    return 1000 * G * b_meters * math.sin(theta_rad / 2)

def threshold_angle(b_meters, target_Jm2=0.065):
    ratio = target_Jm2 / (G * b_meters)
    theta_half = math.asin(ratio)
    return math.degrees(2 * theta_half)

b_basal = 4.52e-10
b_nonbasal_7_36 = 7.36e-10
b_nonbasal_8_63 = 8.63e-10
b_nonbasal_avg = 8.0e-10

result = {
    "basal_energy_0.5deg": round(gamma(b_basal, 0.5), 6),
    "basal_energy_3deg": round(gamma(b_basal, 3), 6),
    "basal_energy_5deg": round(gamma(b_basal, 5), 6),
    "nonbasal_energy_0.5deg_b7.36": round(gamma(b_nonbasal_7_36, 0.5), 6),
    "nonbasal_energy_4deg_b7.36": round(gamma(b_nonbasal_7_36, 4), 6),
    "nonbasal_energy_0.5deg_b8.63": round(gamma(b_nonbasal_8_63, 0.5), 6),
    "nonbasal_energy_4deg_b8.63": round(gamma(b_nonbasal_8_63, 4), 6),
    "threshold_angle_basal": round(threshold_angle(b_basal), 6),
    "threshold_angle_nonbasal": round(threshold_angle(b_nonbasal_avg), 6)
}

with open("/app/outputs/energy_estimates.json", "w") as f:
    json.dump(result, f, indent=2)
EOF
