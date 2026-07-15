import sys, csv, math

def gauss(x, A, mu, sigma, baseline):
    return baseline + A * math.exp(-0.5 * ((x - mu) / sigma)**2)

def main(out_path):
    sigma = 0.25          # nm
    A_free = 1000.0
    A_with = 700.0        # 30% reduction
    baseline = 100.0
    mu = 0.0
    step = 0.02
    x_min = -3.0
    x_max = 3.0
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['distance_nm', 'intensity_defect_free', 'intensity_with_defect'])
        x = x_min
        while x <= x_max + 1e-9:
            i_free = gauss(x, A_free, mu, sigma, baseline)
            i_with = gauss(x, A_with, mu, sigma, baseline)
            writer.writerow([round(x, 8), round(i_free, 2), round(i_with, 2)])
            x += step

if __name__ == '__main__':
    main(sys.argv[1])