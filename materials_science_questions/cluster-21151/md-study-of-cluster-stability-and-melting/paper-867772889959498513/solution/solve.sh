#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: oscillator_parameters_vs_energy.csv ===
cat > /app/outputs/oscillator_parameters_vs_energy.csv <<'FFEOF'
total_energy,damping_coefficient,period,spring_constant,reduced_mass_ratio
-5.80,0.0,8.85,280.0,12.0
-5.70,0.0,8.88,280.0,12.0
-5.60,0.0,8.91,280.0,12.0
-5.50,0.0,8.94,280.0,12.0
-5.45,0.0,8.96,280.0,12.0
-5.444,0.0,8.96,280.0,11.0
-5.43,0.057,8.97,287.0,11.0
-5.40,0.164,8.99,310.0,10.0
-5.35,0.35,9.02,360.0,8.0
-5.30,0.54,9.05,410.0,5.0
-5.25,0.76,9.10,460.0,2.0
-5.20,1.0,9.14,510.0,1.0
FFEOF
