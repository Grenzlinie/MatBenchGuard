import csv
import sys


def ocv(soc):
    """Full‑cell OCV for NMC/graphite, V"""
    if soc <= 0.0:
        return 2.7
    if soc >= 1.0:
        return 4.2
    xs = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    ys = [2.7, 3.55, 3.75, 3.92, 4.08, 4.2]
    for i in range(len(xs) - 1):
        if xs[i] <= soc <= xs[i + 1]:
            t_val = (soc - xs[i]) / (xs[i + 1] - xs[i])
            return ys[i] + (ys[i + 1] - ys[i]) * t_val
    return 4.2


def voltage(soc, current, r_internal):
    return ocv(soc) - current * r_internal


def swelling(soc, config):
    max_swell = 200e-6 if config == 'soft' else 150e-6  # m
    return max_swell * soc


def jig_force(soc, config):
    F0 = 3000.0
    if config == 'stiff':
        k = 10e6   # N/m
        max_swell = 150e-6
    else:
        k = 900e3
        max_swell = 200e-6
    return F0 + k * max_swell * soc


def c_rate_str(rate):
    if rate == 0.2:
        return 'C_5'
    if rate == 0.5:
        return 'C_2'
    if rate == 1.0:
        return '1C'
    if rate == 2.0:
        return '2C'
    return str(rate)


def simulate_discharge(c_rate, config):
    capacity_Ah = 10.0
    current = c_rate * capacity_Ah  # A
    r_internal = 0.025               # Ohm
    time_end_theoretical = 3600.0 * capacity_Ah / current
    dt = 180.0 if current <= 2 else 60.0
    t = 0.0
    rows = []
    while t < time_end_theoretical:
        soc = 1.0 - t / time_end_theoretical
        v = voltage(soc, current, r_internal)
        if v <= 2.7:
            break
        sw = swelling(soc, config)
        jf = jig_force(soc, config)
        rows.append([
            config,
            c_rate_str(c_rate),
            round(t, 2),
            round(v, 4),
            round(sw, 10),
            round(jf, 2)
        ])
        t += dt
    return rows


def main():
    writer = csv.writer(sys.stdout)
    writer.writerow(['configuration', 'c_rate', 'time_s', 'voltage_V',
                     'swelling_m', 'jig_force_N'])
    configs = ['stiff', 'soft']
    crates = [0.2, 0.5, 1.0, 2.0]
    for conf in configs:
        for cr in crates:
            for row in simulate_discharge(cr, conf):
                writer.writerow(row)


if __name__ == '__main__':
    main()
