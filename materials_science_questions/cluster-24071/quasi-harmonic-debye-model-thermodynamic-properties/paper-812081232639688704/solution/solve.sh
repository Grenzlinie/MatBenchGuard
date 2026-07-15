#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /tmp/generate.py << 'GENEOF'
import csv, math, sys, os

R = 8.314

def alpha_fe():
    dh_m = 13800.0  # J/mol
    t_m = 1811.0
    dv_v = 0.034
    ds_m = dh_m / t_m
    xa = 1.0 / (1.0 + dv_v)
    xb = 1.0 - xa
    ds_pos = -R * (xa * math.log(xa) + xb * math.log(xb))
    ds_vib = ds_m - ds_pos
    return 2.0 * ds_vib / (3.0 * R) + 1.0

def alpha_se():
    dh_m = 5400.0
    t_m = 494.0
    ds_vib = dh_m / t_m
    return 2.0 * ds_vib / (3.0 * R) + 1.0

def alpha_pb():
    dh_m = 4770.0
    t_m = 600.61
    dv_v = 0.035
    ds_m = dh_m / t_m
    xa = 1.0 / (1.0 + dv_v)
    xb = 1.0 - xa
    ds_pos = -R * (xa * math.log(xa) + xb * math.log(xb))
    ds_vib = ds_m - ds_pos
    return 2.0 * ds_vib / (3.0 * R) + 1.0

def alpha_aral():
    h_ar = 0.3650
    h_al = 0.2863
    t_ar = 83.80
    t_al = 933.47
    return 0.5 * (((h_al / h_ar) ** 2) * (t_ar / t_al) + 1.0)

def d_range():
    return [float(d) for d in range(3, 101)]

def write_debye(output_path, elem, d0, alpha):
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['D (nm)', 'Theta_D_ratio (dimensionless)'])
        for D in d_range():
            ratio = math.sqrt(math.exp(-(alpha - 1.0) / (D / d0 - 1.0)))
            w.writerow([D, f'{ratio:.6f}'])

def write_einstein(output_path, elem, d0, alpha):
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['D (nm)', 'Theta_E_ratio (dimensionless)'])
        for D in d_range():
            ratio = math.sqrt(math.exp(-(alpha - 1.0) / (D / d0 - 1.0)))
            w.writerow([D, f'{ratio:.6f}'])

def write_alpha_v(output_path, d0_se, alpha_se, d0_pb, alpha_pb):
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['D (nm)', 'element', 'alpha_v_ratio (dimensionless)'])
        for D in d_range():
            ratio_se = math.exp((alpha_se - 1.0) / (D / d0_se - 1.0))
            w.writerow([D, 'Se', f'{ratio_se:.6f}'])
        for D in d_range():
            ratio_pb = math.exp((alpha_pb - 1.0) / (D / d0_pb - 1.0))
            w.writerow([D, 'Pb', f'{ratio_pb:.6f}'])

def write_params(output_path):
    with open(output_path, 'w') as f:
        f.write('Fe: D0=1.4892 nm, alpha=1.5148\n')
        f.write('Se: D0=2.6196 nm, alpha=1.8764\n')
        f.write('Pb: D0=2.1 nm, alpha=1.5386\n')
        f.write('Ar/Al: D0=2.19 nm, alpha=0.5276\n')

if __name__ == '__main__':
    path = sys.argv[1]
    basename = os.path.basename(path)
    if basename == 'params_summary.txt':
        write_params(path)
    elif basename == 'debye_ratio_free_Fe.csv':
        write_debye(path, 'Fe', 6*0.2482, alpha_fe())
    elif basename == 'debye_ratio_embedded_ArAl.csv':
        write_debye(path, 'ArAl', 6*0.3650, alpha_aral())
    elif basename == 'einstein_ratio_Se.csv':
        write_einstein(path, 'Se', 6*0.4366, alpha_se())
    elif basename == 'alpha_v_ratio_Se_Pb.csv':
        write_alpha_v(path, 6*0.4366, alpha_se(), 6*0.35, alpha_pb())
GENEOF
chmod +x /tmp/generate.py

# === solve block: debye_ratio_free_Fe.csv ===
python3 << 'PYEOF'
import csv, math
R = 8.314
dh_m = 13800.0
t_m = 1811.0
dv_v = 0.034
ds_m = dh_m / t_m
xa = 1.0 / (1.0 + dv_v)
xb = 1.0 - xa
ds_pos = -R * (xa * math.log(xa) + xb * math.log(xb))
ds_vib = ds_m - ds_pos
alpha = 2.0 * ds_vib / (3.0 * R) + 1.0
d0 = 6.0 * 0.2482
with open('/app/outputs/debye_ratio_free_Fe.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['D (nm)', 'Theta_D_ratio (dimensionless)'])
    for D_nm in range(2, 101):
        D = float(D_nm)
        ratio = math.sqrt(math.exp(-(alpha - 1.0) / (D / d0 - 1.0)))
        w.writerow([D_nm, f'{ratio:.6f}'])
PYEOF

# === solve block: debye_ratio_embedded_ArAl.csv ===
python3 /tmp/generate.py /app/outputs/debye_ratio_embedded_ArAl.csv

# === solve block: einstein_ratio_Se.csv ===
python3 /tmp/generate.py /app/outputs/einstein_ratio_Se.csv

# === solve block: alpha_v_ratio_Se_Pb.csv ===
python3 /tmp/generate.py /app/outputs/alpha_v_ratio_Se_Pb.csv
