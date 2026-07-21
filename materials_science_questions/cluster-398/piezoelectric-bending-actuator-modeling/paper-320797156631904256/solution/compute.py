import math, csv

sigma0 = 1.0e8
epsilon0 = 8.854187817e-12
epsilon = 10.0 * epsilon0
q = 1.602176634e-19
Omega = 1.0e-29
gamma_val = 1.0e-12
a_D = 1.0e-7
lam = 1.0e3
nu = 0.9
delta = 1.0e-6
Gamma_s = 1.0e3 * a_D
K_I = 1.0e6
K_II = 1.0e6

omega = 1.0e6
tau_sigma = 1.0e-3
rho = 5.0e3
c_t = 3.0e3
C11 = 1.2e11
C12 = 0.6e11
C44 = 0.6e11

sqrt3 = math.sqrt(3.0)
sqrt2 = math.sqrt(2.0)
n_vec = [1/sqrt3, 1/sqrt3, 1/sqrt3]
m_vec = [1/sqrt2, -1/sqrt2, 0.0]
e_vec = m_vec

def contract_gamma_full(A, B):
    return (A[0] * gamma_val * (B[1][2] + B[2][1]) +
            A[1] * gamma_val * (B[2][0] + B[0][2]) +
            A[2] * gamma_val * (B[0][1] + B[1][0]))

def contract_gamma_sym(A, Byz, Bzx, Bxy):
    return 2*gamma_val * (A[0]*Byz + A[1]*Bzx + A[2]*Bxy)

B_nn = [[n_vec[i]*n_vec[j] for j in range(3)] for i in range(3)]
B_nm = [[n_vec[i]*m_vec[j] for j in range(3)] for i in range(3)]
B_mm = [[m_vec[i]*m_vec[j] for j in range(3)] for i in range(3)]

C1 = contract_gamma_full(n_vec, B_nn)
C2 = contract_gamma_full(n_vec, B_mm)
C3 = contract_gamma_full(m_vec, B_nm)
C4 = contract_gamma_full(m_vec, B_nn)
C5 = contract_gamma_full(m_vec, B_mm)
C6 = contract_gamma_full(n_vec, B_nm)

sqrt_1mv2 = math.sqrt(1.0 - nu*nu)

A_I = [8.0/21.0, -8.0/15.0, 0.0]
B_I = [-2.0, -12.0/15.0, 0.0]
C_I = [-8.0/21.0, 8.0/15.0, 0.0]
D_I = [0.0, 0.0, -16.0/15.0]
E_I = [0.0, 0.0, -8.0/15.0]
F_I = [0.0, 0.0, -16.0/15.0]

A_II = [0.0, 0.0, 16.0/15.0]
B_II = [0.0, 0.0, -8.0/15.0]
C_II = [0.0, 0.0, -16.0/15.0]
D_II = [6.0/7.0, -44.0/15.0, 0.0]
E_II = [8.0/21.0, -8.0/15.0, 0.0]
F_II = [8.0/21.0, -8.0/15.0, 0.0]

gamma_I = [0.0, 0.0, 0.0]
gamma_II = [0.0, 0.0, 0.0]
for j in range(3):
    gamma_I[j] = C1*A_I[j] + C2*B_I[j] + C3*C_I[j] + sqrt_1mv2*(C4*D_I[j] + C5*E_I[j] + C6*F_I[j])
    gamma_II[j] = C1*A_II[j] + C2*B_II[j] + C3*C_II[j] + sqrt_1mv2*(C4*D_II[j] + C5*E_II[j] + C6*F_II[j])

eps_Omega_div_12piq = (epsilon * Omega) / (12.0 * math.pi * q)
Q_shock_dilat = sigma0 * eps_Omega_div_12piq
Q_shock_piezo = sigma0 * C1
Q_shock_total = Q_shock_dilat + Q_shock_piezo

D_shock_dilat = Q_shock_dilat
D_shock_piezo = Q_shock_piezo * lam * a_D
D_shock_total = D_shock_dilat + D_shock_piezo

eps_Omega_div_4piq = (epsilon * Omega) / (4.0 * math.pi * q)
sqrt2pi = math.sqrt(2.0*math.pi)
sqrt2pi_delta = math.sqrt(2.0*math.pi*delta)
sqrt_lam_delta_aD = math.sqrt(lam * delta * a_D)
sqrt_nu = math.sqrt(nu)
nu32 = nu * sqrt_nu
nu2 = nu*nu
lam_aD = lam * a_D

common_dilat_I = (3.0 * nu2 * K_I) / (5.0 * sqrt_1mv2 * sqrt2pi_delta)
Q_I_dilat = eps_Omega_div_4piq * common_dilat_I * (1.0 + (5.0/24.0) * sqrt_nu * sqrt_lam_delta_aD / Gamma_s)

factor_d1 = (3.0 * nu2 * K_I * lam_aD) / (5.0 * sqrt_1mv2 * sqrt2pi_delta)
D1_I_dilat = eps_Omega_div_4piq * factor_d1 * (nu + (5.0/21.0) * nu32 * sqrt_lam_delta_aD / Gamma_s - (50.0/21.0) * delta / lam_aD)

denom_d2 = (1.0 - nu2) * sqrt2pi_delta
D2_II_dilat = -eps_Omega_div_4piq * (10.0 * nu2 * K_II * lam_aD) / denom_d2 * (delta / lam_aD + (1.0/3.0) * sqrt_nu * sqrt_lam_delta_aD / Gamma_s)

factor_d1_II = (3.0 * nu2 * K_II * lam_aD) / (5.0 * sqrt_1mv2 * sqrt2pi_delta)
D1_II_dilat = eps_Omega_div_4piq * factor_d1_II * (nu + (5.0/21.0) * nu32 * sqrt_lam_delta_aD / Gamma_s - (50.0/21.0) * delta / lam_aD)

sqrt_aDlam = math.sqrt(a_D * lam)
pow_aDlam_32 = (a_D * lam) ** 1.5

factor_Q_piezo = a_D * sqrt_aDlam * sqrt_nu / (sqrt_1mv2 * 2.0 * sqrt2pi)
factor_D1_piezo = pow_aDlam_32 * nu32 / (sqrt_1mv2 * 2.0 * sqrt2pi)
factor_D2_piezo = pow_aDlam_32 * nu32 / ((1.0 - nu2) * 2.0 * sqrt2pi)

Q_I_piezo = gamma_I[0] * factor_Q_piezo * K_I
D1_I_piezo = (gamma_I[0] + gamma_I[1]) * factor_D1_piezo * K_I
D2_I_piezo = gamma_I[2] * factor_D2_piezo * K_I

Q_II_piezo = gamma_II[0] * factor_Q_piezo * (-K_II)
D2_II_piezo = gamma_II[2] * factor_D2_piezo * (-K_II)

Q_I_total = Q_I_dilat + Q_I_piezo
D1_I_total = D1_I_dilat + D1_I_piezo
D2_I_total = D2_I_piezo

Q_II_total = Q_II_piezo
D1_II_total = D1_II_dilat
D2_II_total = D2_II_dilat + D2_II_piezo

# sound absorption
n = n_vec
e = e_vec
S = [[0.0]*3 for _ in range(3)]
for mu in range(3):
    for nu in range(3):
        val = 0.0
        for alpha in range(3):
            for beta in range(3):
                if mu==nu and alpha==beta:
                    if mu==alpha:
                        val += C11 * n[alpha] * e[beta]
                    else:
                        val += C12 * n[alpha] * e[beta]
                elif mu==alpha and nu==beta:
                    val += C44 * n[alpha] * e[beta]
                elif mu==beta and nu==alpha:
                    val += C44 * n[alpha] * e[beta]
        S[mu][nu] = val

num = contract_gamma_full(n, S)
num_sq = num * num
denom = rho * c_t**3 * omega**2 * tau_sigma**2 + (1.0 + omega**2 * tau_sigma**2 / lam**2)**2
gamma_t = 2.0 * omega**2 * tau_sigma * num_sq / denom

with open('/app/outputs/results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['quantity', 'value', 'unit'])
    data = [
        ('Q_shock_dilat', Q_shock_dilat, 'C/m^2'),
        ('Q_shock_piezo', Q_shock_piezo, 'C/m^2'),
        ('Q_shock_total', Q_shock_total, 'C/m^2'),
        ('D_shock_dilat', D_shock_dilat, 'C/m'),
        ('D_shock_piezo', D_shock_piezo, 'C/m'),
        ('D_shock_total', D_shock_total, 'C/m'),
        ('Q_I_dilat', Q_I_dilat, 'C/m'),
        ('Q_I_piezo', Q_I_piezo, 'C/m'),
        ('Q_I_total', Q_I_total, 'C/m'),
        ('D1_I_dilat', D1_I_dilat, 'C/m'),
        ('D1_I_piezo', D1_I_piezo, 'C/m'),
        ('D1_I_total', D1_I_total, 'C/m'),
        ('D2_I_piezo', D2_I_piezo, 'C/m'),
        ('D2_I_total', D2_I_total, 'C/m'),
        ('Q_II_piezo', Q_II_piezo, 'C/m'),
        ('Q_II_total', Q_II_total, 'C/m'),
        ('D1_II_dilat', D1_II_dilat, 'C/m'),
        ('D1_II_total', D1_II_total, 'C/m'),
        ('D2_II_dilat', D2_II_dilat, 'C/m'),
        ('D2_II_piezo', D2_II_piezo, 'C/m'),
        ('D2_II_total', D2_II_total, 'C/m'),
        ('gamma_t', gamma_t, 'm^{-1}'),
    ]
    for row in data:
        writer.writerow(row)
