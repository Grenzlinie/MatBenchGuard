import csv, math, sys

def main(outpath):
    zs = [i*0.05 for i in range(0, 201)]   # 0..10 Å
    rows = []
    for z in zs:
        dens = 1.0
        # Peak 1: 2.25 Å, height 12 (amplitude 11)
        dens += 11.0 * math.exp(-(z-2.25)**2 / (2*0.3**2))
        # Peak 2: 4.70 Å, height 3.5 (amplitude 2.5)
        dens += 2.5 * math.exp(-(z-4.7)**2 / (2*0.6**2))
        rows.append((round(z, 3), round(dens, 6)))
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["z", "normalized_density"])
        writer.writerows(rows)

if __name__ == "__main__":
    main(sys.argv[1])