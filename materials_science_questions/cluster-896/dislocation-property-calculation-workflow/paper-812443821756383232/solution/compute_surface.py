import json
import numpy as np

# Model parameters
E_Y = 200e9          # Pa
nu = 0.31
# Convert E_Y to eV/Å³: 1 Pa = 1 J/m³ = 1 J/m³ * (1 eV / 1.602e-19 J) / (1e-10 m/Å)³ = 1 / (1.602e-19 * 1e-30) eV/Å³
# 1 Pa = 1 / (1.602e-19) * 1e30? Actually 1 J = 6.242e18 eV, 1 m = 1e10 Å, so 1 J/m³ = 6.242e18 eV / (1e10 Å)³ = 6.242e18 eV / 1e30 Å³ = 6.242e-12 eV/Å³.
# So E_Y in eV/Å³ = 200e9 * 6.242e-12 = 1.2484 eV/Å³.
E_Y_ev = 200e9 * 6.241509e-12   # more precise 1 eV = 1.602176634e-19 J, 1 m = 1e10 Å
# Let's compute: 1e-19*1e-30 = 1e-49, so 1 Pa = 1 J/m³ = 1/(1.602e-19) * 1/1e-30 = 6.2415e12 eV/Å³.
# Actually, 1 J = 6.2415e18 eV, 1 m³ = 1e30 Å³, so 1 J/m³ = 6.2415e-12 eV/Å³. So 200 GPa = 200e9 Pa = 200e9 * 6.2415e-12 = 1.2483 eV/Å³.
E_Y_ev = 200e9 * 6.241509074e-12   # 1.2483018148 eV/Å³

C = 8 * (1 - nu**2) / (3 * E_Y_ev)  # units Å³/eV

# Surface energies
gamma1 = 0.1   # eV/Å² (not used in E_I directly, but listed)
gamma2 = 0.23  # eV/Å²
gamma3 = 0.1   # eV/Å²
d0 = 2.5       # Å

# Born-Mayer potential
A_bm = 0.003736  # eV
alpha = 3.083     # Å⁻¹

# Fixed total number of He atoms
N_He = 200

# fcc neighbour shells: (distance in units of nearest neighbour d, multiplicity)
shells = [
    (1.0, 12),
    (2.0**0.5, 6),
    (3.0**0.5, 24),
    (2.0, 12),
    (5.0**0.5, 24),
    (6.0**0.5, 8),
    (8.0**0.5, 48),
    (3.0, 6),
    (10.0**0.5, 24),
    (11.0**0.5, 24),
    (12.0**0.5, 8),
    (13.0**0.5, 24),
    (14.0**0.5, 48),
    (4.0, 12),
    (17.0**0.5, 48),
    (18.0**0.5, 6),
    (19.0**0.5, 24),
    (20.0**0.5, 48),
]

# Precompute for p(d) and e(d) the sums for a given d

def pressure_d(d):
    """Gas pressure in eV/Å³ for nearest-neighbour distance d (Å)."""
    sum_R_exp = 0.0
    for R, mult in shells:
        sum_R_exp += mult * R * A_bm * np.exp(-alpha * d * R)
    p = (alpha * sum_R_exp) / (3 * np.sqrt(2) * d**2)
    return p

def energy_per_atom_d(d):
    """Total energy per He atom (eV) for distance d."""
    e = 0.0
    for R, mult in shells:
        e += 0.5 * mult * A_bm * np.exp(-alpha * d * R)
    return e

def V_atom_d(d):
    """Volume per He atom (Å³) for fcc at nearest-neighbour distance d."""
    return d**3 * np.sqrt(2) / 2

# Effective radius
def r_eff(r_p, r_s, N_s=1):
    """Compute (r_eff)^3 for given main radius r_p, satellite radius r_s."""
    factor = N_s * r_s / (np.pi * r_p)
    term1 = (r_p + 2*r_s)**3 * factor
    term2 = r_p**3 * (1 - factor)
    return term1 + term2

# Minimum volume
def V_min(r_p, r_s, N_s=1):
    return np.pi * d0 * (r_p**2 + N_s * r_s**2)

# Solve for d given r_p, r_s
def solve_d(r_p, r_s):
    """Return equilibrium d (Å) for platelet+satellite system."""
    r_eff_val = r_eff(r_p, r_s)
    Vmin = V_min(r_p, r_s)
    # Equation: N_He * V_atom(d) = Vmin + 2*C * r_eff_val * p(d)
    # We solve using bisection on d.
    # Reasonable bounds: d from 0.5 Å to 5.0 Å
    d_lo = 0.5
    d_hi = 5.0
    def f(d):
        V_gas = N_He * V_atom_d(d)
        p_val = pressure_d(d)
        V_elastic = 2 * C * r_eff_val * p_val
        return V_gas - Vmin - V_elastic
    # Check sign at ends
    if f(d_lo) * f(d_hi) >= 0:
        # If no sign change, try larger range
        d_hi = 10.0
        if f(d_lo) * f(d_hi) >= 0:
            raise ValueError(f"No sign change for r_p={r_p}, r_s={r_s}")
    # Bisection
    for _ in range(100):
        d_mid = (d_lo + d_hi) / 2
        f_mid = f(d_mid)
        if abs(f_mid) < 1e-12:
            return d_mid
        if f(d_lo) * f_mid < 0:
            d_hi = d_mid
        else:
            d_lo = d_mid
    return (d_lo + d_hi) / 2

# Total energy E_I
def E_I(r_p, r_s):
    r_eff_val = r_eff(r_p, r_s)
    Vmin = V_min(r_p, r_s)
    d = solve_d(r_p, r_s)
    p = pressure_d(d)
    E_elastic = C * r_eff_val * p**2
    E_surface_flat = 2 * np.pi * gamma2 * (r_p**2 + r_s**2)   # N_s=1
    E_surface_lateral = 2 * np.pi * gamma3 * (r_p + r_s) * d0  # N_s=1
    E_gas = N_He * energy_per_atom_d(d)
    return E_elastic + E_surface_flat + E_surface_lateral + E_gas

# Generate grid
r_p_vals = np.arange(8.0, 12.01, 0.5)
r_s_vals = np.arange(0.0, 3.01, 0.25)

surface = []
for r_p in r_p_vals:
    for r_s in r_s_vals:
        e = E_I(r_p, r_s)
        surface.append({"r_p": round(r_p, 2), "r_s": round(r_s, 2), "E_I": round(e, 6)})

# Discrete saddle point search: find a point that is a local minimum along one coordinate and local maximum along the other.
# We'll fill a 2D array for easy indexing.
nr = len(r_p_vals)
ns = len(r_s_vals)
E_grid = np.array([E_I(r_p, r_s) for r_p in r_p_vals for r_s in r_s_vals]).reshape(nr, ns)

saddle = None
# Check interior points
for i in range(1, nr-1):
    for j in range(1, ns-1):
        e = E_grid[i, j]
        # neighbors along r_p (i-1, i+1 same j) and along r_s (i, j-1, j+1)
        if (e < E_grid[i-1, j] and e < E_grid[i+1, j] and
            e > E_grid[i, j-1] and e > E_grid[i, j+1]):
            saddle = {
                "r_p_saddle": round(r_p_vals[i], 2),
                "r_s_saddle": round(r_s_vals[j], 2),
                "E_saddle": round(e, 6)
            }
            break
    if saddle:
        break
# If no such saddle, check opposite (max along r_p, min along r_s)
if saddle is None:
    for i in range(1, nr-1):
        for j in range(1, ns-1):
            e = E_grid[i, j]
            if (e > E_grid[i-1, j] and e > E_grid[i+1, j] and
                e < E_grid[i, j-1] and e < E_grid[i, j+1]):
                saddle = {
                    "r_p_saddle": round(r_p_vals[i], 2),
                    "r_s_saddle": round(r_s_vals[j], 2),
                    "E_saddle": round(e, 6)
                }
                break
        if saddle:
            break

output = {
    "surface": surface,
    "saddle_point": saddle
}

with open("/app/outputs/step_01_energy_surface.json", "w") as f:
    json.dump(output, f, indent=2)

print("Energy surface written.")
