import math

# Constants from the paper/instruction
sigma = 1.0          # J/m^2
v_A = 1e-5           # m^3/mol
T = 300              # K
n_A = 1e-4           # mole
N = 1e14
x_A_sat = 1e-5
R = 8.314            # J/(mol K)

S_ini = n_A / x_A_sat  # = 10

def dG(r):
    """Gibbs free energy change per nucleus (J) for radius r in meters."""
    # number of moles of A in all nuclei
    n_A_n = (4.0 * math.pi * r**3 * N) / (3.0 * v_A)
    if r == 0.0:
        return 0.0
    # surface term
    surf = 4.0 * math.pi * r**2 * sigma
    # -⁠ (n_A_n R T / N) ln S_ini
    term1 = -(n_A_n * R * T / N) * math.log(S_ini)
    # (n_A - n_A_n)(R T / N) ln((1 - n_A_n/n_A) / (1 - n_A_n))
    arg1 = (1.0 - n_A_n / n_A) / (1.0 - n_A_n)
    term2 = (n_A - n_A_n) * (R * T / N) * math.log(arg1)
    # (1 - n_A)(R T / N) ln(1 / (1 - n_A_n))
    arg2 = 1.0 / (1.0 - n_A_n)
    term3 = (1.0 - n_A) * (R * T / N) * math.log(arg2)
    return surf + term1 + term2 + term3

# Scan radii from nearly 0 to 10 nm on a fine grid
r_start = 1e-12         # 0.001 nm, avoids log(0) issues
r_end = 10e-9           # 10 nm
num_points = 100001     # ~ 1e-13 m spacing
dr = (r_end - r_start) / (num_points - 1)

r_vals = [r_start + i * dr for i in range(num_points)]
g_vals = [dG(r) for r in r_vals]

# Locate the local maximum (critical radius)
max_idx = None
for i in range(1, num_points - 1):
    if g_vals[i] > g_vals[i-1] and g_vals[i] > g_vals[i+1]:
        max_idx = i
        break

# Locate the local minimum after the maximum
min_idx = None
if max_idx is not None:
    for i in range(max_idx + 1, num_points - 1):
        if g_vals[i] < g_vals[i-1] and g_vals[i] < g_vals[i+1]:
            min_idx = i
            break

if max_idx is None or min_idx is None:
    raise RuntimeError("Failed to locate maximum or minimum in nucleation curve.")

r_max = r_vals[max_idx]
DeltaG_max = g_vals[max_idx]
r_min = r_vals[min_idx]
DeltaG_min = g_vals[min_idx]

# Convert radii to nm for output
r_max_nm = r_max * 1e9
r_min_nm = r_min * 1e9

# Write the required CSV
with open('/app/outputs/extremum_points.csv', 'w') as f:
    f.write('r_max (nm),DeltaG_max (J),r_min (nm),DeltaG_min (J)\n')
    f.write(f'{r_max_nm:.6f},{DeltaG_max:.6e},{r_min_nm:.6f},{DeltaG_min:.6e}\n')
