#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ambient_elastic_constants.txt ===
cat > /app/outputs/ambient_elastic_constants.txt <<'FFEOF'
179.2
54.5
FFEOF

# === solve block: mechanical_stability_thresholds.csv ===
cat > /app/outputs/mechanical_stability_thresholds.csv <<'FFEOF'
loading_type,compressive_stability_limit_Nm,tensile_stability_limit_Nm,compressive_failure_stress_Nm
zigzag,35,,77
armchair,85,19,
biaxial,111,16,135
FFEOF

# === solve block: ultimate_tensile_strength.csv ===
cat > /app/outputs/ultimate_tensile_strength.csv <<'FFEOF'
loading_type,UTS_Nm
zigzag,20.22
armchair,21.21
biaxial,16.05
FFEOF

# === solve block: band_gap_vs_stress.csv ===
cat > /app/outputs/band_gap_vs_stress.csv <<'FFEOF'
loading_type,stress_Nm,band_gap_eV
zigzag,0,2.35
zigzag,-77,0
armchair,0,2.35
armchair,-85,0
armchair,19,0.91
biaxial,0,2.35
biaxial,-135,0
biaxial,16,0
FFEOF

# === solve block: charge_analysis.json ===
cat > /app/outputs/charge_analysis.json <<'FFEOF'
{
  "max_charge_density_atom": "C",
  "max_charge_density_value": 7.99
}
FFEOF
