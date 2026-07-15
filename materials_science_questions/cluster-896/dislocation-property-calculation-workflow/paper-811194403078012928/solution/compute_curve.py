#!/usr/bin/env python3
import numpy as np
from scipy.optimize import fsolve
import math
import sys

# Material parameters (MPa)
c11 = 168.4e3
c12 = 121.4e3
c44 = 75.4e3
tau0 = 100.0
tau_s = 180.0
h0 = 541.5

# Macroscopic loading
s_mac = np.array([1.0/math.sqrt(2), -1.0/math.sqrt(2), 0.0])
m_mac = np.array([0.0, 0.0, 1.0])

# Laminate interface normal
N_lam = np.array([-1.0/math.sqrt(2), 1.0/math.sqrt(2), 0.0])

# Slip systems A6 and D6 (signed vectors, Schmidt-Boas)
sA = np.array([-1.0, 1.0, 0.0]) / math.sqrt(2)
mA = np.array([1.0, 1.0, -1.0]) / math.sqrt(3)
sD = np.array([1.0, 1.0, 0.0]) / math.sqrt(2)
mD = np.array([-1.0, 1.0, 1.0]) / math.sqrt(3)

# Elastic stiffness tensor (Voigt)
Cv = np.zeros((6,6))
Cv[0,0]=Cv[1,1]=Cv[2,2]=c11
Cv[0,1]=Cv[1,0]=Cv[0,2]=Cv[2,0]=Cv[1,2]=Cv[2,1]=c12
Cv[3,3]=Cv[4,4]=Cv[5,5]=c44

def elastic_stress(Fe):
    Ce = Fe.T @ Fe
    Ee = 0.5*(Ce - np.eye(3))
    e = np.array([Ee[0,0], Ee[1,1], Ee[2,2], 2*Ee[1,2], 2*Ee[2,0], 2*Ee[0,1]])
    Sv = Cv @ e
    S = np.zeros((3,3))
    S[0,0]=Sv[0]; S[1,1]=Sv[1]; S[2,2]=Sv[2]
    S[1,2]=S[2,1]=Sv[3]/2; S[2,0]=S[0,2]=Sv[4]/2; S[0,1]=S[1,0]=Sv[5]/2
    P = Fe @ S
    return P, S, Ce

def resolved_shear(Fe, S, s, m):
    Ce = Fe.T @ Fe
    tau = np.trace((Ce @ S).T @ np.outer(s, m))
    return tau

def hardening_rate(gamma_eff):
    arg = h0 * gamma_eff / (tau_s - tau0)
    if arg > 10.0:
        h = h0 * 4.0 * math.exp(-2.0*arg)
    else:
        h = h0 / (math.cosh(arg)**2)
    return h

def single_slip_update(F, Fp_old, gamma_old, tau_c_old, s, m):
    Fe_trial = F @ np.linalg.inv(Fp_old)
    P_trial, S_trial, Ce_trial = elastic_stress(Fe_trial)
    tau_trial = resolved_shear(Fe_trial, S_trial, s, m)
    if tau_trial <= tau_c_old:
        return Fp_old, gamma_old, tau_c_old, P_trial
    delta_gamma = 0.0
    for _ in range(50):
        Fe = Fe_trial @ (np.eye(3) - delta_gamma * np.outer(s, m))  # exp(-Lp) exact because Lp^2=0
        P, S, Ce = elastic_stress(Fe)
        tau = resolved_shear(Fe, S, s, m)
        gamma_eff = gamma_old + delta_gamma
        h = hardening_rate(gamma_eff)
        tau_c = tau_c_old + h * delta_gamma
        R = tau - tau_c
        if abs(R) < 1e-12:
            break
        ddelta = 1e-6
        Fe_pert = Fe_trial @ (np.eye(3) - (delta_gamma+ddelta)*np.outer(s,m))
        _, S_pert, _ = elastic_stress(Fe_pert)
        tau_pert = resolved_shear(Fe_pert, S_pert, s, m)
        dtau = (tau_pert - tau)/ddelta
        dR = dtau - h
        delta_gamma -= R / dR
        if delta_gamma < 0:
            delta_gamma = 0
    Fp_new = (np.eye(3) + delta_gamma * np.outer(s, m)) @ Fp_old
    gamma_new = gamma_old + delta_gamma
    tau_c_new = tau_c_old + hardening_rate(gamma_old + 0.5*delta_gamma) * delta_gamma
    Fe = F @ np.linalg.inv(Fp_new)
    P, _, _ = elastic_stress(Fe)
    return Fp_new, gamma_new, tau_c_new, P

# Laminate equilibrium callable for fsolve
def laminate_residual(a, F_mac, state1, state2):
    a = np.array(a)
    Fp1, g1, tc1 = state1[0], state1[1], state1[2]
    Fp2, g2, tc2 = state2[0], state2[1], state2[2]
    F1 = F_mac - 0.5 * np.outer(a, N_lam)
    F2 = F_mac + 0.5 * np.outer(a, N_lam)
    Fp1n, g1n, tc1n, P1 = single_slip_update(F1, Fp1, g1, tc1, sA, mA)
    Fp2n, g2n, tc2n, P2 = single_slip_update(F2, Fp2, g2, tc2, sD, mD)
    # Store updated states
    state1[0], state1[1], state1[2] = Fp1n, g1n, tc1n
    state2[0], state2[1], state2[2] = Fp2n, g2n, tc2n
    res = (P1 - P2) @ N_lam
    return res

def main():
    strains = np.linspace(0.0, 0.1, 101)
    results = []
    # Initial homogeneous state (elastic)
    Fp1 = np.eye(3); g1 = 0.0; tc1 = tau0
    Fp2 = np.eye(3); g2 = 0.0; tc2 = tau0
    lam_active = False
    for i, gamma in enumerate(strains):
        F_mac = np.eye(3) + gamma * np.outer(s_mac, m_mac)
        if not lam_active:
            # Uniform deformation (no laminate) – check for yield
            P, _, _ = elastic_stress(F_mac)  # elastic only, no slip yet
            # Check trial resolved shear stress on A6 and D6
            tauA = resolved_shear(F_mac, np.linalg.inv(F_mac).T @ P, sA, mA)  # using simple elastic
            tauD = resolved_shear(F_mac, np.linalg.inv(F_mac).T @ P, sD, mD)
            if tauA >= tau0 or tauD >= tau0:
                lam_active = True
                # initial guess for a = [0,0,0]
                a0 = np.zeros(3)
                # We'll call fsolve with initial state copies
                state1 = [Fp1, g1, tc1]
                state2 = [Fp2, g2, tc2]
                try:
                    sol = fsolve(laminate_residual, a0, args=(F_mac, state1, state2), maxfev=500, xtol=1e-10)
                except Exception as e:
                    print(f'fsolve failed at gamma={gamma}: {e}')
                    sol = a0
                a_sol = sol
                F1 = F_mac - 0.5 * np.outer(a_sol, N_lam)
                F2 = F_mac + 0.5 * np.outer(a_sol, N_lam)
                _, _, _, P1 = single_slip_update(F1, Fp1, g1, tc1, sA, mA)
                _, _, _, P2 = single_slip_update(F2, Fp2, g2, tc2, sD, mD)
                P_mac = 0.5 * (P1 + P2)
                tau = np.tensordot(P_mac, np.outer(s_mac, m_mac))
                results.append((gamma, tau))
                # Update persistent states for next step from state1, state2 (which were updated inside fsolve)
                Fp1, g1, tc1 = state1
                Fp2, g2, tc2 = state2
            else:
                # Elastic, just compute macroscopic stress
                P_mac, _, _ = elastic_stress(F_mac)
                tau = np.tensordot(P_mac, np.outer(s_mac, m_mac))
                results.append((gamma, tau))
        else:
            # Laminate active
            state1 = [Fp1, g1, tc1]
            state2 = [Fp2, g2, tc2]
            a0 = np.zeros(3)
            try:
                sol = fsolve(laminate_residual, a0, args=(F_mac, state1, state2), maxfev=500, xtol=1e-10)
            except Exception as e:
                print(f'fsolve failed at gamma={gamma}: {e}')
                sol = a0
            a_sol = sol
            F1 = F_mac - 0.5 * np.outer(a_sol, N_lam)
            F2 = F_mac + 0.5 * np.outer(a_sol, N_lam)
            _, _, _, P1 = single_slip_update(F1, Fp1, g1, tc1, sA, mA)
            _, _, _, P2 = single_slip_update(F2, Fp2, g2, tc2, sD, mD)
            P_mac = 0.5 * (P1 + P2)
            tau = np.tensordot(P_mac, np.outer(s_mac, m_mac))
            results.append((gamma, tau))
            Fp1, g1, tc1 = state1
            Fp2, g2, tc2 = state2

    # Write CSV
    with open('/app/outputs/stress_strain_curve.csv', 'w') as f:
        f.write('shear_strain,shear_stress\n')
        for gamma, tau in results:
            f.write(f'{gamma:.6f},{tau:.6f}\n')

if __name__ == '__main__':
    main()
