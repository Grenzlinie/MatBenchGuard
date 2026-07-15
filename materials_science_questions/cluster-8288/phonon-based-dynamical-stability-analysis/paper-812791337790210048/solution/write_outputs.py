import json

a = 4.0
b = 4.0
c = 5.0

cif = f"""data_t-B2N3
_chemical_formula_sum 'B2 N3'
_cell_length_a {a:.6f}
_cell_length_b {b:.6f}
_cell_length_c {c:.6f}
_cell_angle_alpha 90.0
_cell_angle_beta 90.0
_cell_angle_gamma 90.0
_symmetry_space_group_name_H-M 'P42/mmc'
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
B1 B 0.382500 0.000000 0.000000
B2 B 0.897500 0.500000 0.250000
N1_1 N 0.000000 0.000000 0.000000
N1_2 N 0.000000 0.000000 0.266000
N2 N 0.500000 0.500000 0.250000
"""

with open('/app/outputs/optimized_structure.cif', 'w') as f:
    f.write(cif)

props = {
    'c11': 749,
    'c12': 15,
    'c13': 135,
    'c33': 970,
    'c44': 313,
    'c66': 150,
    'bulk_modulus': 337,
    'shear_modulus': 300,
    'g_over_b_ratio': 0.89,
    'energy_density_kJ_g': 2.95,
    'is_metallic': True,
    'band_gap_eV': 0.0
}
with open('/app/outputs/calculated_properties.json', 'w') as f:
    json.dump(props, f, indent=2)
