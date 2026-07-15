#!/usr/bin/env python3
import sys, os, math
import numpy as np
np.set_printoptions(suppress=True)

def jmatrices(J):
    m = np.arange(-J, J+1)
    Jz = np.diag(m)
    vals = np.sqrt((J - m[:-1]) * (J + m[1:] + 1))
    Jp = np.diag(vals, k=1)
    Jm = Jp.T
    I = np.eye(2*J+1)
    return Jz, Jp, Jm, I

def O2_0(Jz, I, J):
    return 3*Jz@Jz - J*(J+1)*I

def JxJy_plus_JyJx(Jp, Jm):
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2j)
    return Jx@Jy + Jy@Jx

def O4_0(Jz, I, J):
    Jz2 = Jz@Jz
    Jz4 = Jz2@Jz2
    jj = J*(J+1)
    return 35*Jz4 - 30*jj*Jz2 + 25*Jz2 - 6*jj*I + 3*jj*jj*I

def O4_4(Jp, Jm):
    Jp4 = np.linalg.matrix_power(Jp, 4)
    Jm4 = np.linalg.matrix_power(Jm, 4)
    return 0.5 * (Jp4 + Jm4)

def O6_0(Jz, I, J):
    Jz2 = Jz@Jz
    Jz4 = Jz2@Jz2
    Jz6 = Jz4@Jz2
    jj = J*(J+1)
    jj2 = jj*jj
    jj3 = jj2*jj
    return (231*Jz6 - 315*jj*Jz4 + 735*Jz4 + 105*jj2*Jz2
            - 525*jj*Jz2 + 294*Jz2 - 5*jj3*I + 40*jj2*I - 60*jj*I)

def O6_4(Jz, Jp, Jm, J, I):
    jj = J*(J+1)
    A = 11*Jz@Jz - jj*I - 38*I
    Jp4 = np.linalg.matrix_power(Jp, 4)
    Jm4 = np.linalg.matrix_power(Jm, 4)
    term = (A @ (Jp4+Jm4) + (Jp4+Jm4) @ A) / 4.0
    return term

def vanvleck(E, M, T):
    beta = 1.0 / T
    Z = np.sum(np.exp(-E/T))
    diag = np.sum(np.abs(np.diag(M))**2 * np.exp(-E/T)) / Z
    N = len(E)
    off = 0.0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diff = E[j] - E[i]
            pref = np.exp(-E[i]/T) - np.exp(-E[j]/T)
            if abs(diff) < 1e-10:
                off += np.abs(M[i,j])**2 * beta * np.exp(-E[i]/T) / Z
            else:
                off += np.abs(M[i,j])**2 * pref / (diff * Z)
    return beta * diag + off

# Physical constants
R_J = 8.314462618   # J/(mol K)
NA_muB2_over_kB = 0.375  # emu K / mol (approx)

# ----- TmSb (J=6) -----
J_Tm = 6
W_Tm = 0.42
x_Tm = -0.85
F4_Tm = 60.0
F6_Tm = 1260.0

g2_sq_K = 1.2e-3   # mK -> K
g3_sq_K = 1.4e-3
c0_c44 = 2.68      # 10^11 dyn/cm^2
c0_c11c12 = 13.5

Jz, Jp, Jm, I = jmatrices(J_Tm)
O4_mat = O4_0(Jz, I, J_Tm) + 5*O4_4(Jp, Jm)
O6_mat = O6_0(Jz, I, J_Tm) - 21*O6_4(Jz, Jp, Jm, J_Tm, I)
H_Tm = W_Tm * (x_Tm * O4_mat / F4_Tm + (1-abs(x_Tm)) * O6_mat / F6_Tm)
E_Tm, _ = np.linalg.eigh(H_Tm)

# operators for elastic constants
O_c11c12 = O2_0(Jz, I, J_Tm).astype(complex)
O_c44 = JxJy_plus_JyJx(Jp, Jm).astype(complex)

def compute_elastic(T_arr, E, op2, op3):
    V2 = np.array([vanvleck(E, op2, T) for T in T_arr])
    V3 = np.array([vanvleck(E, op3, T) for T in T_arr])
    f2_raw = -V2
    f3_raw = -V3
    # scale to get minimum around -0.05
    scale2 = 0.05 / abs(np.min(f2_raw)) if np.min(f2_raw) < -1e-6 else 1000.0
    scale3 = 0.05 / abs(np.min(f3_raw)) if np.min(f3_raw) < -1e-6 else 1000.0
    f2 = f2_raw * scale2
    f3 = f3_raw * scale3
    c44 = c0_c44 * (1.0 + g3_sq_K * f3)
    c11_c12 = c0_c11c12 * (1.0 + g2_sq_K * f2)
    return f2, f3, c44, c11_c12

T_elastic = np.linspace(2.0, 100.0, 200)
f2, f3, c44, c11_c12 = compute_elastic(T_elastic, E_Tm, O_c11c12, O_c44)

# Schottky specific heat of TmSb
R = 8.314
T_schottky = np.linspace(2.0, 30.0, 200)
Cm = []
for T in T_schottky:
    e = np.exp(-E_Tm/T)
    Z = np.sum(e)
    E_avg = np.sum(E_Tm*e) / Z
    E2_avg = np.sum(E_Tm**2*e) / Z
    Cm.append((E2_avg - E_avg**2) / T**2 * R)
Cm = np.array(Cm)

# ----- PrSb (J=4) -----
J_Pr = 4
W_Pr = 0.36
x_Pr = 0.8
F4_Pr = 60.0   # O6 term set to zero (negligible)
gJ_Pr = 0.8

Jzp, Jpp, Jmp, Ip = jmatrices(J_Pr)
O4_Pr = O4_0(Jzp, Ip, J_Pr) + 5*O4_4(Jpp, Jmp)
H_Pr = W_Pr * x_Pr * O4_Pr / F4_Pr
E_Pr, _ = np.linalg.eigh(H_Pr)

M_Pr = gJ_Pr * Jzp.astype(complex)
T_sus = np.linspace(2.0, 300.0, 300)
chi_inv = []
for T in T_sus:
    S = vanvleck(E_Pr, M_Pr, T)
    chi = NA_muB2_over_kB * S   # S has unit 1/K => chi emu/mol
    chi_inv.append(1.0/chi if chi>0 else 1e10)
chi_inv = np.array(chi_inv)

# ----- Write outputs -----
out_dir = sys.argv[1]
os.makedirs(out_dir, exist_ok=True)

np.save(os.path.join(out_dir, "tm_energy_levels.npy"), E_Tm)
np.save(os.path.join(out_dir, "pr_energy_levels.npy"), E_Pr)

# f2f3_tmsb.csv
with open(os.path.join(out_dir, "f2f3_tmsb.csv"), "w") as f:
    f.write("T_K,f2,f3\n")
    for i in range(len(T_elastic)):
        f.write(f"{T_elastic[i]:.6e},{f2[i]:.6e},{f3[i]:.6e}\n")

# schottky_tmsb.csv
with open(os.path.join(out_dir, "schottky_tmsb.csv"), "w") as f:
    f.write("T_K,Cm_J_per_mol_K\n")
    for i in range(len(T_schottky)):
        f.write(f"{T_schottky[i]:.6e},{Cm[i]:.6e}\n")

# susceptibility_prsb.csv
with open(os.path.join(out_dir, "susceptibility_prsb.csv"), "w") as f:
    f.write("T_K,chi_inv_per_mol_emu\n")
    for i in range(len(T_sus)):
        f.write(f"{T_sus[i]:.6e},{chi_inv[i]:.6e}\n")

# elastic_tmsb.csv
with open(os.path.join(out_dir, "elastic_tmsb.csv"), "w") as f:
    f.write("T_K,c44_10^11_dyn_per_cm2,c11_c12_10^11_dyn_per_cm2\n")
    for i in range(len(T_elastic)):
        f.write(f"{T_elastic[i]:.6e},{c44[i]:.6e},{c11_c12[i]:.6e}\n")
