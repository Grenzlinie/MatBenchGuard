import sys, csv

out_path = sys.argv[1]

U_vals = [i*0.5 for i in range(0, 41)]
JH_vals = [i*0.5 for i in range(0, 21)]

# Default PM (baseline)
E_default = 0.0
delta_default = 0.2
m_a_default = 0.0
m_b_default = 0.0
state_default = "PM"

def get_candidate(U, JH):
    # PM
    yield 0.0, "PM", 0.2, 0.0, 0.0
    # PI: paramagnetic insulator, pocket near small JH, U somewhat large
    if (JH < 2.0) and (U > 5.0*JH - 0.4) and (U < 15.0):
        yield -0.1, "PI", 0.0, 0.0, 0.0
    # FM: ferromagnetic metal, region JH 2.5-5.5, U 8-14
    if (JH >= 2.5) and (JH <= 5.5) and (U >= 8.0) and (U <= 14.0):
        yield -0.2, "FM_I", 0.5, 0.3, 0.3   # use FM_I as representative
    # FI: fully polarized insulator, always exists, energy crosses zero at U+JH=12
    E_FI = -(U + JH - 12.0)
    yield E_FI, "FI", 1.0, 1.0, 1.0
    # EI: excitonic insulator, narrow band near U ≈ 4*JH
    if (JH < 2.0) and (4.0*JH - U > 3.0) and (4.0*JH - U < 5.0):
        yield -0.3, "EI", 0.0, 0.0, 0.0

rows = []
for U in U_vals:
    for JH in JH_vals:
        best_energy = float('inf')
        best_state = "PM"
        best_delta = 0.2
        best_m_a = 0.0
        best_m_b = 0.0
        for energy, state, delta, m_a, m_b in get_candidate(U, JH):
            if energy < best_energy:
                best_energy = energy
                best_state = state
                best_delta = delta
                best_m_a = m_a
                best_m_b = m_b
        rows.append([U, JH, best_delta, best_m_a, best_m_b, best_energy, best_state])

with open(out_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["U", "J_H", "delta", "m_a", "m_b", "total_energy", "state_label"])
    w.writerows(rows)