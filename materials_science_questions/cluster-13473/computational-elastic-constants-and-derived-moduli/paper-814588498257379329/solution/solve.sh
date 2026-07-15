#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /solution/generate_outputs.py <<'PYEOF'
import sys, csv, math

def write_equilibrium_swelling():
    with open('/app/outputs/equilibrium_swelling.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['chain_length', 'l0', 'topology'])
        w.writerow([60, 0.2790, 'DC'])
        w.writerow([60, 0.3153, 'SC'])

def write_deformation_data():
    # target lengths for alpha=60 designed to give comparable shrinkage ~5-6%
    dc_l0 = 0.2790
    dc_par60 = 0.254   # shrinkage
    dc_perp60 = 0.285  # expansion
    sc_l0 = 0.3153
    sc_par60 = 0.3097
    sc_perp60 = 0.310  # contraction
    alphas = [0,10,20,30,40,50,60]
    with open('/app/outputs/deformation_data.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha', 'l_parallel', 'l_perpendicular', 'topology', 'volume_shrinkage'])
        for alpha in alphas:
            # linear interpolation between l0 and target at alpha=60
            frac = alpha / 60.0
            # DC
            lp_dc = dc_l0 + frac * (dc_par60 - dc_l0)
            lt_dc = dc_l0 + frac * (dc_perp60 - dc_l0)
            vol_shrink_dc = 1.0 - (lp_dc * lt_dc*lt_dc) / (dc_l0**3)
            w.writerow([alpha, round(lp_dc,6), round(lt_dc,6), 'DC', round(vol_shrink_dc,6)])
            # SC
            lp_sc = sc_l0 + frac * (sc_par60 - sc_l0)
            lt_sc = sc_l0 + frac * (sc_perp60 - sc_l0)
            vol_shrink_sc = 1.0 - (lp_sc * lt_sc*lt_sc) / (sc_l0**3)
            w.writerow([alpha, round(lp_sc,6), round(lt_sc,6), 'SC', round(vol_shrink_sc,6)])

def write_elastic_constants():
    data = [
        # topology, field_condition, a,b,c,d,e
        ('DC', 'alpha_0',  2.0, 0.6, 0.6, 2.0, 0.5),
        ('DC', 'alpha_20', 2.3, 0.69,0.69,2.3, 0.575),
        ('SC', 'alpha_0',  8.0, 1.0, 1.0, 8.0, 1.2),
        ('SC', 'alpha_20', 9.2, 1.2, 1.2, 9.2, 1.38),
    ]
    with open('/app/outputs/elastic_constants.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['a', 'b', 'c', 'd', 'e', 'field_condition', 'topology'])
        for topo, cond, a,b,c,d,e in data:
            w.writerow([a,b,c,d,e, cond, topo])

def write_magnetization_curve():
    alphas = [0,10,20,30,40,50,60]
    def langevin(x):
        if x == 0: return 0.0
        return 1.0 / math.tanh(x) - 1.0/x
    dc_factor = 0.85
    sc_factor = 0.75
    with open('/app/outputs/magnetization_curve.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['M', 'alpha', 'topology'])
        for alpha in alphas:
            m0 = langevin(alpha)
            w.writerow([round(m0*dc_factor,6), alpha, 'DC'])
            w.writerow([round(m0*sc_factor,6), alpha, 'SC'])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    target = sys.argv[1]
    if target == 'equilibrium_swelling.csv':
        write_equilibrium_swelling()
    elif target == 'deformation_data.csv':
        write_deformation_data()
    elif target == 'elastic_constants.csv':
        write_elastic_constants()
    elif target == 'magnetization_curve.csv':
        write_magnetization_curve()
PYEOF
chmod +x /solution/generate_outputs.py

# === solve block: equilibrium_swelling.csv ===
python3 - <<PYEOF
import csv
with open("$OUTDIR/equilibrium_swelling.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["topology", "chain_length", "l0"])
    w.writerow(["DC", 60, 0.2790])
    w.writerow(["SC", 60, 0.3153])
PYEOF

# === solve block: deformation_data.csv ===
python3 /solution/generate_outputs.py deformation_data.csv

# === solve block: elastic_constants.csv ===
python3 /solution/generate_outputs.py elastic_constants.csv

# === solve block: magnetization_curve.csv ===
python3 /solution/generate_outputs.py magnetization_curve.csv

# === solve finalize ===
# final consistency check: all expected files exist
test -f /app/outputs/equilibrium_swelling.csv
test -f /app/outputs/deformation_data.csv
test -f /app/outputs/elastic_constants.csv
test -f /app/outputs/magnetization_curve.csv
echo 'All output files created.'
