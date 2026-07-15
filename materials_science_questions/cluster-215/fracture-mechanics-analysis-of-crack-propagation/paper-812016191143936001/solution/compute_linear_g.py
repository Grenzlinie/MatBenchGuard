import math, csv

E1 = 181e9
E2 = 10.3e9
nu12 = 0.28
G12 = 7.17e9
Lx = 0.3
Ly = 0.3
B = 0.0025
a = 0.05
Fy = 0.331e6

a11 = 1/E1
a22 = 1/E2
a12 = -nu12/E1
a66 = 1/G12

psi = ((a22/a11)**0.5 + (2*a12 + a66)/(2*a11))**0.5 * (a11*a22/2)**0.5

def compute(beta_deg, k):
    beta = math.radians(beta_deg)
    Fx = k * Fy
    cosb = math.cos(beta)
    sinb = math.sin(beta)
    Gx = (math.pi * a * psi / (4 * B**2 * Ly**2)) * Fx**2 * cosb**2 * (cosb**2 + (a11/a22)**0.5 * sinb**2)
    Gy = (math.pi * a * psi / (4 * B**2 * Lx**2)) * Fy**2 * sinb**2 * (sinb**2 + (a11/a22)**0.5 * cosb**2)
    Gxy = (math.pi * a * psi / (2 * B**2 * Lx * Ly)) * Fx * Fy * sinb**2 * cosb**2 * (1 - (a11/a22)**0.5)
    G_total = Gx + Gy + Gxy
    return Gx/1e6, Gy/1e6, Gxy/1e6, G_total/1e6

rows = []
for beta in [0,30,45,60,90]:
    rows.append([beta, 0.5, *compute(beta, 0.5)])
for k in [-1,0,1]:
    rows.append([45, k, *compute(45, k)])

with open('/app/outputs/linear_energy_release_rates.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['beta','k','G_x','G_y','G_xy','G_total'])
    w.writerows(rows)
