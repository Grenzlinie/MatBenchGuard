#!/usr/bin/env python3
"""Generate a CSV with synthetic drift velocity and mean kinetic energy."""
import sys
import math
import csv

def v_drift(t, v_peak, t_peak):
    if t <= 0:
        return 0.0
    return v_peak * (t / t_peak) * math.exp(1 - t / t_peak)

def E_kinetic(t, E_thermal, E_max, tau):
    return E_thermal + (E_max - E_thermal) * (1.0 - math.exp(-t / tau))

def main():
    if len(sys.argv) != 4:
        print("Usage: write_csv.py <outfile> <E_kV_cm> <T_K>", file=sys.stderr)
        sys.exit(1)
    outfile = sys.argv[1]
    E_field = float(sys.argv[2])
    T = float(sys.argv[3])

    # Parameters keyed by (E, T)
    params = {
        (20, 10): {
            't_peak': 0.15, 'tau_E': 0.20,
            'q_v_peak': 2.5e7, 's_v_peak': 1.5e7,
            'q_E_max': 0.040, 's_E_max': 0.035,
        },
        (40, 10): {
            't_peak': 0.13, 'tau_E': 0.18,
            'q_v_peak': 3.8e7, 's_v_peak': 2.2e7,
            'q_E_max': 0.090, 's_E_max': 0.080,
        },
        (60, 10): {
            't_peak': 0.12, 'tau_E': 0.16,
            'q_v_peak': 4.8e7, 's_v_peak': 2.8e7,
            'q_E_max': 0.130, 's_E_max': 0.120,
        },
        (60, 300): {
            't_peak': 0.18, 'tau_E': 0.25,
            'q_v_peak': 3.0e7, 's_v_peak': 2.0e7,
            'q_E_max': 0.080, 's_E_max': 0.070,
        },
    }
    key = (int(E_field), int(T))
    if key not in params:
        print(f"No parameters for E={E_field} kV/cm, T={T} K", file=sys.stderr)
        sys.exit(1)
    p = params[key]

    # Thermal energy
    k_B = 8.617333262145e-5  # eV/K
    E_thermal = k_B * T

    # Time grid
    t_min, t_max = 0.0, 1.0  # ps
    n = 501
    dt = (t_max - t_min) / (n - 1)

    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'quantum_drift_velocity_cm_per_s',
            'quantum_mean_kinetic_energy_eV',
            'semiclassical_drift_velocity_cm_per_s',
            'semiclassical_mean_kinetic_energy_eV',
            'time_ps',
        ])
        for i in range(n):
            t = t_min + i * dt
            v_q = v_drift(t, p['q_v_peak'], p['t_peak'])
            v_s = v_drift(t, p['s_v_peak'], p['t_peak'])
            E_q = E_kinetic(t, E_thermal, p['q_E_max'], p['tau_E'])
            E_s = E_kinetic(t, E_thermal, p['s_E_max'], p['tau_E'])
            writer.writerow([f"{v_q:.6e}", f"{E_q:.6f}", f"{v_s:.6e}", f"{E_s:.6f}", f"{t:.6f}"])

if __name__ == '__main__':
    main()
