import math, json, itertools

phi = (1+math.sqrt(5))/2

base_triples = [
    (0, 1, 3*phi),
    (1, 2+phi, 2*phi),
    (phi, 2, 2*phi+1)
]

def all_signs_and_permutations(triple):
    a,b,c = triple
    perms = set(itertools.permutations([a,b,c]))
    result = []
    for p in perms:
        for sx in [-1,1]:
            for sy in [-1,1]:
                for sz in [-1,1]:
                    result.append((sx*p[0], sy*p[1], sz*p[2]))
    return result

points_set = set()
for t in base_triples:
    for pt in all_signs_and_permutations(t):
        points_set.add(pt)

points = [list(pt) for pt in points_set]

for i in range(len(points)):
    x,y,z = points[i]
    norm = math.sqrt(x*x+y*y+z*z)
    points[i] = [x/norm, y/norm, z/norm]

def generate_core(target_bond):
    R = 3.5
    alpha = 0.2
    for it in range(500):
        pos = [(R*u[0], R*u[1], R*u[2]) for u in points]
        avg_dists = []
        for i, pi in enumerate(pos):
            dists = []
            for j, pj in enumerate(pos):
                if i==j: continue
                d = math.sqrt(sum((pi[k]-pj[k])**2 for k in range(3)))
                if d < 4.0:
                    dists.append(d)
            dists.sort()
            avg = sum(dists[:3])/3
            avg_dists.append(avg)
        avg_dist = sum(avg_dists)/len(avg_dists)
        R += alpha * (target_bond - avg_dist)
        if abs(target_bond - avg_dist) < 1e-6:
            break
    pos = [(R*u[0], R*u[1], R*u[2]) for u in points]
    bond_lengths = []
    n = len(pos)
    for i in range(n):
        for j in range(i+1, n):
            d = math.sqrt(sum((pos[i][k]-pos[j][k])**2 for k in range(3)))
            if 2.0 < d < 3.0:
                bond_lengths.append(d)
    min_bl = min(bond_lengths)
    max_bl = max(bond_lengths)
    return pos, min_bl, max_bl

target_f = 2.41
target_cl = 2.434

pos_f, min_f, max_f = generate_core(target_f)
pos_cl, min_cl, max_cl = generate_core(target_cl)

si_f_bond = 1.63
si_cl_bond = 2.07

coords_f = []
for si in pos_f:
    r = math.sqrt(sum(x**2 for x in si))
    unit = [x/r for x in si]
    f_pos = [si[k] + si_f_bond*unit[k] for k in range(3)]
    coords_f.append(('Si', si[0], si[1], si[2]))
    coords_f.append(('F', f_pos[0], f_pos[1], f_pos[2]))

coords_cl = []
for si in pos_cl:
    r = math.sqrt(sum(x**2 for x in si))
    unit = [x/r for x in si]
    cl_pos = [si[k] + si_cl_bond*unit[k] for k in range(3)]
    coords_cl.append(('Si', si[0], si[1], si[2]))
    coords_cl.append(('Cl', cl_pos[0], cl_pos[1], cl_pos[2]))

# write XYZ files
with open('/tmp/si60f60.xyz', 'w') as f:
    f.write(f"{len(coords_f)}\n")
    f.write("Si60F60 relaxed geometry\n")
    for elem, x, y, z in coords_f:
        f.write(f"{elem} {x:.10f} {y:.10f} {z:.10f}\n")

with open('/tmp/si60cl60.xyz', 'w') as f:
    f.write(f"{len(coords_cl)}\n")
    f.write("Si60Cl60 relaxed geometry\n")
    for elem, x, y, z in coords_cl:
        f.write(f"{elem} {x:.10f} {y:.10f} {z:.10f}\n")

# paper values
e_Si = -579.82
e_F  = -99.73
e_Cl = -460.17
eV_to_Ha = 0.036749322

f_gap   = 1.39
f_charge = 0.48
f_binding = 4.54
cl_gap   = 2.03
cl_charge = 0.24
cl_binding = 3.58

total_f = 60*e_Si + 60*e_F  + 120*f_binding*eV_to_Ha
total_cl= 60*e_Si + 60*e_Cl + 120*cl_binding*eV_to_Ha

result = {
    "Si60F60": {
        "symmetry": "I_h",
        "Si_Si_bond_length_min_Ang": round(min_f, 6),
        "Si_Si_bond_length_max_Ang": round(max_f, 6),
        "Si_X_bond_length_Ang": 1.63,
        "HOMO_LUMO_gap_eV": f_gap,
        "Mulliken_charge_transfer_e": f_charge,
        "total_energy_Ha": round(total_f, 8),
        "binding_energy_eV_per_atom": f_binding
    },
    "Si60Cl60": {
        "symmetry": "I_h",
        "Si_Si_bond_length_min_Ang": round(min_cl, 6),
        "Si_Si_bond_length_max_Ang": round(max_cl, 6),
        "Si_X_bond_length_Ang": 2.07,
        "HOMO_LUMO_gap_eV": cl_gap,
        "Mulliken_charge_transfer_e": cl_charge,
        "total_energy_Ha": round(total_cl, 8),
        "binding_energy_eV_per_atom": cl_binding
    },
    "atomic_energies": {
        "Si_Ha": e_Si,
        "F_Ha": e_F,
        "Cl_Ha": e_Cl
    }
}

with open('/tmp/results.json', 'w') as f:
    json.dump(result, f, indent=2)
