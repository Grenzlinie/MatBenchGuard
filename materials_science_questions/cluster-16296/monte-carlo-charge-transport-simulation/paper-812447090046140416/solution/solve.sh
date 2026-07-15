#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
cat > /tmp/gen_csv.py <<'PYEOF'
import csv
import sys

T = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

P_longitudinal = [
    1.50, 1.67, 1.87, 2.10, 2.38, 2.70, 3.07, 3.50, 4.00,
    4.58, 5.23, 5.95, 6.73, 7.55
]

P_transverse = [
    3.30, 3.5455, 3.8263, 4.1354, 4.5039, 4.9015, 5.3370,
    5.8154, 6.3385, 6.9052, 7.4829, 8.0554, 8.5937, 9.06
]

K = [p1/p2 for p1, p2 in zip(P_transverse, P_longitudinal)]
D = [(p1-p2)/(p1+p2) for p1, p2 in zip(P_transverse, P_longitudinal)]

def write_temp_dep(out):
    w = csv.writer(out)
    w.writerow(['T', 'P_transverse', 'P_longitudinal'])
    for i in range(len(T)):
        w.writerow([T[i], P_transverse[i], P_longitudinal[i]])

def write_aniso(out):
    w = csv.writer(out)
    w.writerow(['T', 'K', 'D'])
    for i in range(len(T)):
        w.writerow([T[i], K[i], D[i]])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: gen_csv.py <mode>', file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    if mode == 'temperature_dependence':
        write_temp_dep(sys.stdout)
    elif mode == 'anisotropy_and_polarization':
        write_aniso(sys.stdout)
    else:
        print('Unknown mode', file=sys.stderr)
        sys.exit(1)
PYEOF

# === solve block: temperature_dependence.csv ===
python3 /tmp/gen_csv.py temperature_dependence > "$OUTDIR/temperature_dependence.csv"

# === solve block: anisotropy_and_polarization.csv ===
python3 /tmp/gen_csv.py anisotropy_and_polarization > "$OUTDIR/anisotropy_and_polarization.csv"
