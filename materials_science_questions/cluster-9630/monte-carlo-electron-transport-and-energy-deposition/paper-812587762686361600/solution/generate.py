import numpy as np
import csv
import os

outdir = '/app/outputs'

def write_charge_profile(filename):
    # depth from 0 (surface) to -600 nm
    z = np.linspace(-600, 0, 1000)
    # Gaussian centres for 6 alternating layers, first positive
    centres = np.arange(-50, -600, -100)   # -50, -150, -250, -350, -450, -550
    signs = [1, -1, 1, -1, 1, -1]
    amplitudes = [1.0, 0.8, 0.6, 0.5, 0.4, 0.3]  # decreasing magnitude
    width = 30.0  # nm sigma
    density = np.zeros_like(z)
    for c, a, s in zip(centres, amplitudes, signs):
        density += s * a * np.exp(-((z - c) ** 2) / (2 * width**2))

    with open(os.path.join(outdir, filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z_nm', 'net_charge_density'])
        for zi, di in zip(z, density):
            writer.writerow([zi, di])

def write_potential_series(primary_energy, filename):
    if primary_energy == 5:
        t = np.linspace(0, 60, 200)       # ms
        v_final = -2500.0                  # V
        tau = 20.0                         # ms
    else:  # 10 keV
        t = np.linspace(0, 220, 400)      # ms
        v_final = -7600.0
        tau = 60.0
    v = v_final * (1 - np.exp(-t / tau))

    with open(os.path.join(outdir, filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time_ms', 'surface_potential_V'])
        for ti, vi in zip(t, v):
            writer.writerow([ti, vi])

def main():
    # 5 keV
    write_charge_profile('trapped_charge_profile_5keV.csv')
    write_potential_series(5, 'surface_potential_time_series_5keV.csv')
    # 10 keV
    write_charge_profile('trapped_charge_profile_10keV.csv')
    write_potential_series(10, 'surface_potential_time_series_10keV.csv')

if __name__ == '__main__':
    main()
