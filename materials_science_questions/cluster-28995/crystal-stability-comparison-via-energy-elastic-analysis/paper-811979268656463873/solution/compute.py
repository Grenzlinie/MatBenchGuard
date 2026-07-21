import csv

data = [
    # element, structure, C, N_free(3d), r1, r2, n1, n2, C_max, K
    ("Cu", "f.c.c.", 11, 9, 2.4151, 3.4154, 12, 6, 10, 1),
    ("Ni", "f.c.c.", 10, 8, 2.3543, 3.3295, 12, 6, 10, 1),
    ("Co", "f.c.c.", 9, 7, 2.3679, 3.3487, 12, 6, 10, 1),
    ("Fe", "f.c.c.", 8, 6, 2.4368, 3.4461, 12, 6, 10, 0),
    ("Mn", "f.c.c.", 7, 5, 2.440, 2.5227, 12, 6, 10, 0),
    ("Cr", "f.c.c.", 6, 5, 2.5605, 2.5680, 12, 6, 10, 0),
    ("Sc", "s.c. in f.c.c.", 3, 1, 3.062, 4.3302, 6, 6, 6, 0),
    ("Ti", "s.c. in f.c.c.", 4, 2, 2.754, 3.8941, 6, 6, 6, 0),
    ("V", "s.c. in f.c.c.", 5, 3, 2.478, 3.5036, 6, 6, 6, 0),
    ("Cr", "s.c. in f.c.c.", 6, 5, 2.5605, 2.5680, 6, 6, 6, 0),
]

rows = []
for el, struct, C, Nf, r1, r2, n1, n2, Cmax, K in data:
    # Effective radius R
    R = 0.065 * ((C/2)**2 - (4.75 + K)*(C - 8) + 5)
    # Effective nuclear charge
    Z = 9.0 / R
    # Overlap parameters
    b1 = 0.6780 * n1 * (r1 - R)
    b2 = 0.6780 * n2 * (r2 - R)
    # Fractional magnetic moment
    if struct == "f.c.c.":
        Dm = (3*Z - K*b1 - Cmax) / 2.0
    else:  # s.c. in f.c.c.
        Dm = (Z - Cmax) / 2.0 + b2
    # Total 3d electrons, method 8
    N8 = 8.0 + b1 - ((3*Z - K*b1)/2.0 - 5.0) * 0.1
    # Total 3d electrons, method 9
    N9 = Nf + Dm
    
    def ec_str(Ntot, Ctotal):
        x = round(Ntot, 1)
        y = round(Ctotal - x, 1)
        return f"3d^{x:.1f} 4s^{y:.1f}"
    
    ec8 = ec_str(N8, C)
    ec9 = ec_str(N9, C)
    
    rows.append([el, struct, f"{R:.4f}", f"{Z:.4f}", f"{b1:.4f}", f"{b2:.4f}",
                 f"{Dm:.4f}", f"{N8:.4f}", f"{N9:.4f}", ec8, ec9])

with open('/app/outputs/computed_properties.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        "element", "structure", "R", "Z3d", "b1", "b2",
        "Delta_m", "Ntot_8", "Ntot_9", "EC_8", "EC_9"
    ])
    writer.writerows(rows)
