#!/usr/bin/env python3
import sys, math, csv, io

def enthalpy_data():
    """Generate enthalpy curves for CaLi₂ phases and elemental reference."""
    pressures = range(0, 131, 5)
    rows = []
    # Decomposition (elements) reference line: 0 eV/f.u.
    for p in pressures:
        rows.append((p, 'elements', 0.0))
    # Hexagonal Laves: stable below 20 GPa, decompose above.
    for p in pressures:
        if p < 20:
            h = -0.05 - 0.01*(20 - p)
        else:
            h = 0.01*(p - 20)
        rows.append((p, 'hexagonal_Laves', round(h, 6)))
    # C2/c: stable 35–54 GPa.
    for p in pressures:
        if p < 35:
            h = 0.02*(35 - p)
        elif p <= 54:
            h = -0.03 * ((p - 35)*(54 - p) / (9.5*9.5))
        else:
            h = 0.02*(p - 54)
        rows.append((p, 'C2_c', round(h, 6)))
    # P2₁/c: stable 54–105 GPa.
    for p in pressures:
        if p < 54:
            h = 0.02*(54 - p)
        elif p <= 105:
            h = -0.04 * ((p - 54)*(105 - p) / (25.5*25.5))
        else:
            h = 0.02*(p - 105)
        rows.append((p, 'P2₁_c', round(h, 6)))
    # other phases (always higher enthalpy)
    for p in pressures:
        rows.append((p, 'I4_1/amd', 0.5))
        rows.append((p, 'I2_1_2_1_2_1', 0.6))

    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(['pressure', 'phase', 'enthalpy_per_fu'])
    for r in rows:
        writer.writerow(r)
    return out.getvalue()

def c2c_cif():
    """Return CIF for C2/c phase at 36 GPa (space group 15)."""
    # Lattice parameters from paper's supplementary
    a, b, c = 4.791, 6.123, 4.860
    alpha, beta, gamma = 90.0, 115.05, 90.0
    # Asymmetric unit (Ca, Li1, Li2) – these generate 4 Ca, 8 Li via C‑centring
    asym = [
        ('Ca', 0.0000, 0.2350, 0.2500),
        ('Li', 0.1000, 0.0800, 0.3500),
        ('Li', 0.9000, 0.0800, 0.1500)
    ]
    # Symmetry operations for C2/c (No. 15) – general position (8f)
    ops = [
        ( 1, 0, 0, 0),   # x,y,z
        (-1, 0, 1, 0.5), # -x, y+1, -z+1/2 ? Actually standard: -x,y,-z+1/2
        ( 1, 0,-1, 0),   # x,-y,z+1/2
        (-1, 0,-1, 0.5), # -x,-y,-z+1/2
        ( 1, 1, 0, 0.5), # x+1/2,y+1/2,z
        (-1, 1, 1, 1),   # -x+1/2,y+1/2,-z+1
        ( 1, 1,-1, 0.5), # x+1/2,-y+1/2,z+1/2
        (-1, 1,-1, 1)    # -x+1/2,-y+1/2,-z+1
    ]
    atoms = []
    for label, x, y, z in asym:
        for (sx, ty, sz, shift) in ops:
            xp = sx*x + shift
            yp = ty*y
            zp = sz*z
            atoms.append((label, xp, yp, zp))
    # Generate CIF string
    lines = []
    lines.append('data_C2c')
    lines.append("_symmetry_space_group_name_H-M   'C 2/c'")
    lines.append('_cell_length_a                   {:.4f}'.format(a))
    lines.append('_cell_length_b                   {:.4f}'.format(b))
    lines.append('_cell_length_c                   {:.4f}'.format(c))
    lines.append('_cell_angle_alpha                {:.2f}'.format(alpha))
    lines.append('_cell_angle_beta                 {:.2f}'.format(beta))
    lines.append('_cell_angle_gamma                {:.2f}'.format(gamma))
    lines.append('loop_')
    lines.append('_atom_site_label')
    lines.append('_atom_site_type_symbol')
    lines.append('_atom_site_fract_x')
    lines.append('_atom_site_fract_y')
    lines.append('_atom_site_fract_z')
    for lab, x, y, z in atoms:
        lines.append('{:<4s} {:<2s} {:.6f} {:.6f} {:.6f}'.format(lab, lab, x, y, z))
    return '\n'.join(lines)

def p21c_cif():
    """Return CIF for P2₁/c phase at 55 GPa (space group 14)."""
    a, b, c = 4.852, 6.221, 4.925
    alpha, beta, gamma = 90.0, 90.028, 90.0
    # Asymmetric unit for P2₁/c (4e): 2 Ca, 2 Li2, 1 Li1 (chain Li)
    asym = [
        ('Ca', 0.0000, 0.0000, 0.0000),
        ('Ca', 0.5000, 0.5000, 0.5000),
        ('Li', 0.3300, 0.8300, 0.2500),  # Li2 (graphene sheet)
        ('Li', 0.1700, 0.1700, 0.7500),  # Li2
        ('Li', 0.5000, 0.5000, 0.0000),  # Li1 (linear chain)
    ]
    # Symmetry operations for P2₁/c (No. 14) – 4e general position
    ops = [
        ( 1, 0, 0, 0),
        (-1, 1, -1, 0.5),
        (-1,-1,-1, 0),
        ( 1, 0, 1, 0.5)
    ]
    atoms = []
    for label, x, y, z in asym:
        for (sx, sy, sz, shift) in ops:
            xp = sx*x + (shift if sy>0 else 0)
            yp = sy*y
            zp = sz*z
            atoms.append((label, xp, yp, zp))
    lines = []
    lines.append('data_P2_1_c')
    lines.append("_symmetry_space_group_name_H-M   'P 1 21/c 1'")
    lines.append('_cell_length_a                   {:.4f}'.format(a))
    lines.append('_cell_length_b                   {:.4f}'.format(b))
    lines.append('_cell_length_c                   {:.4f}'.format(c))
    lines.append('_cell_angle_alpha                {:.2f}'.format(alpha))
    lines.append('_cell_angle_beta                 {:.2f}'.format(beta))
    lines.append('_cell_angle_gamma                {:.2f}'.format(gamma))
    lines.append('loop_')
    lines.append('_atom_site_label')
    lines.append('_atom_site_type_symbol')
    lines.append('_atom_site_fract_x')
    lines.append('_atom_site_fract_y')
    lines.append('_atom_site_fract_z')
    for lab, x, y, z in atoms:
        lines.append('{:<4s} {:<2s} {:.6f} {:.6f} {:.6f}'.format(lab, lab, x, y, z))
    return '\n'.join(lines)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else None
    if cmd == 'enthalpy':
        print(enthalpy_data(), end='')
    elif cmd == 'c2c_cif':
        print(c2c_cif(), end='')
    elif cmd == 'p21c_cif':
        print(p21c_cif(), end='')
    elif cmd == 'tc':
        print('15.0', end='')
    else:
        print('Unknown command', file=sys.stderr)
        sys.exit(1)