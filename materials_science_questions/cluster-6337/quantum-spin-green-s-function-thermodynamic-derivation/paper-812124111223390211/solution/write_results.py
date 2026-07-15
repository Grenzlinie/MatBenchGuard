import math, csv, itertools

S = 1
J = 1.0
D = 1.0
T = 10.0

fD = 1.0 / (math.exp(D/T) - 1.0)
C1 = 2.0 * math.pi * fD
C2 = 2.0 * math.pi * (2.0 * fD + 1.0)

phi = {}
for m in [-1, 0, 1]:
    phi[m] = C1 + C2 * (m - 2)

phi_m1 = phi[-1]
phi_0  = phi[0]
a0 = 1.0
a1 = (1.0 + phi_m1) / phi_m1
a2 = a1 * (1.0 + phi_0) / phi_0
sum_a = a0 + a1 + a2
lam = [a0/sum_a, a1/sum_a, a2/sum_a]

M2 = lam[0] + lam[2]

xs = [i*0.1 for i in range(-50, 51)]
with open('/app/outputs/omega_x_values.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x', 'Omega'])
    for x in xs:
        Omega = lam[0]*math.exp(-x) + lam[1] + lam[2]*math.exp(x)
        w.writerow([x, Omega])

cs = [-lam[0], 0.0, lam[2]]
with open('/app/outputs/lambda_ij_coefficients.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['m', 'c'])
    for m, c in enumerate(cs):
        w.writerow([m, c])

chi0 = M2 / T
J0 = 4.0 * J

q_points = [(0,0), (math.pi,0), (math.pi,math.pi), (0,math.pi)]
for i in range(10):
    qx = -math.pi + (2.0*math.pi) * i / 9.0
    for j in range(10):
        qy = -math.pi + (2.0*math.pi) * j / 9.0
        q_points.append((qx, qy))

with open('/app/outputs/chi_qzz_values.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['q_x', 'q_y', 'chi_qzz'])
    for qx, qy in q_points:
        Jq = 2.0 * J * (math.cos(qx) + math.cos(qy))
        denom = 1.0/chi0 + 2.0*(J0 - Jq)
        chi = T / denom
        w.writerow([qx, qy, chi])
