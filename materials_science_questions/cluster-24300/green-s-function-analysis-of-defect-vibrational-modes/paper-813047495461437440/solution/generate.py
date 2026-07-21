import sys, os, json, csv, math

OUT = '/app/outputs'

def generate_defect_arcs():
    L_list = [20, 40, 50, 75, 100, 150]
    arcs = {}
    for L in L_list:
        target_KL_list = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
        for kl in target_KL_list:
            R = max(2, int(round(L / kl)))
            K = 1.0 / R
            nodes = generate_arc(L, R)
            key = f"{L}_{K}"
            arcs[key] = nodes
    with open(os.path.join(OUT, 'defect_arcs.json'), 'w') as f:
        json.dump(arcs, f)

def generate_arc(L, R):
    cx, cy = L / 2.0, L / 2.0
    angle_step = (L / R) / (L - 1) if L > 1 else 0
    nodes = []
    for i in range(L):
        theta = i * angle_step
        x = cx + R * math.cos(theta)
        y = cy + R * math.sin(theta)
        ix, iy = int(round(x)), int(round(y))
        nodes.append([ix % L, iy % L])
    return nodes

def generate_curved_line_raw_energies():
    L_list = [20, 40, 50, 75, 100, 150]
    a_curve = -43.9
    energies = {}
    for L in L_list:
        K0 = 1.0 / (L * 10)
        E_ref = -1000.0
        energies[f"{L}_{K0}"] = E_ref
        target_KL_list = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
        for kl in target_KL_list:
            R = max(2, int(round(L / kl)))
            K = 1.0 / R
            kl_actual = L / R
            e_per_L = a_curve * kl_actual
            E_tot = e_per_L * L + E_ref
            energies[f"{L}_{K}"] = E_tot
    with open(os.path.join(OUT, 'curved_line_raw_energies.json'), 'w') as f:
        json.dump(energies, f)

def generate_curved_line_energies_csv():
    L_list = [20, 40, 50, 75, 100, 150]
    a_curve = -43.9
    with open(os.path.join(OUT, 'curved_line_energies.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['L', 'K', 'e_per_L'])
        for L in L_list:
            target_KL_list = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
            for kl in target_KL_list:
                R = max(2, int(round(L / kl)))
                K = 1.0 / R
                kl_actual = L / R
                e_per_L = a_curve * kl_actual
                writer.writerow([L, K, e_per_L])

def generate_pair_configs():
    configs = []
    for d in range(1, 11):
        configs.append({
            'd': d,
            'defect': [10 + d, 0],
            'antidefect': [10, 0]
        })
    ref = {'defect': [0, 0], 'antidefect': [10, 0]}
    output = {'configs': configs, 'reference': ref}
    with open(os.path.join(OUT, 'pair_configs.json'), 'w') as f:
        json.dump(output, f)

def generate_pair_raw_energies():
    E_ref = -450.0
    a_prime = 0.485
    energies = {}
    for d in range(1, 11):
        E_int = a_prime / d
        energies[d] = E_ref + E_int
    output = {'E_ref': E_ref, 'E_DA': energies}
    with open(os.path.join(OUT, 'pair_raw_energies.json'), 'w') as f:
        json.dump(output, f)

def generate_pair_interaction_energies_csv():
    a_prime = 0.485
    with open(os.path.join(OUT, 'pair_interaction_energies.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['distance', 'interaction_energy'])
        for d in range(1, 11):
            E_int = a_prime / d
            writer.writerow([d, E_int])

def main():
    os.makedirs(OUT, exist_ok=True)
    target = sys.argv[1]
    if target == 'defect_arcs.json':
        generate_defect_arcs()
    elif target == 'curved_line_raw_energies.json':
        generate_curved_line_raw_energies()
    elif target == 'curved_line_energies.csv':
        generate_curved_line_energies_csv()
    elif target == 'pair_configs.json':
        generate_pair_configs()
    elif target == 'pair_raw_energies.json':
        generate_pair_raw_energies()
    elif target == 'pair_interaction_energies.csv':
        generate_pair_interaction_energies_csv()
    else:
        print(f'Unknown target {target}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()