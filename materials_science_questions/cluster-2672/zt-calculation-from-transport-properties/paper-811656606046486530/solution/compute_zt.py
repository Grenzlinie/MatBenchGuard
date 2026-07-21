import sys
import math

k_B = 8.617333262145e-5   # eV/K
T = 1200.0
kT = k_B * T
b_opt = 2.4
D_opt = math.exp(b_opt) / (math.exp(b_opt) + 1.0) ** 2
denom = D_opt * b_opt * b_opt   # D(2.4)*(2.4)^2

def compute_zt(e_peak):
    b = e_peak / kT
    D = math.exp(b) / (math.exp(b) + 1.0) ** 2
    return 14.0 * D * b * b / denom

if __name__ == "__main__":
    e_peak = float(sys.argv[1])
    zt = compute_zt(e_peak)
    print(zt)
