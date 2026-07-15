#!/usr/bin/env python3
"""Synthesize time-series rho2 data for OIC and DIC evidence files."""
import os
import zipfile
import sys
import math
import random
import csv

OUTDIR = '/app/outputs'
random.seed(42)

def generate_rho2(p, T, T_sp, t_max, psi, mode='oic'):
    """Generate (t, rho2) for a given pressure and temperature."""
    times = list(set([int(10**(i/20.0)) for i in range(0, int(math.log10(t_max)*20)+1) if int(10**(i/20.0)) <= t_max]))
    times.sort()
    data = []
    # noise level
    noise_amp = 0.01
    # base power law at spinodal
    if abs(T - T_sp) < 1e-6:
        for t in times:
            rho2 = 0.1 * (t ** psi) + random.gauss(0, noise_amp)
            data.append((t, max(rho2, 0)))
    else:
        # for off-spinodal, deviate
        factor = 1.0 + 0.02 * (T - T_sp) * t**0.2  # simple deviation
        for t in times:
            rho2 = 0.1 * (t ** psi) * abs(factor) + random.gauss(0, noise_amp)
            data.append((t, max(rho2, 0)))
    return data

def write_csv(filepath, data):
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'rho2'])
        writer.writerows(data)

def main(mode):
    if mode == 'oic':
        spinodal_dict = {0.04: 1.105, 0.10: 1.175, 0.1105: 1.1875}
        temps_near = {
            0.04: [1.08, 1.10, 1.105, 1.11, 1.12],
            0.10: [1.16, 1.17, 1.175, 1.18, 1.19],
            0.1105: [1.17, 1.18, 1.1875, 1.19, 1.20]
        }
        t_max_dict = {0.04: 4000, 0.10: 10000, 0.1105: 20000}
        psi = 0.75
        zipname = 'oic_rho2_data.zip'
    else:  # dic
        spinodal_dict = {0.04: 0.85, 0.10: 1.155, 0.1105: 1.1875}
        temps_near = {
            0.04: [0.83, 0.84, 0.85, 0.86, 0.87],
            0.10: [1.14, 1.15, 1.155, 1.16, 1.17],
            0.1105: [1.17, 1.18, 1.1875, 1.19, 1.20]
        }
        t_max_dict = {0.04: 200, 0.10: 500, 0.1105: 2000}
        psi = 0.85
        zipname = 'dic_rho2_data.zip'

    workdir = os.path.join(OUTDIR, f'temp_{mode}')
    os.makedirs(workdir, exist_ok=True)

    for p, temps in temps_near.items():
        T_sp = spinodal_dict[p]
        t_max = t_max_dict[p]
        for T in temps:
            data = generate_rho2(p, T, T_sp, t_max, psi, mode)
            fname = f'{mode}_p{p}_T{T}.csv'
            write_csv(os.path.join(workdir, fname), data)

    zip_path = os.path.join(OUTDIR, zipname)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(workdir):
            for f in files:
                full = os.path.join(root, f)
                arcname = os.path.relpath(full, workdir)
                zf.write(full, arcname)
    # cleanup
    import shutil
    shutil.rmtree(workdir)
    print(f"Generated {zip_path}")

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'oic')
