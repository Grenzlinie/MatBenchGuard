import math

bridges = {
    'polyacetylene': {'L': 14.3, 'm_eff': 0.455, 'R0': 4.69},
    'polypyrrole': {'L': 41.48, 'm_eff': 0.502, 'R0': 4.69},
    'polythiophene': {'L': 44.64, 'm_eff': 0.446, 'R0': 4.69}
}
m_pa = 0.455; L_pa = 14.3; f0_pa = 0.85
for name, d in bridges.items():
    if name == 'polyacetylene':
        d['f0'] = f0_pa
    else:
        d['f0'] = f0_pa * math.sqrt( (m_pa * L_pa**2) / (d['m_eff'] * d['L']**2) )
radii = [4.69, 7.41, 10.0, 12.0, 14.0]
with open('/app/outputs/ctp_frequencies.csv', 'w') as f:
    f.write('bridge,R_angstrom,frequency_eV\n')
    for name in ['polyacetylene', 'polypyrrole', 'polythiophene']:
        d = bridges[name]
        f0 = d['f0']
        for r in radii:
            freq = f0 * math.sqrt(d['R0'] / r)
            f.write(f'{name},{r},{freq:.6f}\n')
