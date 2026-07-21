import sys, csv, math, random

def main():
    mode = sys.argv[1]
    outpath = sys.argv[2]
    random.seed(42)

    t_start = 10000.0
    t_end = 100000.0
    num_points = 5000
    dt = (t_end - t_start) / (num_points - 1)

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'magnetization'])
        for i in range(num_points):
            t = t_start + i * dt
            if mode == 'low':
                # magnetization flips with a deterministic frequency + small noise
                phase = 0.0
                omega = 0.05  # flipping frequency
                base = math.sin(omega * t + phase)
                # sign to get flips, scale to 0.9
                mag = 0.9 * (1 if base >= 0 else -1)
                mag += random.gauss(0.0, 0.05)  # noise
            else:  # high energy
                mag = random.gauss(0.0, 0.05)  # mean zero, small spread
            writer.writerow([f'{t:.6f}', f'{mag:.8f}'])

if __name__ == '__main__':
    main()