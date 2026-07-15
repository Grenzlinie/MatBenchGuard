#!/usr/bin/env python3
import math, json, csv, sys, os

# ---------- Blackburn oxygen-potential model ----------
def pO2_blackburn(T, x, is_liquid=True):
    """Return p(O2) in atm. is_liquid selects the parameter set."""
    if is_liquid:
        A1, B1 = 7.680, -57576.0
        A2, B2 = -25986.0, 147352.0
    else:
        A1, B1 = 7.680, -60805.0
        A2, B2 = -28786.0, 159317.0
    lnK1 = A1 + B1 / T
    K1 = math.exp(lnK1)
    # solve for (U4+) from Eq. (37)
    disc = 1.0 - (x*x - 1.0) * (4.0*K1 - 1.0)
    if disc <= 0.0:
        return 0.0
    U4 = (-1.0 + math.sqrt(disc)) / (4.0*K1 - 1.0)
    # (U2+) from Eq. (35)
    U2 = (1.0 + x - U4) / 2.0
    # p(O2) from Eq. (38) – in atm
    ln_pO2 = 2.0 * math.log(max((U4 * (2.0 - x)) / U2, 1e-12)) - (A2 + B2 / T)
    return math.exp(ln_pO2)

# ---------- Gas-phase and condensed-phase free energies (kJ/mol) ----------
# Coefficients from Table 1 (ΔGf° = A + B*T + C*T^2 + D/T + E*ln(T) + F*T^3)

COEFFS = {
    'O': {
        (298.15, 1400): (252.36, -6.2747e-2, -1.3294e-6, -527.69, 0.0, 0.0),
        (1400, 6000):  (259.03, -6.7710e-2, -1.6525e-8, -3747.4, 0.0, 0.0)
    },
    'U': {
        (298.15, 1400): (539.11, -1.6007e-1, 1.7321e-5, -1046.4, 0.0, 0.0),
        (1400, 4435):  (749.73, -8.3008e-2, -2.0904e-6, 0.0, -40.548, 0.0),
        (4435, 6000):  (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    },
    'UO': {
        (298.15, 1400): (26.863, -1.0515e-1, 1.6100e-5, -1002.4, 0.0, 0.0),
        (1400, 4435):  (178.98, -4.2342e-2, 2.0064e-6, 0.0, -29.432, 0.0),
        (4435, 6000):  (-521.65, 5.8124e-2, 2.4020e-6, 0.0, 0.0, 0.0)
    },
    'UO2': {
        (298.15, 1400): (-501.42, -4.2567e-2, 1.4530e-5, 0.0, 7.5475, 0.0),
        (1400, 4435):  (-367.02, 1.4476e-2, 1.7735e-6, 0.0, -18.571, 0.0),
        (4435, 6000):  (-989.24, 1.1823e-1, 2.0798e-6, 0.0, 0.0, 0.0)
    },
    'UO3': {
        (298.15, 1400): (-822.97, 2.5295e-2, 1.4770e-5, 0.0, 4.9754, 0.0),
        (1400, 4435):  (-707.37, 8.0256e-2, 1.9058e-6, 0.0, -18.131, 0.0),
        (4435, 6000):  (-1321.1, 1.8201e-1, 2.4230e-6, 0.0, 0.0, 0.0)
    },
    'UO2c': {
        (298.15, 1400): (-1131.0, 1.4405e-1, 8.1068e-6, 0.0, 9.7445, 0.0),
        (1400, 2670):  (-1079.8, 1.5714e-1, 1.2365e-4, 0.0, 0.0, -2.6564e-1),
        (2670, 3120):  (-1167.1, 2.4280e-1, -1.4569e-5, 0.0, 0.0, 0.0),
        (3120, 4435):  (-1002.7, 1.6163e-1, -5.4369e-6, 0.0, 0.0, 0.0),
        (4435, 6000):  (-1453.7, 2.5458e-1, -3.4634e-6, 0.0, 0.0, 0.0)
    }
}

def get_DGf(species, T):
    table = COEFFS[species]
    for (lo, hi), coeffs in table.items():
        if lo <= T <= hi:
            A, B, C, D, E, F = coeffs
            return A + B*T + C*T*T + D/T + (E*math.log(T) if E else 0) + F*T*T*T
    return 0.0

# ---------- Integration helper ----------
def cumulative_trapz(y, dx):
    c = [0.0]
    for i in range(1, len(y)):
        c.append(c[-1] + 0.5 * (y[i-1] + y[i]) * dx)
    return c

# ---------- Main computation ----------
def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    R = 0.008314  # kJ/(mol·K)
    atm_to_MPa = 0.101325
    # temperatures for grids and targets
    T_list = [3150.0, 5000.0, 6000.0]
    # fine x grid from 0 to 0.5
    dx = 0.001
    x_grid = [i*dx for i in range(501)]   # 0.0, 0.001, ..., 0.500
    # target x values for O/U = 1.90 (x=0.10), 1.96 (x=0.04), 2.00 (x=0.00)
    target_x = [0.10, 0.04, 0.00]
    # also need x for UO1.96 (x=0.04) at 5000K, and UO2.00 (x=0.0) at 5000K

    # ---------- Step 1: pO2 grids (in atm) ----------
    pO2_grids = {}  # T -> dict x -> pO2_atm
    for T in T_list:
        pO2_grids[T] = [pO2_blackburn(T, x, is_liquid=True) for x in x_grid]

    # Save pO2_grid.csv (columns: T, x, pO2_MPa)
    with open(os.path.join(outdir, 'pO2_grid.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'x', 'pO2_MPa'])
        for T in T_list:
            for x, p in zip(x_grid, pO2_grids[T]):
                writer.writerow([T, x, p * atm_to_MPa])

    # ---------- Step 2: integrate and compute ΔGf(UO2−x,c) ----------
    deltaG_grids = {}  # T -> list of DGf(UO2_x) in kJ/mol
    for T in T_list:
        DGf_UO2_stoich = get_DGf('UO2c', T)
        ln_pO2 = [math.log(max(p, 1e-30)) for p in pO2_grids[T]]
        integral_ln = cumulative_trapz(ln_pO2, dx)
        # Δ(0,x) = (R*T/2) * integral
        Delta = [(R * T / 2.0) * val for val in integral_ln]
        # Eq. (24) for Region VI (all target T > 3120 K)
        DGf_UO2x = [DGf_UO2_stoich - d for d in Delta]
        deltaG_grids[T] = DGf_UO2x

    # Save deltaG_grid.csv
    with open(os.path.join(outdir, 'deltaG_grid.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'x', 'deltaG_kJ_per_mol'])
        for T in T_list:
            for x, dg in zip(x_grid, deltaG_grids[T]):
                writer.writerow([T, x, dg])

    # ---------- Step 3: compute scored outputs ----------
    results = {}
    # Helper to interpolate (nearest neighbour on fine grid is sufficient)
    def interp(x_vals, y_vals, x_target):
        idx = min(range(len(x_vals)), key=lambda i: abs(x_vals[i] - x_target))
        return y_vals[idx]

    # First: p(O2) at the six target conditions (MPa)
    conds = [
        (3150, 0.10, 'pO2_3150_1_90'),
        (3150, 0.04, 'pO2_3150_1_96'),
        (3150, 0.00, 'pO2_3150_2_00'),
        (6000, 0.10, 'pO2_6000_1_90'),
        (6000, 0.04, 'pO2_6000_1_96'),
        (6000, 0.00, 'pO2_6000_2_00'),
    ]
    for T, x, key in conds:
        p_atm = interp(x_grid, pO2_grids[T], x)
        results[key] = p_atm * atm_to_MPa

    # Next: total pressure at 5000 K for UO2.00 (x=0.0) and vapor O/U at 5000 K for UO1.96 (x=0.04)
    for (Tref, xref, key_total, key_ou) in [(5000, 0.0, 'total_pressure_5000_UO2', None),
                                             (5000, 0.04, None, 'vapor_OU_5000_UO1_96')]:
        # Get pO2_atm and DGf(UO2-x,c) for this point
        pO2_atm = interp(x_grid, pO2_grids[Tref], xref)
        DGf_cond = interp(x_grid, deltaG_grids[Tref], xref)
        # Gas-phase free energies (kJ/mol)
        DGf_O = get_DGf('O', Tref)
        DGf_U = get_DGf('U', Tref)
        DGf_UO = get_DGf('UO', Tref)
        DGf_UO2 = get_DGf('UO2', Tref)
        DGf_UO3 = get_DGf('UO3', Tref)
        ln_pO2 = math.log(pO2_atm)
        # Partial pressures (atm) using Eqs. (8)-(12)
        ln_p_O = 0.5 * ln_pO2 - DGf_O / (R * Tref)
        p_O = math.exp(ln_p_O)
        ln_p_UO2 = (xref / 2.0) * ln_pO2 + (DGf_cond - DGf_UO2) / (R * Tref)
        p_UO2 = math.exp(ln_p_UO2)
        ln_p_UO = ln_p_UO2 - 0.5 * ln_pO2 + (DGf_UO2 - DGf_UO) / (R * Tref)
        p_UO = math.exp(ln_p_UO)
        ln_p_UO3 = ln_p_UO2 + 0.5 * ln_pO2 + (DGf_UO2 - DGf_UO3) / (R * Tref)
        p_UO3 = math.exp(ln_p_UO3)
        ln_p_U = ln_p_UO2 - ln_pO2 + (DGf_UO2 - DGf_U) / (R * Tref)
        p_U = math.exp(ln_p_U)
        total_atm = p_O + p_O2_atm + p_U + p_UO + p_UO2 + p_UO3
        if key_total:
            results[key_total] = total_atm * atm_to_MPa
        if key_ou:
            numer = p_O + 2.0 * p_O2_atm + p_UO + 2.0 * p_UO2 + 3.0 * p_UO3
            denom = p_U + p_UO + p_UO2 + p_UO3
            results[key_ou] = numer / denom if denom > 0 else 0.0

    # Write step_01_results.json
    with open(os.path.join(outdir, 'step_01_results.json'), 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == '__main__':
    main(sys.argv[1])
