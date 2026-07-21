import sys, math, csv

E_20 = 8e8
alpha = 6.6e-18
x20 = alpha * E_20**2
b2_20 = 1 - (0.5 + 0.5 / math.sqrt(1 + x20))
QS_4s_20 = -0.288
QS_latt_20 = -0.196

r_table = {20: 1.0, 40: 0.93, 60: 0.81, 80: 0.66, 100: 0.46}
temps = [20, 40, 60, 80, 100]

writer = csv.writer(sys.stdout)
writer.writerow(['T_C', 'QS_mm_s'])
for T in temps:
    r = r_table[T]
    E = E_20 * r
    x = alpha * E**2
    a2 = 0.5 + 0.5 / math.sqrt(1 + x)
    b2 = 1 - a2
    delta = QS_4s_20 * (b2 / b2_20)
    QS_latt = QS_latt_20 * r
    total = QS_latt + delta
    writer.writerow([T, round(total, 3)])
