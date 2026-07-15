import numpy as np
from scipy.integrate import quad

# Constants
k_B = 1.380649e-23  # J/K
hbar = 1.054571817e-34  # J·s
Theta = 141.0
alpha = 1.0
Theta1 = 57.0   # K
Theta2 = 95.0   # K
Theta3 = 145.0  # K
Theta4 = 100.0  # K
V_T1 = 1.98e5 * 1e-2  # m/s (1980)
V_T2 = 1.32e5 * 1e-2  # 1320
V_L1 = 4.07e5 * 1e-2  # 4070
V_L2 = 1.97e5 * 1e-2  # 1970
tau_B_inv = 6.17e5  # s^-1
A_pt = 57e-44  # s^3
B_T = 3.82e-5  # K^{-m}
B_L1 = 7.5e-22  # s·K^{-m}
B_L2 = 5e-18    # s·K^{-m}

# m(T) values from Table 1
m_T_data = np.array([
    [10, 5.10],
    [20, 3.35],
    [30, 2.45],
    [40, 1.95],
    [60, 1.55],
    [80, 1.5],
    [100, 1.30],
    [150, 1.25],
    [200, 1.25],
    [300, 1.25]
])
m_L1_data = np.array([
    [10, 8.00],
    [20, 4.15],
    [30, 2.8],
    [40, 2.4],
    [60, 1.80],
    [80, 1.6],
    [100, 1.4],
    [150, 1.32],
    [200, 1.32],
    [300, 1.32]
])
m_L2_data = np.array([
    [10, 1.0],
    [20, 1.0],
    [30, 1.0],
    [40, 1.0],
    [60, 1.0],
    [80, 1.0],
    [100, 1.0],
    [150, 1.0],
    [200, 1.0],
    [300, 1.0]
])

def m_T_func(T):
    return np.interp(T, m_T_data[:,0], m_T_data[:,1])

def m_L1_func(T):
    return np.interp(T, m_L1_data[:,0], m_L1_data[:,1])

def m_L2_func(T):
    return np.interp(T, m_L2_data[:,0], m_L2_data[:,1])

def transverse_rate(T, x):
    omega = (k_B * T / hbar) * x
    mT = m_T_func(T)
    tau_ph = B_T * omega * (T ** mT) * np.exp(-Theta / (alpha * T))
    tau_pt = A_pt * (omega ** 4)
    total = tau_B_inv + tau_pt + tau_ph
    return total

def longitudinal_rate(T, x):
    omega = (k_B * T / hbar) * x
    mL1 = m_L1_func(T)
    mL2 = m_L2_func(T)
    tau_ph = (B_L1 * (omega ** 2) * (T ** mL1) + B_L2 * (omega ** 2) * (T ** mL2)) * np.exp(-Theta / (alpha * T))
    tau_pt = A_pt * (omega ** 4)
    total = tau_B_inv + tau_pt + tau_ph
    return total

def integrand(T, x, rate_func):
    if x == 0:
        return 0.0
    rate = rate_func(T, x)
    if rate == 0:
        return 0.0
    numerator = x**4 * np.exp(x)
    denominator = (np.exp(x) - 1)**2 * rate
    return numerator / denominator

def compute_KT(T):
    lower = 0.0
    upper1 = Theta1 / T
    I1, _ = quad(integrand, lower, upper1, args=(T, transverse_rate), limit=200)
    upper2 = Theta2 / T
    I2, _ = quad(integrand, upper1, upper2, args=(T, transverse_rate), limit=200)
    factor = (2.0/3.0) * (k_B / (2.0 * np.pi**2)) * (k_B * T / hbar)**3
    K_T = factor * ( (1.0/V_T1) * I1 + (1.0/V_T2) * I2 )
    return K_T

def compute_KL(T):
    lower = 0.0
    upper1 = Theta4 / T
    I3, _ = quad(integrand, lower, upper1, args=(T, longitudinal_rate), limit=200)
    upper2 = Theta3 / T
    I4, _ = quad(integrand, upper1, upper2, args=(T, longitudinal_rate), limit=200)
    factor = (1.0/3.0) * (k_B / (2.0 * np.pi**2)) * (k_B * T / hbar)**3
    K_L = factor * ( (1.0/V_L1) * I3 + (1.0/V_L2) * I4 )
    return K_L

# Write mT_values.csv
T_vals = [10,20,30,40,60,80,100,150,200,300]
with open('/app/outputs/mT_values.csv', 'w') as f:
    f.write("T,mT_classI,mL1_classI,mL2_classII\n")
    for T in T_vals:
        f.write(f"{T},{m_T_func(T)},{m_L1_func(T)},{m_L2_func(T)}\n")

# Write thermal_conductivity.csv
T_list = [2,5,10,15,20,30,40,50,60,80,100,150,200,250,300]
with open('/app/outputs/thermal_conductivity.csv', 'w') as f:
    f.write("T,K_total,K_transverse,K_longitudinal\n")
    for T in T_list:
        KT = compute_KT(T)
        KL = compute_KL(T)
        Ktotal = KT + KL
        f.write(f"{T},{Ktotal},{KT},{KL}\n")
