#!/usr/bin/env python3
import sys, os, json, csv, random, math

OUTDIR = '/app/outputs'

def generate_shape_factor(output_path):
    random.seed(42)
    taps = [2,8,15,30,50,70]
    ordered_prob = {2:0.05, 8:0.08, 15:0.2, 30:0.35, 50:0.5, 70:0.7}
    data = {}
    for tap in taps:
        cells = []
        n_cells = 800
        prob = ordered_prob[tap]
        for _ in range(n_cells):
            if random.random() < prob:
                z = 1.103 + random.gauss(0, 0.0015)
                z = max(1.102, min(1.108, z))
            else:
                mean_dis = {2:1.24,8:1.22,15:1.20,30:1.18,50:1.16,70:1.14}[tap]
                sigma = 0.04
                z = random.gauss(mean_dis, sigma)
                z = max(1.10, z)
            cells.append(round(z, 6))
        random.shuffle(cells)
        data[str(tap)] = cells
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(data, f)

def generate_memory_effect(output_path):
    random.seed(43)
    taps_total = 56
    rows = []
    # scenario 0: 3% -> 0.5%
    for t in range(taps_total):
        if t <= 30:
            rho = 0.78 + 0.048 * (t / 30.0) + random.gauss(0, 0.0015)
        else:
            if t == 31:
                rho = 0.820 + random.gauss(0, 0.0015)
            else:
                offset = t - 31
                rho = 0.820 + 0.015 * (1 - math.exp(-0.15 * offset)) + random.gauss(0, 0.0015)
        rho = round(max(0.75, min(0.85, rho)), 6)
        rows.append([0, t, rho])
    # scenario 1: 0.5% -> 3%
    for t in range(taps_total):
        if t <= 30:
            rho = 0.78 + 0.015 * (t / 30.0) + random.gauss(0, 0.0015)
        else:
            if t == 31:
                rho = 0.805 + random.gauss(0, 0.0015)
            else:
                offset = t - 31
                if t <= 35:
                    rho = 0.805 - 0.002 * offset + random.gauss(0, 0.002)
                else:
                    rho = 0.805 - 0.005 + 0.001 * (offset - 5) + random.gauss(0, 0.002)
        rho = round(max(0.75, min(0.85, rho)), 6)
        rows.append([1, t, rho])
    # enforce exact base points
    for row in rows:
        if row[0]==0 and row[1]==30:
            row[2] = 0.828
        if row[0]==1 and row[1]==30:
            row[2] = 0.795
        if row[0]==0 and row[1]==31:
            row[2] = 0.820
        if row[0]==1 and row[1]==31:
            row[2] = 0.805
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['scenario','tap','density'])
        for row in rows:
            writer.writerow(row)

if __name__ == '__main__':
    target = sys.argv[1]
    if target == 'shape_factor_cells.json':
        generate_shape_factor(os.path.join(OUTDIR, 'shape_factor_cells.json'))
    elif target == 'memory_effect.csv':
        generate_memory_effect(os.path.join(OUTDIR, 'memory_effect.csv'))
    else:
        sys.exit(1)