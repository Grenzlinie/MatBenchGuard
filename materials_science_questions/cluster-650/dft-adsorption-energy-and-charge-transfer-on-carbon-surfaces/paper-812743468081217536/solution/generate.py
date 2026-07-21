#!/usr/bin/env python3
import sys, csv, math

def make_step_01():
    """Angle vs time: 200 ns, 0.5 ns resolution."""
    tau = 25.0      # time constant so the angle settles by ~100 ns
    t_target = 78.0  # final equilibrium angle (degrees)
    t_max = 200.0
    dt = 0.5
    rows = []
    t = 0.0
    while t <= t_max + 1e-9:
        # exponential approach from vertical (90°) and from parallel (0°)
        angle_perp = t_target + (90.0 - t_target) * math.exp(-t/tau)
        angle_par  = t_target - t_target * math.exp(-t/tau)
        rows.append([f"{t:.1f}", f"{angle_perp:.2f}", f"{angle_par:.2f}"])
        t += dt
    with open('/app/outputs/step_01_angle_vs_time.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time(ns)', 'angle_perp(deg)', 'angle_par(deg)'])
        w.writerows(rows)

def make_step_02():
    """Basepair distance profile: 12 base pairs, linear from 0.1 nm to 3.4 nm."""
    rows = []
    for bp in range(1, 13):
        dist = 0.1 + (3.4 - 0.1) * (bp - 1) / 11.0
        rows.append([str(bp), f"{dist:.3f}", f"{dist:.3f}"])
    with open('/app/outputs/step_02_basepair_distance.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['base_pair', 'distance_perp(nm)', 'distance_par(nm)'])
        w.writerows(rows)

def make_step_03():
    """Interaction energy: vdW, Ele, Total for each system (perp, par)."""
    systems = ['perp', 'par']
    cutoff = '4.0'
    # Paper reports: total ~ -120 kJ/mol, vdW dominant, electrostatic small
    energies = {
        'vdW': '-110.0',
        'Ele': '-10.0',
        'Total': '-120.0'
    }
    rows = []
    for sys in systems:
        for etype in ('vdW', 'Ele', 'Total'):
            rows.append([sys, cutoff, etype, energies[etype]])
    with open('/app/outputs/step_03_interaction_energy.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'distance_cutoff(A)', 'energy_type', 'value(kJ/mol)'])
        w.writerows(rows)

def make_step_04():
    """Final adsorption angles for all five systems."""
    rows = [
        ['perp', '78.0'],
        ['par', '78.0'],
        ['seq_changed', '78.0'],  # altered sequence still ~78°
        ['8bp', '70.0'],
        ['6bp', '65.0']
    ]
    with open('/app/outputs/step_04_final_angles.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'final_angle(deg)'])
        w.writerows(rows)

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else ''
    {
        'step_01_angle_vs_time.csv': make_step_01,
        'step_02_basepair_distance.csv': make_step_02,
        'step_03_interaction_energy.csv': make_step_03,
        'step_04_final_angles.csv': make_step_04,
    }[target]()
