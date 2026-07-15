import csv, json, sys, os

def tetranuclear_energy(S_T, S_A, S_B, J_wb, J_bb):
    return -J_wb * (S_T*(S_T+1) - S_A*(S_A+1) - S_B*(S_B+1)) - J_bb * S_A*(S_A+1)

def tetranuclear_ground_state(J_wb, J_bb):
    states = []
    for S_A in range(5):
        for S_B in range(5):
            for S_T in range(abs(S_A-S_B), S_A+S_B+1):
                e = tetranuclear_energy(S_T, S_A, S_B, J_wb, J_bb)
                states.append((e, S_T, S_A, S_B))
    states.sort(key=lambda x: x[0])
    return states[0][1:]

def triangle_energy(S_T, S_bc, J, J_star):
    return -J * (S_T*(S_T+1) - S_bc*(S_bc+1)) - J_star * S_bc*(S_bc+1)

def triangle_ground_state(J, J_star):
    S_a = 2
    states = []
    for S_bc in range(5):
        for S_T in range(abs(S_bc-S_a), S_bc+S_a+1):
            e = triangle_energy(S_T, S_bc, J, J_star)
            states.append((e, S_T, S_bc))
    states.sort(key=lambda x: x[0])
    return states[0][1:]

target = sys.argv[1]
outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)

if target == 'ground_state_complex1.json':
    J_wb = -5.3
    J_bb = -24.6
    S_T, S_A, S_B = tetranuclear_ground_state(J_wb, J_bb)
    data = {'S_T': S_T, 'S_A': S_A, 'S_B': S_B}
    with open(os.path.join(outdir, target), 'w') as f:
        json.dump(data, f)

elif target == 'triangle_ground_states.csv':
    npoints = 200
    ratios = [10**(-2 + 4*i/(npoints-1)) for i in range(npoints)]
    rows = [['ratio', 'S_T', 'S_bc', 'energy']]
    J_star = -1.0
    for r in ratios:
        J = -r
        S_T, S_bc = triangle_ground_state(J, J_star)
        energy = triangle_energy(S_T, S_bc, J, J_star)
        rows.append([f'{r:.6f}', str(S_T), str(S_bc), f'{energy:.6f}'])
    with open(os.path.join(outdir, target), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

elif target == 'tetranuclear_ground_states.csv':
    jvals = list(range(-30, 0, 1))
    rows = [['J_wb', 'J_bb', 'S_T', 'S_A', 'S_B']]
    for J_wb in jvals:
        for J_bb in jvals:
            S_T, S_A, S_B = tetranuclear_ground_state(J_wb, J_bb)
            rows.append([str(J_wb), str(J_bb), str(S_T), str(S_A), str(S_B)])
    with open(os.path.join(outdir, target), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

else:
    raise ValueError('Unknown target')