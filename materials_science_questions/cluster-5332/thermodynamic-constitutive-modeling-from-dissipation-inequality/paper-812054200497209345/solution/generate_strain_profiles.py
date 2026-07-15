import math
import csv

# Parameters from the instruction
E1 = 200e9
M1 = 1e-6
H1 = 20e9
J1 = 1e-6
E2 = 100e9
M2 = 5e-7
H2 = 10e9
J2 = 5e-7
sigma = 300e6
sigma_y = 250e6

# Internal lengths
ell1 = math.sqrt(M1 / E1)
ell2 = math.sqrt(M2 / E2)
ell1p = math.sqrt(J1 / H1)
ell2p = math.sqrt(J2 / H2)

# Common factors
Omega_e = (E2 - E1) / (E1 * ell1 + E2 * ell2)
Omega_p = (H2 - H1) / (H1 * ell1p + H2 * ell2p)

# Determine x range based on maximum internal length
max_ell = max(ell1, ell2, ell1p, ell2p)
x_min = -5 * max_ell
x_max = 5 * max_ell

# Number of points per case (must be at least 500)
n = 500
xs = [x_min + i * (x_max - x_min) / (n - 1) for i in range(n)]

# Helper to compute strain for general case
# For x >= 0
def general_x_pos(x):
    ee = (sigma / E1) * (1.0 - Omega_e * ell2 * math.exp(-x / ell1))
    ep = ((sigma - sigma_y) / H1) * (1.0 - Omega_p * ell2p * math.exp(-x / ell1p))
    return ee, ep

# For x <= 0
def general_x_neg(x):
    ee = (sigma / E2) * (1.0 + Omega_e * ell1 * math.exp(x / ell2))   # x is negative
    ep = ((sigma - sigma_y) / H2) * (1.0 + Omega_p * ell1p * math.exp(x / ell2p))
    return ee, ep

# Case1: rigid gradient substrate (x>=0: kinematic HO, x<0: 0)
def case1_x_pos(x):
    ee = (sigma / E1) * (1.0 - math.exp(-x / ell1))
    ep = ((sigma_var - sigma_y) / H1) * (1.0 - math.exp(-x / ell1p))
    return ee, ep

# Case2: rigid local substrate (x>0: uniform strains)
def case2_x_pos(x):
    ee = sigma / E1
    ep = (sigma - sigma_y) / H1
    return ee, ep

# Case3: mixed local-elastic + gradient-plastic (x>0: elastic uniform, plastic exponential)
def case3_x_pos(x):
    ee = sigma / E1
    ep = ((sigma - sigma_y) / H1) * (1.0 - math.exp(-x / ell1p))
    return ee, ep

# Write CSV
with open('/app/outputs/strain_profiles.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['case', 'x', 'epsilon_e', 'epsilon_p'])
    
    # General case
    for x in xs:
        if x >= 0:
            ee, ep = general_x_pos(x)
        else:
            ee, ep = general_x_neg(x)
        writer.writerow(['general', x, ee, ep])
    
    # Case1
    for x in xs:
        if x >= 0:
            ee, ep = case1_x_pos(x)
        else:
            ee, ep = 0.0, 0.0
        writer.writerow(['case1', x, ee, ep])
    
    # Case2
    for x in xs:
        if x > 0:
            ee, ep = case2_x_pos(x)
        elif x == 0:
            # at x=0, we can use the same uniform value (continuous)
            ee, ep = case2_x_pos(x)
        else:
            ee, ep = 0.0, 0.0
        writer.writerow(['case2', x, ee, ep])
    
    # Case3
    for x in xs:
        if x >= 0:
            ee, ep = case3_x_pos(x)
        else:
            ee, ep = 0.0, 0.0
        writer.writerow(['case3', x, ee, ep])