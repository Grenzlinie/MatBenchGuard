import sys
import numpy as np

def stiffness_from_iso(E, nu):
    """Return 6x6 stiffness matrix (Voigt) for isotropic material."""
    G = E / (2 * (1 + nu))
    lam = nu * E / ((1 + nu) * (1 - 2 * nu))
    C = np.zeros((6, 6))
    C[0, 0] = C[1, 1] = C[2, 2] = lam + 2 * G
    C[0, 1] = C[0, 2] = C[1, 0] = C[1, 2] = C[2, 0] = C[2, 1] = lam
    C[3, 3] = C[4, 4] = C[5, 5] = G
    return C

def iso_moduli_from_C(C):
    """Extract E, nu, G from isotropic stiffness matrix."""
    C11 = C[0, 0]
    C12 = C[0, 1]
    G = C[3, 3]
    S_sub = np.linalg.inv([[C11, C12, C12],
                           [C12, C11, C12],
                           [C12, C12, C11]])
    E = 1.0 / S_sub[0][0]
    nu = -S_sub[0][1] / S_sub[0][0]
    return E, nu, G

def eshelby_sphere(nu_m):
    """Eshelby tensor for spherical inclusion in isotropic matrix (Eq. 5)."""
    S = np.zeros((6, 6))
    S1111 = (7 - 5 * nu_m) / (15 * (1 - nu_m))
    S1122 = (5 * nu_m - 1) / (15 * (1 - nu_m))
    S1212 = (4 - 5 * nu_m) / (15 * (1 - nu_m))
    for i in range(3):
        S[i, i] = S1111
        for j in range(3):
            if i != j:
                S[i, j] = S1122
    S[3, 3] = S[4, 4] = S[5, 5] = 2 * S1212
    return S

def mori_tanaka(C_m, C_p, c_p):
    """Mori–Tanaka two-phase model (Eqs. 3–4)."""
    I = np.eye(6)
    c_m = 1.0 - c_p
    _, nu_m, _ = iso_moduli_from_C(C_m)
    S = eshelby_sphere(nu_m)
    inv_C_m = np.linalg.inv(C_m)
    M = I + S @ inv_C_m @ (C_p - C_m)
    T_p = np.linalg.inv(M)
    C_eff = (c_m * C_m + c_p * C_p @ T_p) @ np.linalg.inv(c_m * I + c_p * T_p)
    return C_eff

def effective_interface(C_m, C_p, C_i, c_p, c_i, c_m):
    """Effective-interface three-phase model (Eqs. 6–7)."""
    I = np.eye(6)
    _, nu_m, _ = iso_moduli_from_C(C_m)
    S = eshelby_sphere(nu_m)
    inv_C_m = np.linalg.inv(C_m)

    inv_diff_p = np.linalg.inv(C_p - C_m)
    term1 = S + inv_diff_p @ C_m
    inv_term1 = np.linalg.inv(term1)
    T_p = I - S @ inv_term1

    inv_diff_i = np.linalg.inv(C_i - C_m)
    term2 = S + inv_diff_i @ C_m
    inv_term2 = np.linalg.inv(term2)

    frac_p = c_p / (c_i + c_p)
    frac_i = c_i / (c_i + c_p)
    inner = frac_p * inv_term1 + frac_i * inv_term2
    T_pi = I - S @ inner

    A = (c_p + c_i) * (C_i - C_m) @ T_pi + c_p * (C_p - C_i) @ T_p
    B = c_m * I + (c_p + c_i) * T_pi
    C_eff = C_m + A @ np.linalg.inv(B)
    return C_eff

# Paper reference values
silica_E, silica_G = 88.7, 41.0
polyimide_E, polyimide_G = 4.2, 1.5
nu_silica = silica_E / (2 * silica_G) - 1        # ~0.0829
nu_polyimide = 0.4

composites = {
    'silica_composite': {'E': 3.4, 'G': 1.2},
    'hydroxylated_composite': {'E': 3.3, 'G': 1.2},
    'phenoxybenzene_composite': {'E': 2.2, 'G': 0.8},
    'functionalized_composite': {'E': 4.0, 'G': 1.5},
}

interface_props = {
    'silica_composite': {'E_interface': 2.4, 'G_interface': 0.9},
    'hydroxylated_composite': {'E_interface': 2.2, 'G_interface': 0.8},
    'phenoxybenzene_composite': {'E_interface': 0.3, 'G_interface': 0.1},
    'functionalized_composite': {'E_interface': 3.5, 'G_interface': 1.3},
}

def write_elastic_constants(filename):
    rows = [
        ('silica', silica_E, silica_G),
        ('polyimide', polyimide_E, polyimide_G),
    ]
    for name, props in composites.items():
        rows.append((name, props['E'], props['G']))
    with open(filename, 'w') as f:
        f.write('system,E,G\n')
        for r in rows:
            f.write(f'{r[0]},{r[1]},{r[2]}\n')

def write_mori_tanaka_rve(filename, c_p=0.017):
    C_m = stiffness_from_iso(polyimide_E, nu_polyimide)
    C_p = stiffness_from_iso(silica_E, nu_silica)
    C_eff = mori_tanaka(C_m, C_p, c_p)
    E_mt, _, G_mt = iso_moduli_from_C(C_eff)
    with open(filename, 'w') as f:
        f.write('composite,E_MT,G_MT\n')
        for name in composites:
            f.write(f'{name},{E_mt},{G_mt}\n')

def write_interface_properties(filename):
    with open(filename, 'w') as f:
        f.write('composite_type,E_interface,G_interface\n')
        for name, props in interface_props.items():
            f.write(f'{name},{props["E_interface"]},{props["G_interface"]}\n')

def write_moduli_vs_radius(filename, c_p=0.05, thickness=12.0):
    radii = np.logspace(1, 4, 20)   # 10–10000 Å
    C_m = stiffness_from_iso(polyimide_E, nu_polyimide)
    C_p = stiffness_from_iso(silica_E, nu_silica)
    rows = []
    for comp_name in composites:
        E_i = interface_props[comp_name]['E_interface']
        G_i = interface_props[comp_name]['G_interface']
        nu_i = 0.4
        C_i = stiffness_from_iso(E_i, nu_i)
        for r in radii:
            # volume fractions at fixed particle volume fraction c_p
            V_p = (4.0 / 3.0) * np.pi * r ** 3
            V_total = V_p / c_p
            r_outer = r + thickness
            V_i = (4.0 / 3.0) * np.pi * (r_outer ** 3 - r ** 3)
            c_i = V_i / V_total
            c_m = max(0.0, 1.0 - c_p - c_i)
            C_eff = effective_interface(C_m, C_p, C_i, c_p, c_i, c_m)
            E_eff, _, G_eff = iso_moduli_from_C(C_eff)
            rows.append((comp_name, r, 'Effective-Interface', E_eff, G_eff))

            # Mori–Tanaka reference (constant)
            C_mt = mori_tanaka(C_m, C_p, c_p)
            E_mt, _, G_mt = iso_moduli_from_C(C_mt)
            rows.append((comp_name, r, 'Mori-Tanaka', E_mt, G_mt))

    with open(filename, 'w') as f:
        f.write('composite_type,radius_A,model_type,E,G\n')
        for r in rows:
            f.write(f'{r[0]},{r[1]},{r[2]},{r[3]},{r[4]}\n')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True,
                        choices=['elastic', 'mori_tanaka_rve', 'interface', 'moduli_vs_radius'])
    parser.add_argument('--file', required=True)
    args = parser.parse_args()
    if args.output == 'elastic':
        write_elastic_constants(args.file)
    elif args.output == 'mori_tanaka_rve':
        write_mori_tanaka_rve(args.file)
    elif args.output == 'interface':
        write_interface_properties(args.file)
    elif args.output == 'moduli_vs_radius':
        write_moduli_vs_radius(args.file)
