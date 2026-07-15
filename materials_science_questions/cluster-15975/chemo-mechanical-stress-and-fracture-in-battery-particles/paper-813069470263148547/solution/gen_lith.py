import csv
import math
import sys


CS_MAX = 31374.0   # mol/m3  (graphite maximum Li concentration)


def generate_charge(pressure):
    initial_soc = 0.2
    capacity_As = 10.0 * 3600.0
    current = 5.0  # A
    soc_end_cc = 0.95
    t_cc = (soc_end_cc - initial_soc) * capacity_As / current
    total_time = t_cc + 1800.0
    dt = 60.0
    t = 0.0
    rows = []
    while t <= total_time:
        if t <= t_cc:
            soc = initial_soc + t * current / capacity_As
        else:
            tau = 600.0
            soc = soc_end_cc + (0.98 - soc_end_cc) * (1.0 - math.exp(-(t - t_cc) / tau))
        c_avg = CS_MAX * soc
        # pressure‑dependent lithiation heterogeneity
        if pressure <= 0.4:
            factor = 0.1
        elif pressure <= 2.0:
            factor = 0.5
        else:
            factor = 1.0
        delta = factor * 6000 * soc
        c_sep = min(c_avg + delta, CS_MAX)
        c_cc = max(c_avg - delta, 0.0)
        rows.append([
            pressure,
            round(t, 2),
            round(soc, 6),
            round(c_sep, 2),
            round(c_cc, 2)
        ])
        t += dt
    return rows


def main():
    writer = csv.writer(sys.stdout)
    writer.writerow(['pressure_MPa', 'time_s', 'soc',
                     'anode_conc_sep_mol_m3', 'anode_conc_cc_mol_m3'])
    for p in [0.4, 2.0, 4.0]:
        for row in generate_charge(p):
            writer.writerow(row)


if __name__ == '__main__':
    main()
