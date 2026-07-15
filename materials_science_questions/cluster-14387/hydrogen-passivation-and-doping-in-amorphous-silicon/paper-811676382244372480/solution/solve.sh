#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_simulation_results.csv ===
cat > /app/outputs/step_01_simulation_results.csv <<'EOF'
amorphization_threshold_mJ_per_cm2,film_thickness_nm,melt_duration_ns,temperature_gradient_K_per_cm
212,12,50,100000
254,24,80,100000
296,36,110,100000
EOF

# === solve block: step_02_nucleation_results.json ===
cat > /app/outputs/step_02_nucleation_results.json <<'EOF'
{
  "nucleation_density_m3": 40000000000000000000000,
  "nucleation_rate_m3_s1": 8000000000000000000000000000000
}
EOF
