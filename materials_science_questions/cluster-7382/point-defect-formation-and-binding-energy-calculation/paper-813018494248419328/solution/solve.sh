#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: trapping_energies.csv ===
cat > /app/outputs/trapping_energies.csv <<'FFEOF'
system,trapping_energy_eV
pure_V,-1.18
Re1_V_OIS_I,-1.12
Re1_V_OIS_II,-1.17
Re2_V,-1.18
Re3_V,-1.11
Re4_V,-1.03
Re5_V,-0.96
Re6_V,-0.90
Re7_V,-0.84
Re8_V,-0.79
FFEOF

# === solve block: decomposition_energies.csv ===
cat > /app/outputs/decomposition_energies.csv <<'FFEOF'
system,total_solution_energy_eV,MC_eV,EC_eV
pure_V,-0.270,0.015,-0.285
Re1_V_OIS_I,-0.210,0.020,-0.230
Re1_V_OIS_II,-0.290,0.018,-0.308
Re2_V,-0.270,0.022,-0.292
Re3_V,-0.200,0.026,-0.226
Re4_V,-0.120,0.030,-0.150
Re5_V,-0.050,0.036,-0.086
Re6_V,0.010,0.042,-0.032
Re7_V,0.060,0.050,0.010
Re8_V,0.120,0.058,0.032
FFEOF

# === solve block: sequential_trapping.csv ===
cat > /app/outputs/sequential_trapping.csv <<'FFEOF'
system,n,trapping_energy_eV
pure_V,1,-1.18
pure_V,2,-1.05
pure_V,3,-0.95
pure_V,4,-0.85
pure_V,5,-0.75
pure_V,6,-0.65
pure_V,7,-0.55
pure_V,8,-0.35
pure_V,9,-0.30
pure_V,10,-0.25
pure_V,11,-0.20
pure_V,12,-0.15
Re1_V,1,-1.18
Re1_V,2,-1.05
Re1_V,3,-0.95
Re1_V,4,-0.85
Re1_V,5,-0.75
Re1_V,6,-0.65
Re1_V,7,-0.55
Re1_V,8,-0.35
Re1_V,9,-0.30
Re1_V,10,-0.25
Re1_V,11,-0.20
Re1_V,12,-0.15
Re4_V,1,-1.03
Re4_V,2,-0.90
Re4_V,3,-0.75
Re4_V,4,-0.60
Re4_V,5,-0.45
Re4_V,6,-0.30
Re4_V,7,-0.10
Re4_V,8,0.50
FFEOF

# === solve block: max_H_at_RT.csv ===
cat > /app/outputs/max_H_at_RT.csv <<'FFEOF'
system,heating_rate_K_per_s,max_n_H_at_RT
pure_V,1,6
pure_V,5,6
Re1_V,1,5
Re1_V,5,5
Re4_V,1,4
Re4_V,5,4
FFEOF
