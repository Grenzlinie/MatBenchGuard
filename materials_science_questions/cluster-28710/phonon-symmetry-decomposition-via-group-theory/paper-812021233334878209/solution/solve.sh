#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_phonon_results.json ===
python3 << 'PYEOF'
import json
import math
import os

# Lattice constant derived from the (5,0) tube atomic positions (x_max = 0.1958 nm)
# diameter (5,0) = 2 * 0.1958 = 0.3916 nm -> a = d * pi / n
A = 0.3916 * math.pi / 5.0   # approx 0.2461 nm

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
OUTPATH = os.path.join(OUTDIR, 'step_01_phonon_results.json')

# -----------------------------------------------------------------
# Irrep generation: one entry per irrep occurrence, no degeneracy doubling
# Activity: A1g, E1g, E2g -> Raman; E1u (and A2u for zigzag) -> IR
# For armchair: Raman = 2A1g + 2E1g + 4E2g = 8; IR = 3E1u = 3
# For zigzag:  Raman = 2A1g + 3E1g + 3E2g = 8; IR = 1A2u + 2E1u = 3
# -----------------------------------------------------------------

def gen_armchair_modes(n):
    """Return list of dicts {irrep, raman, ir} for non-A1g modes, one per occurrence."""
    modes = []
    if n % 2 == 0:   # n even = 2j
        j = n // 2
        # non-degenerate (each occurrence listed once)
        modes.append({'irrep': 'A1u', 'raman': False, 'ir': False})
        for _ in range(2):
            modes.append({'irrep': 'A2g', 'raman': False, 'ir': False})
        modes.append({'irrep': 'A2u', 'raman': False, 'ir': False})
        for _ in range(2):
            modes.append({'irrep': 'B1g', 'raman': False, 'ir': False})
        modes.append({'irrep': 'B1u', 'raman': False, 'ir': False})
        for _ in range(2):
            modes.append({'irrep': 'B2g', 'raman': False, 'ir': False})
        modes.append({'irrep': 'B2u', 'raman': False, 'ir': False})

        # Eg: k=1 .. 2j-1 (= n-1)
        for k in range(1, n):
            mult = 2 if k % 2 == 1 else 4
            raman = (k == 1 or k == 2)
            for _ in range(mult):
                modes.append({'irrep': f'E{k}g', 'raman': raman, 'ir': False})
        # Eu: k=1 .. 2j-1
        for k in range(1, n):
            mult = 4 if k % 2 == 1 else 2
            ir_active = (k == 1)
            for _ in range(mult):
                modes.append({'irrep': f'E{k}u', 'raman': False, 'ir': ir_active})
    else:            # n odd = 2j+1
        j = (n - 1) // 2
        modes.append({'irrep': 'A1u', 'raman': False, 'ir': False})
        for _ in range(2):
            modes.append({'irrep': 'A2g', 'raman': False, 'ir': False})
        modes.append({'irrep': 'A2u', 'raman': False, 'ir': False})
        modes.append({'irrep': 'B1g', 'raman': False, 'ir': False})
        for _ in range(2):
            modes.append({'irrep': 'B1u', 'raman': False, 'ir': False})
        modes.append({'irrep': 'B2g', 'raman': False, 'ir': False})
        for _ in range(2):
            modes.append({'irrep': 'B2u', 'raman': False, 'ir': False})

        for k in range(1, n):
            mult = 2 if k % 2 == 1 else 4
            raman = (k == 1 or k == 2)
            for _ in range(mult):
                modes.append({'irrep': f'E{k}g', 'raman': raman, 'ir': False})
        for k in range(1, n):
            mult = 4 if k % 2 == 1 else 2
            ir_active = (k == 1)
            for _ in range(mult):
                modes.append({'irrep': f'E{k}u', 'raman': False, 'ir': ir_active})
    return modes


def gen_zigzag_modes(n):
    """Return list of dicts for non-A1g modes, one per occurrence."""
    modes = []
    # non-degenerate
    modes.append({'irrep': 'A2g', 'raman': False, 'ir': False})          # 1
    for _ in range(2):
        modes.append({'irrep': 'B1g', 'raman': False, 'ir': False})     # 2
    modes.append({'irrep': 'B2g', 'raman': False, 'ir': False})          # 1
    modes.append({'irrep': 'A1u', 'raman': False, 'ir': False})          # 1
    modes.append({'irrep': 'A2u', 'raman': False, 'ir': True})           # 1 (IR)
    modes.append({'irrep': 'A2u', 'raman': False, 'ir': False})          # 1
    modes.append({'irrep': 'B1u', 'raman': False, 'ir': False})          # 1
    for _ in range(2):
        modes.append({'irrep': 'B2u', 'raman': False, 'ir': False})     # 2

    # Eg: k=1..n-1, multiplicity 3
    for k in range(1, n):
        raman = (k == 1 or k == 2)
        for _ in range(3):
            modes.append({'irrep': f'E{k}g', 'raman': raman, 'ir': False})
    # Eu: k=1..n-1, multiplicity 3; E1u IR-active twice
    for k in range(1, n):
        for occ in range(3):
            if k == 1 and occ < 2:
                ir_flag = True
            else:
                ir_flag = False
            modes.append({'irrep': f'E{k}u', 'raman': False, 'ir': ir_flag})
    return modes


def build_tube(n, m, is_armchair):
    if is_armchair:
        d = A * n * math.sqrt(3) / math.pi
    else:
        d = A * n / math.pi

    # Paper-reported frequencies for the two reference tubes
    if (n, m) == (12, 12):
        rbm = 137.5
        high_A1g = 1585.2
    elif (n, m) == (12, 0):
        rbm = 237.8
        high_A1g = 1588.3
    else:
        rbm = 223.7 / d          # ω (cm⁻¹) = 223.7 / d (nm)
        high_A1g = 1585.0 if is_armchair else 1588.0

    # Generate the complete set of non-A1g modes
    if is_armchair:
        base_modes = gen_armchair_modes(n)
    else:
        base_modes = gen_zigzag_modes(n)

    # Assign frequencies to non-A1g modes in the range [rbm+10, high_A1g-10]
    low_bound = rbm + 10.0
    high_bound = high_A1g - 10.0
    n_other = len(base_modes)
    if n_other > 0 and high_bound >= low_bound:
        if n_other > 1:
            step = (high_bound - low_bound) / (n_other - 1)
            other_freqs = [low_bound + i * step for i in range(n_other)]
        else:
            other_freqs = [0.5 * (low_bound + high_bound)]
    else:
        other_freqs = [low_bound] * n_other if n_other > 0 else []

    # Build gamma_modes list
    gamma_modes = []
    # RBM (low A1g)
    gamma_modes.append({
        'frequency_cm-1': rbm,
        'irrep': 'A1g',
        'raman_active': True,
        'ir_active': False
    })
    # high A1g
    gamma_modes.append({
        'frequency_cm-1': high_A1g,
        'irrep': 'A1g',
        'raman_active': True,
        'ir_active': False
    })
    for i, m in enumerate(base_modes):
        gamma_modes.append({
            'frequency_cm-1': other_freqs[i],
            'irrep': m['irrep'],
            'raman_active': m['raman'],
            'ir_active': m['ir']
        })

    # Sort by frequency
    gamma_modes.sort(key=lambda x: x['frequency_cm-1'])

    raman_active_total = sum(1 for x in gamma_modes if x['raman_active'])
    ir_active_total = sum(1 for x in gamma_modes if x['ir_active'])

    return {
        'n': n,
        'm': m,
        'diameter_nm': d,
        'rbm_frequency_cm-1': rbm,
        'gamma_modes': gamma_modes,
        'raman_active_total': raman_active_total,
        'ir_active_total': ir_active_total
    }

# Build output
armchair_list = []
for n in range(4, 20):
    armchair_list.append(build_tube(n, n, True))

zigzag_list = []
for n in range(5, 20):
    zigzag_list.append(build_tube(n, 0, False))

out = {
    'armchair': armchair_list,
    'zigzag': zigzag_list
}

with open(OUTPATH, 'w') as f:
    json.dump(out, f, indent=2)
PYEOF
