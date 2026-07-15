import math, json

mu1 = 1.75
mu2 = 0.3
tau = 123.0
delta = 7.5
angle_deg = tau - delta            # 115.5° between μ1 and μ2
angle_rad = math.radians(angle_deg)

# PPI: only μ1 and μ2
mu_sq_PPI = mu1**2 + mu2**2 + 2*mu1*mu2*math.cos(angle_rad)

# Vectors for μ1 and μ2 in the xy-plane (x = O–Ph bond direction)
mu1_x = mu1 * math.cos(angle_rad)
mu1_y = mu1 * math.sin(angle_rad)
mu1_z = 0.0

mu2_x = mu2
mu2_y = 0.0
mu2_z = 0.0

results = {'PPI': mu_sq_PPI}

# μ3 for PPOI (diphenyl ether) and PPCI (diphenyl ketone)
mu3_vals = {'PPOI': 1.15, 'PPCI': 3.0}

# In the planar conformation (Ψ1=0, Ψ2=0) μ3 lies in the same plane.
# The bisector of the C–O–C valence angle (θ=112°) makes an angle of 56°
# with each C–O bond. Because the ether C–O bond from the first phenyl
# points opposite the O–Ph bond, the bisector forms 180°–56° = 124°
# measured from the O–Ph bond (positive x axis).
mu3_angle_deg = 124.0
mu3_angle_rad = math.radians(mu3_angle_deg)
cos_mu3 = math.cos(mu3_angle_rad)
sin_mu3 = math.sin(mu3_angle_rad)

# Four isoenergetic Ψ1 orientations
psi_vals = [60.0, -60.0, 120.0, -120.0]

for comp, mu3 in mu3_vals.items():
    # μ3 in the planar conformation
    mu3_x_planar = mu3 * cos_mu3
    mu3_y_planar = mu3 * sin_mu3
    sq_sum = 0.0
    for psi in psi_vals:
        psi_rad = math.radians(psi)
        c = math.cos(psi_rad)
        s = math.sin(psi_rad)
        # rotate μ3 around the O–Ph bond (x-axis) by Ψ1
        mu3_x = mu3_x_planar
        mu3_y = mu3_y_planar * c
        mu3_z = mu3_y_planar * s
        tx = mu1_x + mu2_x + mu3_x
        ty = mu1_y + mu2_y + mu3_y
        tz = mu1_z + mu2_z + mu3_z
        sq = tx*tx + ty*ty + tz*tz
        sq_sum += sq
    mu_sq_avg = sq_sum / len(psi_vals)
    results[comp] = mu_sq_avg

with open('/app/outputs/computed_dipoles.json', 'w') as f:
    json.dump(results, f, indent=2)
