import numpy as np
from scipy.linalg import eigh
import json, csv, os

# --- parameters from the paper ---
B4 = -20.8e-3  # meV
eta3 = 21.0    # meV
N = 1.227e28   # m^-3
C0 = 73.9      # GPa
s = 18.3       # GPa
TE = 783       # K
kB = 0.0861733 # meV/K

# --- build J=4 operators ---
Jdim = 9
J = 4
# Jz
Jz = np.diag(np.arange(J, -J-1, -1))
# J+ and J-
Jplus = np.zeros((Jdim, Jdim), dtype=complex)
for i, m in enumerate(np.arange(J, -J-1, -1)):
    if m+1 <= J:
        j = np.where(np.arange(J, -J-1, -1) == m+1)[0][0]
        Jplus[i, j] = np.sqrt((J-m)*(J+m+1))
Jminus = Jplus.T
Jx = 0.5 * (Jplus + Jminus)
Jy = -0.5j * (Jplus - Jminus)

# --- Stevens operators O4^0 and O4^4 for J=4 ---
Jz2 = Jz @ Jz
Jz4 = Jz2 @ Jz2
O40 = 35 * Jz4 - 575 * Jz2 + 1080 * np.eye(Jdim)   # 35 Jz^4 - (30 J(J+1)-25) Jz^2 + (3 J^2(J+1)^2 - 6 J(J+1)) I
Jplus4 = np.linalg.matrix_power(Jplus, 4)
Jminus4 = np.linalg.matrix_power(Jminus, 4)
O44 = 0.5 * (Jplus4 + Jminus4)

# CEF Hamiltonian at zero strain
Hcef = B4 * (O40 + 5 * O44)

# ---------- Step 1: CEF level scheme ----------
evals = np.sort(eigh(Hcef, eigvals_only=True))
evals_K = evals / kB

# group degeneracies (tolerance 0.2 K)
tol = 0.2
groups = []
for e in evals_K:
    found = False
    for grp in groups:
        if abs(np.mean(grp) - e) < tol:
            grp.append(e)
            found = True
            break
    if not found:
        groups.append([e])
# sort groups by mean energy
groups.sort(key=lambda g: np.mean(g))
# expected degeneracy order for negative B4: 1,3,2,3
irreps = ['Γ1', 'Γ4', 'Γ3', 'Γ5']
levels_list = []
for i, grp in enumerate(groups):
    degen = len(grp)
    irrep = irreps[i] if i < 4 else '?'
    for e in grp:
        levels_list.append({'energy_K': round(float(e), 6), 'degeneracy': degen, 'irrep': irrep})
levels_list.sort(key=lambda x: x['energy_K'])

with open('/app/outputs/cef_levels.json', 'w') as f:
    json.dump(levels_list, f, indent=2)

# ---------- Step 2: C55(T) ----------
# magnetoelastic coupling operator
strain_coupling = eta3 * (Jx @ Jy + Jy @ Jx)

# finite difference strain magnitude
delta = 1e-3

def get_evals(strain):
    H = Hcef + strain * strain_coupling
    return np.sort(eigh(H, eigvals_only=True))

ev0 = get_evals(0.0)
ev_p = get_evals(delta)
ev_m = get_evals(-delta)

# first and second derivatives of each eigenvalue
dE_de = (ev_p - ev_m) / (2 * delta)
d2E_de2 = (ev_p + ev_m - 2 * ev0) / (delta ** 2)

# temperatures to evaluate
temps = [50, 100, 150, 200, 250, 300]
# conversion factor: ΔC55 (in GPa) = N * [bracket in meV] * 1.602176634e-22 (J/meV) / 1e9
conv_factor = N * 1.602176634e-31

outrows = []
for T in temps:
    beta = 1.0 / (kB * T)
    exp_vals = np.exp(-beta * ev0)
    Z = np.sum(exp_vals)
    term1 = np.sum(d2E_de2 * exp_vals)
    term2 = - (1.0 / (kB * T)) * np.sum((dE_de ** 2) * exp_vals)
    bracket = (term1 + term2) / Z   # units: meV
    Delta_C55 = conv_factor * bracket   # GPa
    Cbg = C0 - s / (np.exp(TE / T) - 1.0)
    C55_total = Cbg + Delta_C55
    outrows.append([T, C55_total])

with open('/app/outputs/c55_curve.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T_K', 'C55_GPa'])
    for row in outrows:
        writer.writerow(row)
