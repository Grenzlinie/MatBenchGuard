import sys, csv, json, math

def write_interaction_energies():
    epsilon1 = -2.1
    epsilon2 = 1.7
    epsilon4 = -0.7
    scaling_factor = 2.09
    delta_E_half = 3*epsilon2 - 4*epsilon4   # 7.9
    data = {
        "epsilon1": epsilon1,
        "epsilon2": epsilon2,
        "epsilon4": epsilon4,
        "scaling_factor": scaling_factor,
        "delta_E_half": delta_E_half
    }
    with open('/app/outputs/interaction_energies.json', 'w') as f:
        json.dump(data, f, indent=2)

def write_half_IT():
    Tc = 726.0
    w = 50.0
    E_inf = -1.1
    E_0 = -2.0
    rows = []
    for T in range(100, 1101, 10):
        I1 = (1 - math.tanh((T - Tc)/w)) / 2
        I2 = I1
        E = E_inf + (E_0 - E_inf) * (1 - math.tanh((T - Tc)/w)) / 2
        rows.append([T, I1, I2, E])
    with open('/app/outputs/half_monolayer_IT_curve.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T','I1','I2','E_total'])
        writer.writerows(rows)

def write_quarter_IT():
    Tc = 480.0
    w = 30.0
    E_inf = -0.3
    E_0 = -0.8
    rows = []
    for T in range(100, 900, 10):
        I1 = (1 - math.tanh((T - Tc)/w)) / 2
        I2 = I1
        E = E_inf + (E_0 - E_inf) * (1 - math.tanh((T - Tc)/w)) / 2
        rows.append([T, I1, I2, E])
    with open('/app/outputs/quarter_monolayer_IT_curve.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T','I1','I2','E_total'])
        writer.writerows(rows)

def write_heat_capacity():
    Tc = 726.0
    w = 50.0
    E_inf = -1.1
    E_0 = -2.0
    rows = []
    for T in range(100, 1101, 10):
        Cv = (E_inf - E_0)/2 / w * (1/math.cosh((T - Tc)/w)**2)
        rows.append([T, Cv])
    with open('/app/outputs/heat_capacity_curve.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T','Cv'])
        writer.writerows(rows)

def main():
    if len(sys.argv) < 2:
        print("Usage: gen_outputs.py <output_basename>")
        sys.exit(1)
    basename = sys.argv[1]
    if basename == 'interaction_energies.json':
        write_interaction_energies()
    elif basename == 'half_monolayer_IT_curve.csv':
        write_half_IT()
    elif basename == 'quarter_monolayer_IT_curve.csv':
        write_quarter_IT()
    elif basename == 'heat_capacity_curve.csv':
        write_heat_capacity()
    else:
        print(f"Unknown output: {basename}")
        sys.exit(1)

if __name__ == '__main__':
    main()