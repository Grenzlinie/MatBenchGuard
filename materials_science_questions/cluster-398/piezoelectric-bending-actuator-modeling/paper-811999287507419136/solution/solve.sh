#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: c_values.json ===
python3 -c "
import json, math, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

# ---------- geometry & material constants ----------
L0 = 5.5e-3

# negative strain component (ESC) geometry (same for all)
t_neg = 470e-6
b_neg = 3e-3          # effective width (not used for strain)
# active EAP layer geometry
t_active = 16e-6
b_active = 3e-3

# inactive layers for clamping ratio (original design dimensions)
def S(E, t, b):
    return E * t * b

E_inact_ea = 1e9
E_epoxy = 5e9
E_gold = 74e9
E_margins = 1e9

S_inact_total = (S(E_inact_ea, 15e-6, 4.5e-3) +
                 S(E_epoxy, 1e-6, 4.5e-3) +
                 2 * S(E_gold, 0.1e-6, 3e-3) +
                 2 * S(E_margins, 16e-6, 0.75e-3))

# ---------- arc-length integrand & Riemann sum ----------
def integrand(x, c, Ld):
    return math.sqrt(c*c * (4*x*x*x - Ld*Ld*x)**2 + 1.0)

def riemann_sum(c, Ld, n=1000):
    a = -Ld/2
    b =  Ld/2
    dx = (b - a) / n
    total = 0.0
    x = a
    for _ in range(n):
        total += integrand(x, c, Ld)
        x += dx
    return total * dx

# ---------- iterative solver for c ----------
def solve_c(Ld, RHS, initial_guess=1.0, tol=1e-5):
    low, high = 0.0, max(10.0, initial_guess*2)
    while riemann_sum(high, Ld) < RHS:
        high *= 2
    for _ in range(200):
        mid = (low + high) / 2
        LHS = riemann_sum(mid, Ld)
        if LHS < RHS:
            low = mid
        else:
            high = mid
        LHS_cur = riemann_sum(mid, Ld)
        error = abs(LHS_cur - RHS) / RHS * 100
        if error < tol:
            return mid, error
        if high - low < 1e-12:
            break
    c = (low + high) / 2
    LHS = riemann_sum(c, Ld)
    error = abs(LHS - RHS) / RHS * 100
    return c, error

# ---------- strain helpers ----------
def compute_Ld(active_esc, V, d31_neg):
    if active_esc:
        s_neg = d31_neg * V / t_neg
        return L0 * (1 + s_neg)
    else:
        return L0

def compute_RHS(active_eap, V, d31_pos, E_active):
    if active_eap:
        k = S_inact_total / (E_active * t_active * b_active)
        s0 = d31_pos * V / t_active
        s_eff = s0 / (1 + k)
        return L0 * (1 + s_eff)
    else:
        return L0

# ========== Step 1: c_values for original HYBAS ==========
cases = []
voltages = [200, 400, 800, 1600]
modes = [('EAP', True, False), ('ESC', False, True), ('HYBAS', True, True)]
d31_neg_orig = -970e-12
d31_pos_orig = 20e-12
E_active_orig = 1e9
for V in voltages:
    for mode_name, active_eap, active_esc in modes:
        Ld = compute_Ld(active_esc, V, d31_neg_orig)
        RHS = compute_RHS(active_eap, V, d31_pos_orig, E_active_orig)
        c_val, err = solve_c(Ld, RHS)
        c10 = c_val * 1e-6
        cases.append({
            'voltage': V,
            'active_elements': mode_name,
            'c': round(c10, 4),
            'percent_error': round(err, 4)
        })
with open(f'{OUTDIR}/c_values.json', 'w') as f:
    json.dump(cases, f, indent=2)
print('c_values.json written')

# ========== Step 2: max_displacements for trade study ==========
neg_materials = [
    ('Hard PZT (TRS100HD)', -150e-12, 79e9),
    ('Soft PZT (TRSHK1HD)', -360e-12, 67e9),
    ('PZN-4.5%PT single crystal', -970e-12, 12e9)
]
pos_materials = [
    ('Uni-axial PVDF', 20e-12, 2e9),
    ('Bi-axial PVDF', 8e-12, 2e9)
]
max_disp = []
for Vrms in [100, 650]:
    for neg_name, d31_neg, E_neg in neg_materials:
        for pos_name, d31_pos, E_pos in pos_materials:
            Ld = compute_Ld(True, Vrms, d31_neg)   # both active
            RHS = compute_RHS(True, Vrms, d31_pos, E_pos)
            c_val, _ = solve_c(Ld, RHS)
            w_microns = (c_val * (Ld**4) / 16) * 1e6
            max_disp.append({
                'negative_strain_material': neg_name,
                'positive_strain_material': pos_name,
                'voltage': Vrms,
                'max_displacement': round(w_microns, 4)
            })
with open(f'{OUTDIR}/max_displacements.json', 'w') as f:
    json.dump(max_disp, f, indent=2)
print('max_displacements.json written')
"

# === solve block: max_displacements.json ===
python3 /solution/compute.py --output max_displacements.json
