import json, math

# Model parameters
t1 = 0.2
t2 = 1.0
ep_minus_ed = 4.0  # e_p - e_d
U = 7.0
J = 0.12

# Derived quantities
ed_minus_ep = -ep_minus_ed  # e_d - e_p
ed_plus_U_minus_ep = ed_minus_ep + U  # e_d + U - e_p = -4 + 7 = 3

# Optimal cluster size n (Eq.11)
coeff = (1.0 / (0.19 * J)) * (3.0 / ed_plus_U_minus_ep + 2.0 / ep_minus_ed)
n = t2 * math.sqrt(coeff)

# Total formation energy ΔE (Eq.10)
Delta_E = (-2 * t1
           + (t2**2 / ed_plus_U_minus_ep) * (3.0 / n - 4.0)
           + 2.0 * t2**2 / (n * ep_minus_ed)
           + 0.19 * n * J)

# Thermal hopping barrier
v = 0.19 * J

# Critical doping densities
x_AF_SG = 1.0 / n**2

epsilon_link = 0.19 * J
epsilon_bond = 0.75 * J

term1 = epsilon_link / (4 * t1)
term2 = (3 * epsilon_link) / (4 * t1 + 8 * n * epsilon_link)
x_SG_L = max(term1, term2)

x_L_A = epsilon_bond / (4 * t1)

# Write results JSON
output = {
    "n": n,
    "Delta_E": Delta_E,
    "v": v,
    "x_AF_SG": x_AF_SG,
    "x_SG_L": x_SG_L,
    "x_L_A": x_L_A
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(output, f, indent=2)
