import json, math, csv
import numpy as np
from scipy.linalg import eigh

with open("/app/outputs/host_params.json", "r") as f:
    host = json.load(f)
A = host["A"]
B = host["B"]

r0_cm = 2.282e-8
e_esu = 4.803e-10
e2 = e_esu * e_esu
u = 1.660539e-24
M_Cs = 132.9 * u
M_H = 1.0 * u
M_D = 2.0 * u

neighbours_signs = [
    (1,1,1),
    (-1,-1,-1),
    (-1,1,1),
    (1,-1,-1),
    (1,-1,1),
    (-1,1,-1),
    (1,1,-1),
    (-1,-1,1)
]

impurities = [("H", M_H), ("D", M_D)]
A_prime_values = [4.7452, 4.0, 3.0, 2.0, 1.0, 0.5]

results = []
for imp_name, M0 in impurities:
    for Ap in A_prime_values:
        masses = [M0] + [M_Cs]*8
        pos = [np.zeros(3)] + [np.array(s)*r0_cm for s in neighbours_signs]
        charge_factor = [-1 if i==0 else 1 for i in range(9)]
        D = np.zeros((27,27))

        # Coulomb
        for i in range(9):
            for j in range(i+1,9):
                r_vec = pos[j] - pos[i]
                r = np.linalg.norm(r_vec)
                qprod = charge_factor[i] * charge_factor[j]
                coeff = - qprod * e2 / (r**3)
                M_factor = 1.0 / math.sqrt(masses[i]*masses[j])
                for a in range(3):
                    for ap in range(3):
                        val = M_factor * coeff * ( (r_vec[a]*r_vec[ap]/(r*r)) - (1 if a==ap else 0) )
                        D[3*i+a, 3*j+ap] += val
                        D[3*j+ap, 3*i+a] += val

        # Short-range on-site
        diag_imp = (1.0 / M0) * (e2 / (8.0 * r0_cm**3)) * (8.0/3.0) * (Ap + 2.0*B)
        for a in range(3):
            D[3*0+a, 3*0+a] += diag_imp
        M_neigh = M_Cs
        diag_neigh = (1.0 / M_neigh) * (e2 / (8.0 * r0_cm**3)) * (1.0/3.0) * (Ap + 7.0*A + 16.0*B)
        for l in range(1,9):
            for a in range(3):
                D[3*l+a, 3*l+a] += diag_neigh

        # Short-range impurity-neighbour
        for l in range(1,9):
            s = np.array(neighbours_signs[l-1])
            M_sqrt = 1.0 / math.sqrt(M0 * M_neigh)
            for a in range(3):
                for ap in range(3):
                    val = - M_sqrt * (e2 / (8.0 * r0_cm**3)) * ( (Ap - B) * (s[a]*s[ap]) / 3.0 + B * (1 if a==ap else 0) )
                    D[3*0+a, 3*l+ap] += val
                    D[3*l+ap, 3*0+a] += val

        eigenvalues, _ = eigh(D)
        max_omega2 = np.max(eigenvalues)
        if max_omega2 < 0:
            omega = 0.0
        else:
            omega = math.sqrt(max_omega2)
        omega_13 = omega * 1e-13
        results.append((Ap, imp_name, omega_13))

with open("/app/outputs/localized_frequencies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["A_prime", "impurity", "frequency"])
    for row in results:
        writer.writerow(row)
