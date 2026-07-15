import csv, math
import numpy as np
from scipy.optimize import minimize, Bounds, LinearConstraint

def f0_gamma(gamma):
    # hard-sphere f0(γ) from cell-model: diverges at η_cp=0.74, unstable below 0.46
    if gamma < 0.46:
        return 1000.0
    if gamma >= 0.74:
        gamma = 0.74 - 1e-12
    return -3.0 * math.log(1.0 - gamma / 0.74) + 2.0844

def free_energy(z, w, eta, t):
    if z < 0 or w < 0 or z + w > 1.0001:
        return 1e8
    denom = 1.0 + z + 2.0 * w
    gamma = eta / denom
    f0 = f0_gamma(gamma)
    term2 = (z + 3.0 * w) / denom * (1.0 / t)
    term3 = (z * math.log(2.0) + w * math.log(6.0)) / denom
    s = 1.0 - z - w
    mix = 0.0
    if z > 0:
        mix += z * math.log(z)
    if w > 0:
        mix += w * math.log(w)
    if s > 0:
        mix += s * math.log(s)
    mix /= denom
    return f0 + term2 + term3 + mix

# build condition list
eta_scan = [round(0.5 + i*0.05, 3) for i in range(31)]   # 0.5 .. 2.0 step 0.05
conditions = []
for eta in eta_scan:
    conditions.append((eta, 0.05))
conditions.append((0.8, 0.1))

results = []
for eta, t in conditions:
    # initial guess tailored to regime
    if t == 0.05:
        if eta <= 0.74:
            x0 = np.array([0.0, 0.0])
        elif eta <= 1.5:
            x0 = np.array([0.3, 0.0])
        else:
            x0 = np.array([0.7, 0.15])
    else:
        x0 = np.array([0.3, 0.0])

    bounds = Bounds([0.0, 0.0], [1.0, 1.0])
    cons = LinearConstraint([[1.0, 1.0]], [0.0], [1.0])
    res = minimize(lambda x: free_energy(x[0], x[1], eta, t), x0,
                   method='SLSQP', bounds=bounds, constraints=cons,
                   options={'maxiter': 2000, 'ftol': 1e-12})
    z_opt, w_opt = res.x
    f_opt = free_energy(z_opt, w_opt, eta, t)
    results.append([eta, t, round(z_opt, 10), round(w_opt, 10), round(f_opt, 10)])

with open('/app/outputs/clustering_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['eta', 't', 'z', 'w', 'free_energy_per_particle'])
    for row in results:
        writer.writerow(row)
