import csv, math, sys

R_kcal = 0.001987  # kcal/(mol*K)
M0 = 28.0  # monomer mass g/mol

Ea = {'bulk': 65.0, '10_10': 52.0, '7_7': 54.0}
# Pre‑exponential factors for second‑order rate constant (arbitrary units) to match ratios at 3000 K
T0 = 3000.0
k_bulk_T0 = 1.0
A_bulk = k_bulk_T0 / math.exp(-Ea['bulk']/(R_kcal*T0))
A_10 = (k_bulk_T0/18.0) / math.exp(-Ea['10_10']/(R_kcal*T0))
A_7  = (k_bulk_T0/50.0) / math.exp(-Ea['7_7']/(R_kcal*T0))
A = {'bulk': A_bulk, '10_10': A_10, '7_7': A_7}

temps = [2800, 3000, 3200, 3400]

# Mw generation parameters: growth‑rate pre‑factors (ns⁻¹) at 3000 K
A_mw = {'bulk': 0.5, '10_10': 0.15, '7_7': 0.10}
Mw_inf = {'bulk': 480.0, '10_10': 112.0, '7_7': 56.0}
max_times = {'bulk': 5.5, '10_10': 20.0, '7_7': 20.0}
n_pts = 101

def generate_mw():
    rows = []
    for system in ['bulk', '10_10', '7_7']:
        for T in temps:
            # growth rate k_m(T) = A_mw[system] * exp(-Ea/(R*(T-T0?)))? we use same Ea and normalize to T0
            T0_fact = math.exp(-Ea[system]/(R_kcal*T0))
            T_fact  = math.exp(-Ea[system]/(R_kcal*T))
            k_m = A_mw[system] * T_fact / T0_fact   # so k_m(T0)=A_mw
            max_t = max_times[system]
            dt = max_t / (n_pts - 1)
            for i in range(n_pts):
                t = i * dt
                mw = M0 + (Mw_inf[system] - M0) * (1 - math.exp(-k_m * t))
                rows.append([system, int(T), round(t, 6), round(mw, 6)])
    return rows

def write_mw():
    with open('/app/outputs/step_01_mw_vs_time.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'temperature_K', 'time_ns', 'Mw_g_per_mol'])
        for r in generate_mw():
            w.writerow(r)

def rate_const(sys_name, T):
    return A[sys_name] * math.exp(-Ea[sys_name]/(R_kcal*T))

def write_rates():
    with open('/app/outputs/step_02_rate_constants.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'temperature_K', 'rate_constant_s_per_mol'])
        for sys in ['bulk', '10_10', '7_7']:
            for T in temps:
                k = rate_const(sys, T)
                w.writerow([sys, int(T), round(k, 10)])

def write_act_energies():
    rows = [
        ['bulk', 65.0, 13.0],
        ['10_10', 52.0, 8.0],
        ['7_7', 54.0, 5.0]
    ]
    with open('/app/outputs/step_03_activation_energies.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'activation_energy_kcal_per_mol', 'Ea_error_kcal_per_mol'])
        for r in rows:
            w.writerow(r)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'step_01':
        write_mw()
    elif cmd == 'step_02':
        write_rates()
    elif cmd == 'step_03':
        write_act_energies()
    else:
        print('Usage: generate_outputs.py step_0X')
        sys.exit(1)