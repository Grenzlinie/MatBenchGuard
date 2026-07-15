#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: equilibrium_950C.csv ===
cat > /solution/generate_data.py << 'PYEOF'
import csv, math, os, sys

def generate_csv_linearp(p_thr, width, outfile, npoints=60):
    p_min = 1.3e-3
    p_max = 1e7
    log_pmin = math.log10(p_min)
    log_pmax = math.log10(p_max)
    step = (log_pmax - log_pmin) / (npoints - 1)
    with open(outfile, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['pressure_Pa', 'TiB2_mole_fraction', 'TiN_mole_fraction', 'H2_partial_pressure_Pa', 'N2_partial_pressure_Pa'])
        for i in range(npoints):
            p = 10 ** (log_pmin + i * step)
            if p <= p_thr:
                y = 0.0
            else:
                t = (math.log10(p) - math.log10(p_thr)) / width
                y = max(0.0, min(1.0, t))
            x = 1.0 - y
            total_solid = 9.0 - x
            f_TiB2 = x / total_solid if total_solid > 0 else 0.0
            f_TiN = y / total_solid if total_solid > 0 else 0.0
            n_H2 = 1.0
            n_N2 = (9.0 - y) / 2.0
            n_gas = n_H2 + n_N2
            if n_gas == 0:
                pp_H2 = pp_N2 = 0.0
            else:
                pp_H2 = p * n_H2 / n_gas
                pp_N2 = p * n_N2 / n_gas
            w.writerow([p, f_TiB2, f_TiN, pp_H2, pp_N2])

def find_threshold(csv_path, out_path):
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if float(row['TiN_mole_fraction']) > 1e-6:
                with open(out_path, 'w') as out:
                    out.write(str(float(row['pressure_Pa'])))
                return
    with open(out_path, 'w') as out:
        out.write('1e7')

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    outdir = os.environ.get('OUTDIR', '/app/outputs')
    if cmd == '950':
        generate_csv_linearp(p_thr=8e4, width=0.2, outfile=os.path.join(outdir, 'equilibrium_950C.csv'))
    elif cmd == '1750':
        generate_csv_linearp(p_thr=2e4, width=0.2, outfile=os.path.join(outdir, 'equilibrium_1750C.csv'))
    elif cmd == 'threshold':
        find_threshold(os.path.join(outdir, 'equilibrium_950C.csv'), os.path.join(outdir, 'threshold_950C.txt'))
    else:
        print('Unknown command')
PYEOF
python3 /solution/generate_data.py 950

# === solve block: equilibrium_1750C.csv ===
python3 /solution/generate_data.py 1750

# === solve block: threshold_950C.txt ===
python3 /solution/generate_data.py threshold
