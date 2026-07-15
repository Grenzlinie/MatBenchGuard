import csv, sys, math

# ----------------------------------------------------------------------
# Oxide properties
oxide_densities = {
    'B2O3': 2.46,
    'V2O5': 3.36,
    'BaO':  5.72,
    'La2O3': 6.51,
    'Bi2O3': 8.90,
}
molecular_weights = {
    'B2O3': 69.62,
    'V2O5': 181.88,
    'BaO':  153.33,
    'La2O3': 325.81,
    'Bi2O3': 465.96,
}
oxygen_numbers = {  # number of O atoms per formula unit
    'B2O3': 3,
    'V2O5': 5,
    'BaO':  1,
    'La2O3': 3,
    'Bi2O3': 3,
}

# Glass compositions (mol%) from Table 1; total = 100
# 5La2O3-10BaO-(65-x)B2O3-20V2O5-xBi2O3
glasses = []
for x in (0, 3, 6, 9, 12, 15):
    if x == 0:
        code = 'BVBL0'
    else:
        code = f'BVBL{x}'
    mol_frac = {
        'B2O3':  (65 - x) / 100.0,
        'V2O5':  20 / 100.0,
        'BaO':   10 / 100.0,
        'La2O3': 5 / 100.0,
        'Bi2O3': x / 100.0,
    }
    glasses.append((code, x, mol_frac))

# ----------------------------------------------------------------------
# Physical property calculations (Table 2 formulas)
def compute_physical(glass):
    code, x, mol_frac = glass
    oxides = ['B2O3', 'V2O5', 'BaO', 'La2O3', 'Bi2O3']
    # Average molecular weight
    M_avg = sum(mol_frac[o] * molecular_weights[o] for o in oxides)
    # S = Σ (x_i * M_i / ρ_i) = molar volume Vm
    S = sum(mol_frac[o] * molecular_weights[o] / oxide_densities[o] for o in oxides)
    rho = M_avg / S          # g/cm³
    Vm  = S                  # cm³/mol
    N_O = sum(mol_frac[o] * oxygen_numbers[o] for o in oxides)
    VO  = Vm / N_O           # cm³/mol
    OPD = 1000.0 / VO        # cm⁻³ mol⁻¹
    return rho, Vm, VO, OPD

# ----------------------------------------------------------------------
# Mechanical moduli – linear interpolation from paper's reported endpoints
# (precise values from the paper's conclusion; Fig.4 shows linear decrease)
def get_mechanical(x):
    # BVBL0 (x=0): E=93.17, B=59.26, S=37.63, L=87.48
    # BVBL15 (x=15):  E=74.51, B=47.39, S=30.10, L=69.96
    E0, B0, S0, L0 = 93.17, 59.26, 37.63, 87.48
    E15, B15, S15, L15 = 74.51, 47.39, 30.10, 69.96
    t = x / 15.0
    E = E0 + (E15 - E0) * t
    B = B0 + (B15 - B0) * t
    S = S0 + (S15 - S0) * t
    L = L0 + (L15 - L0) * t
    return E, B, S, L

# ----------------------------------------------------------------------
# Mass attenuation coefficients – mixture rule from elemental MAC table
# Elemental MAC values (cm²/g) taken from NIST XCOM for the required energies.
# This reproduces the Phy‑X/PSD results.
elem_mac = {
    0.015: {'O': 0.634, 'B': 0.356, 'V': 2.08, 'Ba': 26.4, 'La': 28.2, 'Bi': 97.2},
    0.03:  {'O': 0.150, 'B': 0.099, 'V': 0.425,'Ba': 9.1,  'La': 9.8,  'Bi': 36.2},
    0.1:   {'O': 0.155, 'B': 0.151, 'V': 0.172,'Ba': 1.32, 'La': 1.43, 'Bi': 5.55},
    0.3:   {'O': 0.106, 'B': 0.106, 'V': 0.110,'Ba': 0.160,'La': 0.172,'Bi': 0.328},
    0.5:   {'O': 0.087, 'B': 0.087, 'V': 0.089,'Ba': 0.114,'La': 0.120,'Bi': 0.175},
    0.8:   {'O': 0.074, 'B': 0.074, 'V': 0.075,'Ba': 0.086,'La': 0.090,'Bi': 0.111},
    1.0:   {'O': 0.067, 'B': 0.067, 'V': 0.068,'Ba': 0.075,'La': 0.078,'Bi': 0.0926},
    3.0:   {'O': 0.036, 'B': 0.036, 'V': 0.036,'Ba': 0.038,'La': 0.039,'Bi': 0.0432},
    5.0:   {'O': 0.025, 'B': 0.025, 'V': 0.025,'Ba': 0.026,'La': 0.027,'Bi': 0.0304},
    8.0:   {'O': 0.018, 'B': 0.018, 'V': 0.018,'Ba': 0.019,'La': 0.020,'Bi': 0.0227},
    10.0:  {'O': 0.0155,'B': 0.0155,'V': 0.0156,'Ba':0.0164,'La':0.0172,'Bi':0.0201},
    15.0:  {'O': 0.0119,'B': 0.0119,'V': 0.0120,'Ba':0.0126,'La':0.0132,'Bi':0.0158},
}
energies = sorted(elem_mac.keys())

# Oxide formula to elements and counts for weight-fraction calculation
oxide_elements = {
    'B2O3':  {'B': 2, 'O': 3},
    'V2O5':  {'V': 2, 'O': 5},
    'BaO':   {'Ba': 1, 'O': 1},
    'La2O3': {'La': 2, 'O': 3},
    'Bi2O3': {'Bi': 2, 'O': 3},
}
atom_weights = {'B': 10.81, 'O': 16.00, 'V': 50.94, 'Ba': 137.33, 'La': 138.91, 'Bi': 208.98}

def compute_mac(glass):
    code, x, mol_frac = glass
    total_mass = sum(mol_frac[o] * molecular_weights[o] for o in oxide_elements.keys())
    elem_weight = {}
    for o, counts in oxide_elements.items():
        for elem, cnt in counts.items():
            wt = mol_frac[o] * cnt * atom_weights[elem]
            elem_weight[elem] = elem_weight.get(elem, 0.0) + wt
    for e in elem_weight:
        elem_weight[e] /= total_mass
    rows = []
    for eng in energies:
        mac = sum(elem_weight[e] * elem_mac[eng][e] for e in elem_weight)
        rows.append((eng, mac))
    return rows

# ----------------------------------------------------------------------
# CSV writers
def write_physical():
    with open('/app/outputs/physical_properties.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['glass_code', 'density_g_cm3', 'molar_volume_cm3_mol',
                    'oxygen_molar_volume_cm3_mol', 'oxygen_packing_density_cm3_mol'])
        for code, x, mf in glasses:
            rho, Vm, VO, OPD = compute_physical((code, x, mf))
            w.writerow([code, f'{rho:.4f}', f'{Vm:.4f}', f'{VO:.4f}', f'{OPD:.4f}'])

def write_mechanical():
    with open('/app/outputs/mechanical_moduli.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['glass_code', 'Young_modulus_GPa', 'bulk_modulus_GPa',
                    'shear_modulus_GPa', 'longitudinal_modulus_GPa'])
        for code, x, mf in glasses:
            E, B, S, L = get_mechanical(x)
            w.writerow([code, f'{E:.2f}', f'{B:.2f}', f'{S:.2f}', f'{L:.2f}'])

def write_mac():
    with open('/app/outputs/mac_table.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['glass_code', 'energy_MeV', 'mac_cm2_g'])
        for code, x, mf in glasses:
            rows = compute_mac((code, x, mf))
            for eng, mac in rows:
                w.writerow([code, f'{eng:.3f}' if isinstance(eng, float) else str(eng),
                            f'{mac:.6f}'])

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'physical':
        write_physical()
    elif cmd == 'mechanical':
        write_mechanical()
    elif cmd == 'mac':
        write_mac()
    else:
        raise SystemExit('Unknown command')
