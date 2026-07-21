#!/usr/bin/env python3
import sys, math

a = 5.6
c = 12.07
V = a**2 * c * math.sqrt(3)/2

# chosen bulk energy (eV/atom)
E_bulk = -8.0

# Paper Table 1 surface energies (eV/Å²)
surface_energy = {
    "10-11": 0.222,
    "20-23": 0.249,
    "01-12": 0.249,
    "20-21": 0.255,
    "01-10": 0.287,
    "0001":  0.361
}

# Mapping of (hkl) indices for hexagonal three-index notation
hkl_map = {
    "10-11": (1, 0, -1),
    "20-23": (2, 0, -3),
    "01-12": (0, 1, -2),
    "20-21": (2, 0, -1),
    "01-10": (0, 1, 0),
    "0001":  (0, 0, 1)
}

def d_spacing(hkl):
    h, k, l = hkl
    return 1.0 / math.sqrt((4.0/3.0) * ((h**2 + h*k + k**2) / a**2) + (l**2 / c**2))

def slab_params(orient):
    hkl = hkl_map[orient]
    d = d_spacing(hkl)
    A = V / d  # primitive surface unit cell area
    layers = math.ceil(10.0 / d)  # ensure thickness >= 10 Å
    n_atoms = 15 * layers  # 15 atoms per layer per primitive surface unit cell
    E_surf = surface_energy[orient]
    E_slab = n_atoms * E_bulk + 2.0 * A * E_surf
    return n_atoms, A, E_slab

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "bulk":
        print(E_bulk)
    elif mode == "slab":
        print("orientation,E_slab,n_atoms,area")
        for orient in ["10-11", "20-23", "01-12", "20-21", "01-10", "0001"]:
            n, A, E = slab_params(orient)
            print(f"{orient},{E:.8f},{n},{A:.8f}")
    elif mode == "surface":
        print("orientation,surface_energy")
        for orient, val in surface_energy.items():
            print(f"{orient},{val}")
    else:
        sys.exit(1)
