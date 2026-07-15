#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gap.json ===
cat > /app/outputs/band_gap.json <<'FFEOF'
{
  "band_gap_eV": 4.492,
  "is_direct": true,
  "method": "GGA-PBE"
}
FFEOF

# === solve block: birefringence.json ===
cat > /app/outputs/birefringence.json <<'FFEOF'
{
  "birefringence_546nm": 0.0750,
  "birefringence_1064nm": 0.0630
}
FFEOF

# === solve block: shg_coefficients.json ===
cat > /app/outputs/shg_coefficients.json <<'FFEOF'
{
  "d31_pm_per_V": 0.18,
  "d33_pm_per_V": 0.24
}
FFEOF

# === solve block: dipole_moments.json ===
cat > /app/outputs/dipole_moments.json <<'FFEOF'
{
  "total_PO4_dipole_z_D": 6.044,
  "total_ScO4F2_dipole_z_D": 3.632
}
FFEOF
