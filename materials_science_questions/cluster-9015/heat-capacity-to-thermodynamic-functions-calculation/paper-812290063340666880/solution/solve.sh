#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: free_energy_functions.csv ===
OUTDIR="/app/outputs"
cat > "$OUTDIR/free_energy_functions.csv" <<'EOF'
T_K,F_solid,F_vapor,Delta_F_evap
1000,-13.942,-57.420,-43.478
1100,-14.998,-58.195,-43.197
1200,-15.988,-58.907,-42.919
1300,-16.918,-59.567,-42.649
1400,-17.795,-60.183,-42.388
1500,-18.626,-60.763,-42.137
1600,-19.414,-61.306,-41.892
1700,-20.165,-61.815,-41.650
1800,-20.881,-62.292,-41.411
1900,-21.566,-62.745,-41.179
2000,-22.223,-63.182,-40.959
EOF

# === solve block: delta_H0_values.txt ===
cat > /app/outputs/delta_H0_values.txt <<'EOF'
Run 6: T=1438, log10(p)=-8.6, ΔH₀=117489.0
Run 5: T=1441, log10(p)=-8.7, ΔH₀=118156.0
Run 7: T=1495, log10(p)=-7.9, ΔH₀=117070.0
Run 4: T=1511, log10(p)=-7.6, ΔH₀=115997.0
Run 2: T=1529, log10(p)=-7.6, ΔH₀=117233.0
Run 1: T=1566, log10(p)=-7.1, ΔH₀=116386.0
Average ΔH₀ = 117055 cal/mol
EOF

# === solve block: vapor_pressure_equation.txt ===
cat > /app/outputs/vapor_pressure_equation.txt <<'EOF'
log10(p/atm) = -25586/T - 7.67e-4 T + 7.21e-8 T^2 + 10.198
EOF
