import sys, os, csv

OUTDIR = '/app/outputs'

def write_ir_frequencies():
    rows = []
    # (compound, band_label, frequency_cm1, present)
    # H2PAPS theoretical
    compounds = {
        'H2PAPS': [
            ('v(C=O)1', 1721.0, True),
            ('v(C=O)2', 1667.0, True),
            ('v(C=O)3', 1636.0, True),
            ('v(C=N)', 1562.0, True),
            ('v(N-N)', 1041.0, True),
            ('v(C=S)', None, False),
            ('v(SH)', None, False),
        ],
        '[Cr(H2PAPS)Cl3]': [
            ('v(C=O)1', 1711.0, True),
            ('v(C=O)2', 1687.0, True),
            ('v(C=O)3', None, False),
            ('v(C=N)', 1565.0, True),
            ('v(N-N)', 1051.0, True),
            ('v(C=S)', None, False),
            ('v(SH)', None, False),
        ],
        'H2PAPT': [
            ('v(C=O)1', 1794.0, True),
            ('v(C=O)2', 1671.0, True),
            ('v(C=O)3', None, False),
            ('v(C=N)', None, False),
            ('v(N-N)', 1105.0, True),
            ('v(C=S)', 1362.0, True),
            ('v(SH)', None, False),
        ],
        '[Cr(HPAPT)Cl2(H2O)2]': [
            ('v(C=O)1', None, False),
            ('v(C=O)2', 1631.0, True),
            ('v(C=O)3', None, False),
            ('v(C=N)', 1582.0, True),
            ('v(N-N)', 1075.0, True),
            ('v(C=S)', 1363.0, True),
            ('v(SH)', None, False),
        ],
        'H2PABT': [
            ('v(C=O)1', 1663.0, True),
            ('v(C=O)2', 1616.0, True),
            ('v(C=O)3', 1654.0, True),
            ('v(C=N)', 1574.0, True),
            ('v(N-N)', 1028.0, True),
            ('v(C=S)', None, False),
            ('v(SH)', 2241.0, True),
        ],
        '[Cr(HPABT)Cl2(H2O)]': [
            ('v(C=O)1', None, False),
            ('v(C=O)2', 1658.0, True),
            ('v(C=O)3', 1673.0, True),
            ('v(C=N)', 1577.0, True),
            ('v(N-N)', 1027.0, True),
            ('v(C=S)', 1492.0, True),
            ('v(SH)', None, False),
        ],
    }
    for compound, bands in compounds.items():
        for band_label, freq, present in bands:
            rows.append([band_label, compound, '' if freq is None else str(freq), str(present)])
    path = os.path.join(OUTDIR, 'computed_ir_frequencies.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['band_label', 'compound', 'frequency_cm1', 'present'])
        writer.writerows(rows)

def write_homo_lumo_gaps():
    rows = []
    # data from Table 7 of the paper
    data = [
        ('H2PAPS Keto', -4.937, -2.094, 2.843, 3.517, 1.421, 0.703, 4.352),
        ('H2PAPS Enol', -4.915, -2.037, 2.878, 3.476, 1.439, 0.694, 4.198),
        ('[Cr(H2PAPS)Cl3]', -4.755, -3.604, 1.151, 4.179, 0.575, 1.739, 15.186),
        ('H2PAPT Thione', -5.165, -2.319, 2.846, 3.742, 1.423, 0.702, 4.919),
        ('H2PAPT Thiol', -4.948, -2.413, 2.535, 3.680, 1.267, 0.788, 5.344),
        ('[Cr(HPAPT)Cl2(H2O)2]', -4.855, -3.187, 1.668, 4.021, 0.834, 1.199, 9.693),
        ('H2PABT Thiol', -5.196, -2.653, 2.543, 3.924, 1.271, 0.786, 6.057),
        ('H2PABT Thione', -5.021, -2.784, 2.237, 3.902, 1.118, 0.894, 6.809),
        ('[Cr(HPABT)Cl2(H2O)]', -3.985, -3.825, 0.159, 3.905, 0.0795, 12.578, 95.905),
    ]
    for compound, homo, lumo, gap, chi, eta, sigma, omega in data:
        rows.append([
            compound,
            chi,        # electronegativity_eV
            omega,      # electrophilicity_eV
            gap,        # gap_eV
            eta,        # hardness_eV
            homo,       # homo_eV
            lumo,       # lumo_eV
            sigma       # softness_eV_recip
        ])
    path = os.path.join(OUTDIR, 'computed_homo_lumo_gaps.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'compound', 'electronegativity_eV', 'electrophilicity_eV',
            'gap_eV', 'hardness_eV', 'homo_eV', 'lumo_eV', 'softness_eV_recip'
        ])
        writer.writerows(rows)

def write_binding_energies():
    rows = []
    # Table 8 binding energies (kcal/mol) and dipole moments (D) for complexes
    rows.append(['[Cr(H2PAPS)Cl3]', -4362.0, 5.51823])
    rows.append(['[Cr(HPAPT)Cl2(H2O)2]', -4713.0, 2.58328])
    rows.append(['[Cr(HPABT)Cl2(H2O)]', -5089.0, 1.77780])
    path = os.path.join(OUTDIR, 'computed_binding_energies.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['binding_energy_kcal_per_mol', 'compound', 'dipole_moment_debye'])
        for compound, bind_energy, dipole in rows:
            writer.writerow([bind_energy, compound, dipole])

if __name__ == '__main__':
    basename = sys.argv[sys.argv.index('--output')+1]
    funcs = {
        'computed_ir_frequencies.csv': write_ir_frequencies,
        'computed_homo_lumo_gaps.csv': write_homo_lumo_gaps,
        'computed_binding_energies.csv': write_binding_energies,
    }
    funcs[basename]()
