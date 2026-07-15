import sys, math

R = 8.314462618  # J/mol/K
Theta_D = 380.0  # K
N_atoms_per_formula = 3
Cv_limit = 9 * R  # 74.826... J/mol/K

def debye_D(x):
    """Debye function D(x) = (3/x^3) * int_0^x t^4 e^t/(e^t-1)^2 dt"""
    if x <= 0:
        return 1.0
    if x > 20:
        # asymptotic limit 1
        return 1.0
    N = 2000   # integration steps
    dt = x / N
    integral = 0.0
    for i in range(N):
        t_low = i * dt
        t_high = (i+1) * dt
        t_mid = (t_low + t_high) / 2
        f_mid = (t_mid**4) * math.exp(t_mid) / (math.exp(t_mid) - 1)**2
        integral += f_mid * dt
    D = 3.0 * integral / (x**3)
    return D

def cv(T):
    if T <= 0:
        return 0.0
    x = Theta_D / T
    if x > 20:
        return Cv_limit  # low T approximation? Actually high T limit
    return Cv_limit * debye_D(x)

def entropy(T):
    # integrate Cv/T' dT' from Tmin to T
    Tmin = 0.1
    steps = 10000
    if T <= Tmin:
        return 0.0
    delta = (T - Tmin) / steps
    S = 0.0
    for i in range(steps):
        t1 = Tmin + i * delta
        t2 = t1 + delta
        tmid = (t1 + t2) / 2
        S += (cv(tmid) / tmid) * delta
    return S

# generate temperatures from 0 to 1500 K with at least 30 points
T_list = list(range(0, 1501, 50))  # 0,50,...,1500 -> 31 points
sys.stdout.write("temperature_K,entropy_J_per_mol_K,heat_capacity_Cv_J_per_mol_K\n")
for T in T_list:
    S_val = entropy(T)
    Cv_val = cv(T)
    sys.stdout.write(f"{T},{S_val:.4f},{Cv_val:.4f}\n")
