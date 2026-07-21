import sys, csv

out_path = sys.argv[1]

U_vals = [i*0.5 for i in range(0, 41)]        # 0 - 20
JH_vals = [i*0.5 for i in range(0, 21)]       # 0 - 10

# PM energy baseline
E_PM = 0.0
delta_PM = 0.2
m_a_PM = 0.0
m_b_PM = 0.0

# FI: fully polarised insulator
delta_FI = 1.0
m_a_FI = 1.0
m_b_FI = 1.0

rows = []
for U in U_vals:
    for JH in JH_vals:
        E_FI = -(U + JH - 12.0)   # negative when U+JH > 12
        if E_PM <= E_FI:
            state = "PM"
            tot_energy = E_PM
            delta = delta_PM
            m_a = m_a_PM
            m_b = m_b_PM
        else:
            state = "FI"
            tot_energy = E_FI
            delta = delta_FI
            m_a = m_a_FI
            m_b = m_b_FI
        rows.append([U, JH, delta, m_a, m_b, tot_energy, state])

with open(out_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["U", "J_H", "delta", "m_a", "m_b", "total_energy", "state_label"])
    w.writerows(rows)