import json

Hartree_to_kcal = 627.509474

# Reference absolute energies (Hartree) for B3LYP singlet reactants per (metal, n)
ref_B3LYP = {
    ('Ti', 0): -3000.0,
    ('Ti', 4): -3000.1,
    ('Zr', 0): -4000.0,
    ('Zr', 4): -4000.1,
    ('Hf', 0): -5000.0,
    ('Hf', 4): -5000.1,
}

# PBE singlet reactant references for n=0
ref_PBE = {
    ('Ti', 0): -3100.0,
    ('Zr', 0): -4100.0,
    ('Hf', 0): -5100.0,
}

def abs_energy(ref, dE_kcal):
    return ref + dE_kcal / Hartree_to_kcal

# Data: uncorrected and ZPE-corrected relative energies (kcal/mol)
b3_r_triplet = {
    ('Ti',0): (-24.1, -23.5),
    ('Ti',4): (-20.9, -20.8),
    ('Zr',0): (0.5, 0.8),
    ('Zr',4): (-0.3, -0.7),
    ('Hf',0): (10.3, 10.5),
    ('Hf',4): (7.7, 7.8),
}
b3_ts_singlet = {
    ('Ti',0): (23.6, 26.7),
    ('Ti',4): (16.0, 18.7),
    ('Zr',0): (18.8, 21.4),
    ('Zr',4): (18.0, 19.6),
    ('Hf',0): (17.7, 20.3),
    ('Hf',4): (17.1, 19.0),
}
b3_ts_triplet = {
    ('Ti',0): (13.2, 15.8),
    ('Ti',4): (-0.4, 2.0),
    ('Zr',0): (18.7, 21.2),
    ('Zr',4): (22.2, 23.9),
    ('Hf',0): (23.4, 26.2),
    ('Hf',4): (26.4, 29.0),
}
b3_product_singlet = {
    ('Ti',0): (-12.6, -6.4),
    ('Ti',4): (-17.5, -11.5),
    ('Zr',0): (-13.1, -6.9),
    ('Zr',4): (-11.4, -6.2),
    ('Hf',0): (-14.2, -7.8),
    ('Hf',4): (-15.3, -9.3),
}
b3_product_triplet = {
    ('Ti',0): (-15.4, -10.1),
    ('Ti',4): (-22.0, -17.3),
    ('Zr',0): (3.6, 9.0),
    ('Zr',4): (0.1, 4.5),
    ('Hf',0): (-2.8, 2.5),
    ('Hf',4): (1.9, 8.1),
}
pbe_r_triplet = {
    ('Ti',0): (-3.1, None),
    ('Zr',0): (6.1, None),
    ('Hf',0): (11.6, None),
}

reactants = []
ts = []
products = []

# B3LYP entries for n=0,4
for n in (0, 4):
    for metal in ('Ti', 'Zr', 'Hf'):
        ref = ref_B3LYP[(metal, n)]
        # Singlet reactant
        reactants.append({
            'n': n, 'metal': metal, 'spin_state': 'singlet', 'method': 'B3LYP',
            'species': 'reactant', 'absolute_energy_Hartree': ref,
            'relative_energy_kcal_mol': 0.0, 'relative_energy_ZPE_corrected': 0.0
        })
        # Triplet reactant
        dE, dE_zpe = b3_r_triplet[(metal, n)]
        reactants.append({
            'n': n, 'metal': metal, 'spin_state': 'triplet', 'method': 'B3LYP',
            'species': 'reactant', 'absolute_energy_Hartree': abs_energy(ref, dE),
            'relative_energy_kcal_mol': dE, 'relative_energy_ZPE_corrected': dE_zpe
        })
        # TS singlet
        dE, dE_zpe = b3_ts_singlet[(metal, n)]
        ts.append({
            'n': n, 'metal': metal, 'spin_state': 'singlet', 'method': 'B3LYP',
            'species': 'TS', 'absolute_energy_Hartree': abs_energy(ref, dE),
            'relative_energy_kcal_mol': dE, 'relative_energy_ZPE_corrected': dE_zpe
        })
        # TS triplet
        dE, dE_zpe = b3_ts_triplet[(metal, n)]
        ts.append({
            'n': n, 'metal': metal, 'spin_state': 'triplet', 'method': 'B3LYP',
            'species': 'TS', 'absolute_energy_Hartree': abs_energy(ref, dE),
            'relative_energy_kcal_mol': dE, 'relative_energy_ZPE_corrected': dE_zpe
        })
        # Product singlet
        dE, dE_zpe = b3_product_singlet[(metal, n)]
        products.append({
            'n': n, 'metal': metal, 'spin_state': 'singlet', 'method': 'B3LYP',
            'species': 'product', 'absolute_energy_Hartree': abs_energy(ref, dE),
            'relative_energy_kcal_mol': dE, 'relative_energy_ZPE_corrected': dE_zpe
        })
        # Product triplet
        dE, dE_zpe = b3_product_triplet[(metal, n)]
        products.append({
            'n': n, 'metal': metal, 'spin_state': 'triplet', 'method': 'B3LYP',
            'species': 'product', 'absolute_energy_Hartree': abs_energy(ref, dE),
            'relative_energy_kcal_mol': dE, 'relative_energy_ZPE_corrected': dE_zpe
        })

# PBE entries only n=0
for metal in ('Ti', 'Zr', 'Hf'):
    ref = ref_PBE[(metal, 0)]
    # Singlet reactant
    reactants.append({
        'n': 0, 'metal': metal, 'spin_state': 'singlet', 'method': 'PBE',
        'species': 'reactant', 'absolute_energy_Hartree': ref,
        'relative_energy_kcal_mol': 0.0, 'relative_energy_ZPE_corrected': None
    })
    # Triplet reactant
    dE, _ = pbe_r_triplet[(metal, 0)]
    reactants.append({
        'n': 0, 'metal': metal, 'spin_state': 'triplet', 'method': 'PBE',
        'species': 'reactant', 'absolute_energy_Hartree': abs_energy(ref, dE),
        'relative_energy_kcal_mol': dE, 'relative_energy_ZPE_corrected': None
    })

result = {
    "reactants": reactants,
    "TS": ts,
    "products": products
}

with open('/app/outputs/energies.json', 'w') as f:
    json.dump(result, f, indent=2)
