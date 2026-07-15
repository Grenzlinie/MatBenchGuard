import csv
import math
import itertools

# Spin states: five discrete orientations (unit vectors)
states = [
    (0.0, 0.0, 1.0),   # 0: easy axis
    (0.0, 0.0, -1.0),   # 1
    (1.0, 0.0, 0.0),    # 2
    (-1.0, 0.0, 0.0),   # 3
    (0.0, 1.0, 0.0)     # 4
]

# Constants
kB = 1.380649e-23
J11_val = 0.9e-23
J12_val = -J11_val / 1.96  # J11/J12 = -1.96
EMAE = 3.04e-26
D12 = 1.5e-23
# Zeeman coefficient: mu0 M, where M = 5.4 muB in J/T, mu0 H = H(Oe)*1e-4 T
M_J = 5.4 * 9.274009994e-24          # J/T
zeeman_per_Oe = M_J * 1e-4          # J per Oe per unit z-component
# i.e., Zeeman energy = -zeeman_per_Oe * H * spin_z

# Geometry: 2 rows (0..1) x 4 columns (0..3), index mapping
sites = [(i, j) for i in range(2) for j in range(4)]
site_to_idx = {pos: idx for idx, pos in enumerate(sites)}
n = len(sites)  # 8

# Nearest neighbour (90° bonds): Manhattan distance 1
bonds_90 = []
for (i, j) in sites:
    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < 2 and 0 <= nj < 4:
            if (i, j) < (ni, nj):  # avoid duplicates
                bonds_90.append((site_to_idx[(i,j)], site_to_idx[(ni,nj)]))

# Next-nearest neighbour (180° bonds): diagonal, Manhattan distance 2
bonds_180 = []
for (i, j) in sites:
    for di, dj in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < 2 and 0 <= nj < 4:
            if (i, j) < (ni, nj):
                bonds_180.append((site_to_idx[(i,j)], site_to_idx[(ni,nj)]))

# Surface 90° bonds: horizontal bonds are always on top/bottom boundary (rows 0,1)
# vertical bonds only at leftmost (col 0) and rightmost (col 3)
surface_90 = []
for a, b in bonds_90:
    (i1, j1), (i2, j2) = sites[a], sites[b]
    if i1 == i2:  # horizontal
        surface_90.append((a, b))
    else:  # vertical
        assert j1 == j2
        if j1 in (0, 3):
            surface_90.append((a, b))

# Precompute surface set for fast lookup
surface_set = set(surface_90)

# Precompute dot products for pairs of spin states
# We'll compute on the fly using inline dot

def compute_config_data():
    """Return list of (fixed_energy, total_z) for each spin configuration."""
    configs = []
    for spins in itertools.product(range(5), repeat=n):
        # Exchange + DMI + anisotropy (fixed part)
        E = 0.0
        # 90° bonds with DMI on surface
        for (a, b) in bonds_90:
            sa, sb = spins[a], spins[b]
            dot = states[sa][0]*states[sb][0] + states[sa][1]*states[sb][1] + states[sa][2]*states[sb][2]
            cos_th = dot  # spin vectors are unit
            E += -J12_val * cos_th
            if (a, b) in surface_set:
                sin_th = math.sqrt(max(0.0, 1.0 - cos_th*cos_th))
                E += -D12 * sin_th
        # 180° bonds (no DMI)
        for (a, b) in bonds_180:
            sa, sb = spins[a], spins[b]
            dot = states[sa][0]*states[sb][0] + states[sa][1]*states[sb][1] + states[sa][2]*states[sb][2]
            E += -J11_val * dot
        # Anisotropy: penalty for any state not easy axis (index 0)
        for s in spins:
            if s != 0:
                E += EMAE
        # total z-magnetization (projection onto field direction)
        total_z = sum(states[s][2] for s in spins)
        configs.append((E, total_z))
    return configs

# Precompute once
print("Enumerating all 5^8 configurations...")
config_data = compute_config_data()
print(f"Total configs: {len(config_data)}")

# Output CSV
output_path = "/app/outputs/magnetization_curves.csv"
with open(output_path, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Temperature_K", "Field_Oe", "Normalized_Magnetization"])

    # Temperature 2..30 K in steps of 1 K
    for T in range(2, 31):
        beta = 1.0 / (kB * T)
        for H in (200, 500, 1000):
            Z = 0.0
            Mz = 0.0
            # Zeeman coefficient for this field
            zeeman_factor = zeeman_per_Oe * H  # energy per unit z-component
            for (E_fixed, z_sum) in config_data:
                # total energy = fixed + Zeeman
                E_total = E_fixed - zeeman_factor * z_sum  # Zeeman: -μ0 M H z
                bf = math.exp(-E_total * beta)
                Z += bf
                Mz += z_sum * bf
            # Normalized magnetization = average z per site
            norm_mag = (Mz / Z) / n  # n = 8
            writer.writerow([float(T), H, round(norm_mag, 12)])

print("Done.")
