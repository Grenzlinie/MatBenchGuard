import csv, math, sys

writer = csv.writer(sys.stdout)
writer.writerow(["delta", "temperature", "q", "omega"])
deltas = [0.1, 0.3, 0.6]
temperature = 0.15
q_step = 0.01
q_max = math.pi
q = 0.0
while q <= q_max + 1e-9:
    for delta in deltas:
        if delta < 0.5:
            omega = 2.0 * math.sin(q / 2.0)
        else:
            omega = 2.0 * math.sin(q)
        writer.writerow([delta, temperature, round(q, 10), round(omega, 10)])
    q = round(q + q_step, 10)
