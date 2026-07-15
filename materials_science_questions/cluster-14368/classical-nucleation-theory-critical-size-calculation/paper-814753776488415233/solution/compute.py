import json
import math

PI = math.pi
sigma = 500.0          # dyn/cm
Lambda = 2.0
d0_nm = 1.0
d0_cm = 1.0e-7
E0_Vcm = 1.0e6         # V/cm, convert to statV/cm (CGS)
E0_statVcm = E0_Vcm / 299.792458
epsilon = 1.0

# Critical length h0 (cm) and nucleation barrier W (erg, eV)
h0_cm = math.sqrt((PI * sigma * Lambda * d0_cm) / (epsilon * (E0_statVcm ** 2)))
h0_nm = h0_cm * 1.0e7
W_erg = (2.0/3.0) * PI * sigma * d0_cm * h0_cm
eV_to_erg = 1.602176634e-12
W_eV = W_erg / eV_to_erg

# Mobility b = D/(kT)
k = 1.380649e-16       # erg/K
T = 300.0
D = 1.0e-18            # cm^2/s
kT = k * T
b = D / kT

E0_sq = E0_statVcm ** 2

# Incubation time t0 (Eq.21)
t0_s = (3 * Lambda) / (b * epsilon * E0_sq * h0_cm)

# Characteristic growth time tL and growth rate (Eq.22)
L_cm = 3.0 * 1.0e-4   # 3 um -> cm
tL_s = (3 * Lambda) / (b * epsilon * E0_sq * L_cm)
growth_rate_cm_per_s = L_cm / tL_s
growth_rate_Angstrom_per_s = growth_rate_cm_per_s * 1.0e8  # 1 cm = 1e8 Å

# Probability density g(h/L), find peak
beta = 1.0
gamma = 0.15

def g(x):
    if x <= 0:
        return 0.0
    tmp = (1 + math.sqrt(1 + x*x)) ** 2 / (4 * math.sqrt(1 + x*x))
    return x * math.exp(-gamma * (x * math.log(tmp)) ** 2)

# scan with coarse then fine steps
best_x = 0.1
best_val = g(best_x)
step = 1e-4
x = 0.1 + step
while x <= 20.0:
    v = g(x)
    if v > best_val:
        best_val, best_x = v, x
    x += step

fine_step = 1e-6
low = max(0.1, best_x - 0.01)
high = best_x + 0.01
x = low
while x <= high:
    v = g(x)
    if v > best_val:
        best_val, best_x = v, x
    x += fine_step

distribution_peak_h_over_L = best_x

result = {
    "W_eV": W_eV,
    "h0_nm": h0_nm,
    "t0_s": t0_s,
    "tL_s": tL_s,
    "growth_rate_Angstrom_per_s": growth_rate_Angstrom_per_s,
    "distribution_peak_h_over_L": distribution_peak_h_over_L
}

print(json.dumps(result))
