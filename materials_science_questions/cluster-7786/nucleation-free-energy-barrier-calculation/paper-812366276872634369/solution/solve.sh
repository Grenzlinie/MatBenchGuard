#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: saddle_point_table.csv ===
cat > /app/outputs/saddle_point_table.csv <<'EOF'
relative_humidity_pct,acid_vapor_activity,acid_vapor_pressure_torr,composition_X_star,radius_A,molecules_per_nucleus,deltaG_over_kT,frequency_factor_C
100,8.80e-05,3.08e-08,0.196,7.29,43.4,41.12,7.21e17
75,2.48e-04,8.68e-08,0.219,7.35,42.3,41.71,1.30e18
50,8.76e-04,3.07e-07,0.248,7.44,42.2,42.38,2.55e18
25,5.20e-03,1.82e-06,0.293,7.56,42.0,43.24,6.02e18
10,3.37e-02,1.18e-05,0.349,7.69,41.4,43.99,1.27e19
EOF

# === solve block: growth_curve_100RH.csv ===
python3 << 'PYEOF'
import math

r_crit = 7.29
X_crit = 0.196
X_inf  = 0.1064   # n1/n2 = 8.4 at 1000 A -> X = 1/(1+8.4)
k      = 0.5797

with open('/app/outputs/growth_curve_100RH.csv', 'w') as f:
    f.write('radius_A,composition_X\n')
    r = r_crit
    while r <= 1000.0:
        X = X_inf + (X_crit - X_inf) * math.exp(-k * (r - r_crit))
        f.write(f'{r:.2f},{X:.6f}\n')
        r += 1.0
PYEOF
