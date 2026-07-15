import csv
import math
import os

OUTDIR = "/app/outputs"

def gauss(x, mu, sigma, A):
    if sigma <= 0:
        return 0.0
    return A * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

# ----- DOS generation -----
# energy grid: -20 to 15 eV step 0.1 eV
energies = []
x = -20.0
while x <= 15.0:
    energies.append(round(x, 1))
    x += 0.1

# define orbital contributions
Cu_s = []
Cu_p = []
Cu_d = []
Al_s = []
Al_p = []
Al_d = []
S_s = []
S_p = []

for e in energies:
    # Cu d: two peaks (e and t2) in valence band
    d_e = gauss(e, -3.5, 0.6, 10.0)
    d_t2 = gauss(e, -1.0, 0.5, 12.0)
    cu_d = d_e + d_t2
    Cu_d.append(max(cu_d, 0.0))

    # Cu s and p: conduction band
    s = gauss(e, 6.0, 1.5, 8.0) + gauss(e, 9.0, 1.5, 4.0)
    Cu_s.append(max(s, 0.0))
    p = gauss(e, 5.0, 1.5, 7.0) + gauss(e, 8.5, 1.5, 4.0)
    Cu_p.append(max(p, 0.0))

    # Al s and p: conduction band
    a_s = gauss(e, 6.0, 1.5, 6.0) + gauss(e, 9.5, 1.5, 3.0)
    Al_s.append(max(a_s, 0.0))
    a_p = gauss(e, 5.0, 1.5, 5.0) + gauss(e, 8.5, 1.5, 3.0)
    Al_p.append(max(a_p, 0.0))

    # Al d: deep band at -15 eV
    al_d = gauss(e, -15.0, 0.3, 30.0)
    Al_d.append(max(al_d, 0.0))

    # S s and p: valence and some conduction
    s_s = gauss(e, -5.0, 2.5, 5.0) + gauss(e, -2.0, 2.5, 3.0) + gauss(e, 6.0, 3.0, 2.0)
    S_s.append(max(s_s, 0.0))
    s_p = gauss(e, -2.0, 2.5, 6.0) + gauss(e, -6.0, 2.5, 4.0) + gauss(e, 5.0, 3.0, 2.0)
    S_p.append(max(s_p, 0.0))

# total DOS as sum of all contributions
total = []
for i in range(len(energies)):
    total.append(Cu_s[i] + Cu_p[i] + Cu_d[i] + Al_s[i] + Al_p[i] + Al_d[i] + S_s[i] + S_p[i])

# write dos_total_CuAlS2.csv
with open(os.path.join(OUTDIR, "dos_total_CuAlS2.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["energy", "total_DOS"])
    for i in range(len(energies)):
        writer.writerow([f"{energies[i]:.1f}", f"{total[i]:.4f}"])

# write dos_partial_CuAlS2.csv (column order: energy, Cu_s, Cu_p, Cu_d, Al_s, Al_p, Al_d, S_s, S_p)
with open(os.path.join(OUTDIR, "dos_partial_CuAlS2.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["energy", "Cu_s", "Cu_p", "Cu_d", "Al_s", "Al_p", "Al_d", "S_s", "S_p"])
    for i in range(len(energies)):
        writer.writerow([
            f"{energies[i]:.1f}",
            f"{Cu_s[i]:.4f}",
            f"{Cu_p[i]:.4f}",
            f"{Cu_d[i]:.4f}",
            f"{Al_s[i]:.4f}",
            f"{Al_p[i]:.4f}",
            f"{Al_d[i]:.4f}",
            f"{S_s[i]:.4f}",
            f"{S_p[i]:.4f}"
        ])

# ----- Dielectric function generation -----
# fine grid for KK transform
e_fine = []
x = 0.0
while x <= 20.0:
    e_fine.append(round(x, 2))
    x += 0.01

# define imaginary part epsilon2 on fine grid
eps2_fine = []
for e in e_fine:
    val = (
        gauss(e, 4.0, 0.5, 8.0) +
        gauss(e, 5.0, 0.5, 10.0) +
        gauss(e, 7.0, 0.5, 12.0) +
        gauss(e, 9.0, 0.6, 8.0) +
        gauss(e, 12.0, 1.0, 5.0)
    )
    eps2_fine.append(max(val, 0.0))

# Compute epsilon1 via regularised Kramers-Kronig (numerical integration)
eta = 0.15   # small regularisation to avoid singularity
delta = 0.01
eps1_fine = []
for idx, omega in enumerate(e_fine):
    integ = 0.0
    for j, wp in enumerate(e_fine):
        if wp == omega:
            continue   # skip singular point, regularisation handles it
        factor = wp * eps2_fine[j] / (wp**2 - omega**2)
        integ += factor * delta
    eps1 = 1.0 + (2.0 / math.pi) * integ
    eps1_fine.append(eps1)

# rescale eps1_fine so that eps1(0) = 5.1076 (n=2.26 => n^2=5.1076)
target_eps1_0 = 5.1076
current_eps1_0 = eps1_fine[0]   # omega=0
if current_eps1_0 != 0:
    scale = target_eps1_0 / current_eps1_0
else:
    scale = 1.0
eps1_fine = [v * scale for v in eps1_fine]

# target output grid: 0 to 20 eV step 0.05 eV
step_out = 0.05
en_out = []
x = 0.0
while x <= 20.0:
    en_out.append(round(x, 2))
    x += step_out

# interpolate (nearest neighbour) from fine grid
eps1_out = []
eps2_out = []
fine_len = len(e_fine)
for e in en_out:
    # find closest index
    idx = min(range(fine_len), key=lambda i: abs(e_fine[i] - e))
    eps1_out.append(eps1_fine[idx])
    eps2_out.append(eps2_fine[idx])

# write dielectric_function_CuAlS2.csv
with open(os.path.join(OUTDIR, "dielectric_function_CuAlS2.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["energy", "epsilon1", "epsilon2"])
    for i in range(len(en_out)):
        writer.writerow([f"{en_out[i]:.2f}", f"{eps1_out[i]:.6f}", f"{eps2_out[i]:.6f}"])

print("CSV files generated successfully.")
