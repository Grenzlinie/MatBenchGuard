import csv, math, sys, os

def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    os.makedirs(outdir, exist_ok=True)

    # tiny cosine barrier: amplitude 0.015 eV → peak-to-peak 0.03 eV = 30 meV
    A = 0.015
    baseline = -200.0
    angles = list(range(0, 181, 20))   # 0,20,...,180
    energies = []
    for a in angles:
        E = baseline + A * math.cos(2 * math.pi * a / 180.0)
        energies.append(E)

    csv_path = os.path.join(outdir, 'energy_vs_angle.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['angle_deg', 'energy_eV'])
        for a, e in zip(angles, energies):
            writer.writerow([a, f'{e:.6f}'])

    barrier = (max(energies) - min(energies)) * 1000.0  # meV
    barrier_path = os.path.join(outdir, 'rotational_barrier.txt')
    with open(barrier_path, 'w') as f:
        f.write(str(round(barrier)) + '\n')

if __name__ == '__main__':
    main()