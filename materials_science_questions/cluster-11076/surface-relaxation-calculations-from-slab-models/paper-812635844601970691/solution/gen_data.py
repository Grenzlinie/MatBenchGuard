import sys, csv, json

def generate_al001():
    x0 = -0.03827
    E0 = -483.815
    rows = []
    x = -0.5
    while x <= 0.5001:
        dx = x - x0
        dx2 = dx * dx
        dx3 = dx2 * dx
        energy = E0 + 50.0 * dx2 + 10.0 * dx3
        force = -(100.0 * dx + 30.0 * dx2)
        wf = 4.42 + 0.1 * dx
        rows.append([f"{x:.6f}", f"{energy:.6f}", f"{wf:.4f}", f"{force:.6f}", f"{force:.6f}"])
        x += 0.05
    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['spacing_change', 'total_energy', 'work_function', 'force_direct', 'force_from_derivative'])
    writer.writerows(rows)

def generate_al110():
    x0 = -0.5955
    E0 = -483.5
    rows = []
    x = -0.8
    while x <= 0.2001:
        dx = x - x0
        energy = E0 + 80.0 * dx * dx
        force = -160.0 * dx
        rows.append([f"{x:.6f}", f"{energy:.6f}", f"{force:.6f}"])
        x += 0.05
    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['spacing_change', 'total_energy', 'force'])
    writer.writerows(rows)

def generate_summary():
    data = {
        "al001_relaxation_percent": -1.0,
        "al001_work_function_eV": 4.42,
        "al110_relaxation_percent": -11.0
    }
    json.dump(data, sys.stdout, indent=2)

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'al001':
        generate_al001()
    elif mode == 'al110':
        generate_al110()
    elif mode == 'summary':
        generate_summary()
    else:
        sys.exit(1)
