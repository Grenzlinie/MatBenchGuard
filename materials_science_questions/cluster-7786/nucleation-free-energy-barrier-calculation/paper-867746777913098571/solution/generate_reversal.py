import csv, math, random
random.seed(42)
s_values = [0.5, 2.0, 2.5, 3.0, 3.5]
x_all = [1.25, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 15.0, 18.0, 22.0, 26.0, 30.0]
x1 = 2.5
x2 = 10.0
C0 = 0.0
m_c = 0.12
m_n = 0.36
noise_sigma = 0.05
with open('/app/outputs/reversal_times.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['s','h','tau'])
    for s in s_values:
        x_vals = sorted(x_all)
        for x in x_vals:
            if x <= x1:
                ln_tau = C0
            elif x <= x2:
                ln_tau = C0 + m_c * (x - x1)
            else:
                ln_tau_at_x2 = C0 + m_c * (x2 - x1)
                ln_tau = ln_tau_at_x2 + m_n * (x - x2)
            tau = math.exp(ln_tau + random.gauss(0, noise_sigma))
            h = -1.0 / x
            writer.writerow([s, h, tau])
