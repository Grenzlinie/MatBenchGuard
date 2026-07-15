import json
import numpy as np
import itertools

J = 65.0  # meV

def J_func(qx, qy, qz, Jz):
    return 2*J*(np.cos(qx)+np.cos(qy)) + 2*Jz*np.cos(qz)

def epsilon_nu_func(qx, qy, qz, Gamma_x, Gamma_y, Jz, nu):
    J0 = 4*J + 2*Jz
    Jq = J_func(qx, qy, qz, Jz)
    term = J0**2 - Jq**2 + 4*Gamma_x*(J0 + Gamma_x)
    if nu == -1:
        return np.sqrt(term - 2*Gamma_y*(J0 + Jq + 2*Gamma_x)*np.cos(qy))
    else:
        return np.sqrt(term + 2*Gamma_y*(J0 - Jq + 2*Gamma_x)*np.cos(qy))

def J_nn_func(qx, qy):
    Jprime = -J/3
    Jprime2 = J/4
    return 4*Jprime*np.cos(qx)*np.cos(qy) + 2*Jprime2*(np.cos(2*qx)+np.cos(2*qy))

def epsilon_nu_NNN(qx, qy, qz, Gamma_x, Gamma_y, Jz, nu):
    J0 = 4*J + 2*Jz
    Jq = J_func(qx, qy, qz, Jz)
    Jnn0 = 4*(-J/3) + 2*(J/4)
    Jnn_q = J_nn_func(qx, qy)
    A_q = J0 + 2*Gamma_x - Jnn0 + Jnn_q
    B = Gamma_y * np.cos(qy)
    C = Jq + Gamma_y * np.cos(qy)
    if nu == -1:
        return np.sqrt(A_q**2 + B**2 - C**2 - 2*A_q*B)
    else:
        return np.sqrt(A_q**2 + B**2 - C**2 + 2*A_q*B)

def I_mu_nu(qx, qy, qz, Gamma_x, Gamma_y, Jz, mu, nu, NNN=False):
    if NNN:
        J0 = 4*J + 2*Jz
        Jnn0 = 4*(-J/3) + 2*(J/4)
        Jnn_q = J_nn_func(qx, qy)
        A = J0 + 2*Gamma_x - Jnn0 + Jnn_q
    else:
        A = 4*J + 2*Jz + 2*Gamma_x
    B = Gamma_y * np.cos(qy)
    Jq = J_func(qx, qy, qz, Jz)
    C = Jq + Gamma_y * np.cos(qy)
    if NNN:
        eps = epsilon_nu_NNN(qx, qy, qz, Gamma_x, Gamma_y, Jz, nu)
    else:
        eps = epsilon_nu_func(qx, qy, qz, Gamma_x, Gamma_y, Jz, nu)
    omega = eps
    w = mu*omega
    a_w = w**3 + A*w**2 - (A**2 + B**2 - C**2)*w - A**3 + A*(B**2 + C**2)
    denom = 8*mu*nu*omega*A*B
    if abs(denom) < 1e-12:
        return 0.0
    return a_w / denom

def compute_C(Gamma_x, Gamma_y, Jz, NNN=False, n_grid=(30,30,15)):
    nx, ny, nz = n_grid
    qx_vals = np.linspace(-np.pi, np.pi, nx, endpoint=False)
    qy_vals = np.linspace(-np.pi, np.pi, ny, endpoint=False)
    qz_vals = np.linspace(-np.pi, np.pi, nz, endpoint=False)
    total = 0.0
    for qx in qx_vals:
        for qy in qy_vals:
            for qz in qz_vals:
                s = 0.0
                for nu in [-1,1]:
                    for mu in [-1,1]:
                        if NNN:
                            eps = epsilon_nu_NNN(qx, qy, qz, Gamma_x, Gamma_y, Jz, nu)
                        else:
                            eps = epsilon_nu_func(qx, qy, qz, Gamma_x, Gamma_y, Jz, nu)
                        if eps < 1e-12:
                            continue
                        Ival = I_mu_nu(qx, qy, qz, Gamma_x, Gamma_y, Jz, mu, nu, NNN)
                        s += Ival/(mu*eps)
                total += s
    avg = total / (nx*ny*nz)
    return avg

def gen_dispersion(Gamma_x, Gamma_y, Jz):
    pts = []
    # Gamma (0,0) -> X (pi,0)
    for qx in np.linspace(0, np.pi, 40):
        qy=0.0; qz=0.0
        om = epsilon_nu_func(qx,qy,qz,Gamma_x,Gamma_y,Jz,-1)
        op = epsilon_nu_func(qx,qy,qz,Gamma_x,Gamma_y,Jz,+1)
        pts.append({"q_point":[qx,qy,qz], "omega_minus":float(om), "omega_plus":float(op)})
    # X (pi,0) -> M (pi,pi)
    for qy in np.linspace(0, np.pi, 40):
        qx=np.pi; qz=0.0
        om = epsilon_nu_func(qx,qy,qz,Gamma_x,Gamma_y,Jz,-1)
        op = epsilon_nu_func(qx,qy,qz,Gamma_x,Gamma_y,Jz,+1)
        pts.append({"q_point":[qx,qy,qz], "omega_minus":float(om), "omega_plus":float(op)})
    # M (pi,pi) -> Gamma (0,0)
    for t in np.linspace(0, 1, 40):
        q = np.pi*(1-t); qz=0.0
        om = epsilon_nu_func(q,q,qz,Gamma_x,Gamma_y,Jz,-1)
        op = epsilon_nu_func(q,q,qz,Gamma_x,Gamma_y,Jz,+1)
        pts.append({"q_point":[q,q,qz], "omega_minus":float(om), "omega_plus":float(op)})
    return pts

def grid_iter(n_grid):
    nx, ny, nz = n_grid
    qx_vals = np.linspace(-np.pi, np.pi, nx, endpoint=False)
    qy_vals = np.linspace(-np.pi, np.pi, ny, endpoint=False)
    qz_vals = np.linspace(-np.pi, np.pi, nz, endpoint=False)
    for qx in qx_vals:
        for qy in qy_vals:
            for qz in qz_vals:
                yield qx, qy, qz

def compute_magnetization_curve(Gamma_x, Gamma_y, Jz_val, T_vals, n_grid=(16,16,8)):
    results = []
    sigma = 0.4
    nx, ny, nz = n_grid
    N_mesh = nx*ny*nz
    for T in T_vals:
        for _ in range(15):
            corr_sum = 0.0
            J0 = 4*J + 2*Jz_val
            for qx, qy, qz in grid_iter(n_grid):
                A = sigma * (J0 + 2*Gamma_x)
                B = sigma * Gamma_y * np.cos(qy)
                Jq = J_func(qx, qy, qz, Jz_val)
                C = sigma * (Jq + Gamma_y * np.cos(qy))
                for nu in [-1,1]:
                    disc = A**2 + B**2 - C**2 + 2*nu*A*B
                    if disc < 0:
                        continue
                    omega = np.sqrt(disc)
                    if omega < 1e-12:
                        continue
                    for mu in [-1,1]:
                        w = mu*omega
                        if T < 1e-12:
                            N_bose = 0.0
                        else:
                            if w > 0:
                                N_bose = 1.0/(np.exp(w/T) - 1.0)
                            else:
                                N_bose = -1.0/(np.exp(abs(w)/T) - 1.0) - 1.0
                        a_w = w**3 + A*w**2 - (A**2+B**2-C**2)*w - A**3 + A*(B**2+C**2)
                        denom = 8*mu*nu*omega*A*B
                        if abs(denom) < 1e-12:
                            continue
                        Ival = a_w / denom
                        corr_sum += Ival * N_bose
            avg_corr = corr_sum / N_mesh
            sigma_new = 0.5 - avg_corr
            sigma = 0.7*sigma + 0.3*sigma_new
            if sigma < 0:
                sigma = 0.0
        results.append({"T": T, "sigma": round(sigma, 6)})
    return results

# Parameters
Gamma_x_sym = 0.052*J   # 3.38 meV
Gamma_y_sym = 0.052*J
Jz_sym = 5e-5*J         # ~0.00325 meV

# --- dispersion (symmetric, Jz=0) ---
Gamma_x0 = 0.052*J
Gamma_y0 = 0.052*J
Jz0 = 0.0
dispersion = gen_dispersion(Gamma_x0, Gamma_y0, Jz0)

# --- magnetization curve (symmetric, Jz=5e-5J) ---
T_vals = np.linspace(0, 0.37*J, 7)  # 0, ~6, 12, 18, 24 meV
magn_curve = compute_magnetization_curve(Gamma_x_sym, Gamma_y_sym, Jz_sym, T_vals)

# --- Néel temperatures ---
neel = {}

# symmetric Ba2IrO4
C1 = compute_C(Gamma_x_sym, Gamma_y_sym, Jz_sym, NNN=False, n_grid=(30,30,15))
Tc1_m = 1.0/(4*C1) * J
neel["symmetric_Ba2IrO4"] = {"Tc_meV": round(Tc1_m, 3), "Tc_K": round(Tc1_m*11.605, 1)}

# anisotropic ratios
for r in [0.95, 0.5, 0.1]:
    Gamma_y = r * Gamma_x_sym
    C = compute_C(Gamma_x_sym, Gamma_y, Jz_sym, NNN=False, n_grid=(30,30,15))
    Tc_m = 1.0/(4*C) * J
    neel[f"anisotropic_{r}"] = {"Tc_meV": round(Tc_m, 3), "Tc_K": round(Tc_m*11.605, 1)}

# NNN case (symmetric + Jz=5e-5J)
C_nnn = compute_C(Gamma_x_sym, Gamma_y_sym, Jz_sym, NNN=True, n_grid=(20,20,10))
Tc_nnn_m = 1.0/(4*C_nnn) * J
neel["NNN_symmetric"] = {"Tc_meV": round(Tc_nnn_m, 3), "Tc_K": round(Tc_nnn_m*11.605, 1)}

# write output
data = {
    "dispersion": dispersion,
    "magnetization_curve": magn_curve,
    "neel_temperatures": neel
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
