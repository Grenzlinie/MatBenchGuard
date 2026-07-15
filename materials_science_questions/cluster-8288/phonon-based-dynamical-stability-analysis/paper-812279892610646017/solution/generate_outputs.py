#!/usr/bin/env python3
"""Reference oracle output generator for paper-812279892610646017.
Writes each scored artifact directly from hardcoded reference values."""
import csv
import math
import sys
import os

def write_structural_properties(outdir):
    """step_01_structural_properties.csv"""
    # Pressures from 0 to 20 GPa with extra points near 12 GPa
    pressures = [0, 2, 4, 6, 8, 10, 11, 12, 13, 14, 16, 18, 20]
    # c/a transition: from ~1.55 to ~1.25 via a steep hyperbolic tangent
    # u transition: from ~0.375 to ~0.5
    # volume per 4 atoms: from ~315 Bohr^3 at 0 GPa to ~302 Bohr^3 at 20 GPa, smooth
    rows = []
    for P in pressures:
        # c/a: 1.40 - 0.15 * tanh((P-12)/0.5)  → at low P ~1.55, at high P ~1.25
        c_a = 1.40 - 0.15 * math.tanh((P - 12) / 0.5)
        # u: 0.4375 + 0.0625 * tanh((P-12)/0.5) → low P 0.375, high P 0.5
        u = 0.4375 + 0.0625 * math.tanh((P - 12) / 0.5)
        u_scn = u
        u_gan = u
        # volume: V = 315 - 0.6*P - 0.0025*P^2
        vol = 315 - 0.6 * P - 0.0025 * P * P
        rows.append((P, round(c_a, 4), round(u_scn, 4), round(u_gan, 4), round(vol, 2)))

    path = os.path.join(outdir, 'step_01_structural_properties.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pressure_GPa', 'c_over_a', 'u_ScN', 'u_GaN', 'volume_per4atoms_Bohr3'])
        for P, c, us, ug, v in rows:
            writer.writerow([P, c, us, ug, v])

def write_transition_pressure(outdir):
    """step_02_transition_pressure.txt"""
    path = os.path.join(outdir, 'step_02_transition_pressure.txt')
    with open(path, 'w') as f:
        f.write('12.0\n')

def write_piezoelectric(outdir):
    """step_03_piezoelectric_e33.txt"""
    path = os.path.join(outdir, 'step_03_piezoelectric_e33.txt')
    with open(path, 'w') as f:
        f.write('2.0\n')

def write_phonon_frequency(outdir):
    """step_04_phonon_frequency.csv, showing soft mode near 12 GPa"""
    # Pressures and frequencies (cm^-1) forming a V-shaped dip
    points = [
        (8, 220),
        (10, 140),
        (11, 70),
        (12, 10),
        (14, 100),
    ]
    path = os.path.join(outdir, 'step_04_phonon_frequency.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pressure_GPa', 'A1_TO_frequency_cm-1'])
        for P, freq in points:
            writer.writerow([P, freq])

if __name__ == '__main__':
    outdir = os.environ.get('OUTDIR', '/app/outputs')
    mode = sys.argv[1]
    if mode == 'structural_properties':
        write_structural_properties(outdir)
    elif mode == 'transition_pressure':
        write_transition_pressure(outdir)
    elif mode == 'piezoelectric':
        write_piezoelectric(outdir)
    elif mode == 'phonon_frequency':
        write_phonon_frequency(outdir)
    else:
        sys.exit(f'Unknown mode: {mode}')
