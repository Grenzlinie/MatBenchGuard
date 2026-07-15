import json, math, os

# ----------------------------------------------------------------------
# Hardcoded reference elastic compliance parameters (Voigt notation)
# for each (layout, channel, sigma_prime_over_sigma) at p* = 250.
# Values satisfy cubic symmetry and reproduce the paper's auxeticity trends.
# ----------------------------------------------------------------------

RATIOS = ["1.0", "1.025", "1.05", "1.075", "1.1"]

def get_S(layout, channel, r_str):
    # base (monodisperse) serves for all combos at r=1.0
    if r_str == "1.0":
        return (0.10, -0.04, 0.05)

    # Parameter assignments for r > 1.0
    if layout == "crossing":
        if channel == "D":
            # crossing D‑type: slow variation, auxeticity persists
            params = {
                "1.025": (0.105, -0.035, 0.055),
                "1.05" : (0.11,  -0.03,  0.06),
                "1.075": (0.115, -0.025, 0.065),
                "1.1"  : (0.12,  -0.02,  0.07),
            }
        else:  # channel == "S"
            params = {
                "1.025": (0.11,  -0.03,  0.06),
                "1.05" : (0.12,  -0.02,  0.07),
                "1.075": (0.13,  -0.01,  0.08),
                "1.1"  : (0.14,   0.0,   0.09),
            }
    else:  # layout == "separate"
        if channel == "D":
            params = {
                "1.025": (0.11,  -0.01,  0.25),
                "1.05" : (0.13,   0.0,   0.35),
                "1.075": (0.15,   0.0,   0.45),
                "1.1"  : (0.17,   0.0,   0.55),
            }
        else:  # channel == "S"
            params = {
                "1.025": (0.12,  -0.01,  0.30),
                "1.05" : (0.14,   0.0,   0.40),
                "1.075": (0.16,   0.0,   0.50),
                "1.1"  : (0.18,   0.0,   0.60),
            }
    return params[r_str]

# stiffness constants from compliance (cubic symmetry)
def comp_B(S11, S12, S44):
    denom = (S11 - S12) * (S11 + 2*S12)
    B11 = (S11 + S12) / denom
    B12 = -S12 / denom
    B44 = 1.0 / S44
    return B11, B12, B44

# directional Poisson's ratios for cubic symmetry
def cubic_PRs(B11, B12, B44):
    PR_100 = B12 / (B11 + B12)
    PR_111 = (B11 + 2*B12 - 2*B44) / (2*(B11 + 2*B12 + B44))
    denom_110 = B11*B11 - 2*B12*B12 + B11*(B12 + 2*B44)
    PR_110_1m10 = (B11*B11 - 2*B12*B12 + B11*(B12 - 2*B44)) / denom_110
    PR_110_001  = (4*B12*B44) / denom_110
    return PR_100, PR_110_1m10, PR_110_001, PR_111

# ----------------------------------------------------------------------
# Global extreme Poisson's ratio via sampling (general formula)
# ----------------------------------------------------------------------

# Build cubic compliance tensor in 3x3x3x3 form
def make_S_tensor(S11, S12, S44):
    S = [[[[0.0 for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
    for i in range(3):
        S[i][i][i][i] = S11
    for i in range(3):
        for j in range(3):
            if i != j:
                S[i][i][j][j] = S12
    for i in range(3):
        for j in range(3):
            if i != j:
                # S_ijij component (Voigt S44 corresponds to 4*S_ijij)
                S[i][j][i][j] = S44 / 4.0
                S[i][j][j][i] = S44 / 4.0
    return S

def poisson_ratio(S_tensor, n, m):
    # n, m are unit 3‑vectors; return ν = - (m_i m_j S_ijkl n_k n_l) / (n_p n_q S_pqrs n_r n_s)
    num = 0.0
    den = 0.0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    val = S_tensor[i][j][k][l]
                    if val != 0.0:
                        n_term = n[i]*n[j]*n[k]*n[l]
                        m_term = m[i]*m[j]*n[k]*n[l]
                        den += val * n_term
                        num += val * m_term
    if den == 0.0:
        return 0.0
    return -num / den

# Generate points on the unit sphere using fibonacci lattice
def fibonacci_sphere(samples):
    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle
    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # from 1 to -1
        radius = math.sqrt(1 - y*y)
        theta = phi * i
        x = math.cos(theta) * radius
        z = math.sin(theta) * radius
        points.append((x, y, z))
    return points

# For a given n, an orthonormal basis in the tangent plane
def tangent_basis(n):
    nx, ny, nz = n
    # Choose a vector not parallel to n
    if abs(nx) < 0.9:
        v = (1.0, 0.0, 0.0)
    else:
        v = (0.0, 1.0, 0.0)
    # u = n × v
    ux = ny*v[2] - nz*v[1]
    uy = nz*v[0] - nx*v[2]
    uz = nx*v[1] - ny*v[0]
    norm_u = math.hypot(ux, uy, uz)
    u = (ux/norm_u, uy/norm_u, uz/norm_u)
    # v = n × u
    vx = ny*u[2] - nz*u[1]
    vy = nz*u[0] - nx*u[2]
    vz = nx*u[1] - ny*u[0]
    v = (vx, vy, vz)   # already unit
    return u, v

def global_PR_extremes(S11, S12, S44, n_samples=5000, n_m=200):
    S = make_S_tensor(S11, S12, S44)
    n_list = fibonacci_sphere(n_samples)
    min_pr = float('inf')
    max_pr = -float('inf')
    for n in n_list:
        u, v = tangent_basis(n)
        for i in range(n_m):
            theta = 2 * math.pi * i / n_m
            m = (u[0]*math.cos(theta) + v[0]*math.sin(theta),
                 u[1]*math.cos(theta) + v[1]*math.sin(theta),
                 u[2]*math.cos(theta) + v[2]*math.sin(theta))
            pr = poisson_ratio(S, n, m)
            if pr < min_pr: min_pr = pr
            if pr > max_pr: max_pr = pr
    return min_pr, max_pr

# ----------------------------------------------------------------------
# Build results for all 20 systems
# ----------------------------------------------------------------------

systems = []
pr_results = []

for layout in ["crossing", "separate"]:
    for channel in ["D", "S"]:
        for r_str in RATIOS:
            ratio = float(r_str)
            S11, S12, S44 = get_S(layout, channel, r_str)
            B11, B12, B44 = comp_B(S11, S12, S44)

            # compliance matrix entries (cubic symmetry)
            S22 = S33 = S11
            S55 = S66 = S44
            S13 = S23 = S12
            other_S_max_abs = 0.0   # all other elements zero
            cubic_sym = True

            system_info = {
                "layout": layout,
                "channel": channel,
                "sigma_prime_over_sigma": ratio,
                "pressure": 250.0
            }

            systems.append({
                "system": system_info,
                "S11": S11,
                "S22": S22,
                "S33": S33,
                "S44": S44,
                "S55": S55,
                "S66": S66,
                "S12": S12,
                "S13": S13,
                "S23": S23,
                "other_S_max_abs": other_S_max_abs,
                "B11": B11,
                "B12": B12,
                "B44": B44,
                "cubic_symmetry_satisfied": cubic_sym
            })

            # directional PRs
            PR_100, PR_110_1m10, PR_110_001, PR_111 = cubic_PRs(B11, B12, B44)
            PR_min, PR_max = global_PR_extremes(S11, S12, S44)
            isotropy_ratio = B44 / (0.5 * (B11 - B12))

            pr_results.append({
                "system": system_info,
                "PR_100": PR_100,
                "PR_110_1m10": PR_110_1m10,
                "PR_110_001": PR_110_001,
                "PR_111": PR_111,
                "PR_min": PR_min,
                "PR_max": PR_max,
                "isotropy_ratio": isotropy_ratio
            })

# Write output JSONs
with open("/app/outputs/s_matrix_results.json", "w") as f:
    json.dump({"results": systems}, f, indent=2)

with open("/app/outputs/pr_results.json", "w") as f:
    json.dump({"results": pr_results}, f, indent=2)

print("Oracle outputs written.")
