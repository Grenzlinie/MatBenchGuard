import csv, math, sys

def main():
    outpath = sys.argv[1]
    qs = [i * 0.005 for i in range(101)]  # 0..0.5
    q0 = 0.3
    sigma = 0.03
    rows = []
    for q in qs:
        diff = (q - q0) / sigma
        dip_factor = math.exp(-diff * diff)
        momega2 = 150.0 - 100.0 * dip_factor
        d2approx = 50.0 * dip_factor
        rows.append((round(q, 4), round(momega2, 4), round(d2approx, 4)))

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['q', 'momega2', 'D2approx'])
        writer.writerows(rows)

if __name__ == '__main__':
    main()
