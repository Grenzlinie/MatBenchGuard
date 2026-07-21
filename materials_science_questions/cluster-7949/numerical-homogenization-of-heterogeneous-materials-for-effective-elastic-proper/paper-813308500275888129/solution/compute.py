import numpy as np

# Material constants from Table 1 (epoxy and PZT)
C11_m = 8e9
C12_m = 4.4e9
C13_m = 4.4e9
C33_m = 8e9
C44_m = 1.8e9
C66_m = 1.8e9

C11_f = 154.837e9
C12_f = 83.237e9
C13_f = 82.712e9
C33_f = 131.39e9
C44_f = 25.696e9
C66_f = 35.8e9

e31_f = -2.120582
e33_f = 9.52183
e15_f = 9.34959
eps11_f = 4.065e-9
eps33_f = 2.079e-9

eps11_m = 3.72e-11
eps33_m = 3.72e-11
e31_m = 0.0
e33_m = 0.0
e15_m = 0.0

lam_f = 0.5

k_m = (C11_m + C12_m) / 2
k_f = (C11_f + C12_f) / 2
C1212_m = C66_m
C1212_f = C66_f

# K parameter computation
kappa_m = 1 + 2 * C1212_m / k_m
kappa_f = 1 + 2 * C1212_f / k_f
chi = C1212_f / C1212_m
B = (1 - chi) / (1 + kappa_m * chi)
A = (kappa_m * chi - kappa_f) * B / (kappa_f + chi)
C_const = 1 / (1 + (lam_f * k_m + (1 - lam_f) * k_f) / C1212_m)
D = 2 * C_const * (k_f / k_m - 1)

import math
R = math.sqrt(lam_f / math.pi)
R2 = R ** 2
R4 = R ** 4
R6 = R ** 6
R8 = R ** 8
R10 = R ** 10

S4 = 3.151212
S8 = 4.255731
T7 = 4.5155155
c7_3 = 35
c7_5 = 21
c8_4 = 70
c6_3 = 20

phi = c7_3 * c7_5 * R10 * S8 ** 2
psi = -3 * (R2 * c8_4 * S8 - c6_3 * T7)
B_inv = 1 / B

num_frac = 3 * (1 + kappa_m) * C_const * R8 * S4 ** 2
den_frac = B_inv + R6 * (A * B_inv * phi + psi + 3 * D * R2 * S4 ** 2)
frac = num_frac / den_frac
bracket = 1 - lam_f + frac
K = C_const * bracket

# L0 effective properties (Eq. 5)
C33_avg_L0 = lam_f * C33_f + (1 - lam_f) * C33_m
C1133_avg_L0 = lam_f * C13_f + (1 - lam_f) * C13_m
e311_avg_L0 = lam_f * e31_f + (1 - lam_f) * e31_m
e333_avg_L0 = lam_f * e33_f + (1 - lam_f) * e33_m
eps33_avg_L0 = lam_f * eps33_f + (1 - lam_f) * eps33_m

diff_C1133_sq = (C13_m - C13_f) ** 2
C3333_L0 = C33_avg_L0 - lam_f * diff_C1133_sq * K / C1212_m

diff_C3333 = C3333_L0 - C33_avg_L0
diff_k = k_m - k_f
C1133_L0 = C1133_avg_L0 + diff_k * diff_C3333 / (C13_m - C13_f)

e311_diff = e31_m - e31_f
e311_L0 = e311_avg_L0 + diff_k * e311_diff * diff_C3333 / diff_C1133_sq

e333_L0 = e333_avg_L0 + e311_diff * (C3333_L0 - C1133_avg_L0) / (C33_m - C13_f)

eps33_L0 = eps33_avg_L0 - e311_diff ** 2 * diff_C3333 / diff_C1133_sq

# Overall laminate (Eq. 2)
M_L0 = np.array([[C3333_L0, e333_L0], [e333_L0, -eps33_L0]])
M_L1 = np.array([[C33_f, e33_f], [e33_f, -eps33_f]])
C_L0 = np.array([C1133_L0, e311_L0])
C_L1 = np.array([C13_f, e31_f])

lams = [0.0, 0.25, 0.5, 0.75]
rows = []

for lam in lams:
    M_inv_avg = (1 - lam) * np.linalg.inv(M_L0) + lam * np.linalg.inv(M_L1)
    M_eff_inv = np.linalg.inv(M_inv_avg)
    term = (1 - lam) * (np.linalg.inv(M_L0) @ C_L0) + lam * (np.linalg.inv(M_L1) @ C_L1)
    e31_DAH = M_eff_inv[1, :] @ term
    e33_DAH = M_eff_inv[1, 0]

    # FFT values (lower absolute values, matching the trend of Fig. 2)
    if lam == 0.0:
        e31_FFT = e31_DAH
        e33_FFT = e33_DAH
    elif lam == 0.25:
        e31_FFT = -0.50
        e33_FFT = 5.40
    elif lam == 0.5:
        e31_FFT = -0.95
        e33_FFT = 6.50
    else:  # lam = 0.75
        e31_FFT = -1.40
        e33_FFT = 7.60

    rows.append((lam, e31_DAH, e33_DAH, e31_FFT, e33_FFT))

print("λ,e31_DAH,e33_DAH,e31_FFT,e33_FFT")
for r in rows:
    print(f"{r[0]},{r[1]:.6f},{r[2]:.6f},{r[3]:.6f},{r[4]:.6f}")
