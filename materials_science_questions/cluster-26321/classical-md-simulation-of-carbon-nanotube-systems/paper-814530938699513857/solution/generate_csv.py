import csv
import math
import random
import sys

def gen_time_series(scheme, temperature):
    if scheme == '1LR':
        if temperature == 200:
            target_mid = 50.0
        elif temperature == 300:
            target_mid = 85.0
        else:  # 400
            target_mid = 130.0
    else:
        if temperature == 200:
            target_mid = 70.0
        else:
            target_mid = 133.0

    # acceleration time constant: shorter for more IRD atoms
    n_ird = int(scheme[0])
    tau = 3000.0 / n_ird
    tau = max(300, tau)
    tau_inner = tau * 3

    # generate time points: coarse before 6000, fine in the last 2000 ps
    time_points = []
    t = 0.0
    while t <= 6000:
        time_points.append(t)
        t += 10.0
    t = 6000.0
    while t <= 7000:
        time_points.append(t)
        t += 5.0
    t = 7000.0
    while t <= 8000:
        time_points.append(t)
        t += 1.0
    time_points = sorted(set(time_points))

    rows = []
    f_mid = 0.0
    f_inner = 0.0
    prev_t = 0.0
    amp = 1.5
    mean_z = 3.0
    period = 100.0  # ps

    for t in time_points:
        dt = t - prev_t
        if dt > 0:
            drift = (target_mid - f_mid) * (1 - math.exp(-dt / tau))
            noise = random.gauss(0, 2.0) * (dt / 1.0)
            f_mid += drift + noise
            f_mid = max(0, f_mid)

            drift_inner = (target_mid - f_inner) * (1 - math.exp(-dt / tau_inner))
            noise_inner = random.gauss(0, 3.0) * (dt / 1.0)
            f_inner += drift_inner + noise_inner
            f_inner = max(0, f_inner)

        z = amp * math.sin(2 * math.pi * t / period) + mean_z + random.gauss(0, 0.05)
        rows.append([scheme, temperature, round(t, 3), round(f_mid, 4), round(f_inner, 4), round(z, 6)])
        prev_t = t
    return rows

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    outpath = sys.argv[1]
    random.seed(42)
    schemes = ['1L','2L','3L','4L','1LR','2LR','3LR','4LR']
    temperatures = [200, 300, 400]
    header = ['scheme','temperature','time','mid_rotor_frequency','inner_rotor_frequency','inner_rotor_z_position']
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for scheme in schemes:
            for temp in temperatures:
                rows = gen_time_series(scheme, temp)
                writer.writerows(rows)

if __name__ == '__main__':
    main()