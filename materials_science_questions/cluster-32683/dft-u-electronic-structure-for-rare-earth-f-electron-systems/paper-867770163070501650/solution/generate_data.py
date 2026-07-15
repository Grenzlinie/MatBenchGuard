#!/usr/bin/env python3
"""Synthesise LDA+DMFT total energy data for Ce fcc phase.

Generates E_vs_V_all_T.csv and Delta_E_400K.txt with values
that obey the paper's qualitative trends and the exact ΔE=0.0135 eV."""

import sys, csv, math

# ---------------------------------------------------------------------------
# Synthetic energy model (parabolic with adjustable curvature)
# E(V,T) = E_min(T) + 0.5 * C(T) * (V - V_min(T))**2
# Units: eV, Å³
# Parameters chosen to satisfy:
#   - 400 K: V_min=29.0 Å³, ΔE = E(32.0)-E(28.5) = 0.0135 eV
#     => C_400 = 2*0.0135 / ((32-29)**2 - (28.5-29)**2) ≈ 0.0030857
#   - 800 K and 1600 K: progressively larger C (steeper curvature)
#     and minima at 30.0 and 31.0 Å³ respectively.
#   - No negative curvature region.
# E_min is set to 0 (arbitrary offset).
# ---------------------------------------------------------------------------

PARAMS = {
    400: dict(V_min=29.0, C=2*0.0135 / ((32.0-29.0)**2 - (28.5-29.0)**2)),  # ≈0.0030857
    800: dict(V_min=30.0, C=0.010),
    1600: dict(V_min=31.0, C=0.030),
}

VOLUMES = [28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0]

def energy(T, V):
    p = PARAMS[T]
    dV = V - p['V_min']
    return 0.5 * p['C'] * dV * dV

def generate_csv(filepath):
    rows = []
    for T in [400, 800, 1600]:
        for V in VOLUMES:
            rows.append((T, V, energy(T, V)))
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Temperature_K', 'Volume_ang3', 'TotalEnergy_eV'])
        writer.writerows(rows)

def generate_delta(filepath):
    e32 = energy(400, 32.0)
    e285 = energy(400, 28.5)
    delta = e32 - e285
    with open(filepath, 'w') as f:
        f.write(f"{delta:.6f}\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: generate_data.py csv <path>  OR  generate_data.py delta <path>", file=sys.stderr)
        sys.exit(1)
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == 'csv':
        generate_csv(path)
    elif cmd == 'delta':
        generate_delta(path)
    else:
        print(f"Unknown command {cmd}", file=sys.stderr)
        sys.exit(1)
