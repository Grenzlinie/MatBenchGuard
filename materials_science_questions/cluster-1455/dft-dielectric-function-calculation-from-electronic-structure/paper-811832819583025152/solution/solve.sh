#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > /app/outputs/dft_results.json <<'FFEOF'
{
  "compositions": [
    {"name": "GeTe", "phase": "stable", "band_gap_indirect": 0.66, "band_gap_direct_min": 0.75, "static_dielectric_constant": 39.28, "critical_point_energies": [0.7, 1.2, 1.7, 2.0, 2.3, 3.3, 3.8]},
    {"name": "Ge2Sb2Te5", "phase": "stable", "band_gap_indirect": 0.41, "band_gap_direct_min": 0.41, "static_dielectric_constant": 45.75, "critical_point_energies": []},
    {"name": "Ge2Sb2Te5", "phase": "metastable", "band_gap_indirect": 0.51, "band_gap_direct_min": 0.51, "static_dielectric_constant": 40.85, "critical_point_energies": []},
    {"name": "Ge1Sb2Te4", "phase": "stable", "band_gap_indirect": 0.43, "band_gap_direct_min": 0.46, "static_dielectric_constant": 45.46, "critical_point_energies": []},
    {"name": "Ge1Sb2Te4", "phase": "metastable", "band_gap_indirect": 0.55, "band_gap_direct_min": 0.55, "static_dielectric_constant": 39.15, "critical_point_energies": []},
    {"name": "Ge1Sb4Te7", "phase": "stable", "band_gap_indirect": 0.34, "band_gap_direct_min": 0.34, "static_dielectric_constant": 44.99, "critical_point_energies": []},
    {"name": "Ge1Sb4Te7", "phase": "metastable", "band_gap_indirect": 0.51, "band_gap_direct_min": 0.51, "static_dielectric_constant": 36.59, "critical_point_energies": []},
    {"name": "Sb2Te3", "phase": "stable", "band_gap_indirect": 0.17, "band_gap_direct_min": 0.17, "static_dielectric_constant": 45.36, "critical_point_energies": []}
  ]
}
FFEOF
