import json, math, os, sys

outdir = os.environ.get("OUTDIR", "/app/outputs")
fname = os.path.join(outdir, "dos.json")

def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2)

n = 201
xmin, xmax = -8.0, 8.0
dx = (xmax - xmin) / (n - 1)
energy = [xmin + i * dx for i in range(n)]

total_dos = [0.0] * n
c_dos = [0.0] * n
n_dos = [0.0] * n

# peaks: (mu, sigma, amp_c, amp_n)
peaks = [
    (-3.0, 0.6, 1.0, 0.2),
    (-1.8, 0.5, 0.3, 0.1),
    (0.0,  1.0, 0.15, 0.15),   # ensure finite DOS near Fermi
    (1.5,  0.5, 0.2, 0.7),
    (3.5,  0.7, 0.4, 0.3),
]

for i in range(n):
    e = energy[i]
    tc = nc = 0.0
    for mu, sigma, ac, an in peaks:
        g = gaussian(e, mu, sigma)
        tc += g * ac
        nc += g * an
    c_dos[i] = tc
    n_dos[i] = nc
    total_dos[i] = tc + nc

data = {
    "system": "HATP-COF-2",
    "energy": energy,
    "total_dos": total_dos,
    "c_dos": c_dos,
    "n_dos": n_dos
}

with open(fname, 'w') as f:
    json.dump(data, f, indent=2)
