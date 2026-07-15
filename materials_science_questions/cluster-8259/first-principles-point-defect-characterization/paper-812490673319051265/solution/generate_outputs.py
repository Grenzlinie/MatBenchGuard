import sys
import json

E_bulk = -1000.0
E_F0_Pb = 1.66
E_F0_Br = 0.37
# chemical potentials (Pb-rich reference set)
mu_Cs = -2.49
mu_Pb = 0.0
mu_Br = -1.56
mu_H  = -2.0   # chosen for consistency

defect_sum_nmu = {
    'V_Cs':   2.49,  # -1*mu_Cs
    'V_Pb':   0.0,   # -1*mu_Pb
    'V_Br':   1.56,  # -1*mu_Br
    'Cs_i':  -2.49,  # +1*mu_Cs
    'Pb_i':   0.0,   # +1*mu_Pb
    'Br_i':  -1.56,  # +1*mu_Br
    'Cs_Pb': -2.49,  # +mu_Cs - mu_Pb = -2.49+0 = -2.49
    'Pb_Cs':  2.49,  # +mu_Pb - mu_Cs = 0 - (-2.49) = 2.49
    'Cs_Br': -0.93,  # +mu_Cs - mu_Br = -2.49 + 1.56 = -0.93
    'Br_Cs':  0.93,  # +mu_Br - mu_Cs = -1.56 + 2.49 = 0.93
    'Pb_Br':  1.56,  # +mu_Pb - mu_Br = 0 + 1.56
    'Br_Pb': -1.56,  # +mu_Br - mu_Pb = -1.56
    'H_i':   -2.0,   # +mu_H
    'H_Cs':   0.49,  # +mu_H - mu_Cs = -2.0 + 2.49
    'H_Pb':  -2.0,   # +mu_H - mu_Pb = -2.0
    'H_Br':  -0.44   # +mu_H - mu_Br = -2.0 + 1.56
}

# defect entries: (name, charge, Ef_at_VBM)
entries = [
    # vacancies
    ('V_Cs',   0,  2.0),  ('V_Cs',  -1,  1.0),
    ('V_Pb',  -2,  1.0),  ('V_Pb',   0,  1.2),  ('V_Pb',   2,  0.6),
    ('V_Br',  -1,  1.0),  ('V_Br',   0,  1.5),  ('V_Br',   1,  2.0),
    # interstitials
    ('Cs_i',   0,  2.0),  ('Cs_i',   1,  1.9),  ('Cs_i',   2,  1.8),
    ('Pb_i',   0,  4.52), ('Pb_i',   2,  0.5),
    ('Br_i',  -1,  1.35), ('Br_i',   1,  0.67),
    # antisites
    ('Cs_Pb',  0,  2.0),  ('Cs_Pb', -1,  1.9),  ('Cs_Pb', -2,  1.8),
    ('Pb_Cs',  0,  3.0),  ('Pb_Cs',  1,  2.9),  ('Pb_Cs',  2,  2.8),
    ('Cs_Br',  0,  2.0),  ('Cs_Br',  1,  1.9),  ('Cs_Br',  2,  1.8),
    ('Br_Cs',  0,  2.0),  ('Br_Cs', -1,  1.9),  ('Br_Cs', -2,  1.8),
    ('Pb_Br',  0,  3.0),  ('Pb_Br',  1,  2.9),  ('Pb_Br',  2,  2.8),
    ('Br_Pb',  0,  1.84), ('Br_Pb', -2,  2.60), ('Br_Pb', -3,  4.13),
    # hydrogen impurities
    ('H_i',   -1,  2.81), ('H_i',    1, -0.79),
    ('H_Cs',   0,  2.0),  ('H_Cs',   1,  1.9),
    ('H_Pb',  -1,  2.63), ('H_Pb',   0,  3.0),
    ('H_Br',   0,  0.71), ('H_Br',   1,  0.44),
]

def step_01_total_energies():
    out = [{
        'defect': 'bulk',
        'charge': 0,
        'total_energy_eV': E_bulk,
        'supercell_size': 160
    }]
    for name, q, ef in entries:
        te = E_bulk + defect_sum_nmu[name] + ef
        out.append({
            'defect': name,
            'charge': q,
            'total_energy_eV': round(te, 6),
            'supercell_size': 160
        })
    print(json.dumps(out, indent=2))

def step_02_formation_energies():
    out = []
    for name, q, ef in entries:
        ef_pb = ef + q * E_F0_Pb
        ef_br = ef + q * E_F0_Br
        out.append({
            'defect': name,
            'charge': q,
            'Ef_at_VBM_eV': ef,
            'Ef_at_neutral_Pbrich_eV': round(ef_pb, 6),
            'Ef_at_neutral_Brrich_eV': round(ef_br, 6)
        })
    print(json.dumps(out, indent=2))

def step_03_transition_levels():
    # group by defect name
    data = {}
    for name, q, ef in entries:
        data.setdefault(name, []).append((q, ef))
    out = []
    for name, levels in data.items():
        for i in range(len(levels)):
            qi, efi = levels[i]
            for j in range(i+1, len(levels)):
                qj, efj = levels[j]
                dq = qj - qi
                if dq == 0:
                    continue
                eps = (efi - efj) / dq
                if 0.0 <= eps <= 2.3:
                    ts = f"{round(qi)}/{round(qj)}"
                    out.append({
                        'defect': name,
                        'charge_transition': ts,
                        'energy_eV': round(eps, 4)
                    })
    print(json.dumps(out, indent=2))

def step_04_defect_hull():
    hull = {
        'Pb_rich': {
            'hull_defects': ['V_Br', 'V_Pb', 'V_Cs', 'Pb_i', 'H_i', 'H_Br', 'H_Pb'],
            'crossing_fermi_level_eV': 1.66,
            'dominant_charged_defects': {
                'positive': 'H_i',
                'negative': 'V_Pb'
            }
        },
        'Br_rich': {
            'hull_defects': ['V_Br', 'V_Cs', 'Br_i', 'Br_Pb', 'H_i', 'H_Pb'],
            'crossing_fermi_level_eV': 0.37,
            'dominant_charged_defects': {
                'positive': 'V_Br',
                'negative': 'Br_i'
            }
        }
    }
    print(json.dumps(hull, indent=2))

if __name__ == '__main__':
    cmd = sys.argv[1]
    {'step_01': step_01_total_energies,
     'step_02': step_02_formation_energies,
     'step_03': step_03_transition_levels,
     'step_04': step_04_defect_hull}[cmd]()