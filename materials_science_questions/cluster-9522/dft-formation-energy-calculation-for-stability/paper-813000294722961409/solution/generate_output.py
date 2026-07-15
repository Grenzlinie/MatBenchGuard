import json
import sys
import os

# Helper to map coordinates to [0,1)
def wrap(x):
    return x - int(x)

# O-phase (Cmcm) atomic positions
def gen_o_phase(a, b, c, Ti_x, Ti_y, Al_y, Nb_y):
    atoms = []
    # Ti: 8g site (x, y, 0.25) with centering (0,0,0) and (0.5,0.5,0)
    ti_base = [
        (Ti_x, Ti_y, 0.25),
        (-Ti_x, -Ti_y, 0.75),
        (-Ti_x, Ti_y, 0.75),
        (Ti_x, -Ti_y, 0.25)
    ]
    for (x, y, z) in ti_base:
        for ox, oy, oz in [(0,0,0), (0.5,0.5,0)]:
            atoms.append({
                'element': 'Ti',
                'fractional_coordinates': [wrap(x+ox), wrap(y+oy), wrap(z+oz)]
            })
    # Al: 4c (0, y, 0.25) with centering
    al_base = [
        (0.0, Al_y, 0.25),
        (0.0, -Al_y, 0.75)
    ]
    for (x, y, z) in al_base:
        for ox, oy, oz in [(0,0,0), (0.5,0.5,0)]:
            atoms.append({
                'element': 'Al',
                'fractional_coordinates': [wrap(x+ox), wrap(y+oy), wrap(z+oz)]
            })
    # Nb: 4c (0, y, 0.25) with centering
    nb_base = [
        (0.0, Nb_y, 0.25),
        (0.0, -Nb_y, 0.75)
    ]
    for (x, y, z) in nb_base:
        for ox, oy, oz in [(0,0,0), (0.5,0.5,0)]:
            atoms.append({
                'element': 'Nb',
                'fractional_coordinates': [wrap(x+ox), wrap(y+oy), wrap(z+oz)]
            })
    return atoms

# Heusler Fm-3m
def gen_heusler(a, ti_coord, al_coord, nb_coord):
    atoms = []
    # F-centering translations
    centering = [(0,0,0), (0,0.5,0.5), (0.5,0,0.5), (0.5,0.5,0)]
    # Ti on 8c (multiplicity 8): coordinates (1/4,1/4,1/4) and (3/4,3/4,3/4)
    ti_sites = [(0.25,0.25,0.25), (0.75,0.75,0.75)]
    for (x,y,z) in ti_sites:
        for dx,dy,dz in centering:
            atoms.append({
                'element': 'Ti',
                'fractional_coordinates': [wrap(x+dx), wrap(y+dy), wrap(z+dz)]
            })
    # Al 4a (0,0,0)
    for dx,dy,dz in centering:
        atoms.append({
            'element': 'Al',
            'fractional_coordinates': [wrap(dx), wrap(dy), wrap(dz)]
            })
    # Nb 4b (0.5,0.5,0.5)
    for dx,dy,dz in centering:
        atoms.append({
            'element': 'Nb',
            'fractional_coordinates': [wrap(0.5+dx), wrap(0.5+dy), wrap(0.5+dz)]
            })
    return atoms

def main():
    out_path = sys.argv[1]

    # Data from Table 2 and Table 3
    entries = []

    # O-phase parameters for each functional
    o_params = {
        'LDA': {'a':5.94, 'b':9.31, 'c':4.56, 'Ti_x':0.2371, 'Ti_y':0.9013, 'Al_y':0.1608, 'Nb_y':0.6390, 'E': -1992.6374},
        'PBE': {'a':6.04, 'b':9.49, 'c':4.65, 'Ti_x':0.2368, 'Ti_y':0.9026, 'Al_y':0.1623, 'Nb_y':0.6396, 'E': -1997.2125},
        'B3LYP': {'a':6.05, 'b':9.55, 'c':4.66, 'Ti_x':0.2344, 'Ti_y':0.9067, 'Al_y':0.1647, 'Nb_y':0.6409, 'E': -1997.4068}
    }

    # Heusler parameters
    h_params = {
        'LDA': {'a':6.310, 'E_H1': -1992.6314, 'E_H2': -1992.6314},
        'PBE': {'a':6.4322, 'E_H1': -1997.2054, 'E_H2': -1997.2054},
        'B3LYP': {'a':6.44, 'E_H1': -1997.3976, 'E_H2': -1997.3976}
    }

    # O-phase entries
    for func, p in o_params.items():
        atoms = gen_o_phase(p['a'], p['b'], p['c'], p['Ti_x'], p['Ti_y'], p['Al_y'], p['Nb_y'])
        entries.append({
            'structure_id': 'O',
            'functional': func,
            'lattice_parameters_angstrom': {'a': p['a'], 'b': p['b'], 'c': p['c']},
            'atomic_positions': atoms,
            'total_energy_per_fu': p['E'],
            'energy_unit': 'Hartree'
        })

    # H1 and H2 entries
    # H1: Ti at 8c, Al at 4a, Nb at 4b
    # H2: same lattice, swap Al<->Nb
    for func, hp in h_params.items():
        a = hp['a']
        # H1
        atoms_h1 = gen_heusler(a, ti_coord=None, al_coord=None, nb_coord=None) # positions as per standard
        # Actually the function uses fixed positions, so fine
        entries.append({
            'structure_id': 'H1',
            'functional': func,
            'lattice_parameters_angstrom': {'a': a, 'b': a, 'c': a},
            'atomic_positions': atoms_h1,
            'total_energy_per_fu': hp['E_H1'],
            'energy_unit': 'Hartree'
        })
        # H2: identical coordinates, just swap element labels? Actually H2 is obtained by swapping Al and Nb.
        # So we generate atoms with Ti same, but Al and Nb positions swapped.
        # We'll define a helper that swaps.
        atoms_h2 = []
        for atom in atoms_h1:
            if atom['element'] == 'Al':
                atoms_h2.append({'element': 'Nb', 'fractional_coordinates': atom['fractional_coordinates']})
            elif atom['element'] == 'Nb':
                atoms_h2.append({'element': 'Al', 'fractional_coordinates': atom['fractional_coordinates']})
            else:
                atoms_h2.append(atom)
        entries.append({
            'structure_id': 'H2',
            'functional': func,
            'lattice_parameters_angstrom': {'a': a, 'b': a, 'c': a},
            'atomic_positions': atoms_h2,
            'total_energy_per_fu': hp['E_H2'],
            'energy_unit': 'Hartree'
        })

    with open(out_path, 'w') as f:
        json.dump(entries, f, indent=2)

if __name__ == '__main__':
    main()
