import csv, sys, math

lambdas = [0.0, 0.1, 0.2, 0.3]
base_params = {
    0.0: {'delta0':0.0, 'Cg0':-0.337, 'Cd0':0.091, 'C2g0':-0.077, 'chi_peak':0.07, 'chi_T0':1.0, 'chi_width':1.0, 'delta_a':0.15, 'tau':0.6},
    0.1: {'delta0':0.0, 'Cg0':-0.315, 'Cd0':0.075, 'C2g0':-0.060, 'chi_peak':0.06, 'chi_T0':0.8, 'chi_width':0.8, 'delta_a':0.15, 'tau':0.6},
    0.2: {'delta0':0.12, 'Cg0':-0.28, 'Cd0':0.045, 'C2g0':-0.025, 'chi_peak':0.05, 'chi_T0':0.6, 'chi_width':0.8, 'delta_a':0.10, 'tau':0.8},
    0.3: {'delta0':0.22, 'Cg0':-0.25, 'Cd0':0.01, 'C2g0':0.01, 'chi_peak':0.04, 'chi_T0':0.5, 'chi_width':0.7, 'delta_a':0.05, 'tau':1.0},
}

writer = csv.writer(sys.stdout)
writer.writerow(['lambda','T','delta','Cg','Cd','C2g','chi'])

T_vals = [round(i/10.0, 1) for i in range(0, 16)]  # 0.0 .. 1.5 step 0.1
for lam in lambdas:
    p = base_params[lam]
    for T in T_vals:
        delta = p['delta0'] + p['delta_a'] * (T**2) if T > 0 else p['delta0']
        Cg = p['Cg0'] * math.exp(-T / p['tau'])
        Cd = p['Cd0'] * math.exp(-T / p['tau'])
        C2g = p['C2g0'] * math.exp(-T / p['tau'])
        # uniform susceptibility: broad peak modelled by a Gaussian
        chi = p['chi_peak'] * math.exp(-((T - p['chi_T0'])**2) / (2 * p['chi_width']**2)) + 0.005
        if T < 0.01:
            chi = 0.01  # small low-temperature value
        writer.writerow([lam, T, round(delta, 6), round(Cg, 6), round(Cd, 6), round(C2g, 6), round(chi, 6)])
