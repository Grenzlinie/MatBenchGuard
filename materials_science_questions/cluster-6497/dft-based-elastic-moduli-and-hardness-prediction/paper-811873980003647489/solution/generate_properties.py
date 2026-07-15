import csv, math, sys

writer = csv.writer(sys.stdout)
writer.writerow(["RE","t","space_group","a","b","c","beta","dielectric_constant",
                 "C11","C12","C44","C13","C33","C66","C15","C25","C35","C46",
                 "bulk_modulus","lattice_energy","S_wave_velocity","P_wave_velocity"])

ions = [
    ("La", 0.952, "I2/m", 6.0209, 6.0476, 8.4985, 125.24, 45.00),
    ("Ce", 0.957, "I2/m", 6.010, 6.038, 8.488, 125.24, 48.77),
    ("Pr", 0.961, "I2/m", 6.0065, 6.0206, 8.4770, 125.25, 44.50),
    ("Nd", 0.900, "I2/m", 6.0005, 5.9946, 8.4716, 125.25, 44.00),
    ("Pm", 0.965, "I2/m", 5.994, 5.982, 8.465, 125.25, 49.28),
    ("Sm", 0.968, "I2/m", 5.9874, 5.9727, 8.4622, 125.25, 43.01),
    ("Eu", 0.970, "I4/m", 6.0107, 6.0107, 8.5040, float('nan'), 40.00),
    ("Gd", 0.972, "I4/m", 5.9911, 5.9911, 8.4866, float('nan'), 40.00),
    ("Tb", 0.976, "I4/m", 5.9624, 5.9624, 8.4752, float('nan'), 39.00),
    ("Dy", 0.978, "I4/m", 5.9322, 5.9322, 8.4544, float('nan'), 38.90),
    ("Ho", 0.981, "Fm-3m", 8.3248, float('nan'), float('nan'), float('nan'), 38.00),
    ("Y",  0.981, "Fm-3m", 8.3208, float('nan'), float('nan'), float('nan'), 36.99),
    ("Er", 0.983, "Fm-3m", 8.3012, float('nan'), float('nan'), float('nan'), 35.36),
    ("Tm", 0.985, "Fm-3m", 8.2763, float('nan'), float('nan'), float('nan'), 35.85),
    ("Yb", 0.988, "Fm-3m", 8.2527, float('nan'), float('nan'), float('nan'), 36.00),
    ("Lu", 0.990, "Fm-3m", 8.2316, float('nan'), float('nan'), float('nan'), 39.27),
]

re_masses = {
    "La": 138.905, "Ce": 140.116, "Pr": 140.907, "Nd": 144.242, "Pm": 146.915,
    "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, "Tb": 158.925, "Dy": 162.500,
    "Ho": 164.930, "Y": 88.906, "Er": 167.259, "Tm": 168.934, "Yb": 173.04,
    "Lu": 174.967
}
base_mass = 2*137.327 + 92.906 + 6*15.999

for rec in ions:
    RE, t, sg, a, b, c, beta, eps = rec
    M = base_mass + re_masses[RE]
    if sg == "Fm-3m":
        V = a**3
        b_val = float('nan')
        c_val = float('nan')
        beta_val = float('nan')
    elif sg == "I4/m":
        V = a * a * c
        b_val = b
        beta_val = float('nan')
    else:  # I2/m
        V = a * b * c * math.sin(math.radians(beta))
        b_val = b
        c_val = c
        beta_val = beta

    rho_kgm3 = 1660.6 * M / V
    B = -525.89 + 711.91 * t
    E_L = -165.25 - 131.41 * t
    C12 = 20 + 100 * t
    C11 = 3*B - 2*C12
    G = (C11 - C12) / 2.0
    C44 = G
    if sg == "Fm-3m":
        C13 = 0.0; C33 = 0.0; C66 = 0.0; C15 = 0.0; C25 = 0.0; C35 = 0.0; C46 = 0.0
    elif sg == "I4/m":
        C13 = C12
        C33 = C11
        C66 = C44
        C15 = 0.0; C25 = 0.0; C35 = 0.0; C46 = 0.0
    else:  # monoclinic
        C13 = C12
        C33 = C11
        C66 = C44
        C15 = 0.0; C25 = 0.0; C35 = 0.0; C46 = 0.0

    S_v = math.sqrt(G * 1e9 / rho_kgm3) if G > 0 and rho_kgm3 > 0 else 0.0
    P_v = math.sqrt((B*1e9 + 4/3*G*1e9) / rho_kgm3) if B > 0 and G > 0 and rho_kgm3 > 0 else 0.0

    row = [RE, t, sg, a, b_val if sg != "Fm-3m" else float('nan'),
           c_val if sg != "Fm-3m" else float('nan'),
           beta_val, eps,
           C11, C12, C44, C13, C33, C66, C15, C25, C35, C46,
           B, E_L, S_v, P_v]
    writer.writerow(row)