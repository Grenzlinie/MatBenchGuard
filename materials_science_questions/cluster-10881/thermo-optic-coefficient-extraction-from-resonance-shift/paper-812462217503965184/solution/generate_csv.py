import math
import csv

B0 = 1.63e-4
tau0 = 0.887  # ps/m
S_B = -3e-4
S_tau = -7e-4

temps = [10, 20, 30, 40, 50]
rows = []
for T in temps:
    dt = T - 10
    B = B0 * math.exp(S_B * dt)
    tau = tau0 * math.exp(S_tau * dt)
    rows.append((T, B, tau))

with open('/app/outputs/temperature_scan_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'B', 'tau'])
    for T, B, tau in rows:
        writer.writerow([T, f'{B:.8e}', f'{tau:.6f}'])
