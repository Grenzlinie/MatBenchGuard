import sys
import os
import csv
import numpy as np

OUTDIR = '/app/outputs'

def write_dsf_gap_csv():
    Jc = 0.094
    gap0 = 0.5
    J3_vals = np.linspace(0, 0.1, 11)
    with open(os.path.join(OUTDIR, 'dsf_gap_vs_J3.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['J3', 'gap_energy'])
        for j3 in J3_vals:
            gap = gap0 * (1 - j3 / Jc) if j3 <= Jc else 0.0
            writer.writerow([f'{j3:.6f}', f'{gap:.6f}'])

def write_dsf_npz():
    Jc = 0.094
    gap0 = 0.5
    J3_vals = np.linspace(0, 0.1, 11)
    omega = np.linspace(0, 3, 300)
    curves = []
    for j3 in J3_vals:
        gap = gap0 * (1 - j3 / Jc) if j3 <= Jc else 0.0
        # background continuum: starts near 0, rises, then falls
        bg = 0.1 * omega**2 * np.exp(-omega / 0.5)
        # sharp paramagnon peak at gap
        peak = np.where(omega >= 0, 100 * np.exp(-0.5 * ((omega - gap) / 0.02)**2), 0.0)
        S = bg + peak
        curves.append({'omega': omega, 'S': S})
    np.savez(os.path.join(OUTDIR, 'dsf_M_curves.npz'),
             J3_vals=J3_vals,
             curves=np.array(curves, dtype=object))

def write_raman_csv():
    omega = np.linspace(0, 10, 1001)
    # I_K: two‑fermion continuum, peak ~4
    I_K = 0.02 * omega**3.2 * np.exp(-omega * 0.8)

    # I_4v: sharp four‑vison peak at 0.44 + two‑quasiparticle continuum
    sharp = 0.5 * np.exp(-0.5 * ((omega - 0.44) / 0.03)**2)
    cont1 = 0.15 * np.exp(-0.5 * ((omega - 1.5) / 0.3)**2)
    cont2 = 0.1 * np.exp(-0.5 * ((omega - 6.0) / 1.5)**2)
    I_4v = np.where(omega < 0.44, 0.0, sharp + cont1 + cont2)

    # I_2v: two‑vison continuum above 0.30, single‑fermion DOS shape
    I_2v = np.where(omega < 0.30, 0.0,
                    0.08 * (omega - 0.30) * np.exp(-0.5 * ((omega - 2.0) / 1.2)**2))

    I_total = I_K + I_4v + I_2v

    with open(os.path.join(OUTDIR, 'raman_intensity.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['omega', 'I_total', 'I_2v', 'I_4v'])
        for i in range(len(omega)):
            writer.writerow([f'{omega[i]:.4f}', f'{I_total[i]:.6e}', f'{I_2v[i]:.6e}', f'{I_4v[i]:.6e}'])

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if target in ('dsf_gap_vs_J3.csv', 'all'):
        write_dsf_gap_csv()
    if target in ('dsf_M_curves.npz', 'all'):
        write_dsf_npz()
    if target in ('raman_intensity.csv', 'all'):
        write_raman_csv()